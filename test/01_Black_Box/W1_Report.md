# Week 1 - Application Analysis and Black-Box Testing

| Item | Value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance, September 2026 |
| Lab group | Wednesday Lab - Group 2 |
| Phase owner | Darius Lee Shin |
| Execution date | 18 October 2026 (UTC+08:00) |
| Environment | macOS Tahoe 26.5.2; Google Chrome 155.0.8059.80 (arm64); Python 3.14.7, Flask 3.0.3; app served by `python app.py` at `http://127.0.0.1:5000` |

## Deliverable checklist

- [x] [1. Application overview and feature inventory](#1-application-overview-and-feature-inventory)
- [x] [2. Initial test scope/risk matrix](#2-initial-test-scoperisk-matrix)
- [x] [3. Black-box test scenarios and cases](#3-black-box-test-scenarios-and-cases) - 44 cases in [test_cases.md](test_cases.md)
- [x] [4. Test data and technique justification](#4-test-data-and-technique-justification) - EP, BVA, decision tables, state transitions
- [x] [5. Execution evidence and initial defect records](#5-execution-evidence-and-initial-defect-records) - 3 defects in [defects.md](defects.md)

## 1. Application overview and feature inventory

PyTodo Pro is a web task manager for individuals organising work, study and personal activities. A registered user can create tasks, assign categories and due dates, mark work complete, search and filter the task list, and view summary counters. Tests follow normal user interactions: enter valid or invalid input, perform an action, and compare the visible response with the expected result.

### Test basis

| Basis | Description |
| --- | --- |
| Registration interface | Username 3-20 characters, letters/numbers/underscore; password minimum 8 characters |
| Task interface | `Title` is required; `Description`, `Category` and `Due Date` can be left empty |
| Documented urgency rules | Completed -> Done, regardless of due date<br>Open tasks: no date -> No due date; past -> Overdue; today -> Due Today; 1-2 days ahead -> Due Soon; 3+ days ahead -> Upcoming |

Assumptions:

1. Urgency distinguishes today from past dates, so the dashboard Overdue count excludes tasks due today.
2. A task title must contain at least one non-whitespace character. Empty or whitespace-only titles are rejected with a validation message and no task is created.

### Feature inventory

| Requirement | Feature | User expectation |
| --- | --- | --- |
| REQ-001 | Registration | Valid details are accepted after passing the stated validation |
| REQ-002 | Login, logout and protected pages | Valid credentials permit access to protected pages; logout revokes access |
| REQ-003 | Create, view, edit and delete tasks | Saved task information persists and each action has the stated effect |
| REQ-004 | Complete and reopen tasks | State changes and visible urgency remain consistent |
| REQ-005 | Category/status filters and title search | Results satisfy all active conditions |
| REQ-006 | Due-date urgency | Tasks receive the documented time-based classification |
| REQ-007 | Dashboard | Counters agree with independently counted task data |
| REQ-008 | User task-list separation | Each user sees only their own tasks |

Users: one role, the authenticated individual. An unauthenticated visitor is also considered for registration, login and protected-page checks. No administrator role exists.

### Test accounts

| Purpose | Account |
| --- | --- |
| Task workflows | `w1d_a_2315` |
| Controlled dashboard dataset | `w1d_dash_2315` |
| User task-list separation | `w1d_b_2315` |

Synthetic password `Test12345`, except for the boundary and wrong-password inputs listed in each case. Registration cases use their own candidate usernames.

## 2. Initial test scope/risk matrix

In scope: normal and invalid web-interface workflows, input boundaries, condition combinations and state changes. API contracts, code coverage, compatibility, accessibility, security and performance are covered in Weeks 2-5.

Likelihood and impact: 1 = Low, 2 = Medium, 3 = High. Score = likelihood x impact. Priority: High 6-9, Medium 3-4, Low 1-2.

| Risk | Feature | Potential consequence | Likelihood | Impact | Score / priority | Planned response |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Registration | Valid users cannot register or invalid inputs are accepted | 3 | 2 | 6 / High | EP and length boundaries |
| R-02 | Login, logout and protected pages | Incorrect access decisions or ineffective logout | 2 | 3 | 6 / High | Credential decision table and session transitions |
| R-03 | Create, view, edit and delete tasks | Invalid task data is saved, or saved data is lost or changed | 2 | 3 | 6 / High | Input validation and create/edit/cancel/delete workflows |
| R-04 | Complete and reopen tasks | Task state and displayed urgency diverge | 2 | 2 | 4 / Medium | Open -> Done -> Open transitions |
| R-05 | Category/status filters and title search | Matching tasks hidden or unrelated tasks returned | 2 | 2 | 4 / Medium | Match/non-match partitions and combined-filter table |
| R-06 | Due-date urgency | Users misjudge task deadlines | 3 | 2 | 6 / High | Yesterday/today/+1/+2/+3 boundaries |
| R-07 | Dashboard | Summary counts do not reflect task data | 2 | 2 | 4 / Medium | Independent seven-task reconciliation |
| R-08 | User task-list separation | Another user's tasks appear | 2 | 3 | 6 / High | Two-account visible-list comparison |

After execution, R-01 (DEF-001), R-03 (DEF-003), R-06 and R-07 (DEF-002) have observed failures. Passing visible-list isolation (R-08) does not cover direct task IDs or the API; those are tested in Weeks 4 and 5.

## 3. Black-box test scenarios and cases

Full cases: [test_cases.md](test_cases.md). Requirements traceability:

| Requirement/Feature | Test Scenario | Test Case ID | Technique | Result | Defect ID | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-001 Registration | Username length 2 | [TC-BB-001](test_cases.md#tc-bb-001---username-length-2) | BVA | Pass | — | [jpg](evidences/TC-BB-001.jpg) |
| REQ-001 Registration | Username length 3 | [TC-BB-002](test_cases.md#tc-bb-002---username-length-3) | BVA | Pass | — | [jpg](evidences/TC-BB-002.jpg) |
| REQ-001 Registration | Username length 4 | [TC-BB-003](test_cases.md#tc-bb-003---username-length-4) | BVA | Pass | — | [jpg](evidences/TC-BB-003.jpg) |
| REQ-001 Registration | Username length 19 | [TC-BB-004](test_cases.md#tc-bb-004---username-length-19) | BVA | Pass | — | [jpg](evidences/TC-BB-004.jpg) |
| REQ-001 Registration | Username length 20 | [TC-BB-005](test_cases.md#tc-bb-005---username-length-20) | BVA | Pass | — | [jpg](evidences/TC-BB-005.jpg) |
| REQ-001 Registration | Username length 21 | [TC-BB-006](test_cases.md#tc-bb-006---username-length-21) | BVA | Pass | — | [jpg](evidences/TC-BB-006.jpg) |
| REQ-001 Registration | Password length 7 | [TC-BB-007](test_cases.md#tc-bb-007---password-length-7) | BVA | Pass | — | [jpg](evidences/TC-BB-007.jpg) |
| REQ-001 Registration | Password length 8 | [TC-BB-008](test_cases.md#tc-bb-008---password-length-8) | BVA | Fail | [DEF-001](defects.md#def-001---eight-character-password-is-rejected) | [jpg](evidences/TC-BB-008.jpg) |
| REQ-001 Registration | Password length 9 | [TC-BB-009](test_cases.md#tc-bb-009---password-length-9) | BVA | Pass | — | [jpg](evidences/TC-BB-009.jpg) |
| REQ-001 Registration | Valid registration | [TC-BB-010](test_cases.md#tc-bb-010---valid-registration) | EP | Pass | — | [jpg](evidences/TC-BB-010.jpg) |
| REQ-001 Registration | Disallowed username character | [TC-BB-011](test_cases.md#tc-bb-011---disallowed-username-character) | EP | Pass | — | [jpg](evidences/TC-BB-011.jpg) |
| REQ-001 Registration | Empty registration username | [TC-BB-012](test_cases.md#tc-bb-012---empty-registration-username) | EP / Browser validation | Pass | — | [jpg](evidences/TC-BB-012.jpg) |
| REQ-001 Registration | Empty registration password | [TC-BB-013](test_cases.md#tc-bb-013---empty-registration-password) | EP / Browser validation | Pass | — | [jpg](evidences/TC-BB-013.jpg) |
| REQ-002 Login/logout | Credential decision rule 1 | [TC-BB-014](test_cases.md#tc-bb-014---login-credential-decision-rule-1) | Decision table | Pass | — | [jpg](evidences/TC-BB-014.jpg) |
| REQ-002 Login/logout | Credential decision rule 2 | [TC-BB-015](test_cases.md#tc-bb-015---login-credential-decision-rule-2) | Decision table | Pass | — | [jpg](evidences/TC-BB-015.jpg) |
| REQ-002 Login/logout | Credential decision rule 3 | [TC-BB-016](test_cases.md#tc-bb-016---login-credential-decision-rule-3) | Decision table | Pass | — | [jpg](evidences/TC-BB-016.jpg) |
| REQ-002 Login/logout | Credential decision rule 4 | [TC-BB-017](test_cases.md#tc-bb-017---login-credential-decision-rule-4) | Decision table | Pass | — | [jpg](evidences/TC-BB-017.jpg) |
| REQ-002 Login/logout | Protected page while logged out | [TC-BB-018](test_cases.md#tc-bb-018---protected-page-while-logged-out) | State transition | Pass | — | [jpg](evidences/TC-BB-018.jpg) |
| REQ-002 Login/logout | Logout revokes protected-page access | [TC-BB-019](test_cases.md#tc-bb-019---logout-revokes-protected-page-access) | State transition | Pass | — | [jpg](evidences/TC-BB-019.jpg) |
| REQ-003 Tasks | Create and persist a full-field task | [TC-BB-020](test_cases.md#tc-bb-020---create-and-persist-a-full-field-task) | EP | Pass | — | [jpg](evidences/TC-BB-020.jpg) |
| REQ-003 Tasks | Create a title-only task | [TC-BB-021](test_cases.md#tc-bb-021---create-a-title-only-task) | EP | Pass | — | [jpg](evidences/TC-BB-021.jpg) |
| REQ-003 Tasks | Empty title browser validation | [TC-BB-022](test_cases.md#tc-bb-022---empty-title-browser-validation) | EP / Browser validation | Pass | — | [jpg](evidences/TC-BB-022.jpg) |
| REQ-003 Tasks | Reject a whitespace-only title | [TC-BB-023](test_cases.md#tc-bb-023---reject-a-whitespace-only-title) | EP / Input validation | Fail | [DEF-003](defects.md#def-003---whitespace-only-title-creates-a-task-with-a-blank-displayed-title) | [jpg](evidences/TC-BB-023.jpg) |
| REQ-003 Tasks | Edit and persist all task fields | [TC-BB-024](test_cases.md#tc-bb-024---edit-and-persist-all-task-fields) | Functional | Pass | — | [jpg](evidences/TC-BB-024.jpg) |
| REQ-003 Tasks | Cancel edit preserves saved data | [TC-BB-025](test_cases.md#tc-bb-025---cancel-edit-preserves-saved-data) | State transition | Pass | — | [jpg](evidences/TC-BB-025.jpg) |
| REQ-003 Tasks | Cancel deletion retains task | [TC-BB-026](test_cases.md#tc-bb-026---cancel-deletion-retains-task) | State transition | Pass | — | [jpg](evidences/TC-BB-026.jpg) |
| REQ-003 Tasks | Confirm deletion and verify persistence | [TC-BB-027](test_cases.md#tc-bb-027---confirm-deletion-and-verify-persistence) | State transition | Pass | — | [jpg](evidences/TC-BB-027.jpg) |
| REQ-004 Complete/reopen | Complete an Open task | [TC-BB-028](test_cases.md#tc-bb-028---complete-an-open-task) | State transition | Pass | — | [jpg](evidences/TC-BB-028.jpg) |
| REQ-004 Complete/reopen | Reopen a Done task | [TC-BB-029](test_cases.md#tc-bb-029---reopen-a-done-task) | State transition | Pass | — | [jpg](evidences/TC-BB-029.jpg) |
| REQ-005 Filters/search | Filter by category | [TC-BB-030](test_cases.md#tc-bb-030---filter-by-category) | EP | Pass | — | [jpg](evidences/TC-BB-030.jpg) |
| REQ-005 Filters/search | Filter Open tasks | [TC-BB-031](test_cases.md#tc-bb-031---filter-open-tasks) | EP | Pass | — | [jpg](evidences/TC-BB-031.jpg) |
| REQ-005 Filters/search | Filter Done tasks | [TC-BB-032](test_cases.md#tc-bb-032---filter-done-tasks) | EP | Pass | — | [jpg](evidences/TC-BB-032.jpg) |
| REQ-005 Filters/search | Matching title search | [TC-BB-033](test_cases.md#tc-bb-033---matching-title-search) | EP | Pass | — | [jpg](evidences/TC-BB-033.jpg) |
| REQ-005 Filters/search | Non-matching title search | [TC-BB-034](test_cases.md#tc-bb-034---nonmatching-title-search) | EP | Pass | — | [jpg](evidences/TC-BB-034.jpg) |
| REQ-005 Filters/search | Combined filters: all conditions required | [TC-BB-035](test_cases.md#tc-bb-035---combined-filters-all-conditions-required) | Decision table | Pass | — | [jpg](evidences/TC-BB-035.jpg) |
| REQ-006 Urgency | BB-NO-DATE | [TC-BB-036](test_cases.md#tc-bb-036---urgency-bb-no-date) | EP | Pass | — | [jpg](evidences/TC-BB-036.jpg) |
| REQ-006 Urgency | BB-YESTERDAY | [TC-BB-037](test_cases.md#tc-bb-037---urgency-bb-yesterday) | BVA | Pass | — | [jpg](evidences/TC-BB-037.jpg) |
| REQ-006 Urgency | BB-TODAY | [TC-BB-038](test_cases.md#tc-bb-038---urgency-bb-today) | BVA | Fail | [DEF-002](defects.md#def-002---today-is-classified-and-counted-as-overdue) | [jpg](evidences/TC-BB-038.jpg) |
| REQ-006 Urgency | BB-TOMORROW | [TC-BB-039](test_cases.md#tc-bb-039---urgency-bb-tomorrow) | BVA | Pass | — | [jpg](evidences/TC-BB-039.jpg) |
| REQ-006 Urgency | BB-PLUS-TWO | [TC-BB-040](test_cases.md#tc-bb-040---urgency-bb-plus-two) | BVA | Pass | — | [jpg](evidences/TC-BB-040.jpg) |
| REQ-006 Urgency | BB-PLUS-THREE | [TC-BB-041](test_cases.md#tc-bb-041---urgency-bb-plus-three) | BVA | Pass | — | [jpg](evidences/TC-BB-041.jpg) |
| REQ-004 / REQ-006 | Completion overrides overdue urgency | [TC-BB-042](test_cases.md#tc-bb-042---completion-overrides-overdue-urgency) | State transition | Pass | — | [jpg](evidences/TC-BB-042.jpg) |
| REQ-007 Dashboard | Reconcile dashboard with controlled data | [TC-BB-043](test_cases.md#tc-bb-043---reconcile-dashboard-with-controlled-data) | Independent calculation | Fail | [DEF-002](defects.md#def-002---today-is-classified-and-counted-as-overdue) | [jpg](evidences/TC-BB-043.jpg) |
| REQ-008 Separation | Visible task-list isolation between accounts | [TC-BB-044](test_cases.md#tc-bb-044---visible-task-list-isolation-between-accounts) | EP | Pass | — | [jpg](evidences/TC-BB-044.jpg) |

## 4. Test data and technique justification

All credentials are synthetic local test data. Execution used the development database with dedicated test accounts.

### Equivalence Partitioning (EP)

EP picks one representative from each input class expected to behave alike, covering valid and invalid conditions without repetition.

| Input | Valid partitions / representatives | Invalid or alternative partitions | Cases |
| --- | --- | --- | --- |
| Username length | 3-20 characters | Below 3; above 20 | 001-006 |
| Username character set | Letters, numbers and underscore: `w1d_a_2315` | Hyphen: `w1-d` | 010 (valid); 011 (hyphen) |
| Username presence | Non-empty username | Empty username (`""`) | 012 |
| Password | At least 8 characters | Below 8; empty | 007-009, 013 |
| Credentials | Existing username with matching password | Wrong password; unknown username | 014-017 |
| Task data | All fields filled; title only | Empty title; whitespace-only title | 020-023 |
| Search | Matching substring `MATCH` | Absent term `NO-SUCH-TITLE-881` | 033-034 |
| Due date | No date; past; today; near future; later future | Malformed dates (tested in Week 4) | 036-041 |

Empty-field cases show the browser's `required` validation only, not server-side validation.

### Boundary Value Analysis (BVA)

BVA checks values just below, at and just above each specified boundary.

| Boundary | Values / expected result | Cases |
| --- | --- | --- |
| Username minimum/maximum | 2 reject; 3 accept; 4 accept; 19 accept; 20 accept; 21 reject | 001-006 |
| Password minimum | 7 reject; 8 accept; 9 accept | 007-009 |
| Today boundary | D-1 Overdue; D Due Today; D+1 Due Soon | 037-039 |
| Due Soon upper boundary | D+1/D+2 Due Soon; D+3 Upcoming | 039-041 |

Password inputs were `Test123` (7), `Test1234` (8) and `Test12345` (9). The UI masks passwords, so the exact values are recorded in the test cases.

### Authentication decision table

| Condition / action | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Username is the registered baseline account | Yes | Yes | No | No |
| Password equals the baseline account password | Yes | No | Yes | No |
| Allow login | Yes | No | No | No |
| Test | TC-BB-014 | TC-BB-015 | TC-BB-016 | TC-BB-017 |

The unknown username is `w1d_unknown_2315`.

### Combined-filter decision table

| Fixture | Title | Category = Work? | Status = Open? | Title contains MATCH? | Include? |
| --- | --- | --- | --- | --- | --- |
| F1 | BB-MATCH-WORK-OPEN | Yes | Yes | Yes | Yes |
| F2 | BB-MATCH-WORK-DONE | Yes | No | Yes | No |
| F3 | BB-MATCH-STUDY-OPEN | No | Yes | Yes | No |
| F4 | BB-OTHER-WORK-OPEN | Yes | Yes | No | No |

TC-BB-035 checks that each condition on its own excludes a task; it does not cover all eight Boolean combinations.

### State transitions

| Initial state | Event | Expected next state | Case / result |
| --- | --- | --- | --- |
| Logged out | Valid login | Logged in | 014 / Pass |
| Logged out | Invalid login | Logged out | 015-017 / Pass |
| Logged in | Logout | Logged out; protected page requires login | 019 / Pass |
| Saved task | Save edited fields | Updated saved task | 024 / Pass |
| Saved task with unsaved draft | Cancel edit | Original saved task | 025 / Pass |
| Open task | Complete | Done | 028 / Pass |
| Done task | Reopen | Open with recalculated urgency | 029 / Pass |
| Existing task | Cancel deletion | Task retained | 026 / Pass |
| Existing task | Confirm deletion | Deleted and absent after refresh | 027 / Pass |

### Controlled urgency/dashboard dataset

The dashboard account held exactly these seven Study tasks ([dataset evidence](evidences/dashboard-dataset.jpg)). The first six are Open; BB-COMPLETED was marked Done during the run. Execution date D = 2026-10-18.

| Task | Due date | Expected urgency |
| --- | --- | --- |
| BB-NO-DATE | None | No due date |
| BB-YESTERDAY | 2026-10-17 | Overdue |
| BB-TODAY | 2026-10-18 | Due Today |
| BB-TOMORROW | 2026-10-19 | Due Soon |
| BB-PLUS-TWO | 2026-10-20 | Due Soon |
| BB-PLUS-THREE | 2026-10-21 | Upcoming |
| BB-COMPLETED | 2026-10-17 | Done |

| Counter | Expected | Observed |
| --- | --- | --- |
| Total | 7 | 7 |
| Open | 6 | 6 |
| Overdue | 1 | **2** |
| Due Soon | 2 | 2 |
| Completed in last 7 days | 1 | 1 |

## 5. Execution evidence and initial defect records

| Test cases | Pass | Fail | Blocked | Not Run | Pass rate |
| --- | --- | --- | --- | --- | --- |
| 44 | 40 | 4 | 0 | 0 | 40 / 44 = 90.9% |

Each case has a screenshot in [`evidences/`](evidences/), linked in the table in section 3. Required-field checks rely on the browser's visible validation; deletion checks use Cancel/OK in the confirmation dialog and then check the task list.

The four failures map to three defects, recorded in full in [defects.md](defects.md):

| Defect | Title | Failing case(s) | Severity / Priority |
| --- | --- | --- | --- |
| DEF-001 | Eight-character password is rejected | TC-BB-008 | Moderate / Medium |
| DEF-002 | Today is classified and counted as overdue | TC-BB-038, TC-BB-043 | Moderate / High |
| DEF-003 | Whitespace-only title creates a task with a blank displayed title | TC-BB-023 | Moderate / Medium |
