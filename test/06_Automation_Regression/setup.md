# Week 6 — Environment setup and execution guide

This guide accompanies the [Week 6 report](README.md). The regression suite is
written in **pytest + Selenium WebDriver**. It needs no change to the
application and does not touch the development database.

## Verified environment

| Component | Verified version |
| --- | --- |
| OS | Windows 11 Home 10.0.26200 |
| Python | 3.14.7 |
| pytest | 9.2.0 |
| Selenium (Python) | 4.53.0, with Selenium Manager resolving the driver |
| Browser | Microsoft Edge 157.0.4341.60, headless, 1366x900 window |
| Flask / Werkzeug | 3.0.3 / 3.1.9 |

All dependencies are pinned in [requirements-test-lock.txt](requirements-test-lock.txt).

## 1. Create the environment

Run these from `test/06_Automation_Regression/`.

```bash
python -m venv .venv
source .venv/bin/activate              # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install --no-cache-dir -r requirements-test-lock.txt
python -m pip check
```

You do not need to install a browser driver. On the first run, Selenium Manager
downloads the driver that matches your installed Chrome, Edge or Firefox, so that
first run needs network access.

## 2. Run the suites

Run every command from `test/06_Automation_Regression/` so that pytest picks up
this folder's `pytest.ini`. Use `python -B` so that importing `app.py` and
`helpers.py` does not write `__pycache__` folders into the application root.

| Purpose | Command | Typical time |
| --- | --- | --- |
| Smoke (critical path, run on every change) | `python -B -m pytest -m smoke --browser chrome` | about 14 s |
| Full focused regression suite | `python -B -m pytest --browser chrome` | about 37 s |
| Business rules only (no browser or server) | `python -B -m pytest -m unit` | under 1 s |
| Known defects counted as failures | `python -B -m pytest --browser chrome --defects-as-failures` | about 35 s |

- `--browser` takes `chrome` (the default), `edge` or `firefox`.
- `--headed` shows the browser window. Runs are headless by default.
- `--base-url http://127.0.0.1:5000` runs the suite against a server you started yourself instead of an isolated one. That server's database will then receive the test accounts.
- `--run-label <text>` adds a suffix to the run folder name, for example `rerun2`.

## 3. How a run is isolated

1. `conftest.py` starts [run_app.py](run_app.py) on port **5006**. That script imports the unchanged `app.py`, points its `DATABASE` setting at a new temporary SQLite file and calls `init_db()`. Every run therefore starts with an empty database that has only the four default categories.
2. Each test registers a new account through the API, named `w6_<purpose>_<HHMMSS><n>`, and seeds that account's tasks through the API. The UI steps then cover only the behaviour being checked.
3. One browser is used for the whole session. Its cookies are cleared before each test, so no login state carries over from one test to the next.
4. Due dates are calculated as offsets from the day of the run, so the urgency and dashboard data remain valid on any date.

## 4. Outputs

Each run writes a folder `evidences/runs/<YYYYMMDD-HHMMSS>-<browser>[-label]/` containing:

| File | Content |
| --- | --- |
| `results.md` / `results.json` | Environment, totals, and one row per check: auto ID, manual case(s), requirement, known defect, status, duration, failure message, screenshot |
| `junit.xml` | Standard JUnit XML for CI tools |
| `pytest.log` | Timestamped log of each UI and API step |
| `server.log` | Request log of the isolated application server |
| `screenshots/` | A PNG for every failed check and every known-defect check |

## 5. Reading the result

| pytest outcome | Course status | Meaning |
| --- | --- | --- |
| passed | Pass | The behaviour matches the specification. |
| xfailed | Fail (known defect) | The check failed with an `AssertionError` linked to an open `DEF-` record. The assertion still describes the *specified* behaviour. |
| XPASS(strict), shown as failed | Retest | A check for a known defect now passes. Retest the defect and close it if it is fixed, then remove the `known_defect` marker. |
| failed | Fail | A new regression, or a new defect to log. |
| error during setup | Blocked | An environment, data-seeding or driver problem. |

Exit code 0 means no unexpected result. Exit code 1 means at least one check is a new failure or a strict XPASS.
