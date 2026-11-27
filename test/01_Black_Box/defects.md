# Week 1 - Defects

Defects first found in Week 1, in the project Defect Report Template. Later re-tests are recorded in the Week 3 and Week 4 `defects.md`.

| Defect | Title | Severity / Priority | Status |
| --- | --- | --- | --- |
| [DEF-001](#def-001---eight-character-password-is-rejected) | Eight-character password is rejected | Moderate / Medium | Open |
| [DEF-002](#def-002---today-is-classified-and-counted-as-overdue) | Today is classified and counted as overdue | Moderate / High | Open |
| [DEF-003](#def-003---whitespace-only-title-creates-a-task-with-a-blank-displayed-title) | Whitespace-only title creates a task with a blank displayed title | Moderate / Medium | Open |

## DEF-001 - Eight-character password is rejected

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-001 |
| Title | Registration rejects the stated minimum-length password |
| Affected Feature | Registration / REQ-001 |
| Environment | Google Chrome on macOS; `http://127.0.0.1:5000/register` |
| Preconditions | Logged out; username `w1d_p8_2315` is available |
| Steps to Reproduce | 1. Open Register.<br>2. Enter username `w1d_p8_2315`.<br>3. Enter `Test1234` (8 characters).<br>4. Select Register. |
| Expected Result | Registration succeeds, because the form states a minimum of 8 characters |
| Actual Result | Registration is rejected with "Password must be at least 8 characters". The 7-character control is rejected and the 9-character control accepted. |
| Severity | Moderate - valid input rejected; a longer password is a workaround |
| Priority | Medium |
| Evidence | [Input](evidences/TC-BB-008-input.jpg); [TC-BB-008.jpg](evidences/TC-BB-008.jpg) |
| Status | Open |

## DEF-002 - Today is classified and counted as overdue

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-002 |
| Title | A task due today displays Overdue and inflates the dashboard Overdue counter |
| Affected Feature | Due-date urgency / Dashboard, REQ-006 and REQ-007 |
| Environment | Google Chrome on macOS; `http://127.0.0.1:5000`; D = 2026-10-18, UTC+08:00 |
| Preconditions | Logged in as `w1d_dash_2315` with an empty task list |
| Steps to Reproduce | 1. Create Open task BB-TODAY due 2026-10-18.<br>2. Observe its urgency.<br>3. Create the rest of the seven-task dataset (W1_Report section 4), leaving six tasks Open and marking only BB-COMPLETED Done.<br>4. Open Dashboard and compare with the expected counts. |
| Expected Result | BB-TODAY displays Due Today; only yesterday's Open task counts as overdue; dashboard Overdue = 1 |
| Actual Result | BB-TODAY displays Overdue; dashboard Overdue = 2. The yesterday, +1, +2 and +3 controls are correct. |
| Severity | Moderate - misleading deadline information, no data loss |
| Priority | High - core deadline prioritisation affected |
| Evidence | [TC-BB-038.jpg](evidences/TC-BB-038.jpg); [TC-BB-043.jpg](evidences/TC-BB-043.jpg) |
| Status | Open |

## DEF-003 - Whitespace-only title creates a task with a blank displayed title

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-003 |
| Title | Creating a task accepts a whitespace-only title without validation |
| Affected Feature | Task creation / REQ-003 |
| Environment | Google Chrome on macOS; `http://127.0.0.1:5000`; 18 October 2026, UTC+08:00 |
| Preconditions | Logged in as `w1d_a_2315`; the New Task form is open |
| Steps to Reproduce | 1. Open + New Task.<br>2. Enter three spaces (`"   "`) in Title.<br>3. Select Create Task.<br>4. Observe the response and the task list. |
| Expected Result | The title is rejected with a validation message and no task is created |
| Actual Result | A task row is created with an empty displayed title. (An empty string is blocked by the browser; see TC-BB-022.) |
| Severity | Moderate - invalid input is saved and the task has no visible title |
| Priority | Medium |
| Evidence | [Input](evidences/TC-BB-023-input.jpg); [TC-BB-023.jpg](evidences/TC-BB-023.jpg) |
| Status | Open |
