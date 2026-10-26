# Week 3 - Detailed GUI, Compatibility, Usability and Accessibility Test Cases

This document contains 54 planned test cases for the [Week 3 plan](README.md):

| Prefix | Cases | Task |
| --- | --- | --- |
| `TC-GUI-` | 001-022 | [Task 1 - GUI checklist](README.md#task-1) |
| `TC-CMP-` | 001-008 | [Task 2 - Compatibility](README.md#task-2) |
| `TC-USA-` | 001-006 | [Task 3 - Usability](README.md#task-3) |
| `TC-A11Y-` | 001-018 | [Task 4 - Accessibility](README.md#task-4) |

Each case uses the template fields from the project guideline:

| Field | Required Information |
| --- | --- |
| Test Case ID | Unique identifier, e.g. `TC-GUI-001` |
| Feature/Requirement | Week 1 requirement (`REQ-001` to `REQ-008`), page, or WCAG success criterion |
| Technique/Test Type | GUI checklist, Compatibility, Usability walkthrough or Accessibility (WCAG) |
| Objective | What the test verifies |
| Preconditions | Required initial state; codes are defined in [Shared preconditions](#shared-preconditions) |
| Test Data | Input values in JSON format; fixture IDs refer to [Fixture sets](#fixture-sets) |
| Steps | Numbered procedure |
| Expected Result | Expected behaviour defined before execution, with its basis |
| Actual Result | Observed behaviour |
| Status | Pass / Fail / Blocked / Not Run |
| Evidence | Planned screenshot or report filename |
| Defect ID | Related defect, or an earlier defect to re-check |

**Status of this document:** drafted on 2026-10-27; awaiting peer review. Every case is `Not Run`. Fill in Actual Result, Status, Evidence and Defect ID only after execution. Replace `<YYYYMMDD>` in evidence filenames with the execution date.

## Review sign-off

Expected results must be reviewed before execution (plan step 3). The reviewer checks that each expected result cites a basis from [README 0.3](README.md#03-test-basis) and was not derived from observed behaviour.

| Reviewer | Date | Cases reviewed | Changes requested | Approved |
| --- | --- | --- | --- | --- |
| | | TC-GUI-001 to 022 | | |
| | | TC-CMP-001 to 008 | | |
| | | TC-USA-001 to 006 | | |
| | | TC-A11Y-001 to 018 | | |

## Shared preconditions

| Code | Meaning |
| --- | --- |
| P-APP | `python app.py` is running at `http://127.0.0.1:5000` from the recorded commit. Configuration C01 (Chrome on macOS, 1440x900 window) unless the case says otherwise |
| P-OUT | P-APP, and the browser is logged out (open `/logout` first) |
| P-A | P-APP, logged in as account A with [Fixture Set A](#fixture-set-a---gui-and-accessibility) seeded on the execution day |
| P-B | P-APP, logged in as a usability account with [Fixture Set B](#fixture-set-b---usability-one-account-per-participant) seeded on the session day |
| P-C | P-APP, logged in as account C, which has no tasks |
| P-VO | VoiceOver is on (Command-F5) and Chrome is the active window |

## Fixture sets

Relative dates such as `today+2` are calculated on the execution day and entered as `YYYY-MM-DD`. Seed through the web UI or `POST /api/tasks`, and record which method was used.

### Accounts

| Account | Username | Password | Tasks |
| --- | --- | --- | --- |
| A | `w3<initial>_gui_<ddmm>` | `Test12345` | Fixture Set A |
| C | `w3<initial>_empty_<ddmm>` | `Test12345` | None |
| Usability | `w3<initial>_usa_p<n>_<ddmm>`, one per participant | `Test12345` | Fixture Set B |
| Per configuration | `w3<initial>_<config>_<ddmm>`, e.g. `w3d_c04_2810` | `Test12345` | Created during TC-CMP-001 |

### Fixture Set A - GUI and accessibility

| ID | Title | Description | Category | Due date | State |
| --- | --- | --- | --- | --- | --- |
| F1 | `GUI-Overdue` | `Fixture overdue` | Work | today-3 | Open |
| F2 | `GUI-Today` | `Fixture due today` | Personal | today | Open |
| F3 | `GUI-Soon` | `Week 3 GUI fixture` | Study | today+2 | Open |
| F4 | `GUI-Upcoming` | (empty) | Urgent | today+7 | Open |
| F5 | `GUI-NoDate` | (empty) | None | (empty) | Open |
| F6 | `GUI-Done` | (empty) | Work | today+1 | Done (complete it after creating) |
| F7 | 200-character title, see below | (empty) | Personal | (empty) | Open |
| F8 | 60-character unbroken title, see below | (empty) | None | (empty) | Open |
| F9 | `GUI-Special & <b>bold</b> "double" 'single' Résumé 报告` | (empty) | Study | (empty) | Open |

Generate the F7 and F8 titles exactly:

```bash
python3 -c "print(('GUI-Long ' + 'quarterly report review ' * 9)[:200])"   # F7, 200 characters
python3 -c "print('GUI-Unbroken-' + 'A' * 47)"                             # F8, 60 characters
```

F9 contains HTML tags only to check that text is displayed literally. Do not enter `<script>` or event-handler payloads in Week 3; script behaviour belongs to the Week 5 security tests.

### Fixture Set B - usability (one account per participant)

| ID | Title | Category | Due date | State |
| --- | --- | --- | --- | --- |
| B1 | `Quarterly report draft` | Work | today-2 | Open |
| B2 | `Report sign-off` | Work | today-1 | Done |
| B3 | `Expense report` | Personal | today+1 | Open |
| B4 | `Team meeting notes` | Work | today-5 | Open |
| B5 | `Gym session` | Personal | today+4 | Open |

No B task is due today, so DEF-002 cannot affect the usability results. After TC-USA-004 and TC-USA-005 are completed as intended, the open overdue tasks are B1 and B4, so the expected answer for TC-USA-006 is **2**.

## Case index

| ID | Title | ID | Title |
| --- | --- | --- | --- |
| [TC-GUI-001](#tc-gui-001---login-page-layout) | Login page layout | [TC-CMP-001](#tc-cmp-001---register-log-in-and-log-out) | Register, log in and log out |
| [TC-GUI-002](#tc-gui-002---login-error-message) | Login error message | [TC-CMP-002](#tc-cmp-002---create-a-task-with-the-date-picker) | Create a task with the date picker |
| [TC-GUI-003](#tc-gui-003---registration-hints) | Registration hints | [TC-CMP-003](#tc-cmp-003---filter-and-search) | Filter and search |
| [TC-GUI-004](#tc-gui-004---registration-error-messages) | Registration error messages | [TC-CMP-004](#tc-cmp-004---complete-and-reopen) | Complete and reopen |
| [TC-GUI-005](#tc-gui-005---navigation-bar) | Navigation bar | [TC-CMP-005](#tc-cmp-005---edit-a-task) | Edit a task |
| [TC-GUI-006](#tc-gui-006---brand-link) | Brand link | [TC-CMP-006](#tc-cmp-006---delete-with-confirmation) | Delete with confirmation |
| [TC-GUI-007](#tc-gui-007---task-list-header) | Task list header | [TC-CMP-007](#tc-cmp-007---navigation-bar-and-task-table-layout) | Navigation bar and task table layout |
| [TC-GUI-008](#tc-gui-008---filter-controls) | Filter controls | [TC-CMP-008](#tc-cmp-008---dashboard-layout) | Dashboard layout |
| [TC-GUI-009](#tc-gui-009---task-table-and-empty-state) | Task table and empty state | [TC-USA-001](#tc-usa-001---create-an-account-and-log-in) | Create an account and log in |
| [TC-GUI-010](#tc-gui-010---urgency-badges) | Urgency badges | [TC-USA-002](#tc-usa-002---add-a-study-task-due-tomorrow) | Add a Study task due tomorrow |
| [TC-GUI-011](#tc-gui-011---complete-and-reopen-button) | Complete and reopen button | [TC-USA-003](#tc-usa-003---find-open-work-tasks-about-a-report) | Find open Work tasks about a report |
| [TC-GUI-012](#tc-gui-012---edit-link-opens-a-pre-filled-form) | Edit link opens a pre-filled form | [TC-USA-004](#tc-usa-004---complete-a-task-then-undo-it) | Complete a task, then undo it |
| [TC-GUI-013](#tc-gui-013---delete-confirmation) | Delete confirmation | [TC-USA-005](#tc-usa-005---delete-one-specific-task) | Delete one specific task |
| [TC-GUI-014](#tc-gui-014---new-task-form) | New Task form | [TC-USA-006](#tc-usa-006---find-the-number-of-overdue-tasks) | Find the number of overdue tasks |
| [TC-GUI-015](#tc-gui-015---edit-task-form) | Edit Task form | [TC-A11Y-001](#tc-a11y-001---non-text-content) | Non-text content |
| [TC-GUI-016](#tc-gui-016---required-title) | Required title | [TC-A11Y-002](#tc-a11y-002---info-and-relationships) | Info and relationships |
| [TC-GUI-017](#tc-gui-017---feedback-after-actions) | Feedback after actions | [TC-A11Y-003](#tc-a11y-003---use-of-colour) | Use of colour |
| [TC-GUI-018](#tc-gui-018---dashboard-cards) | Dashboard cards | [TC-A11Y-004](#tc-a11y-004---text-contrast) | Text contrast |
| [TC-GUI-019](#tc-gui-019---long-content) | Long content | [TC-A11Y-005](#tc-a11y-005---form-labels-associated-with-fields) | Form labels associated with fields |
| [TC-GUI-020](#tc-gui-020---special-characters) | Special characters | [TC-A11Y-006](#tc-a11y-006---filter-and-search-labels) | Filter and search labels |
| [TC-GUI-021](#tc-gui-021---page-titles) | Page titles | [TC-A11Y-007](#tc-a11y-007---complete-and-reopen-button-name-and-state) | Complete/reopen button name and state |
| [TC-GUI-022](#tc-gui-022---visual-consistency) | Visual consistency | [TC-A11Y-008](#tc-a11y-008---keyboard-operation) | Keyboard operation |
| | | [TC-A11Y-009](#tc-a11y-009---bypass-the-navigation-bar) | Bypass the navigation bar |
| | | [TC-A11Y-010](#tc-a11y-010---page-titles) | Page titles |
| | | [TC-A11Y-011](#tc-a11y-011---focus-order-and-visible-focus) | Focus order and visible focus |
| | | [TC-A11Y-012](#tc-a11y-012---reflow-at-320-css-pixels) | Reflow at 320 CSS pixels |
| | | [TC-A11Y-013](#tc-a11y-013---text-resize-to-200) | Text resize to 200% |
| | | [TC-A11Y-014](#tc-a11y-014---language-of-page) | Language of page |
| | | [TC-A11Y-015](#tc-a11y-015---error-identification-and-announcement) | Error identification and announcement |
| | | [TC-A11Y-016](#tc-a11y-016---target-size) | Target size |
| | | [TC-A11Y-017](#tc-a11y-017---descriptive-headings-and-labels) | Descriptive headings and labels |
| | | [TC-A11Y-018](#tc-a11y-018---automated-scan-summary) | Automated scan summary |

# Task 1 - GUI checklist cases

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-001-login-layout-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-002-login-error-<YYYYMMDD>.png` |
| Defect ID | — |

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-003-register-hints-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-004-register-errors-<YYYYMMDD>.png` (one capture per submission, suffixed `-s1`, `-s2`, `-s3`) |
| Defect ID | Re-check DEF-001 |

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-005-nav-<state>-<YYYYMMDD>.png` |
| Defect ID | — |

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-006-brand-link-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-007-list-header-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-008-filters-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-009-empty-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-010-badges-<YYYYMMDD>.png` |
| Defect ID | Re-check DEF-002 |

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-011-toggle-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-012-edit-prefill-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-013-delete-dialog-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-014-new-form-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-015-edit-form-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-016-required-title-<YYYYMMDD>.png` |
| Defect ID | Re-check DEF-003 |

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-017-feedback-<action>-<YYYYMMDD>.png` |
| Defect ID | — |

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-018-dashboard-<YYYYMMDD>.png` |
| Defect ID | — |

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-019-long-content-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-020-special-chars-<YYYYMMDD>.png` |
| Defect ID | — |

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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-021-page-titles-<YYYYMMDD>.png` |
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
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-GUI-022-consistency-<page>-<YYYYMMDD>.png` |
| Defect ID | — |

# Task 2 - Compatibility cases

Run each case once per configuration in [README 2.1](README.md#21-configurations). Record the verdict for each configuration in the [README 2.2 matrix](README.md#22-compatibility-smoke-scenarios), not in the case's Actual Result field. Save captures in the configuration's evidence folder from README 2.1, e.g. `mac-firefox/desktop/` or `win-chrome/desktop/`. Compare each result with C01. Native dialogs, date pickers and validation popups do not appear in browser or WebDriver screenshots; capture them with an operating-system screenshot.

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
| Evidence | `<os>-<browser>/<viewport>/TC-CMP-001-<YYYYMMDD>.png` |
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
| Evidence | `<os>-<browser>/<viewport>/TC-CMP-002-<YYYYMMDD>.png` |
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
| Evidence | `<os>-<browser>/<viewport>/TC-CMP-003-<YYYYMMDD>.png` |
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
| Expected Result | The same states as TC-GUI-011: `✓`, strikethrough and `Done` after step 1; `○`, no strikethrough and `Due Soon` after step 2. Both symbols render as symbols, not as empty boxes. Basis: REQ-004. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `<os>-<browser>/<viewport>/TC-CMP-004-<YYYYMMDD>.png` |
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
| Evidence | `<os>-<browser>/<viewport>/TC-CMP-005-<YYYYMMDD>.png` |
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
| Evidence | `<os>-<browser>/<viewport>/TC-CMP-006-<YYYYMMDD>.png` |
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
| Steps | 1. Open `/` with no filters.<br>2. Inspect the navigation bar.<br>3. Inspect the table, including F7 and F8.<br>4. Run the horizontal-scroll check from TC-GUI-019 in the browser's console.<br>5. Capture the full page. |
| Expected Result | Each navigation item fits on one line with no overlap. All six table columns are readable with no clipped text or controls. The page does not scroll horizontally, unless a scrolling table is the only cause and it is recorded. Basis: interface; H1; H10. |
| Actual Result | Recorded per configuration in README 2.2. |
| Status | Not Run |
| Evidence | `<os>-<browser>/<viewport>/TC-CMP-007-<YYYYMMDD>.png` |
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
| Evidence | `<os>-<browser>/<viewport>/TC-CMP-008-<YYYYMMDD>.png` |
| Defect ID | — |

# Task 3 - Usability walkthrough cases

Each participant (P1-P3) runs TC-USA-001 to 006 in order on C01. Record per-participant results in [README 3.1](README.md#31-walkthrough-tasks) and observations in [README 3.3](README.md#33-observation-log).

**Facilitator script for every case:**
1. Give the participant only the scenario card text. Do not name pages, buttons or menus.
2. Ask them to think aloud. Start the timer when they finish reading.
3. Do not help. If they ask, reply "What would you try?" Stop at the 3-minute limit.
4. Record: completed (yes/no), time, errors or wrong paths, and quotes.
5. Ask the Single Ease Question: "Overall, how easy or difficult was this task?" on a 1 (very difficult) to 7 (very easy) scale.

**Shared pass criteria for every TC-USA case** (fixed before the sessions): at least 2 of 3 participants complete the task without help within 3 minutes, and the median ease rating is 5 or higher. Any task that misses either target produces at least one `USA-OBS-` entry.

## TC-USA-001 - Create an account and log in

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-001 |
| Feature/Requirement | REQ-001, REQ-002 |
| Technique/Test Type | Usability walkthrough |
| Objective | Assess whether a first-time user can create an account and reach their task list without help. |
| Preconditions | P-OUT; browser open at `/login` |
| Test Data | {"scenarioCard": "You want to start using PyTodo Pro. Create an account with the username and password on this card, and get to your task list.", "username": "w3<initial>_new_p<n>_<ddmm>", "password": "Test12345"} |
| Steps | Facilitator script steps 1-5. Success point: the participant reaches `My Tasks`. |
| Expected Result | Shared pass criteria. Basis: guideline activity A3 (ease of navigation, understandability). |
| Actual Result | Recorded per participant in README 3.1. |
| Status | Not Run |
| Evidence | `evidences/usability/TC-USA-001-P<n>.md` |
| Defect ID | — |

## TC-USA-002 - Add a Study task due tomorrow

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-002 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Usability walkthrough |
| Objective | Assess whether a user can create a categorised task with a due date. |
| Preconditions | P-B (the facilitator logs the participant into their usability account) |
| Test Data | {"scenarioCard": "Add a task to revise for your Software Testing quiz. Put it in the Study category and make it due tomorrow."} |
| Steps | Facilitator script steps 1-5. Success point: a new task with category Study and tomorrow's date is listed. |
| Expected Result | Shared pass criteria. Basis: guideline activity A3 (feedback, error prevention). |
| Actual Result | Recorded per participant in README 3.1. |
| Status | Not Run |
| Evidence | `evidences/usability/TC-USA-002-P<n>.md` |
| Defect ID | — |

## TC-USA-003 - Find open Work tasks about a report

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-003 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | Usability walkthrough |
| Objective | Assess whether a user can combine the category, status and search controls. |
| Preconditions | P-B |
| Test Data | {"scenarioCard": "Show only your unfinished Work tasks that have the word 'report' in the title."} |
| Steps | Facilitator script steps 1-5. Success point: the list shows only B1 `Quarterly report draft`. |
| Expected Result | Shared pass criteria. Basis: guideline activity A3 (understandability). |
| Actual Result | Recorded per participant in README 3.1. |
| Status | Not Run |
| Evidence | `evidences/usability/TC-USA-003-P<n>.md` |
| Defect ID | — |

## TC-USA-004 - Complete a task, then undo it

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-004 |
| Feature/Requirement | REQ-004 |
| Technique/Test Type | Usability walkthrough |
| Objective | Assess whether the complete/reopen control is discoverable and reversible. |
| Preconditions | P-B; filters cleared by the facilitator |
| Test Data | {"scenarioCard": "Mark 'Team meeting notes' as finished. Then change your mind and make it unfinished again."} |
| Steps | Facilitator script steps 1-5. Success point: B4 is shown as open again. |
| Expected Result | Shared pass criteria. Basis: guideline activity A3 (understandability, user control). |
| Actual Result | Recorded per participant in README 3.1. |
| Status | Not Run |
| Evidence | `evidences/usability/TC-USA-004-P<n>.md` |
| Defect ID | — |

## TC-USA-005 - Delete one specific task

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-005 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Usability walkthrough |
| Objective | Assess whether deletion is clear and protected against mistakes. |
| Preconditions | P-B |
| Test Data | {"scenarioCard": "You no longer need the task 'Expense report'. Remove it."} |
| Steps | Facilitator script steps 1-5. Success point: B3 is removed and every other task remains. |
| Expected Result | Shared pass criteria. Basis: guideline activity A3 (error prevention). |
| Actual Result | Recorded per participant in README 3.1. |
| Status | Not Run |
| Evidence | `evidences/usability/TC-USA-005-P<n>.md` |
| Defect ID | — |

## TC-USA-006 - Find the number of overdue tasks

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-006 |
| Feature/Requirement | REQ-007 |
| Technique/Test Type | Usability walkthrough |
| Objective | Assess whether a user can find a summary figure without counting by hand. |
| Preconditions | P-B; TC-USA-004 and TC-USA-005 completed as intended. If not, the facilitator restores that state before starting |
| Test Data | {"scenarioCard": "Without counting tasks one by one, find out how many of your tasks are overdue.", "expectedAnswer": 2} |
| Steps | Facilitator script steps 1-5. Success point: the participant states 2, taken from the dashboard. |
| Expected Result | Shared pass criteria. Basis: guideline activity A3 (ease of navigation, understandability). |
| Actual Result | Recorded per participant in README 3.1. |
| Status | Not Run |
| Evidence | `evidences/usability/TC-USA-006-P<n>.md` |
| Defect ID | — |

# Task 4 - Accessibility cases

Run on C01 unless the case says otherwise. Tools: Chrome DevTools (Elements, Accessibility pane, Rendering, device toolbar, colour picker contrast), Lighthouse, axe DevTools or WAVE, VoiceOver. The screen-reader steps are repeated with NVDA on Windows during the [Windows run](README.md#242-windows-11-run-c05-chrome-c06-firefox).

## TC-A11Y-001 - Non-text content

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-001 |
| Feature/Requirement | WCAG 2.2 SC 1.1.1 Non-text Content (A) - all pages |
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that every non-text control or symbol has a text alternative that conveys its purpose. |
| Preconditions | P-A |
| Test Data | {} |
| Steps | 1. On each page, list every symbol-only control or image.<br>2. For each one, open DevTools -> Elements -> Accessibility and record its computed name. |
| Expected Result | Every symbol-only control has a computed name that describes its purpose. Basis: WCAG 1.1.1. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-001-names-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-002 - Info and relationships

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-002 |
| Feature/Requirement | WCAG 2.2 SC 1.3.1 Info and Relationships (A) - all pages |
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that headings, the task table and forms are structured in the markup, not only visually. |
| Preconditions | P-A |
| Test Data | {} |
| Steps | 1. On each page, list the headings and their levels (DevTools Elements, or the VoiceOver rotor).<br>2. On `/`, check that table headers are marked up as header cells.<br>3. Check for landmarks (navigation, main). |
| Expected Result | Each page has one top-level heading that matches its visible title. The table uses header cells for its column headings. The navigation bar and main content are identifiable as regions. Basis: WCAG 1.3.1. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-002-structure-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-003 - Use of colour

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-003 |
| Feature/Requirement | WCAG 2.2 SC 1.4.1 Use of Color (A) - task list, dashboard |
| Technique/Test Type | Accessibility (WCAG) - simulation |
| Objective | Verify that urgency and completion are not shown by colour alone. |
| Preconditions | P-A |
| Test Data | {"fixtures": ["F1", "F2", "F3", "F4", "F5", "F6"]} |
| Steps | 1. Open DevTools -> Rendering -> Emulate vision deficiencies -> Achromatopsia.<br>2. Open `/` and `/dashboard`.<br>3. Check whether each urgency and the done state can still be identified. |
| Expected Result | Every urgency is identifiable from its badge text. Completed tasks are identifiable by more than colour (symbol and strikethrough). Dashboard cards are identifiable by their labels. Basis: WCAG 1.4.1. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-003-greyscale-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-004 - Text contrast

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-004 |
| Feature/Requirement | WCAG 2.2 SC 1.4.3 Contrast (Minimum) (AA) - all pages |
| Technique/Test Type | Accessibility (WCAG) - measurement |
| Objective | Verify that text meets the minimum contrast ratio. |
| Preconditions | P-A; one completed task (F6) and the empty state (TC-GUI-009) available |
| Test Data | {"pairs": ["completed task title", "empty-state message", "registration hints", "navigation username", "navigation links", "muted text", "each badge", "dashboard labels", "Edit/Delete links"]} |
| Steps | 1. For each pair, open the DevTools colour picker on the text and record the contrast ratio.<br>2. Note whether the text is large (at least 24 px, or at least 18.66 px bold).<br>3. Cross-check against the axe contrast results from TC-A11Y-018. |
| Expected Result | Normal text is at least 4.5:1; large text is at least 3:1. Planning predicted failures for the completed title and empty-state text (2.85:1, H5); these must be confirmed by measurement. Disabled or decorative text is exempt and must be identified. Basis: WCAG 1.4.3. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-004-contrast-<element>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-005 - Form labels associated with fields

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-005 |
| Feature/Requirement | WCAG 2.2 SC 1.3.1 (A) and 4.1.2 Name, Role, Value (A) - `/login`, `/register`, `/tasks/new` |
| Technique/Test Type | Accessibility (WCAG) - inspection and screen reader |
| Objective | Verify that each form field is announced with its visible label (H2). |
| Preconditions | P-OUT for the auth pages; P-A for `/tasks/new`; P-VO for step 3 |
| Test Data | {} |
| Steps | 1. Click each label's text and note whether focus moves into its field.<br>2. In DevTools -> Accessibility, record each field's computed name.<br>3. With VoiceOver, Tab into each field and record what is announced. |
| Expected Result | Clicking a label focuses its field. Each field's computed name equals its visible label (for example `Username`). VoiceOver announces the label with the field type. Basis: WCAG 1.3.1, 4.1.2. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-005-labels-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-006 - Filter and search labels

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-006 |
| Feature/Requirement | WCAG 2.2 SC 3.3.2 Labels or Instructions (A) - task list filters |
| Technique/Test Type | Accessibility (WCAG) - inspection and screen reader |
| Objective | Verify that the category list, status list and search box have labels (H4). |
| Preconditions | P-A; P-VO for step 2 |
| Test Data | {} |
| Steps | 1. Record whether each filter control has a visible label and its computed name in DevTools.<br>2. With VoiceOver, Tab to each control and record the announcement. |
| Expected Result | Each control has a visible label or instruction and a computed name that says what it filters. Placeholder text alone does not count as a label. Basis: WCAG 3.3.2. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-006-filter-labels-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-007 - Complete and reopen button name and state

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-007 |
| Feature/Requirement | WCAG 2.2 SC 4.1.2 Name, Role, Value (A) - task list |
| Technique/Test Type | Accessibility (WCAG) - screen reader |
| Objective | Verify that the complete/reopen button announces what it does and the task's state (H3). |
| Preconditions | P-A; P-VO |
| Test Data | {"fixtures": ["F3", "F6"]} |
| Steps | 1. With VoiceOver, Tab to the button on F3 (open) and record the announcement.<br>2. Repeat on F6 (done).<br>3. Record the computed name in DevTools. |
| Expected Result | Each announcement identifies the action and the task, and the state is conveyed, for example "Mark GUI-Soon as done, button" and "Mark GUI-Done as not done, button". Basis: WCAG 4.1.2. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-007-toggle-name-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-008 - Keyboard operation

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-008 |
| Feature/Requirement | WCAG 2.2 SC 2.1.1 Keyboard (A), 2.1.2 No Keyboard Trap (A) - all pages |
| Technique/Test Type | Accessibility (WCAG) - keyboard |
| Objective | Verify that every function can be operated with the keyboard alone. |
| Preconditions | P-OUT; mouse and trackpad not used |
| Test Data | {"title": "A11Y-Keyboard", "category": "Work", "dueDate": "today+3"} |
| Steps | 1. Log in as account A.<br>2. Create the test task, including choosing the category and the date with the keyboard.<br>3. Filter to Work and search `A11Y`.<br>4. Complete and reopen the task.<br>5. Edit and save it.<br>6. Delete it, answering the dialog with the keyboard.<br>7. Open the dashboard and log out. |
| Expected Result | Every step can be done with Tab, Shift-Tab, Enter, Space, Escape and the arrow keys. Focus never gets stuck in a control. Basis: WCAG 2.1.1, 2.1.2. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-008-keyboard-<step>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-009 - Bypass the navigation bar

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-009 |
| Feature/Requirement | WCAG 2.2 SC 2.4.1 Bypass Blocks (A) - logged-in pages |
| Technique/Test Type | Accessibility (WCAG) - keyboard and screen reader |
| Objective | Verify that keyboard and screen-reader users can skip the navigation bar (H8). |
| Preconditions | P-A; P-VO for step 2 |
| Test Data | {} |
| Steps | 1. Open `/`, press Tab once and record what receives focus.<br>2. With VoiceOver, open the rotor (VO-U) and check the Landmarks list for a main-content landmark. |
| Expected Result | A "skip to content" link appears on the first Tab, or a main landmark lets the user jump past the navigation bar. Basis: WCAG 2.4.1. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-009-bypass-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-010 - Page titles

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-010 |
| Feature/Requirement | WCAG 2.2 SC 2.4.2 Page Titled (A) - all pages |
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that each page has a descriptive title. |
| Preconditions | As TC-GUI-021 |
| Test Data | {} |
| Steps | 1. Use the titles recorded in TC-GUI-021.<br>2. Judge each against WCAG 2.4.2. |
| Expected Result | Each title describes the page's topic or purpose. Basis: WCAG 2.4.2. May share evidence with TC-GUI-021. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | Same as TC-GUI-021 |
| Defect ID | — |

## TC-A11Y-011 - Focus order and visible focus

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-011 |
| Feature/Requirement | WCAG 2.2 SC 2.4.3 Focus Order (A), 2.4.7 Focus Visible (AA) - all pages |
| Technique/Test Type | Accessibility (WCAG) - keyboard |
| Objective | Verify that focus moves in a logical order and is always visible. |
| Preconditions | P-OUT, then P-A |
| Test Data | {} |
| Steps | 1. On each page, press Tab repeatedly from the top.<br>2. Record the focus order and capture any control where the focus indicator is missing or hard to see.<br>3. Pay attention to the `○`/`✓` buttons, the `Delete` text button and the navigation links. |
| Expected Result | Focus follows the visual reading order (left to right, top to bottom) and every focused control shows a visible indicator. Basis: WCAG 2.4.3, 2.4.7. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-011-focus-<page>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-012 - Reflow at 320 CSS pixels

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-012 |
| Feature/Requirement | WCAG 2.2 SC 1.4.10 Reflow (AA) - all pages |
| Technique/Test Type | Accessibility (WCAG) - viewport |
| Objective | Verify that content can be used at 320 CSS px wide without scrolling in two directions (H1, H10). |
| Preconditions | P-OUT, then P-A |
| Test Data | {"viewport": "320x640, DevTools device toolbar, Responsive"} |
| Steps | 1. Set the viewport.<br>2. Open each page.<br>3. Run the horizontal-scroll check from TC-GUI-019.<br>4. Check that every control is visible and usable. |
| Expected Result | No horizontal scrolling except within the data table, which WCAG allows for content that needs two dimensions. No content or control is lost. The navigation bar is readable. Basis: WCAG 1.4.10. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-012-reflow-<page>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-013 - Text resize to 200%

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-013 |
| Feature/Requirement | WCAG 2.2 SC 1.4.4 Resize Text (AA) - all pages |
| Technique/Test Type | Accessibility (WCAG) - zoom |
| Objective | Verify that the pages work at 200% browser zoom. |
| Preconditions | P-OUT, then P-A; 1280x800 window |
| Test Data | {"zoom": "200%"} |
| Steps | 1. Zoom to 200% (Command-+).<br>2. Open each page and perform its main action. |
| Expected Result | No text is clipped, overlapping or hidden, and every function remains available. Basis: WCAG 1.4.4. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-013-zoom-<page>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-014 - Language of page

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-014 |
| Feature/Requirement | WCAG 2.2 SC 3.1.1 Language of Page (A) - all pages |
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that each page declares its language. |
| Preconditions | P-OUT, then P-A |
| Test Data | {} |
| Steps | 1. On each page, inspect the `<html>` element in DevTools. |
| Expected Result | Every page declares English (`lang="en"`). Basis: WCAG 3.1.1. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-014-lang-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-015 - Error identification and announcement

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-015 |
| Feature/Requirement | WCAG 2.2 SC 3.3.1 Error Identification (A), 4.1.3 Status Messages (AA) - `/login`, `/register` |
| Technique/Test Type | Accessibility (WCAG) - screen reader |
| Objective | Verify that form errors are described in text and announced to screen-reader users (H7). |
| Preconditions | P-OUT; P-VO |
| Test Data | {"login": {"username": "w3<initial>_gui_<ddmm>", "password": "WrongPass1"}, "register": {"username": "ab", "password": "Test12345"}} |
| Steps | 1. With VoiceOver on, submit the login data.<br>2. Record what VoiceOver says after the page reloads, without moving focus.<br>3. Repeat with the register data. |
| Expected Result | Each error is described in text. VoiceOver announces the error after submission without the user having to search for it. Basis: WCAG 3.3.1, 4.1.3. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-015-error-announce-<YYYYMMDD>.png` plus VoiceOver caption-panel screenshot |
| Defect ID | — |

## TC-A11Y-016 - Target size

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-016 |
| Feature/Requirement | WCAG 2.2 SC 2.5.8 Target Size (Minimum) (AA) - task list, navigation bar |
| Technique/Test Type | Accessibility (WCAG) - measurement |
| Objective | Verify that small click targets meet the minimum size or spacing. |
| Preconditions | P-A |
| Test Data | {"targets": ["○/✓ button", "Edit link", "Delete button", "navigation links"]} |
| Steps | 1. Inspect each target in DevTools and record its rendered width and height.<br>2. For targets under 24x24 CSS px, measure the spacing to the nearest other target. |
| Expected Result | Each target is at least 24x24 CSS px, or meets the spacing exception (a 24 px circle centred on it does not overlap another target). Inline text links in sentences are exempt. Basis: WCAG 2.5.8. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-016-target-<element>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-017 - Descriptive headings and labels

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-017 |
| Feature/Requirement | WCAG 2.2 SC 2.4.6 Headings and Labels (AA) - all pages |
| Technique/Test Type | Accessibility (WCAG) - review |
| Objective | Verify that headings, labels and column headers describe their purpose. |
| Preconditions | P-A |
| Test Data | {} |
| Steps | 1. List every heading, form label and table column header.<br>2. Judge whether each one describes its content or purpose on its own. |
| Expected Result | Every heading and label is descriptive. Table columns that hold controls have headers that say what the controls do. Basis: WCAG 2.4.6. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-A11Y-017-headings-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-A11Y-018 - Automated scan summary

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-018 |
| Feature/Requirement | WCAG 2.2 A/AA subset - all six pages |
| Technique/Test Type | Accessibility (WCAG) - automated scan |
| Objective | Record automated scan results and triage every serious or critical issue. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages; Lighthouse and axe DevTools versions recorded |
| Test Data | {"pages": ["/login", "/register", "/", "/tasks/new", "/tasks/<F3 id>/edit", "/dashboard"]} |
| Steps | 1. On each page, run Lighthouse (DevTools -> Lighthouse -> Accessibility, Desktop, Navigation) and save the report.<br>2. Run an axe DevTools full-page scan and export the results.<br>3. Fill the README 4.2 table.<br>4. Link each critical or serious issue to a TC-A11Y case, a `DEF-` record, or a written false-positive reason. |
| Expected Result | Reports are saved for all six pages and every critical or serious issue is triaged. The case passes when triage is complete; the scores themselves are findings, not the verdict. Basis: README Task 4 method. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/a11y-reports/<tool>-<page>-<YYYYMMDD>.html` |
| Defect ID | — |
