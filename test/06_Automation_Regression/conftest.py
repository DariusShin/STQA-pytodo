"""Fixtures, markers and result recording for the Week 6 regression suite.

Every session:
  * starts the unchanged app on an isolated, empty SQLite database (or uses
    --base-url to target a server you started yourself);
  * drives a real browser through Selenium WebDriver;
  * writes a run folder under evidences/runs/<stamp>-<browser>/ with the JUnit
    XML, a step log, the server log, failure screenshots and a results table
    that maps every automated check back to its manual test case.
"""

import json
import os
import platform
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

import pytest
import selenium
from selenium import webdriver

from api_client import ApiClient
from pages import PyTodoUI

PHASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = PHASE_DIR.parents[1]
RUN_STARTED = datetime.now()
RUN_STAMP = RUN_STARTED.strftime("%Y%m%d-%H%M%S")
TODAY = date.today()
PASSWORD = "Test12345"  # 9 characters: valid under both the spec and the current implementation
DEFAULT_PORT = 5006     # not 5000, so a developer's own server is never touched

_results = []
_counter = {"n": 0}


# ---------------------------------------------------------------------------
# Command-line options and markers
# ---------------------------------------------------------------------------

def pytest_addoption(parser):
    group = parser.getgroup("week6", "Week 6 regression suite")
    group.addoption("--browser", default="chrome", choices=["chrome", "edge", "firefox"],
                    help="browser driven by Selenium (default: chrome)")
    group.addoption("--headed", action="store_true", help="show the browser window")
    group.addoption("--base-url", default=None,
                    help="use an already-running server instead of starting an isolated one")
    group.addoption("--defects-as-failures", action="store_true",
                    help="report known-defect checks as plain failures instead of xfail")
    group.addoption("--run-label", default=None,
                    help="extra suffix for the run folder name, e.g. smoke or rerun2")


def pytest_configure(config):
    browser = config.getoption("--browser")
    label = config.getoption("--run-label")
    name = f"{RUN_STAMP}-{browser}" + (f"-{label}" if label else "")
    run_dir = PHASE_DIR / "evidences" / "runs" / name
    config.w6_run_dir = run_dir
    if config.option.collectonly or hasattr(config, "workerinput"):
        return
    run_dir.mkdir(parents=True, exist_ok=True)
    # Route the step log and JUnit XML into the run folder unless overridden.
    if not config.option.xmlpath:
        config.option.xmlpath = str(run_dir / "junit.xml")
    if not config.option.log_file:
        config.option.log_file = str(run_dir / "pytest.log")


def pytest_collection_modifyitems(config, items):
    as_failures = config.getoption("--defects-as-failures")
    for item in items:
        item.add_marker(pytest.mark.regression)
        marker = item.get_closest_marker("known_defect")
        if marker and not as_failures:
            # strict: if the defect is fixed the check XPASSes and the run fails,
            # prompting the team to retest/close the defect and drop the marker.
            # raises=AssertionError: any *other* error is still a real failure.
            item.add_marker(pytest.mark.xfail(
                reason=f"known open defect {marker.args[0]}", strict=True, raises=AssertionError))


# ---------------------------------------------------------------------------
# Application server
# ---------------------------------------------------------------------------

def _reachable(base_url):
    try:
        urllib.request.urlopen(f"{base_url}/login", timeout=1)
        return True
    except OSError:
        return False


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    external = pytestconfig.getoption("--base-url")
    if external:
        external = external.rstrip("/")
        if not _reachable(external):
            pytest.exit(f"--base-url {external} is not reachable", returncode=3)
        yield external
        return

    url = f"http://127.0.0.1:{DEFAULT_PORT}"
    if _reachable(url):
        pytest.exit(f"port {DEFAULT_PORT} is already in use; stop that process or pass --base-url",
                    returncode=3)
    db_dir = tempfile.mkdtemp(prefix="w6-pytodo-")
    db_path = os.path.join(db_dir, "regression.db")
    server_log = open(pytestconfig.w6_run_dir / "server.log", "w", encoding="utf-8")
    proc = subprocess.Popen(
        [sys.executable, "-B", str(PHASE_DIR / "run_app.py"), db_path, str(DEFAULT_PORT)],
        cwd=REPO_ROOT, stdout=server_log, stderr=subprocess.STDOUT,
    )
    try:
        for _ in range(150):
            if _reachable(url):
                break
            if proc.poll() is not None:
                raise RuntimeError("run_app.py exited early; see server.log")
            time.sleep(0.2)
        else:
            raise RuntimeError(f"app did not start on {url}")
        yield url
    finally:
        proc.terminate()
        proc.wait(timeout=10)
        server_log.close()


# ---------------------------------------------------------------------------
# Browser
# ---------------------------------------------------------------------------

def _make_driver(name, headed):
    if name == "firefox":
        opts = webdriver.FirefoxOptions()
        if not headed:
            opts.add_argument("-headless")
        driver = webdriver.Firefox(options=opts)
    else:
        opts = webdriver.EdgeOptions() if name == "edge" else webdriver.ChromeOptions()
        if not headed:
            opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1366,900")
        opts.add_argument("--lang=en-US")
        opts.add_experimental_option("prefs", {"intl.accept_languages": "en-US"})
        driver = webdriver.Edge(options=opts) if name == "edge" else webdriver.Chrome(options=opts)
    driver.set_window_size(1366, 900)
    driver.implicitly_wait(0)  # explicit waits only (see pages.py)
    driver.set_page_load_timeout(15)
    return driver


@pytest.fixture(scope="session")
def _session_driver(pytestconfig):
    """One browser per session for speed; cookies are cleared before every test."""
    driver = _make_driver(pytestconfig.getoption("--browser"), pytestconfig.getoption("--headed"))
    caps = driver.capabilities
    pytestconfig.w6_browser_version = f"{caps.get('browserName')} {caps.get('browserVersion')}"
    yield driver
    driver.quit()


@pytest.fixture
def driver(_session_driver, base_url, request):
    _session_driver.get(base_url + "/login")
    _session_driver.delete_all_cookies()
    request.node.w6_driver = _session_driver
    return _session_driver


@pytest.fixture
def ui(driver, base_url):
    return PyTodoUI(driver, base_url)


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

def unique_username(purpose):
    """Unique, rule-compliant username: w6_<purpose>_<HHMMSS><n> (max 20 chars)."""
    _counter["n"] += 1
    name = f"w6_{purpose}_{RUN_STARTED:%H%M%S}{_counter['n']}"
    assert len(name) <= 20, f"generated username too long: {name}"
    return name


def iso_in(days):
    return None if days is None else (TODAY + timedelta(days=days)).isoformat()


@pytest.fixture
def new_account(base_url):
    """Factory: register a fresh account via the API and return its credentials + client."""
    def _create(purpose="acct"):
        username = unique_username(purpose)
        api = ApiClient(base_url)
        api.register(username, PASSWORD)
        return {"username": username, "password": PASSWORD, "api": api}
    return _create


@pytest.fixture
def logged_in(ui, new_account):
    """A fresh account that is logged in through the UI."""
    account = new_account("ui")
    ui.login(account["username"], account["password"])
    assert ui.path == "/", "precondition: login failed"
    return account


# ---------------------------------------------------------------------------
# Result recording (manual-to-automated traceability)
# ---------------------------------------------------------------------------

def _marker_args(item, name):
    return [a for m in item.iter_markers(name) for a in m.args]


def _status(report):
    if hasattr(report, "wasxfail"):
        return "Fail (known defect)" if report.skipped else "Retest (XPASS - defect may be fixed)"
    if report.failed and str(report.longrepr).startswith("[XPASS(strict)]"):
        return "Retest (XPASS - defect may be fixed)"
    if report.passed:
        return "Pass"
    if report.skipped:
        return "Not Run"
    return "Blocked" if report.when == "setup" else "Fail"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "setup" and report.passed:
        return
    if report.when == "teardown" and not report.failed:
        return
    screenshot = None
    drv = getattr(item, "w6_driver", None)
    if drv is not None and report.when == "call" and (report.failed or hasattr(report, "wasxfail")):
        shots = item.config.w6_run_dir / "screenshots"
        shots.mkdir(exist_ok=True)
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in item.name)[:90]
        path = shots / f"{safe}.png"
        try:
            drv.save_screenshot(str(path))
            screenshot = path.relative_to(item.config.w6_run_dir).as_posix()
        except Exception:  # browser may already be gone
            pass
    message = None
    if report.failed or hasattr(report, "wasxfail"):
        lines = str(report.longrepr).strip().splitlines()
        errs = [ln for ln in lines if ln.startswith("E ")]
        message = (errs[0][1:].strip() if errs else lines[-1])[:300] if lines else None
    _results.append({
        "auto_id": (_marker_args(item, "auto") or ["-"])[0],
        "nodeid": item.nodeid,
        "manual": _marker_args(item, "manual"),
        "req": _marker_args(item, "req"),
        "defect": _marker_args(item, "known_defect"),
        "smoke": item.get_closest_marker("smoke") is not None,
        "status": _status(report),
        "duration_s": round(report.duration, 2),
        "message": message,
        "screenshot": screenshot,
    })


def pytest_sessionfinish(session, exitstatus):
    if not _results or hasattr(session.config, "workerinput"):
        return
    config = session.config
    run_dir = config.w6_run_dir
    finished = datetime.now()
    counts = {}
    for r in _results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO_ROOT,
                                capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        commit = "unknown"
    meta = {
        "run_started": RUN_STARTED.isoformat(timespec="seconds"),
        "run_finished": finished.isoformat(timespec="seconds"),
        "wall_time_s": round((finished - RUN_STARTED).total_seconds(), 1),
        "timezone": time.strftime("%Z"),
        "execution_date_used_for_due_dates": TODAY.isoformat(),
        "app_commit": commit,
        "browser": getattr(config, "w6_browser_version", "none (no browser check selected)"),
        "headless": not config.getoption("--headed"),
        "selenium": selenium.__version__,
        "pytest": pytest.__version__,
        "python": platform.python_version(),
        "os": f"{platform.system()} {platform.release()} ({platform.version()})",
        "target": config.getoption("--base-url") or f"isolated server on port {DEFAULT_PORT}",
        "run_label": config.getoption("--run-label") or "-",
        "marker_expression": config.getoption("markexpr") or "(all)",
        "defects_as_failures": config.getoption("--defects-as-failures"),
        "pytest_exit_status": int(exitstatus),
        "counts": counts,
    }
    (run_dir / "results.json").write_text(
        json.dumps({"meta": meta, "results": _results}, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [f"# Regression run {RUN_STAMP}", "", "| Item | Value |", "| --- | --- |"]
    lines += [f"| {k} | {v} |" for k, v in meta.items()]
    lines += ["", "| Auto ID | Manual case(s) | Requirement | Known defect | Smoke | Status | Time (s) | Note |",
              "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in _results:
        note = (r["message"] or "").replace("|", "\\|")
        if r["screenshot"]:
            note += f" [screenshot]({r['screenshot']})"
        lines.append(
            f"| {r['auto_id']} | {', '.join(r['manual']) or '-'} | {', '.join(r['req']) or '-'} | "
            f"{', '.join(r['defect']) or '-'} | {'Y' if r['smoke'] else ''} | {r['status']} | "
            f"{r['duration_s']} | {note.strip()} |")
    (run_dir / "results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
