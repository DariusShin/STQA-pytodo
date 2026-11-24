# Week 6 - Test Automation and Regression

| Item | Recorded value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / Lab Group | September 2026 / Wednesday Lab - Group 2 |
| Tools | pytest 9.2.0, Selenium WebDriver 4.53.0 (Python), Microsoft Edge 157 headless |
| Phase status | Ready for review. The suite was built and executed on 2026-11-20. |

## Deliverable Checklist

- [ ] [Task 1](#task-1) - Automation candidate justification.
- [ ] [Task 2](#task-2) - Automated scripts.
- [ ] [Task 3](#task-3) - Manual-to-automated traceability.
- [ ] [Task 4](#task-4) - Execution report/logs.
- [ ] [Task 5](#task-5) - Regression suite and automation reflection.

Tick a task only after peer review. Expected results come from the earlier manual cases and the agreed requirements (REQ-001 to REQ-008). No assertion was changed to match the application's current behaviour.

## Deliverable structure

```
06_Automation_Regression/
├── README.md                    ← this report (Tasks 1-5)
├── setup.md                     ← environment, commands, outputs, how to read a result
├── requirements-test-lock.txt   ← pinned dependencies
├── pytest.ini, conftest.py      ← markers, isolated server, browser, result recording
├── run_app.py                   ← starts the unchanged app.py on a temporary database
├── pages.py                     ← Selenium page helpers (locators and waits in one place)
├── api_client.py                ← API client for seeding data and independent checks
├── test_01_auth.py              ← REQ-001 registration, REQ-002 login/logout/access
├── test_02_tasks.py             ← REQ-003 CRUD, REQ-004 complete/reopen, REQ-008 separation
├── test_03_filters.py           ← REQ-005 filters and search
├── test_04_urgency_dashboard.py ← REQ-006 urgency, REQ-007 dashboard
├── test_05_rules_unit.py        ← browser-free checks of the same rules on helpers.py
└── evidences/
    ├── runs/<stamp>-<browser>[-label]/   ← results.md/json, junit.xml, pytest.log, server.log, screenshots/
    └── mutation/                         ← seeded-fault runs (Task 4.4)
```

---

## Task 1

### Automation candidate justification

#### 1.1 Manual tests reviewed

| Phase | Source | Cases | Recorded outcome |
| --- | --- | --- | --- |
| Week 1 black-box | [01_Black_Box/test_cases.md](../01_Black_Box/test_cases.md) | TC-BB-001 to 044 | 40 Pass and 4 Fail (DEF-001, DEF-002, DEF-003) |
| Week 2 white-box | `02_White_Box_Coverage/` on branch `w2-whitebox` | pytest unit and integration tests | Already automated |
| Week 3 GUI | `03_Special_Testing/1_GUI/test_cases.md` on branch `w3-special-testing` | TC-GUI-001 to 022 | Includes DEF-004 and DEF-005 |
| Week 3 compatibility | `03_Special_Testing/2_Compatibility/` | TC-CMP-001 to 008 | C01-C04 executed |
| Week 3 usability | `03_Special_Testing/3_Usability/` | TC-USA-001 to 005 | Not Run (human review) |
| Week 3 accessibility | `03_Special_Testing/4_Accessibility/` | TC-A11Y-001 to 018 | DEF-007 to DEF-013 |

Weeks 4 and 5 had no executed cases when this phase was carried out. Section 5.4 shows how their cases will be added to the suite.

#### 1.2 Selection criteria

Each group of cases was scored from 1 (low) to 3 (high) on the four criteria in the brief:

| Criterion | 3 means | 1 means |
| --- | --- | --- |
| **Repetition (R)** | The check is needed after every change, or once per data value (BVA/EP rows) | It is run once or rarely |
| **Stability (S)** | The expected result is exact and deterministic, and the page and locators do not change often | The result needs human judgement, depends on visuals, or changes between runs or configurations |
| **Criticality (C)** | A failure blocks a core user goal (account, access, task data) | A failure is cosmetic |
| **Regression value (V)** | The behaviour is likely to break when the code changes, or it guards a known defect | It is unlikely to break, or a break would be obvious anyway |

**Rule:** automate when the total is at least 9 of 12 **and** the expected result can be checked by a program without human judgement. Groups scoring 7-8 are automated only for the part that has an exact oracle.

#### 1.3 Candidate decisions

| Manual cases | What they check | R | S | C | V | Total | Decision and justification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BB-001 to 011 | Username/password BVA and EP | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** Eleven rows of one procedure with different inputs, which suits `parametrize`. Guards DEF-001. |
| TC-BB-012, 013, 022 | Native `required` validation | 2 | 3 | 2 | 2 | 9 | **Automate the exact part.** Assert the DOM validity state (`valueMissing`), not the browser's message wording, which differs between browsers and locales. |
| TC-BB-014 to 017 | Login decision table | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** Four rules of one table. |
| TC-BB-018, 019 | Access control and logout | 3 | 3 | 3 | 3 | 12 | **Automate.** Security-relevant. Extended to `/dashboard` and `/tasks/new`. |
| TC-BB-020, 021, 024 to 027 | Create, edit, cancel, delete | 3 | 3 | 3 | 3 | 12 | **Automate.** Core workflow, run after every change. Selenium's alert API answers the native delete dialog. |
| TC-BB-023 | Whitespace-only title | 2 | 3 | 2 | 3 | 10 | **Automate.** Guards DEF-003. The API task count is the oracle. |
| TC-BB-028, 029, 042 | Complete/reopen state | 3 | 3 | 3 | 3 | 12 | **Automate** as one state-transition sequence. |
| TC-BB-030 to 035 | Filters and search | 3 | 3 | 2 | 3 | 11 | **Automate (data-driven)** using the Week 1 fixtures F1-F4 in a fresh account, so each expected set is exact. |
| TC-BB-036 to 041 | Urgency labels | 3 | 2 | 3 | 3 | 11 | **Automate.** Stability is 2 because the result depends on the date. Mitigated by date-relative data and a date-injected unit layer. Guards DEF-002. |
| TC-BB-043 | Dashboard counters | 3 | 2 | 2 | 3 | 10 | **Automate, split in two.** The DEF-002 counter is isolated so the other four counters still protect against new regressions. |
| TC-BB-044 | Account task separation | 3 | 3 | 3 | 3 | 12 | **Automate.** Data-isolation risk. |
| TC-GUI-004, 008, 010, 011, 012, 013, 015, 016 | Functional assertions inside GUI cases | 3 | 3 | 2 | 3 | 11 | **Automate the functional part.** These checks overlap Week 1 cases and are mapped in Task 3. The visual parts are not automated. |
| TC-GUI-020 | Special characters | 2 | 3 | 2 | 3 | 10 | **Automate.** Exact text oracle. Guards DEF-005. |
| TC-GUI-002 | Login error message | 2 | 3 | 2 | 2 | 9 | **Partly covered** by TC-AUT-006, which checks the exact error text. Its visual style is not checked. |
| TC-GUI-001, 003, 006, 007, 009, 014, 021 | Static layout, labels, titles | 1 | 2 | 1 | 2 | 6 | **Do not automate.** These rarely change, and a break would be obvious. Week 3's Playwright scripts can be rerun if the templates change. |
| TC-GUI-005, 017, 018, 019, 022 | Visual layout and heuristics (DEF-004) | 1 | 1 | 1 | 2 | 5 | **Do not automate.** They need visual judgement and are viewport-specific, so automated checks of them would be brittle. |
| TC-CMP-001 to 008 | Cross-configuration smoke | 2 | 2 | 2 | 2 | 8 | **Out of scope for the focused suite.** Already scripted in Week 3. This suite can still run on `--browser chrome/edge/firefox` (Section 5.3). |
| TC-USA-001 to 005 | Usability review | 1 | 1 | 2 | 1 | 5 | **Not automatable.** They need human participants and judgement. |
| TC-A11Y-001 to 018 | Accessibility (DEF-007 to 013) | 1 | 2 | 2 | 2 | 7 | **Do not add to the regression suite.** The axe/Lighthouse scans from Week 3 are the right tool for these, and keyboard and focus checks need a human. Recommendation in 5.4. |
| Week 2 white-box tests | Unit and integration tests | - | - | - | - | - | **Already automated.** That suite measures coverage. This suite reuses only the three boundary rules (TC-AUT-026 to 028), so the regression run does not depend on another phase's branch. |

**Outcome:** all 44 Week 1 cases and the functional parts of 10 Week 3 GUI cases are automated in 28 automated test cases (TC-AUT-001 to 028). These run as **65 pytest checks**, 48 through the browser and 17 at rule level. The following are deliberately left manual: 12 GUI cases (visual or static), the usability review, and the accessibility and compatibility matrices.

#### 1.4 Design decisions that follow from the selection

| Decision | Reason |
| --- | --- |
| **Selenium WebDriver** for UI checks | The approved tool. It drives a real browser through the W3C WebDriver protocol, the same path a user's clicks take. Week 3 used Playwright for visual work, but this phase uses the approved tool. |
| **Preconditions seeded through the JSON API** | Each check covers only its own behaviour. For example, a filter check does not fail because task creation broke; that is the job of TC-AUT-009. Seeding is also much faster than clicking through forms. |
| **API used as an independent oracle** where the page could hide a problem | For example, TC-AUT-012 counts tasks through the API rather than trusting what the list shows. |
| **Isolated server on a temporary database** | Every run starts from a known state. The shared `pytodo_pro.db` is never modified, and runs can be repeated. |
| **Data-driven tests** (`pytest.mark.parametrize`) | One procedure covers each BVA/EP/decision-table row, and the row ID is the manual case ID. |
| **Known defects as strict, narrow xfail** | The assertion keeps the *specified* result. `strict=True` turns a fixed defect into a visible XPASS. `raises=AssertionError` means any other error is still reported as a failure (Section 5.2). |
| **Page helpers in `pages.py`** | Locators and waits are kept in one place, so a template change needs one fix, not one per test. Only explicit waits are used, with no sleeps. |

---

## Task 2

### Automated scripts

| Script | Automated cases | Description |
| --- | --- | --- |
| [conftest.py](conftest.py) | - | Command-line options (`--browser`, `--headed`, `--base-url`, `--defects-as-failures`, `--run-label`). Starts the isolated server and the browser session. Provides account fixtures. Converts `known_defect` markers into xfail. Records results to `results.md/json` and takes failure screenshots. |
| [run_app.py](run_app.py) | - | Imports the unchanged `app.py`, points `DATABASE` at a temporary file, runs `init_db()` and serves on port 5006 without the debug reloader. |
| [pages.py](pages.py) | - | `PyTodoUI`: `register`, `login`, `logout`, `create_task`, `fill_task_form`, `rows`, `toggle`, `open_edit`, `delete` (handles `confirm()`), `filter_category`/`filter_status`/`search`, `dashboard_counters`, `validation_state`. Each action is logged. |
| [api_client.py](api_client.py) | - | Standard-library API client used for setup and oracles. |
| [test_01_auth.py](test_01_auth.py) | TC-AUT-001 to 008 | Registration BVA/EP, required fields, login decision table, access control, logout |
| [test_02_tasks.py](test_02_tasks.py) | TC-AUT-009 to 020 | Create, title-only, empty and whitespace title, edit, cancel edit, cancel and confirm delete, complete/reopen, special characters, account separation |
| [test_03_filters.py](test_03_filters.py) | TC-AUT-021 | Category, status, search, no-match and combined filters, with checks that the filter controls keep their values |
| [test_04_urgency_dashboard.py](test_04_urgency_dashboard.py) | TC-AUT-022 to 025 | Six urgency labels, completed-overrides-overdue, dashboard counters (split around DEF-002) |
| [test_05_rules_unit.py](test_05_rules_unit.py) | TC-AUT-026 to 028 | Username, password and urgency rules on `helpers.py`, with the date injected |

Markers tie each check to the documentation:

```python
@pytest.mark.auto("TC-AUT-002")          # automated case ID (Task 3)
@pytest.mark.req("REQ-001")               # requirement
@pytest.mark.parametrize("password, accepted", [
    pytest.param("Test123",   False, marks=pytest.mark.manual("TC-BB-007"), id="TC-BB-007-len7"),
    pytest.param("Test1234",  True,  marks=[pytest.mark.manual("TC-BB-008", "TC-GUI-004"),
                                            pytest.mark.known_defect("DEF-001")], id="TC-BB-008-len8"),
    pytest.param("Test12345", True,  marks=pytest.mark.manual("TC-BB-009"), id="TC-BB-009-len9"),
])
def test_password_length_boundaries(ui, password, accepted):
    username = username_of_length(12)
    ui.register(username, password)
    if accepted:
        assert_registered(ui, username)        # specified result: 8 characters is accepted
    else:
        assert_rejected(ui, PASSWORD_RULE)
```

See [setup.md](setup.md) for how to install and run the scripts.

---

## Task 3

### Manual-to-automated traceability

`Result` is the outcome of the baseline run on 2026-11-20 ([run 1](#41-execution-runs)). `Fail (known)` means the check failed with the documented defect symptom and was reported as strict xfail. **S** = in the smoke subset.

| Auto ID | Script :: test | Manual case(s) | Requirement | Technique | Checks | S | Defect | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-AUT-001 | test_01_auth :: test_username_length_boundaries | TC-BB-001, 002, 003, 004, 005, 006 | REQ-001 | BVA | 6 | | - | 6 Pass |
| TC-AUT-002 | test_01_auth :: test_password_length_boundaries | TC-BB-007, 008, 009; TC-GUI-004 | REQ-001 | BVA | 3 | | DEF-001 | 2 Pass, TC-BB-008 Fail (known) |
| TC-AUT-003 | test_01_auth :: test_valid_registration_opens_task_list | TC-BB-010 | REQ-001 | EP | 1 | S | - | Pass |
| TC-AUT-004 | test_01_auth :: test_username_with_hyphen_is_rejected | TC-BB-011 | REQ-001 | EP | 1 | | - | Pass |
| TC-AUT-005 | test_01_auth :: test_empty_registration_field_blocked_by_browser | TC-BB-012, 013 | REQ-001 | EP / browser validation | 2 | | - | 2 Pass |
| TC-AUT-006 | test_01_auth :: test_login_decision_table | TC-BB-014, 015, 016, 017; TC-GUI-002 (text only) | REQ-002 | Decision table | 4 | S (rule 1) | - | 4 Pass |
| TC-AUT-007 | test_01_auth :: test_protected_page_redirects_when_logged_out | TC-BB-018 (extended to 3 pages) | REQ-002 | State transition | 3 | S | - | 3 Pass |
| TC-AUT-008 | test_01_auth :: test_logout_revokes_protected_page_access | TC-BB-019 | REQ-002 | State transition | 1 | S | - | Pass |
| TC-AUT-009 | test_02_tasks :: test_create_full_field_task_persists | TC-BB-020 | REQ-003 | EP | 1 | S | - | Pass |
| TC-AUT-010 | test_02_tasks :: test_create_title_only_task | TC-BB-021 | REQ-003 | EP | 1 | | - | Pass |
| TC-AUT-011 | test_02_tasks :: test_empty_title_blocked_by_browser | TC-BB-022 | REQ-003 | EP / browser validation | 1 | | - | Pass |
| TC-AUT-012 | test_02_tasks :: test_whitespace_only_title_rejected | TC-BB-023; TC-GUI-016 | REQ-003 | EP / input validation | 1 | | DEF-003 | Fail (known) |
| TC-AUT-013 | test_02_tasks :: test_edit_persists_all_fields | TC-BB-024; TC-GUI-012, 015 | REQ-003 | Functional | 1 | | - | Pass |
| TC-AUT-014 | test_02_tasks :: test_cancel_edit_preserves_saved_data | TC-BB-025 | REQ-003 | State transition | 1 | | - | Pass |
| TC-AUT-015 | test_02_tasks :: test_cancel_deletion_retains_task | TC-BB-026; TC-GUI-013 | REQ-003 | State transition | 1 | | - | Pass |
| TC-AUT-016 | test_02_tasks :: test_confirm_deletion_removes_only_that_task | TC-BB-027; TC-GUI-013 | REQ-003 | State transition | 1 | S | - | Pass |
| TC-AUT-017 | test_02_tasks :: test_complete_then_reopen_task | TC-BB-028, 029; TC-GUI-011 | REQ-004 | State transition | 1 | S | - | Pass |
| TC-AUT-018 | test_02_tasks :: test_special_characters_preserved_in_edit_form | TC-GUI-020 (edit form) | REQ-003 | Functional | 1 | | - | Pass |
| TC-AUT-019 | test_02_tasks :: test_special_characters_displayed_literally_in_list | TC-GUI-020 (list) | REQ-003 | Functional | 1 | | DEF-005 | Fail (known) |
| TC-AUT-020 | test_02_tasks :: test_each_account_sees_only_its_own_tasks | TC-BB-044 | REQ-008 | EP | 1 | S | - | Pass |
| TC-AUT-021 | test_03_filters :: test_filters_return_only_matching_tasks | TC-BB-030, 031, 032, 033, 034, 035; TC-GUI-008 | REQ-005 | EP / decision table | 6 | S (035) | - | 6 Pass |
| TC-AUT-022 | test_04_urgency_dashboard :: test_urgency_label | TC-BB-036, 037, 038, 039, 040, 041; TC-GUI-010 | REQ-006 | BVA | 6 | | DEF-002 | 5 Pass, TC-BB-038 Fail (known) |
| TC-AUT-023 | test_04_urgency_dashboard :: test_completion_overrides_overdue | TC-BB-042 | REQ-004, REQ-006 | State transition | 1 | | - | Pass |
| TC-AUT-024 | test_04_urgency_dashboard :: test_dashboard_counters_unaffected_by_def002 | TC-BB-043 (Total, Open, Due Soon, Completed) | REQ-007 | Independent calculation | 1 | | - | Pass |
| TC-AUT-025 | test_04_urgency_dashboard :: test_dashboard_overdue_counter | TC-BB-043 (Overdue) | REQ-007 | Independent calculation | 1 | | DEF-002 | Fail (known) |
| TC-AUT-026 | test_05_rules_unit :: test_username_rule | TC-BB-001 to 006, 010, 011 | REQ-001 | BVA / EP (unit) | 8 | | - | 8 Pass |
| TC-AUT-027 | test_05_rules_unit :: test_password_rule | TC-BB-007, 008, 009 | REQ-001 | BVA (unit) | 3 | | DEF-001 | 2 Pass, TC-BB-008 Fail (known) |
| TC-AUT-028 | test_05_rules_unit :: test_urgency_rule | TC-BB-036 to 041 | REQ-006 | BVA (unit) | 6 | | DEF-002 | 5 Pass, TC-BB-038 Fail (known) |
| **Total** | | | | | **65** | 11 | | **58 Pass, 7 Fail (known)** |

#### 3.1 Reverse check: every Week 1 case is automated

| Requirement | Manual cases | Automated by |
| --- | --- | --- |
| REQ-001 Registration | TC-BB-001 to 013 | TC-AUT-001 to 005; rules in TC-AUT-026, 027 |
| REQ-002 Login/logout/access | TC-BB-014 to 019 | TC-AUT-006 to 008 |
| REQ-003 Task CRUD | TC-BB-020 to 027 | TC-AUT-009 to 016, 018, 019 |
| REQ-004 Complete/reopen | TC-BB-028, 029, 042 | TC-AUT-017, 023 |
| REQ-005 Filters/search | TC-BB-030 to 035 | TC-AUT-021 |
| REQ-006 Urgency | TC-BB-036 to 042 | TC-AUT-022, 023; rules in TC-AUT-028 |
| REQ-007 Dashboard | TC-BB-043 | TC-AUT-024, 025 |
| REQ-008 Account separation | TC-BB-044 | TC-AUT-020 |

All 44 of 44 Week 1 cases (100%) and all 8 requirements are covered by at least one automated check. Every automated check traces back to a manual case.

#### 3.2 Deviations from the manual procedure

| Case | Difference from the manual case | Why it does not weaken the check |
| --- | --- | --- |
| All | Accounts and fixtures are created through the API, not the UI | Creation through the UI has its own checks (TC-AUT-003, 009, 010). |
| TC-BB-031 | Expects 3 Open rows, where Week 1 expected 5 | Week 1's account also held its CRUD tasks. Here the account holds only F1-F4, so the expected set is exact. |
| TC-BB-036 to 043 | Due dates are offsets from the run day, where Week 1 used fixed October 2026 dates | The boundaries tested are the same (D-1, D, D+1, D+2, D+3). |
| Date fields | The ISO value is set via JavaScript plus `input`/`change` events, and is not typed into the date picker | Typed dates depend on the browser locale. The date picker itself is a Week 3 usability concern. |
| TC-BB-012, 013, 022 | Assert `validity.valueMissing` and that a message exists, not the message text | The message wording belongs to the browser and differs by locale. |
| TC-BB-018 | Also checks `/dashboard` and `/tasks/new` | Adds coverage at no extra cost. |

---

## Task 4

### Execution report/logs

#### 4.1 Execution runs

| Item | Value |
| --- | --- |
| Date / timezone | 2026-11-20, Malay Peninsula Standard Time (UTC+8) |
| Application commit | `9cc1f34`. `app.py`, `helpers.py` and `templates/` are unchanged from the version tested in Weeks 1-3 |
| Environment | Windows 11 Home 10.0.26200, Python 3.14.7, pytest 9.2.0, Selenium 4.53.0, Microsoft Edge 157.0.4341.60 (headless, 1366x900) |
| Target | Isolated `app.py` on port 5006 with a new temporary SQLite database for each run |
| How runs were executed | From the command line, as described in [setup.md](setup.md) |

| # | Run folder (`evidences/runs/`) | Scope | Checks | Pass | Fail (known defect) | Fail (new) | Wall time | Exit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [20261120-210226-edge-full-run1](evidences/runs/20261120-210226-edge-full-run1/results.md) | Full regression | 65 | 58 | 7 | 0 | 36.8 s | 0 |
| 2 | [20261120-210303-edge-full-run2](evidences/runs/20261120-210303-edge-full-run2/results.md) | Full regression (repeat) | 65 | 58 | 7 | 0 | 37.4 s | 0 |
| 3 | [20261120-210341-edge-full-run3](evidences/runs/20261120-210341-edge-full-run3/results.md) | Full regression (repeat) | 65 | 58 | 7 | 0 | 36.3 s | 0 |
| 4 | [20261120-210419-edge-smoke](evidences/runs/20261120-210419-edge-smoke/results.md) | `-m smoke` | 11 | 11 | 0 | 0 | 13.8 s | 0 |
| 5 | [20261120-210433-edge-unit](evidences/runs/20261120-210433-edge-unit/results.md) | `-m unit` (no browser) | 17 | 15 | 2 | 0 | 0.2 s | 0 |
| 6 | [20261120-210434-edge-defects-as-failures](evidences/runs/20261120-210434-edge-defects-as-failures/results.md) | Full, `--defects-as-failures` | 65 | 58 | - | 7 | 34.4 s | 1 |

Every run folder has `results.md` (one row per check), `results.json`, `junit.xml`, `pytest.log` (each UI/API step with a timestamp), `server.log` (HTTP request log) and `screenshots/`.

**Stability.** Runs 1-3 gave identical results for every one of the 65 checks. No check needed a retry, and none passed in one run and failed in another. Run 6 reports the same seven checks as plain failures (exit 1), so the known defects are not hidden when that view is chosen.

#### 4.2 Known defects re-tested by the suite

| Defect | Automated checks | Symptom observed on 2026-11-20 (run 1) | Evidence | Status after retest |
| --- | --- | --- | --- | --- |
| DEF-001 Eight-character password rejected | TC-AUT-002 [TC-BB-008], TC-AUT-027 [TC-BB-008] | The browser stays on `/register` and shows "Password must be at least 8 characters." The unit check gives `is_valid_password("Test1234") is False` | [screenshot](evidences/runs/20261120-210226-edge-full-run1/screenshots/test_password_length_boundaries_TC-BB-008-len8_.png) | Open, reproduced |
| DEF-002 Today classified and counted as overdue | TC-AUT-022 [TC-BB-038], TC-AUT-025, TC-AUT-028 [TC-BB-038] | `BB-TODAY due 2026-11-20 shows 'Overdue'`. The Overdue counter is 2, expected 1 | [label](evidences/runs/20261120-210226-edge-full-run1/screenshots/test_urgency_label_TC-BB-038-today_.png), [dashboard](evidences/runs/20261120-210226-edge-full-run1/screenshots/test_dashboard_overdue_counter.png) | Open, reproduced |
| DEF-003 Whitespace-only title creates a task | TC-AUT-012 | `whitespace-only title created 1 task(s): ['']` | [screenshot](evidences/runs/20261120-210226-edge-full-run1/screenshots/test_whitespace_only_title_rejected.png) | Open, reproduced |
| DEF-005 Title HTML rendered as markup | TC-AUT-019 | The list shows `GUI-Special & bold "double" ...`: the `<b>` tags are interpreted as markup, not shown as text | [screenshot](evidences/runs/20261120-210226-edge-full-run1/screenshots/test_special_characters_displayed_literally_in_list.png) | Open, reproduced |

The suite found no new defects. Every check that passed in Weeks 1 and 3 still passes on the current build. DEF-004 and DEF-006 to DEF-013 are visual or accessibility defects. They are outside this suite's scope (Task 1.3) and were not retested here.

#### 4.3 Log excerpt: TC-AUT-025 in run 1

The excerpt below is from [pytest.log](evidences/runs/20261120-210226-edge-full-run1/pytest.log). It shows the dataset being seeded through the API, followed by the UI step that reads the dashboard.

```text
21:02:53 INFO  w6.api: API POST /api/tasks -> 201
21:02:53 INFO  w6.api: API PUT /api/tasks/45 -> 200
21:02:53 INFO  w6.ui: UI login username='w6_dash_21022636'
...
21:02:59 INFO  w6.ui: UI open /dashboard
21:03:00 INFO  w6.ui: UI dashboard counters {'Total Tasks': 7, 'Open': 6, 'Overdue': 2, 'Due Soon': 2, 'Completed (last 7 days)': 1}
```

#### 4.4 Can the suite detect regressions? (seeded-fault check)

A green suite only has value if it turns red when something breaks. To test this, seven realistic faults were injected one at a time into **copies** of the application held outside the repository. The 48 browser checks were run against each copy using `--base-url`. The real source was not modified. The script is [mutation_runs.py](evidences/mutation/mutation_runs.py), and the console output is in [mutation-console.log](evidences/mutation/mutation-console.log).

| Mutant | Injected fault | Requirement | Detected by | Result folder | Detected? |
| --- | --- | --- | --- | --- | --- |
| M1 | Task list ignores the `Done` status filter | REQ-005 | TC-AUT-021 [TC-BB-032] | [M1](evidences/mutation/20261120-205719-edge-mutant-M1/results.md) | Yes |
| M2 | Web delete is not committed | REQ-003 | TC-AUT-016 [TC-BB-027] (the task reappears) | [M2](evidences/mutation/20261120-205755-edge-mutant-M2/results.md) | Yes |
| M3 | `/dashboard` loses `login_required_web` | REQ-002 | TC-AUT-007 [dashboard] | [M3](evidences/mutation/20261120-205831-edge-mutant-M3/results.md) | Yes |
| M4 | Task list no longer limited to the logged-in user | REQ-008 | TC-AUT-020 and 4 CRUD checks fail. 13 checks are Blocked by their precondition guards | [M4](evidences/mutation/20261120-205908-edge-mutant-M4/results.md) | Yes |
| M5 | "Due Soon" window widened from 2 to 3 days | REQ-006 | TC-AUT-022 [TC-BB-041], TC-AUT-024, TC-AUT-009 | [M5](evidences/mutation/20261120-210004-edge-mutant-M5/results.md) | Yes |
| M6 | DEF-001 *fixed* (`len >= 8`) | REQ-001 | TC-AUT-002 [TC-BB-008] reports **Retest (XPASS)** | [M6](evidences/mutation/20261120-210526-edge-mutant-M6/results.md) | Yes (fix flagged) |
| M7 | A Done task can no longer be reopened | REQ-004 | TC-AUT-017 [TC-BB-029] | [M7](evidences/mutation/20261120-210118-edge-mutant-M7/results.md) | Yes |

**All 7 seeded faults were detected**, each by a check traced to the matching requirement. Except for M4, each fault failed only the checks for the broken behaviour, which points directly to the cause. In M4, the precondition guards reported `Blocked` instead of misleading `Fail` results. M6 shows that a fixed known defect is reported for retest instead of passing unnoticed.

---

## Task 5

### Regression suite and automation reflection

#### 5.1 The focused regression suite

| Tier | Selection | Checks | Time | When to run |
| --- | --- | --- | --- | --- |
| **Smoke** | `-m smoke`: register, log in, access control (3 pages), logout, create, delete, complete/reopen, combined filter, account separation | 11 | about 14 s | Every code change or commit, before anything else |
| **Rules** | `-m unit`: username, password and urgency boundaries on `helpers.py` | 17 | under 1 s | Every change to `helpers.py`, and in any environment without a browser |
| **Full regression** | All checks | 65 | about 37 s | Before merging a branch, after any defect fix, and before each weekly submission |
| **Defect view** | Full suite with `--defects-as-failures` | 65 | about 35 s | When reporting quality metrics (Week 8), so known defects count as failures |

The suite is *focused*: it has one check per manual case or BVA/decision-table row, and together these cover all eight requirements and every open functional defect. Visual, usability and accessibility checks were left out (Task 1.3). They would make the suite slower and more brittle without adding regression value.

**Maintenance rules**

1. A new manual case that meets the Task 1.2 rule gets a `TC-AUT` ID, `manual`/`req` markers and a row in Task 3, all in the same commit.
2. When a defect is logged, add a check that fails because of it and mark it `known_defect("DEF-nnn")`. When the defect is fixed, the strict XPASS shows `Retest`. Retest the defect, close it, and remove the marker.
3. Never edit an expected result to make a run pass. Change it only if the requirement itself changes, and record that change in the RTM (Week 7).
4. A template change that breaks a locator is fixed in `pages.py` only.

#### 5.2 Benefits observed

| Benefit | Evidence from this phase |
| --- | --- |
| **Speed and repeatability** | All 44 Week 1 cases plus 10 Week 3 functional checks run in about 37 s, with no manual data preparation. Week 1 needed dedicated accounts, fixed calendar dates and a screenshot for each case. |
| **Consistency** | Three consecutive runs gave identical results for all 65 checks (Section 4.1). Every run uses the same inputs, the same clean database and the same expected results. |
| **Detects real regressions** | All 7 seeded faults were detected, each by a check traced to the matching requirement (Section 4.4). |
| **Defect retesting at no extra effort** | DEF-001, 002, 003 and 005 are retested on every run. A fix shows up automatically as `Retest` (M6). |
| **Date independence** | Relative due dates, and the fixed date passed to the unit checks, remove Week 1's dependence on specific October dates. TC-BB-036 to 043 can now be rerun on any day. |
| **Precise evidence** | Each failure records the exact observed value (for example, `Overdue counter is 2, expected 1`), a screenshot, a step log and a JUnit file for CI. |
| **Isolation** | The isolated database keeps the suite from changing the team's development data, and keeps that data from affecting the suite. |

#### 5.3 Limitations and how they were handled

| Limitation | Effect | Handling / residual risk |
| --- | --- | --- |
| **Native browser UI does not appear in WebDriver screenshots**: the `required` bubble, the `confirm()` dialog and the date picker | These parts of TC-BB-012/013/022/026/027 are checked indirectly | The validity state and dialog text are asserted instead. The date-picker experience remains a manual Week 3 usability concern. |
| **Dates are set via JavaScript**, not typed | A defect in date typing or picking would be missed | Typed dates depend on the locale and would make the suite flaky. Covered by Week 3 TC-CMP-002. |
| **Data seeded through the API** | A bug that only affects creating tasks through the UI would not show up in most checks | UI creation has its own checks (TC-AUT-003, 009, 010). This is a deliberate trade-off: seeding is faster and makes faults easier to locate. |
| **Midnight boundary** | If a run crosses midnight, the test's "today" and the server's "today" can differ for TC-AUT-022 to 025 | The unit checks (TC-AUT-028) use a fixed date and are unaffected. Do not schedule runs at 00:00. |
| **Strict xfail can mask a second fault** in the same assertion | A new fault that produces the same symptom inside a known-defect check would look "expected" | xfail is limited to `AssertionError`. Known-defect assertions are kept small: the dashboard check was split so that only the Overdue counter is xfail. `--defects-as-failures` gives the raw view. |
| **Only one browser executed** (Edge 157 on Windows) | Chrome and Firefox were not run in this phase | `--browser chrome/firefox` is supported. Cross-browser behaviour was covered in Week 3 (C01-C04). |
| **No visual, layout, usability or accessibility assertions** | DEF-004 and DEF-006 to 013 are not covered by regression checks | Recommendation: run the Week 3 axe scan as a scheduled job (Section 5.4). Visual review stays manual. |
| **Automation checks only what it asserts** | A page could pass while showing an unexpected extra element | Checks compare whole result sets (for example, exact title lists), not just whether one item is present. Exploratory manual testing is still needed. |
| **Maintenance cost** | Template or ID changes need script updates | Locators live only in `pages.py`. Where possible they use stable `name` attributes and table structure, not styling classes. |
| **First run needs network access** | Selenium Manager downloads the browser driver | Documented in setup.md. Later runs use the cached driver. |

#### 5.4 Reflection

- **What to automate.** The clearest returns came from data-driven cases with an exact expected result, namely the BVA, EP and decision-table rows. One parametrized function replaces six to eight manual executions and their screenshots. Cases that need human judgement (layout, heuristics, usability) scored low and were left manual. Automated versions of them would either break on harmless changes or pass without checking anything meaningful.
- **Automation needs its own design work.** The most important early decisions were not about Selenium itself. They were the isolated database, seeding through the API, relative dates and explicit waits. These are why three runs in a row gave identical results and why each seeded fault showed up as a specific failure.
- **Handling known defects.** Each assertion keeps the specified result, and open defects are marked as strict xfail. The suite therefore stays green when nothing new has broken, but it cannot hide a defect: `--defects-as-failures` and the results table always list them, and a fix is reported automatically for retest.
- **Layering.** Browser checks prove that a rule is used by the pages. Unit checks prove the rule itself, quickly and without depending on the current date. Having both makes a fault easier to locate: in M5, the UI urgency check and the dashboard check failed together, which pointed to `helpers.py`.
- **Limits.** A green run means only that the checked behaviours did not regress. It says nothing about usability, accessibility, security or performance. Weeks 4 and 5 (API and security) should add their confirmed findings to this suite using the same markers. The main candidate is the missing ownership check in `DELETE /api/tasks/<id>`, which a comment in the source code points out. It is not logged as a defect here because no Week 4 or 5 test has confirmed it yet. The Week 3 axe scan should run as a scheduled job alongside this suite, not inside it.
