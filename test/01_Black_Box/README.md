# Week 1 - Application Analysis and Black-Box Testing

| Item | Recorded value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / group | September 2026 / Wednesday - Group 2 |
| Application | PyTodo Pro |

## Deliverable Checklist

- [x] [Task 1](#task-1) - Application overview and feature inventory.
- [x] [Task 2](#task-2) - Initial test scope/risk matrix.
- [x] [Task 3](#task-3) - Black-box scenarios and cases. 44 functional cases with recorded inputs and responses.
- [x] [Task 4](#task-4) - Test data and technique justification. EP, BVA, decision tables and state transitions documented.
- [x] [Task 5](#task-5) - Execution evidence and initial defects. New captures and observations recorded; three defects documented; peer review pending.

The completion boxes remain unchecked because the group still needs to review the artefacts. This report records observed behaviour and expectation mismatches against the agreed requirements.

## Task 1

### Application overview and feature inventory

PyTodo Pro is a web-based task-management application for individuals organising work, study and personal activities. A registered user can maintain tasks, assign categories and due dates, mark work complete, search/filter the task list and view summary counters.

Testing follows normal user interactions with the web application: enter valid or invalid input, perform an action and compare the visible response with the expected result. Expected results come from application documentation, interface instructions and explicitly stated assumptions.

### Test basis and assumptions

| Basis | Description |
| --- | --- |
| Registration interface | Username 3-20 characters, letters/numbers/underscore; password minimum 8 characters |
| Task interface | `Title` is a required field for a task, and all the `description`, `category` and due `date` can be left empty |
| Documented urgency contract | No date -> No due date<br>completed -> Done<br>past -> Overdue<br> today -> Due Today<br> 1-2 days ahead -> Due Soon<br> 3+ days ahead -> Upcoming |

The urgency expectations treat today separately from past dates; expected dashboard Overdue counts therefore exclude today. A task title must contain at least one non-whitespace character. Empty or whitespace-only titles must be rejected with a validation message asking the user to enter a valid title, and no task should be created. The whitespace rule was clarified on 19 October 2026; the existing TC-BB-023 observation is assessed as Fail and linked to DEF-003. Username uniqueness, ASCII versus Unicode letters, case-sensitive search and an unspecified maximum task-title length remain outside the confirmed requirements.

### Users and features

| Requirement | Feature | User expectation |
| --- | --- | --- |
| REQ-001 | Registration | Valid details accepted; stated validation enforced |
| REQ-002 | Login, logout and protected pages | Valid credentials permit access; logout revokes it |
| REQ-003 | Create, view, edit and delete tasks | Saved information persists and actions have the stated effect |
| REQ-004 | Complete and reopen tasks | State changes and visible urgency remain consistent |
| REQ-005 | Category/status filters and title search | Results satisfy all active conditions |
| REQ-006 | Due-date urgency | Tasks receive the documented time-based classification |
| REQ-007 | Dashboard | Counters agree with independently counted task data |
| REQ-008 | User task-list separation | Each user sees their own tasks |

The normal user is an authenticated individual. An unauthenticated visitor is also considered for registration, login and protected-page checks. No administrator role is documented or assumed.

### Recorded execution environment

| Component | Value / limitation |
| --- | --- |
| Target | User-managed `app.py` development server at `http://127.0.0.1:5000` |
| Browser | Google Chrome - Version 155.0.8059.80 (Official Build) (arm64) |
| Host Operating System| macOS Tahoe v26.5.2 |
| Runtime versions | Project setup records Python 3.14.7 / Flask 3.0.3 |
| Data handling | Existing development database retained. A dedicated synthetic test accounts for the execution.|
| Execution operator | Local live server on Chrome browser interactions done by Darius Lee Shin |

### Test accounts and data

| Purpose | Recorded account |
| --- | --- |
| Task workflows | `w1d_a_2315` |
| Controlled dashboard dataset | `w1d_dash_2315` |
| User task-list separation | `w1d_b_2315` |

Synthetic password: `Test12345`, except the seven/eight-character boundary and wrong-password inputs recorded in the cases. Registration cases use their listed candidate usernames. Existing development data was retained; only the synthetic BB-MINIMAL task was deleted in the confirm-delete case.

## Task 2

### Initial test scope/risk matrix

This section includes normal and invalid web-interface workflows, input boundaries, combinations of conditions and meaningful state changes. Detailed API contracts, code coverage, cross-browser compatibility, accessibility, penetration testing, performance and a reusable automated regression suite are deferred to the relevant later phases.

Likelihood and impact use 1 = Low, 2 = Medium, 3 = High. Initial score = likelihood x impact. Priority is High for 6-9, Medium for 3-4 and Low for 1-2. Scores are initial planning judgments, not measured defect probabilities.

| Risk | Feature | Potential consequence | Likelihood | Impact | Score / priority | Planned response |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Registration | Valid users cannot register or invalid inputs are accepted | 3 | 2 | 6 / High | EP and length boundaries |
| R-02 | Authentication | Incorrect access decisions or ineffective logout | 2 | 3 | 6 / High | Credential decision table and session transitions |
| R-03 | Task management | Saved task data is lost or changed incorrectly | 2 | 3 | 6 / High | Create/edit/persistence/cancel/delete workflows |
| R-04 | Completion | Task state and displayed urgency diverge | 2 | 2 | 4 / Medium | Open -> Done -> Open transitions |
| R-05 | Filtering | Required tasks hidden or unrelated tasks returned | 2 | 2 | 4 / Medium | Match/nonmatch partitions and combined-filter table |
| R-06 | Urgency | User misjudges deadlines | 3 | 2 | 6 / High | Yesterday/today/+1/+2/+3 boundaries |
| R-07 | Dashboard | Summary counts mislead the user | 2 | 2 | 4 / Medium | Independent seven-task reconciliation |
| R-08 | User separation | Another user's task data appears | 2 | 3 | 6 / High | Two-account visible-list comparison |

After execution, R-01 and R-06 have observed failures. R-07 also has a visible discrepancy associated with the today/overdue behaviour. R-03 cancel and confirm deletion checks passed; broader data-integrity risk remains outside these selected cases. Passing visible-list isolation does not close authorisation risks for direct task IDs or APIs.

## Task 3

### Black-box scenarios and cases

[Detailed test cases](test_cases.md) record the required fields, including test data, numbered user actions, expected/actual results and evidence. The [evidence index](evidences/README.md) links the observed responses.

### Requirements Traceability Matrix (RTM)

| Requirement/Feature | Test Scenario | Test Case ID(s) | Test Type/Technique | Result | Defect ID |
| --- | --- | --- | --- | --- | --- |
| REQ-001 - Registration | Username length 2 | [TC-BB-001](test_cases.md#tc-bb-001---username-length-2) | BVA / Functional | Pass | — |
| REQ-001 - Registration | Username length 3 | [TC-BB-002](test_cases.md#tc-bb-002---username-length-3) | BVA / Functional | Pass | — |
| REQ-001 - Registration | Username length 4 | [TC-BB-003](test_cases.md#tc-bb-003---username-length-4) | BVA / Functional | Pass | — |
| REQ-001 - Registration | Username length 19 | [TC-BB-004](test_cases.md#tc-bb-004---username-length-19) | BVA / Functional | Pass | — |
| REQ-001 - Registration | Username length 20 | [TC-BB-005](test_cases.md#tc-bb-005---username-length-20) | BVA / Functional | Pass | — |
| REQ-001 - Registration | Username length 21 | [TC-BB-006](test_cases.md#tc-bb-006---username-length-21) | BVA / Functional | Pass | — |
| REQ-001 - Registration | Password length 7 | [TC-BB-007](test_cases.md#tc-bb-007---password-length-7) | BVA / Functional | Pass | — |
| REQ-001 - Registration | Password length 8 | [TC-BB-008](test_cases.md#tc-bb-008---password-length-8) | BVA / Functional | Fail | DEF-001 |
| REQ-001 - Registration | Password length 9 | [TC-BB-009](test_cases.md#tc-bb-009---password-length-9) | BVA / Functional | Pass | — |
| REQ-001 - Registration | Valid registration | [TC-BB-010](test_cases.md#tc-bb-010---valid-registration) | EP / Functional | Pass | — |
| REQ-001 - Registration | Disallowed username character | [TC-BB-011](test_cases.md#tc-bb-011---disallowed-username-character) | EP / Functional | Pass | — |
| REQ-001 - Registration | Empty registration username | [TC-BB-012](test_cases.md#tc-bb-012---empty-registration-username) | EP / Functional / Browser validation | Pass | — |
| REQ-001 - Registration | Empty registration password | [TC-BB-013](test_cases.md#tc-bb-013---empty-registration-password) | EP / Functional / Browser validation | Pass | — |
| REQ-002 - Login, logout and protected pages | Login credential decision rule 1 | [TC-BB-014](test_cases.md#tc-bb-014---login-credential-decision-rule-1) | Decision table / Functional | Pass | — |
| REQ-002 - Login, logout and protected pages | Login credential decision rule 2 | [TC-BB-015](test_cases.md#tc-bb-015---login-credential-decision-rule-2) | Decision table / Functional | Pass | — |
| REQ-002 - Login, logout and protected pages | Login credential decision rule 3 | [TC-BB-016](test_cases.md#tc-bb-016---login-credential-decision-rule-3) | Decision table / Functional | Pass | — |
| REQ-002 - Login, logout and protected pages | Login credential decision rule 4 | [TC-BB-017](test_cases.md#tc-bb-017---login-credential-decision-rule-4) | Decision table / Functional | Pass | — |
| REQ-002 - Login, logout and protected pages | Protected page while logged out | [TC-BB-018](test_cases.md#tc-bb-018---protected-page-while-logged-out) | State transition / Functional | Pass | — |
| REQ-002 - Login, logout and protected pages | Logout revokes protected-page access | [TC-BB-019](test_cases.md#tc-bb-019---logout-revokes-protected-page-access) | State transition / Functional | Pass | — |
| REQ-003 - Task management | Create and persist a full-field task | [TC-BB-020](test_cases.md#tc-bb-020---create-and-persist-a-full-field-task) | EP / Functional | Pass | — |
| REQ-003 - Task management | Create a title-only task | [TC-BB-021](test_cases.md#tc-bb-021---create-a-title-only-task) | EP / Functional | Pass | — |
| REQ-003 - Task management | Empty title browser validation | [TC-BB-022](test_cases.md#tc-bb-022---empty-title-browser-validation) | EP / Browser validation | Pass | — |
| REQ-003 - Task management | Reject a whitespace-only title | [TC-BB-023](test_cases.md#tc-bb-023---reject-a-whitespace-only-title) | EP / Functional / Input validation | Fail | DEF-003 |
| REQ-003 - Task management | Edit and persist all task fields | [TC-BB-024](test_cases.md#tc-bb-024---edit-and-persist-all-task-fields) | Functional | Pass | — |
| REQ-003 - Task management | Cancel edit preserves saved data | [TC-BB-025](test_cases.md#tc-bb-025---cancel-edit-preserves-saved-data) | State transition / Functional | Pass | — |
| REQ-003 - Task management | Cancel deletion retains task | [TC-BB-026](test_cases.md#tc-bb-026---cancel-deletion-retains-task) | State transition / Functional | Pass | — |
| REQ-003 - Task management | Confirm deletion and verify persistence | [TC-BB-027](test_cases.md#tc-bb-027---confirm-deletion-and-verify-persistence) | State transition / Functional | Pass | — |
| REQ-004 - Task completion | Complete an Open task | [TC-BB-028](test_cases.md#tc-bb-028---complete-an-open-task) | State transition / Functional | Pass | — |
| REQ-004 - Task completion | Reopen a Done task | [TC-BB-029](test_cases.md#tc-bb-029---reopen-a-done-task) | State transition / Functional | Pass | — |
| REQ-005 - Filters and search | Filter by category | [TC-BB-030](test_cases.md#tc-bb-030---filter-by-category) | EP / Functional | Pass | — |
| REQ-005 - Filters and search | Filter Open tasks | [TC-BB-031](test_cases.md#tc-bb-031---filter-open-tasks) | EP / Functional | Pass | — |
| REQ-005 - Filters and search | Filter Done tasks | [TC-BB-032](test_cases.md#tc-bb-032---filter-done-tasks) | EP / Functional | Pass | — |
| REQ-005 - Filters and search | Matching title search | [TC-BB-033](test_cases.md#tc-bb-033---matching-title-search) | EP / Functional | Pass | — |
| REQ-005 - Filters and search | Nonmatching title search | [TC-BB-034](test_cases.md#tc-bb-034---nonmatching-title-search) | EP / Functional | Pass | — |
| REQ-005 - Filters and search | Combined filters: all conditions required | [TC-BB-035](test_cases.md#tc-bb-035---combined-filters-all-conditions-required) | Decision table / Functional | Pass | — |
| REQ-006 - Task urgency | Urgency: BB-NO-DATE | [TC-BB-036](test_cases.md#tc-bb-036---urgency-bb-no-date) | EP / Functional | Pass | — |
| REQ-006 - Task urgency | Urgency: BB-YESTERDAY | [TC-BB-037](test_cases.md#tc-bb-037---urgency-bb-yesterday) | BVA / Functional | Pass | — |
| REQ-006 - Task urgency | Urgency: BB-TODAY | [TC-BB-038](test_cases.md#tc-bb-038---urgency-bb-today) | BVA / Functional | Fail | DEF-002 |
| REQ-006 - Task urgency | Urgency: BB-TOMORROW | [TC-BB-039](test_cases.md#tc-bb-039---urgency-bb-tomorrow) | BVA / Functional | Pass | — |
| REQ-006 - Task urgency | Urgency: BB-PLUS-TWO | [TC-BB-040](test_cases.md#tc-bb-040---urgency-bb-plus-two) | BVA / Functional | Pass | — |
| REQ-006 - Task urgency | Urgency: BB-PLUS-THREE | [TC-BB-041](test_cases.md#tc-bb-041---urgency-bb-plus-three) | BVA / Functional | Pass | — |
| REQ-004 / REQ-006 - Task completion / Task urgency | Completion overrides overdue urgency | [TC-BB-042](test_cases.md#tc-bb-042---completion-overrides-overdue-urgency) | State transition / Functional | Pass | — |
| REQ-007 - Dashboard | Reconcile dashboard with controlled data | [TC-BB-043](test_cases.md#tc-bb-043---reconcile-dashboard-with-controlled-data) | Functional / Independent calculation | Fail | DEF-002 |
| REQ-008 - User task-list separation | Visible task-list isolation between accounts | [TC-BB-044](test_cases.md#tc-bb-044---visible-task-list-isolation-between-accounts) | EP / Functional | Pass | — |

TC-BB-023 fails because a whitespace-only title creates a task with nothing displayed as its title. The expected response is validation asking for a valid title without creating a task. TC-BB-022 separately checks a truly empty title, which the browser rejects. Both cancel and confirm deletion passed.

## Task 4

### Test data and technique justification

All credentials below are synthetic, local test data. No personal or real account password is used. This execution used the existing development database with dedicated test accounts. For another replay, choose new account suffixes and record all actual inputs; do not reset shared data without a separate request.

#### Equivalence Partitioning (EP)

EP selects representatives from input classes expected to behave alike. This reduces repetitive testing while covering valid/invalid conditions.

| Input | Valid partitions / representatives | Invalid or alternative partitions | Cases |
| --- | --- | --- | --- |
| Username length | 3-20 characters | Below 3; above 20 | 001-006 |
| Username character set | Test account names such as `w1d_a_2315` | Hyphens in `w1-d`, `w1-t`, `w1-m`; empty | 010-012 |
| Password | At least 8 characters | Below 8; empty | 007-009, 013 |
| Credentials | Existing username with matching password | Wrong password; unknown username | 014-017 |
| Task optional data | All fields filled; title only | Empty required title; whitespace-only title | 020-023 |
| Search | Matching substring MATCH | Absent term NO-SUCH-TITLE-881 | 033-034 |
| Due date | No date; past; today; near future; later future | Malformed date inputs deferred to later web/API work | 036-041 |

Empty-field cases demonstrate the browser's `required` validation only. They do not prove equivalent server-side validation.

#### Boundary Value Analysis (BVA)

BVA checks values immediately below, at and above the specified boundaries rather than deriving expectations from current implementation behaviour.

| Boundary | Values / expected result | Cases |
| --- | --- | --- |
| Username minimum/maximum | 2 reject; 3 accept; 4 accept; 19 accept; 20 accept; 21 reject | 001-006 |
| Password minimum | 7 reject; 8 accept; 9 accept | 007-009 |
| Today boundary | D-1 Overdue; D Due Today; D+1 Due Soon | 037-039 |
| Due Soon upper boundary | D+1/D+2 Due Soon; D+3 Upcoming | 039-041 |

Executed password strings were `Test123` (7), `Test1234` (8) and `Test12345` (9). The UI masks passwords, so the exact values and lengths are recorded in the test records rather than inferred from screenshot dots.

#### Authentication decision table

| Condition / action | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Username is baseline registered account | Yes | Yes | No | No |
| Password equals baseline account password | Yes | No | Yes | No |
| Allow login | Yes | No | No | No |
| Test | TC-BB-014 | TC-BB-015 | TC-BB-016 | TC-BB-017 |

The unknown username is `w1d_unknown_2315`. Its password comparison is to the known baseline account; it does not imply an unknown account has its own valid password.

#### Combined-filter decision table and fixtures

| Fixture | Title | Category matches Work? | Status matches Open? | Title matches MATCH? | Include? |
| --- | --- | --- | --- | --- | --- |
| F1 | BB-MATCH-WORK-OPEN | Yes | Yes | Yes | Yes |
| F2 | BB-MATCH-WORK-DONE | Yes | No | Yes | No |
| F3 | BB-MATCH-STUDY-OPEN | No | Yes | Yes | No |
| F4 | BB-OTHER-WORK-OPEN | Yes | Yes | No | No |

TC-BB-035 verifies that all three selected conditions must hold. This is focused coverage of each individual exclusion condition, not an exhaustive claim over all eight Boolean combinations.

#### State transitions

| Initial state | Event | Expected next state | Case / result |
| --- | --- | --- | --- |
| Logged out | Valid login | Logged in | 014 / Pass |
| Logged out | Invalid login | Logged out | 015-017 / Pass |
| Logged in | Logout | Logged out; protected page requires login | 019 / Pass |
| Saved task | Save edited fields | Updated saved task | 024 / Pass |
| Saved task with unsaved draft | Cancel edit | Original saved task | 025 / Pass |
| Open task | Complete | Done | 028 / Pass |
| Done task | Reopen | Open with recalculated urgency | 029 / Pass |
| Existing task | Cancel deletion | Existing task retained | 026 / Pass |
| Existing task | Confirm deletion | Deleted and absent after refresh | 027 / Pass |

#### Controlled urgency/dashboard dataset

The dashboard test account contained exactly these seven tasks. All use Study category. The first six are Open; BB-COMPLETED was marked Done during the run.

| Task | Due date | Expected urgency |
| --- | --- | --- |
| BB-NO-DATE | None | No due date |
| BB-YESTERDAY | 2026-10-17 | Overdue |
| BB-TODAY | 2026-10-18 | Due Today |
| BB-TOMORROW | 2026-10-19 | Due Soon |
| BB-PLUS-TWO | 2026-10-20 | Due Soon |
| BB-PLUS-THREE | 2026-10-21 | Upcoming |
| BB-COMPLETED | 2026-10-17 | Done |

| Counter | Independently expected | Observed |
| --- | --- | --- |
| Total | 7 | 7 |
| Open | 6 | 6 |
| Overdue | 1 | 2 |
| Due Soon | 2 | 2 |
| Completed in last 7 days | 1 | 1 |

## Task 5

### Execution evidence and initial defect records

#### Execution summary

| Test cases | Pass | Fail | Blocked | Not Run |
| --- | --- | --- | --- | --- |
| 44 | 40 | 4 | 0 | 0 |

Each test case is counted once. Pass rate = 40 / 44 = 90.91%. Verdict completion = 44 / 44 = 100%. The four failing cases map to three defect records: TC-BB-008 to DEF-001, TC-BB-038/043 to DEF-002, and TC-BB-023 to DEF-003. TC-BB-023 was reassessed using the clarified requirement and existing execution evidence; no new browser run is claimed.

#### Evidence and traceability

The screenshots `TC-BB-001.jpg` through `TC-BB-044.jpg` are stored directly in `evidences/`. Each test case names its corresponding screenshot in the Evidence field. The [evidence index](evidences/README.md) links these screenshots; [detailed cases](test_cases.md) record the inputs and expected/actual responses.

Required-field checks use the browser's visible validation and unchanged form state. Deletion checks use Cancel/OK in the confirmation dialog and verify the resulting task list.

#### DEF-001 - Eight-character password is rejected

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-001 |
| Title | Registration rejects the stated minimum-length password |
| Affected Feature | Registration / REQ-001 |
| Environment | Google Chrome on macOS; `http://127.0.0.1:5000/register` |
| Preconditions | Logged out; username `w1d_p8_2315` is available for registration |
| Steps to Reproduce | 1. Open Register.<br>2. Enter username `w1d_p8_2315`.<br>3. Enter Test1234 (8 characters).<br>4. Select Register. |
| Expected Result | Successful registration because the form states minimum 8 characters |
| Actual Result | Registration rejected with Password must be at least 8 characters |
| Severity | Moderate - valid input rejected; longer-password workaround exists |
| Priority | Medium |
| Evidence | [TC-BB-008.jpg](evidences/TC-BB-008.jpg) |
| Status | Open |

The seven-character control was rejected and the nine-character control accepted. No source-level cause or application fix is claimed.

#### DEF-002 - Today is classified and counted as overdue

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-002 |
| Title | A task due today displays Overdue and inflates the dashboard Overdue counter |
| Affected Feature | Urgency / dashboard, REQ-006 and REQ-007 |
| Environment | Google Chrome on macOS; `http://127.0.0.1:5000`; D = 2026-10-18, UTC+08:00 |
| Preconditions | Dashboard account `w1d_dash_2315` contains the seven-task dataset |
| Steps to Reproduce | 1. Create Open BB-TODAY due 2026-10-18.<br>2. Observe urgency.<br>3. Complete the seven-task dataset.<br>4. Open Dashboard and compare independently counted values. |
| Expected Result | BB-TODAY displays Due Today; only yesterday's Open task counts as overdue; dashboard Overdue = 1 |
| Actual Result | BB-TODAY displays Overdue; dashboard Overdue = 2 |
| Severity | Moderate - misleading deadline information without observed data loss |
| Priority | High - core deadline prioritisation affected |
| Evidence | [TC-BB-038.jpg](evidences/TC-BB-038.jpg); [TC-BB-043.jpg](evidences/TC-BB-043.jpg) |
| Status | Open |

The label and count symptoms are grouped in one initial record. A shared source-level cause is not asserted here. Yesterday, +1, +2 and +3 date controls passed.

#### DEF-003 - Whitespace-only title creates a task with a blank displayed title

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-003 |
| Title | Creating a task accepts a whitespace-only title without validation |
| Affected Feature | Task creation / REQ-003 |
| Environment | Google Chrome on macOS; `http://127.0.0.1:5000`; execution date 18 October 2026, UTC+08:00 |
| Preconditions | Logged in as Account A (`w1d_a_2315`); the New Task form is available |
| Steps to Reproduce | 1. Open + New Task.<br>2. Enter three spaces (`"   "`) in Title.<br>3. Select Create Task.<br>4. Observe the response and the task list. |
| Expected Result | Reject the whitespace-only title, display a validation message asking the user to enter a valid title, and do not create a task. |
| Actual Result | Submitting three spaces creates a task row with an empty displayed title instead of rejecting the input and asking for a valid title. |
| Severity | Moderate - invalid input is saved and the task has no visible title in the todo list |
| Priority | Medium |
| Evidence | [TC-BB-023.jpg](evidences/TC-BB-023.jpg) |
| Status | Open |

The title requirement was clarified on 19 October 2026. This defect uses the existing observation that three spaces created a task with a blank displayed title. TC-BB-022 covers the empty string separately and passed browser required-field validation.

### Black-Box Testing Evidence

Application: `http://127.0.0.1:5000`. Execution date: 18 October 2026, UTC+08:00.

Each row links the screenshot stored directly in this folder for its test case. The [detailed test cases](../test_cases.md) record the corresponding inputs, expected/actual responses and screenshot filenames.

| Test Case ID | Test Scenario | Result | Evidence |
| --- | --- | --- | --- |
| TC-BB-001 | Username length 2 | Pass | [TC-BB-001.jpg](TC-BB-001.jpg) |
| TC-BB-002 | Username length 3 | Pass | [TC-BB-002.jpg](TC-BB-002.jpg) |
| TC-BB-003 | Username length 4 | Pass | [TC-BB-003.jpg](TC-BB-003.jpg) |
| TC-BB-004 | Username length 19 | Pass | [TC-BB-004.jpg](TC-BB-004.jpg) |
| TC-BB-005 | Username length 20 | Pass | [TC-BB-005.jpg](TC-BB-005.jpg) |
| TC-BB-006 | Username length 21 | Pass | [TC-BB-006.jpg](TC-BB-006.jpg) |
| TC-BB-007 | Password length 7 | Pass | [TC-BB-007.jpg](TC-BB-007.jpg) |
| TC-BB-008 | Password length 8 | Fail | [TC-BB-008.jpg](TC-BB-008.jpg) |
| TC-BB-009 | Password length 9 | Pass | [TC-BB-009.jpg](TC-BB-009.jpg) |
| TC-BB-010 | Valid registration | Pass | [TC-BB-010.jpg](TC-BB-010.jpg) |
| TC-BB-011 | Disallowed username character | Pass | [TC-BB-011.jpg](TC-BB-011.jpg) |
| TC-BB-012 | Empty registration username | Pass | [TC-BB-012.jpg](TC-BB-012.jpg) |
| TC-BB-013 | Empty registration password | Pass | [TC-BB-013.jpg](TC-BB-013.jpg) |
| TC-BB-014 | Login credential decision rule 1 | Pass | [TC-BB-014.jpg](TC-BB-014.jpg) |
| TC-BB-015 | Login credential decision rule 2 | Pass | [TC-BB-015.jpg](TC-BB-015.jpg) |
| TC-BB-016 | Login credential decision rule 3 | Pass | [TC-BB-016.jpg](TC-BB-016.jpg) |
| TC-BB-017 | Login credential decision rule 4 | Pass | [TC-BB-017.jpg](TC-BB-017.jpg) |
| TC-BB-018 | Protected page while logged out | Pass | [TC-BB-018.jpg](TC-BB-018.jpg) |
| TC-BB-019 | Logout revokes protected-page access | Pass | [TC-BB-019.jpg](TC-BB-019.jpg) |
| TC-BB-020 | Create and persist a full-field task | Pass | [TC-BB-020.jpg](TC-BB-020.jpg) |
| TC-BB-021 | Create a title-only task | Pass | [TC-BB-021.jpg](TC-BB-021.jpg) |
| TC-BB-022 | Empty title browser validation | Pass | [TC-BB-022.jpg](TC-BB-022.jpg) |
| TC-BB-023 | Reject a whitespace-only title | Fail | [TC-BB-023.jpg](TC-BB-023.jpg) |
| TC-BB-024 | Edit and persist all task fields | Pass | [TC-BB-024.jpg](TC-BB-024.jpg) |
| TC-BB-025 | Cancel edit preserves saved data | Pass | [TC-BB-025.jpg](TC-BB-025.jpg) |
| TC-BB-026 | Cancel deletion retains task | Pass | [TC-BB-026.jpg](TC-BB-026.jpg) |
| TC-BB-027 | Confirm deletion and verify persistence | Pass | [TC-BB-027.jpg](TC-BB-027.jpg) |
| TC-BB-028 | Complete an Open task | Pass | [TC-BB-028.jpg](TC-BB-028.jpg) |
| TC-BB-029 | Reopen a Done task | Pass | [TC-BB-029.jpg](TC-BB-029.jpg) |
| TC-BB-030 | Filter by category | Pass | [TC-BB-030.jpg](TC-BB-030.jpg) |
| TC-BB-031 | Filter Open tasks | Pass | [TC-BB-031.jpg](TC-BB-031.jpg) |
| TC-BB-032 | Filter Done tasks | Pass | [TC-BB-032.jpg](TC-BB-032.jpg) |
| TC-BB-033 | Matching title search | Pass | [TC-BB-033.jpg](TC-BB-033.jpg) |
| TC-BB-034 | Nonmatching title search | Pass | [TC-BB-034.jpg](TC-BB-034.jpg) |
| TC-BB-035 | Combined filters: all conditions required | Pass | [TC-BB-035.jpg](TC-BB-035.jpg) |
| TC-BB-036 | Urgency: BB-NO-DATE | Pass | [TC-BB-036.jpg](TC-BB-036.jpg) |
| TC-BB-037 | Urgency: BB-YESTERDAY | Pass | [TC-BB-037.jpg](TC-BB-037.jpg) |
| TC-BB-038 | Urgency: BB-TODAY | Fail | [TC-BB-038.jpg](TC-BB-038.jpg) |
| TC-BB-039 | Urgency: BB-TOMORROW | Pass | [TC-BB-039.jpg](TC-BB-039.jpg) |
| TC-BB-040 | Urgency: BB-PLUS-TWO | Pass | [TC-BB-040.jpg](TC-BB-040.jpg) |
| TC-BB-041 | Urgency: BB-PLUS-THREE | Pass | [TC-BB-041.jpg](TC-BB-041.jpg) |
| TC-BB-042 | Completion overrides overdue urgency | Pass | [TC-BB-042.jpg](TC-BB-042.jpg) |
| TC-BB-043 | Reconcile dashboard with controlled data | Fail | [TC-BB-043.jpg](TC-BB-043.jpg) |
| TC-BB-044 | Visible task-list isolation between accounts | Pass | [TC-BB-044.jpg](TC-BB-044.jpg) |


#### Reproducing a case

Open the application at `http://127.0.0.1:5000` in Chrome and follow the numbered steps in [test_cases.md](test_cases.md). Use dedicated test accounts, update date-dependent inputs for the execution date, and record the actual response with new evidence.