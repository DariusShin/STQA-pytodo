# Week 3 - Compatibility Test Cases

Detailed cases for [Task 2 - Compatibility/configuration matrix](../README.md#task-2) of the [Week 3 plan](../README.md). Each case uses the guideline's test-case template fields. Precondition codes (P-APP, P-OUT, P-A, P-C), test accounts and fixture IDs (F1-F9) are defined in [fixtures.md](../fixtures.md). Executed by the Playwright suite [test_compatibility.py](test_compatibility.py), once per configuration (`--w3-config <ID>`). C01, C02 and C03 were executed on 2026-11-18 (Chrome 157.0.8103.80, macOS 26.5.2, headless; C02/C03 with Chrome mobile emulation). Recorded runs: C01 [results-C01-20261118-202509.json](evidences/mac-chrome/desktop/results-C01-20261118-202509.json) (first C01 run: [results-C01-20261118-1931.json](evidences/mac-chrome/desktop/results-C01-20261118-1931.json)); C02 [results-C02-20261118-202514.json](evidences/mac-chrome/tablet/results-C02-20261118-202514.json) and [results-C02-20261118-202524.json](evidences/mac-chrome/tablet/results-C02-20261118-202524.json); C03 [results-C03-20261118-202519.json](evidences/mac-chrome/mobile/results-C03-20261118-202519.json) and [results-C03-20261118-202529.json](evidences/mac-chrome/mobile/results-C03-20261118-202529.json). C04 (Firefox 159.0 (Playwright build v1572; the installed Firefox is 160.0.1)) was executed on 2026-11-18: [results-C04-20261118-210941.json](evidences/mac-firefox/desktop/results-C04-20261118-210941.json) and [results-C04-20261118-210946.json](evidences/mac-firefox/desktop/results-C04-20261118-210946.json). C05 (Chrome 124.0.6367.119) and C06 (Firefox 159.0, Playwright build v1572) were executed on 2026-11-24 on Windows 11 build 26200 at 1536x864, headless: C05 [results-C05-20261124-215412.json](evidences/win-chrome/desktop/results-C05-20261124-215412.json) and [results-C05-20261124-215427.json](evidences/win-chrome/desktop/results-C05-20261124-215427.json); C06 [results-C06-20261124-215447.json](evidences/win-firefox/desktop/results-C06-20261124-215447.json) and [results-C06-20261124-215513.json](evidences/win-firefox/desktop/results-C06-20261124-215513.json). Configurations not yet run stay `Not Run`.

**Changes to the scripted checks on 2026-11-18.** The first C02/C03 runs passed TC-CMP-007 because the script checked wrapping and clipping but not the "readable" part of the expected result; the step 6 text-size measurement was added and C01-C03 were re-run under the same check. On emulated devices, screenshots capture the device screen rather than the whole layout. Three runs between 20:20 and 20:24 were discarded because their per-run usernames were stamped only to the minute, so runs started in the same minute shared accounts; the stamp now includes seconds.

## Review sign-off

Expected results must be reviewed before execution (plan step 3). The reviewer checks that each expected result cites a basis from [README 0.3](../README.md#03-test-basis) and was not derived from observed behaviour.

| Reviewer | Date | Cases reviewed | Changes requested | Approved |
| --- | --- | --- | --- | --- |
| Team (verbal approval of execution, recorded by Darius Lee Shin) | 2026-11-18 | TC-CMP-001 to 008 | None recorded | Yes (verbal) |

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
| Actual Result | C01: Registering opened `My Tasks` with the new username in the navigation bar; `Log out` returned to `/login`; logging in again opened `My Tasks`. C02 and C03: same result as C01. C04: same result as C01. C05 and C06: same result as C01. Other configurations: recorded per configuration in README 2.2. |
| Status | C01: Pass. C02: Pass. C03: Pass. C04: Pass. C05: Pass. C06: Pass. C07: Not Run |
| Evidence | Pattern `evidences/<os>-<browser>/<viewport>/TC-CMP-001-<desc>-<YYYYMMDD>.jpg`. C01: [TC-CMP-001-registered-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-001-registered-20261118.jpg)<br>[TC-CMP-001-logged-in-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-001-logged-in-20261118.jpg)<br>C02: [mac-chrome/tablet/](evidences/mac-chrome/tablet/)<br>C03: [mac-chrome/mobile/](evidences/mac-chrome/mobile/)<br>C04: [mac-firefox/desktop/](evidences/mac-firefox/desktop/)<br>C05: [win-chrome/desktop/](evidences/win-chrome/desktop/)<br>C06: [win-firefox/desktop/](evidences/win-firefox/desktop/) |
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
| Actual Result | C01: `CMP-Date` (Study) listed with due date today+7 in `YYYY-MM-DD` and badge `Upcoming`. The date was entered by value; the native picker UI was not exercised. C02 and C03: same result as C01. C04: same result as C01. C05 and C06: same result as C01. Other configurations: recorded per configuration in README 2.2. |
| Status | C01: Pass. C02: Pass. C03: Pass. C04: Pass. C05: Pass. C06: Pass. C07: Not Run |
| Evidence | Pattern `evidences/<os>-<browser>/<viewport>/TC-CMP-002-<desc>-<YYYYMMDD>.jpg`. C01: [TC-CMP-002-created-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-002-created-20261118.jpg)<br>C02: [mac-chrome/tablet/](evidences/mac-chrome/tablet/)<br>C03: [mac-chrome/mobile/](evidences/mac-chrome/mobile/)<br>C04: [mac-firefox/desktop/](evidences/mac-firefox/desktop/)<br>C05: [win-chrome/desktop/](evidences/win-chrome/desktop/)<br>C06: [win-firefox/desktop/](evidences/win-firefox/desktop/) |
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
| Actual Result | C01: Category and status applied on change without `Filter`; the final list contained `GUI-Overdue` only. C02 and C03: same result as C01. C04: same result as C01. C05 and C06: same result as C01. Other configurations: recorded per configuration in README 2.2. |
| Status | C01: Pass. C02: Pass. C03: Pass. C04: Pass. C05: Pass. C06: Pass. C07: Not Run |
| Evidence | Pattern `evidences/<os>-<browser>/<viewport>/TC-CMP-003-<desc>-<YYYYMMDD>.jpg`. C01: [TC-CMP-003-filtered-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-003-filtered-20261118.jpg)<br>C02: [mac-chrome/tablet/](evidences/mac-chrome/tablet/)<br>C03: [mac-chrome/mobile/](evidences/mac-chrome/mobile/)<br>C04: [mac-firefox/desktop/](evidences/mac-firefox/desktop/)<br>C05: [win-chrome/desktop/](evidences/win-chrome/desktop/)<br>C06: [win-firefox/desktop/](evidences/win-firefox/desktop/) |
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
| Actual Result | C01: `✓`, strikethrough and `Done` after completing; `○`, no strikethrough and `Due Soon` after reopening; both symbols rendered as glyphs. C02 and C03: same result as C01. C04: same result as C01. C05 and C06: same result as C01. Other configurations: recorded per configuration in README 2.2. |
| Status | C01: Pass. C02: Pass. C03: Pass. C04: Pass. C05: Pass. C06: Pass. C07: Not Run |
| Evidence | Pattern `evidences/<os>-<browser>/<viewport>/TC-CMP-004-<desc>-<YYYYMMDD>.jpg`. C01: [TC-CMP-004-done-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-004-done-20261118.jpg)<br>[TC-CMP-004-reopened-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-004-reopened-20261118.jpg)<br>C02: [mac-chrome/tablet/](evidences/mac-chrome/tablet/)<br>C03: [mac-chrome/mobile/](evidences/mac-chrome/mobile/)<br>C04: [mac-firefox/desktop/](evidences/mac-firefox/desktop/)<br>C05: [win-chrome/desktop/](evidences/win-chrome/desktop/)<br>C06: [win-firefox/desktop/](evidences/win-firefox/desktop/) |
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
| Actual Result | C01: The edit form showed the saved date; the new date (today+10) was saved, listed and shown again in the form. C02 and C03: same result as C01. C04: same result as C01. C05 and C06: same result as C01. Other configurations: recorded per configuration in README 2.2. |
| Status | C01: Pass. C02: Pass. C03: Pass. C04: Pass. C05: Pass. C06: Pass. C07: Not Run |
| Evidence | Pattern `evidences/<os>-<browser>/<viewport>/TC-CMP-005-<desc>-<YYYYMMDD>.jpg`. C01: [TC-CMP-005-edited-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-005-edited-20261118.jpg)<br>C02: [mac-chrome/tablet/](evidences/mac-chrome/tablet/)<br>C03: [mac-chrome/mobile/](evidences/mac-chrome/mobile/)<br>C04: [mac-firefox/desktop/](evidences/mac-firefox/desktop/)<br>C05: [win-chrome/desktop/](evidences/win-chrome/desktop/)<br>C06: [win-firefox/desktop/](evidences/win-firefox/desktop/) |
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
| Actual Result | C01: Confirmation dialog `Delete this task?` appeared (recorded text); Cancel kept the task and OK removed it. C02 and C03: same result as C01. C04: same result as C01. C05 and C06: same result as C01. Other configurations: recorded per configuration in README 2.2. |
| Status | C01: Pass. C02: Pass. C03: Pass. C04: Pass. C05: Pass. C06: Pass. C07: Not Run |
| Evidence | Pattern `evidences/<os>-<browser>/<viewport>/TC-CMP-006-<desc>-<YYYYMMDD>.jpg`. C01: [TC-CMP-006-deleted-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-006-deleted-20261118.jpg)<br>C02: [mac-chrome/tablet/](evidences/mac-chrome/tablet/)<br>C03: [mac-chrome/mobile/](evidences/mac-chrome/mobile/)<br>C04: [mac-firefox/desktop/](evidences/mac-firefox/desktop/)<br>C05: [win-chrome/desktop/](evidences/win-chrome/desktop/)<br>C06: [win-firefox/desktop/](evidences/win-firefox/desktop/) |
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
| Steps | 1. Open `/` with no filters.<br>2. Inspect the navigation bar.<br>3. Inspect the table, including F7 and F8.<br>4. Run the horizontal-scroll check from [TC-GUI-019](../1_GUI/test_cases.md#tc-gui-019---long-content) in the browser's console.<br>5. Capture the page.<br>6. Measure the smallest navigation and table text as rendered on the device screen (CSS font size x page scale) against the 12 px legibility threshold used by Lighthouse. |
| Expected Result | Each navigation item fits on one line with no overlap. All six table columns are readable with no clipped text or controls. The page does not scroll horizontally, unless a scrolling table is the only cause and it is recorded. Basis: interface; H1; H10. |
| Actual Result | C01: At 1440x900 every navigation item fits on one line within the viewport with no overlap; all six table columns are within the viewport; no horizontal page scroll. C02 and C03: navigation and table fit without wrapping or clipping, but the page is laid out at 980 CSS px and scaled down to fit the screen (H1), so the smallest navigation/table text renders at **9.8 px on C02** and **5.0 px on C03**, below the 12 px legibility threshold. C04: navigation and table fit and text renders at 12.5 px or more; cosmetic differences from Chrome (larger `○` glyph, due dates on one line, table about 40 px wider than its container) do not affect any check. C05 and C06: at 1536x864 every navigation item fits on one line within the viewport with no overlap; all six table columns are within the viewport; no horizontal page scroll; smallest text renders at 12.5 px. Pages render in Segoe UI rather than the macOS system font, and Firefox's `○` glyph is the same size as Chrome's; neither affects any check. Other configurations: recorded per configuration in README 2.2. |
| Status | C01: Pass. C02: Fail. C03: Fail. C04: Pass. C05: Pass. C06: Pass. C07: Not Run |
| Evidence | Pattern `evidences/<os>-<browser>/<viewport>/TC-CMP-007-<desc>-<YYYYMMDD>.jpg`. C01: [TC-CMP-007-layout-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-007-layout-20261118.jpg)<br>C02: [mac-chrome/tablet/](evidences/mac-chrome/tablet/)<br>C03: [mac-chrome/mobile/](evidences/mac-chrome/mobile/)<br>C04: [mac-firefox/desktop/](evidences/mac-firefox/desktop/)<br>C05: [win-chrome/desktop/](evidences/win-chrome/desktop/)<br>C06: [win-firefox/desktop/](evidences/win-firefox/desktop/) |
| Defect ID | DEF-006 (C02, C03) |

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
| Actual Result | C01: Cards do not overlap. Counter values on 2026-11-18: Total Tasks 9, Open 8, Overdue 2, Due Soon 1, Completed (last 7 days) 1. These are the C01 reference values for same-day comparison. C02 and C03: cards do not overlap; counter values identical to C01 (9, 8, 2, 1, 1). C04: cards do not overlap; counter values identical to C01 on the same day. C05 and C06 (run on 2026-11-24, no same-day C01 run): cards do not overlap; counter values 9, 8, 2, 1, 1, equal to the C01 values recalculated for that date (Fixture Set A dates are relative to the run date). Other configurations: recorded per configuration in README 2.2. |
| Status | C01: Pass. C02: Pass. C03: Pass. C04: Pass. C05: Pass. C06: Pass. C07: Not Run |
| Evidence | Pattern `evidences/<os>-<browser>/<viewport>/TC-CMP-008-<desc>-<YYYYMMDD>.jpg`. C01: [TC-CMP-008-dashboard-20261118.jpg](evidences/mac-chrome/desktop/TC-CMP-008-dashboard-20261118.jpg)<br>C02: [mac-chrome/tablet/](evidences/mac-chrome/tablet/)<br>C03: [mac-chrome/mobile/](evidences/mac-chrome/mobile/)<br>C04: [mac-firefox/desktop/](evidences/mac-firefox/desktop/)<br>C05: [win-chrome/desktop/](evidences/win-chrome/desktop/)<br>C06: [win-firefox/desktop/](evidences/win-firefox/desktop/) |
| Defect ID | — |
