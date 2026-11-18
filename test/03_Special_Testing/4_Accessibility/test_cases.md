# Week 3 - Accessibility Test Cases

Detailed cases for [Task 4 - Basic accessibility findings](../README.md#task-4) of the [Week 3 plan](../README.md). Each case uses the guideline's test-case template fields. Precondition codes (P-APP, P-OUT, P-A, P-C, P-VO), test accounts and fixture IDs (F1-F9) are defined in [fixtures.md](../fixtures.md). Every case is `Not Run` until executed; fill in Actual Result, Status, Evidence and Defect ID only after execution, and replace `<YYYYMMDD>` in evidence filenames with the execution date.

## Review sign-off

Expected results must be reviewed before execution (plan step 3). The reviewer checks that each expected result cites a basis from [README 0.3](../README.md#03-test-basis) and was not derived from observed behaviour.

| Reviewer | Date | Cases reviewed | Changes requested | Approved |
| --- | --- | --- | --- | --- |
| | | TC-A11Y-001 to 018 | | |

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
| Preconditions | P-A; one completed task (F6) and the empty state ([TC-GUI-009](../1_GUI/test_cases.md#tc-gui-009---task-table-and-empty-state)) available |
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
| Preconditions | As [TC-GUI-021](../1_GUI/test_cases.md#tc-gui-021---page-titles) |
| Test Data | {} |
| Steps | 1. Use the titles recorded in [TC-GUI-021](../1_GUI/test_cases.md#tc-gui-021---page-titles).<br>2. Judge each against WCAG 2.4.2. |
| Expected Result | Each title describes the page's topic or purpose. Basis: WCAG 2.4.2. May share evidence with [TC-GUI-021](../1_GUI/test_cases.md#tc-gui-021---page-titles). |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | Same as [TC-GUI-021](../1_GUI/test_cases.md#tc-gui-021---page-titles) |
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
| Steps | 1. Set the viewport.<br>2. Open each page.<br>3. Run the horizontal-scroll check from [TC-GUI-019](../1_GUI/test_cases.md#tc-gui-019---long-content).<br>4. Check that every control is visible and usable. |
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
| Evidence | `evidences/reports/<tool>-<page>-<YYYYMMDD>.html` |
| Defect ID | — |
