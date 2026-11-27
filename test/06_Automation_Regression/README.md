# Week 6 - Test Automation and Regression

| Item | Recorded value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / Lab Group | September 2026 / Wednesday Lab - Group 2 |
| Tools | pytest 9.2.0, Selenium WebDriver 4.53.0 (Python), Microsoft Edge 157/158 headless; Python standard-library HTTP client for the Week 4 Web/API checks |
| Phase status | Ready for review. The suite was built and executed on 2026-11-20. The Week 4 Web/API cases were added and executed on 2026-11-27 (Sections 1.5, 3.3, 4.5 and 4.6). |

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
├── api_client.py                ← HTTP client: JSON API and web form routes (seeding, oracles, Week 4 checks)
├── api_checks.py                ← Week 4 assertions (status + JSON error, redirects) and HTML readers
├── test_01_auth.py              ← REQ-001 registration, REQ-002 login/logout/access
├── test_02_tasks.py             ← REQ-003 CRUD, REQ-004 complete/reopen, REQ-008 separation
├── test_03_filters.py           ← REQ-005 filters and search
├── test_04_urgency_dashboard.py ← REQ-006 urgency, REQ-007 dashboard
├── test_05_rules_unit.py        ← browser-free checks of the same rules on helpers.py
├── test_06_api.py               ← Week 4 TC-API-001 to 045 (REST API, REQ-001 to 009)
├── test_07_web_forms.py         ← Week 4 TC-WEB-001 to 016 (web forms, server-side validation, UI vs API)
└── evidences/
    ├── runs/<stamp>-<browser>[-label]/   ← results.md/json, junit.xml, pytest.log, server.log, screenshots/
    └── mutation/                         ← seeded-fault runs (Task 4.4, 4.6)
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
| Week 4 Web/API | [04_Web_API/test_cases.md](../04_Web_API/test_cases.md) | TC-WEB-001 to 016, TC-API-001 to 045 | 43 Pass and 18 Fail (DEF-001 to 003 reproduced; DEF-014 to DEF-023). Added on 2026-11-27, see 1.5 |

Week 5 had no executed cases when the browser suite was built on 2026-11-20. Week 4 was executed on 2026-11-24 and added to this suite on 2026-11-27 (Section 1.5).

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

**Outcome:** all 44 Week 1 cases and the functional parts of 10 Week 3 GUI cases are automated in 28 automated test cases (TC-AUT-001 to 028). These run as **65 pytest checks**, 48 through the browser and 17 at rule level. The following are deliberately left manual: 12 GUI cases (visual or static), the usability review, and the accessibility and compatibility matrices. The Week 4 cases added on 2026-11-27 bring the suite to 89 automated cases and 166 checks (Section 1.5).

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

#### 1.5 Week 4 Web/API cases (added 2026-11-27)

The same criteria (1.2) were applied to the 61 Week 4 cases, and the priorities in [Week 4 Section 5.5](../04_Web_API/README.md#55-recommendations-for-week-6-automation-in-pytest) were followed.

| Week 4 cases | What they check | R | S | C | V | Total | Decision and justification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-API-024, 033, 037, 040, 044; TC-WEB-013 | One user cannot read, list, change or delete another user's task | 3 | 3 | 3 | 3 | 12 | **Automate.** Week 4 priority 1. Guards DEF-014 (Critical). |
| TC-API-011, 012; TC-WEB-004 | Every protected endpoint and page refuses a logged-out caller | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** One row per endpoint or page. Guards DEF-023. |
| TC-API-001 to 010; TC-WEB-001 to 003, 016 | Registration and login partitions, wrong types, duplicates | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** Guards DEF-001, 016, 018. |
| TC-API-014 to 020, 036; TC-WEB-010 to 012 | Input validation on create, update and the web forms; nothing saved after a rejection | 3 | 3 | 3 | 3 | 12 | **Automate (data-driven).** One row per invalid value. Guards DEF-003, 015, 018, 019, 020. |
| TC-API-021, 042, 043 | Urgency boundaries and dashboard counts | 3 | 2 | 3 | 3 | 11 | **Automate.** Dates are offsets from the run day, as in TC-AUT-022. Guards DEF-002. |
| TC-API-022, 023, 025, 034, 035, 038, 039, 041, 045 | Read, update, delete round trips and API error contract | 3 | 3 | 2 | 3 | 11 | **Automate.** Exact status and JSON oracles. Guards DEF-021. |
| TC-API-026 to 032 | Filters, search, paging | 3 | 3 | 2 | 3 | 11 | **Automate** on the Week 4 five-task list dataset. Guards DEF-017, 022. |
| TC-WEB-005 to 009, 014, 015 | The web pages and the API agree | 3 | 3 | 2 | 3 | 11 | **Automate.** The API is the oracle for the web route, and the reverse for TC-WEB-006, 014. |
| TC-WEB-010 to 012 browser screenshots | DevTools evidence in Week 4 | 1 | 2 | 1 | 1 | 5 | **Not automated**, as Week 4 recommended. The server-side behaviour they show is automated. |

**Outcome:** all 61 Week 4 cases are automated as 61 automated test cases (TC-AUT-029 to 089, one per Week 4 case ID). They run as **101 pytest checks**, one per lettered variant (for example TC-API-036a to f). With them, the suite covers 115 manual cases (44 Week 1, the functional parts of 10 Week 3 GUI cases, 61 Week 4) in 89 automated cases and **166 checks**.

| Decision | Reason |
| --- | --- |
| **HTTP checks without a browser** (`test_06_api.py`, `test_07_web_forms.py`, marker `api`) | Week 4 tested status codes, JSON bodies and form submissions, not page rendering. A browser would add time and flakiness and nothing to these checks. |
| **Same isolated server as the browser checks**, not Flask's `test_client()` (Week 4 5.5 suggested either) | One server, one database and one run folder for the whole suite. `--base-url` and the seeded-fault script (4.6) also work for these checks, and the real HTTP stack (cookies, redirects, content types) is what is checked. |
| **Redirects are not followed; HTML 500 pages are not parsed as JSON** (`api_client.py`) | A web form's 302 and its target are asserted directly. A 500 page fails as an `AssertionError` with the observed status, so it is reported as the known defect rather than as an unrelated error. |
| **Fresh accounts for every check** | The Week 4 Postman run had to put the invalid-date cases last, because DEF-015 leaves a user unable to load their list. Here each check has its own users, so no ordering is needed and no check can affect another. |
| **One row per lettered variant, each with its own `known_defect`** | TC-API-036 has six variants with four different defects. Each variant fails or passes on its own, so a fix to one defect is reported for retest without waiting for the others. |
| **Follow-up requests inside the same assertion message** | For example, TC-API-019 reports both the create status and the list/dashboard status afterwards, so the failure message shows the whole DEF-015 symptom. |

---

## Task 2

### Automated scripts

| Script | Automated cases | Description |
| --- | --- | --- |
| [conftest.py](conftest.py) | - | Command-line options (`--browser`, `--headed`, `--base-url`, `--defects-as-failures`, `--run-label`). Starts the isolated server and the browser session. Provides account fixtures. Converts `known_defect` markers into xfail. Records results to `results.md/json` and takes failure screenshots. |
| [run_app.py](run_app.py) | - | Imports the unchanged `app.py`, points `DATABASE` at a temporary file, runs `init_db()` and serves on port 5006 without the debug reloader. |
| [pages.py](pages.py) | - | `PyTodoUI`: `register`, `login`, `logout`, `create_task`, `fill_task_form`, `rows`, `toggle`, `open_edit`, `delete` (handles `confirm()`), `filter_category`/`filter_status`/`search`, `dashboard_counters`, `validation_state`. Each action is logged. |
| [api_client.py](api_client.py) | - | Standard-library HTTP client used for setup, oracles and the Week 4 checks. One client is one cookie jar (one user session). It sends JSON or form bodies, does not follow redirects, and parses a body as JSON only when the server says it is JSON. |
| [api_checks.py](api_checks.py) | - | Week 4 assertions (`expect_json_error`, `expect_redirect`, `expect_not_accepted`), exact-length usernames, and standard-library HTML readers for the task table, the error message and the dashboard counters. |
| [test_01_auth.py](test_01_auth.py) | TC-AUT-001 to 008 | Registration BVA/EP, required fields, login decision table, access control, logout |
| [test_02_tasks.py](test_02_tasks.py) | TC-AUT-009 to 020 | Create, title-only, empty and whitespace title, edit, cancel edit, cancel and confirm delete, complete/reopen, special characters, account separation |
| [test_03_filters.py](test_03_filters.py) | TC-AUT-021 | Category, status, search, no-match and combined filters, with checks that the filter controls keep their values |
| [test_04_urgency_dashboard.py](test_04_urgency_dashboard.py) | TC-AUT-022 to 025 | Six urgency labels, completed-overrides-overdue, dashboard counters (split around DEF-002) |
| [test_05_rules_unit.py](test_05_rules_unit.py) | TC-AUT-026 to 028 | Username, password and urgency rules on `helpers.py`, with the date injected |
| [test_06_api.py](test_06_api.py) | TC-AUT-029 to 073 | Week 4 TC-API-001 to 045: registration, login, authentication, create/read/update/delete, validation, filters, paging, ownership, dashboard, HTTP method |
| [test_07_web_forms.py](test_07_web_forms.py) | TC-AUT-074 to 089 | Week 4 TC-WEB-001 to 016: web form workflows, server-side validation with the browser checks bypassed, web versus API comparison |

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

#### 3.3 Week 4 Web/API traceability

`Result` is the outcome of the full run on 2026-11-27 ([run 7](#45-execution-runs-week-4-cases-added)). It matches the Week 4 Postman result for every case and variant: the 61 cases contain 101 checked variants, and exactly the 32 variants that failed in Week 4 fail here, each with the same symptom. None of these checks is in the smoke subset. Run them as their own tier with `-m api` (Section 5.1).

| Auto ID | Script :: test | Manual case(s) | Requirement | Technique | Checks | Defect | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-AUT-029 | test_06_api :: test_api_register_valid_account | TC-API-001 | REQ-001 | EP / API functional | 1 | - | Pass |
| TC-AUT-030 | test_06_api :: test_api_username_valid_length_boundaries | TC-API-002 | REQ-001 | BVA / API | 2 | - | 2 Pass |
| TC-AUT-031 | test_06_api :: test_api_invalid_username_partitions | TC-API-003 | REQ-001 | EP + BVA / API negative | 4 | - | 4 Pass |
| TC-AUT-032 | test_06_api :: test_api_password_length_7_rejected | TC-API-004 | REQ-001 | BVA / API negative | 1 | - | Pass |
| TC-AUT-033 | test_06_api :: test_api_password_length_8_accepted | TC-API-005 | REQ-001 | BVA / API | 1 | DEF-001 | Fail (known) |
| TC-AUT-034 | test_06_api :: test_api_missing_password_rejected | TC-API-006 | REQ-001 | EP / API negative | 1 | - | Pass |
| TC-AUT-035 | test_06_api :: test_api_username_wrong_json_type | TC-API-007 | REQ-001, REQ-009 | EP (data type) / API negative | 1 | DEF-018 | Fail (known) |
| TC-AUT-036 | test_06_api :: test_api_duplicate_username_rejected | TC-API-008 | REQ-001 | EP / API negative | 1 | DEF-016 | Fail (known) |
| TC-AUT-037 | test_06_api :: test_api_login_valid_credentials | TC-API-009 | REQ-002 | Decision table (valid/valid) / API | 1 | - | Pass |
| TC-AUT-038 | test_06_api :: test_api_login_invalid_credentials | TC-API-010 | REQ-002 | Decision table / API negative | 3 | - | 3 Pass |
| TC-AUT-039 | test_06_api :: test_api_protected_endpoints_require_session | TC-API-011 | REQ-002, REQ-009 | EP (unauthenticated) / API negative | 6 | - | 6 Pass |
| TC-AUT-040 | test_06_api :: test_api_categories_require_session | TC-API-012 | REQ-009 | EP (unauthenticated) / API negative | 1 | DEF-023 | Fail (known) |
| TC-AUT-041 | test_06_api :: test_api_list_categories | TC-API-013 | REQ-009 | API functional | 1 | - | Pass |
| TC-AUT-042 | test_06_api :: test_api_create_task_with_all_fields | TC-API-014 | REQ-003 | EP (valid) / API functional | 1 | - | Pass |
| TC-AUT-043 | test_06_api :: test_api_create_title_only_task | TC-API-015 | REQ-003 | EP (valid, optional fields omitted) / API | 1 | - | Pass |
| TC-AUT-044 | test_06_api :: test_api_title_required | TC-API-016 | REQ-003 | EP (invalid) / API negative | 3 | - | 3 Pass |
| TC-AUT-045 | test_06_api :: test_api_non_json_body_rejected | TC-API-017 | REQ-009 | EP (invalid format) / API negative | 1 | - | Pass |
| TC-AUT-046 | test_06_api :: test_api_wrong_json_types_on_create | TC-API-018 | REQ-003, REQ-009 | EP (data type) / API negative | 3 | DEF-018 | 3 Fail (known) |
| TC-AUT-047 | test_06_api :: test_api_invalid_due_date_on_create | TC-API-019 | REQ-003, REQ-006 | EP (invalid) / API negative | 3 | DEF-015 | 3 Fail (known) |
| TC-AUT-048 | test_06_api :: test_api_invalid_category_on_create | TC-API-020 | REQ-003 | EP (invalid) / API negative | 2 | DEF-019 | 2 Fail (known) |
| TC-AUT-049 | test_06_api :: test_api_urgency_boundaries | TC-API-021 | REQ-006 | BVA / API | 5 | DEF-002 | 4 Pass, TC-API-021b Fail (known) |
| TC-AUT-050 | test_06_api :: test_api_read_own_task | TC-API-022 | REQ-003 | API functional | 1 | - | Pass |
| TC-AUT-051 | test_06_api :: test_api_read_missing_task | TC-API-023 | REQ-003, REQ-009 | EP (invalid id) / API negative | 1 | - | Pass |
| TC-AUT-052 | test_06_api :: test_api_read_another_users_task | TC-API-024 | REQ-008 | EP (foreign id) / API negative | 1 | - | Pass |
| TC-AUT-053 | test_06_api :: test_api_non_integer_task_id | TC-API-025 | REQ-009 | EP (invalid type) / API negative | 1 | - | Pass |
| TC-AUT-054 | test_06_api :: test_api_filter_by_category | TC-API-026 | REQ-005 | EP / API functional | 1 | - | Pass |
| TC-AUT-055 | test_06_api :: test_api_filter_by_status | TC-API-027 | REQ-005 | EP / API functional | 2 | - | 2 Pass |
| TC-AUT-056 | test_06_api :: test_api_title_search | TC-API-028 | REQ-005 | EP / API functional | 1 | - | Pass |
| TC-AUT-057 | test_06_api :: test_api_combined_filters | TC-API-029 | REQ-005 | Decision table / API functional | 1 | - | Pass |
| TC-AUT-058 | test_06_api :: test_api_search_with_apostrophe | TC-API-030 | REQ-005 | EP (special character) / API negative | 1 | DEF-017 | Fail (known) |
| TC-AUT-059 | test_06_api :: test_api_pagination | TC-API-031 | REQ-005, REQ-009 | BVA / API functional | 1 | - | Pass |
| TC-AUT-060 | test_06_api :: test_api_invalid_pagination | TC-API-032 | REQ-009 | EP + BVA (invalid) / API negative | 3 | DEF-022 | 3 Fail (known) |
| TC-AUT-061 | test_06_api :: test_api_task_list_scoped_to_user | TC-API-033 | REQ-008 | EP / API | 1 | - | Pass |
| TC-AUT-062 | test_06_api :: test_api_partial_update | TC-API-034 | REQ-003 | API functional | 1 | - | Pass |
| TC-AUT-063 | test_06_api :: test_api_complete_and_reopen | TC-API-035 | REQ-004 | State transition (Open -> Done -> Open) / API | 1 | - | Pass |
| TC-AUT-064 | test_06_api :: test_api_invalid_values_on_update | TC-API-036 | REQ-003, REQ-009 | EP (invalid) / API negative | 6 | DEF-015, DEF-018, DEF-019, DEF-020 | 6 Fail (known) |
| TC-AUT-065 | test_06_api :: test_api_update_another_users_task | TC-API-037 | REQ-008 | EP (foreign id) / API negative | 1 | - | Pass |
| TC-AUT-066 | test_06_api :: test_api_update_missing_task | TC-API-038 | REQ-009 | EP (invalid id) / API negative | 1 | - | Pass |
| TC-AUT-067 | test_06_api :: test_api_delete_own_task | TC-API-039 | REQ-003 | State transition (exists -> deleted) / API | 1 | - | Pass |
| TC-AUT-068 | test_06_api :: test_api_delete_another_users_task | TC-API-040 | REQ-008 | EP (foreign id) / API negative | 1 | DEF-014 | Fail (known) |
| TC-AUT-069 | test_06_api :: test_api_delete_missing_task | TC-API-041 | REQ-009 | EP (invalid id) / API negative | 1 | DEF-021 | Fail (known) |
| TC-AUT-070 | test_06_api :: test_api_dashboard_counts | TC-API-042 | REQ-007 | API functional (oracle: independent count) | 1 | - | Pass |
| TC-AUT-071 | test_06_api :: test_api_dashboard_due_today_not_overdue | TC-API-043 | REQ-006, REQ-007 | BVA / API | 1 | DEF-002 | Fail (known) |
| TC-AUT-072 | test_06_api :: test_api_dashboard_scoped_to_user | TC-API-044 | REQ-008 | EP / API | 1 | - | Pass |
| TC-AUT-073 | test_06_api :: test_api_unsupported_method | TC-API-045 | REQ-009 | EP (invalid method) / API negative | 1 | - | Pass |
| TC-AUT-074 | test_07_web_forms :: test_web_register_through_form | TC-WEB-001 | REQ-001 | Workflow / web | 1 | - | Pass |
| TC-AUT-075 | test_07_web_forms :: test_web_registration_validated_on_server | TC-WEB-002 | REQ-001 | Client-server validation / EP | 3 | - | 3 Pass |
| TC-AUT-076 | test_07_web_forms :: test_web_login_through_form | TC-WEB-003 | REQ-002 | Decision table / web | 2 | - | 2 Pass |
| TC-AUT-077 | test_07_web_forms :: test_web_protected_pages_redirect_when_logged_out | TC-WEB-004 | REQ-002 | EP (unauthenticated) / web | 6 | - | 6 Pass |
| TC-AUT-078 | test_07_web_forms :: test_web_created_task_matches_api | TC-WEB-005 | REQ-003 | Workflow / UI vs API comparison | 1 | - | Pass |
| TC-AUT-079 | test_07_web_forms :: test_api_created_task_matches_web_list | TC-WEB-006 | REQ-003, REQ-006 | Workflow / API vs UI comparison | 1 | - | Pass |
| TC-AUT-080 | test_07_web_forms :: test_web_edit_matches_api | TC-WEB-007 | REQ-003 | Workflow / UI vs API comparison | 1 | - | Pass |
| TC-AUT-081 | test_07_web_forms :: test_web_toggle_matches_api | TC-WEB-008 | REQ-004 | State transition / UI vs API comparison | 1 | - | Pass |
| TC-AUT-082 | test_07_web_forms :: test_web_delete_matches_api | TC-WEB-009 | REQ-003 | Workflow / UI vs API comparison | 1 | - | Pass |
| TC-AUT-083 | test_07_web_forms :: test_web_blank_title_validated_on_server | TC-WEB-010 | REQ-003 | Client-server validation / EP | 2 | DEF-003 | 2 Fail (known) |
| TC-AUT-084 | test_07_web_forms :: test_web_due_date_validated_on_server | TC-WEB-011 | REQ-003, REQ-006 | Client-server validation / EP | 2 | DEF-015 | 2 Fail (known) |
| TC-AUT-085 | test_07_web_forms :: test_web_category_validated_on_server | TC-WEB-012 | REQ-003 | Client-server validation / EP | 1 | DEF-019 | Fail (known) |
| TC-AUT-086 | test_07_web_forms :: test_web_actions_on_another_users_task | TC-WEB-013 | REQ-008 | EP (foreign id) / UI vs API comparison | 1 | - | Pass |
| TC-AUT-087 | test_07_web_forms :: test_web_dashboard_matches_api | TC-WEB-014 | REQ-007 | UI vs API comparison | 1 | - | Pass |
| TC-AUT-088 | test_07_web_forms :: test_web_search_with_apostrophe | TC-WEB-015 | REQ-005 | EP (special character) / UI vs API comparison | 1 | - | Pass |
| TC-AUT-089 | test_07_web_forms :: test_web_duplicate_username_rejected | TC-WEB-016 | REQ-001 | EP / web negative | 1 | DEF-016 | Fail (known) |
| **Total** | | | | | **101** | | **69 Pass, 32 Fail (known)** |

#### 3.4 Reverse check: every Week 4 case is automated

| Requirement | Week 4 cases | Automated by |
| --- | --- | --- |
| REQ-001 Registration | TC-API-001 to 008; TC-WEB-001, 002, 016 | TC-AUT-029 to 036, 074, 075, 089 |
| REQ-002 Login and access | TC-API-009 to 011; TC-WEB-003, 004 | TC-AUT-037 to 039, 076, 077 |
| REQ-003 Task CRUD | TC-API-014 to 016, 018 to 020, 022, 023, 034, 036, 039; TC-WEB-005 to 007, 009 to 012 | TC-AUT-042 to 044, 046 to 048, 050, 051, 062, 064, 067, 078 to 080, 082 to 085 |
| REQ-004 Complete/reopen | TC-API-035; TC-WEB-008 | TC-AUT-063, 081 |
| REQ-005 Filters/search | TC-API-026 to 031; TC-WEB-015 | TC-AUT-054 to 059, 088 |
| REQ-006 Urgency | TC-API-019, 021, 043; TC-WEB-006, 011 | TC-AUT-047, 049, 071, 079, 084 |
| REQ-007 Dashboard | TC-API-042, 043; TC-WEB-014 | TC-AUT-070, 071, 087 |
| REQ-008 Account separation | TC-API-024, 033, 037, 040, 044; TC-WEB-013 | TC-AUT-052, 061, 065, 068, 072, 086 |
| REQ-009 API contract | TC-API-007, 011 to 013, 017, 018, 023, 025, 031, 032, 036, 038, 041, 045 | TC-AUT-035, 039 to 041, 045, 046, 051, 053, 059, 060, 064, 066, 069, 073 |

All 61 of 61 Week 4 cases (100%) are automated, and REQ-009 is now covered as well as REQ-001 to REQ-008.

#### 3.5 Deviations from the Week 4 procedure

| Case | Difference from the Postman case | Why it does not weaken the check |
| --- | --- | --- |
| All | Each check registers its own users, instead of one set of users per Postman folder | Removes the order dependence that DEF-015 forced on Week 4 (folder 99 had to run last). |
| TC-API-019, 036f; TC-WEB-011 | Fresh users per invalid-date variant, so each variant starts from a user whose list still loads | In Week 4, variants b and c ran on a user already broken by variant a. Here each variant shows the full symptom on its own. |
| TC-API-010, TC-API-001, TC-API-009 | Also check whether a session was started (`GET /api/tasks` is 200 after a valid login and 401 after a failed one) | Adds the "starts a session" / "no session" part of the Week 4 objective at no extra cost. |
| TC-API-031 | Five tasks created by the check itself | The Week 4 precondition says three tasks, but its expected results (pages of 2, 2 and 1, "all five tasks") need five. |
| TC-WEB-014 | A four-task set (today-1, today+1, no date, one completed) compared between the web page and the API | Week 4 used "a similar four-task set". No task is due today, so the comparison does not depend on DEF-002. |
| TC-API-002a | The 3-character username comes from a per-run counter (`u` + two base-36 characters) | A 3-character name cannot include the time. It is unique within a run on the isolated database. |

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

#### 4.5 Execution runs: Week 4 cases added

| Item | Value |
| --- | --- |
| Date / timezone | 2026-11-27, Malay Peninsula Standard Time (UTC+8) |
| Application commit | `f34f7e0`. `app.py`, `helpers.py`, `templates/` and `static/` are identical to `9cc1f34` (runs 1-6) and to `fc0767f` (the Week 4 Postman run) |
| Environment | Windows 11 Home 10.0.26200, Python 3.14.7, pytest 9.2.0, Selenium 4.53.0, Microsoft Edge 158.0.4370.45 (headless, 1366x900). Edge had updated from 157 since runs 1-6 |
| Target | Isolated `app.py` on port 5006 with a new temporary SQLite database for each run |

| # | Run folder (`evidences/runs/`) | Scope | Checks | Pass | Fail (known defect) | Fail (new) | Wall time | Exit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | [20261127-144603-edge-full-w4-run1](evidences/runs/20261127-144603-edge-full-w4-run1/results.md) | Full regression (browser + Week 4) | 166 | 127 | 39 | 0 | 84.4 s | 0 |
| 8 | [20261127-144908-chrome-api-run2](evidences/runs/20261127-144908-chrome-api-run2/results.md) | `-m api` (no browser) | 101 | 69 | 32 | 0 | 21.3 s | 0 |
| 9 | [20261127-144931-chrome-api-run3](evidences/runs/20261127-144931-chrome-api-run3/results.md) | `-m api` (repeat) | 101 | 69 | 32 | 0 | 21.4 s | 0 |
| 10 | [20261127-144953-chrome-api-defects-as-failures](evidences/runs/20261127-144953-chrome-api-defects-as-failures/results.md) | `-m api --defects-as-failures` | 101 | 69 | - | 32 | 21.2 s | 1 |

Runs 8-10 start no browser; their folder name carries the default `--browser` value, and their `results.md` records the browser as `none (no browser check selected)`.

**Results.** In run 7 the 65 browser and rule checks gave the same results as runs 1-3 (58 Pass, 7 Fail (known)), so the new Edge version changed nothing. The 101 Week 4 checks gave 69 Pass and 32 Fail (known). These are the same verdicts as the Week 4 Postman run (2026-11-24) for every case and every variant.

**Stability.** The 101 Week 4 checks gave identical results in runs 7, 8 and 9. Run 10 reports the same 32 checks as plain failures (exit 1). The Week 4 checks take about 21 s, most of it password hashing for the 90 registration requests they send.

**Known defects re-tested by the Week 4 checks** (symptoms from run 7 `results.md`; each matches the Week 4 defect record):

| Defect | Automated checks | Symptom observed on 2026-11-27 | Status after retest |
| --- | --- | --- | --- |
| DEF-001 Eight-character password rejected | TC-AUT-033 [TC-API-005] | `400 {"error": "invalid password"}` for `abcd1234` | Open, reproduced through the API |
| DEF-002 Today counted as overdue | TC-AUT-049 [TC-API-021b], TC-AUT-071 [TC-API-043] | `urgency 'Overdue'` for a task due today; `Overdue counter is 2, expected 1` | Open, reproduced through the API |
| DEF-003 Blank title saved by the web form | TC-AUT-083 [TC-WEB-010a, b] | `302 redirect to /` and the blank-titled task saved, for both `""` and `"   "` | Open, reproduced |
| DEF-014 API deletes another user's task | TC-AUT-068 [TC-API-040] | `intruder DELETE returned 200; owner's GET afterwards returned 404` | Open, reproduced |
| DEF-015 Invalid due date saved, then 500s | TC-AUT-047 [TC-API-019a-c], TC-AUT-064 [TC-API-036f], TC-AUT-084 [TC-WEB-011a, b] | Create returns 500 HTML and the list/dashboard then return `(500, 500)`; the web form redirects with 302 | Open, reproduced |
| DEF-016 Duplicate username accepted | TC-AUT-036 [TC-API-008], TC-AUT-089 [TC-WEB-016] | `201` with a new id for the existing name; web form `302 redirect to /` | Open, reproduced |
| DEF-017 Apostrophe in API search causes 500 | TC-AUT-058 [TC-API-030] | `500 text/html` for `q=O'Brien` | Open, reproduced |
| DEF-018 Wrong JSON types cause 500 | TC-AUT-035 [TC-API-007], TC-AUT-046 [TC-API-018a-c], TC-AUT-064 [TC-API-036d] | `500 text/html` instead of 400 JSON in all five variants | Open, reproduced |
| DEF-019 Unknown category accepted | TC-AUT-048 [TC-API-020a, b], TC-AUT-064 [TC-API-036e], TC-AUT-085 [TC-WEB-012] | `201` with `category_id: 999` / `"abc"`; PUT 200; web form 302 | Open, reproduced |
| DEF-020 Update skips title validation; `"false"` means done | TC-AUT-064 [TC-API-036a-c] | `200` and blank title stored; `{"done": "false"}` sets `completed_at` | Open, reproduced |
| DEF-021 Deleting a missing task reports success | TC-AUT-069 [TC-API-041] | `200 {"result": "ok"}` for id 999999999 | Open, reproduced |
| DEF-022 Invalid paging values accepted | TC-AUT-060 [TC-API-032a-c] | `200` with a task list for `per_page=-1`, `page=-1`, `page=abc` | Open, reproduced |
| DEF-023 Categories work without login | TC-AUT-040 [TC-API-012] | `200` with the four categories, no session | Open, reproduced |

No new defects were found. All 43 Week 4 cases that passed still pass.

#### 4.6 Seeded-fault check for the Week 4 checks

The same method as 4.4 was used, with five faults in the API code. The script now runs the browser checks for M1-M7 (`-m "not unit and not api"`, unchanged from 4.4) and the Week 4 checks for M8-M12 (`-m api`).

| Mutant | Injected fault | Requirement | Detected by | Result folder | Detected? |
| --- | --- | --- | --- | --- | --- |
| M8 | `GET /api/tasks/<id>` no longer limited to the owner | REQ-008 | TC-AUT-052 [TC-API-024]: 200 with the owner's task, expected 404 | [M8](evidences/mutation/20261127-144353-edge-mutant-M8/results.md) | Yes |
| M9 | `/api/dashboard` loses `login_required_api` | REQ-002, REQ-009 | TC-AUT-039 [TC-API-011f]: 500 HTML, expected 401 JSON | [M9](evidences/mutation/20261127-144415-edge-mutant-M9/results.md) | Yes |
| M10 | DEF-014 and DEF-021 *fixed*: delete limited to the owner, 404 when nothing was deleted | REQ-008, REQ-009 | TC-AUT-068 [TC-API-040] and TC-AUT-069 [TC-API-041] report **Retest (XPASS)** | [M10](evidences/mutation/20261127-144434-edge-mutant-M10/results.md) | Yes (fixes flagged) |
| M11 | API `status=done` filter ignored | REQ-005 | TC-AUT-055 [TC-API-027b]: every task returned, expected only `Report archive` | [M11](evidences/mutation/20261127-144511-edge-mutant-M11/results.md) | Yes |
| M12 | `POST /api/login` accepts any password | REQ-002 | TC-AUT-038 [TC-API-010a]: 200, expected 401 | [M12](evidences/mutation/20261127-144532-edge-mutant-M12/results.md) | Yes |

**All 5 seeded faults were detected.** Each failed exactly one check, the one traced to the broken behaviour, and the other 100 checks kept their baseline result. M10 also shows that a partial fix is not enough. An earlier draft of M10 only limited the delete to the owner, and TC-API-040 still failed because the intruder still got 200 instead of the 404 Week 4 specifies. The final M10 fixes both, and both checks report Retest.

---

## Task 5

### Regression suite and automation reflection

#### 5.1 The focused regression suite

| Tier | Selection | Checks | Time | When to run |
| --- | --- | --- | --- | --- |
| **Smoke** | `-m smoke`: register, log in, access control (3 pages), logout, create, delete, complete/reopen, combined filter, account separation | 11 | about 14 s | Every code change or commit, before anything else |
| **Rules** | `-m unit`: username, password and urgency boundaries on `helpers.py` | 17 | under 1 s | Every change to `helpers.py`, and in any environment without a browser |
| **Web/API** | `-m api`: Week 4 REST API and web form checks over HTTP, no browser | 101 | about 21 s | Every change to `app.py` (routes, validation, queries), together with smoke. Also in any environment without a browser |
| **Full regression** | All checks | 166 | about 85 s | Before merging a branch, after any defect fix, and before each weekly submission |
| **Defect view** | Full suite with `--defects-as-failures` | 166 | about 85 s | When reporting quality metrics (Week 8), so known defects count as failures |

The suite is *focused*: it has one check per manual case or BVA/decision-table row, and together these cover all nine requirements (REQ-009 since the Week 4 cases were added) and every open functional defect. Visual, usability and accessibility checks were left out (Task 1.3). They would make the suite slower and more brittle without adding regression value.

**Maintenance rules**

1. A new manual case that meets the Task 1.2 rule gets a `TC-AUT` ID, `manual`/`req` markers and a row in Task 3, all in the same commit.
2. When a defect is logged, add a check that fails because of it and mark it `known_defect("DEF-nnn")`. When the defect is fixed, the strict XPASS shows `Retest`. Retest the defect, close it, and remove the marker.
3. Never edit an expected result to make a run pass. Change it only if the requirement itself changes, and record that change in the RTM (Week 7).
4. A template change that breaks a locator is fixed in `pages.py` only. A change to the table or error markup that the Week 4 checks read is fixed in the HTML readers in `api_checks.py` only.
5. Week 4 checks use only the `api` marker plus their traceability markers, and every one of them creates its own accounts. A new HTTP-level check follows the same pattern, so it runs without a browser and in any order.

#### 5.2 Benefits observed

| Benefit | Evidence from this phase |
| --- | --- |
| **Speed and repeatability** | All 44 Week 1 cases plus 10 Week 3 functional checks run in about 37 s, with no manual data preparation. Week 1 needed dedicated accounts, fixed calendar dates and a screenshot for each case. |
| **Consistency** | Three consecutive runs gave identical results for all 65 checks (Section 4.1), and three runs gave identical results for all 101 Week 4 checks (Section 4.5). Every run uses the same inputs, the same clean database and the same expected results. |
| **Detects real regressions** | All 12 seeded faults were detected, each by a check traced to the matching requirement (Sections 4.4 and 4.6). |
| **Defect retesting at no extra effort** | DEF-001, 002, 003, 005 and DEF-014 to 023 are retested on every run. A fix shows up automatically as `Retest` (M6, M10). |
| **Faster than the manual API run** | The 61 Week 4 cases (101 variants) run in about 21 s from the command line, with no Postman session switching and no required folder order. |
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
| **Only one browser executed** (Edge 157, then Edge 158 on Windows) | Chrome and Firefox were not run in this phase | `--browser chrome/firefox` is supported. Cross-browser behaviour was covered in Week 3 (C01-C04). |
| **No visual, layout, usability or accessibility assertions** | DEF-004 and DEF-006 to 013 are not covered by regression checks | Recommendation: run the Week 3 axe scan as a scheduled job (Section 5.4). Visual review stays manual. |
| **Week 4 web checks do not render pages** | TC-WEB checks post forms and read the returned HTML, but run no JavaScript and use no browser | The same behaviour is checked through a real browser by TC-AUT-001 to 025. The Week 4 checks cover what a browser cannot send: bypassed `required` fields, text in date fields and unknown category ids. |
| **Expected error codes are a team assumption** (Week 4 0.3) | The README defines no error contract, so 400, 404 and 409 come from HTTP conventions | Recorded as a Week 4 assumption. If the team agrees a different contract, change the expected codes in one place (the Week 4 test basis) and record the change in the RTM (maintenance rule 3). |
| **Automation checks only what it asserts** | A page could pass while showing an unexpected extra element | Checks compare whole result sets (for example, exact title lists), not just whether one item is present. Exploratory manual testing is still needed. |
| **Maintenance cost** | Template or ID changes need script updates | Locators live only in `pages.py`. Where possible they use stable `name` attributes and table structure, not styling classes. |
| **First run needs network access** | Selenium Manager downloads the browser driver | Documented in setup.md. Later runs use the cached driver. |

#### 5.4 Reflection

- **What to automate.** The clearest returns came from data-driven cases with an exact expected result, namely the BVA, EP and decision-table rows. One parametrized function replaces six to eight manual executions and their screenshots. Cases that need human judgement (layout, heuristics, usability) scored low and were left manual. Automated versions of them would either break on harmless changes or pass without checking anything meaningful.
- **Automation needs its own design work.** The most important early decisions were not about Selenium itself. They were the isolated database, seeding through the API, relative dates and explicit waits. These are why three runs in a row gave identical results and why each seeded fault showed up as a specific failure.
- **Handling known defects.** Each assertion keeps the specified result, and open defects are marked as strict xfail. The suite therefore stays green when nothing new has broken, but it cannot hide a defect: `--defects-as-failures` and the results table always list them, and a fix is reported automatically for retest.
- **Layering.** Browser checks prove that a rule is used by the pages. Unit checks prove the rule itself, quickly and without depending on the current date. Having both makes a fault easier to locate: in M5, the UI urgency check and the dashboard check failed together, which pointed to `helpers.py`.
- **Adding Week 4.** The Week 4 cases were the easiest to automate, because Postman had already turned every expected result into an exact status-and-body check. The main design work was making each check independent. In Postman, a single user broken by DEF-015 forced a folder order. Here every check creates its own users. The seeded faults (4.6) each failed exactly one Week 4 check, so a red result points straight at one endpoint and one rule. M10 also showed that the suite holds a fix to the *specified* result: limiting the delete to the owner while still answering 200 is not yet a fix for TC-API-040.
- **Limits.** A green run means only that the checked behaviours did not regress. It says nothing about usability, accessibility, security or performance. The missing ownership check in `DELETE /api/tasks/<id>`, flagged here as a candidate on 2026-11-20, was confirmed by Week 4 as DEF-014 and is now retested on every run (TC-AUT-068). Week 5 (security and performance) should add its confirmed findings using the same markers. Attack payloads and load tests should stay in their own Week 5 scripts, and only the functional symptom of each confirmed defect should be added here. The Week 3 axe scan should run as a scheduled job alongside this suite, not inside it.
