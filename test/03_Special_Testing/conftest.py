"""Shared Playwright fixtures for the Week 3 special-testing suites.

Test data comes from fixtures.json (described in fixtures.md). The suites run
against the real `python app.py` server and the existing development database;
every run registers its own uniquely named accounts, so earlier data is never
modified.
"""

import json
import os
import signal
import subprocess
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

import pytest

PHASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = PHASE_DIR.parents[1]
DATA = json.loads((PHASE_DIR / "fixtures.json").read_text(encoding="utf-8"))
RUN_DATE = date.today()
RUN_STAMP = datetime.now().strftime("%m%d%H%M%S")
BASE_URL = DATA["base_url"]

_results = {}


def pytest_addoption(parser):
    parser.addoption(
        "--w3-config",
        default="C01",
        choices=sorted(DATA["configurations"]),
        help="Week 3 configuration ID from README 2.1 (default: C01)",
    )


def pytest_configure(config):
    config.w3_config_id = config.getoption("--w3-config")


# ---------------------------------------------------------------------------
# Configuration and browser settings
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def w3_config(pytestconfig):
    config_id = pytestconfig.w3_config_id
    return {"id": config_id, **DATA["configurations"][config_id]}


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args, w3_config):
    channel = w3_config.get("channel")
    return {**browser_type_launch_args, **({"channel": channel} if channel else {})}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, w3_config):
    args = {**browser_context_args, "base_url": BASE_URL, "viewport": w3_config["viewport"]}
    for key in ("is_mobile", "has_touch", "device_scale_factor"):
        if key in w3_config:
            args[key] = w3_config[key]
    return args


# ---------------------------------------------------------------------------
# Application server
# ---------------------------------------------------------------------------

def _reachable():
    try:
        urllib.request.urlopen(f"{BASE_URL}/login", timeout=1)
        return True
    except OSError:
        return False


@pytest.fixture(scope="session", autouse=True)
def app_server():
    """Reuse a running `python app.py`, or start one for the session (P-APP)."""
    if _reachable():
        yield BASE_URL
        return
    kwargs = {"cwd": REPO_ROOT, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    if os.name == "nt":
        kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        kwargs["start_new_session"] = True
    proc = subprocess.Popen([sys.executable, "app.py"], **kwargs)
    try:
        for _ in range(100):
            if _reachable():
                break
            time.sleep(0.2)
        else:
            raise RuntimeError("app.py did not start on " + BASE_URL)
        yield BASE_URL
    finally:
        # app.run(debug=True) starts a reloader child, so stop the whole group.
        if os.name == "nt":
            proc.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            os.killpg(proc.pid, signal.SIGTERM)
        proc.wait(timeout=10)


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

def username_for(purpose):
    name = f"w3{DATA['tester_initial']}_{purpose}_{RUN_STAMP}"
    assert len(name) <= 20, f"username too long for the registration rule: {name}"
    return name


def iso_in(days):
    return None if days is None else (RUN_DATE + timedelta(days=days)).isoformat()


def _register_and_seed(playwright, purpose, fixture_set):
    api = playwright.request.new_context(base_url=BASE_URL)
    try:
        username = username_for(purpose)
        resp = api.post("/api/register", data={"username": username, "password": DATA["password"]})
        assert resp.status == 201, f"seeding failed to register {username}: {resp.status}"
        categories = {c["name"]: c["id"] for c in api.get("/api/categories").json()}
        tasks = {}
        for item in DATA.get(f"fixture_set_{fixture_set}", []) if fixture_set else []:
            payload = {
                "title": item["title"],
                "description": item["description"],
                "category_id": categories.get(item["category"]),
                "due_date": iso_in(item["due_offset_days"]),
            }
            created = api.post("/api/tasks", data=payload)
            assert created.status == 201, f"seeding failed for {item['id']}: {created.status}"
            task = created.json()
            if item["done"]:
                task = api.put(f"/api/tasks/{task['id']}", data={"done": True}).json()
            tasks[item["id"]] = {**item, "task_id": task["id"], "due_date": payload["due_date"]}
        return {"username": username, "password": DATA["password"], "tasks": tasks}
    finally:
        api.dispose()


@pytest.fixture(scope="session")
def account_a(playwright, app_server):
    """Account A with Fixture Set A (precondition P-A)."""
    return _register_and_seed(playwright, DATA["accounts"]["A"]["purpose"], "A")


@pytest.fixture(scope="session")
def account_c(playwright, app_server):
    """Account C with no tasks (precondition P-C)."""
    return _register_and_seed(playwright, DATA["accounts"]["C"]["purpose"], None)


@pytest.fixture(scope="session")
def api_as(playwright, app_server):
    """Return an API request context logged in as the given account (setup/cleanup only)."""
    contexts = []

    def _open(account):
        api = playwright.request.new_context(base_url=BASE_URL)
        api.post("/api/login", data={"username": account["username"], "password": account["password"]})
        contexts.append(api)
        return api

    yield _open
    for api in contexts:
        api.dispose()


def case_data(case_id):
    return DATA["cases"].get(case_id, {})


# ---------------------------------------------------------------------------
# Page helpers
# ---------------------------------------------------------------------------

def login(page, account):
    page.goto("/login")
    page.fill("input[name=username]", account["username"])
    page.fill("input[name=password]", account["password"])
    with page.expect_navigation():
        page.click("button[type=submit]")


def row_for(page, title_prefix):
    return page.locator("table.task-table tbody tr", has=page.locator("td.title-cell", has_text=title_prefix))


def listed_titles(page):
    return [t.strip() for t in page.locator("table.task-table td.title-cell").all_inner_texts()]


def create_task_ui(page, title, category=None, due_date=None):
    page.goto("/tasks/new")
    page.fill("input[name=title]", title)
    if category:
        page.select_option("select[name=category_id]", label=category)
    if due_date:
        page.fill("input[name=due_date]", due_date)
    with page.expect_navigation():
        page.click("form.task-form button[type=submit]")


def text_lines(locator):
    """Number of rendered text lines inside an element."""
    return locator.evaluate(
        """el => { const r = document.createRange(); r.selectNodeContents(el);
                   return new Set([...r.getClientRects()].map(x => Math.round(x.top))).size; }"""
    )


def boxes_overlap(a, b):
    return not (a["x"] + a["width"] <= b["x"] or b["x"] + b["width"] <= a["x"]
                or a["y"] + a["height"] <= b["y"] or b["y"] + b["height"] <= a["y"])


def nav_layout(page):
    """Line count and overlap of each navigation-bar item (H10)."""
    items = page.locator("nav.topnav .brand, nav.topnav .nav-links > *")
    layout = []
    for i in range(items.count()):
        item = items.nth(i)
        layout.append({"text": item.inner_text().strip(), "lines": text_lines(item), "box": item.bounding_box()})
    overlaps = [(a["text"], b["text"]) for i, a in enumerate(layout) for b in layout[i + 1:]
                if boxes_overlap(a["box"], b["box"])]
    return layout, overlaps


def has_horizontal_scroll(page):
    return page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")


def computed(locator, *props):
    return locator.evaluate("(el, props) => Object.fromEntries(props.map(p => [p, getComputedStyle(el)[p]]))",
                            list(props))


# ---------------------------------------------------------------------------
# Evidence and result recording
# ---------------------------------------------------------------------------

class Recorder:
    """Collects checks and observations for one test case.

    Each `expect` is one check derived from the case's expected result. All
    checks run before the test fails, so the recorded actual result lists every
    mismatch, not only the first.
    """

    def __init__(self, case_id, evidence_dir, full_page=True):
        self.case_id = case_id
        self.evidence_dir = evidence_dir
        self.full_page = full_page
        self.checks = []
        self.notes = []
        self.evidence = []

    def expect(self, passed, description, actual=None):
        self.checks.append({"check": description, "passed": bool(passed), "actual": actual})
        return passed

    def note(self, text):
        self.notes.append(text)

    def capture(self, page, desc=None, full_page=None):
        full_page = self.full_page if full_page is None else full_page
        name = "-".join(p for p in (self.case_id, desc, RUN_DATE.strftime("%Y%m%d")) if p)
        path = self.evidence_dir / f"{name}.jpg"
        path.parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(path), type="jpeg", quality=85, full_page=full_page)
        self.evidence.append(path.relative_to(PHASE_DIR).as_posix())
        return path

    def assert_all(self):
        failed = [c for c in self.checks if not c["passed"]]
        assert not failed, "; ".join(f"{c['check']} (actual: {c['actual']})" for c in failed)


@pytest.fixture
def rec(request, w3_config):
    case_id = request.node.get_closest_marker("case").args[0]
    suite_dir = request.node.path.parent
    evidence_dir = suite_dir / "evidences"
    if suite_dir.name == "2_Compatibility":
        evidence_dir = evidence_dir / w3_config["folder"]
    # On emulated mobile devices a full-page capture renders the whole layout viewport, not what
    # the device screen shows, so those configurations capture the screen instead.
    recorder = Recorder(case_id, evidence_dir, full_page=not w3_config.get("is_mobile", False))
    request.node.w3_recorder = recorder
    return recorder


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    recorder = getattr(item, "w3_recorder", None)
    if recorder is None or report.when not in ("setup", "call"):
        return
    if report.when == "setup" and report.passed:
        return
    status = {"passed": "Pass", "failed": "Fail", "skipped": "Not Run"}[report.outcome]
    if report.when == "setup" and report.failed:
        status = "Blocked"
    _results[recorder.case_id] = {
        "status": status,
        "checks": recorder.checks,
        "notes": recorder.notes,
        "evidence": recorder.evidence,
        "error": None if report.passed else str(report.longrepr).splitlines()[-1][:500],
        "suite": item.path.parent.name,
        "evidence_dir": recorder.evidence_dir,
    }


def pytest_sessionfinish(session):
    if not _results:
        return
    config_id = session.config.w3_config_id
    by_dir = {}
    for case_id, result in _results.items():
        by_dir.setdefault(result.pop("evidence_dir"), {})[case_id] = result
    for evidence_dir, cases in by_dir.items():
        evidence_dir.mkdir(parents=True, exist_ok=True)
        out = evidence_dir / f"results-{config_id}-{RUN_DATE:%Y%m%d}-{RUN_STAMP[-6:]}.json"
        out.write_text(json.dumps({
            "configuration": config_id,
            "run_started": RUN_STAMP,
            "run_date": RUN_DATE.isoformat(),
            "cases": dict(sorted(cases.items())),
        }, indent=2, ensure_ascii=False), encoding="utf-8")
