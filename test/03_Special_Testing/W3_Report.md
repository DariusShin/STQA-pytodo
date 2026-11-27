# Week 3 - GUI, Compatibility, Usability and Accessibility Testing

| Item | Value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance, September 2026 |
| Lab group | Wednesday Lab - Group 2 |
| Phase owner | Darius Lee Shin |
| Execution dates | 2026-11-18: GUI, accessibility, compatibility C01-C04 (macOS)<br>2026-11-24: compatibility C05-C06 (Windows 11)<br>2026-11-26: usability session (users: Eu Kwan Ik, Ameera Alysha binti Azlan; recorded by Darius Lee Shin, Mohamad Shukri Bin Abdul Ajed) |
| Environment | macOS 26.5.2; Windows 11 Home 25H2 (build 26200, Acer Nitro 5 AN515-45); Python 3.14.7, pytest 9.1.1, pytest-playwright 0.10.0, Playwright 1.65.2; axe-core 4.12.1; Lighthouse 12.8.2; app served by `python app.py` at `http://127.0.0.1:5000` |

## Deliverable checklist

- [x] [2. GUI testing checklist/results](#2-gui-testing-checklist-and-results) - 22 cases in [1_GUI/test_cases.md](1_GUI/test_cases.md)
- [x] [3. Compatibility/configuration matrix](#3-compatibilityconfiguration-matrix) - 8 scenarios x 6 configurations in [2_Compatibility/test_cases.md](2_Compatibility/test_cases.md)
- [x] [4. Usability observations](#4-usability-observations) - 4 rated observations in [3_Usability/observations.md](3_Usability/observations.md)
- [x] [5. Basic accessibility findings](#5-basic-accessibility-findings) - 18 WCAG checks in [4_Accessibility/test_cases.md](4_Accessibility/test_cases.md)
- [x] [6. Defects and improvement recommendations](#6-defects-and-improvement-recommendations) - DEF-004 to DEF-013 in [defects.md](defects.md)

## 1. Scope, method and environment

| In scope | Out of scope (owning phase) |
| --- | --- |
| The six pages: `/login`, `/register`, `/`, `/tasks/new`, `/tasks/<id>/edit`, `/dashboard`, and the shared navigation bar | API behaviour and status codes (Week 4) |
| Selected browser, OS and viewport combinations | Script injection and other security behaviour (Week 5) |
| Keyboard, accessibility-tree and contrast checks against a WCAG 2.2 A/AA subset | Load and response time (Week 5) |
| Usability by a short session with team members as users | Testing with real end users; full WCAG conformance audit; screen readers |

**Test basis.** Expected results were written before execution and cite the interface text (for example `min 8 characters`), the project README, Week 1 requirements REQ-001 to REQ-008, WCAG 2.2 success criteria, or Nielsen's heuristics.

**Method.** GUI, compatibility and accessibility cases are automated with Playwright and pytest (`1_GUI/test_gui.py`, `2_Compatibility/test_compatibility.py`, `4_Accessibility/test_accessibility.py`). Each script performs the documented steps, checks the expected result, saves `.jpg` evidence and writes a per-run results file listing every check with its actual value. Each suite was run twice with identical verdicts. Visual judgements are recorded as notes and checked against the screenshots. Accessible names are read from Chrome's accessibility tree.

**Test data.** Fixture Set A ([fixtures.md](fixtures.md)) gives every page a populated state: one task per urgency class, one per category, a 200-character and a 60-character unbroken title, a title with `&`, `<`, `>`, quotes and non-Latin text, and an empty account for empty-state checks.

**Pre-execution source review.** Reading `templates/*.html` and `static/style.css` produced ten hypotheses, each confirmed in the browser before a defect was logged:

| # | Source observation | Confirmed by |
| --- | --- | --- |
| H1 | No `<meta name="viewport">`; no `@media` rules | TC-CMP-007 on C02/C03 (DEF-006) |
| H2 | Labels have no `for`, inputs no `id` | TC-A11Y-005 (DEF-007) |
| H3 | Complete/reopen button content is only `○` or `✓` | TC-A11Y-001/007 (DEF-008) |
| H4 | Filters and search have no visible labels | TC-GUI-008, TC-A11Y-006 (DEF-007) |
| H5 | `#999999` on white = 2.85:1 | TC-A11Y-004 (DEF-009) |
| H6 | No success message after create/edit/delete/complete | TC-GUI-017 (USA-OBS-001) |
| H7 | Errors have no `role="alert"` or live region | TC-A11Y-015 (DEF-011) |
| H8 | No skip link | TC-A11Y-009 (DEF-010) |
| H9 | Task title rendered with the `safe` filter | TC-GUI-020 (DEF-005) |
| H10 | Non-wrapping flex navigation with fixed padding | TC-GUI-005 at 390 px (DEF-004) |

**Entry and exit criteria.**

| Entry | Exit |
| --- | --- |
| App starts locally with Fixture Set A seeded | Every case is Pass, Fail, Blocked or Not Run, with a reason for Blocked |
| Configuration matrix agreed and browser versions recorded | Every Fail links to a defect or a usability observation |
| Expected results written before execution | Every defect reproduced at least twice, with screenshot evidence |

## 2. GUI testing checklist and results

Executed 2026-11-18 on C01 (Chrome 157.0.8103.80, macOS, 1440x900, headless). Full cases: [1_GUI/test_cases.md](1_GUI/test_cases.md).

| ID | Page / element | Check | Expected result | Actual | Status | Evidence | Defect |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-GUI-001 | Login - layout | Heading, fields, button and Register link present and aligned | All elements in one card; password masked | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-001-login-layout-20261118.jpg) | — |
| TC-GUI-002 | Login - error message | Invalid credentials show an error | Distinct error box; stays on `/login`; does not reveal which field was wrong | As expected; username field emptied | Pass | [jpg](1_GUI/evidences/TC-GUI-002-login-error-20261118.jpg) | — |
| TC-GUI-003 | Register - hints | Field rules visible before input | Username and password hints readable beside labels | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-003-register-hints-20261118.jpg) | — |
| TC-GUI-004 | Register - error messages | Each invalid input gets a specific message | Message names the broken rule; an 8-character password is accepted | Messages correct; 8-character password rejected; fields emptied | Fail | [jpg](1_GUI/evidences/TC-GUI-004-register-errors-s1-20261118.jpg) | DEF-001 |
| TC-GUI-005 | Navigation bar | Items match login state and stay readable | Correct items; no item text broken across lines (H10) | Correct items; at 390 px the brand and `Log out` wrap and `Log out` is pushed off-screen | Fail | [jpg](1_GUI/evidences/TC-GUI-005-nav-logged-out-20261118.jpg) | DEF-004 |
| TC-GUI-006 | Brand link | Goes to the right place | Logged in -> `/`; logged out -> `/login` | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-006-brand-link-20261118.jpg) | — |
| TC-GUI-007 | Task list - header | Heading and New Task button | `My Tasks`; `+ New Task` opens `/tasks/new` | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-007-list-header-20261118.jpg) | — |
| TC-GUI-008 | Task list - filters | Filters behave predictably | Selects apply on change; search on button or Enter; values persist | As expected; filters have no visible labels (see TC-A11Y-006) | Pass | [jpg](1_GUI/evidences/TC-GUI-008-filters-applied-20261118.jpg) | — |
| TC-GUI-009 | Task list - table/empty state | Column headers and empty message | Headers present; single "no tasks match" message | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-009-empty-search-20261118.jpg) | — |
| TC-GUI-010 | Urgency badges | Distinct, labelled badge per class | Six texts; four date classes distinguishable | Task due today shows `Overdue`; others correct | Fail | [jpg](1_GUI/evidences/TC-GUI-010-badges-20261118.jpg) | DEF-002 |
| TC-GUI-011 | Complete/reopen button | Button matches task state | `○` open, `✓` done; done row struck through | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-011-toggle-done-20261118.jpg) | — |
| TC-GUI-012 | Edit link | Opens pre-filled form | All saved values pre-filled | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-012-edit-prefill-20261118.jpg) | — |
| TC-GUI-013 | Delete confirmation | Delete asks for confirmation | Dialog; Cancel keeps, OK removes | As expected (`Delete this task?`) | Pass | [jpg](1_GUI/evidences/TC-GUI-013-before-delete-20261118.jpg) | — |
| TC-GUI-014 | New Task form | Fields and controls | Title, Description, Category (None + 4), Due Date; Create and Cancel | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-014-new-form-20261118.jpg) | — |
| TC-GUI-015 | Edit Task form | Edit-mode labelling | `Edit Task`, `Save Changes`; Cancel does not save | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-015-edit-form-20261118.jpg) | — |
| TC-GUI-016 | Required title | Empty and whitespace titles blocked | Both blocked with a message; no task created | Empty blocked; whitespace-only creates a task | Fail | [jpg](1_GUI/evidences/TC-GUI-016-empty-title-20261118.jpg) | DEF-003 |
| TC-GUI-017 | Action feedback | Visible confirmation after actions | Message or highlight after create, edit, delete, complete | None after any action | Fail | [jpg](1_GUI/evidences/TC-GUI-017-feedback-create-20261118.jpg) | USA-OBS-001 |
| TC-GUI-018 | Dashboard cards | Five labelled counters | Labels correct; colours match badges | `Completed (last 7 days)` green; `Done` badge grey | Fail | [jpg](1_GUI/evidences/TC-GUI-018-dashboard-20261118.jpg) | USA-OBS-002 |
| TC-GUI-019 | Long content | Long titles keep layout | No overflow or page scroll at 1440 px | As expected | Pass | [jpg](1_GUI/evidences/TC-GUI-019-long-content-20261118.jpg) | — |
| TC-GUI-020 | Special characters | Titles displayed as entered | `&`, `<`, `>`, quotes, non-Latin text shown literally | `<b>bold</b>` rendered as bold in the list | Fail | [jpg](1_GUI/evidences/TC-GUI-020-special-list-20261118.jpg) | DEF-005 |
| TC-GUI-021 | Page titles | Tab title identifies the page | Six distinct titles with the app name | As expected | Pass | [json](1_GUI/evidences/results-C01-20261118-1933.json) | — |
| TC-GUI-022 | Visual consistency | Consistent controls across pages | One style per control type | Buttons, links, headings and card corners differ | Fail | [jpg](1_GUI/evidences/TC-GUI-022-consistency-login-20261118.jpg) | USA-OBS-003 |

| Total | Pass | Fail | Blocked | Not Run | Pass rate |
| --- | --- | --- | --- | --- | --- |
| 22 | 14 | 8 | 0 | 0 | 63.6% |

The eight failures are three re-confirmed Week 1 defects (DEF-001 to 003), two new defects (DEF-004, DEF-005) and three usability observations (USA-OBS-001 to 003).

## 3. Compatibility/configuration matrix

Scenarios: [2_Compatibility/test_cases.md](2_Compatibility/test_cases.md). Each configuration was run twice; only differences from C01 are reported. Tablet and phone results use Chrome mobile emulation, not real devices.

### 3.1 Configurations

| Config | OS | Browser | Viewport / device | Scaling | Locale / timezone | Type | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 (baseline) | macOS 26.5.2 | Chrome 157.0.8103.80 | 1440x900 | 100%, DPR 1 | en-GB / Asia/Kuala_Lumpur | Real | 8/8 Pass |
| C02 | macOS 26.5.2 | Chrome 157.0.8103.80, mobile emulation | 768x1024 tablet, touch | DPR 2 | en-GB / Asia/Kuala_Lumpur | Emulated | 7/8 (TC-CMP-007, DEF-006) |
| C03 | macOS 26.5.2 | Chrome 157.0.8103.80, mobile emulation | 390x844 phone, touch | DPR 3 | en-GB / Asia/Kuala_Lumpur | Emulated | 7/8 (TC-CMP-007, DEF-006) |
| C04 | macOS 26.5.2 | Firefox 159.0 (Playwright build v1572) | 1440x900 | 100%, DPR 1 | Default / Asia/Kuala_Lumpur | Real | 8/8 Pass |
| C05 | Windows 11 25H2 (build 26200) | Chrome 157.0.8103.80 | 1536x864 (1920x1080 native) | 125% display, DPR 1 | en-US, `dd/MM/yy` / UTC+08:00 | Real | 8/8 Pass |
| C06 | Windows 11 25H2 (build 26200) | Firefox 159.0 (Playwright build v1572) | 1536x864 (1920x1080 native) | 125% display, DPR 1 | en-US, `dd/MM/yy` / UTC+08:00 | Real | 8/8 Pass |
| C07 | iOS or Android | Mobile browser | Physical phone | Default | - | Real | Blocked: the app listens on 127.0.0.1 only and is not modified |

**Selection.** The desktop configurations form a 2x2 design, two operating systems by two browser engines (Chrome/Blink, Firefox/Gecko), so OS and browser effects can be separated. Chrome on the Windows laptop was updated to 157.0.8103.80, the same release as on macOS, so C01 and C05 compare the same browser version. Chrome emulation adds tablet and phone widths. Playwright drives its own Firefox build (159.0), not the installed release (160.0.1). Microsoft Edge (same Blink engine as Chrome) and Safari/WebKit were excluded to keep scope manageable.

### 3.2 Compatibility smoke scenarios

| ID | Scenario | Expected on every configuration | C01 | C02 | C03 | C04 | C05 | C06 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-CMP-001 | Register, log in, log out | Pages render; forms submit; redirects match C01 | Pass | Pass | Pass | Pass | Pass | Pass |
| TC-CMP-002 | Create task with date picker | Date saved as `YYYY-MM-DD` whatever the display format | Pass | Pass | Pass | Pass | Pass | Pass |
| TC-CMP-003 | Filter and search | Auto-submit works; results match C01 | Pass | Pass | Pass | Pass | Pass | Pass |
| TC-CMP-004 | Complete and reopen | Button and strikethrough update | Pass | Pass | Pass | Pass | Pass | Pass |
| TC-CMP-005 | Edit task | Pre-filled values, including date, shown and saved | Pass | Pass | Pass | Pass | Pass | Pass |
| TC-CMP-006 | Delete with confirmation | Native dialog; Cancel/OK as on C01 | Pass | Pass | Pass | Pass | Pass | Pass |
| TC-CMP-007 | Navigation and table layout | All items readable; no clipped text | Pass | Fail (DEF-006) | Fail (DEF-006) | Pass | Pass | Pass |
| TC-CMP-008 | Dashboard layout | Cards reflow without overlap | Pass | Pass | Pass | Pass | Pass | Pass |

48 case runs: 46 Pass, 2 Fail (95.8%).

### 3.3 Interpretation

| Question | Answer |
| --- | --- |
| Browser differences? | None functional. Chrome and Firefox give the same results on macOS and Windows, including the date control, delete dialog and auto-submitting filters. Firefox differs only cosmetically (due dates on one line, native select styling; on macOS a larger `○` glyph). |
| OS differences? | None functional, with the same Chrome release (157.0.8103.80) on both systems. Windows renders in Segoe UI, giving slightly taller rows. Smallest text is 12.5 px on every desktop configuration. Windows used a 1536x864 viewport, so layout comparisons with C01 are not exact. |
| Viewport differences? | Yes. Emulated tablet and phone lay the page out at 980 px and scale it down, so text renders at 9.8 px and 5.0 px (DEF-006). Narrow desktop windows wrap the navigation and push `Log out` off-screen (DEF-004). |
| Is any task blocked? | No. Reading on phones needs zooming (DEF-006) and logging out in narrow windows needs horizontal scrolling (DEF-004), so both are Moderate. |

## 4. Usability observations

**Method.** On 2026-11-26, Eu Kwan Ik and Ameera Alysha binti Azlan used PyTodo Pro running locally in a short usability session, carrying out the everyday tasks (register, log in, create, edit, complete and delete tasks, filter, view the dashboard). Darius Lee Shin and Mohamad Shukri Bin Abdul Ajed recorded what they experienced. The problems they met matched the four usability issues found by the GUI suite, so these were mapped to Nielsen's heuristics and given an agreed severity on Nielsen's 0-4 scale. Full records: [3_Usability/observations.md](3_Usability/observations.md).

**Severity scale.** Each rating combines frequency, impact and persistence: 0 not a problem; 1 cosmetic (fix if time allows); 2 minor (low priority); 3 major (high priority); 4 catastrophe (must fix before release). A rating of 3 or 4 would be logged as a defect.

| ID | Guideline quality | Heuristic | Observation | Severity | Recommendation |
| --- | --- | --- | --- | --- | --- |
| USA-OBS-001 | Feedback | 1 Visibility of system status | No confirmation after create, edit, complete or delete | 2 Minor | R3 |
| USA-OBS-002 | Consistency | 4 Consistency and standards | Dashboard "completed" card green; `Done` badge grey | 1 Cosmetic | R5 |
| USA-OBS-003 | Consistency | 4 Consistency and standards | Buttons, links, headings and card corners styled differently across pages | 1 Cosmetic | R5 |
| USA-OBS-004 | Error prevention / recovery | 9 Help users recover from errors | Username emptied after a login or registration error | 2 Minor | R4 |

**Interpretation.** No observation reaches severity 3, so the interface is usable but gives weak feedback and is visually inconsistent. No separate issues with ease of navigation or understandability were recorded in the session; these were also covered by the GUI cases (TC-GUI-005 to 007, 014, 015, 021).

## 5. Basic accessibility findings

Executed 2026-11-18 on C01. Three passes: automated scans (axe-core and Lighthouse), a keyboard-only pass, and accessibility-tree, reflow and zoom checks. Full cases: [4_Accessibility/test_cases.md](4_Accessibility/test_cases.md).

### 5.1 WCAG 2.2 checklist (Level A/AA subset)

| ID | WCAG SC (level) | Check | Expected | Actual | Status | Evidence | Defect |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-A11Y-001 | 1.1.1 Non-text content (A) | Icon-only controls have a text alternative | Every icon control named | `○`/`✓` named only by the symbol | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-001-names-20261118.jpg) | DEF-008 |
| TC-A11Y-002 | 1.3.1 Info and relationships (A) | Structure in markup | One `h1`; `th` cells; landmarks | `h1` and headers present; no `main` landmark | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-002-structure-20261118.jpg) | DEF-010 |
| TC-A11Y-003 | 1.4.1 Use of colour (A) | Urgency not by colour alone | Badge text conveys urgency | Identifiable in greyscale | Pass | [jpg](4_Accessibility/evidences/TC-A11Y-003-greyscale-list-20261118.jpg) | — |
| TC-A11Y-004 | 1.4.3 Contrast minimum (AA) | Text contrast ≥ 4.5:1 | All text passes | Completed title and empty state 2.85:1 | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-004-contrast-empty-state-20261118.jpg) | DEF-009 |
| TC-A11Y-005 | 1.3.1 / 4.1.2 Labels associated | Label focuses its field; field named by label | Each field named (H2) | Labels do not focus fields; names empty | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-005-labels-20261118.jpg) | DEF-007 |
| TC-A11Y-006 | 3.3.2 Labels or instructions (A) | Every input has a visible label | Filters labelled (H4) | No visible labels; search named by placeholder | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-006-filter-labels-20261118.jpg) | DEF-007 |
| TC-A11Y-007 | 4.1.2 Name, role, value (A) | Toggle states purpose and state | e.g. "Mark <title> as done" (H3) | Names `○` / `✓` only | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-007-toggle-name-20261118.jpg) | DEF-008 |
| TC-A11Y-008 | 2.1.1 Keyboard (A) | All functions by keyboard | Task flow by keyboard; no trap | Completed; no trap | Pass | [jpg](4_Accessibility/evidences/TC-A11Y-008-keyboard-end-20261118.jpg) | — |
| TC-A11Y-009 | 2.4.1 Bypass blocks (A) | Skip the navigation bar | Skip link or landmark (H8) | Neither present | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-009-bypass-20261118.jpg) | DEF-010 |
| TC-A11Y-010 | 2.4.2 Page titled (A) | Unique, descriptive titles | As TC-GUI-021 | Six unique titles | Pass | [json](4_Accessibility/evidences/results-C01-20261118-213348.json) | — |
| TC-A11Y-011 | 2.4.3 / 2.4.7 Focus order and visible (AA) | Logical order; visible focus | Both | Both | Pass | [jpg](4_Accessibility/evidences/TC-A11Y-011-focus-first-20261118.jpg) | — |
| TC-A11Y-012 | 1.4.10 Reflow (AA) | Usable at 320 CSS px | No 2-D scrolling except the table (H1) | Navigation overflows; forms and dashboard scroll sideways | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-012-reflow-login-20261118.jpg) | DEF-004 |
| TC-A11Y-013 | 1.4.4 Resize text (AA) | 200% zoom | No clipping or overlap | As expected | Pass | [jpg](4_Accessibility/evidences/TC-A11Y-013-zoom-register-20261118.jpg) | — |
| TC-A11Y-014 | 3.1.1 Language of page (A) | `lang` attribute | `lang="en"` | Present on every page | Pass | [json](4_Accessibility/evidences/results-C01-20261118-213348.json) | — |
| TC-A11Y-015 | 3.3.1 / 4.1.3 Errors announced (A/AA) | Errors described and announced | Announced without focus change (H7) | Text only; no alert role, live region or focus move | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-015-error-login-20261118.jpg) | DEF-011 |
| TC-A11Y-016 | 2.5.8 Target size (AA) | Targets ≥ 24x24 CSS px | Minimum or spacing exception met | `Edit` 23x15, `Delete` 39x15, stacked | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-016-targets-20261118.jpg) | DEF-012 |
| TC-A11Y-017 | 2.4.6 Headings and labels (AA) | Descriptive headings and labels | Clear text | Control columns have empty headers | Fail | [jpg](4_Accessibility/evidences/TC-A11Y-017-headings-20261118.jpg) | DEF-013 |
| TC-A11Y-018 | Automated scan summary | Lighthouse and axe per page | Every critical/serious issue triaged | Six pages scanned; all triaged | Pass | [json](4_Accessibility/evidences/reports/summary-20261118.json) | — |

**Result:** 18 cases, 7 Pass, 11 Fail.

### 5.2 Automated scan results

| Page | Lighthouse score | axe critical | axe serious | axe moderate/minor | Reports |
| --- | --- | --- | --- | --- | --- |
| `/login` | 91 | 1 (`label`) | 0 | 2 (`landmark-one-main`, `region`) | [axe](4_Accessibility/evidences/reports/axe-login-20261118.json), [Lighthouse](4_Accessibility/evidences/reports/lighthouse-login-20261118.report.html) |
| `/register` | 91 | 1 (`label`) | 0 | 2 (`landmark-one-main`, `region`) | [axe](4_Accessibility/evidences/reports/axe-register-20261118.json), [Lighthouse](4_Accessibility/evidences/reports/lighthouse-register-20261118.report.html) |
| `/` | 76 | 1 (`select-name`) | 1 (`color-contrast`) | 3 (`landmark-one-main`, `region`, `empty-table-header`) | [axe](4_Accessibility/evidences/reports/axe-list-20261118.json), [Lighthouse](4_Accessibility/evidences/reports/lighthouse-list-20261118.report.html) |
| `/tasks/new` | 82 | 2 (`label`, `select-name`) | 0 | 2 (`landmark-one-main`, `region`) | [axe](4_Accessibility/evidences/reports/axe-new-20261118.json), [Lighthouse](4_Accessibility/evidences/reports/lighthouse-new-20261118.report.html) |
| `/tasks/<id>/edit` | 82 | 2 (`label`, `select-name`) | 0 | 2 (`landmark-one-main`, `region`) | [axe](4_Accessibility/evidences/reports/axe-edit-20261118.json), [Lighthouse](4_Accessibility/evidences/reports/lighthouse-edit-20261118.report.html) |
| `/dashboard` | 100 | 0 | 0 | 2 (`landmark-one-main`, `region`) | [axe](4_Accessibility/evidences/reports/axe-dashboard-20261118.json), [Lighthouse](4_Accessibility/evidences/reports/lighthouse-dashboard-20261118.report.html) |

**Triage.** `label` and `select-name` -> DEF-007; `color-contrast` -> DEF-009; `landmark-one-main`/`region` -> DEF-010; `empty-table-header`/`td-has-header` -> DEF-013; `target-size` -> DEF-012. No false positives. Neither tool flagged the `○`/`✓` button names (DEF-008), because a symbol counts as a name; only the manual-equivalent check found it, so a clean scan is not sufficient evidence.

## 6. Defects and improvement recommendations

Full records: [defects.md](defects.md). Severity guidance: **Major** when a task cannot be completed; **Moderate** when it is materially harder or misleading; **Minor** for cosmetic or consistency issues.

| Defect | Title | Source case(s) | Config | Severity / Priority |
| --- | --- | --- | --- | --- |
| DEF-004 | Navigation bar wraps and pushes `Log out` off-screen at a 390 px viewport | TC-GUI-005, TC-A11Y-012 | C01 at 390x844 | Moderate / Medium |
| DEF-005 | HTML in a task title is rendered as markup in the task list | TC-GUI-020 | C01 | Moderate / High |
| DEF-006 | Pages render at a 980 px desktop layout on tablets and phones | TC-CMP-007 | C02, C03 | Moderate / Medium |
| DEF-007 | Form fields and filters have no programmatically associated labels | TC-A11Y-005, 006 | C01 | Major / High |
| DEF-008 | Complete/reopen button has no meaningful accessible name or state | TC-A11Y-001, 007 | C01 | Major / High |
| DEF-009 | Completed titles and empty-state text have 2.85:1 contrast | TC-A11Y-004 | C01 | Moderate / Medium |
| DEF-010 | No main landmark and no skip link | TC-A11Y-002, 009 | C01 | Minor / Low |
| DEF-011 | Form errors are not exposed for screen-reader announcement | TC-A11Y-015 | C01 | Moderate / Medium |
| DEF-012 | Edit and Delete targets are too small and too close together | TC-A11Y-016 | C01 | Minor / Low |
| DEF-013 | Table columns holding controls have empty headers | TC-A11Y-017 | C01 | Minor / Low |

DEF-001 to DEF-003 (Week 1) were reproduced by TC-GUI-004, 010 and 016.

### Recommendations

| # | Recommendation | Addresses | Effort | Priority |
| --- | --- | --- | --- | --- |
| R1 | Escape task titles when rendering the task list | DEF-005 | L | High |
| R6 | Associate every label with its field (`for`/`id`); give filters visible labels | DEF-007 | L | High |
| R7 | Name the toggle "Mark <title> as done" and expose its state (`aria-pressed` or a checkbox) | DEF-008 | L | High |
| R2 | Add a viewport meta tag and a narrow-screen navigation layout | DEF-004, DEF-006 | M | Medium |
| R3 | Show a confirmation message after create, edit, complete and delete | USA-OBS-001 | L | Medium |
| R8 | Darken completed-title and empty-state text to ≥ 4.5:1 (e.g. `#767676`) | DEF-009 | L | Medium |
| R9 | Mark form errors with `role="alert"` or move focus to them | DEF-011 | L | Medium |
| R4 | Keep the entered username after a login or registration error | USA-OBS-004 | L | Low |
| R5 | Apply one style per control type on every page | USA-OBS-002, 003 | M | Low |
| R10 | Wrap content in `<main>` and add a skip link | DEF-010 | L | Low |
| R11 | Make Edit/Delete at least 24x24 px or separate them | DEF-012 | L | Low |
| R12 | Give control columns header text (visually hidden if needed) | DEF-013 | L | Low |

A viewport tag alone (R2) would expose DEF-004 on phones, so both defects need the narrow-screen navigation as well.

## 7. Summary and limitations

| Technique | Cases | Pass | Fail | Blocked | Not Run | Pass rate |
| --- | --- | --- | --- | --- | --- | --- |
| GUI | 22 | 14 | 8 | 0 | 0 | 63.6% |
| Compatibility (a case fails if it failed on any configuration) | 8 | 7 | 1 | 0 | 0 | 87.5% |
| Accessibility | 18 | 7 | 11 | 0 | 0 | 38.9% |
| **Total** | **48** | **28** | **20** | **0** | **0** | **58.3%** |

- **New defects:** 10 (2 Major, 5 Moderate, 3 Minor). Accessibility produced 7 of the 10 and both Major ones, so it is the weakest quality area measured this week.
- **Usability:** 4 observations (2 Minor, 2 Cosmetic), none blocking.

Limitations:
- Tablet and phone results come from Chrome emulation, not real devices; a physical phone (C07) could not reach the app.
- Firefox was tested through Playwright's 159.0 build, not the installed 160.0.1. Edge and Safari/WebKit were not tested.
- All runs were headless. Native dialogs, date pickers and validation bubbles are recorded as text, not screenshots, and date fields were filled by value.
- 200% zoom was emulated with an equivalent viewport. Only a subset of WCAG 2.2 A/AA was checked, and screen readers were not used.
- The usability session was short and its two users were team members, not real end users.
