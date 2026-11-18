# Week 3 - Compatibility Test Cases

Detailed cases for [Task 2 - Compatibility/configuration matrix](../README.md#task-2) of the [Week 3 plan](../README.md). Each case uses the guideline's test-case template fields. Precondition codes (P-APP, P-OUT, P-A, P-C, P-VO), test accounts and fixture IDs (F1-F9) are defined in [fixtures.md](../fixtures.md). Every case is `Not Run` until executed; fill in Actual Result, Status, Evidence and Defect ID only after execution, and replace `<YYYYMMDD>` in evidence filenames with the execution date.

## Review sign-off

Expected results must be reviewed before execution (plan step 3). The reviewer checks that each expected result cites a basis from [README 0.3](../README.md#03-test-basis) and was not derived from observed behaviour.

| Reviewer | Date | Cases reviewed | Changes requested | Approved |
| --- | --- | --- | --- | --- |
| | | TC-CMP-001 to 008 | | |

## Case index

| ID | Title |
| --- | --- |
| [TC-CMP-001](#tc-cmp-001---register-log-in-and-log-out) | Register, log in and log out |
| [TC-CMP-002](#tc-cmp-002---create-a-task-with-the-date-picker) | Create a task with the date picker |
| [TC-CMP-003](#tc-cmp-003---filter-and-search) | Filter and search |
| [TC-CMP-004](#tc-cmp-004---complete-and-reopen) | Complete and reopen |
| [TC-CMP-005](#tc-cmp-005---edit-a-task) | Edit a task |
| [TC-CMP-006](#tc-cmp-006---delete-with-confirmation) | Delete with confirmation |
| [TC-CMP-007](#tc-cmp-007---navigation-bar-and-task-table-layout) | Navigation bar and task table layout |
| [TC-CMP-008](#tc-cmp-008---dashboard-layout) | Dashboard layout |

## How to run

Run each case once per configuration in [README 2.1](../README.md#21-configurations). Record the verdict for each configuration in the [README 2.2 matrix](../README.md#22-compatibility-smoke-scenarios), not in the case's Actual Result field. Save captures in the configuration's evidence folder from README 2.1, e.g. `evidences/mac-firefox/desktop/` or `evidences/win-chrome/desktop/`. Compare each result with C01. Native dialogs, date pickers and validation popups do not appear in browser or WebDriver screenshots; capture them with an operating-system screenshot.

Shared preconditions for every TC-CMP case: P-APP on the configuration under test; Fixture Set A seeded on that machine on the execution day; the configuration's OS, browser version, viewport and scaling recorded.

## TC-CMP-001 - Register, log in and log out

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-CMP-001 |
| Feature/Requirement | REQ-001, REQ-002 |
| Technique/Test Type | Compatibility |
| Objective | Verify the account flow works the same on the configuration under test. |
| Preconditions | Shared TC-CMP preconditions; logged out |
| Test Data | {"username": "w3<initial>_<config>_<ddmm>", "password": "Test12345"} |
| Steps | 1. Open `/register` and register with the test data.<br>2. Select `Log out`.<br>3. Log in with the same data. |
| Expected Result | Step 1 opens `My Tasks` with the username in the navigation bar. Step 2 returns to `/login`. Step 3 opens `My Tasks`. Pages render and redirect as on C01. Basis: REQ-001, REQ-002. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `evidences/<os>-<browser>/<viewport>/TC-CMP-001-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-CMP-002 - Create a task with the date picker

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-CMP-002 |
| Feature/Requirement | REQ-003, REQ-006 |
| Technique/Test Type | Compatibility |
| Objective | Verify that the browser's date control can be used and the date is saved correctly. |
| Preconditions | Shared TC-CMP preconditions; logged in |
| Test Data | {"title": "CMP-Date", "category": "Study", "dueDate": "today+7, chosen with the picker"} |
| Steps | 1. Open `/tasks/new`.<br>2. Enter the title and category.<br>3. Open the date control and choose the due date with it (not by typing).<br>4. Capture the open picker with an OS screenshot.<br>5. Select `Create Task`. |
| Expected Result | A date picker opens, or a date field that accepts the date if the browser has no picker. The list shows `CMP-Date` with the due date as `YYYY-MM-DD`, whatever the browser's display format, and the badge `Upcoming`. Basis: README task fields; REQ-006. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `evidences/<os>-<browser>/<viewport>/TC-CMP-002-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-CMP-003 - Filter and search

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-CMP-003 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | Compatibility |
| Objective | Verify that the auto-submitting filters and the search work on the configuration under test. |
| Preconditions | Shared TC-CMP preconditions; logged in as account A on that machine |
| Test Data | {"category": "Work", "status": "Open", "q": "GUI"} |
| Steps | 1. Open `/`.<br>2. Choose `Work`, then `Open`.<br>3. Type `GUI` and press Enter.<br>4. Record the listed titles. |
| Expected Result | Each list change applies without selecting `Filter`. The final list contains the same titles as on C01 for the same fixture set (F1 only). Basis: REQ-005. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `evidences/<os>-<browser>/<viewport>/TC-CMP-003-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-CMP-004 - Complete and reopen

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-CMP-004 |
| Feature/Requirement | REQ-004 |
| Technique/Test Type | Compatibility |
| Objective | Verify that the complete/reopen control works and renders on the configuration under test. |
| Preconditions | Shared TC-CMP preconditions; logged in as account A on that machine |
| Test Data | {"fixture": "F3"} |
| Steps | 1. Select `○` on F3 and capture.<br>2. Select `✓` on F3 and capture. |
| Expected Result | The same states as [TC-GUI-011](../1_GUI/test_cases.md#tc-gui-011---complete-and-reopen-button): `✓`, strikethrough and `Done` after step 1; `○`, no strikethrough and `Due Soon` after step 2. Both symbols render as symbols, not as empty boxes. Basis: REQ-004. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `evidences/<os>-<browser>/<viewport>/TC-CMP-004-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-CMP-005 - Edit a task

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-CMP-005 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Compatibility |
| Objective | Verify that the edit form shows saved values, including the date, and saves changes. |
| Preconditions | Shared TC-CMP preconditions; `CMP-Date` from TC-CMP-002 exists |
| Test Data | {"task": "CMP-Date", "newDueDate": "today+10, chosen with the picker"} |
| Steps | 1. Select `Edit` on `CMP-Date`.<br>2. Check that the due date shows today+7.<br>3. Choose the new date with the picker and select `Save Changes`.<br>4. Open `Edit` again. |
| Expected Result | Step 2 shows the saved date. After step 3, the list shows the new date. Step 4 shows the new date in the form. Basis: REQ-003. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `evidences/<os>-<browser>/<viewport>/TC-CMP-005-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-CMP-006 - Delete with confirmation

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-CMP-006 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Compatibility |
| Objective | Verify that the browser's confirmation dialog appears and both answers work. |
| Preconditions | Shared TC-CMP preconditions; `CMP-Date` exists |
| Test Data | {"task": "CMP-Date"} |
| Steps | 1. Select `Delete` on `CMP-Date` and capture the dialog with an OS screenshot.<br>2. Select `Cancel`.<br>3. Select `Delete` again and confirm. |
| Expected Result | The dialog appears with a delete question and two choices. Cancel keeps the task; confirming removes it. Same behaviour as on C01. Basis: REQ-003. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `evidences/<os>-<browser>/<viewport>/TC-CMP-006-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-CMP-007 - Navigation bar and task table layout

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-CMP-007 |
| Feature/Requirement | REQ-002, REQ-003 |
| Technique/Test Type | Compatibility |
| Objective | Verify that the navigation bar and task table are readable at the configuration's viewport (H1, H10). |
| Preconditions | Shared TC-CMP preconditions; logged in as account A on that machine |
| Test Data | {"fixtures": ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]} |
| Steps | 1. Open `/` with no filters.<br>2. Inspect the navigation bar.<br>3. Inspect the table, including F7 and F8.<br>4. Run the horizontal-scroll check from [TC-GUI-019](../1_GUI/test_cases.md#tc-gui-019---long-content) in the browser's console.<br>5. Capture the full page. |
| Expected Result | Each navigation item fits on one line with no overlap. All six table columns are readable with no clipped text or controls. The page does not scroll horizontally, unless a scrolling table is the only cause and it is recorded. Basis: interface; H1; H10. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `evidences/<os>-<browser>/<viewport>/TC-CMP-007-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-CMP-008 - Dashboard layout

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-CMP-008 |
| Feature/Requirement | REQ-007 |
| Technique/Test Type | Compatibility |
| Objective | Verify that the dashboard cards reflow correctly and show the same values as on C01. |
| Preconditions | Shared TC-CMP preconditions; logged in as account A on that machine; same execution day as the C01 run, or C01 values recalculated for the day |
| Test Data | {} |
| Steps | 1. Open `/dashboard`.<br>2. Record the five counter values.<br>3. Capture the page. |
| Expected Result | The five cards do not overlap and wrap into rows as the width shrinks. The counter values equal those on C01 for the same fixture set and date. Basis: REQ-007; interface. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `evidences/<os>-<browser>/<viewport>/TC-CMP-008-<YYYYMMDD>.png` |
| Defect ID | — |
