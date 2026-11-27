# Formal Software Test Plan: PyTodo Pro

| Item | Value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / Lab Group | September 2026 / Wednesday Lab - Group 2 |
| Deliverable | Project Week 7 - Test Management and Consolidation (`/07_Test_Management`) |
| Application under test | PyTodo Pro: Flask 3.0.3 + SQLite task manager, `app.py` and `helpers.py` |
| Plan version | 1.1, consolidated from Weeks 1-4 and 6; Week 5 pending |

## 1. Test objectives

1. Verify the nine requirements `REQ-001` to `REQ-009` (see Section 2.1) through the web pages and the JSON API.
2. Show which internal paths and statements were exercised in selected backend code (`app.py`) and in `helpers.py`.
3. Assess presentation quality: GUI consistency, compatibility across browsers and viewports, a WCAG 2.2 A/AA subset and usability.
4. Check the REST API contract: status codes, JSON error bodies, authentication and ownership.
5. Assess security and performance (Week 5, pending).
6. Keep a repeatable automated regression suite, and show that it detects regressions.
7. Report quality through a traceable [RTM](rtm.md), [master test-case repository](master_test_cases.md), [defect log](defect_log.md), [execution summary](execution_summary.md) and [risk register](risk_register.md).

## 2. Scope

### 2.1 In scope

| Requirement | Feature |
| --- | --- |
| `REQ-001` | Registration (username 3-20 characters, letters/digits/underscore; password at least 8 characters) |
| `REQ-002` | Login, logout and protected pages |
| `REQ-003` | Create, view, edit and delete tasks (title, description, category, due date) |
| `REQ-004` | Complete and reopen tasks |
| `REQ-005` | Category and status filters, title search, paging (API) |
| `REQ-006` | Due-date urgency: Overdue, Due Today, Due Soon (1-2 days), Upcoming (3+ days), No due date, Done |
| `REQ-007` | Dashboard counters |
| `REQ-008` | Separation of each user's tasks |
| `REQ-009` | JSON REST API contract, added in Week 4: HTTP status codes, session authentication, JSON error bodies |

There is one user role: an authenticated individual (plus the unauthenticated visitor). There is no administrator role. Categories are four seeded values: Work, Personal, Study, Urgent. Web pages: `/login`, `/register`, `/`, `/tasks/new`, `/tasks/<id>/edit`, `/dashboard`. API: nine endpoints under `/api` (register, login, tasks list/create, task read/update/delete, dashboard, categories).

### 2.2 Out of scope

- Hosting, TLS, production deployment and any production WSGI/database stack.
- Native mobile apps (tablet and phone widths are covered by browser emulation only).
- Modifying the application: defects are reported, not fixed.
- Full WCAG conformance audit, screen-reader testing, and usability testing with end users.

## 3. Test approach

Details are in [test_strategy.md](test_strategy.md). Summary by phase:

| Week | Folder | Approach | Status |
| --- | --- | --- | --- |
| 1 | `/01_Black_Box` | Black-box: EP, BVA, decision tables, state transitions; 44 cases | Complete |
| 2 | `/02_White_Box_Coverage` | Control-flow graphs and basis paths for 8 backend functions; 19 path cases run as 50 pytest instances; statement coverage measured (not branch) | Complete |
| 3 | `/03_Special_Testing` | GUI checklist (22), compatibility (8 cases x 6 configurations), accessibility (18), usability (5) | Executed except usability (Not Run); compatibility C07 blocked |
| 4 | `/04_Web_API` | Postman collection: 61 cases (190 requests, 339 checks) over 9 endpoints and the web forms; UI-versus-API comparison | Complete |
| 5 | `/05_Security_Performance` | STRIDE review and safe probing; latency and load checks. Inputs from W4: `DEF-017` (SQL built from search text), `DEF-014` (broken authorisation), `debug=True` tracebacks, `DEF-016` (duplicate usernames), no CSRF token, `per_page=-1` | **Pending** |
| 6 | `/06_Automation_Regression` | pytest + Selenium regression suite; 28 automated cases, 65 checks; 7 seeded-fault runs | Complete |

Session-cookie security flags were not tested in Week 4; they belong to Week 5.

## 4. Test environment and data

### 4.1 Environment by phase

| Phase | Platform and tools | Application |
| --- | --- | --- |
| W1 | macOS Tahoe 26.5.2; Chrome 155.0.8059.80; manual | Existing development database, dedicated test accounts, `127.0.0.1:5000` |
| W2 | Python 3.14, pytest, pytest-cov | Flask test client; `app.DATABASE` patched to a temporary file per test |
| W3 | macOS 26.5.2 (C01-C04) and Windows 11 25H2 (C05, C06); Chrome 157.0.8103.80 (macOS) and 124.0.6367.119 (Windows); Playwright Firefox 159.0 (v1572); Playwright 1.65.2, pytest 9.1.1; axe-core 4.12.1; Lighthouse 12.8.2; headless | `python app.py` on port 5000, seeded Fixture Set A |
| W4 | Windows 11 25H2; Python 3.14; Flask 3.0.3; Postman 12.38.2 Collection Runner (Newman as a free alternative) | `python -B app.py`, commit `fc0767f`, started on a deleted-and-recreated main database |
| W6 | Windows 11; Python 3.14.7; pytest 9.2.0; Selenium 4.53.0; Microsoft Edge 157 headless (Chrome and Firefox supported by option) | `run_app.py` serves the unchanged `app.py` on port 5006 with a new temporary database per run, commit `9cc1f34` |

### 4.2 Test data

- Synthetic accounts only; password `Test12345` unless a boundary value is under test.
- Date-dependent data is relative to the run day (W4 `{{today}}` variables; W6 offsets; W3 Fixture Set A), so verdicts hold on any day. W1 used fixed October 2026 dates.
- Datasets: W1 seven-task urgency/dashboard set and F1-F4 filter fixtures; W3 Fixture Set A (F1-F9, accounts A, B, C); W4 five-task list and dashboard datasets and per-folder users.
- Isolation differs by phase: temporary database per test (W2), emptied main database (W4), temporary database per run (W6), retained development database (W1).

## 5. Tools

| Purpose | Tool |
| --- | --- |
| Test runner | pytest 9.x |
| Coverage | pytest-cov / coverage.py (statement coverage) |
| API and web-form testing | Postman 12.38.2 Collection Runner; Newman |
| Browser automation | Selenium WebDriver (W6, Edge); Playwright (W3: Chrome, Firefox) |
| Accessibility | axe-core, Lighthouse, Chrome accessibility tree |
| Documentation and version control | Markdown, Git and GitHub |

## 6. Team and roles

| Student | ID | Role (course brief) | Contribution |
| --- | --- | --- | --- |
| Eu Kwan Ik | 22001674 | Test Lead | Plan, scope and schedule |
| Mohamad Shukri Bin Abd Ajed | 22006255 | Test Design Coordinator | Case design standards, RTM and master repository |
| Darius Lee Shin | 22003269 | Automation / Tool Coordinator | Playwright suites, automation testing, execution operator |
| Ameera Alysha binti Azlan | 22002998 | Defect & Metrics Coordinator | Defect log, execution summary, risk register |


## 7. Entry, suspension and exit criteria

### 7.1 Entry

- The application starts and `/login` returns 200.
- Expected results are written before execution (W3 records a review sign-off; W4 writes the checks before the run).
- Weekly test environment recorded; empty or isolated database where the phase requires it.

### 7.2 Suspension and resumption

- Suspend a phase if the application does not start or login is broken for every user. Resume when the same build starts and a smoke check passes. The application is frozen for assessment, so a fix is not expected; defects found are logged and testing continues.

### 7.3 Test-completion criteria (what Week 7 checks)

| Criterion | Status |
| --- | --- |
| Every planned case has a recorded status (Pass, Fail, Blocked or Not Run), with a reason for each Blocked and Not Run | W1, W2, W3, W4 yes; W5 pending |
| Every Fail links to a defect, or to a recorded observation | Yes for W1-W4 |
| Every defect reproduced at least twice (status `Confirmed`) | Yes, 23 of 23 |
| Evidence saved and linked | Yes for W1-W4; W6 run folders |
| All Not Run cases run | **Not met**: `TC-USA-001` to `005` pending; compatibility C07 blocked; W5 pending |
| IDs consistent across RTM, master repository and defect log | Checked in this version |

### 7.4 Quality gate (what Week 8 reports)

The application must not be modified, so "0 unresolved Critical defects" cannot be met by fixing. The gate is reported, and any exception is recorded as accepted risk.

| Gate | Result |
| --- | --- |
| 0 unresolved Critical defects | **Not met**: `DEF-014` and `DEF-015` are open. Recommendation: not ready for release; recorded as accepted risk for assessment purposes |
| Automated smoke suite 100% | Met: 11 of 11 |
| Automated regression: 0 unexpected failures | Met: 7 failures are known defects (strict xfail) |
| Regression suite detects seeded faults | Met: 7 of 7 |
| Requirements `REQ-001` to `009` mapped and executed | Mapped (RTM); executed except where W5 or usability review is pending |

## 8. Risks and limitations

Risks are scored in [risk_register.md](risk_register.md), a supporting file (not a separate deliverable). Summary of the current picture:

| Risk | Summary | Score |
| --- | --- | --- |
| R-08 | Another user's data changed: `DEF-014`, any logged-in user can delete another user's task through the API (Critical) | 6 / High, confirmed |
| R-03, R-06, R-07 | Invalid data saved; one bad due date locks a user out of their task list and dashboard (`DEF-015`, Critical); today shown as Overdue (`DEF-002`) | 6 / High; R-07 4 / Medium |
| R-01, R-05, R-09 | Inconsistent validation between web and API (`DEF-003`, `016`, `017`, `018`, `020`) and API contract failures | R-09 6 / High (proposed) |
| R-13 | Accessibility: unlabelled fields and unnamed complete button (`DEF-007`, `DEF-008`, both Major) | 6 / High (proposed) |
| R-12 | Compatibility: tablet and phone layout (`DEF-006`), narrow viewports (`DEF-004`); emulation only | 6 / High (proposed) |
| R-14 | Regression suite predates the W4 and W3 failures, so most defects are unguarded | 6 / High (proposed) |
| R-10, R-11 | Security and performance not yet assessed (Week 5) | TBD |
| R-15 | Week 5 and the usability review are unfinished, so totals are provisional | 4 / Medium (proposed) |

Limitations:

- One recorded run per phase on one or two machines; W3 compatibility results for tablet and phone come from emulation.
- Firefox was tested through Playwright's build 159.0, not the installed release; Chrome on Windows was 124 against 157 on macOS. Edge on Windows and Safari were excluded.
- Error codes (400, 404, 409) are a team assumption because the README defines no error contract.
- W6 automation does not cover visual, usability or accessibility checks, and ran before the W4 failures existed.
- Local development server and SQLite: no production-like load.

## 9. Deliverables, folders and schedule

| Week | Folder | Output | Status |
| --- | --- | --- | --- |
| 1 | `/01_Black_Box` | 44 cases, 3 defects | Complete |
| 2 | `/02_White_Box_Coverage` | CFGs, 19 path cases, 50 tests, coverage | Complete |
| 3 | `/03_Special_Testing` | GUI, compatibility, usability, accessibility; `DEF-004` to `013` | Executed except usability |
| 4 | `/04_Web_API` | 61 cases, `DEF-014` to `023` | Complete |
| 5 | `/05_Security_Performance` | Security and performance cases | Pending |
| 6 | `/06_Automation_Regression` | Suite, runs, seeded-fault check | Complete |
| 7 | `/07_Test_Management` | Plan, strategy, RTM, master repository, defect log, execution summary, risk register | In progress (W5 and usability review pending) |
| 8 | `/08_Final_QA_Report` | Final quality evaluation and metrics | Upcoming |
| 9 | `/09_Presentation` | Standards integration, presentation and live demonstration (course Week 12) | Upcoming |
