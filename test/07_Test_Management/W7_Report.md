# Week 7 - Test Planning, Traceability and Defect Management

| Item | Value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance, September 2026 |
| Lab group | Wednesday Lab - Group 2 |
| Phase owner | Ameera Alysha binti Azlan |
| Consolidation date | 2026-11-27, covering Weeks 1-6 |
| Build under test | `app.py` SHA-256 `050b4ee4...f30f`, `helpers.py` `bf914033...6d80`, `templates/`, `static/`; unchanged throughout the project |

## Deliverable checklist

- [x] [Formal Software Test Plan](#1-software-test-plan)
- [x] [Test Strategy](#2-test-strategy)
- [x] [Updated RTM](#3-requirements-traceability) - [test/rtm.md](../rtm.md), REQ-001 to REQ-014
- [x] [Master test-case repository](#4-master-test-case-repository) - [test/master_test_cases.md](../master_test_cases.md), 302 cases
- [x] [Consolidated defect log](#5-defect-management) - [test/consolidated_defect_logs.md](../consolidated_defect_logs.md), DEF-001 to DEF-037
- [x] [Test execution/regression status](#6-execution-and-regression-status)

The RTM, repository and defect log are project-level files in `test/`, consolidated from the weekly records.

## 1. Software Test Plan

### 1.1 Objective: why we test

1. Evaluate whether PyTodo Pro meets its documented and agreed requirements (REQ-001 to REQ-014).
2. Find, record and classify defects with enough evidence for a developer to reproduce them.
3. Measure the quality of the functional, API, GUI, usability, accessibility, security and performance attributes.
4. Provide a repeatable regression suite that re-tests every open functional defect.
5. Report residual risk and prioritised recommendations (Week 8), without claiming the software is defect-free.

### 1.2 Scope: what will and will not be tested

Test items: PyTodo Pro (Flask + SQLite), `app.py` (482 lines), `helpers.py`, `templates/`, `static/`, with the hashes in the header; 6 web pages and 9 JSON endpoints under `/api`; the application `README.md`, `helpers.py` docstrings and interface text as the test basis.

| In scope | Out of scope |
| --- | --- |
| Registration, login/logout, protected pages, task CRUD, complete/reopen, filters and search, urgency, dashboard, user separation | Changing or fixing the application |
| JSON REST API contract (status codes, JSON errors, authentication) | Production deployment, HTTPS, real network conditions |
| GUI, compatibility (2 OS × 2 browser engines, emulated tablet/phone), usability, WCAG 2.2 A/AA subset | Real mobile devices, Safari/WebKit, Edge, screen readers |
| Security threats from a STRIDE model, tested safely on localhost | Uncontrolled penetration testing, password cracking, network attacks |
| Load, stress and data-volume behaviour on a local machine | Long soak tests, production-capacity claims |
| Statement coverage of `helpers.py` and selected `app.py` functions | Python standard library and Flask internals |

### 1.3 Approach: how we test

The approach is risk-based. Each feature is rated on likelihood (how likely it is to be wrong) and impact (how much damage a failure causes), each on a 1-3 scale and judged separately; the score is likelihood × impact. Higher scores receive more techniques and more cases.

| Score | Priority | Test depth |
| --- | --- | --- |
| 6-9 | High | Deep: several techniques, negative and security cases, automated regression |
| 3-4 | Medium | Standard: main flows with key negative cases |
| 1-2 | Low | Light: smoke or exploratory checks |

Product risk profile (ratings from Week 1, re-assessed with the evidence of Weeks 1-6; cases from the [RTM](../rtm.md)):

| Risk | Area | L | I | Score | Priority | Cases (passed) |
| --- | --- | ---: | ---: | ---: | --- | ---: |
| R-01 | Registration wrong (REQ-001) | 3 | 2 | 6 | High | 47 (35) |
| R-02 | Login, sessions or access control wrong (REQ-002) | 3 | 3 | 9 | High | 33 (31) |
| R-03 | Task create/edit/delete or validation wrong (REQ-003) | 3 | 3 | 9 | High | 84 (63) |
| R-04 | Complete/reopen wrong (REQ-004) | 1 | 2 | 2 | Low | 12 (11) |
| R-05 | Filters or search wrong (REQ-005) | 3 | 3 | 9 | High | 24 (22) |
| R-06 | Due-date urgency wrong (REQ-006) | 3 | 2 | 6 | High | 23 (11) |
| R-07 | Dashboard counts wrong (REQ-007) | 2 | 2 | 4 | Medium | 12 (7) |
| R-08 | One user reaches another user's tasks (REQ-008) | 3 | 3 | 9 | High | 14 (12) |
| R-09 | API contract wrong (REQ-009) | 3 | 2 | 6 | High | 28 (16) |
| R-10 | GUI, layout or accessibility poor (REQ-010, 012) | 3 | 2 | 6 | High | 48 (28) |
| R-11 | Security configuration weak (REQ-013) | 3 | 3 | 9 | High | 24 (6) |
| R-12 | Slow or failing under load (REQ-014) | 2 | 2 | 4 | Medium | 8 (6) |

Product likelihood × impact matrix:

| Likelihood ↓ / Impact → | Low (1) | Medium (2) | High (3) |
| --- | --- | --- | --- |
| **High (3)** | 3 | 6: R-01, R-06, R-09, R-10 | 9: R-02, R-03, R-05, R-08, R-11 |
| **Medium (2)** | 2 | 4: R-07, R-12 | 6 |
| **Low (1)** | 1 | 2: R-04 | 3 |

### 1.4 Entry criteria: when we start testing

A phase starts when all of the following hold:

- The application files match the hashes in the header (not modified by the team).
- `python -m pip install -r requirements.txt` succeeds and the app starts locally on `127.0.0.1`; the login page loads (smoke test).
- Test cases with expected results are written in the Test Case Template before execution.
- Test accounts and data for the phase are prepared (section 1.6).
- The tools of the phase are installed and their versions recorded.

### 1.5 Exit criteria: when we stop testing

| Criterion | Result (2026-11-27) | Met |
| --- | --- | --- |
| 100% of planned cases executed; each Pass, Fail or Blocked with a reason | 302 of 302; 1 Blocked (PERF-06b, test-machine port limit) | Yes |
| Every Fail linked to a defect or usability observation | 86 of 86 (83 to defects; TC-GUI-017, 018, 022 to USA-OBS-001 to 003) | Yes |
| Every requirement traced to at least one executed case | 14 of 14 (REQ-011 by the usability session) | Yes |
| Every case traced to at least one requirement | 302 of 302 | Yes |
| Every defect recorded in the Defect Report Template with severity, priority and evidence | 37 of 37 | Yes |
| Statement coverage of `helpers.py` at least 95% | 100% | Yes |
| Full regression suite on the final build with 0 new failures | Week 6 run 7: 0 new failures | Yes |
| Residual risks and a release recommendation stated | [Week 8 report](../08_Final_QA_Report/W8_Report.md) | Yes |

### 1.6 Environment and test data: what we need

| Item | Description |
| --- | --- |
| Hardware / OS | Weeks 1, 2, 3 (C01-C04) and 5 performance: MacBook Air M4, macOS 26.5.2 · Weeks 3 (C05-C06) and 4: Acer Nitro 5 AN515-45, Windows 11 25H2 · Week 5 security: desktop PC, Ryzen 5 5500, Windows 64-bit · Week 6: Windows 11 Home 10.0.26200 |
| Application runtime | Flask development server on `127.0.0.1`; Python 3.14.7 (3.12.10 for Week 5 security), Flask 3.0.3 |
| Tools | pytest and pytest-cov (unit, integration, regression); Playwright, axe-core and Lighthouse (GUI, compatibility, accessibility); Postman and Newman (web and API); Selenium WebDriver (regression UI); pip-audit and bandit (security); Apache JMeter 5.6.3 (performance); Git and GitHub (version control, evidence) |
| Browsers | Chrome 157.0.8103.80 on macOS and Windows; Playwright Firefox 159.0; Edge 157/158 (Week 6) |
| Test data | Synthetic accounts only (`w1d_*`, `w3*`, `w4*`, `w6_*`, `sec_user_*`, `perf_user_*`), password `Test12345` unless a boundary case needs another value. Controlled sets: Week 1 seven-task urgency set, Week 3 Fixture Set A, Week 4 `test_data.md`, Week 5 20 users × 50 tasks. Automated suites use a fresh temporary database per run and dates relative to the run day |
| Boundary values | Username length 2/3/4 and 19/20/21; password length 7/8/9; due date yesterday/today/tomorrow/+2/+3 days; 1/5/10/25/50 load users, stress steps to 200 users; 50/500/2,000 tasks per user |

### 1.7 Roles and schedule: who does what and when

| Member | Role |
| --- | --- |
| Eu Kwan Ik | QA/Test Lead |
| Mohamad Shukri Bin Abdul Ajed | Test Design Coordinator |
| Darius Lee Shin | Automation/Tool Coordinator |
| Ameera Alysha binti Azlan | Defect & Metrics Coordinator |
| Wan Haziqah Binti Wan Hanafi | Test Assistant / Tester |

| Phase | Activity | Owner | Executed |
| --- | --- | --- | --- |
| Week 1 | Application analysis, black-box testing | Darius Lee Shin | 2026-10-18 |
| Week 2 | White-box testing and coverage | Darius Lee Shin | 2026-10-26 |
| Week 3 | GUI, compatibility, usability, accessibility | Darius Lee Shin | 2026-11-18 to 2026-11-26 |
| Week 4 | Web and API testing | Mohamad Shukri Bin Abdul Ajed | 2026-11-24 |
| Week 5 | Security and performance testing | Wan Haziqah Binti Wan Hanafi | 2026-11-25 to 2026-11-27 |
| Week 6 | Test automation and regression | Eu Kwan Ik | 2026-11-20, 2026-11-27 |
| Week 7 | Test plan, RTM, defect consolidation | Ameera Alysha binti Azlan | 2026-11-27 |
| Week 8 | Metrics and final quality evaluation | Darius Lee Shin, Mohamad Shukri Bin Abdul Ajed | 2026-11-27 |

### 1.8 Risks and contingency: what could go wrong with the testing itself

| ID | Project risk | L | I | Score | Contingency | Owner |
| --- | --- | ---: | ---: | ---: | --- | --- |
| P1 | Phases run on different machines and dates, so results are not directly comparable | 3 | 2 | 6 | Environment recorded in every report header; application hashes checked unchanged | Darius |
| P2 | Date-dependent behaviour (urgency) makes tests fail on another day | 3 | 2 | 6 | Dates relative to the run day; fixed dates injected in unit checks | Darius |
| P3 | Work lost or overwritten between members | 2 | 3 | 6 | Git with one branch per phase, merged into `main` by reviewed pull request | Eu Kwan Ik |
| P4 | Test machine limits under stress fail the load generator before the app | 2 | 2 | 4 | Stepped stress with short steps; client errors separated from server errors | Haziqah |
| P5 | Shared database causes test-data collisions | 2 | 2 | 4 | Isolated temporary database for every automated run | Eu Kwan Ik |
| P6 | Expected API error codes unclear (no error contract in the README) | 3 | 1 | 3 | Team decision recorded as the Week 4 test basis | Shukri |
| P7 | A member is unavailable during a phase | 2 | 1 | 2 | Every phase has a named owner; another member reviews and can take it over | Ameera |

### 1.9 Limitations

Tests ran on a local development server only; mobile results are emulated; usability users were team members; security testing shows the presence of weaknesses, not their full exploitability; performance figures describe one MacBook, not production capacity.

## 2. Test Strategy

### 2.1 Levels and types

| Level | What is tested | Weeks | Main tools |
| --- | --- | --- | --- |
| Unit | `helpers.py` rules and selected `app.py` functions | 2, 6 | pytest |
| Integration | Functions with Flask and SQLite; decorators with real routes | 2 | pytest, Flask test client |
| System - functional | Web workflows and REST API end to end | 1, 4, 6 | Browser, Postman, Selenium, HTTP checks |
| System - non-functional | GUI, compatibility, usability, accessibility, security, performance | 3, 5 | Playwright, axe, Lighthouse, pytest, JMeter |
| Regression | Re-run of selected cases after any change | 6 | pytest tiers: smoke, rules, Web/API, full |

### 2.2 Techniques by risk

| Risk | Priority | Techniques applied | Defects found |
| --- | --- | --- | --- |
| R-01 Registration | High | EP, BVA, decision table, API negative | DEF-001, 016, 018, 027 |
| R-02 Login, sessions, access | High | Decision table, state transition, security tests | DEF-023 to 026, 028, 030 |
| R-03 Task CRUD and validation | High | EP, BVA, client-server validation, API negative | DEF-003, 015, 018 to 020, 033 |
| R-04 Complete/reopen | Low | State transition | None |
| R-05 Filters and search | High | EP, decision table, injection tests | DEF-017, 022, 029, 034 |
| R-06 Due-date urgency | High | BVA, unit rules with injected dates | DEF-002 |
| R-07 Dashboard | Medium | Independent calculation, UI vs API | DEF-002 |
| R-08 User separation | High | Foreign-id EP, cross-user API checks | DEF-014 |
| R-09 API contract | High | Status/JSON contract checks | DEF-021, 022, 023 |
| R-10 GUI, layout, accessibility | High | GUI checklist, compatibility matrix, WCAG checks | DEF-004 to 013 |
| R-11 Security configuration | High | STRIDE, code review, bandit, pip-audit | DEF-028, 031, 032, 035, 036 |
| R-12 Performance | Medium | Load, stepped stress, data volume (JMeter) | DEF-037 |

Higher-risk areas received more techniques and more cases: task CRUD/validation (R-03) has the most cases (84), and the five risks scoring 9 together account for 21 of the 37 defects, including all 4 Critical ones.

### 2.3 Automation strategy

Automate a case when it scores at least 9 of 12 on repetition, stability, criticality and regression value, and a program can check its expected result (Week 6). Manual or human-judged checks (visual layout, usability, keyboard accessibility) stay manual. Known defects are kept as strict xfail so the suite stays green yet reports any fix as Retest.

## 3. Requirements traceability

Full matrix: [test/rtm.md](../rtm.md). REQ-001 to REQ-008 come from Week 1 and REQ-009 from Week 4; REQ-010 to REQ-014 were added this week so that GUI, usability, accessibility, security and performance testing trace to stated quality requirements.

| Requirement | Cases | Pass | Fail | Blocked | Open defects |
| --- | ---: | ---: | ---: | ---: | ---: |
| REQ-001 Registration | 47 | 35 | 12 | 0 | 3 |
| REQ-002 Login, logout and protected pages | 33 | 31 | 2 | 0 | 2 |
| REQ-003 Create, view, edit and delete tasks | 84 | 63 | 21 | 0 | 7 |
| REQ-004 Complete and reopen tasks | 12 | 11 | 1 | 0 | 0 |
| REQ-005 Filters and title search | 24 | 22 | 2 | 0 | 1 |
| REQ-006 Due-date urgency | 23 | 11 | 12 | 0 | 2 |
| REQ-007 Dashboard | 12 | 7 | 5 | 0 | 1 |
| REQ-008 User task separation | 14 | 12 | 2 | 0 | 1 |
| REQ-009 JSON REST API contract | 28 | 16 | 12 | 0 | 7 |
| REQ-010 GUI and compatibility | 30 | 21 | 9 | 0 | 6 |
| REQ-011 Usability | 4 observations | - | - | - | 0 |
| REQ-012 Accessibility | 18 | 7 | 11 | 0 | 8 |
| REQ-013 Security | 24 | 6 | 18 | 0 | 18 |
| REQ-014 Performance | 8 | 6 | 1 | 1 | 1 |

A case can trace to more than one requirement, so the column totals exceed the number of cases.

## 4. Master test-case repository

[test/master_test_cases.md](../master_test_cases.md) lists all 302 cases with requirement, technique, status and defect, each linked to its full record in the weekly folder.

| Week | Area | Cases | Pass | Fail | Blocked | Not Run |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | Black-box | 44 | 40 | 4 | 0 | 0 |
| 2 | White-box | 28 | 28 | 0 | 0 | 0 |
| 3 | GUI | 22 | 14 | 8 | 0 | 0 |
| 3 | Compatibility | 8 | 7 | 1 | 0 | 0 |
| 3 | Accessibility | 18 | 7 | 11 | 0 | 0 |
| 4 | Web and API | 61 | 43 | 18 | 0 | 0 |
| 5 | Security and performance | 32 | 12 | 19 | 1 | 0 |
| 6 | Automation and regression | 89 | 64 | 25 | 0 | 0 |
| **Total** | | **302** | **215** | **86** | **1** | **0** |

Week 6 cases automate earlier manual cases, so 213 cases are distinct manual or design-level tests and 89 are their automated counterparts.

## 5. Defect management

### 5.1 Process

| Item | Rule |
| --- | --- |
| IDs | One series DEF-001 to DEF-037 across all weeks; never reused |
| Logging | Only after the failure is reproduced at least twice |
| Record | Project Defect Report Template in the `defects.md` of the week the defect was first found |
| Re-tests | Listed in the later week's "Re-tested defects" table and automated in Week 6 where possible |
| Severity | Critical: data loss, account takeover or a user locked out of their data · Major: core task blocked or security weakness with direct impact · Moderate: wrong or misleading behaviour with a workaround · Minor: cosmetic, documentation or low-impact issue |
| Priority | High: fix before release · Medium: fix in the next cycle · Low: fix when convenient |
| Lifecycle | Open -> (fix delivered) -> Retest -> Closed, or Reopened if the retest fails. No fixes were delivered during the project, so every defect is Open; the Week 6 suite reports a delivered fix automatically as Retest (XPASS) |

### 5.2 Consolidated defect log

Full log: [test/consolidated_defect_logs.md](../consolidated_defect_logs.md).

| Severity | Count | Defects |
| --- | ---: | --- |
| Critical | 4 | DEF-014, 015, 028, 029 |
| Major | 6 | DEF-005, 007, 008, 016, 017, 031 |
| Moderate | 16 | DEF-001 to 004, 006, 009, 011, 018 to 020, 024, 026, 030, 033, 034, 037 |
| Minor | 11 | DEF-010, 012, 013, 021 to 023, 025, 027, 032, 035, 036 |
| **Total** | **37** | Priority: 11 High, 13 Medium, 13 Low |

| Found in | New defects |
| --- | ---: |
| Week 1 | 3 |
| Week 2 | 0 |
| Week 3 | 10 |
| Week 4 | 10 |
| Week 5 | 14 |
| Week 6 | 0 |

Severity changes: DEF-005 was upgraded from Moderate to Major in Week 5, when a script payload in a task title was shown to execute.

## 6. Execution and regression status

### 6.1 Execution status

All 302 cases were executed: 215 Pass, 86 Fail, 1 Blocked (PERF-06b, stopped by the test machine's port limit), 0 Not Run.

### 6.2 Regression status (final build)

| Tier | Latest run | Checks | Pass | Fail (known defect) | Fail (new) | Retest (XPASS) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Full regression | Week 6 run 7, 2026-11-27 | 166 | 127 | 39 | 0 | 0 |
| Web/API | Week 6 runs 8-9, 2026-11-27 | 101 | 69 | 32 | 0 | 0 |
| Security | Week 5, 2026-11-25 | 23 | 6 | 17 | 0 | 0 |

No regression was found: every check that passed in Weeks 1-4 still passes, and 14 open functional defects are re-tested automatically on every run. Defects not covered by automated regression are the visual, accessibility and performance ones (DEF-004, DEF-006 to 013, DEF-037), which keep their Week 3 and Week 5 scripts.
