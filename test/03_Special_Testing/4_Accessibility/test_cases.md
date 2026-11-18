# Week 3 - Accessibility Test Cases

Detailed cases for [Task 4 - Basic accessibility findings](../README.md#task-4) of the [Week 3 plan](../README.md). Each case uses the guideline's test-case template fields. Precondition codes (P-APP, P-OUT, P-A, P-C, P-VO), test accounts and fixture IDs (F1-F9) are defined in [fixtures.md](../fixtures.md). Executed on 2026-11-18 on C01 (Chrome 157.0.8103.80, macOS 26.5.2, headless) by the Playwright suite [test_accessibility.py](test_accessibility.py), run twice: [results-C01-20261118-205048.json](evidences/results-C01-20261118-205048.json) is the recorded run and [results-C01-20261118-204716.json](evidences/results-C01-20261118-204716.json) the first reproduction. Results were identical in both runs except TC-A11Y-008, whose first-run failure was a script error (see that case).

**How the steps were automated.** The script performs the DevTools steps with equivalent programmatic checks: computed styles for contrast, focus and target size; Chrome's accessibility tree (read through the DevTools protocol and Playwright accessibility snapshots) for names, roles and landmarks; Chrome's vision-deficiency emulation for TC-A11Y-003; and a 640x400 CSS-pixel viewport at device scale 2 for 200% zoom (TC-A11Y-013). The screen-reader steps (VoiceOver, NVDA) were not run: for TC-A11Y-005, 007 and 015 the accessibility tree a screen reader reads already shows the failure, so the verdict does not depend on them. The NVDA pass planned for the Windows run remains optional supporting evidence.

## Review sign-off

Expected results must be reviewed before execution (plan step 3). The reviewer checks that each expected result cites a basis from [README 0.3](../README.md#03-test-basis) and was not derived from observed behaviour.

| Reviewer | Date | Cases reviewed | Changes requested | Approved |
| --- | --- | --- | --- | --- |
| Team (verbal approval of execution, recorded by Darius Lee Shin) | 2026-11-18 | TC-A11Y-001 to 018 | None recorded | Yes (verbal) |

## Case index

| ID | Title |
| --- | --- |
| [TC-A11Y-001](#tc-a11y-001---non-text-content) | Non-text content |
| [TC-A11Y-002](#tc-a11y-002---info-and-relationships) | Info and relationships |
| [TC-A11Y-003](#tc-a11y-003---use-of-colour) | Use of colour |
| [TC-A11Y-004](#tc-a11y-004---text-contrast) | Text contrast |
| [TC-A11Y-005](#tc-a11y-005---form-labels-associated-with-fields) | Form labels associated with fields |
| [TC-A11Y-006](#tc-a11y-006---filter-and-search-labels) | Filter and search labels |
| [TC-A11Y-007](#tc-a11y-007---complete-and-reopen-button-name-and-state) | Complete and reopen button name and state |
| [TC-A11Y-008](#tc-a11y-008---keyboard-operation) | Keyboard operation |
| [TC-A11Y-009](#tc-a11y-009---bypass-the-navigation-bar) | Bypass the navigation bar |
| [TC-A11Y-010](#tc-a11y-010---page-titles) | Page titles |
| [TC-A11Y-011](#tc-a11y-011---focus-order-and-visible-focus) | Focus order and visible focus |
| [TC-A11Y-012](#tc-a11y-012---reflow-at-320-css-pixels) | Reflow at 320 CSS pixels |
| [TC-A11Y-013](#tc-a11y-013---text-resize-to-200) | Text resize to 200% |
| [TC-A11Y-014](#tc-a11y-014---language-of-page) | Language of page |
| [TC-A11Y-015](#tc-a11y-015---error-identification-and-announcement) | Error identification and announcement |
| [TC-A11Y-016](#tc-a11y-016---target-size) | Target size |
| [TC-A11Y-017](#tc-a11y-017---descriptive-headings-and-labels) | Descriptive headings and labels |
| [TC-A11Y-018](#tc-a11y-018---automated-scan-summary) | Automated scan summary |

## How to run

Run on C01 unless the case says otherwise. Tools: Chrome DevTools (Elements, Accessibility pane, Rendering, device toolbar, colour picker contrast), Lighthouse, axe DevTools or WAVE, VoiceOver. The screen-reader steps are repeated with NVDA on Windows during the [Windows run](../README.md#242-windows-11-run-c05-chrome-c06-firefox).

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
| Actual Result | The complete/reopen buttons on `/` have the accessible names `○` and `✓` only; no other symbol-only controls or images on the six pages. |
| Status | Fail |
| Evidence | [TC-A11Y-001-names-20261118.jpg](evidences/TC-A11Y-001-names-20261118.jpg) |
| Defect ID | DEF-008 |

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
| Actual Result | Each page has one `h1` and the task table exposes six column-header cells, but no page has a `main` landmark; only the navigation landmark exists. |
| Status | Fail |
| Evidence | [TC-A11Y-002-structure-20261118.jpg](evidences/TC-A11Y-002-structure-20261118.jpg) |
| Defect ID | DEF-010 |

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
| Actual Result | With achromatopsia emulation, every urgency is still identifiable from its badge text, the completed task from `✓` and strikethrough, and the dashboard cards from their labels. |
| Status | Pass |
| Evidence | [TC-A11Y-003-greyscale-list-20261118.jpg](evidences/TC-A11Y-003-greyscale-list-20261118.jpg)<br>[TC-A11Y-003-greyscale-dashboard-20261118.jpg](evidences/TC-A11Y-003-greyscale-dashboard-20261118.jpg) |
| Defect ID | — |

## TC-A11Y-004 - Text contrast

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-004 |
| Feature/Requirement | WCAG 2.2 SC 1.4.3 Contrast (Minimum) (AA) - all pages |
| Technique/Test Type | Accessibility (WCAG) - measurement |
| Objective | Verify that text meets the minimum contrast ratio. |
| Preconditions | P-A; one completed task (F6) and the empty state ([TC-GUI-009](../1_GUI/test_cases.md#tc-gui-009---task-table-and-empty-state)) available |
| Test Data | {"pairs": ["completed task title", "empty-state message", "registration hints", "navigation username", "navigation links", "muted text", "each badge", "dashboard labels", "Edit/Delete links"]} |
| Steps | 1. For each pair, open the DevTools colour picker on the text and record the contrast ratio.<br>2. Note whether the text is large (at least 24 px, or at least 18.66 px bold).<br>3. Cross-check against the axe contrast results from TC-A11Y-018. |
| Expected Result | Normal text is at least 4.5:1; large text is at least 3:1. Planning predicted failures for the completed title and empty-state text (2.85:1, H5); these must be confirmed by measurement. Disabled or decorative text is exempt and must be identified. Basis: WCAG 1.4.3. |
| Actual Result | Completed task title and empty-state message measure **2.85:1** (14.72 px, normal weight; 4.5:1 required). All other pairs pass: hint 4.54:1, muted text 5.74:1, navigation link 8.79:1, username 5.18:1, Edit/Delete 5.82:1, badges 4.78-5.89:1, dashboard labels 5.74:1. |
| Status | Fail |
| Evidence | [TC-A11Y-004-contrast-empty-state-20261118.jpg](evidences/TC-A11Y-004-contrast-empty-state-20261118.jpg)<br>[TC-A11Y-004-contrast-list-20261118.jpg](evidences/TC-A11Y-004-contrast-list-20261118.jpg) |
| Defect ID | DEF-009 |

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
| Actual Result | Clicking any label on `/login`, `/register` or `/tasks/new` leaves focus on the page body, and every field's accessible name is empty, so a screen reader announces only the field type. The VoiceOver step was not needed for the verdict: the accessibility tree a screen reader reads has no names. |
| Status | Fail |
| Evidence | [TC-A11Y-005-labels-20261118.jpg](evidences/TC-A11Y-005-labels-20261118.jpg) |
| Defect ID | DEF-007 |

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
| Actual Result | The filter form has no visible labels. The category and status lists have empty accessible names; the search box is named only by its placeholder `Search title...`. |
| Status | Fail |
| Evidence | [TC-A11Y-006-filter-labels-20261118.jpg](evidences/TC-A11Y-006-filter-labels-20261118.jpg) |
| Defect ID | DEF-007 |

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
| Actual Result | Accessibility snapshots: `button "○"` (open task) and `button "✓"` (completed task). Neither name states the action or the task, and no pressed/checked state is exposed. |
| Status | Fail |
| Evidence | [TC-A11Y-007-toggle-name-20261118.jpg](evidences/TC-A11Y-007-toggle-name-20261118.jpg) |
| Defect ID | DEF-008 |

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
| Actual Result | Every step was completed with the keyboard only: log in, create a task (Work chosen by typing `W`, date typed into the segmented date control), filter, search, complete, reopen, edit, save, delete, open the dashboard and log out. No keyboard trap. The native delete dialog was answered by Playwright. The first run failed because the script typed the title before tabbing into the Title field; that script error was fixed, and this result is from the second run. |
| Status | Pass |
| Evidence | [TC-A11Y-008-keyboard-end-20261118.jpg](evidences/TC-A11Y-008-keyboard-end-20261118.jpg) |
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
| Actual Result | The first Tab on `/` focuses the `PyTodo Pro` brand link; there is no skip link and no `main` landmark. |
| Status | Fail |
| Evidence | [TC-A11Y-009-bypass-20261118.jpg](evidences/TC-A11Y-009-bypass-20261118.jpg) |
| Defect ID | DEF-010 |

## TC-A11Y-010 - Page titles

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-010 |
| Feature/Requirement | WCAG 2.2 SC 2.4.2 Page Titled (A) - all pages |
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that each page has a descriptive title. |
| Preconditions | As [TC-GUI-021](../1_GUI/test_cases.md#tc-gui-021---page-titles) |
| Test Data | {} |
| Steps | 1. Use the titles recorded in [TC-GUI-021](../1_GUI/test_cases.md#tc-gui-021---page-titles).<br>2. Judge each against WCAG 2.4.2. |
| Expected Result | Each title describes the page's topic or purpose. Basis: WCAG 2.4.2. May share evidence with [TC-GUI-021](../1_GUI/test_cases.md#tc-gui-021---page-titles). |
| Actual Result | Six unique titles, each naming its page and the application (same evidence as TC-GUI-021). |
| Status | Pass |
| Evidence | [TC-GUI-021 results](../1_GUI/evidences/results-C01-20261118-1933.json); [this run](evidences/results-C01-20261118-205048.json) |
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
| Actual Result | On all six pages every focused control shows a visible focus indicator (browser default focus ring), and the Tab order follows the visual reading order. |
| Status | Pass |
| Evidence | [TC-A11Y-011-focus-first-20261118.jpg](evidences/TC-A11Y-011-focus-first-20261118.jpg) |
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
| Steps | 1. Set the viewport.<br>2. Open each page.<br>3. Run the horizontal-scroll check from [TC-GUI-019](../1_GUI/test_cases.md#tc-gui-019---long-content).<br>4. Check that every control is visible and usable. |
| Expected Result | No horizontal scrolling except within the data table, which WCAG allows for content that needs two dimensions. No content or control is lost. The navigation bar is readable. Basis: WCAG 1.4.10. |
| Actual Result | At 320 px the login and register pages reflow correctly. On `/`, `/tasks/new`, the edit form and `/dashboard` the navigation wraps (`PyTodo Pro`, `Log out`) and the username and `Log out` extend past the viewport; on the form and dashboard pages this makes the whole page scroll horizontally. The task list's horizontal scroll is caused by the table, which is allowed. |
| Status | Fail |
| Evidence | [TC-A11Y-012-reflow-login-20261118.jpg](evidences/TC-A11Y-012-reflow-login-20261118.jpg)<br>[TC-A11Y-012-reflow-register-20261118.jpg](evidences/TC-A11Y-012-reflow-register-20261118.jpg)<br>[TC-A11Y-012-reflow-list-20261118.jpg](evidences/TC-A11Y-012-reflow-list-20261118.jpg)<br>[TC-A11Y-012-reflow-dashboard-20261118.jpg](evidences/TC-A11Y-012-reflow-dashboard-20261118.jpg) |
| Defect ID | DEF-004 |

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
| Actual Result | At the 200% equivalent (640x400 CSS px, device scale 2) no text is clipped or overlapping, the navigation stays on one line, and every page's main action remains available. |
| Status | Pass |
| Evidence | [TC-A11Y-013-zoom-register-20261118.jpg](evidences/TC-A11Y-013-zoom-register-20261118.jpg)<br>[TC-A11Y-013-zoom-list-20261118.jpg](evidences/TC-A11Y-013-zoom-list-20261118.jpg) |
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
| Actual Result | Every page declares `lang="en"`. |
| Status | Pass |
| Evidence | [results-C01-20261118-205048.json](evidences/results-C01-20261118-205048.json) (recorded values) |
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
| Actual Result | Both errors are described in text (`Invalid username or password.`; `Username must be 3-20 characters ...`), but neither has an alert role or live region, and focus is not moved to it after the page reloads. Based on the accessibility tree; a VoiceOver confirmation can be added, but it would not change the verdict. |
| Status | Fail |
| Evidence | [TC-A11Y-015-error-login-20261118.jpg](evidences/TC-A11Y-015-error-login-20261118.jpg)<br>[TC-A11Y-015-error-register-20261118.jpg](evidences/TC-A11Y-015-error-register-20261118.jpg) |
| Defect ID | DEF-011 |

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
| Actual Result | `Edit` (23x15 px) and `Delete` (39x15 px) are below 24 px high and are stacked directly above each other, so their 24 px spacing circles overlap and neither meets the spacing exception. The navigation links (18-22 px high) meet the spacing exception, and the `○`/`✓` buttons are at least 24x24 px. |
| Status | Fail |
| Evidence | [TC-A11Y-016-targets-20261118.jpg](evidences/TC-A11Y-016-targets-20261118.jpg) |
| Defect ID | DEF-012 |

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
| Actual Result | Headings (`Log in`, `Create an account`, `My Tasks`, `New Task`, `Edit Task`, `Dashboard`) and form labels are descriptive, but the first and last table columns, which hold the complete/reopen and Edit/Delete controls, have empty headers. |
| Status | Fail |
| Evidence | [TC-A11Y-017-headings-20261118.jpg](evidences/TC-A11Y-017-headings-20261118.jpg) |
| Defect ID | DEF-013 |

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
| Actual Result | axe-core 4.12.1 and Lighthouse 12.8.2 reports saved for all six pages; Lighthouse audited each intended page (no redirects). Lighthouse accessibility scores: `/login` 91, `/register` 91, `/` 76, `/tasks/new` 82, edit 82, `/dashboard` 100. Every critical and serious issue is triaged to a failed case (README 4.2); none is a false positive. |
| Status | Pass |
| Evidence | [evidences/reports/](evidences/reports/) (axe JSON and Lighthouse HTML/JSON per page; [summary](evidences/reports/summary-20261118.json)) |
| Defect ID | — |
