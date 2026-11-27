# 06_Automation_Regression - Test Automation and Regression

Week 6 selects the earlier manual cases worth automating, automates them with pytest, Selenium WebDriver and HTTP checks, and organises them into a focused regression suite with smoke, rules, Web/API and full tiers.

| File / folder | Contents |
| --- | --- |
| [W6_Report.md](W6_Report.md) | Week 6 report: candidate selection, scripts, traceability summary, execution runs, seeded-fault check, regression suite and reflection |
| [test_cases.md](test_cases.md) | TC-AUT-001 to 089 traced to their manual cases, with results |
| `test_01_auth.py` ... `test_05_rules_unit.py` | Browser and rule checks for Week 1 and Week 3 cases |
| `test_06_api.py`, `test_07_web_forms.py` | HTTP checks for the Week 4 cases |
| `conftest.py`, `pytest.ini`, `run_app.py`, `pages.py`, `api_client.py`, `api_checks.py` | Harness: options, isolated server, page helpers, HTTP client, assertions |
| `requirements-test-lock.txt` | Exact package versions |
| [evidences/runs/](evidences/runs/) | One folder per run: `results.md/json`, `junit.xml`, `pytest.log`, `server.log`, `screenshots/` |
| [evidences/mutation/](evidences/mutation/) | Seeded-fault runs M1 to M12 and the script that created them |

No new defects were found in Week 6, so there is no `defects.md`; re-tested defects are listed in [W6_Report.md section 4.2](W6_Report.md#42-known-defects-re-tested-by-the-suite).

## How to run

From `test/06_Automation_Regression/` (so this folder's `pytest.ini` is used). No browser driver install is needed: Selenium Manager downloads it on the first run, which needs network access.

```bash
python -m venv .venv
source .venv/bin/activate              # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-test-lock.txt
```

| Purpose | Command | Time |
| --- | --- | --- |
| Smoke | `python -B -m pytest -m smoke --browser chrome` | ~14 s |
| Web/API checks (no browser) | `python -B -m pytest -m api` | ~21 s |
| Rules only (no browser or server) | `python -B -m pytest -m unit` | < 1 s |
| Full regression | `python -B -m pytest --browser chrome` | ~85 s |
| Known defects counted as failures | `python -B -m pytest --browser chrome --defects-as-failures` | ~85 s |

- `--browser` takes `chrome` (default), `edge` or `firefox`; `--headed` shows the window; `--base-url http://127.0.0.1:5000` targets a server you started yourself; `--run-label <text>` names the run folder.
- Each run starts the unchanged `app.py` on port 5006 with a new temporary database and writes `evidences/runs/<YYYYMMDD-HHMMSS>-<browser>[-label]/`.
- `python -B` stops imports of `app.py` from writing `__pycache__` into the application root.

**Reading a result:** passed = Pass; xfailed = Fail (known defect, the assertion still states the specified behaviour); XPASS(strict), shown as failed = Retest (a known defect now passes); failed = new regression or defect; setup error = Blocked. Exit code 0 means no unexpected result.
