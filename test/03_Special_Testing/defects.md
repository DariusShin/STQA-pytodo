# Week 3 - Defects

Defects first found in Week 3, in the project Defect Report Template, followed by Week 1 defects re-tested this week. Unless stated, the environment is C01: Chrome 157.0.8103.80 on macOS 26.5.2, 1440x900, Playwright headless. Every defect was reproduced in two runs.

| Defect | Title | Severity / Priority | Status |
| --- | --- | --- | --- |
| [DEF-004](#def-004---navigation-bar-breaks-at-a-narrow-viewport) | Navigation bar breaks at a narrow viewport | Moderate / Medium | Open |
| [DEF-005](#def-005---task-title-html-is-rendered-as-markup) | Task title HTML is rendered as markup | Moderate / High | Open (upgraded in Week 5) |
| [DEF-006](#def-006---desktop-layout-scaled-down-on-tablets-and-phones) | Desktop layout scaled down on tablets and phones | Moderate / Medium | Open |
| [DEF-007](#def-007---form-fields-have-no-programmatic-labels) | Form fields have no programmatic labels | Major / High | Open |
| [DEF-008](#def-008---completereopen-button-has-no-meaningful-name) | Complete/reopen button has no meaningful name | Major / High | Open |
| [DEF-009](#def-009---low-contrast-text) | Low-contrast text | Moderate / Medium | Open |
| [DEF-010](#def-010---no-main-landmark-or-skip-link) | No main landmark or skip link | Minor / Low | Open |
| [DEF-011](#def-011---errors-not-announced) | Errors not announced | Moderate / Medium | Open |
| [DEF-012](#def-012---small-crowded-targets) | Small, crowded targets | Minor / Low | Open |
| [DEF-013](#def-013---empty-column-headers) | Empty column headers | Minor / Low | Open |

## DEF-004 - Navigation bar breaks at a narrow viewport

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-004 |
| Title | Navigation bar wraps and pushes `Log out` off-screen at a 390 px viewport |
| Affected Feature | Shared navigation bar; REQ-002 |
| Environment | C01 machine with the viewport set to 390x844 (desktop device type, no mobile emulation) |
| Preconditions | Logged in as account A |
| Steps to Reproduce | 1. Log in.<br>2. Resize the viewport to 390x844.<br>3. Open `/`, `/tasks/new` or `/dashboard`. |
| Expected Result | Each navigation item fits on one line and every item can be clicked. Basis: interface; TC-GUI-005 |
| Actual Result | `PyTodo Pro` and `Log out` each wrap to two lines, and `Log out` extends past the right edge, so it is visible only after scrolling sideways. Same on all three pages. Also reproduced at 320 px by TC-A11Y-012. |
| Severity | Moderate - logging out needs horizontal scrolling on narrow screens |
| Priority | Medium |
| Evidence | [TC-GUI-005-nav-390-20261118.jpg](1_GUI/evidences/TC-GUI-005-nav-390-20261118.jpg); [TC-A11Y-012](4_Accessibility/evidences/TC-A11Y-012-reflow-login-20261118.jpg) |
| Status | Open |

## DEF-005 - Task title HTML is rendered as markup

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-005 |
| Title | HTML in a task title is rendered as markup in the task list |
| Affected Feature | Task list `/`; REQ-003 |
| Environment | C01 |
| Preconditions | Logged in; a task titled `GUI-Special & <b>bold</b> "double" 'single' Résumé 报告` exists (fixture F9) |
| Steps to Reproduce | 1. Create a task with the title above.<br>2. Open `/`. |
| Expected Result | The title is displayed exactly as entered, including the literal `<b>bold</b>`. Basis: REQ-003; TC-GUI-020 |
| Actual Result | The list shows `bold` in bold type and hides the tags; the edit form shows the exact title. |
| Severity | Moderate - displayed task data differs from what was saved (upgraded to Major in Week 5, where a script payload was shown to execute) |
| Priority | High |
| Evidence | [list](1_GUI/evidences/TC-GUI-020-special-list-20261118.jpg); [edit form](1_GUI/evidences/TC-GUI-020-special-edit-20261118.jpg) |
| Status | Open |

## DEF-006 - Desktop layout scaled down on tablets and phones

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-006 |
| Title | Pages render at a 980 px desktop layout on tablet and phone screens, so text is too small to read |
| Affected Feature | Every page (shared layout); observed on the task list, REQ-003 |
| Environment | C02: Chrome 157.0.8103.80 mobile emulation, 768x1024, DPR 2. C03: 390x844, DPR 3. macOS 26.5.2, headless |
| Preconditions | Logged in as account A with Fixture Set A |
| Steps to Reproduce | 1. Open the app with Chrome mobile emulation for a 390x844 phone or a 768x1024 tablet.<br>2. Log in and open `/`.<br>3. Compare `window.innerWidth` with the device width and measure the smallest navigation/table text. |
| Expected Result | All columns and the navigation are readable without zooming; text renders at 12 px or more. Basis: TC-CMP-007 |
| Actual Result | The page is laid out at 980 CSS px and scaled to 0.784 (tablet) or 0.398 (phone). The smallest text renders at 9.8 px on the tablet and 5.0 px on the phone. Cause: no viewport meta tag (H1). |
| Severity | Moderate - all content is present but needs zooming |
| Priority | Medium |
| Evidence | [tablet](2_Compatibility/evidences/mac-chrome/tablet/TC-CMP-007-layout-20261118.jpg); [phone](2_Compatibility/evidences/mac-chrome/mobile/TC-CMP-007-layout-20261118.jpg) |
| Status | Open |

## DEF-007 - Form fields have no programmatic labels

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-007 |
| Title | Form fields and filter controls have no programmatically associated labels |
| Affected Feature | `/login`, `/register`, `/tasks/new`, `/tasks/<id>/edit` and the task-list filters; REQ-001 to REQ-003, REQ-005; WCAG 1.3.1, 3.3.2, 4.1.2 |
| Environment | C01 |
| Preconditions | Logged out for the auth pages; logged in as account A for the others |
| Steps to Reproduce | 1. Open `/login`.<br>2. Click the `Username` label.<br>3. Inspect the field's accessible name in the accessibility tree.<br>4. Repeat on the other forms and the filter controls. |
| Expected Result | Clicking a label focuses its field; each field's accessible name is its visible label; filters have visible labels. Basis: WCAG 1.3.1, 3.3.2, 4.1.2; TC-A11Y-005/006 |
| Actual Result | Focus stays on the page body; every field's accessible name is empty; the category and status lists are unnamed and the search box is named only by its placeholder. axe reports `label` and `select-name` as critical. |
| Severity | Major - a screen-reader user cannot tell which field is which |
| Priority | High |
| Evidence | [TC-A11Y-005](4_Accessibility/evidences/TC-A11Y-005-labels-20261118.jpg); [TC-A11Y-006](4_Accessibility/evidences/TC-A11Y-006-filter-labels-20261118.jpg); [axe login report](4_Accessibility/evidences/reports/axe-login-20261118.json) |
| Status | Open |

## DEF-008 - Complete/reopen button has no meaningful name

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-008 |
| Title | Complete/reopen button has no meaningful accessible name or state |
| Affected Feature | Task list `/`; REQ-004; WCAG 1.1.1, 4.1.2 |
| Environment | C01 |
| Preconditions | Logged in as account A with Fixture Set A |
| Steps to Reproduce | 1. Open `/`.<br>2. Inspect the accessibility snapshot of the `○` button on an open task and the `✓` button on a completed task. |
| Expected Result | The name states the action and the task, and the state is conveyed, e.g. "Mark GUI-Soon as done". Basis: WCAG 1.1.1, 4.1.2; TC-A11Y-001/007 |
| Actual Result | Snapshots read `button "○"` and `button "✓"`, with no task, action or pressed state. Neither axe nor Lighthouse flags this. |
| Severity | Major - a screen-reader user cannot tell what the button does or which task it affects |
| Priority | High |
| Evidence | [TC-A11Y-007](4_Accessibility/evidences/TC-A11Y-007-toggle-name-20261118.jpg); [run results](4_Accessibility/evidences/results-C01-20261118-213348.json) |
| Status | Open |

## DEF-009 - Low-contrast text

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-009 |
| Title | Completed task titles and the empty-state message have insufficient contrast (2.85:1) |
| Affected Feature | Task list `/`; WCAG 1.4.3 |
| Environment | C01 |
| Preconditions | Logged in as account A; one completed task (F6); a search with no results |
| Steps to Reproduce | 1. Open `/` and measure the completed task's title.<br>2. Search for `NO-SUCH-TITLE-W3` and measure the message. |
| Expected Result | Normal-size text has at least 4.5:1 contrast. Basis: WCAG 1.4.3; TC-A11Y-004 |
| Actual Result | Both measure 2.85:1 (`#999999` on white, 14.72 px); axe reports `color-contrast` as serious. |
| Severity | Moderate - low-vision users may not read completed tasks or the empty-state message |
| Priority | Medium |
| Evidence | [list](4_Accessibility/evidences/TC-A11Y-004-contrast-list-20261118.jpg); [empty state](4_Accessibility/evidences/TC-A11Y-004-contrast-empty-state-20261118.jpg) |
| Status | Open |

## DEF-010 - No main landmark or skip link

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-010 |
| Title | No main landmark and no skip link |
| Affected Feature | All pages (shared layout); WCAG 1.3.1, 2.4.1 |
| Environment | C01 |
| Preconditions | Logged in as account A |
| Steps to Reproduce | 1. Open `/` and press Tab once.<br>2. Inspect the page's landmarks. |
| Expected Result | A skip link on the first Tab, or a main landmark to jump to. Basis: WCAG 2.4.1; TC-A11Y-002/009 |
| Actual Result | The first Tab focuses the brand link; only a navigation landmark exists. axe reports `landmark-one-main` and `region`. |
| Severity | Minor - keyboard users pass four navigation links on every page; nothing is blocked |
| Priority | Low |
| Evidence | [TC-A11Y-009](4_Accessibility/evidences/TC-A11Y-009-bypass-20261118.jpg) |
| Status | Open |

## DEF-011 - Errors not announced

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-011 |
| Title | Form errors are not exposed for screen-reader announcement |
| Affected Feature | `/login`, `/register`; REQ-001, REQ-002; WCAG 3.3.1, 4.1.3 |
| Environment | C01 |
| Preconditions | Logged out |
| Steps to Reproduce | 1. Submit `/login` with a wrong password, or `/register` with username `ab`.<br>2. Inspect the error element's role, live-region attributes and the focused element. |
| Expected Result | The error is described in text and announced without the user searching for it. Basis: WCAG 3.3.1, 4.1.3; TC-A11Y-015 |
| Actual Result | The error is in text, but has no alert role or live region and focus does not move to it. |
| Severity | Moderate - screen-reader users may not notice why the form was rejected |
| Priority | Medium |
| Evidence | [login](4_Accessibility/evidences/TC-A11Y-015-error-login-20261118.jpg); [register](4_Accessibility/evidences/TC-A11Y-015-error-register-20261118.jpg) |
| Status | Open |

## DEF-012 - Small, crowded targets

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-012 |
| Title | Edit and Delete targets are too small and too close together |
| Affected Feature | Task list `/`; REQ-003; WCAG 2.5.8 |
| Environment | C01 |
| Preconditions | Logged in as account A |
| Steps to Reproduce | 1. Open `/`.<br>2. Measure the `Edit` and `Delete` controls in any row. |
| Expected Result | Each target is at least 24x24 CSS px or meets the spacing exception. Basis: WCAG 2.5.8; TC-A11Y-016 |
| Actual Result | `Edit` is 23x15 px and `Delete` 39x15 px, stacked directly above each other. Lighthouse fails `target-size`. |
| Severity | Minor - easy to tap Delete instead of Edit on touch screens; the confirmation dialog prevents accidental deletion |
| Priority | Low |
| Evidence | [TC-A11Y-016](4_Accessibility/evidences/TC-A11Y-016-targets-20261118.jpg) |
| Status | Open |

## DEF-013 - Empty column headers

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-013 |
| Title | Table columns holding controls have empty headers |
| Affected Feature | Task list `/`; WCAG 1.3.1, 2.4.6 |
| Environment | C01 |
| Preconditions | Logged in as account A |
| Steps to Reproduce | 1. Open `/`.<br>2. Read the table's column headers. |
| Expected Result | Every column has a header saying what it contains. Basis: WCAG 2.4.6; TC-A11Y-017 |
| Actual Result | The first (complete/reopen) and last (Edit/Delete) headers are empty. axe reports `empty-table-header`; Lighthouse fails `td-has-header`. |
| Severity | Minor - screen-reader users hear no column name for these controls |
| Priority | Low |
| Evidence | [TC-A11Y-017](4_Accessibility/evidences/TC-A11Y-017-headings-20261118.jpg) |
| Status | Open |

## Re-tested defects

| Defect | Original record | Re-tested by | Result (2026-11-18, C01) | Severity change |
| --- | --- | --- | --- | --- |
| DEF-001 | [Week 1](../01_Black_Box/defects.md#def-001---eight-character-password-is-rejected) | TC-GUI-004 | Still fails: 8-character password rejected | None |
| DEF-002 | [Week 1](../01_Black_Box/defects.md#def-002---today-is-classified-and-counted-as-overdue) | TC-GUI-010 | Still fails: task due today shows `Overdue` | None |
| DEF-003 | [Week 1](../01_Black_Box/defects.md#def-003---whitespace-only-title-creates-a-task-with-a-blank-displayed-title) | TC-GUI-016 | Still fails: whitespace-only title creates a task | None |
