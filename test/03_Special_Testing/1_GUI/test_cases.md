# Week 3 - GUI Test Cases

Detailed cases for [Task 1 - GUI checklist](../README.md#task-1) of the [Week 3 plan](../README.md). Each case uses the guideline's test-case template fields. Precondition codes (P-APP, P-OUT, P-A, P-C), test accounts and fixture IDs (F1-F9) are defined in [fixtures.md](../fixtures.md). Executed on 2026-11-18 on C01 (Chrome 157.0.8103.80, macOS 26.5.2, 1440x900, headless) by the Playwright suite [test_gui.py](test_gui.py), run twice: [results-C01-20261118-1933.json](evidences/results-C01-20261118-1933.json) is the recorded run, and `results-C01-20261118-1928.json` is the first reproduction. In the first run the TC-GUI-010 colour comparison was keyed on the expected class rather than the displayed one; the check was corrected before the recorded run.

## Review sign-off

Expected results must be reviewed before execution (plan step 3). The reviewer checks that each expected result cites a basis from [README 0.3](../README.md#03-test-basis) and was not derived from observed behaviour.

| Reviewer | Date | Cases reviewed | Changes requested | Approved |
| --- | --- | --- | --- | --- |
| Team (verbal approval of execution, recorded by Darius Lee Shin) | 2026-11-18 | TC-GUI-001 to 022 | None recorded | Yes (verbal) |

## Case index

| ID | Title |
| --- | --- |
| [TC-GUI-001](#tc-gui-001---login-page-layout) | Login page layout |
| [TC-GUI-002](#tc-gui-002---login-error-message) | Login error message |
| [TC-GUI-003](#tc-gui-003---registration-hints) | Registration hints |
| [TC-GUI-004](#tc-gui-004---registration-error-messages) | Registration error messages |
| [TC-GUI-005](#tc-gui-005---navigation-bar) | Navigation bar |
| [TC-GUI-006](#tc-gui-006---brand-link) | Brand link |
| [TC-GUI-007](#tc-gui-007---task-list-header) | Task list header |
| [TC-GUI-008](#tc-gui-008---filter-controls) | Filter controls |
| [TC-GUI-009](#tc-gui-009---task-table-and-empty-state) | Task table and empty state |
| [TC-GUI-010](#tc-gui-010---urgency-badges) | Urgency badges |
| [TC-GUI-011](#tc-gui-011---complete-and-reopen-button) | Complete and reopen button |
| [TC-GUI-012](#tc-gui-012---edit-link-opens-a-pre-filled-form) | Edit link opens a pre-filled form |
| [TC-GUI-013](#tc-gui-013---delete-confirmation) | Delete confirmation |
| [TC-GUI-014](#tc-gui-014---new-task-form) | New Task form |
| [TC-GUI-015](#tc-gui-015---edit-task-form) | Edit Task form |
| [TC-GUI-016](#tc-gui-016---required-title) | Required title |
| [TC-GUI-017](#tc-gui-017---feedback-after-actions) | Feedback after actions |
| [TC-GUI-018](#tc-gui-018---dashboard-cards) | Dashboard cards |
| [TC-GUI-019](#tc-gui-019---long-content) | Long content |
| [TC-GUI-020](#tc-gui-020---special-characters) | Special characters |
| [TC-GUI-021](#tc-gui-021---page-titles) | Page titles |
| [TC-GUI-022](#tc-gui-022---visual-consistency) | Visual consistency |

## TC-GUI-001 - Login page layout

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-001 |
| Feature/Requirement | REQ-002 - Login page `/login` |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the login page shows every element needed to log in, in a clear layout. |
| Preconditions | P-OUT |
| Test Data | {"password": "abc"} |
| Steps | 1. Open `/login`.<br>2. Inspect the heading, field labels, inputs, button and link.<br>3. Type the test password into Password.<br>4. Capture the page. |
| Expected Result | Heading `Log in`. `Username` and `Password` labels, each directly above its input. A `Log in` button. The text `No account? Register`, where `Register` links to `/register`. Password characters are masked. All elements sit in one card with consistent spacing. Basis: interface and README page list. |
| Actual Result | Heading `Log in`; `Username` and `Password` labels each directly above their inputs; one `Log in` button; `No account? Register` with `Register` linking to `/register`; the typed password is masked; all four controls are inside one card. Spacing judged consistent from the screenshot. |
| Status | Pass |
| Evidence | [TC-GUI-001-login-layout-20261118.jpg](evidences/TC-GUI-001-login-layout-20261118.jpg) |
| Defect ID | — |

## TC-GUI-002 - Login error message

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-002 |
| Feature/Requirement | REQ-002 - Login page `/login` |
| Technique/Test Type | GUI checklist |
| Objective | Verify that failed login shows a visible, understandable error. |
| Preconditions | P-OUT; account A exists |
| Test Data | {"username": "w3<initial>_gui_<ddmm>", "password": "WrongPass1"} |
| Steps | 1. Open `/login`.<br>2. Enter the test data.<br>3. Select `Log in`.<br>4. Observe the page and the URL.<br>5. Record whether the Username field still contains the entered value. |
| Expected Result | The browser stays on `/login`. An error message is shown above the form in a visually distinct box and says the login failed. It does not reveal whether the username or the password was wrong. Step 5 is recorded as an observation for Task 3 and does not affect the verdict. Basis: REQ-002; interface. |
| Actual Result | Stayed on `/login`. `Invalid username or password.` is shown above the form in a red box distinct from the white card, and does not say which field was wrong. Observation for Task 3: the Username field is emptied after the error. |
| Status | Pass |
| Evidence | [TC-GUI-002-login-error-20261118.jpg](evidences/TC-GUI-002-login-error-20261118.jpg) |
| Defect ID | USA-OBS-004 (observation) |

## TC-GUI-003 - Registration hints

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-003 |
| Feature/Requirement | REQ-001 - Register page `/register` |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the input rules are visible before the user types. |
| Preconditions | P-OUT |
| Test Data | {} |
| Steps | 1. Open `/register`.<br>2. Inspect the labels and hints without entering data.<br>3. Capture the page. |
| Expected Result | Heading `Create an account`. The Username label shows `(3-20 chars, letters/numbers/underscore)` and the Password label shows `(min 8 characters)`, each next to its own label and readable at normal zoom. A `Register` button and a `Log in` link to `/login`. Contrast is measured separately in TC-A11Y-004. Basis: interface. |
| Actual Result | Heading `Create an account`; `(3-20 chars, letters/numbers/underscore)` and `(min 8 characters)` shown beside their labels at 12.8 px; `Register` button and `Log in` link to `/login` present. |
| Status | Pass |
| Evidence | [TC-GUI-003-register-hints-20261118.jpg](evidences/TC-GUI-003-register-hints-20261118.jpg) |
| Defect ID | — |

## TC-GUI-004 - Registration error messages

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-004 |
| Feature/Requirement | REQ-001 - Register page `/register` |
| Technique/Test Type | GUI checklist |
| Objective | Verify that each invalid registration shows a message naming the broken rule, and re-check DEF-001 in the GUI. |
| Preconditions | P-OUT |
| Test Data | {"submission1": {"username": "ab", "password": "Test12345"}, "submission2": {"username": "w3<initial>_short_<ddmm>", "password": "Test123"}, "submission3": {"username": "w3<initial>_p8_<ddmm>", "password": "Test1234"}} |
| Steps | 1. Open `/register`.<br>2. Enter submission 1 and select `Register`. Capture the result.<br>3. Enter submission 2 and select `Register`. Capture the result.<br>4. Enter submission 3 and select `Register`. Capture the result.<br>5. For steps 2 and 3, record which fields kept their values. |
| Expected Result | Submission 1: stays on `/register` with a message stating the username rule (3-20 characters, letters/numbers/underscore). Submission 2 (7 characters): stays on `/register` with a message stating the password minimum of 8 characters. Submission 3 (8 characters): accepted, because the hint says `min 8 characters`; the browser shows `My Tasks`. Messages appear in the same error style as on the login page. Basis: interface hints; REQ-001. |
| Actual Result | Submission 1: stayed on `/register` with `Username must be 3-20 characters (letters, numbers, underscore).` Submission 2 (7 characters): stayed with `Password must be at least 8 characters.` Submission 3 (8 characters, `Test1234`): **rejected** with `Password must be at least 8 characters.`, contradicting the `min 8 characters` hint. Messages use the same style as the login error. Both fields are emptied after every error. |
| Status | Fail |
| Evidence | [TC-GUI-004-register-errors-s1-20261118.jpg](evidences/TC-GUI-004-register-errors-s1-20261118.jpg)<br>[TC-GUI-004-register-errors-s2-20261118.jpg](evidences/TC-GUI-004-register-errors-s2-20261118.jpg)<br>[TC-GUI-004-register-errors-s3-20261118.jpg](evidences/TC-GUI-004-register-errors-s3-20261118.jpg) |
| Defect ID | DEF-001 (reproduced) |

## TC-GUI-005 - Navigation bar

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-005 |
| Feature/Requirement | REQ-002 - Shared navigation bar |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the navigation bar matches the login state and stays readable at desktop and narrow widths (H10). |
| Preconditions | P-OUT; account A exists |
| Test Data | {"narrowViewport": "390x844, DevTools device toolbar, Responsive, device type Desktop"} |
| Steps | 1. Open `/login` and inspect the navigation bar.<br>2. Log in as account A.<br>3. Inspect the navigation bar on `/`, `/tasks/new` and `/dashboard`.<br>4. Open the DevTools device toolbar, set the narrow viewport and repeat step 3.<br>5. Capture each state. |
| Expected Result | Logged out: the brand `PyTodo Pro` only. Logged in, on every page: `Tasks`, `Dashboard`, the logged-in username and `Log out`. At both widths, each item fits on one line, no items overlap, and every item can be clicked. Basis: README page list; interface; H10. |
| Actual Result | Logged out: brand only. Logged in: `Tasks`, `Dashboard`, username and `Log out` on `/`, `/tasks/new` and `/dashboard`. At 1440 px every item is on one line with no overlap. At 390 px (desktop Chrome window resized to 390x844) the brand wraps to `PyTodo / Pro` and `Log out` wraps to two lines and is pushed past the right edge of the viewport on all three pages. |
| Status | Fail |
| Evidence | [TC-GUI-005-nav-logged-out-20261118.jpg](evidences/TC-GUI-005-nav-logged-out-20261118.jpg)<br>[TC-GUI-005-nav-1440-20261118.jpg](evidences/TC-GUI-005-nav-1440-20261118.jpg)<br>[TC-GUI-005-nav-390-20261118.jpg](evidences/TC-GUI-005-nav-390-20261118.jpg) |
| Defect ID | DEF-004 |

## TC-GUI-006 - Brand link

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-006 |
| Feature/Requirement | REQ-002 - Shared navigation bar |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the brand link leads somewhere sensible for both login states. |
| Preconditions | P-A |
| Test Data | {} |
| Steps | 1. Open `/dashboard`.<br>2. Select the `PyTodo Pro` brand and note the URL.<br>3. Select `Log out`.<br>4. On `/login`, select the brand and note the URL. |
| Expected Result | Step 2 opens the task list `/`. Step 4 stays on `/login`; a logged-out user is not sent to a protected page. Basis: REQ-002. |
| Actual Result | From `/dashboard` the brand opened `/`. After logging out, the brand on `/login` stayed on `/login`. |
| Status | Pass |
| Evidence | [TC-GUI-006-brand-link-20261118.jpg](evidences/TC-GUI-006-brand-link-20261118.jpg) |
| Defect ID | — |

## TC-GUI-007 - Task list header

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-007 |
| Feature/Requirement | REQ-003 - Task list `/` |
| Technique/Test Type | GUI checklist |
| Objective | Verify the task list heading and the New Task button. |
| Preconditions | P-A |
| Test Data | {} |
| Steps | 1. Open `/`.<br>2. Inspect the page header.<br>3. Select `+ New Task`. |
| Expected Result | Heading `My Tasks` on the left and a `+ New Task` button on the right of the same row. Step 3 opens `/tasks/new` with the heading `New Task`. Basis: interface; README. |
| Actual Result | `My Tasks` on the left and `+ New Task` on the right of the same row; the button opened `/tasks/new` with heading `New Task`. |
| Status | Pass |
| Evidence | [TC-GUI-007-list-header-20261118.jpg](evidences/TC-GUI-007-list-header-20261118.jpg) |
| Defect ID | — |

## TC-GUI-008 - Filter controls

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-008 |
| Feature/Requirement | REQ-005 - Category/status filters and title search |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the filter controls behave predictably and show the active filters. |
| Preconditions | P-A |
| Test Data | {"category": "Work", "status": "Open", "q": "GUI"} |
| Steps | 1. Open `/`.<br>2. Choose `Work` in the category list and note whether the page reloads without selecting `Filter`.<br>3. Choose `Open` in the status list and observe.<br>4. Type `GUI` in the search box and press Enter.<br>5. Clear the search box and select `Filter`.<br>6. Reload the page.<br>7. Record whether each control has a visible label (input for TC-A11Y-006). |
| Expected Result | Steps 2 and 3 apply the filter immediately. Step 4 applies the search with Enter and step 5 with the `Filter` button. After every reload, the chosen category, status and search text remain shown in their controls. The listed tasks satisfy all active filters (only F1 after step 4). Basis: REQ-005; interface. |
| Actual Result | Choosing `Work` and then `Open` reloaded the list immediately without `Filter`; the search applied with Enter and with the `Filter` button; only `GUI-Overdue` was listed; the selected category, status and search text stayed in their controls after each reload. Input for TC-A11Y-006: the filter form has no visible labels; the search box has only the placeholder `Search title...`. |
| Status | Pass |
| Evidence | [TC-GUI-008-filters-applied-20261118.jpg](evidences/TC-GUI-008-filters-applied-20261118.jpg) |
| Defect ID | — |

## TC-GUI-009 - Task table and empty state

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-009 |
| Feature/Requirement | REQ-003, REQ-005 - Task list `/` |
| Technique/Test Type | GUI checklist |
| Objective | Verify the table headers and the message shown when there are no tasks to list. |
| Preconditions | P-A for steps 1-3; P-C for step 4 |
| Test Data | {"q": "NO-SUCH-TITLE-W3"} |
| Steps | 1. Open `/` and inspect the table header row.<br>2. Search for the test data.<br>3. Capture the empty result.<br>4. Log in as account C, open `/` and capture. |
| Expected Result | The Title, Category, Due Date and Urgency columns have headers; the complete/reopen and action columns can be identified by their controls. In steps 2 and 4, a single message that no tasks match is shown inside the table area, not a blank table. Basis: interface; README. |
| Actual Result | `Title`, `Category`, `Due Date` and `Urgency` have headers; the first and last columns have empty headers and are identified by the `○`/`✓` buttons and the `Edit`/`Delete` actions. A no-match search and the empty account C each show a single row `No tasks match your filters.` |
| Status | Pass |
| Evidence | [TC-GUI-009-empty-search-20261118.jpg](evidences/TC-GUI-009-empty-search-20261118.jpg)<br>[TC-GUI-009-empty-account-20261118.jpg](evidences/TC-GUI-009-empty-account-20261118.jpg) |
| Defect ID | — |

## TC-GUI-010 - Urgency badges

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-010 |
| Feature/Requirement | REQ-006 - Due-date urgency |
| Technique/Test Type | GUI checklist |
| Objective | Verify that each urgency class appears as its own labelled, distinguishable badge, and re-check DEF-002 in the GUI. |
| Preconditions | P-A |
| Test Data | {"fixtures": ["F1", "F2", "F3", "F4", "F5", "F6"]} |
| Steps | 1. Open `/` with no filters.<br>2. Record the badge text and colour for F1-F6.<br>3. Capture the table. |
| Expected Result | F1 `Overdue`, F2 `Due Today`, F3 `Due Soon`, F4 `Upcoming`, F5 `No due date`, F6 `Done`. Each badge shows its text. Overdue, Due Today, Due Soon and Upcoming can each be told apart by appearance. Basis: README urgency classes; Week 1 urgency contract. |
| Actual Result | F1 `Overdue`, F3 `Due Soon`, F4 `Upcoming`, F5 `No due date` and F6 `Done` as expected. **F2 (due today) shows `Overdue`** (DEF-002 reproduced). Overdue, Due Soon and Upcoming have distinct colours; `Due Today` is never displayed, so its appearance could not be compared. `No due date` and `Done` share the same grey style. |
| Status | Fail |
| Evidence | [TC-GUI-010-badges-20261118.jpg](evidences/TC-GUI-010-badges-20261118.jpg) |
| Defect ID | DEF-002 (reproduced) |

## TC-GUI-011 - Complete and reopen button

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-011 |
| Feature/Requirement | REQ-004 - Complete and reopen tasks |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the complete/reopen control and the row styling reflect the task state. |
| Preconditions | P-A |
| Test Data | {"fixture": "F3"} |
| Steps | 1. Open `/` and locate F3.<br>2. Select its `○` button and capture the row.<br>3. Select its `✓` button and capture the row. |
| Expected Result | After step 2: the button shows `✓`, the title is struck through and the badge shows `Done`. After step 3: the button shows `○`, the strikethrough is removed and the badge returns to `Due Soon`. Basis: REQ-004; README urgency classes. |
| Actual Result | After completing F3: `✓`, title struck through, badge `Done`. After reopening: `○`, no strikethrough, badge `Due Soon`. |
| Status | Pass |
| Evidence | [TC-GUI-011-toggle-done-20261118.jpg](evidences/TC-GUI-011-toggle-done-20261118.jpg)<br>[TC-GUI-011-toggle-open-20261118.jpg](evidences/TC-GUI-011-toggle-open-20261118.jpg) |
| Defect ID | — |

## TC-GUI-012 - Edit link opens a pre-filled form

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-012 |
| Feature/Requirement | REQ-003 - Edit task |
| Technique/Test Type | GUI checklist |
| Objective | Verify that Edit opens the form with the saved values. |
| Preconditions | P-A |
| Test Data | {"fixture": "F3"} |
| Steps | 1. Open `/`.<br>2. Select `Edit` on F3.<br>3. Compare each field with the Fixture Set A values. |
| Expected Result | Title `GUI-Soon`, Description `Week 3 GUI fixture`, Category `Study` selected, and Due Date showing F3's date. Basis: REQ-003. |
| Actual Result | Form pre-filled with `GUI-Soon`, `Week 3 GUI fixture`, `Study` and F3's due date. |
| Status | Pass |
| Evidence | [TC-GUI-012-edit-prefill-20261118.jpg](evidences/TC-GUI-012-edit-prefill-20261118.jpg) |
| Defect ID | — |

## TC-GUI-013 - Delete confirmation

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-013 |
| Feature/Requirement | REQ-003 - Delete task |
| Technique/Test Type | GUI checklist |
| Objective | Verify that deleting a task asks for confirmation and that both answers behave correctly. |
| Preconditions | P-A |
| Test Data | {"title": "GUI-DeleteMe"} |
| Steps | 1. Create a task titled `GUI-DeleteMe` with no other fields.<br>2. Select `Delete` on it.<br>3. Capture the dialog with a macOS screenshot (Shift-Command-4), because browser screenshots omit native dialogs.<br>4. Select `Cancel` and check the list.<br>5. Select `Delete` again and choose `OK`.<br>6. Check the list. |
| Expected Result | A confirmation dialog asks whether to delete the task and offers Cancel and OK. After Cancel, `GUI-DeleteMe` is still listed. After OK, it is no longer listed and all other tasks are unchanged. Basis: REQ-003; Week 1 delete cases. |
| Actual Result | A confirmation dialog `Delete this task?` (type confirm, OK/Cancel) appeared; text recorded by Playwright because native dialogs are not drawn in page screenshots. Cancel kept `GUI-DeleteMe`; OK removed it; all other tasks unchanged. |
| Status | Pass |
| Evidence | [TC-GUI-013-before-delete-20261118.jpg](evidences/TC-GUI-013-before-delete-20261118.jpg)<br>[TC-GUI-013-after-delete-20261118.jpg](evidences/TC-GUI-013-after-delete-20261118.jpg) |
| Defect ID | — |

## TC-GUI-014 - New Task form

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-014 |
| Feature/Requirement | REQ-003 - Create task `/tasks/new` |
| Technique/Test Type | GUI checklist |
| Objective | Verify the fields, controls and Cancel behaviour of the New Task form. |
| Preconditions | P-A |
| Test Data | {"title": "GUI-CancelMe"} |
| Steps | 1. Open `/tasks/new`.<br>2. Inspect the labels and controls.<br>3. Open the Category list and record its options.<br>4. Open the Due Date picker.<br>5. Type the test title and select `Cancel`.<br>6. Check the task list. |
| Expected Result | Heading `New Task`. Labelled `Title`, `Description` (multi-line), `Category` and `Due Date` fields. Category offers `None` plus Work, Personal, Study and Urgent. Due Date opens a date picker. A primary `Create Task` button and a secondary `Cancel` button. After Cancel, the browser returns to `/` and `GUI-CancelMe` is not created. Basis: README; interface. |
| Actual Result | Heading `New Task`; labelled `Title`, multi-line `Description`, `Category` and `Due Date`; Category offers `None`, Personal, Study, Urgent, Work; Due Date is a date control (the native picker cannot be opened by automation); `Create Task` styled as primary and `Cancel` as secondary; Cancel returned to `/` without creating `GUI-CancelMe`. |
| Status | Pass |
| Evidence | [TC-GUI-014-new-form-20261118.jpg](evidences/TC-GUI-014-new-form-20261118.jpg) |
| Defect ID | — |

## TC-GUI-015 - Edit Task form

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-015 |
| Feature/Requirement | REQ-003 - Edit task `/tasks/<id>/edit` |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the edit form is labelled as editing and that Cancel and Save behave differently. |
| Preconditions | P-A |
| Test Data | {"fixture": "F4", "newTitle": "GUI-Upcoming-edited"} |
| Steps | 1. Select `Edit` on F4.<br>2. Inspect the heading and buttons.<br>3. Change the title to the new title and select `Cancel`.<br>4. Check F4 in the list.<br>5. Edit F4 again, change the title and select `Save Changes`.<br>6. Check the list, then edit the title back to `GUI-Upcoming`. |
| Expected Result | Heading `Edit Task` and a `Save Changes` button instead of `Create Task`. After step 3, F4 is still titled `GUI-Upcoming`. After step 5, F4 is titled `GUI-Upcoming-edited`. Basis: REQ-003; interface. |
| Actual Result | Heading `Edit Task` with `Save Changes` and no `Create Task`. Cancel left F4 as `GUI-Upcoming`; Save changed it to `GUI-Upcoming-edited`. Title restored afterwards. |
| Status | Pass |
| Evidence | [TC-GUI-015-edit-form-20261118.jpg](evidences/TC-GUI-015-edit-form-20261118.jpg)<br>[TC-GUI-015-after-save-20261118.jpg](evidences/TC-GUI-015-after-save-20261118.jpg) |
| Defect ID | — |

## TC-GUI-016 - Required title

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-016 |
| Feature/Requirement | REQ-003 - Create task |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the form blocks an empty or whitespace-only title with a visible message, and re-check DEF-003 in the GUI. |
| Preconditions | P-A |
| Test Data | {"submission1": {"title": ""}, "submission2": {"title": "   "}} |
| Steps | 1. Open `/tasks/new`.<br>2. Leave Title empty and select `Create Task`. Capture the result.<br>3. Enter three spaces as Title and select `Create Task`. Capture the result.<br>4. Check the task list for new rows. |
| Expected Result | Both submissions are blocked with a visible message on the Title field asking for a valid title, and no task is created. Basis: Title is required (interface); Week 1 assumption 2 for whitespace-only titles. |
| Actual Result | Empty title: blocked by the browser message `Please fill in this field.` on Title. Whitespace-only title: **submitted and created a task** (9 rows before, 10 after) instead of being blocked (DEF-003 reproduced). The blank task was deleted after the case. |
| Status | Fail |
| Evidence | [TC-GUI-016-empty-title-20261118.jpg](evidences/TC-GUI-016-empty-title-20261118.jpg)<br>[TC-GUI-016-whitespace-title-20261118.jpg](evidences/TC-GUI-016-whitespace-title-20261118.jpg) |
| Defect ID | DEF-003 (reproduced) |

## TC-GUI-017 - Feedback after actions

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-017 |
| Feature/Requirement | REQ-003, REQ-004 - Task actions |
| Technique/Test Type | GUI checklist / Usability heuristic |
| Objective | Verify that the user is told that each task action succeeded (H6). |
| Preconditions | P-A |
| Test Data | {"title": "GUI-Feedback", "editedTitle": "GUI-Feedback-2"} |
| Steps | 1. Create `GUI-Feedback` and capture the resulting page.<br>2. Edit it to `GUI-Feedback-2` and capture.<br>3. Complete it and capture.<br>4. Delete it (OK in the dialog) and capture. |
| Expected Result | After each action, the resulting page shows a confirmation message (for example `Task created`) or visibly highlights the affected task. Basis: Nielsen heuristic 1, visibility of system status. No stated requirement covers this, so a failure is recorded as a `USA-OBS-` observation, not a `DEF-`. |
| Actual Result | No confirmation message and no highlighted task after create, edit, complete or delete; the page simply returns to the task list. |
| Status | Fail |
| Evidence | [TC-GUI-017-feedback-create-20261118.jpg](evidences/TC-GUI-017-feedback-create-20261118.jpg)<br>[TC-GUI-017-feedback-edit-20261118.jpg](evidences/TC-GUI-017-feedback-edit-20261118.jpg)<br>[TC-GUI-017-feedback-complete-20261118.jpg](evidences/TC-GUI-017-feedback-complete-20261118.jpg)<br>[TC-GUI-017-feedback-delete-20261118.jpg](evidences/TC-GUI-017-feedback-delete-20261118.jpg) |
| Defect ID | USA-OBS-001 |

## TC-GUI-018 - Dashboard cards

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-018 |
| Feature/Requirement | REQ-007 - Dashboard `/dashboard` |
| Technique/Test Type | GUI checklist |
| Objective | Verify that the dashboard shows five clearly labelled counters with consistent colours. |
| Preconditions | P-A |
| Test Data | {} |
| Steps | 1. Open `/dashboard`.<br>2. Record each card's label and value colour.<br>3. Compare the colours with the matching urgency badges from TC-GUI-010.<br>4. Capture the page. |
| Expected Result | Heading `Dashboard` and five cards labelled `Total Tasks`, `Open`, `Overdue`, `Due Soon` and `Completed (last 7 days)`, each with its number above its label. A card with the same meaning as a badge uses the same colour family as that badge. Counter values are checked in Week 1 (REQ-007) and are not judged here. Basis: README dashboard description; interface. |
| Actual Result | Heading `Dashboard`; five cards labelled `Total Tasks`, `Open`, `Overdue`, `Due Soon`, `Completed (last 7 days)`, each number above its label. Overdue and Due Soon cards match their badge colours; **`Completed (last 7 days)` is green while the `Done` badge is grey**. |
| Status | Fail |
| Evidence | [TC-GUI-018-dashboard-20261118.jpg](evidences/TC-GUI-018-dashboard-20261118.jpg) |
| Defect ID | USA-OBS-002 |

## TC-GUI-019 - Long content

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-019 |
| Feature/Requirement | REQ-003 - Task list `/` |
| Technique/Test Type | GUI checklist |
| Objective | Verify that long and unbroken titles do not break the layout. |
| Preconditions | P-A |
| Test Data | {"fixtures": ["F7", "F8"], "viewport": "1440x900"} |
| Steps | 1. Open `/` with no filters.<br>2. Inspect the F7 and F8 rows.<br>3. In the DevTools console, run `document.documentElement.scrollWidth > document.documentElement.clientWidth` and record the result.<br>4. Capture the full page. |
| Expected Result | F7 wraps within the Title cell. F8 does not push the table outside the page container. The other columns stay readable. Step 3 returns `false`, meaning there is no horizontal page scroll. Basis: interface; visual consistency (guideline activity A1). |
| Actual Result | F7 wraps within the Title cell; the table stays inside the page container; F8 fits in its cell; no horizontal page scroll at 1440 px. |
| Status | Pass |
| Evidence | [TC-GUI-019-long-content-20261118.jpg](evidences/TC-GUI-019-long-content-20261118.jpg) |
| Defect ID | — |

## TC-GUI-020 - Special characters

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-020 |
| Feature/Requirement | REQ-003 - Task list and edit form |
| Technique/Test Type | GUI checklist |
| Objective | Verify that a title is displayed exactly as entered (H9). |
| Preconditions | P-A |
| Test Data | {"fixture": "F9"} |
| Steps | 1. Open `/` and inspect the F9 title.<br>2. Select `Edit` on F9 and inspect the Title field.<br>3. Capture both. |
| Expected Result | The list and the edit form both show the exact characters entered, including the literal text `<b>bold</b>`, with no bold formatting applied. `&`, both kinds of quotes, `Résumé` and `报告` display correctly. Basis: REQ-003, saved task information persists as entered. If the tags are rendered as formatting, log a defect and add it to the Week 5 STRIDE table; do not test scripts in Week 3. |
| Actual Result | The list shows `GUI-Special & bold "double" 'single' Résumé 报告` with **`bold` rendered in bold**: the `<b>` tags are interpreted as HTML instead of displayed. The edit form shows the exact title. `&`, quotes, `Résumé` and `报告` display correctly. Logged for the Week 5 STRIDE table (H9); no script payloads were used. |
| Status | Fail |
| Evidence | [TC-GUI-020-special-list-20261118.jpg](evidences/TC-GUI-020-special-list-20261118.jpg)<br>[TC-GUI-020-special-edit-20261118.jpg](evidences/TC-GUI-020-special-edit-20261118.jpg) |
| Defect ID | DEF-005 |

## TC-GUI-021 - Page titles

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-021 |
| Feature/Requirement | All pages |
| Technique/Test Type | GUI checklist |
| Objective | Verify that each browser tab title identifies the page. |
| Preconditions | P-OUT for the first two pages; P-A for the rest |
| Test Data | {} |
| Steps | 1. Open `/login`, `/register`, `/`, `/tasks/new`, `/tasks/<F3 id>/edit` and `/dashboard` in turn.<br>2. Record each tab title exactly. |
| Expected Result | Each of the six titles is different, names its page and includes the application name. Basis: interface consistency; WCAG 2.4.2 (see TC-A11Y-010). |
| Actual Result | Titles: `Log in — PyTodo Pro`, `Register — PyTodo Pro`, `Tasks — PyTodo Pro`, `New Task — PyTodo Pro`, `Edit Task — PyTodo Pro`, `Dashboard — PyTodo Pro`; all six differ and name their page. |
| Status | Pass |
| Evidence | [results-C01-20261118-1933.json](evidences/results-C01-20261118-1933.json) (recorded values) |
| Defect ID | — |

## TC-GUI-022 - Visual consistency

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-GUI-022 |
| Feature/Requirement | All pages |
| Technique/Test Type | GUI checklist |
| Objective | Verify that buttons, links, headings and cards look and behave consistently across pages. |
| Preconditions | P-OUT, then P-A |
| Test Data | {} |
| Steps | 1. Capture all six pages at 1440x900.<br>2. Compare the primary action buttons: `Log in`, `Register`, `+ New Task`, `Filter`, `Create Task`, `Save Changes`.<br>3. Compare the secondary action (`Cancel`) and the text links (`Edit`, `Delete`, `Register`, `Log in`).<br>4. Compare heading sizes and card styling.<br>5. List every inconsistency with page and element. |
| Expected Result | All primary actions share one style. Secondary actions share one style. Text-style actions look alike. Headings of the same level have the same size. Cards share one style. Basis: Nielsen heuristic 4, consistency and standards; guideline activity A1. |
| Actual Result | `Log in`, `Register`, `Create Task` and `Save Changes` share one style, but `+ New Task` uses a smaller font (14.4 px vs 15.2 px) and `Filter` a lighter blue (`#2C6B8F`) at 13.3 px. The `Register`/`Log in` links on the auth pages use the browser-default blue, unlike `Edit`/`Delete` (`#2C6B8F`). Auth-page headings are 22.4 px against 32 px elsewhere. The auth card has a 12 px corner radius against 10 px for the task form and dashboard cards. |
| Status | Fail |
| Evidence | [TC-GUI-022-consistency-login-20261118.jpg](evidences/TC-GUI-022-consistency-login-20261118.jpg)<br>[TC-GUI-022-consistency-register-20261118.jpg](evidences/TC-GUI-022-consistency-register-20261118.jpg)<br>[TC-GUI-022-consistency-list-20261118.jpg](evidences/TC-GUI-022-consistency-list-20261118.jpg)<br>[TC-GUI-022-consistency-new-20261118.jpg](evidences/TC-GUI-022-consistency-new-20261118.jpg)<br>[TC-GUI-022-consistency-edit-20261118.jpg](evidences/TC-GUI-022-consistency-edit-20261118.jpg)<br>[TC-GUI-022-consistency-dashboard-20261118.jpg](evidences/TC-GUI-022-consistency-dashboard-20261118.jpg) |
| Defect ID | USA-OBS-003 |
