# Week 6 - Test Automation and Regression

| Item | Value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance, September 2026 |
| Lab group | Wednesday Lab - Group 2 |
| Phase owner | Eu Kwan Ik |
| Execution dates | 2026-11-20: browser and rule checks (runs 1-6), seeded faults M1-M7<br>2026-11-27: Week 4 Web/API checks added (runs 7-10), seeded faults M8-M12 |
| Environment | Windows 11 Home 10.0.26200; Python 3.14.7; pytest 9.2.0; Selenium WebDriver 4.53.0; Microsoft Edge 157.0.4341.60 (2026-11-20) and 158.0.4370.45 (2026-11-27), headless, 1366x900; Flask 3.0.3 / Werkzeug 3.1.9 |
| Target | Unchanged `app.py` on port 5006 with a new temporary SQLite database for each run |

## Deliverable checklist

- [x] [Automation candidate justification](#1-automation-candidate-justification)
- [x] [Automated scripts](#2-automated-scripts) - 7 test modules, 166 checks
- [x] [Manual-to-automated traceability](#3-manual-to-automated-traceability) - TC-AUT-001 to 089 in [test_cases.md](test_cases.md)
- [x] [Execution report/logs](#4-execution-report-and-logs) - 10 runs and 12 seeded-fault runs in [evidences/](evidences/)
- [x] [Regression suite and automation reflection](#5-regression-suite-and-automation-reflection)

## 1. Automation candidate justification

### 1.1 Manual tests reviewed

| Phase | Cases | Recorded outcome |
| --- | --- | --- |
| Week 1 black-box | TC-BB-001 to 044 | 40 Pass, 4 Fail (DEF-001, 002, 003) |
| Week 2 white-box | pytest unit and integration tests | Already automated |
| Week 3 GUI | TC-GUI-001 to 022 | Includes DEF-004, DEF-005 |
| Week 3 compatibility | TC-CMP-001 to 008 | Already scripted with Playwright |
| Week 3 usability | USA-OBS-001 to 004 | Human session |
| Week 3 accessibility | TC-A11Y-001 to 018 | DEF-007 to DEF-013 |
| Week 4 Web/API | TC-WEB-001 to 016, TC-API-001 to 045 | 43 Pass, 18 Fail (DEF-001 to 003, DEF-014 to 023) |

### 1.2 Selection criteria

Each group of cases was scored 1 (low) to 3 (high) on the four criteria in the brief:

| Criterion | 3 means | 1 means |
| --- | --- | --- |
| **Repetition (R)** | Needed after every change, or once per data value (BVA/EP rows) | Run once or rarely |
| **Stability (S)** | Exact, deterministic expected result; stable page and locators | Needs human judgement, depends on visuals, or varies between runs |
| **Criticality (C)** | A failure blocks a core user goal (account, access, task data) | A failure is cosmetic |
| **Regression value (V)** | Likely to break when code changes, or guards a known defect | Unlikely to break, or a break would be obvious |

**Rule:** automate when the total is at least 9 of 12 **and** a program can check the expected result without human judgement. Groups scoring 7-8 are automated only for the part with an exact oracle.

### 1.3 Candidate decisions

| Manual cases | What they check | R | S | C | V | Total | Decision and justification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BB-001 to 011 | Username/password BVA and EP | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** Eleven rows of one procedure suit `parametrize`. Guards DEF-001. |
| TC-BB-012, 013, 022 | Native `required` validation | 2 | 3 | 2 | 2 | 9 | **Automate the exact part:** assert the DOM validity state (`valueMissing`), not the browser's message wording. |
| TC-BB-014 to 017 | Login decision table | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** |
| TC-BB-018, 019 | Access control and logout | 3 | 3 | 3 | 3 | 12 | **Automate.** Extended to `/dashboard` and `/tasks/new`. |
| TC-BB-020, 021, 024 to 027 | Create, edit, cancel, delete | 3 | 3 | 3 | 3 | 12 | **Automate.** Core workflow; Selenium's alert API answers the delete dialog. |
| TC-BB-023 | Whitespace-only title | 2 | 3 | 2 | 3 | 10 | **Automate.** Guards DEF-003; the API task count is the oracle. |
| TC-BB-028, 029, 042 | Complete/reopen state | 3 | 3 | 3 | 3 | 12 | **Automate** as one state-transition sequence. |
| TC-BB-030 to 035 | Filters and search | 3 | 3 | 2 | 3 | 11 | **Automate (data-driven)** with fixtures F1-F4 in a fresh account. |
| TC-BB-036 to 041 | Urgency labels | 3 | 2 | 3 | 3 | 11 | **Automate.** Date dependence handled with date-relative data and a date-injected unit layer. Guards DEF-002. |
| TC-BB-043 | Dashboard counters | 3 | 2 | 2 | 3 | 10 | **Automate, split in two** so the DEF-002 counter is isolated. |
| TC-BB-044 | Account task separation | 3 | 3 | 3 | 3 | 12 | **Automate.** Data-isolation risk. |
| TC-GUI-004, 008, 010, 011, 012, 013, 015, 016 | Functional assertions inside GUI cases | 3 | 3 | 2 | 3 | 11 | **Automate the functional part**; visual parts stay manual. |
| TC-GUI-020 | Special characters | 2 | 3 | 2 | 3 | 10 | **Automate.** Exact text oracle; guards DEF-005. |
| TC-GUI-002 | Login error message | 2 | 3 | 2 | 2 | 9 | **Partly covered** by TC-AUT-006 (exact text); style not checked. |
| TC-GUI-001, 003, 006, 007, 009, 014, 021 | Static layout, labels, titles | 1 | 2 | 1 | 2 | 6 | **Do not automate.** Rarely change; a break would be obvious. |
| TC-GUI-005, 017, 018, 019, 022 | Visual layout and heuristics | 1 | 1 | 1 | 2 | 5 | **Do not automate.** Need visual judgement; checks would be brittle. |
| TC-CMP-001 to 008 | Cross-configuration smoke | 2 | 2 | 2 | 2 | 8 | **Out of scope** for the focused suite; already scripted in Week 3. The suite can still run with `--browser chrome/edge/firefox`. |
| Usability observations | Human session | 1 | 1 | 2 | 1 | 5 | **Not automatable.** |
| TC-A11Y-001 to 018 | Accessibility | 1 | 2 | 2 | 2 | 7 | **Not in this suite.** The Week 3 axe/Lighthouse scans are the right tool; keyboard checks need a human. |
| TC-API-024, 033, 037, 040, 044; TC-WEB-013 | One user cannot read, list, change or delete another's task | 3 | 3 | 3 | 3 | 12 | **Automate.** Guards DEF-014 (Critical). |
| TC-API-011, 012; TC-WEB-004 | Protected endpoints and pages refuse a logged-out caller | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** Guards DEF-023. |
| TC-API-001 to 010; TC-WEB-001 to 003, 016 | Registration and login partitions, wrong types, duplicates | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** Guards DEF-001, 016, 018. |
| TC-API-014 to 020, 036; TC-WEB-010 to 012 | Input validation; nothing saved after a rejection | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** Guards DEF-003, 015, 018, 019, 020. |
| TC-API-021, 042, 043 | Urgency boundaries and dashboard counts | 3 | 2 | 3 | 3 | 11 | **Automate** with run-day offsets. Guards DEF-002. |
| TC-API-022, 023, 025, 034, 035, 038, 039, 041, 045 | Round trips and API error contract | 3 | 3 | 2 | 3 | 11 | **Automate.** Guards DEF-021. |
| TC-API-026 to 032 | Filters, search, paging | 3 | 3 | 2 | 3 | 11 | **Automate.** Guards DEF-017, 022. |
| TC-WEB-005 to 009, 014, 015 | Web pages and API agree | 3 | 3 | 2 | 3 | 11 | **Automate**, each side as the other's oracle. |

**Outcome.** 115 manual cases (all 44 Week 1, the functional parts of 10 Week 3 GUI cases, all 61 Week 4) are automated in **89 automated cases and 166 checks**: 48 browser checks, 17 rule-level checks and 101 HTTP checks. Visual GUI cases, usability, accessibility and compatibility stay with their Week 3 methods.

### 1.4 Design decisions

| Decision | Reason |
| --- | --- |
| **Selenium WebDriver** for UI checks | The approved tool; drives a real browser through the W3C WebDriver protocol. |
| **HTTP checks without a browser** for the Week 4 cases (marker `api`) | Week 4 tested status codes, bodies and form submissions, not rendering; a browser would only add time and flakiness. |
| **Preconditions seeded through the JSON API** | Each check covers only its own behaviour and runs fast; UI creation has its own checks. |
| **API as an independent oracle** where a page could hide a problem | e.g. TC-AUT-012 counts tasks through the API. |
| **Isolated server on a temporary database; fresh accounts per check** | Every run starts from a known state; no check can affect another (DEF-015 no longer forces an order as in Postman). |
| **Data-driven tests** (`parametrize`) | One procedure per BVA/EP/decision-table row; the row ID is the manual case ID. |
| **Known defects as strict, narrow xfail** | The assertion keeps the *specified* result; `strict=True` turns a fixed defect into a visible XPASS (Retest); `raises=AssertionError` keeps other errors as failures. |
| **Redirects not followed; HTML 500 pages not parsed as JSON** | A 302 and its target are asserted directly; a 500 is reported with its observed status. |
| **Page helpers in `pages.py`; explicit waits only** | Locators in one place; no sleeps. |

## 2. Automated scripts

| Script | Automated cases | Description |
| --- | --- | --- |
| [conftest.py](conftest.py) | - | Options (`--browser`, `--headed`, `--base-url`, `--defects-as-failures`, `--run-label`); starts the isolated server and browser; account fixtures; turns `known_defect` markers into xfail; writes `results.md/json` and failure screenshots |
| [run_app.py](run_app.py) | - | Imports the unchanged `app.py`, points `DATABASE` at a temporary file, serves on port 5006 |
| [pages.py](pages.py) | - | `PyTodoUI` page helpers: register, login, logout, task form, rows, toggle, edit, delete (handles `confirm()`), filters, dashboard counters, validation state |
| [api_client.py](api_client.py) | - | Standard-library HTTP client: one client = one cookie jar; JSON or form bodies; redirects not followed |
| [api_checks.py](api_checks.py) | - | Week 4 assertions and HTML readers for the task table, error message and dashboard counters |
| [test_01_auth.py](test_01_auth.py) | TC-AUT-001 to 008 | Registration BVA/EP, required fields, login decision table, access control, logout |
| [test_02_tasks.py](test_02_tasks.py) | TC-AUT-009 to 020 | Create, edit, cancel, delete, complete/reopen, special characters, account separation |
| [test_03_filters.py](test_03_filters.py) | TC-AUT-021 | Category, status, search and combined filters |
| [test_04_urgency_dashboard.py](test_04_urgency_dashboard.py) | TC-AUT-022 to 025 | Urgency labels, completed-overrides-overdue, dashboard counters |
| [test_05_rules_unit.py](test_05_rules_unit.py) | TC-AUT-026 to 028 | Username, password and urgency rules on `helpers.py` with an injected date |
| [test_06_api.py](test_06_api.py) | TC-AUT-029 to 073 | Week 4 TC-API-001 to 045 |
| [test_07_web_forms.py](test_07_web_forms.py) | TC-AUT-074 to 089 | Week 4 TC-WEB-001 to 016 |

Markers tie each check to the documentation:

```python
@pytest.mark.auto("TC-AUT-002")          # automated case ID
@pytest.mark.req("REQ-001")               # requirement
@pytest.mark.parametrize("password, accepted", [
    pytest.param("Test123",   False, marks=pytest.mark.manual("TC-BB-007"), id="TC-BB-007-len7"),
    pytest.param("Test1234",  True,  marks=[pytest.mark.manual("TC-BB-008", "TC-GUI-004"),
                                            pytest.mark.known_defect("DEF-001")], id="TC-BB-008-len8"),
    pytest.param("Test12345", True,  marks=pytest.mark.manual("TC-BB-009"), id="TC-BB-009-len9"),
])
def test_password_length_boundaries(ui, password, accepted):
    ...
```

## 3. Manual-to-automated traceability

Full mapping of TC-AUT-001 to 089 (script, manual cases, requirement, technique, checks, defect, result): [test_cases.md](test_cases.md).

| Requirement | Manual cases | Automated by |
| --- | --- | --- |
| REQ-001 Registration | TC-BB-001 to 013; TC-API-001 to 008; TC-WEB-001, 002, 016 | TC-AUT-001 to 005, 026, 027, 029 to 036, 074, 075, 089 |
| REQ-002 Login/logout/access | TC-BB-014 to 019; TC-API-009 to 011; TC-WEB-003, 004 | TC-AUT-006 to 008, 037 to 039, 076, 077 |
| REQ-003 Task CRUD | TC-BB-020 to 027; TC-API-014 to 016, 018 to 020, 022, 023, 034, 036, 039; TC-WEB-005 to 007, 009 to 012 | TC-AUT-009 to 016, 018, 019, 042 to 044, 046 to 048, 050, 051, 062, 064, 067, 078 to 080, 082 to 085 |
| REQ-004 Complete/reopen | TC-BB-028, 029, 042; TC-API-035; TC-WEB-008 | TC-AUT-017, 023, 063, 081 |
| REQ-005 Filters/search | TC-BB-030 to 035; TC-API-026 to 031; TC-WEB-015 | TC-AUT-021, 054 to 059, 088 |
| REQ-006 Urgency | TC-BB-036 to 042; TC-API-019, 021, 043; TC-WEB-006, 011 | TC-AUT-022, 023, 028, 047, 049, 071, 079, 084 |
| REQ-007 Dashboard | TC-BB-043; TC-API-042, 043; TC-WEB-014 | TC-AUT-024, 025, 070, 071, 087 |
| REQ-008 Account separation | TC-BB-044; TC-API-024, 033, 037, 040, 044; TC-WEB-013 | TC-AUT-020, 052, 061, 065, 068, 072, 086 |
| REQ-009 API contract | TC-API-007, 011 to 013, 017, 018, 023, 025, 031, 032, 036, 038, 041, 045 | TC-AUT-035, 039 to 041, 045, 046, 051, 053, 059, 060, 064, 066, 069, 073 |

All 44 Week 1 cases and all 61 Week 4 cases (100%) are automated, every requirement REQ-001 to REQ-009 has at least one automated check, and every automated check traces back to a manual case.

## 4. Execution report and logs

Every run folder in [evidences/runs/](evidences/runs/) holds `results.md` (one row per check), `results.json`, `junit.xml`, `pytest.log` (each UI/API step with a timestamp), `server.log` and `screenshots/`.

### 4.1 Execution runs

| # | Date | Run folder | Scope | Checks | Pass | Fail (known) | Fail (new) | Time | Exit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-11-20 | [edge-full-run1](evidences/runs/20261120-210226-edge-full-run1/results.md) | Full (browser + rules) | 65 | 58 | 7 | 0 | 36.8 s | 0 |
| 2 | 2026-11-20 | [edge-full-run2](evidences/runs/20261120-210303-edge-full-run2/results.md) | Repeat | 65 | 58 | 7 | 0 | 37.4 s | 0 |
| 3 | 2026-11-20 | [edge-full-run3](evidences/runs/20261120-210341-edge-full-run3/results.md) | Repeat | 65 | 58 | 7 | 0 | 36.3 s | 0 |
| 4 | 2026-11-20 | [edge-smoke](evidences/runs/20261120-210419-edge-smoke/results.md) | `-m smoke` | 11 | 11 | 0 | 0 | 13.8 s | 0 |
| 5 | 2026-11-20 | [edge-unit](evidences/runs/20261120-210433-edge-unit/results.md) | `-m unit` | 17 | 15 | 2 | 0 | 0.2 s | 0 |
| 6 | 2026-11-20 | [edge-defects-as-failures](evidences/runs/20261120-210434-edge-defects-as-failures/results.md) | Full, `--defects-as-failures` | 65 | 58 | - | 7 | 34.4 s | 1 |
| 7 | 2026-11-27 | [edge-full-w4-run1](evidences/runs/20261127-144603-edge-full-w4-run1/results.md) | Full (browser + rules + Web/API) | 166 | 127 | 39 | 0 | 84.4 s | 0 |
| 8 | 2026-11-27 | [api-run2](evidences/runs/20261127-144908-chrome-api-run2/results.md) | `-m api` (no browser) | 101 | 69 | 32 | 0 | 21.3 s | 0 |
| 9 | 2026-11-27 | [api-run3](evidences/runs/20261127-144931-chrome-api-run3/results.md) | `-m api` (repeat) | 101 | 69 | 32 | 0 | 21.4 s | 0 |
| 10 | 2026-11-27 | [api-defects-as-failures](evidences/runs/20261127-144953-chrome-api-defects-as-failures/results.md) | `-m api --defects-as-failures` | 101 | 69 | - | 32 | 21.2 s | 1 |

Runs 8-10 start no browser; the `chrome` in their folder names is the default option value.

**Stability.** Runs 1-3 gave identical results for all 65 checks, and runs 7-9 identical results for all 101 Web/API checks; no check needed a retry or changed verdict. In run 7 the 65 browser and rule checks matched runs 1-3, so the Edge 157 -> 158 update changed nothing. Runs 6 and 10 report the known defects as plain failures (exit 1), so they are never hidden.

### 4.2 Known defects re-tested by the suite

| Defect | Automated checks | Symptom observed | Status |
| --- | --- | --- | --- |
| DEF-001 8-character password rejected | TC-AUT-002, 027, 033 | Stays on `/register` with "Password must be at least 8 characters"; API `400 invalid password` | Open, reproduced |
| DEF-002 Today counted as overdue | TC-AUT-022, 025, 028, 049, 071 | Task due today shows `Overdue`; Overdue counter 2, expected 1 | Open, reproduced |
| DEF-003 Blank/whitespace title saved | TC-AUT-012, 083 | `whitespace-only title created 1 task(s): ['']`; web form `302` and blank task saved | Open, reproduced |
| DEF-005 Title HTML rendered as markup | TC-AUT-019 | `<b>` tags interpreted as markup in the list | Open, reproduced |
| DEF-014 API deletes another user's task | TC-AUT-068 | Intruder DELETE 200; owner's GET then 404 | Open, reproduced |
| DEF-015 Invalid due date saved, then 500s | TC-AUT-047, 064, 084 | Create 500 HTML; list/dashboard then `(500, 500)`; web form 302 | Open, reproduced |
| DEF-016 Duplicate username accepted | TC-AUT-036, 089 | `201` with a new id; web form 302 | Open, reproduced |
| DEF-017 Apostrophe in API search causes 500 | TC-AUT-058 | `500 text/html` for `q=O'Brien` | Open, reproduced |
| DEF-018 Wrong JSON types cause 500 | TC-AUT-035, 046, 064 | `500 text/html` in all five variants | Open, reproduced |
| DEF-019 Unknown category accepted | TC-AUT-048, 064, 085 | `201` with `category_id: 999` / `"abc"`; PUT 200; web 302 | Open, reproduced |
| DEF-020 Update skips title validation; `"false"` means done | TC-AUT-064 | `200` with blank title; `{"done": "false"}` sets `completed_at` | Open, reproduced |
| DEF-021 Deleting a missing task reports success | TC-AUT-069 | `200 {"result": "ok"}` | Open, reproduced |
| DEF-022 Invalid paging values accepted | TC-AUT-060 | `200` for `per_page=-1`, `page=-1`, `page=abc` | Open, reproduced |
| DEF-023 Categories work without login | TC-AUT-040 | `200` with the four categories | Open, reproduced |

No new defects were found, so Week 6 has no `defects.md`. Every check that passed in Weeks 1, 3 and 4 still passes. Visual and accessibility defects (DEF-004, DEF-006 to 013) are outside this suite.

Log excerpt for TC-AUT-025 (run 1, [pytest.log](evidences/runs/20261120-210226-edge-full-run1/pytest.log)): data seeded through the API, then the dashboard read through the UI.

```text
21:02:53 INFO  w6.api: API POST /api/tasks -> 201
21:02:53 INFO  w6.api: API PUT /api/tasks/45 -> 200
21:02:53 INFO  w6.ui: UI login username='w6_dash_21022636'
...
21:02:59 INFO  w6.ui: UI open /dashboard
21:03:00 INFO  w6.ui: UI dashboard counters {'Total Tasks': 7, 'Open': 6, 'Overdue': 2, 'Due Soon': 2, 'Completed (last 7 days)': 1}
```

### 4.3 Seeded-fault check: can the suite detect regressions?

Twelve realistic faults were injected one at a time into **copies** of the application outside the repository, and the suite was run against each copy with `--base-url` (browser checks for M1-M7, `-m api` for M8-M12). The real source was not modified. Script: [mutation_runs.py](evidences/mutation/mutation_runs.py); console: [mutation-console.log](evidences/mutation/mutation-console.log).

| Mutant | Injected fault | Requirement | Detected by | Result | Detected? |
| --- | --- | --- | --- | --- | --- |
| M1 | Task list ignores the `Done` status filter | REQ-005 | TC-AUT-021 [TC-BB-032] | [M1](evidences/mutation/20261120-205719-edge-mutant-M1/results.md) | Yes |
| M2 | Web delete is not committed | REQ-003 | TC-AUT-016 [TC-BB-027] | [M2](evidences/mutation/20261120-205755-edge-mutant-M2/results.md) | Yes |
| M3 | `/dashboard` loses `login_required_web` | REQ-002 | TC-AUT-007 | [M3](evidences/mutation/20261120-205831-edge-mutant-M3/results.md) | Yes |
| M4 | Task list no longer limited to the logged-in user | REQ-008 | TC-AUT-020 and 4 CRUD checks; 13 checks Blocked by precondition guards | [M4](evidences/mutation/20261120-205908-edge-mutant-M4/results.md) | Yes |
| M5 | "Due Soon" window widened from 2 to 3 days | REQ-006 | TC-AUT-022 [TC-BB-041], 024, 009 | [M5](evidences/mutation/20261120-210004-edge-mutant-M5/results.md) | Yes |
| M6 | DEF-001 fixed (`len >= 8`) | REQ-001 | TC-AUT-002 reports **Retest (XPASS)** | [M6](evidences/mutation/20261120-210526-edge-mutant-M6/results.md) | Yes (fix flagged) |
| M7 | A Done task can no longer be reopened | REQ-004 | TC-AUT-017 [TC-BB-029] | [M7](evidences/mutation/20261120-210118-edge-mutant-M7/results.md) | Yes |
| M8 | `GET /api/tasks/<id>` not limited to the owner | REQ-008 | TC-AUT-052 [TC-API-024] | [M8](evidences/mutation/20261127-144353-edge-mutant-M8/results.md) | Yes |
| M9 | `/api/dashboard` loses `login_required_api` | REQ-002, 009 | TC-AUT-039 [TC-API-011f] | [M9](evidences/mutation/20261127-144415-edge-mutant-M9/results.md) | Yes |
| M10 | DEF-014 and DEF-021 fixed | REQ-008, 009 | TC-AUT-068, 069 report **Retest (XPASS)** | [M10](evidences/mutation/20261127-144434-edge-mutant-M10/results.md) | Yes (fixes flagged) |
| M11 | API `status=done` filter ignored | REQ-005 | TC-AUT-055 [TC-API-027b] | [M11](evidences/mutation/20261127-144511-edge-mutant-M11/results.md) | Yes |
| M12 | `POST /api/login` accepts any password | REQ-002 | TC-AUT-038 [TC-API-010a] | [M12](evidences/mutation/20261127-144532-edge-mutant-M12/results.md) | Yes |

**All 12 seeded faults were detected**, each by a check traced to the matching requirement. Apart from M4, each fault failed only the checks for the broken behaviour; in M4 the precondition guards reported Blocked rather than misleading failures. M6 and M10 show that a fixed defect is reported for retest instead of passing unnoticed. M10 also shows the suite holds a fix to the *specified* result: limiting delete to the owner while still answering 200 would not pass TC-API-040.

## 5. Regression suite and automation reflection

### 5.1 Focused regression suite

| Tier | Selection | Checks | Time | When to run |
| --- | --- | --- | --- | --- |
| **Smoke** | `-m smoke`: register, log in, access control, logout, create, delete, complete/reopen, combined filter, account separation | 11 | ~14 s | Every change, before anything else |
| **Rules** | `-m unit`: username, password and urgency rules on `helpers.py` | 17 | < 1 s | Every change to `helpers.py`; any environment without a browser |
| **Web/API** | `-m api`: Week 4 checks over HTTP | 101 | ~21 s | Every change to `app.py` routes, validation or queries |
| **Full regression** | All checks | 166 | ~85 s | Before merging, after a defect fix, before each submission |
| **Defect view** | Full suite with `--defects-as-failures` | 166 | ~85 s | When reporting quality metrics (Week 8) |

The suite is focused: one check per manual case or BVA/decision-table row, covering all nine requirements and every open functional defect.

**Maintenance rules**
1. A new manual case that meets the selection rule gets a `TC-AUT` ID, `manual`/`req` markers and a row in `test_cases.md` in the same commit.
2. A newly logged defect gets a check marked `known_defect("DEF-nnn")`. When the fix lands, the strict XPASS shows Retest: retest, close the defect, remove the marker.
3. Never edit an expected result to make a run pass; change it only when the requirement changes, and record that in the RTM (Week 7).
4. A template change that breaks a locator is fixed in `pages.py`; a change to markup read by the Web/API checks is fixed in `api_checks.py`.
5. HTTP-level checks use the `api` marker and create their own accounts, so they run without a browser and in any order.

### 5.2 Benefits observed

| Benefit | Evidence |
| --- | --- |
| Speed and repeatability | All 44 Week 1 cases plus 10 GUI functional checks run in ~37 s with no manual data preparation; the 61 Week 4 cases in ~21 s with no Postman folder order |
| Consistency | Identical results across three repeat runs for both the browser and the Web/API tiers |
| Detects real regressions | All 12 seeded faults detected, each by the traced check |
| Defect retesting at no extra effort | 14 open defects retested on every run; fixes show up as Retest (M6, M10) |
| Date independence | Relative due dates remove Week 1's dependence on fixed October dates |
| Precise evidence | Each failure records the observed value (e.g. `Overdue counter is 2, expected 1`), a screenshot, a step log and JUnit XML |
| Isolation | The temporary database keeps the suite and the team's development data apart |

### 5.3 Limitations

| Limitation | Effect | Handling / residual risk |
| --- | --- | --- |
| Native browser UI (`required` bubble, `confirm()` dialog, date picker) is not in WebDriver screenshots | Parts of TC-BB-012/013/022/026/027 are checked indirectly | Validity state and dialog text are asserted; the date-picker experience stays a Week 3 concern |
| Dates set via JavaScript, not typed | A date-typing defect would be missed | Covered by Week 3 TC-CMP-002 |
| Data seeded through the API | A UI-only creation bug would show in few checks | UI creation has its own checks (TC-AUT-003, 009, 010) |
| Midnight boundary | A run crossing midnight can disagree on "today" for TC-AUT-022 to 025 | Unit checks use a fixed date; do not schedule runs at 00:00 |
| Strict xfail could mask a second fault with the same symptom | A new fault inside a known-defect check could look expected | xfail limited to `AssertionError`; known-defect assertions kept narrow; `--defects-as-failures` gives the raw view |
| One browser executed (Edge) | Chrome and Firefox not run in this phase | `--browser chrome/firefox` supported; cross-browser behaviour covered in Week 3 |
| No visual, usability or accessibility assertions | DEF-004, DEF-006 to 013 not in regression | Run the Week 3 axe scan as a scheduled job; visual review stays manual |
| Web/API checks do not render pages | No JavaScript runs for TC-WEB checks | The same behaviour is checked in a real browser by TC-AUT-001 to 025 |
| Expected error codes are a team decision | The README defines no error contract | Change them in one place and record the change in the RTM if the contract changes |
| First run needs network access | Selenium Manager downloads the driver | Later runs use the cached driver |

### 5.4 Reflection

- **What to automate.** The best return came from data-driven cases with exact expected results (BVA, EP, decision tables): one parametrised function replaces six to eight manual runs and screenshots. Cases needing human judgement were left manual; automated versions would break on harmless changes or check nothing meaningful.
- **Automation needs its own design.** The isolated database, API seeding, relative dates and explicit waits are why repeat runs were identical and why each seeded fault showed up as one specific failure.
- **Known defects.** Assertions keep the specified result and open defects are strict xfail, so the suite stays green when nothing new breaks but never hides a defect.
- **Layering.** Browser checks prove the pages use a rule; unit checks prove the rule itself. In M5 the UI urgency and dashboard checks failed together, pointing straight at `helpers.py`.
- **Week 4 cases** were the easiest to automate because Postman had already turned each expected result into an exact status-and-body check; the main work was making every check independent of the others.
- **Limits.** A green run means only that the checked behaviours did not regress; it says nothing about usability, accessibility, security or performance, which keep their own Week 3 and Week 5 tools.
