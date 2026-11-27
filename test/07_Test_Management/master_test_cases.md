# Master Test-Case Repository

Consolidated test cases for **PyTodo Pro** (Weeks 1-6), in the course 12-field test-case template (`Test Case ID`, `Feature/Requirement`, `Technique/Test Type`, `Objective`, `Preconditions`, `Test Data`, `Steps`, `Expected Result`, `Actual Result`, `Status`, `Evidence`, `Defect ID`).

**Rule: results are never edited here.** A correction is made in the source week's file and then copied again. Appendices A and D are verbatim copies; Appendices B and F were normalised to the template (original IDs kept in a `Source ID` column).

## 1. Repository summary

| Week | Phase | Source file | ID range | Designed cases | Execution units | Status of this repository |
| --- | --- | --- | --- | --- | --- | --- |
| W1 | Black-box | `01_Black_Box/test_cases.md` | `TC-BB-001` to `044` | 44 | 44 (40 Pass, 4 Fail) | Copied verbatim (Appendix A) |
| W2 | White-box | `02_White_Box_Coverage/README.md`, Tables 4-6a | `TC-WB-*` (19 basis-path cases) | 19 | 50 pytest instances (all Pass): 30 backend + 20 helper | Normalised (Appendix B) |
| W3 | GUI, compatibility, usability, accessibility | `03_Special_Testing/` (`1_GUI` to `4_Accessibility`) | `TC-GUI-001` to `022`, `TC-CMP-001` to `008`, `TC-USA-001` to `005`, `TC-A11Y-001` to `018` | 53 | 53 (28 Pass, 20 Fail, 5 Not Run) | Copied verbatim (Appendix C); usability review not yet run |
| W4 | Web and API | `04_Web_API/test_cases.md` | `TC-WEB-001` to `016`, `TC-API-001` to `045` | 61 | 61 (43 Pass, 18 Fail) | Copied verbatim (Appendix D) |
| W5 | Security and performance | `05_Security_Performance/` | TBD | TBD | TBD | **Pending**: not complete (Appendix E) |
| W6 | Automation and regression | `06_Automation_Regression/README.md`, Task 3 | `TC-AUT-001` to `028` | 28 (not counted as new scope) | 65 pytest checks (58 Pass, 7 Fail known) | Normalised (Appendix F) |
| **Total (W1-W4)** | | | | **177 designed** (44 + 19 + 53 + 61) | **208 execution units** (44 + 50 + 53 + 61): 161 Pass, 42 Fail, 0 Blocked, 5 Not Run; W6's 65 checks are reported separately | In progress until W5 is merged and TC-USA-001 to 005 are run |

The 208 figure counts execution units because W2's 19 designed path cases run as 50 pytest instances. The index below lists the 177 designed cases (44 + 19 + 53 + 61) plus the 28 W6 automated cases.

**Source commits.** Record the commit of each source file when it is copied: W1 `TBD`, W2 `TBD`, W4 `TBD`, W6 `TBD` (`git rev-parse --short HEAD` on the source branch). Application commits tested: W4 `fc0767f`, W6 `9cc1f34`.

## 2. Master index

Status values: Pass, Fail, Blocked, Not Run. Compatibility cases (`TC-CMP`) are run once per configuration; their status here is the overall result across C01-C06 (Fail if any configuration failed). C07 (physical phone) is optional and blocked by default, so it is not counted. Requirement mapping for W2 was made by the Defect & Metrics Coordinator (the W2 report names none) and needs W2 author sign-off.

### 2.1 Week 1 - Black-box (Appendix A)

| Case ID | Title | Requirement | Technique | Status | Defect |
| --- | --- | --- | --- | --- | --- |
| [TC-BB-001](#tc-bb-001---username-length-2) | Username length 2 | REQ-001 | BVA / Functional | Pass | - |
| [TC-BB-002](#tc-bb-002---username-length-3) | Username length 3 | REQ-001 | BVA / Functional | Pass | - |
| [TC-BB-003](#tc-bb-003---username-length-4) | Username length 4 | REQ-001 | BVA / Functional | Pass | - |
| [TC-BB-004](#tc-bb-004---username-length-19) | Username length 19 | REQ-001 | BVA / Functional | Pass | - |
| [TC-BB-005](#tc-bb-005---username-length-20) | Username length 20 | REQ-001 | BVA / Functional | Pass | - |
| [TC-BB-006](#tc-bb-006---username-length-21) | Username length 21 | REQ-001 | BVA / Functional | Pass | - |
| [TC-BB-007](#tc-bb-007---password-length-7) | Password length 7 | REQ-001 | BVA / Functional | Pass | - |
| [TC-BB-008](#tc-bb-008---password-length-8) | Password length 8 | REQ-001 | BVA / Functional | Fail | DEF-001 |
| [TC-BB-009](#tc-bb-009---password-length-9) | Password length 9 | REQ-001 | BVA / Functional | Pass | - |
| [TC-BB-010](#tc-bb-010---valid-registration) | Valid registration | REQ-001 | EP / Functional | Pass | - |
| [TC-BB-011](#tc-bb-011---disallowed-username-character) | Disallowed username character | REQ-001 | EP / Functional | Pass | - |
| [TC-BB-012](#tc-bb-012---empty-registration-username) | Empty registration username | REQ-001 | EP / Functional / Browser validation | Pass | - |
| [TC-BB-013](#tc-bb-013---empty-registration-password) | Empty registration password | REQ-001 | EP / Functional / Browser validation | Pass | - |
| [TC-BB-014](#tc-bb-014---login-credential-decision-rule-1) | Login credential decision rule 1 | REQ-002 | Decision table / Functional | Pass | - |
| [TC-BB-015](#tc-bb-015---login-credential-decision-rule-2) | Login credential decision rule 2 | REQ-002 | Decision table / Functional | Pass | - |
| [TC-BB-016](#tc-bb-016---login-credential-decision-rule-3) | Login credential decision rule 3 | REQ-002 | Decision table / Functional | Pass | - |
| [TC-BB-017](#tc-bb-017---login-credential-decision-rule-4) | Login credential decision rule 4 | REQ-002 | Decision table / Functional | Pass | - |
| [TC-BB-018](#tc-bb-018---protected-page-while-logged-out) | Protected page while logged out | REQ-002 | State transition / Functional | Pass | - |
| [TC-BB-019](#tc-bb-019---logout-revokes-protected-page-access) | Logout revokes protected-page access | REQ-002 | State transition / Functional | Pass | - |
| [TC-BB-020](#tc-bb-020---create-and-persist-a-full-field-task) | Create and persist a full-field task | REQ-003 | EP / Functional | Pass | - |
| [TC-BB-021](#tc-bb-021---create-a-title-only-task) | Create a title-only task | REQ-003 | EP / Functional | Pass | - |
| [TC-BB-022](#tc-bb-022---empty-title-browser-validation) | Empty title browser validation | REQ-003 | EP / Browser validation | Pass | - |
| [TC-BB-023](#tc-bb-023---reject-a-whitespace-only-title) | Reject a whitespace-only title | REQ-003 | EP / Functional / Input validation | Fail | DEF-003 |
| [TC-BB-024](#tc-bb-024---edit-and-persist-all-task-fields) | Edit and persist all task fields | REQ-003 | Functional | Pass | - |
| [TC-BB-025](#tc-bb-025---cancel-edit-preserves-saved-data) | Cancel edit preserves saved data | REQ-003 | State transition / Functional | Pass | - |
| [TC-BB-026](#tc-bb-026---cancel-deletion-retains-task) | Cancel deletion retains task | REQ-003 | State transition / Functional | Pass | - |
| [TC-BB-027](#tc-bb-027---confirm-deletion-and-verify-persistence) | Confirm deletion and verify persistence | REQ-003 | State transition / Functional | Pass | - |
| [TC-BB-028](#tc-bb-028---complete-an-open-task) | Complete an Open task | REQ-004 | State transition / Functional | Pass | - |
| [TC-BB-029](#tc-bb-029---reopen-a-done-task) | Reopen a Done task | REQ-004 | State transition / Functional | Pass | - |
| [TC-BB-030](#tc-bb-030---filter-by-category) | Filter by category | REQ-005 | EP / Functional | Pass | - |
| [TC-BB-031](#tc-bb-031---filter-open-tasks) | Filter Open tasks | REQ-005 | EP / Functional | Pass | - |
| [TC-BB-032](#tc-bb-032---filter-done-tasks) | Filter Done tasks | REQ-005 | EP / Functional | Pass | - |
| [TC-BB-033](#tc-bb-033---matching-title-search) | Matching title search | REQ-005 | EP / Functional | Pass | - |
| [TC-BB-034](#tc-bb-034---nonmatching-title-search) | Nonmatching title search | REQ-005 | EP / Functional | Pass | - |
| [TC-BB-035](#tc-bb-035---combined-filters-all-conditions-required) | Combined filters: all conditions required | REQ-005 | Decision table / Functional | Pass | - |
| [TC-BB-036](#tc-bb-036---urgency-bb-no-date) | Urgency: BB-NO-DATE | REQ-006 | EP / Functional | Pass | - |
| [TC-BB-037](#tc-bb-037---urgency-bb-yesterday) | Urgency: BB-YESTERDAY | REQ-006 | BVA / Functional | Pass | - |
| [TC-BB-038](#tc-bb-038---urgency-bb-today) | Urgency: BB-TODAY | REQ-006 | BVA / Functional | Fail | DEF-002 |
| [TC-BB-039](#tc-bb-039---urgency-bb-tomorrow) | Urgency: BB-TOMORROW | REQ-006 | BVA / Functional | Pass | - |
| [TC-BB-040](#tc-bb-040---urgency-bb-plus-two) | Urgency: BB-PLUS-TWO | REQ-006 | BVA / Functional | Pass | - |
| [TC-BB-041](#tc-bb-041---urgency-bb-plus-three) | Urgency: BB-PLUS-THREE | REQ-006 | BVA / Functional | Pass | - |
| [TC-BB-042](#tc-bb-042---completion-overrides-overdue-urgency) | Completion overrides overdue urgency | REQ-004 / REQ-006 | State transition / Functional | Pass | - |
| [TC-BB-043](#tc-bb-043---reconcile-dashboard-with-controlled-data) | Reconcile dashboard with controlled data | REQ-007 | Functional / Independent calculation | Fail | DEF-002 |
| [TC-BB-044](#tc-bb-044---visible-task-list-isolation-between-accounts) | Visible task-list isolation between accounts | REQ-008 | EP / Functional | Pass | - |

### 2.2 Week 2 - White-box (Appendix B)

| Case ID | Source ID | Unit under test | Requirement | Technique | Status | Defect |
| --- | --- | --- | --- | --- | --- | --- |
| [TC-WB-DB01](#tc-wb-db01---get_db) | DB01 | `get_db` | Supporting (no REQ) | Basis path / Integration | Pass | - |
| [TC-WB-DB02](#tc-wb-db02---get_db) | DB02 | `get_db` | Supporting (no REQ) | Basis path / Integration | Pass | - |
| [TC-WB-CL01](#tc-wb-cl01---close_connection) | CL01 | `close_connection` | Supporting (no REQ) | Basis path / Unit | Pass | - |
| [TC-WB-CL02](#tc-wb-cl02---close_connection) | CL02 | `close_connection` | Supporting (no REQ) | Basis path / Unit | Pass | - |
| [TC-WB-IN01](#tc-wb-in01---init_db) | IN01 | `init_db` | Supporting (no REQ) | Basis path / Integration | Pass | - |
| [TC-WB-IN02](#tc-wb-in02---init_db) | IN02 | `init_db` | Supporting (no REQ) | Basis path / Integration | Pass | - |
| [TC-WB-RT01](#tc-wb-rt01---row_to_task) | RT01 | `row_to_task` | REQ-003, REQ-006 | Basis path / Unit | Pass | - |
| [TC-WB-RT02](#tc-wb-rt02---row_to_task) | RT02 | `row_to_task` | REQ-003, REQ-004, REQ-006 | Basis path / Unit | Pass | - |
| [TC-WB-CN01](#tc-wb-cn01---get_category_name) | CN01 | `get_category_name` | REQ-003 | Basis path / Unit | Pass | - |
| [TC-WB-CN02](#tc-wb-cn02---get_category_name) | CN02 | `get_category_name` | REQ-003 | Basis path / Integration | Pass | - |
| [TC-WB-CN03](#tc-wb-cn03---get_category_name) | CN03 | `get_category_name` | REQ-003 | Basis path / Integration | Pass | - |
| [TC-WB-CI01](#tc-wb-ci01---get_category_id_by_name) | CI01 | `get_category_id_by_name` | REQ-003 | Basis path / Integration | Pass | - |
| [TC-WB-CI02](#tc-wb-ci02---get_category_id_by_name) | CI02 | `get_category_id_by_name` | REQ-003 | Basis path / Integration | Pass | - |
| [TC-WB-WF01](#tc-wb-wf01---login_required_web-factory) | WF01 | `login_required_web (factory)` | REQ-002 | Basis path / Unit | Pass | - |
| [TC-WB-WA01](#tc-wb-wa01---login_required_web-wrapper) | WA01 | `login_required_web (wrapper)` | REQ-002 | Basis path / Unit | Pass | - |
| [TC-WB-WA02](#tc-wb-wa02---login_required_web-wrapper) | WA02 | `login_required_web (wrapper)` | REQ-002 | Basis path / Unit | Pass | - |
| [TC-WB-AF01](#tc-wb-af01---login_required_api-factory) | AF01 | `login_required_api (factory)` | REQ-002, REQ-009 | Basis path / Unit | Pass | - |
| [TC-WB-AA01](#tc-wb-aa01---login_required_api-wrapper) | AA01 | `login_required_api (wrapper)` | REQ-002, REQ-009 | Basis path / Unit | Pass | - |
| [TC-WB-AA02](#tc-wb-aa02---login_required_api-wrapper) | AA02 | `login_required_api (wrapper)` | REQ-002, REQ-009 | Basis path / Unit | Pass | - |

### 2.3 Week 3 - Special testing (Appendix C)

| Case ID | Title | Requirement / standard | Technique | Status | Defect / observation |
| --- | --- | --- | --- | --- | --- |
| [TC-GUI-001](#tc-gui-001---login-page-layout) | Login page layout | REQ-002 | GUI checklist | Pass | - |
| [TC-GUI-002](#tc-gui-002---login-error-message) | Login error message | REQ-002 | GUI checklist | Pass | USA-OBS-004 (observation) |
| [TC-GUI-003](#tc-gui-003---registration-hints) | Registration hints | REQ-001 | GUI checklist | Pass | - |
| [TC-GUI-004](#tc-gui-004---registration-error-messages) | Registration error messages | REQ-001 | GUI checklist | Fail | DEF-001 (reproduced) |
| [TC-GUI-005](#tc-gui-005---navigation-bar) | Navigation bar | REQ-002 | GUI checklist | Fail | DEF-004 |
| [TC-GUI-006](#tc-gui-006---brand-link) | Brand link | REQ-002 | GUI checklist | Pass | - |
| [TC-GUI-007](#tc-gui-007---task-list-header) | Task list header | REQ-003 | GUI checklist | Pass | - |
| [TC-GUI-008](#tc-gui-008---filter-controls) | Filter controls | REQ-005 | GUI checklist | Pass | - |
| [TC-GUI-009](#tc-gui-009---task-table-and-empty-state) | Task table and empty state | REQ-003, REQ-005 | GUI checklist | Pass | - |
| [TC-GUI-010](#tc-gui-010---urgency-badges) | Urgency badges | REQ-006 | GUI checklist | Fail | DEF-002 (reproduced) |
| [TC-GUI-011](#tc-gui-011---complete-and-reopen-button) | Complete and reopen button | REQ-004 | GUI checklist | Pass | - |
| [TC-GUI-012](#tc-gui-012---edit-link-opens-a-pre-filled-form) | Edit link opens a pre-filled form | REQ-003 | GUI checklist | Pass | - |
| [TC-GUI-013](#tc-gui-013---delete-confirmation) | Delete confirmation | REQ-003 | GUI checklist | Pass | - |
| [TC-GUI-014](#tc-gui-014---new-task-form) | New Task form | REQ-003 | GUI checklist | Pass | - |
| [TC-GUI-015](#tc-gui-015---edit-task-form) | Edit Task form | REQ-003 | GUI checklist | Pass | - |
| [TC-GUI-016](#tc-gui-016---required-title) | Required title | REQ-003 | GUI checklist | Fail | DEF-003 (reproduced) |
| [TC-GUI-017](#tc-gui-017---feedback-after-actions) | Feedback after actions | REQ-003, REQ-004 | GUI checklist / Usability heuristic | Fail | USA-OBS-001 |
| [TC-GUI-018](#tc-gui-018---dashboard-cards) | Dashboard cards | REQ-007 | GUI checklist | Fail | USA-OBS-002 |
| [TC-GUI-019](#tc-gui-019---long-content) | Long content | REQ-003 | GUI checklist | Pass | - |
| [TC-GUI-020](#tc-gui-020---special-characters) | Special characters | REQ-003 | GUI checklist | Fail | DEF-005 |
| [TC-GUI-021](#tc-gui-021---page-titles) | Page titles | All pages | GUI checklist | Pass | - |
| [TC-GUI-022](#tc-gui-022---visual-consistency) | Visual consistency | All pages | GUI checklist | Fail | USA-OBS-003 |
| [TC-CMP-001](#tc-cmp-001---register-log-in-and-log-out) | Register, log in and log out | REQ-001, REQ-002 | Compatibility | Pass | - |
| [TC-CMP-002](#tc-cmp-002---create-a-task-with-the-date-picker) | Create a task with the date picker | REQ-003, REQ-006 | Compatibility | Pass | - |
| [TC-CMP-003](#tc-cmp-003---filter-and-search) | Filter and search | REQ-005 | Compatibility | Pass | - |
| [TC-CMP-004](#tc-cmp-004---complete-and-reopen) | Complete and reopen | REQ-004 | Compatibility | Pass | - |
| [TC-CMP-005](#tc-cmp-005---edit-a-task) | Edit a task | REQ-003 | Compatibility | Pass | - |
| [TC-CMP-006](#tc-cmp-006---delete-with-confirmation) | Delete with confirmation | REQ-003 | Compatibility | Pass | - |
| [TC-CMP-007](#tc-cmp-007---navigation-bar-and-task-table-layout) | Navigation bar and task table layout | REQ-002, REQ-003 | Compatibility | Fail (C02, C03) | DEF-006 (C02, C03) |
| [TC-CMP-008](#tc-cmp-008---dashboard-layout) | Dashboard layout | REQ-007 | Compatibility | Pass | - |
| [TC-USA-001](#tc-usa-001---ease-of-navigation) | Ease of navigation | All pages and the navigation bar; REQ-002, REQ-003, REQ-007 | Usability - heuristic evaluation | Not Run | - |
| [TC-USA-002](#tc-usa-002---feedback) | Feedback | All pages; REQ-001 to REQ-004 | Usability - heuristic evaluation | Not Run | - |
| [TC-USA-003](#tc-usa-003---consistency) | Consistency | All pages | Usability - heuristic evaluation | Not Run | - |
| [TC-USA-004](#tc-usa-004---error-prevention) | Error prevention | `/register`, `/login`, task forms, delete; REQ-001 to REQ-003 | Usability - heuristic evaluation | Not Run | - |
| [TC-USA-005](#tc-usa-005---understandability) | Understandability | All pages; REQ-004, REQ-006, REQ-007 | Usability - heuristic evaluation | Not Run | - |
| [TC-A11Y-001](#tc-a11y-001---non-text-content) | Non-text content | WCAG 2.2 SC 1.1.1 Non-text Content (A) | Accessibility (WCAG) - inspection | Fail | DEF-008 |
| [TC-A11Y-002](#tc-a11y-002---info-and-relationships) | Info and relationships | WCAG 2.2 SC 1.3.1 Info and Relationships (A) | Accessibility (WCAG) - inspection | Fail | DEF-010 |
| [TC-A11Y-003](#tc-a11y-003---use-of-colour) | Use of colour | WCAG 2.2 SC 1.4.1 Use of Color (A) | Accessibility (WCAG) - simulation | Pass | - |
| [TC-A11Y-004](#tc-a11y-004---text-contrast) | Text contrast | WCAG 2.2 SC 1.4.3 Contrast (Minimum) (AA) | Accessibility (WCAG) - measurement | Fail | DEF-009 |
| [TC-A11Y-005](#tc-a11y-005---form-labels-associated-with-fields) | Form labels associated with fields | WCAG 2.2 SC 1.3.1 (A) and 4.1.2 Name, Role, Value (A) | Accessibility (WCAG) - inspection | Fail | DEF-007 |
| [TC-A11Y-006](#tc-a11y-006---filter-and-search-labels) | Filter and search labels | WCAG 2.2 SC 3.3.2 Labels or Instructions (A) | Accessibility (WCAG) - inspection | Fail | DEF-007 |
| [TC-A11Y-007](#tc-a11y-007---complete-and-reopen-button-name-and-state) | Complete and reopen button name and state | WCAG 2.2 SC 4.1.2 Name, Role, Value (A) | Accessibility (WCAG) - inspection | Fail | DEF-008 |
| [TC-A11Y-008](#tc-a11y-008---keyboard-operation) | Keyboard operation | WCAG 2.2 SC 2.1.1 Keyboard (A), 2.1.2 No Keyboard Trap (A) | Accessibility (WCAG) - keyboard | Pass | - |
| [TC-A11Y-009](#tc-a11y-009---bypass-the-navigation-bar) | Bypass the navigation bar | WCAG 2.2 SC 2.4.1 Bypass Blocks (A) | Accessibility (WCAG) - keyboard and inspection | Fail | DEF-010 |
| [TC-A11Y-010](#tc-a11y-010---page-titles) | Page titles | WCAG 2.2 SC 2.4.2 Page Titled (A) | Accessibility (WCAG) - inspection | Pass | - |
| [TC-A11Y-011](#tc-a11y-011---focus-order-and-visible-focus) | Focus order and visible focus | WCAG 2.2 SC 2.4.3 Focus Order (A), 2.4.7 Focus Visible (AA) | Accessibility (WCAG) - keyboard | Pass | - |
| [TC-A11Y-012](#tc-a11y-012---reflow-at-320-css-pixels) | Reflow at 320 CSS pixels | WCAG 2.2 SC 1.4.10 Reflow (AA) | Accessibility (WCAG) - viewport | Fail | DEF-004 |
| [TC-A11Y-013](#tc-a11y-013---text-resize-to-200) | Text resize to 200% | WCAG 2.2 SC 1.4.4 Resize Text (AA) | Accessibility (WCAG) - zoom | Pass | - |
| [TC-A11Y-014](#tc-a11y-014---language-of-page) | Language of page | WCAG 2.2 SC 3.1.1 Language of Page (A) | Accessibility (WCAG) - inspection | Pass | - |
| [TC-A11Y-015](#tc-a11y-015---error-identification-and-announcement) | Error identification and announcement | WCAG 2.2 SC 3.3.1 Error Identification (A), 4.1.3 Status Messages (AA) | Accessibility (WCAG) - inspection | Fail | DEF-011 |
| [TC-A11Y-016](#tc-a11y-016---target-size) | Target size | WCAG 2.2 SC 2.5.8 Target Size (Minimum) (AA) | Accessibility (WCAG) - measurement | Fail | DEF-012 |
| [TC-A11Y-017](#tc-a11y-017---descriptive-headings-and-labels) | Descriptive headings and labels | WCAG 2.2 SC 2.4.6 Headings and Labels (AA) | Accessibility (WCAG) - review | Fail | DEF-013 |
| [TC-A11Y-018](#tc-a11y-018---automated-scan-summary) | Automated scan summary | WCAG 2.2 A/AA subset | Accessibility (WCAG) - automated scan | Pass | - |

### 2.4 Week 4 - Web and API (Appendix D)

| Case ID | Title | Requirement | Technique | Status | Defect |
| --- | --- | --- | --- | --- | --- |
| [TC-WEB-001](#tc-web-001---register-through-the-web-form) | Register through the web form | REQ-001 | Workflow / web | Pass | - |
| [TC-WEB-002](#tc-web-002---registration-validated-on-the-server) | Registration validated on the server | REQ-001 | Client-server validation / EP | Pass | - |
| [TC-WEB-003](#tc-web-003---login-through-the-web-form) | Login through the web form | REQ-002 | Decision table / web | Pass | - |
| [TC-WEB-004](#tc-web-004---protected-pages-redirect-when-logged-out) | Protected pages redirect when logged out | REQ-002 | EP (unauthenticated) / web | Pass | - |
| [TC-WEB-005](#tc-web-005---web-created-task-matches-the-api) | Web-created task matches the API | REQ-003 | Workflow / UI vs API comparison | Pass | - |
| [TC-WEB-006](#tc-web-006---api-created-task-matches-the-web-list) | API-created task matches the web list | REQ-003 / REQ-006 | Workflow / API vs UI comparison | Pass | - |
| [TC-WEB-007](#tc-web-007---web-edit-matches-the-api) | Web edit matches the API | REQ-003 | Workflow / UI vs API comparison | Pass | - |
| [TC-WEB-008](#tc-web-008---web-toggle-matches-the-api) | Web toggle matches the API | REQ-004 | State transition / UI vs API comparison | Pass | - |
| [TC-WEB-009](#tc-web-009---web-delete-matches-the-api) | Web delete matches the API | REQ-003 | Workflow / UI vs API comparison | Pass | - |
| [TC-WEB-010](#tc-web-010---blank-title-validated-on-the-server) | Blank title validated on the server | REQ-003 | Client-server validation / EP | Fail | DEF-003 |
| [TC-WEB-011](#tc-web-011---due-date-validated-on-the-server) | Due date validated on the server | REQ-003 / REQ-006 | Client-server validation / EP | Fail | DEF-015 |
| [TC-WEB-012](#tc-web-012---category-validated-on-the-server) | Category validated on the server | REQ-003 | Client-server validation / EP | Fail | DEF-019 |
| [TC-WEB-013](#tc-web-013---web-actions-on-another-users-task) | Web actions on another user's task | REQ-008 | EP (foreign id) / UI vs API comparison | Pass | - |
| [TC-WEB-014](#tc-web-014---web-dashboard-matches-the-api-dashboard) | Web dashboard matches the API dashboard | REQ-007 | UI vs API comparison | Pass | - |
| [TC-WEB-015](#tc-web-015---web-search-with-an-apostrophe) | Web search with an apostrophe | REQ-005 | EP (special character) / UI vs API comparison | Pass | - |
| [TC-WEB-016](#tc-web-016---duplicate-username-on-the-web-form) | Duplicate username on the web form | REQ-001 | EP / web negative | Fail | DEF-016 |
| [TC-API-001](#tc-api-001---register-a-valid-account) | Register a valid account | REQ-001 | EP / API functional | Pass | - |
| [TC-API-002](#tc-api-002---username-valid-length-boundaries-3-20) | Username valid length boundaries (3, 20) | REQ-001 | BVA / API | Pass | - |
| [TC-API-003](#tc-api-003---invalid-username-partitions) | Invalid username partitions | REQ-001 | EP + BVA / API negative | Pass | - |
| [TC-API-004](#tc-api-004---password-length-7-rejected) | Password length 7 rejected | REQ-001 | BVA / API negative | Pass | - |
| [TC-API-005](#tc-api-005---password-length-8-accepted) | Password length 8 accepted | REQ-001 | BVA / API | Fail | DEF-001 |
| [TC-API-006](#tc-api-006---missing-password-rejected) | Missing password rejected | REQ-001 | EP / API negative | Pass | - |
| [TC-API-007](#tc-api-007---username-of-the-wrong-json-type) | Username of the wrong JSON type | REQ-001 / REQ-009 | EP (data type) / API negative | Fail | DEF-018 |
| [TC-API-008](#tc-api-008---duplicate-username-rejected) | Duplicate username rejected | REQ-001 | EP / API negative | Fail | DEF-016 |
| [TC-API-009](#tc-api-009---login-with-valid-credentials) | Login with valid credentials | REQ-002 | Decision table (valid/valid) / API | Pass | - |
| [TC-API-010](#tc-api-010---login-with-invalid-credentials) | Login with invalid credentials | REQ-002 | Decision table / API negative | Pass | - |
| [TC-API-011](#tc-api-011---protected-endpoints-require-a-session) | Protected endpoints require a session | REQ-002 / REQ-009 | EP (unauthenticated) / API negative | Pass | - |
| [TC-API-012](#tc-api-012---categories-endpoint-requires-a-session) | Categories endpoint requires a session | REQ-009 | EP (unauthenticated) / API negative | Fail | DEF-023 |
| [TC-API-013](#tc-api-013---list-categories) | List categories | REQ-009 | API functional | Pass | - |
| [TC-API-014](#tc-api-014---create-a-task-with-all-fields) | Create a task with all fields | REQ-003 | EP (valid) / API functional | Pass | - |
| [TC-API-015](#tc-api-015---create-a-title-only-task) | Create a title-only task | REQ-003 | EP (valid, optional fields omitted) / API | Pass | - |
| [TC-API-016](#tc-api-016---title-required) | Title required | REQ-003 | EP (invalid) / API negative | Pass | - |
| [TC-API-017](#tc-api-017---non-json-request-body) | Non-JSON request body | REQ-009 | EP (invalid format) / API negative | Pass | - |
| [TC-API-018](#tc-api-018---wrong-json-types-on-create) | Wrong JSON types on create | REQ-003 / REQ-009 | EP (data type) / API negative | Fail | DEF-018 |
| [TC-API-019](#tc-api-019---invalid-due-date-on-create) | Invalid due date on create | REQ-003 / REQ-006 | EP (invalid) / API negative | Fail | DEF-015 |
| [TC-API-020](#tc-api-020---invalid-category-on-create) | Invalid category on create | REQ-003 | EP (invalid) / API negative | Fail | DEF-019 |
| [TC-API-021](#tc-api-021---urgency-boundaries-returned-by-the-api) | Urgency boundaries returned by the API | REQ-006 | BVA / API | Fail | DEF-002 |
| [TC-API-022](#tc-api-022---read-own-task) | Read own task | REQ-003 | API functional | Pass | - |
| [TC-API-023](#tc-api-023---read-a-non-existent-task) | Read a non-existent task | REQ-003 / REQ-009 | EP (invalid id) / API negative | Pass | - |
| [TC-API-024](#tc-api-024---read-another-users-task) | Read another user's task | REQ-008 | EP (foreign id) / API negative | Pass | - |
| [TC-API-025](#tc-api-025---non-integer-task-id) | Non-integer task id | REQ-009 | EP (invalid type) / API negative | Pass | - |
| [TC-API-026](#tc-api-026---filter-by-category) | Filter by category | REQ-005 | EP / API functional | Pass | - |
| [TC-API-027](#tc-api-027---filter-by-status) | Filter by status | REQ-005 | EP / API functional | Pass | - |
| [TC-API-028](#tc-api-028---title-search) | Title search | REQ-005 | EP / API functional | Pass | - |
| [TC-API-029](#tc-api-029---combined-filters) | Combined filters | REQ-005 | Decision table / API functional | Pass | - |
| [TC-API-030](#tc-api-030---search-text-containing-an-apostrophe) | Search text containing an apostrophe | REQ-005 | EP (special character) / API negative | Fail | DEF-017 |
| [TC-API-031](#tc-api-031---pagination) | Pagination | REQ-005 / REQ-009 | BVA / API functional | Pass | - |
| [TC-API-032](#tc-api-032---invalid-pagination-parameters) | Invalid pagination parameters | REQ-009 | EP + BVA (invalid) / API negative | Fail | DEF-022 |
| [TC-API-033](#tc-api-033---task-list-scoped-to-the-user) | Task list scoped to the user | REQ-008 | EP / API | Pass | - |
| [TC-API-034](#tc-api-034---partial-update) | Partial update | REQ-003 | API functional | Pass | - |
| [TC-API-035](#tc-api-035---complete-and-reopen-through-the-api) | Complete and reopen through the API | REQ-004 | State transition (Open -> Done -> Open) / API | Pass | - |
| [TC-API-036](#tc-api-036---invalid-values-on-update) | Invalid values on update | REQ-003 / REQ-009 | EP (invalid) / API negative | Fail | DEF-015, DEF-018, DEF-019, DEF-020 |
| [TC-API-037](#tc-api-037---update-another-users-task) | Update another user's task | REQ-008 | EP (foreign id) / API negative | Pass | - |
| [TC-API-038](#tc-api-038---update-a-non-existent-task) | Update a non-existent task | REQ-009 | EP (invalid id) / API negative | Pass | - |
| [TC-API-039](#tc-api-039---delete-own-task) | Delete own task | REQ-003 | State transition (exists -> deleted) / API | Pass | - |
| [TC-API-040](#tc-api-040---delete-another-users-task) | Delete another user's task | REQ-008 | EP (foreign id) / API negative | Fail | DEF-014 |
| [TC-API-041](#tc-api-041---delete-a-non-existent-task) | Delete a non-existent task | REQ-009 | EP (invalid id) / API negative | Fail | DEF-021 |
| [TC-API-042](#tc-api-042---dashboard-counts-with-a-controlled-dataset) | Dashboard counts with a controlled dataset | REQ-007 | API functional (oracle: independent count) | Pass | - |
| [TC-API-043](#tc-api-043---task-due-today-is-not-overdue-on-the-dashboard) | Task due today is not overdue on the dashboard | REQ-006 / REQ-007 | BVA / API | Fail | DEF-002 |
| [TC-API-044](#tc-api-044---dashboard-scoped-to-the-user) | Dashboard scoped to the user | REQ-008 | EP / API | Pass | - |
| [TC-API-045](#tc-api-045---unsupported-http-method) | Unsupported HTTP method | REQ-009 | EP (invalid method) / API negative | Pass | - |

### 2.5 Week 5 - Security and performance (Appendix E)

Pending. No cases merged.

### 2.6 Week 6 - Automated regression cases (Appendix F; not counted in the 177)

| Case ID | Script :: test | Manual case(s) covered | Requirement | Checks | Status | Defect |
| --- | --- | --- | --- | --- | --- | --- |
| [TC-AUT-001](#tc-aut-001) | test_01_auth :: test_username_length_boundaries | TC-BB-001, 002, 003, 004, 005, 006 | REQ-001 | 6 | Pass | - |
| [TC-AUT-002](#tc-aut-002) | test_01_auth :: test_password_length_boundaries | TC-BB-007, 008, 009; TC-GUI-004 | REQ-001 | 3 | Pass and Fail (known defect) | DEF-001 |
| [TC-AUT-003](#tc-aut-003) | test_01_auth :: test_valid_registration_opens_task_list | TC-BB-010 | REQ-001 | 1 | Pass | - |
| [TC-AUT-004](#tc-aut-004) | test_01_auth :: test_username_with_hyphen_is_rejected | TC-BB-011 | REQ-001 | 1 | Pass | - |
| [TC-AUT-005](#tc-aut-005) | test_01_auth :: test_empty_registration_field_blocked_by_browser | TC-BB-012, 013 | REQ-001 | 2 | Pass | - |
| [TC-AUT-006](#tc-aut-006) | test_01_auth :: test_login_decision_table | TC-BB-014, 015, 016, 017; TC-GUI-002 (text only) | REQ-002 | 4 | Pass | - |
| [TC-AUT-007](#tc-aut-007) | test_01_auth :: test_protected_page_redirects_when_logged_out | TC-BB-018 (extended to 3 pages) | REQ-002 | 3 | Pass | - |
| [TC-AUT-008](#tc-aut-008) | test_01_auth :: test_logout_revokes_protected_page_access | TC-BB-019 | REQ-002 | 1 | Pass | - |
| [TC-AUT-009](#tc-aut-009) | test_02_tasks :: test_create_full_field_task_persists | TC-BB-020 | REQ-003 | 1 | Pass | - |
| [TC-AUT-010](#tc-aut-010) | test_02_tasks :: test_create_title_only_task | TC-BB-021 | REQ-003 | 1 | Pass | - |
| [TC-AUT-011](#tc-aut-011) | test_02_tasks :: test_empty_title_blocked_by_browser | TC-BB-022 | REQ-003 | 1 | Pass | - |
| [TC-AUT-012](#tc-aut-012) | test_02_tasks :: test_whitespace_only_title_rejected | TC-BB-023; TC-GUI-016 | REQ-003 | 1 | Fail (known defect) | DEF-003 |
| [TC-AUT-013](#tc-aut-013) | test_02_tasks :: test_edit_persists_all_fields | TC-BB-024; TC-GUI-012, 015 | REQ-003 | 1 | Pass | - |
| [TC-AUT-014](#tc-aut-014) | test_02_tasks :: test_cancel_edit_preserves_saved_data | TC-BB-025 | REQ-003 | 1 | Pass | - |
| [TC-AUT-015](#tc-aut-015) | test_02_tasks :: test_cancel_deletion_retains_task | TC-BB-026; TC-GUI-013 | REQ-003 | 1 | Pass | - |
| [TC-AUT-016](#tc-aut-016) | test_02_tasks :: test_confirm_deletion_removes_only_that_task | TC-BB-027; TC-GUI-013 | REQ-003 | 1 | Pass | - |
| [TC-AUT-017](#tc-aut-017) | test_02_tasks :: test_complete_then_reopen_task | TC-BB-028, 029; TC-GUI-011 | REQ-004 | 1 | Pass | - |
| [TC-AUT-018](#tc-aut-018) | test_02_tasks :: test_special_characters_preserved_in_edit_form | TC-GUI-020 (edit form) | REQ-003 | 1 | Pass | - |
| [TC-AUT-019](#tc-aut-019) | test_02_tasks :: test_special_characters_displayed_literally_in_list | TC-GUI-020 (list) | REQ-003 | 1 | Fail (known defect) | DEF-005 |
| [TC-AUT-020](#tc-aut-020) | test_02_tasks :: test_each_account_sees_only_its_own_tasks | TC-BB-044 | REQ-008 | 1 | Pass | - |
| [TC-AUT-021](#tc-aut-021) | test_03_filters :: test_filters_return_only_matching_tasks | TC-BB-030, 031, 032, 033, 034, 035; TC-GUI-008 | REQ-005 | 6 | Pass | - |
| [TC-AUT-022](#tc-aut-022) | test_04_urgency_dashboard :: test_urgency_label | TC-BB-036, 037, 038, 039, 040, 041; TC-GUI-010 | REQ-006 | 6 | Pass and Fail (known defect) | DEF-002 |
| [TC-AUT-023](#tc-aut-023) | test_04_urgency_dashboard :: test_completion_overrides_overdue | TC-BB-042 | REQ-004, REQ-006 | 1 | Pass | - |
| [TC-AUT-024](#tc-aut-024) | test_04_urgency_dashboard :: test_dashboard_counters_unaffected_by_def002 | TC-BB-043 (Total, Open, Due Soon, Completed) | REQ-007 | 1 | Pass | - |
| [TC-AUT-025](#tc-aut-025) | test_04_urgency_dashboard :: test_dashboard_overdue_counter | TC-BB-043 (Overdue) | REQ-007 | 1 | Fail (known defect) | DEF-002 |
| [TC-AUT-026](#tc-aut-026) | test_05_rules_unit :: test_username_rule | TC-BB-001 to 006, 010, 011 | REQ-001 | 8 | Pass | - |
| [TC-AUT-027](#tc-aut-027) | test_05_rules_unit :: test_password_rule | TC-BB-007, 008, 009 | REQ-001 | 3 | Pass and Fail (known defect) | DEF-001 |
| [TC-AUT-028](#tc-aut-028) | test_05_rules_unit :: test_urgency_rule | TC-BB-036 to 041 | REQ-006 | 6 | Pass and Fail (known defect) | DEF-002 |

Counts by status (177 designed cases, W1-W4): **Pass 130, Fail 42, Blocked 0, Not Run 5** (the five Not Run are TC-USA-001 to 005).

---

# Appendix A - Week 1 black-box cases (verbatim)

Source: `01_Black_Box/test_cases.md`, commit `TBD`. Everything below is copied unchanged from the first case heading onward. Evidence filenames refer to `01_Black_Box/evidences/`.

## TC-BB-001 - Username length 2

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-001 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Reject a 2-character username. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "dq", "usernameLength": 2, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified username and password.<br>3. Select Register.<br>4. Observe validation or the authenticated task page. |
| Expected Result | Reject a 2-character username. |
| Actual Result | Registration did not proceed. Username must be 3-20 characters (letters, numbers, underscore). |
| Status | Pass |
| Evidence | TC-BB-001.jpg |
| Defect ID | — |

## TC-BB-002 - Username length 3

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-002 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Accept a 3-character username. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "d7r", "usernameLength": 3, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified username and password.<br>3. Select Register.<br>4. Observe validation or the authenticated task page. |
| Expected Result | Accept a 3-character username. |
| Actual Result | Account created; authenticated My Tasks displays d7r. |
| Status | Pass |
| Evidence | TC-BB-002.jpg |
| Defect ID | — |

## TC-BB-003 - Username length 4

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-003 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Accept a 4-character username. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "d6qz", "usernameLength": 4, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified username and password.<br>3. Select Register.<br>4. Observe validation or the authenticated task page. |
| Expected Result | Accept a 4-character username. |
| Actual Result | Account created; authenticated My Tasks page displays d6qz. |
| Status | Pass |
| Evidence | TC-BB-003.jpg |
| Defect ID | — |

## TC-BB-004 - Username length 19

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-004 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Accept a 19-character username. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "daaaaaaaaaaaaaaaaaa", "usernameLength": 19, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified username and password.<br>3. Select Register.<br>4. Observe validation or the authenticated task page. |
| Expected Result | Accept a 19-character username. |
| Actual Result | Account created; authenticated My Tasks page displays daaaaaaaaaaaaaaaaaa. |
| Status | Pass |
| Evidence | TC-BB-004.jpg |
| Defect ID | — |

## TC-BB-005 - Username length 20

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-005 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Accept a 20-character username. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "daaaaaaaaaaaaaaaaaaa", "usernameLength": 20, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified username and password.<br>3. Select Register.<br>4. Observe validation or the authenticated task page. |
| Expected Result | Accept a 20-character username. |
| Actual Result | Account created; authenticated My Tasks page displays daaaaaaaaaaaaaaaaaaa. |
| Status | Pass |
| Evidence | TC-BB-005.jpg |
| Defect ID | — |

## TC-BB-006 - Username length 21

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-006 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Reject a 21-character username. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "daaaaaaaaaaaaaaaaaaaa", "usernameLength": 21, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified username and password.<br>3. Select Register.<br>4. Observe validation or the authenticated task page. |
| Expected Result | Reject a 21-character username. |
| Actual Result | Registration did not proceed. Username must be 3-20 characters (letters, numbers, underscore). |
| Status | Pass |
| Evidence | TC-BB-006.jpg |
| Defect ID | — |

## TC-BB-007 - Password length 7

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-007 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Reject a 7-character password. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "w1d_p7_2315", "usernameLength": 11, "password": "Test123", "passwordLength": 7} |
| Steps | 1. Open `/register` and note the minimum-eight-character hint.<br>2. Enter the specified data.<br>3. Select Register.<br>4. Observe rejection or successful account creation. |
| Expected Result | Reject a 7-character password. |
| Actual Result | Registration rejected: Password must be at least 8 characters. |
| Status | Pass |
| Evidence | TC-BB-007.jpg |
| Defect ID | — |

## TC-BB-008 - Password length 8

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-008 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Accept an 8-character password, matching the displayed minimum. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "w1d_p8_2315", "usernameLength": 11, "password": "Test1234", "passwordLength": 8} |
| Steps | 1. Open `/register` and note the minimum-eight-character hint.<br>2. Enter the specified data.<br>3. Select Register.<br>4. Observe rejection or successful account creation. |
| Expected Result | Accept an 8-character password, matching the displayed minimum. |
| Actual Result | Registration rejected: Password must be at least 8 characters. |
| Status | Fail |
| Evidence | TC-BB-008.jpg |
| Defect ID | DEF-001 |

## TC-BB-009 - Password length 9

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-009 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / Functional |
| Objective | Accept a 9-character password. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "w1d_p9b_2315", "usernameLength": 12, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register` and note the minimum-eight-character hint.<br>2. Enter the specified data.<br>3. Select Register.<br>4. Observe rejection or successful account creation. |
| Expected Result | Accept a 9-character password. |
| Actual Result | Account created; authenticated My Tasks displays w1d_p9b_2315. |
| Status | Pass |
| Evidence | TC-BB-009.jpg |
| Defect ID | — |

## TC-BB-010 - Valid registration

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-010 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / Functional |
| Objective | Create a valid account and display its authenticated task list. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "w1d_a_2315", "usernameLength": 10, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified data.<br>3. Select Register.<br>4. Observe the response or native validation popup. |
| Expected Result | Create a valid account and display its authenticated task list. |
| Actual Result | Account created; authenticated My Tasks page displays w1d_a_2315. |
| Status | Pass |
| Evidence | TC-BB-010.jpg |
| Defect ID | — |

## TC-BB-011 - Disallowed username character

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-011 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / Functional |
| Objective | Reject a username containing a hyphen. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "w1-d", "usernameLength": 4, "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified data.<br>3. Select Register.<br>4. Observe the response or native validation popup. |
| Expected Result | Reject a username containing a hyphen. |
| Actual Result | Registration did not proceed. Username must be 3-20 characters (letters, numbers, underscore). |
| Status | Pass |
| Evidence | TC-BB-011.jpg |
| Defect ID | — |

## TC-BB-012 - Empty registration username

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-012 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / Functional / Browser validation |
| Objective | Browser validation prevents submission with an empty username. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "", "password": "Test12345", "passwordLength": 9} |
| Steps | 1. Open `/register`.<br>2. Enter the specified data.<br>3. Select Register.<br>4. Observe the response or native validation popup. |
| Expected Result | Browser validation prevents submission with an empty username. |
| Actual Result | Native browser validation displays “Please fill in this field”; registration does not proceed. |
| Status | Pass |
| Evidence | TC-BB-012.jpg |
| Defect ID | — |

## TC-BB-013 - Empty registration password

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-013 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / Functional / Browser validation |
| Objective | Browser validation prevents submission with an empty password. |
| Preconditions | Live development instance; logged out. Use the username and password listed in Test Data. No database reset is performed. |
| Test Data | {"username": "w1d_empty_2315", "password": "", "passwordLength": 0} |
| Steps | 1. Open `/register`.<br>2. Enter the specified data.<br>3. Select Register.<br>4. Observe the response or native validation popup. |
| Expected Result | Browser validation prevents submission with an empty password. |
| Actual Result | Native browser validation displays “Please fill in this field”; registration does not proceed. |
| Status | Pass |
| Evidence | TC-BB-013.jpg |
| Defect ID | — |

## TC-BB-014 - Login credential decision rule 1

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-014 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Decision table / Functional |
| Objective | Valid credentials allow authenticated task access. |
| Preconditions | Account A (`w1d_a_2315`) is registered with synthetic password Test12345; unknown username does not belong to the baseline account. Logout/login state is set by the numbered steps. |
| Test Data | {"username": "w1d_a_2315", "password": "Test12345"} |
| Steps | 1. Open `/login`.<br>2. Enter the specified credentials.<br>3. Select Log in.<br>4. Observe authenticated access or rejection. |
| Expected Result | Valid credentials allow authenticated task access. |
| Actual Result | Authenticated My Tasks page displays w1d_a_2315. |
| Status | Pass |
| Evidence | TC-BB-014.jpg |
| Defect ID | — |

## TC-BB-015 - Login credential decision rule 2

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-015 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Decision table / Functional |
| Objective | Invalid credential combination is rejected. |
| Preconditions | Account A (`w1d_a_2315`) is registered with synthetic password Test12345; unknown username does not belong to the baseline account. Logout/login state is set by the numbered steps. |
| Test Data | {"username": "w1d_a_2315", "password": "Wrong12345"} |
| Steps | 1. Open `/login`.<br>2. Enter the specified credentials.<br>3. Select Log in.<br>4. Observe authenticated access or rejection. |
| Expected Result | Invalid credential combination is rejected. |
| Actual Result | Login rejected with Invalid username or password. |
| Status | Pass |
| Evidence | TC-BB-015.jpg |
| Defect ID | — |

## TC-BB-016 - Login credential decision rule 3

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-016 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Decision table / Functional |
| Objective | Invalid credential combination is rejected. |
| Preconditions | Account A (`w1d_a_2315`) is registered with synthetic password Test12345; unknown username does not belong to the baseline account. Logout/login state is set by the numbered steps. |
| Test Data | {"username": "w1d_unknown_2315", "password": "Test12345"} |
| Steps | 1. Open `/login`.<br>2. Enter the specified credentials.<br>3. Select Log in.<br>4. Observe authenticated access or rejection. |
| Expected Result | Invalid credential combination is rejected. |
| Actual Result | Login rejected with Invalid username or password. |
| Status | Pass |
| Evidence | TC-BB-016.jpg |
| Defect ID | — |

## TC-BB-017 - Login credential decision rule 4

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-017 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Decision table / Functional |
| Objective | Invalid credential combination is rejected. |
| Preconditions | Account A (`w1d_a_2315`) is registered with synthetic password Test12345; unknown username does not belong to the baseline account. Logout/login state is set by the numbered steps. |
| Test Data | {"username": "w1d_unknown_2315", "password": "Wrong12345"} |
| Steps | 1. Open `/login`.<br>2. Enter the specified credentials.<br>3. Select Log in.<br>4. Observe authenticated access or rejection. |
| Expected Result | Invalid credential combination is rejected. |
| Actual Result | Login rejected with Invalid username or password. |
| Status | Pass |
| Evidence | TC-BB-017.jpg |
| Defect ID | — |

## TC-BB-018 - Protected page while logged out

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-018 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | State transition / Functional |
| Objective | Unauthenticated visit to / redirects to /login. |
| Preconditions | Logged out; no authenticated session is active. |
| Test Data | {} |
| Steps | 1. Navigate directly to `/`.<br>2. Observe final URL and page. |
| Expected Result | Unauthenticated visit to / redirects to /login. |
| Actual Result | Protected task URL redirected to http://127.0.0.1:5000/login. |
| Status | Pass |
| Evidence | TC-BB-018.jpg |
| Defect ID | — |

## TC-BB-019 - Logout revokes protected-page access

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-019 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | State transition / Functional |
| Objective | After logout, directly requesting / requires login. |
| Preconditions | Account A (`w1d_a_2315`) is registered with synthetic password Test12345; unknown username does not belong to the baseline account. Logout/login state is set by the numbered steps. |
| Test Data | {"username": "w1d_a_2315"} |
| Steps | 1. Log in as Account A (`w1d_a_2315`).<br>2. Select Log out.<br>3. Navigate directly to `/`.<br>4. Observe final URL and login page. |
| Expected Result | After logout, directly requesting / requires login. |
| Actual Result | After Log out, / redirected to http://127.0.0.1:5000/login. |
| Status | Pass |
| Evidence | TC-BB-019.jpg |
| Defect ID | — |

## TC-BB-020 - Create and persist a full-field task

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-020 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP / Functional |
| Objective | Create a full-field task and retain all submitted values on reopening Edit. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"title": "BB-CRUD-Original", "description": "Week 1 full-field task", "category": "Work", "dueDate": "2026-10-21"} |
| Steps | 1. Select + New Task.<br>2. Fill all fields with the specified data.<br>3. Select Create Task.<br>4. Check title, category, date and urgency in the list.<br>5. Open Edit and verify that all four fields were retained. |
| Expected Result | Create a full-field task and retain all submitted values on reopening Edit. |
| Actual Result | Reopened Edit contains BB-CRUD-Original, Week 1 full-field task, Work and 2026-10-21. |
| Status | Pass |
| Evidence | TC-BB-020.jpg |
| Defect ID | — |

## TC-BB-021 - Create a title-only task

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-021 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP / Functional |
| Objective | Create title-only task with optional fields empty. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"title": "BB-MINIMAL"} |
| Steps | 1. Open + New Task.<br>2. Enter only the specified title.<br>3. Select Create Task.<br>4. Check the new row and its optional-field display. |
| Expected Result | Create title-only task with optional fields empty. |
| Actual Result | BB-MINIMAL is listed with no category/date and No due date classification. |
| Status | Pass |
| Evidence | TC-BB-021.jpg |
| Defect ID | — |

## TC-BB-022 - Empty title browser validation

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-022 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP / Browser validation |
| Objective | Browser required-field validation prevents an empty task title. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"title": ""} |
| Steps | 1. Leave Title empty.<br>2. Select Create Task.<br>3. Observe required-field popup and whether navigation occurs. |
| Expected Result | Browser required-field validation prevents an empty task title. |
| Actual Result | Native required-field message appears at Title; the New Task form remains. |
| Status | Pass |
| Evidence | TC-BB-022.jpg |
| Defect ID | — |

## TC-BB-023 - Reject a whitespace-only title

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-023 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP / Functional / Input validation |
| Objective | Verify that a title containing only whitespace is rejected and the user is prompted to enter a valid title. |
| Preconditions | Logged in as Account A (`w1d_a_2315`); the New Task form is available. |
| Test Data | {"title": "   "} |
| Steps | 1. Open + New Task.<br>2. Enter three spaces (`"   "`) in Title.<br>3. Select Create Task.<br>4. Check for validation asking for a valid title and verify that no task with a blank title is created. |
| Expected Result | Reject the whitespace-only title, display a validation message asking the user to enter a valid title, and do not create a task. |
| Actual Result | Submitting three spaces creates a task row with an empty displayed title instead of rejecting the input and asking for a valid title. |
| Status | Fail |
| Evidence | TC-BB-023.jpg |
| Defect ID | DEF-003 |

## TC-BB-024 - Edit and persist all task fields

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-024 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Functional |
| Objective | All edited task fields persist after saving and reopening. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"title": "BB-CRUD-Edited", "description": "Week 1 edited description", "category": "Study", "dueDate": "2026-10-20"} |
| Steps | 1. Open Edit for BB-CRUD-Original.<br>2. Replace all four fields with the specified values.<br>3. Select Save Changes.<br>4. Reopen Edit and compare all saved fields. |
| Expected Result | All edited task fields persist after saving and reopening. |
| Actual Result | Reopened Edit retains BB-CRUD-Edited, Week 1 edited description, Study and 2026-10-20. |
| Status | Pass |
| Evidence | TC-BB-024.jpg |
| Defect ID | — |

## TC-BB-025 - Cancel edit preserves saved data

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-025 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | State transition / Functional |
| Objective | Cancelling edit preserves previously saved data. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"draftTitle": "BB-UNSAVED", "draftDescription": "Unsaved draft"} |
| Steps | 1. Open Edit for BB-CRUD-Edited.<br>2. Enter the unsaved title and description.<br>3. Select Cancel.<br>4. Reopen Edit.<br>5. Verify the previously saved title/description remain. |
| Expected Result | Cancelling edit preserves previously saved data. |
| Actual Result | Saved BB-CRUD-Edited and Week 1 edited description remain; unsaved draft values are absent. |
| Status | Pass |
| Evidence | TC-BB-025.jpg |
| Defect ID | — |

## TC-BB-026 - Cancel deletion retains task

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-026 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | State transition / Functional |
| Objective | Cancel deletion retains BB-MINIMAL. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"task": "BB-MINIMAL", "dialog": "confirm", "action": "Cancel"} |
| Steps | 1. Locate BB-MINIMAL.<br>2. Select Delete.<br>3. Observe the native Chrome confirmation.<br>4. Select Cancel.<br>5. Verify BB-MINIMAL remains. |
| Expected Result | Cancel deletion retains BB-MINIMAL. |
| Actual Result | Native Chrome Cancel dismissed the confirmation; BB-MINIMAL remains in the task list. |
| Status | Pass |
| Evidence | TC-BB-026.jpg |
| Defect ID | — |

## TC-BB-027 - Confirm deletion and verify persistence

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-027 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | State transition / Functional |
| Objective | Confirm deletion removes BB-MINIMAL and it stays absent after refresh. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"task": "BB-MINIMAL", "dialog": "confirm", "action": "OK"} |
| Steps | 1. Locate BB-MINIMAL retained by TC-BB-026.<br>2. Select Delete.<br>3. Observe the native Chrome confirmation.<br>4. Select OK.<br>5. Refresh and verify the task remains absent. |
| Expected Result | Confirm deletion removes BB-MINIMAL and it stays absent after refresh. |
| Actual Result | Native Chrome OK accepted deletion; BB-MINIMAL is absent after refresh. |
| Status | Pass |
| Evidence | TC-BB-027.jpg |
| Defect ID | — |

## TC-BB-028 - Complete an Open task

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-028 |
| Feature/Requirement | REQ-004 |
| Technique/Test Type | State transition / Functional |
| Objective | Completing an Open task changes it to Done. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"task": "BB-CRUD-Edited"} |
| Steps | 1. Locate the task in My Tasks.<br>2. Select its open-circle completion control.<br>3. Observe checked control and Done classification. |
| Expected Result | Completing an Open task changes it to Done. |
| Actual Result | BB-CRUD-Edited displays checked control and Done. |
| Status | Pass |
| Evidence | TC-BB-028.jpg |
| Defect ID | — |

## TC-BB-029 - Reopen a Done task

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-029 |
| Feature/Requirement | REQ-004 |
| Technique/Test Type | State transition / Functional |
| Objective | Reopening a Done task restores Open state and due-date urgency. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). Execute in case order: original task from 020, minimal task from 021, edited task from 024. TC-BB-026 retains BB-MINIMAL; TC-BB-027 deletes only that synthetic task. |
| Test Data | {"task": "BB-CRUD-Edited", "dueDate": "2026-10-20"} |
| Steps | 1. Select the checked completion control.<br>2. Observe Open state.<br>3. Verify Due Soon classification is restored. |
| Expected Result | Reopening a Done task restores Open state and due-date urgency. |
| Actual Result | BB-CRUD-Edited displays open control and Due Soon for 2026-10-20. |
| Status | Pass |
| Evidence | TC-BB-029.jpg |
| Defect ID | — |

## TC-BB-030 - Filter by category

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-030 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / Functional |
| Objective | Work category returns exactly three Work fixtures. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). F1-F4 filter fixtures exist, alongside the edited task and blank-title observation row. BB-MINIMAL has been deleted by TC-BB-027. |
| Test Data | {"category": "Work"} |
| Steps | 1. Start at `/` with filters cleared.<br>2. Choose Work in Category.<br>3. Compare all displayed rows with the three Work fixtures. |
| Expected Result | Work category returns exactly three Work fixtures. |
| Actual Result | Work-filter rows: ○ BB-OTHER-WORK-OPEN Work — No due date Edit Delete \| ✓ BB-MATCH-WORK-DONE Work — Done Edit Delete \| ○ BB-MATCH-WORK-OPEN Work — No due date Edit Delete |
| Status | Pass |
| Evidence | TC-BB-030.jpg |
| Defect ID | — |

## TC-BB-031 - Filter Open tasks

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-031 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / Functional |
| Objective | Open status returns five Open tasks and excludes the Done fixture. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). F1-F4 filter fixtures exist, alongside the edited task and blank-title observation row. BB-MINIMAL has been deleted by TC-BB-027. |
| Test Data | {"status": "open"} |
| Steps | 1. Start at `/` with filters cleared.<br>2. Choose Open in Status.<br>3. Verify five Open rows and absence of the Done fixture. |
| Expected Result | Open status returns five Open tasks and excludes the Done fixture. |
| Actual Result | Open filter displays 5 rows; completed fixture absent: true. |
| Status | Pass |
| Evidence | TC-BB-031.jpg |
| Defect ID | — |

## TC-BB-032 - Filter Done tasks

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-032 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / Functional |
| Objective | Done status returns only BB-MATCH-WORK-DONE. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). F1-F4 filter fixtures exist, alongside the edited task and blank-title observation row. BB-MINIMAL has been deleted by TC-BB-027. |
| Test Data | {"status": "done"} |
| Steps | 1. Start at `/` with filters cleared.<br>2. Choose Done in Status.<br>3. Verify only BB-MATCH-WORK-DONE is displayed. |
| Expected Result | Done status returns only BB-MATCH-WORK-DONE. |
| Actual Result | Done-filter rows: ✓ BB-MATCH-WORK-DONE Work — Done Edit Delete |
| Status | Pass |
| Evidence | TC-BB-032.jpg |
| Defect ID | — |

## TC-BB-033 - Matching title search

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-033 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / Functional |
| Objective | MATCH search returns the three matching fixtures. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). F1-F4 filter fixtures exist, alongside the edited task and blank-title observation row. BB-MINIMAL has been deleted by TC-BB-027. |
| Test Data | {"query": "MATCH"} |
| Steps | 1. Start at `/` with filters cleared.<br>2. Enter MATCH in Search title.<br>3. Select Filter.<br>4. Verify exactly the three BB-MATCH fixture tasks are displayed. |
| Expected Result | MATCH search returns the three matching fixtures. |
| Actual Result | MATCH search displays 3 rows. |
| Status | Pass |
| Evidence | TC-BB-033.jpg |
| Defect ID | — |

## TC-BB-034 - Nonmatching title search

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-034 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / Functional |
| Objective | Unknown query returns the empty-results message. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). F1-F4 filter fixtures exist, alongside the edited task and blank-title observation row. BB-MINIMAL has been deleted by TC-BB-027. |
| Test Data | {"query": "NO-SUCH-TITLE-881"} |
| Steps | 1. Start at `/` with filters cleared.<br>2. Enter the absent search term.<br>3. Select Filter.<br>4. Observe the empty-results message. |
| Expected Result | Unknown query returns the empty-results message. |
| Actual Result | Search NO-SUCH-TITLE-881 displays No tasks match your filters. |
| Status | Pass |
| Evidence | TC-BB-034.jpg |
| Defect ID | — |

## TC-BB-035 - Combined filters: all conditions required

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-035 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | Decision table / Functional |
| Objective | Work + Open + MATCH returns only BB-MATCH-WORK-OPEN. |
| Preconditions | Logged in as Account A (`w1d_a_2315`). F1-F4 filter fixtures exist, alongside the edited task and blank-title observation row. BB-MINIMAL has been deleted by TC-BB-027. |
| Test Data | {"category": "Work", "status": "Open", "query": "MATCH"} |
| Steps | 1. Start at `/` with filters cleared.<br>2. Choose Work, then Open.<br>3. Enter MATCH and select Filter.<br>4. Verify only F1 is present; F2-F4 are absent. |
| Expected Result | Work + Open + MATCH returns only BB-MATCH-WORK-OPEN. |
| Actual Result | Combined-filter rows: ○ BB-MATCH-WORK-OPEN Work — No due date Edit Delete |
| Status | Pass |
| Evidence | TC-BB-035.jpg |
| Defect ID | — |

## TC-BB-036 - Urgency: BB-NO-DATE

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-036 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | EP / Functional |
| Objective | Open task BB-NO-DATE due (none) displays No due date. |
| Preconditions | Logged in as the dedicated dashboard account. D = 2026-10-18 (UTC+08:00). Date cases create the seven-task dataset in order. |
| Test Data | {"title": "BB-NO-DATE", "category": "Study", "dueDate": "", "serverDate": "2026-10-18"} |
| Steps | 1. Open + New Task.<br>2. Create the specified task.<br>3. Locate that task in My Tasks.<br>4. Compare its visible urgency with No due date. |
| Expected Result | Open task BB-NO-DATE due (none) displays No due date. |
| Actual Result | BB-NO-DATE displays No due date for no due date. |
| Status | Pass |
| Evidence | TC-BB-036.jpg |
| Defect ID | — |

## TC-BB-037 - Urgency: BB-YESTERDAY

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-037 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | BVA / Functional |
| Objective | Open task BB-YESTERDAY due 2026-10-17 displays Overdue. |
| Preconditions | Logged in as the dedicated dashboard account. D = 2026-10-18 (UTC+08:00). Date cases create the seven-task dataset in order. |
| Test Data | {"title": "BB-YESTERDAY", "category": "Study", "dueDate": "2026-10-17", "serverDate": "2026-10-18"} |
| Steps | 1. Open + New Task.<br>2. Create the specified task.<br>3. Locate that task in My Tasks.<br>4. Compare its visible urgency with Overdue. |
| Expected Result | Open task BB-YESTERDAY due 2026-10-17 displays Overdue. |
| Actual Result | BB-YESTERDAY displays Overdue for 2026-10-17. |
| Status | Pass |
| Evidence | TC-BB-037.jpg |
| Defect ID | — |

## TC-BB-038 - Urgency: BB-TODAY

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-038 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | BVA / Functional |
| Objective | Open task BB-TODAY due 2026-10-18 displays Due Today. |
| Preconditions | Logged in as the dedicated dashboard account. D = 2026-10-18 (UTC+08:00). Date cases create the seven-task dataset in order. |
| Test Data | {"title": "BB-TODAY", "category": "Study", "dueDate": "2026-10-18", "serverDate": "2026-10-18"} |
| Steps | 1. Open + New Task.<br>2. Create the specified task.<br>3. Locate that task in My Tasks.<br>4. Compare its visible urgency with Due Today. |
| Expected Result | Open task BB-TODAY due 2026-10-18 displays Due Today. |
| Actual Result | BB-TODAY displays Overdue for 2026-10-18. |
| Status | Fail |
| Evidence | TC-BB-038.jpg |
| Defect ID | DEF-002 |

## TC-BB-039 - Urgency: BB-TOMORROW

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-039 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | BVA / Functional |
| Objective | Open task BB-TOMORROW due 2026-10-19 displays Due Soon. |
| Preconditions | Logged in as the dedicated dashboard account. D = 2026-10-18 (UTC+08:00). Date cases create the seven-task dataset in order. |
| Test Data | {"title": "BB-TOMORROW", "category": "Study", "dueDate": "2026-10-19", "serverDate": "2026-10-18"} |
| Steps | 1. Open + New Task.<br>2. Create the specified task.<br>3. Locate that task in My Tasks.<br>4. Compare its visible urgency with Due Soon. |
| Expected Result | Open task BB-TOMORROW due 2026-10-19 displays Due Soon. |
| Actual Result | BB-TOMORROW displays Due Soon for 2026-10-19. |
| Status | Pass |
| Evidence | TC-BB-039.jpg |
| Defect ID | — |

## TC-BB-040 - Urgency: BB-PLUS-TWO

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-040 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | BVA / Functional |
| Objective | Open task BB-PLUS-TWO due 2026-10-20 displays Due Soon. |
| Preconditions | Logged in as the dedicated dashboard account. D = 2026-10-18 (UTC+08:00). Date cases create the seven-task dataset in order. |
| Test Data | {"title": "BB-PLUS-TWO", "category": "Study", "dueDate": "2026-10-20", "serverDate": "2026-10-18"} |
| Steps | 1. Open + New Task.<br>2. Create the specified task.<br>3. Locate that task in My Tasks.<br>4. Compare its visible urgency with Due Soon. |
| Expected Result | Open task BB-PLUS-TWO due 2026-10-20 displays Due Soon. |
| Actual Result | BB-PLUS-TWO displays Due Soon for 2026-10-20. |
| Status | Pass |
| Evidence | TC-BB-040.jpg |
| Defect ID | — |

## TC-BB-041 - Urgency: BB-PLUS-THREE

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-041 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | BVA / Functional |
| Objective | Open task BB-PLUS-THREE due 2026-10-21 displays Upcoming. |
| Preconditions | Logged in as the dedicated dashboard account. D = 2026-10-18 (UTC+08:00). Date cases create the seven-task dataset in order. |
| Test Data | {"title": "BB-PLUS-THREE", "category": "Study", "dueDate": "2026-10-21", "serverDate": "2026-10-18"} |
| Steps | 1. Open + New Task.<br>2. Create the specified task.<br>3. Locate that task in My Tasks.<br>4. Compare its visible urgency with Upcoming. |
| Expected Result | Open task BB-PLUS-THREE due 2026-10-21 displays Upcoming. |
| Actual Result | BB-PLUS-THREE displays Upcoming for 2026-10-21. |
| Status | Pass |
| Evidence | TC-BB-041.jpg |
| Defect ID | — |

## TC-BB-042 - Completion overrides overdue urgency

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-042 |
| Feature/Requirement | REQ-004 / REQ-006 |
| Technique/Test Type | State transition / Functional |
| Objective | Completed past-due task displays Done rather than Overdue. |
| Preconditions | Logged in as the dedicated dashboard account. D = 2026-10-18 (UTC+08:00). Date cases create the seven-task dataset in order. |
| Test Data | {"title": "BB-COMPLETED", "dueDate": "2026-10-17"} |
| Steps | 1. Create the task with yesterday's due date.<br>2. Mark it Done.<br>3. Verify the checked control and Done classification. |
| Expected Result | Completed past-due task displays Done rather than Overdue. |
| Actual Result | BB-COMPLETED displays checked control and Done. |
| Status | Pass |
| Evidence | TC-BB-042.jpg |
| Defect ID | — |

## TC-BB-043 - Reconcile dashboard with controlled data

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-043 |
| Feature/Requirement | REQ-007 |
| Technique/Test Type | Functional / Independent calculation |
| Objective | Seven-task dataset gives Total 7, Open 6, Overdue 1, Due Soon 2, Completed last 7 days 1. |
| Preconditions | Logged in as the dedicated dashboard account. D = 2026-10-18 (UTC+08:00). Date cases create the seven-task dataset in order. |
| Test Data | {"expected": [7, 6, 1, 2, 1], "actual": [7, 6, 2, 2, 1], "account": "w1d_dash_2315"} |
| Steps | 1. Capture the seven-row task list.<br>2. Independently count total, Open, Overdue, Due Soon and recently completed tasks.<br>3. Open Dashboard.<br>4. Compare each counter with 7, 6, 1, 2, 1 respectively. |
| Expected Result | Seven-task dataset gives Total 7, Open 6, Overdue 1, Due Soon 2, Completed last 7 days 1. |
| Actual Result | Observed counters: 7, 6, 2, 2, 1 (Total, Open, Overdue, Due Soon, Completed). |
| Status | Fail |
| Evidence | TC-BB-043.jpg |
| Defect ID | DEF-002 |

## TC-BB-044 - Visible task-list isolation between accounts

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-BB-044 |
| Feature/Requirement | REQ-008 |
| Technique/Test Type | EP / Functional |
| Objective | Separate account B sees only its own task; A list contains only its own fixture tasks. |
| Preconditions | Account A has its own CRUD/filter fixtures. A separate account B (`w1d_b_2315`) is newly registered for the normal visible-list comparison. |
| Test Data | {"accountA": "w1d_a_2315", "accountB": "w1d_b_2315"} |
| Steps | 1. Log in as A and capture its task list.<br>2. Log out and register B.<br>3. Create BB-ACCOUNT-B-ONLY as B.<br>4. Verify B sees only its own task and no A fixture titles. |
| Expected Result | Separate account B sees only its own task; A list contains only its own fixture tasks. |
| Actual Result | Account A had its CRUD/filter fixtures; B shows only BB-ACCOUNT-B-ONLY, with no A fixture titles. |
| Status | Pass |
| Evidence | TC-BB-044.jpg |
| Defect ID | — |

---

# Appendix B - Week 2 white-box cases (normalised)

Source: `02_White_Box_Coverage/README.md`, Tables 3, 4, 6 and 6a; commit `TBD`. The W2 report gives expected results and test mappings per path but no per-case status, actual result or evidence. For these fields the recorded baseline run is used: 50 of 50 pytest instances passed on 2026-10-26, with statement coverage in `02_White_Box_Coverage/htmlcov/index.html`. The W2 author should confirm this mapping. Requirement mapping is by the Defect & Metrics Coordinator.

## TC-WB-DB01 - get_db

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-DB01 (Source ID: DB01) |
| Feature/Requirement | Supporting (no REQ) |
| Technique/Test Type | Basis-path white-box / Integration test |
| Objective | Path DB01: no connection in context -> a connection is created |
| Preconditions | Fresh application context, no `_database` connection |
| Test Data | See Preconditions |
| Steps | 1. Call get_db() |
| Expected Result | SQLite connection stored in `g`; `row_factory` is `sqlite3.Row`; named-column access works |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestDatabaseHelpers.test_get_db_creates_and_reuses_connection` (first call) |
| Defect ID | - |

## TC-WB-DB02 - get_db

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-DB02 (Source ID: DB02) |
| Feature/Requirement | Supporting (no REQ) |
| Technique/Test Type | Basis-path white-box / Integration test |
| Objective | Path DB02: existing connection is reused |
| Preconditions | Context already holds the connection from DB01 |
| Test Data | See Preconditions |
| Steps | 1. Call get_db() a second time |
| Expected Result | Same object returned (identity assertion); no replacement connection |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: Same test, second call |
| Defect ID | - |

## TC-WB-CL01 - close_connection

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-CL01 (Source ID: CL01) |
| Feature/Requirement | Supporting (no REQ) |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path CL01: existing connection is closed |
| Preconditions | Context holds a mock connection |
| Test Data | See Preconditions |
| Steps | 1. Call close_connection(None), and again with an exception argument |
| Expected Result | `close()` called exactly once; an exception argument does not prevent closure |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestCloseConnection.test_closes_existing_connection`, `test_closes_connection_when_teardown_receives_exception` |
| Defect ID | - |

## TC-WB-CL02 - close_connection

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-CL02 (Source ID: CL02) |
| Feature/Requirement | Supporting (no REQ) |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path CL02: no connection is safe |
| Preconditions | Context holds no connection |
| Test Data | See Preconditions |
| Steps | 1. Call close_connection(None) |
| Expected Result | No exception; no connection attribute introduced |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestCloseConnection.test_no_connection_is_safe` |
| Defect ID | - |

## TC-WB-IN01 - init_db

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-IN01 (Source ID: IN01) |
| Feature/Requirement | Supporting (no REQ) |
| Technique/Test Type | Basis-path white-box / Integration test |
| Objective | Path IN01: zero loop iterations |
| Preconditions | Fresh temporary DB; `DEFAULT_CATEGORIES` patched to `[]` |
| Test Data | See Preconditions |
| Steps | 1. Call init_db() |
| Expected Result | Three tables exist; category count 0; no loop entry |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestDatabaseHelpers.test_init_db_with_no_default_categories` |
| Defect ID | - |

## TC-WB-IN02 - init_db

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-IN02 (Source ID: IN02) |
| Feature/Requirement | Supporting (no REQ) |
| Technique/Test Type | Basis-path white-box / Integration test |
| Objective | Path IN02: four loop iterations (production defaults) |
| Preconditions | Fresh temporary DB; defaults Work, Personal, Study, Urgent |
| Test Data | See Preconditions |
| Steps | 1. Call init_db() |
| Expected Result | Four categories committed and readable from another connection; tables and task defaults exist |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestDatabaseHelpers.test_init_db_creates_tables_and_commits_categories` |
| Defect ID | - |

## TC-WB-RT01 - row_to_task

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-RT01 (Source ID: RT01) |
| Feature/Requirement | REQ-003, REQ-006 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path RT01: open task gets computed urgency |
| Preconditions | Record `done=0`, due `2026-10-22`; urgency mock returns `Due Soon`; category None or Study |
| Test Data | See Preconditions |
| Steps | 1. Call row_to_task(record, category) |
| Expected Result | Urgency computed once with the due date; fields mapped; done is False; input unchanged |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `test_row_to_task_converts_fields_and_selects_urgency` (done=0) |
| Defect ID | - |

## TC-WB-RT02 - row_to_task

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-RT02 (Source ID: RT02) |
| Feature/Requirement | REQ-003, REQ-004, REQ-006 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path RT02: completed task is "Done" |
| Preconditions | Record `done=1`; category None or Study |
| Test Data | See Preconditions |
| Steps | 1. Call row_to_task(record, category) |
| Expected Result | Urgency "Done"; urgency computation not called; done is True |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: Same test (done=1) |
| Defect ID | - |

## TC-WB-CN01 - get_category_name

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-CN01 (Source ID: CN01) |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path CN01: falsy category id skips the database |
| Preconditions | id is None, 0 or ""; mock database |
| Test Data | See Preconditions |
| Steps | 1. Call get_category_name(db, id) |
| Expected Result | Returns None; `database.execute` never called |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `test_missing_category_id_skips_database` (3 variants) |
| Defect ID | - |

## TC-WB-CN02 - get_category_name

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-CN02 (Source ID: CN02) |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Basis-path white-box / Integration test |
| Objective | Path CN02: known id returns the name |
| Preconditions | Seeded DB; id of `Study` |
| Test Data | See Preconditions |
| Steps | 1. Call get_category_name(db, id) |
| Expected Result | Returns exactly `Study` |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestDatabaseHelpers.test_category_lookups_find_seeded_category` |
| Defect ID | - |

## TC-WB-CN03 - get_category_name

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-CN03 (Source ID: CN03) |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Basis-path white-box / Integration test |
| Objective | Path CN03: unknown id returns None |
| Preconditions | Seeded DB; id 999999 |
| Test Data | See Preconditions |
| Steps | 1. Call get_category_name(db, 999999) |
| Expected Result | Returns None |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestDatabaseHelpers.test_category_lookups_return_none_for_missing_values` |
| Defect ID | - |

## TC-WB-CI01 - get_category_id_by_name

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-CI01 (Source ID: CI01) |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Basis-path white-box / Integration test |
| Objective | Path CI01: known name returns the id |
| Preconditions | Seeded DB; name `Study` |
| Test Data | See Preconditions |
| Steps | 1. Call get_category_id_by_name(db, "Study") |
| Expected Result | Returned id equals the independently queried id |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestDatabaseHelpers.test_category_lookups_find_seeded_category` |
| Defect ID | - |

## TC-WB-CI02 - get_category_id_by_name

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-CI02 (Source ID: CI02) |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Basis-path white-box / Integration test |
| Objective | Path CI02: unknown name returns None (parameterised query) |
| Preconditions | Names `Unknown` and `Study' OR 1=1 --` |
| Test Data | See Preconditions |
| Steps | 1. Call get_category_id_by_name(db, name) |
| Expected Result | None for both inputs |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestDatabaseHelpers.test_category_lookups_return_none_for_missing_values` |
| Defect ID | - |

## TC-WB-WF01 - login_required_web (factory)

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-WF01 (Source ID: WF01) |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path WF01: decorator returns a wrapper that preserves metadata |
| Preconditions | Named dummy function with docstring |
| Test Data | See Preconditions |
| Steps | 1. Decorate the function |
| Expected Result | Callable returned; name, docstring and `__wrapped__` kept |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestAuthDecorators.test_preserves_wrapped_function_metadata` (web) |
| Defect ID | - |

## TC-WB-WA01 - login_required_web (wrapper)

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-WA01 (Source ID: WA01) |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path WA01: no session user -> redirect |
| Preconditions | Session has no `user_id`, or 0, or "" |
| Test Data | See Preconditions |
| Steps | 1. Call the wrapper |
| Expected Result | HTTP 302 to `/login`; protected function not run |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestAuthDecorators.test_unauthenticated_request_does_not_call_function` (web, 3 variants) |
| Defect ID | - |

## TC-WB-WA02 - login_required_web (wrapper)

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-WA02 (Source ID: WA02) |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path WA02: logged-in user reaches the view |
| Preconditions | Session `user_id=1`; arguments `7`, `category="Study"` |
| Test Data | See Preconditions |
| Steps | 1. Call the wrapper |
| Expected Result | Function called once with both arguments; its result returned by identity |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestAuthDecorators.test_authenticated_request_forwards_arguments_and_result` (web) |
| Defect ID | - |

## TC-WB-AF01 - login_required_api (factory)

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-AF01 (Source ID: AF01) |
| Feature/Requirement | REQ-002, REQ-009 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path AF01: decorator returns a wrapper that preserves metadata |
| Preconditions | Named dummy function with docstring |
| Test Data | See Preconditions |
| Steps | 1. Decorate the function |
| Expected Result | Callable returned; metadata kept |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestAuthDecorators.test_preserves_wrapped_function_metadata` (API) |
| Defect ID | - |

## TC-WB-AA01 - login_required_api (wrapper)

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-AA01 (Source ID: AA01) |
| Feature/Requirement | REQ-002, REQ-009 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path AA01: no session user -> JSON 401 |
| Preconditions | Session has no `user_id`, or 0, or "" |
| Test Data | See Preconditions |
| Steps | 1. Call the wrapper |
| Expected Result | `{"error": "authentication required"}` with HTTP 401; function not run |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestAuthDecorators.test_unauthenticated_request_does_not_call_function` (API, 3 variants) |
| Defect ID | - |

## TC-WB-AA02 - login_required_api (wrapper)

| Field | Value |
| --- | --- |
| Test Case ID | TC-WB-AA02 (Source ID: AA02) |
| Feature/Requirement | REQ-002, REQ-009 |
| Technique/Test Type | Basis-path white-box / Unit test |
| Objective | Path AA02: logged-in user reaches the view |
| Preconditions | Session `user_id=1`; arguments `7`, `category="Study"` |
| Test Data | See Preconditions |
| Steps | 1. Call the wrapper |
| Expected Result | Function called once with the arguments; original result returned |
| Actual Result | As expected; all instances of this case passed in the 2026-10-26 baseline run |
| Status | Pass |
| Evidence | `test_app.py` run output and `htmlcov/`; automated test: `TestAuthDecorators.test_authenticated_request_forwards_arguments_and_result` (API) |
| Defect ID | - |

Helper-function tests in `test_helpers.py` (20 instances: `compute_urgency` 6, `is_valid_password` 3, `is_valid_username` 5, `completed_in_last_n_days` 6) are execution units of W2 but not path cases. They all passed. Their expectations record the implementation's behaviour, including the known mismatches behind DEF-001 and DEF-002 (W2 Section 3.4), so they must not be read as proof of conformance to the requirements.

---

# Appendix C - Week 3 special-testing cases (verbatim)

Source: `03_Special_Testing/1_GUI/test_cases.md`, `2_Compatibility/test_cases.md`, `3_Usability/test_cases.md` and `4_Accessibility/test_cases.md`, commit `TBD`. Each file is copied unchanged, including its own header, review sign-off and index. Relative links resolve inside `03_Special_Testing/`, not here. TC-USA-001 to 005 are Not Run until the two-reviewer heuristic review is carried out.


# Appendix C.1 GUI (`03_Special_Testing/1_GUI/test_cases.md`)

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

# Appendix C.2 Compatibility (`03_Special_Testing/2_Compatibility/test_cases.md`)

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

# Appendix C.3 Usability (`03_Special_Testing/3_Usability/test_cases.md`)

# Week 3 - Usability Test Cases

Detailed cases for [Task 3 - Usability observations](../README.md#task-3) of the [Week 3 plan](../README.md). Each case uses the guideline's test-case template fields. Precondition codes (P-APP, P-OUT, P-A, P-C), test accounts and fixture IDs (F1-F9) are defined in [fixtures.md](../fixtures.md). Every case is `Not Run` until executed; fill in Actual Result, Status, Evidence and Defect ID only after execution, and replace `<YYYYMMDD>` in evidence filenames with the execution date.

## Review sign-off

Expected results must be reviewed before execution (plan step 3). The reviewer checks that each expected result cites a basis from [README 0.3](../README.md#03-test-basis) and was not derived from observed behaviour.

| Reviewer | Date | Cases reviewed | Changes requested | Approved |
| --- | --- | --- | --- | --- |
| Team (verbal approval of execution, recorded by Darius Lee Shin) | 2026-11-18 | TC-USA-001 to 005 | None recorded | Yes (verbal) |

## Case index

| ID | Title |
| --- | --- |
| [TC-USA-001](#tc-usa-001---ease-of-navigation) | Ease of navigation |
| [TC-USA-002](#tc-usa-002---feedback) | Feedback |
| [TC-USA-003](#tc-usa-003---consistency) | Consistency |
| [TC-USA-004](#tc-usa-004---error-prevention) | Error prevention |
| [TC-USA-005](#tc-usa-005---understandability) | Understandability |

## How to run

**Review kit.** Setup, account seeding, the notes template and the GUI-suite inputs are in [review_kit.md](review_kit.md).

**Method: two-reviewer heuristic evaluation.** There are no end-user participants and no automation. Each case covers one of the five usability qualities named in the project guideline, mapped to Nielsen's heuristics. Each case is applied to all six pages: `/login`, `/register`, `/` (task list), `/tasks/new`, `/tasks/<id>/edit` and `/dashboard`, together with the shared navigation bar.

| Role | Member |
| --- | --- |
| Reviewer 1 | Eu Kwan Ik |
| Reviewer 2 | Ameera Alysha binti Azlan |

**Procedure for every case:**

1. Each reviewer works **independently**, on C01 with account A and Fixture Set A, and performs each page's main actions as a first-time user would.
2. The reviewer answers the case's guiding questions for every page and records each problem in their own notes: page, element, description, the heuristic it breaks, a severity from 0 to 4, and a screenshot.
3. The two reviewers then meet and merge their notes. They remove duplicates and agree a severity for each problem; if they cannot agree, the higher rating is used and both ratings are recorded.
4. Each merged problem is logged as a `USA-OBS-` item in the [README 3.3 observation log](../README.md#33-observation-log).
5. The case verdict follows the fixed threshold below.

**Severity scale (Nielsen):** 0 not a usability problem; 1 cosmetic; 2 minor; 3 major; 4 catastrophic.

**Verdict threshold (fixed before the review):** a case **fails** if any merged observation for its quality is rated **3 or 4**. Otherwise it **passes**, even if observations rated 1 or 2 are logged. A failed case links each severity 3-4 observation, and a `DEF-` record is raised only when the observation also breaks a stated requirement or interface promise.

**Inputs from other techniques:** findings from [TC-GUI-017](../1_GUI/test_cases.md#tc-gui-017---feedback-after-actions) (feedback after actions) and the username-retention observation in [TC-GUI-002](../1_GUI/test_cases.md#tc-gui-002---login-error-message) are fed into TC-USA-002 and TC-USA-004 respectively, so that the same problem is not counted twice.

## TC-USA-001 - Ease of navigation

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-001 |
| Feature/Requirement | All pages and the navigation bar; REQ-002, REQ-003, REQ-007 |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess how easily a user can move between pages and get back from any page. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H6 Recognition rather than recall", "H3 User control and freedom"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Guiding questions for each page: Can every main page be reached from the navigation bar? Is it clear which page you are on? Is there always a way back or a Cancel option? Can a user who opens a form by mistake leave it without losing other work? |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (ease of navigation); Nielsen heuristics 3 and 6. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-001-<reviewer-initials>-<YYYYMMDD>.md` (one notes file per reviewer) plus screenshots `evidences/TC-USA-001-<short-desc>-<YYYYMMDD>.jpg` |
| Defect ID | — |

## TC-USA-002 - Feedback

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-002 |
| Feature/Requirement | All pages; REQ-001 to REQ-004 |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess whether the application tells the user what happened after every action. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H1 Visibility of system status"], "actions": ["register", "log in", "log out", "create", "edit", "complete", "reopen", "delete", "filter", "search"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Perform each action in Test Data.<br>3. Guiding questions for each action: Does the page show that the action succeeded or failed? Is the result visible without searching for it? Are active filters and search terms clearly shown? Include the TC-GUI-017 findings (H6). |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (feedback); Nielsen heuristic 1. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-002-<reviewer-initials>-<YYYYMMDD>.md` plus screenshots `evidences/TC-USA-002-<short-desc>-<YYYYMMDD>.jpg` |
| Defect ID | — |

## TC-USA-003 - Consistency

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-003 |
| Feature/Requirement | All pages |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess whether wording, controls and layout are consistent across pages and with common web conventions. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H4 Consistency and standards"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Guiding questions: Are the same actions named the same way everywhere (for example `Log in` and `Log out`, `Create Task` and `Save Changes`)? Do buttons with the same role look and sit in the same place? Do controls behave as users expect from other websites (for example, do filters apply on change or on a button)? Use [TC-GUI-022](../1_GUI/test_cases.md#tc-gui-022---visual-consistency) results as input for visual styling. |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (consistency); Nielsen heuristic 4. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-003-<reviewer-initials>-<YYYYMMDD>.md` plus screenshots `evidences/TC-USA-003-<short-desc>-<YYYYMMDD>.jpg` |
| Defect ID | — |

## TC-USA-004 - Error prevention

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-004 |
| Feature/Requirement | `/register`, `/login`, task forms, delete; REQ-001 to REQ-003 |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess whether the interface prevents mistakes and helps users recover from them. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H5 Error prevention", "H9 Help users recognise, diagnose and recover from errors"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Guiding questions: Are input rules shown before the user types? Are destructive actions (delete) confirmed? Can completing a task by mistake be undone easily? Do error messages say what went wrong and how to fix it? Are entered values kept after an error, so the user does not retype them? Include the TC-GUI-002 username-retention observation. |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (error prevention); Nielsen heuristics 5 and 9. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-004-<reviewer-initials>-<YYYYMMDD>.md` plus screenshots `evidences/TC-USA-004-<short-desc>-<YYYYMMDD>.jpg` |
| Defect ID | — |

## TC-USA-005 - Understandability

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-005 |
| Feature/Requirement | All pages; REQ-004, REQ-006, REQ-007 |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess whether labels, symbols and terms are understandable without explanation. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H2 Match between system and the real world", "H8 Aesthetic and minimalist design"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Guiding questions: Are the urgency names (Overdue, Due Today, Due Soon, Upcoming, No due date, Done) clear without a definition? Is the `○`/`✓` control recognisable as "mark complete"? Are the dashboard counters clear, including what "Completed (last 7 days)" counts? Does any page show information that is irrelevant or distracting? |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (understandability); Nielsen heuristics 2 and 8. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-005-<reviewer-initials>-<YYYYMMDD>.md` plus screenshots `evidences/TC-USA-005-<short-desc>-<YYYYMMDD>.jpg` |
| Defect ID | — |

# Appendix C.4 Accessibility (`03_Special_Testing/4_Accessibility/test_cases.md`)

# Week 3 - Accessibility Test Cases

Detailed cases for [Task 4 - Basic accessibility findings](../README.md#task-4) of the [Week 3 plan](../README.md). Each case uses the guideline's test-case template fields. Precondition codes (P-APP, P-OUT, P-A, P-C), test accounts and fixture IDs (F1-F9) are defined in [fixtures.md](../fixtures.md). Executed on 2026-11-18 on C01 (Chrome 157.0.8103.80, macOS 26.5.2, headless) by the Playwright suite [test_accessibility.py](test_accessibility.py), run twice: [results-C01-20261118-213348.json](evidences/results-C01-20261118-213348.json) is the recorded run and [results-C01-20261118-213235.json](evidences/results-C01-20261118-213235.json) the first reproduction. Results were identical in both runs.

**How the steps were automated.** The script performs the DevTools steps with equivalent programmatic checks: computed styles for contrast, focus and target size; Chrome's accessibility tree (read through the DevTools protocol and Playwright accessibility snapshots) for names, roles and landmarks; Chrome's vision-deficiency emulation for TC-A11Y-003; and a 640x400 CSS-pixel viewport at device scale 2 for 200% zoom (TC-A11Y-013).

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

Run on C01 unless the case says otherwise. Tools: Chrome DevTools (Elements, Accessibility pane, Rendering, device toolbar, colour picker contrast), Lighthouse, axe DevTools or WAVE. Screen readers are out of scope; accessible names, roles and landmarks are read from Chrome's accessibility tree.

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
| Steps | 1. On each page, list the headings and their levels (DevTools Elements or the accessibility tree).<br>2. On `/`, check that table headers are marked up as header cells.<br>3. Check for landmarks (navigation, main). |
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
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that each form field is programmatically labelled with its visible label (H2). |
| Preconditions | P-OUT for the auth pages; P-A for `/tasks/new` |
| Test Data | {} |
| Steps | 1. Click each label's text and note whether focus moves into its field.<br>2. In DevTools -> Accessibility, record each field's computed name. |
| Expected Result | Clicking a label focuses its field. Each field's computed name equals its visible label (for example `Username`). Basis: WCAG 1.3.1, 4.1.2. |
| Actual Result | Clicking any label on `/login`, `/register` or `/tasks/new` leaves focus on the page body, and every field's accessible name is empty, so a screen reader announces only the field type. |
| Status | Fail |
| Evidence | [TC-A11Y-005-labels-20261118.jpg](evidences/TC-A11Y-005-labels-20261118.jpg) |
| Defect ID | DEF-007 |

## TC-A11Y-006 - Filter and search labels

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-006 |
| Feature/Requirement | WCAG 2.2 SC 3.3.2 Labels or Instructions (A) - task list filters |
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that the category list, status list and search box have labels (H4). |
| Preconditions | P-A |
| Test Data | {} |
| Steps | 1. Record whether each filter control has a visible label and its computed name in DevTools. |
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
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that the complete/reopen button's accessible name states what it does, for which task, and the task's state (H3). |
| Preconditions | P-A |
| Test Data | {"fixtures": ["F3", "F6"]} |
| Steps | 1. Record the accessible name and state of the button on F3 (open).<br>2. Repeat on F6 (done). |
| Expected Result | Each accessible name identifies the action and the task, and the state is conveyed, for example "Mark GUI-Soon as done, button" and "Mark GUI-Done as not done, button". Basis: WCAG 4.1.2. |
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
| Actual Result | Every step was completed with the keyboard only: log in, create a task (Work chosen by typing `W`, date typed into the segmented date control), filter, search, complete, reopen, edit, save, delete, open the dashboard and log out. No keyboard trap. The native delete dialog was answered by Playwright. |
| Status | Pass |
| Evidence | [TC-A11Y-008-keyboard-end-20261118.jpg](evidences/TC-A11Y-008-keyboard-end-20261118.jpg) |
| Defect ID | — |

## TC-A11Y-009 - Bypass the navigation bar

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-009 |
| Feature/Requirement | WCAG 2.2 SC 2.4.1 Bypass Blocks (A) - logged-in pages |
| Technique/Test Type | Accessibility (WCAG) - keyboard and inspection |
| Objective | Verify that keyboard and assistive-technology users can skip the navigation bar (H8). |
| Preconditions | P-A |
| Test Data | {} |
| Steps | 1. Open `/`, press Tab once and record what receives focus.<br>2. Check the accessibility tree for a main-content landmark. |
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
| Evidence | [TC-GUI-021 results](../1_GUI/evidences/results-C01-20261118-1933.json); [this run](evidences/results-C01-20261118-213348.json) |
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
| Evidence | [results-C01-20261118-213348.json](evidences/results-C01-20261118-213348.json) (recorded values) |
| Defect ID | — |

## TC-A11Y-015 - Error identification and announcement

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-A11Y-015 |
| Feature/Requirement | WCAG 2.2 SC 3.3.1 Error Identification (A), 4.1.3 Status Messages (AA) - `/login`, `/register` |
| Technique/Test Type | Accessibility (WCAG) - inspection |
| Objective | Verify that form errors are described in text and exposed for announcement by assistive technology (H7). |
| Preconditions | P-OUT |
| Test Data | {"login": {"username": "w3<initial>_gui_<ddmm>", "password": "WrongPass1"}, "register": {"username": "ab", "password": "Test12345"}} |
| Steps | 1. Submit the login data.<br>2. After the page reloads, record the error text, its role and live-region attributes, and where focus is.<br>3. Repeat with the register data. |
| Expected Result | Each error is described in text and exposed for announcement without the user having to search for it (an alert role, a live region, or focus moved to it). Basis: WCAG 3.3.1, 4.1.3. |
| Actual Result | Both errors are described in text (`Invalid username or password.`; `Username must be 3-20 characters ...`), but neither has an alert role or live region, and focus is not moved to it after the page reloads. |
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

---

# Appendix D - Week 4 web and API cases (verbatim)

Source: `04_Web_API/test_cases.md`, commit `TBD`; application commit `fc0767f`. Everything below is copied unchanged from the first case heading onward. Relative links (`evidences/...`, `test_data.md`) resolve inside `04_Web_API/`, not here.

## TC-WEB-001 - Register through the web form

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-001 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | Workflow / web |
| Objective | The registration form logs the user in and opens the task list |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-001a: `form: username='{{web_user}}', password='{{password}}'` |
| Steps | 1. `POST /register` (TC-WEB-001a)<br>2. `GET /` (TC-WEB-001b) |
| Expected Result | TC-WEB-001a: redirects (302) to /<br>TC-WEB-001b: status is 200; page contains "My Tasks"; page shows the username |
| Actual Result | TC-WEB-001a: 302 FOUND - all checks passed<br>TC-WEB-001b: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-002 - Registration validated on the server

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-002 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | Client-server validation / EP |
| Objective | The server re-checks registration input even when the browser's `required` check is bypassed |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-002a: `form: username='', password='{{password}}'`<br>TC-WEB-002b: `form: username='bad-name', password='{{password}}'`<br>TC-WEB-002c: `form: username='{{tmp_name}}', password='abc1234'` |
| Steps | 1. `POST /register` (TC-WEB-002a)<br>2. `POST /register` (TC-WEB-002b)<br>3. `POST /register` (TC-WEB-002c) |
| Expected Result | TC-WEB-002a: status is 200; server shows the username error<br>TC-WEB-002b: status is 200; server shows the username error<br>TC-WEB-002c: status is 200; server shows the password error |
| Actual Result | TC-WEB-002a: 200 OK - all checks passed<br>TC-WEB-002b: 200 OK - all checks passed<br>TC-WEB-002c: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-003 - Login through the web form

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-003 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Decision table / web |
| Objective | Valid login opens the task list; wrong password shows the error and keeps pages protected |
| Preconditions | User A registered; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-003a: `form: username='{{web_user}}', password='{{password}}'`<br>TC-WEB-003b: `form: username='{{web_user}}', password='Wrong12345'` |
| Steps | 1. `POST /login` (TC-WEB-003a)<br>2. `POST /login` (TC-WEB-003b) |
| Expected Result | TC-WEB-003a: redirects (302) to /<br>TC-WEB-003b: status is 200; server shows the login error |
| Actual Result | TC-WEB-003a: 302 FOUND - all checks passed<br>TC-WEB-003b: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-004 - Protected pages redirect when logged out

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-004 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | EP (unauthenticated) / web |
| Objective | Every protected page and action redirects to /login |
| Preconditions | No session cookie; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-004e: `form: `<br>TC-WEB-004f: `form: ` |
| Steps | 1. `GET /` (TC-WEB-004a)<br>2. `GET /tasks/new` (TC-WEB-004b)<br>3. `GET /tasks/1/edit` (TC-WEB-004c)<br>4. `GET /dashboard` (TC-WEB-004d)<br>5. `POST /tasks/1/toggle` (TC-WEB-004e)<br>6. `POST /tasks/1/delete` (TC-WEB-004f) |
| Expected Result | TC-WEB-004a: redirects (302) to /login<br>TC-WEB-004b: redirects (302) to /login<br>TC-WEB-004c: redirects (302) to /login<br>TC-WEB-004d: redirects (302) to /login<br>TC-WEB-004e: redirects (302) to /login<br>TC-WEB-004f: redirects (302) to /login |
| Actual Result | TC-WEB-004a: 302 FOUND - all checks passed<br>TC-WEB-004b: 302 FOUND - all checks passed<br>TC-WEB-004c: 302 FOUND - all checks passed<br>TC-WEB-004d: 302 FOUND - all checks passed<br>TC-WEB-004e: 302 FOUND - all checks passed<br>TC-WEB-004f: 302 FOUND - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-005 - Web-created task matches the API

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-005 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Workflow / UI vs API comparison |
| Objective | A task created with the form is stored exactly as entered |
| Preconditions | User registered and logged in through the web form `POST /register`; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-005a: `form: title='Web-created task', description='via form', category_id='{{cat_personal}}', due_date='{{plus6}}'` |
| Steps | 1. `POST /tasks/new` (TC-WEB-005a)<br>2. `GET /api/tasks?q=Web-created` (TC-WEB-005b) |
| Expected Result | TC-WEB-005a: redirects (302) to /<br>TC-WEB-005b: status is 200; one task with the same title, description, category, date |
| Actual Result | TC-WEB-005a: 302 FOUND - all checks passed<br>TC-WEB-005b: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-006 - API-created task matches the web list

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-006 |
| Feature/Requirement | REQ-003 / REQ-006 |
| Technique/Test Type | Workflow / API vs UI comparison |
| Objective | The web list shows API data with the same category, date and urgency |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | title `API-created task`, category Study, due today+1 |
| Steps | 1. `GET /` (TC-WEB-006) |
| Expected Result | TC-WEB-006: status is 200; the task's row shows category Study and urgency Due Soon |
| Actual Result | TC-WEB-006: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-007 - Web edit matches the API

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-007 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Workflow / UI vs API comparison |
| Objective | Edits saved on the web are returned by the API |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); one task due today+3; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-007a: `form: title='After edit', description='edited on web', category_id='{{cat_urgent}}', due_date='{{plus9}}'` |
| Steps | 1. `POST /tasks/{{w_id}}/edit` (TC-WEB-007a)<br>2. `GET /api/tasks/{{w_id}}` (TC-WEB-007b) |
| Expected Result | TC-WEB-007a: redirects (302) to /<br>TC-WEB-007b: status is 200; title, description, category and date match the edit |
| Actual Result | TC-WEB-007a: 302 FOUND - all checks passed<br>TC-WEB-007b: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-008 - Web toggle matches the API

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-008 |
| Feature/Requirement | REQ-004 |
| Technique/Test Type | State transition / UI vs API comparison |
| Objective | Toggling on the web updates done and completed_at as the API reports them |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); one open task; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-008a: `form: `<br>TC-WEB-008c: `form: ` |
| Steps | 1. `POST /tasks/{{w_id}}/toggle` (TC-WEB-008a)<br>2. `GET /api/tasks/{{w_id}}` (TC-WEB-008b)<br>3. `POST /tasks/{{w_id}}/toggle` (TC-WEB-008c)<br>4. `GET /api/tasks/{{w_id}}` (TC-WEB-008d) |
| Expected Result | TC-WEB-008a: redirects (302) to /<br>TC-WEB-008b: status is 200; done is true; completed_at is set<br>TC-WEB-008c: redirects (302) to /<br>TC-WEB-008d: status is 200; done is false; completed_at is null |
| Actual Result | TC-WEB-008a: 302 FOUND - all checks passed<br>TC-WEB-008b: 200 OK - all checks passed<br>TC-WEB-008c: 302 FOUND - all checks passed<br>TC-WEB-008d: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-009 - Web delete matches the API

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-009 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Workflow / UI vs API comparison |
| Objective | A task deleted on the web is gone from the API |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); one task; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-009a: `form: ` |
| Steps | 1. `POST /tasks/{{w_id}}/delete` (TC-WEB-009a)<br>2. `GET /api/tasks/{{w_id}}` (TC-WEB-009b) |
| Expected Result | TC-WEB-009a: redirects (302) to /<br>TC-WEB-009b: status is 404 |
| Actual Result | TC-WEB-009a: 302 FOUND - all checks passed<br>TC-WEB-009b: 404 NOT FOUND - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-010 - Blank title validated on the server

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-010 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Client-server validation / EP |
| Objective | The server rejects a blank title even when the browser's `required` check is bypassed (the API already does, TC-API-016) |
| Preconditions | User registered and logged in through the web form `POST /register`; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-010a: `form: title='', description='', category_id='', due_date=''`<br>TC-WEB-010b: `form: title='   ', description='', category_id='', due_date=''` |
| Steps | 1. `POST /tasks/new` (TC-WEB-010a)<br>2. `GET /api/tasks` (TC-WEB-010a-check)<br>3. `POST /tasks/new` (TC-WEB-010b)<br>4. `GET /api/tasks` (TC-WEB-010b-check) |
| Expected Result | TC-WEB-010a: server does not accept it (no redirect to the task list)<br>TC-WEB-010a-check: no task was saved<br>TC-WEB-010b: server does not accept it (no redirect to the task list)<br>TC-WEB-010b-check: no task was saved |
| Actual Result | TC-WEB-010a: 302 FOUND - **FAILED:** server does not accept it (no redirect to the task list)<br>TC-WEB-010a-check: 200 OK - **FAILED:** no task was saved<br>TC-WEB-010b: 302 FOUND - **FAILED:** server does not accept it (no redirect to the task list)<br>TC-WEB-010b-check: 200 OK - **FAILED:** no task was saved |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-WEB-010-012-016-web-form-validation-20261124.jpg](evidences/TC-WEB-010-012-016-web-form-validation-20261124.jpg) |
| Defect ID | DEF-003 |

## TC-WEB-011 - Due date validated on the server

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-011 |
| Feature/Requirement | REQ-003 / REQ-006 |
| Technique/Test Type | Client-server validation / EP |
| Objective | The server rejects text that is not a date when the date picker is bypassed |
| Preconditions | User registered and logged in through the web form `POST /register`; Postman folder "99 Run last - invalid due dates" |
| Test Data | TC-WEB-011a: `form: title='bad date', due_date='31/12/2026'`<br>TC-WEB-011b: `form: title='bad date', due_date='not-a-date'` |
| Steps | 1. `POST /tasks/new` (TC-WEB-011a)<br>2. `GET /` (TC-WEB-011a-check1)<br>3. `GET /dashboard` (TC-WEB-011a-check2)<br>4. `POST /tasks/new` (TC-WEB-011b)<br>5. `GET /` (TC-WEB-011b-check1)<br>6. `GET /dashboard` (TC-WEB-011b-check2) |
| Expected Result | TC-WEB-011a: server does not accept it (no redirect to the task list)<br>TC-WEB-011a-check1: status is 200<br>TC-WEB-011a-check2: status is 200<br>TC-WEB-011b: server does not accept it (no redirect to the task list)<br>TC-WEB-011b-check1: status is 200<br>TC-WEB-011b-check2: status is 200 |
| Actual Result | TC-WEB-011a: 302 FOUND - **FAILED:** server does not accept it (no redirect to the task list)<br>TC-WEB-011a-check1: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200<br>TC-WEB-011a-check2: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200<br>TC-WEB-011b: 302 FOUND - **FAILED:** server does not accept it (no redirect to the task list)<br>TC-WEB-011b-check1: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200<br>TC-WEB-011b-check2: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200 |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-WEB-011-web-bad-date-500-20261124.jpg](evidences/TC-WEB-011-web-bad-date-500-20261124.jpg) |
| Defect ID | DEF-015 |

## TC-WEB-012 - Category validated on the server

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-012 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Client-server validation / EP |
| Objective | The server rejects a category id that the select box does not offer |
| Preconditions | User registered and logged in through the web form `POST /register`; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-012a: `form: title='bad category', category_id='999'` |
| Steps | 1. `POST /tasks/new` (TC-WEB-012a)<br>2. `GET /api/tasks` (TC-WEB-012b-check) |
| Expected Result | TC-WEB-012a: server does not accept it (no redirect to the task list)<br>TC-WEB-012b-check: no task was saved |
| Actual Result | TC-WEB-012a: 302 FOUND - **FAILED:** server does not accept it (no redirect to the task list)<br>TC-WEB-012b-check: 200 OK - **FAILED:** no task was saved |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-WEB-010-012-016-web-form-validation-20261124.jpg](evidences/TC-WEB-010-012-016-web-form-validation-20261124.jpg) |
| Defect ID | DEF-019 |

## TC-WEB-013 - Web actions on another user's task

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-013 |
| Feature/Requirement | REQ-008 |
| Technique/Test Type | EP (foreign id) / UI vs API comparison |
| Objective | Web edit/toggle/delete cannot change another user's task (compare TC-API-040) |
| Preconditions | Users A and B registered and logged in, Postman switches between them with SETUP log-in requests; A owns one task; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-013a: `form: title='hijacked'`<br>TC-WEB-013b: `form: `<br>TC-WEB-013c: `form: ` |
| Steps | 1. `POST /tasks/{{o_id}}/edit` (TC-WEB-013a)<br>2. `POST /tasks/{{o_id}}/toggle` (TC-WEB-013b)<br>3. `POST /tasks/{{o_id}}/delete` (TC-WEB-013c)<br>4. `GET /api/tasks/{{o_id}}` (TC-WEB-013d) |
| Expected Result | TC-WEB-013a: action only (verified by the next request)<br>TC-WEB-013b: action only (verified by the next request)<br>TC-WEB-013c: action only (verified by the next request)<br>TC-WEB-013d: status is 200; title unchanged; still open |
| Actual Result | TC-WEB-013a: 302 FOUND<br>TC-WEB-013b: 302 FOUND<br>TC-WEB-013c: 302 FOUND<br>TC-WEB-013d: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-014 - Web dashboard matches the API dashboard

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-014 |
| Feature/Requirement | REQ-007 |
| Technique/Test Type | UI vs API comparison |
| Objective | Both dashboards report the same numbers |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); [dashboard dataset](test_data.md#dashboard-dataset); Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | - |
| Steps | 1. `GET /dashboard` (TC-WEB-014a)<br>2. `GET /api/dashboard` (TC-WEB-014b) |
| Expected Result | TC-WEB-014a: status is 200<br>TC-WEB-014b: status is 200; same five numbers as the web page |
| Actual Result | TC-WEB-014a: 200 OK - all checks passed<br>TC-WEB-014b: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-015 - Web search with an apostrophe

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-015 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP (special character) / UI vs API comparison |
| Objective | The web search handles a quote character (compare TC-API-030) |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); tasks `Call O'Brien` and `Other`; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | `q=O'Brien` |
| Steps | 1. `GET /?q=O'Brien` (TC-WEB-015) |
| Expected Result | TC-WEB-015: status is 200; the matching task is listed; the other task is filtered out |
| Actual Result | TC-WEB-015: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-WEB-016 - Duplicate username on the web form

| Field | Value |
| --- | --- |
| Test Case ID | TC-WEB-016 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / web negative |
| Objective | The web form refuses an existing username |
| Preconditions | User A registered; Postman folder "10 Web forms (server-side validation, UI vs API)" |
| Test Data | TC-WEB-016: `form: username='{{user_a}}', password='Different99'` |
| Steps | 1. `POST /register` (TC-WEB-016) |
| Expected Result | TC-WEB-016: form is shown again with an error (200, not a 302 login) |
| Actual Result | TC-WEB-016: 302 FOUND - **FAILED:** form is shown again with an error (200, not a 302 login) |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-WEB-010-012-016-web-form-validation-20261124.jpg](evidences/TC-WEB-010-012-016-web-form-validation-20261124.jpg) |
| Defect ID | DEF-016 |

## TC-API-001 - Register a valid account

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-001 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / API functional |
| Objective | Valid registration returns 201 with the account and starts a session |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "01 Registration and login" |
| Test Data | TC-API-001: `{"username": "{{user_a}}", "password": "{{password}}"}` |
| Steps | 1. `POST /api/register` (TC-API-001) |
| Expected Result | TC-API-001: status is 201; id is a number; username is echoed back |
| Actual Result | TC-API-001: 201 CREATED - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-002 - Username valid length boundaries (3, 20)

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-002 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / API |
| Objective | Minimum and maximum valid username lengths are accepted |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "01 Registration and login" |
| Test Data | TC-API-002a: `{"username": "{{tmp_name}}", "password": "{{password}}"}`<br>TC-API-002b: `{"username": "{{tmp_name}}", "password": "{{password}}"}` |
| Steps | 1. `POST /api/register` (TC-API-002a)<br>2. `POST /api/register` (TC-API-002b) |
| Expected Result | TC-API-002a: status is 201<br>TC-API-002b: status is 201 |
| Actual Result | TC-API-002a: 201 CREATED - all checks passed<br>TC-API-002b: 201 CREATED - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-003 - Invalid username partitions

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-003 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP + BVA / API negative |
| Objective | Too short, too long, illegal character and missing username are rejected with a JSON error |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "01 Registration and login" |
| Test Data | TC-API-003a: `{"username": "ab", "password": "{{password}}"}`<br>TC-API-003b: `{"username": "wwwwwwwwwwwwwwwwwwwww", "password": "{{password}}"}`<br>TC-API-003c: `{"username": "bad-name", "password": "{{password}}"}`<br>TC-API-003d: `{"password": "{{password}}"}` |
| Steps | 1. `POST /api/register` (TC-API-003a)<br>2. `POST /api/register` (TC-API-003b)<br>3. `POST /api/register` (TC-API-003c)<br>4. `POST /api/register` (TC-API-003d) |
| Expected Result | TC-API-003a: status is 400; response body is JSON (not an HTML error page); error message is "invalid username"<br>TC-API-003b: status is 400; response body is JSON (not an HTML error page); error message is "invalid username"<br>TC-API-003c: status is 400; response body is JSON (not an HTML error page); error message is "invalid username"<br>TC-API-003d: status is 400; response body is JSON (not an HTML error page); error message is "invalid username" |
| Actual Result | TC-API-003a: 400 BAD REQUEST - all checks passed<br>TC-API-003b: 400 BAD REQUEST - all checks passed<br>TC-API-003c: 400 BAD REQUEST - all checks passed<br>TC-API-003d: 400 BAD REQUEST - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-004 - Password length 7 rejected

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-004 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / API negative |
| Objective | Password below the 8-character minimum is rejected |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "01 Registration and login" |
| Test Data | TC-API-004: `{"username": "{{tmp_name}}", "password": "abc1234"}` |
| Steps | 1. `POST /api/register` (TC-API-004) |
| Expected Result | TC-API-004: status is 400; response body is JSON (not an HTML error page); error message is "invalid password" |
| Actual Result | TC-API-004: 400 BAD REQUEST - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-005 - Password length 8 accepted

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-005 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / API |
| Objective | Password at exactly the stated minimum (8) is accepted |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "01 Registration and login" |
| Test Data | TC-API-005: `{"username": "{{tmp_name}}", "password": "abcd1234"}` |
| Steps | 1. `POST /api/register` (TC-API-005) |
| Expected Result | TC-API-005: status is 201 |
| Actual Result | TC-API-005: 400 BAD REQUEST - **FAILED:** status is 201 |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-005-password-8-chars-rejected-20261124.jpg](evidences/TC-API-005-password-8-chars-rejected-20261124.jpg) |
| Defect ID | DEF-001 |

## TC-API-006 - Missing password rejected

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-006 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / API negative |
| Objective | Registration without a password field is rejected |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "01 Registration and login" |
| Test Data | TC-API-006: `{"username": "{{tmp_name}}"}` |
| Steps | 1. `POST /api/register` (TC-API-006) |
| Expected Result | TC-API-006: status is 400; response body is JSON (not an HTML error page) |
| Actual Result | TC-API-006: 400 BAD REQUEST - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-007 - Username of the wrong JSON type

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-007 |
| Feature/Requirement | REQ-001 / REQ-009 |
| Technique/Test Type | EP (data type) / API negative |
| Objective | A non-string username is handled as invalid input, not a server crash |
| Preconditions | Application running; no session cookie (Postman 'Disable cookie jar'); Postman folder "01 Registration and login" |
| Test Data | TC-API-007: `{"username": 12345, "password": "{{password}}"}` |
| Steps | 1. `POST /api/register` (TC-API-007) |
| Expected Result | TC-API-007: status is 400; response body is JSON (not an HTML error page) |
| Actual Result | TC-API-007: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page) |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-007-username-number-500-20261124.jpg](evidences/TC-API-007-username-number-500-20261124.jpg) |
| Defect ID | DEF-018 |

## TC-API-008 - Duplicate username rejected

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-008 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / API negative |
| Objective | A username that already exists cannot be registered again |
| Preconditions | User A registered; Postman folder "01 Registration and login" |
| Test Data | TC-API-008a: `{"username": "{{user_a}}", "password": "Different99"}`<br>TC-API-008b: `{"username": "{{user_a}}", "password": "{{password}}"}` |
| Steps | 1. `POST /api/register` (TC-API-008a)<br>2. `POST /api/login` (TC-API-008b) |
| Expected Result | TC-API-008a: status is 409 or 400 (username already taken); response body is JSON (not an HTML error page)<br>TC-API-008b: status is 200 |
| Actual Result | TC-API-008a: 201 CREATED - **FAILED:** status is 409 or 400 (username already taken)<br>TC-API-008b: 200 OK - all checks passed |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-008-duplicate-username-accepted-20261124.jpg](evidences/TC-API-008-duplicate-username-accepted-20261124.jpg) |
| Defect ID | DEF-016 |

## TC-API-009 - Login with valid credentials

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-009 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Decision table (valid/valid) / API |
| Objective | Valid credentials return 200 with the account and start a session |
| Preconditions | User A registered; Postman folder "01 Registration and login" |
| Test Data | TC-API-009: `{"username": "{{user_a}}", "password": "{{password}}"}` |
| Steps | 1. `POST /api/login` (TC-API-009) |
| Expected Result | TC-API-009: status is 200; username is returned |
| Actual Result | TC-API-009: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-010 - Login with invalid credentials

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-010 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Decision table / API negative |
| Objective | Wrong password, unknown user and empty body are refused with 401 and no session |
| Preconditions | User A registered; Postman folder "01 Registration and login" |
| Test Data | TC-API-010a: `{"username": "{{user_a}}", "password": "Wrong12345"}`<br>TC-API-010b: `{"username": "w4nobody000000", "password": "{{password}}"}`<br>TC-API-010c: `{}` |
| Steps | 1. `POST /api/login` (TC-API-010a)<br>2. `POST /api/login` (TC-API-010b)<br>3. `POST /api/login` (TC-API-010c) |
| Expected Result | TC-API-010a: status is 401; response body is JSON (not an HTML error page); error message is "invalid credentials"<br>TC-API-010b: status is 401; response body is JSON (not an HTML error page); error message is "invalid credentials"<br>TC-API-010c: status is 401; response body is JSON (not an HTML error page); error message is "invalid credentials" |
| Actual Result | TC-API-010a: 401 UNAUTHORIZED - all checks passed<br>TC-API-010b: 401 UNAUTHORIZED - all checks passed<br>TC-API-010c: 401 UNAUTHORIZED - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-011 - Protected endpoints require a session

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-011 |
| Feature/Requirement | REQ-002 / REQ-009 |
| Technique/Test Type | EP (unauthenticated) / API negative |
| Objective | Every task and dashboard endpoint refuses unauthenticated callers with 401 JSON |
| Preconditions | No session cookie; Postman folder "02 Authentication required" |
| Test Data | TC-API-011b: `{"title": "x"}`<br>TC-API-011d: `{"title": "x"}` |
| Steps | 1. `GET /api/tasks` (TC-API-011a)<br>2. `POST /api/tasks` (TC-API-011b)<br>3. `GET /api/tasks/1` (TC-API-011c)<br>4. `PUT /api/tasks/1` (TC-API-011d)<br>5. `DELETE /api/tasks/1` (TC-API-011e)<br>6. `GET /api/dashboard` (TC-API-011f) |
| Expected Result | TC-API-011a: status is 401; response body is JSON (not an HTML error page); error message is "authentication required"<br>TC-API-011b: status is 401; response body is JSON (not an HTML error page); error message is "authentication required"<br>TC-API-011c: status is 401; response body is JSON (not an HTML error page); error message is "authentication required"<br>TC-API-011d: status is 401; response body is JSON (not an HTML error page); error message is "authentication required"<br>TC-API-011e: status is 401; response body is JSON (not an HTML error page); error message is "authentication required"<br>TC-API-011f: status is 401; response body is JSON (not an HTML error page); error message is "authentication required" |
| Actual Result | TC-API-011a: 401 UNAUTHORIZED - all checks passed<br>TC-API-011b: 401 UNAUTHORIZED - all checks passed<br>TC-API-011c: 401 UNAUTHORIZED - all checks passed<br>TC-API-011d: 401 UNAUTHORIZED - all checks passed<br>TC-API-011e: 401 UNAUTHORIZED - all checks passed<br>TC-API-011f: 401 UNAUTHORIZED - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-012 - Categories endpoint requires a session

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-012 |
| Feature/Requirement | REQ-009 |
| Technique/Test Type | EP (unauthenticated) / API negative |
| Objective | The README contract (session auth except register/login) holds for /api/categories |
| Preconditions | No session cookie; Postman folder "02 Authentication required" |
| Test Data | - |
| Steps | 1. `GET /api/categories` (TC-API-012) |
| Expected Result | TC-API-012: status is 401 (README: every endpoint except register/login needs a session) |
| Actual Result | TC-API-012: 200 OK - **FAILED:** status is 401 (README: every endpoint except register/login needs a session) |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-012-categories-without-login-20261124.jpg](evidences/TC-API-012-categories-without-login-20261124.jpg) |
| Defect ID | DEF-023 |

## TC-API-013 - List categories

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-013 |
| Feature/Requirement | REQ-009 |
| Technique/Test Type | API functional |
| Objective | The four seeded categories are returned sorted by name |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "02 Authentication required" |
| Test Data | - |
| Steps | 1. `GET /api/categories` (TC-API-013) |
| Expected Result | TC-API-013: status is 200; the four seeded categories, sorted by name |
| Actual Result | TC-API-013: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-014 - Create a task with all fields

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-014 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP (valid) / API functional |
| Objective | All supplied fields are stored and echoed with derived fields correct |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | TC-API-014: `{"title": "Prepare W4 report", "description": "API section", "category_id": {{cat_work}}, "due_date": "{{plus5}}"}` |
| Steps | 1. `POST /api/tasks` (TC-API-014) |
| Expected Result | TC-API-014: status is 201; title is 'Prepare W4 report'; description is 'API section'; category_id is the Work id; category is 'Work'; due_date is today+5; done is false; completed_at is null; urgency is 'Upcoming' |
| Actual Result | TC-API-014: 201 CREATED - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-015 - Create a title-only task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-015 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP (valid, optional fields omitted) / API |
| Objective | Optional fields default correctly |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | TC-API-015: `{"title": "Title only"}` |
| Steps | 1. `POST /api/tasks` (TC-API-015) |
| Expected Result | TC-API-015: status is 201; description is ''; category_id is null; category is null; due_date is null; urgency is 'No due date' |
| Actual Result | TC-API-015: 201 CREATED - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-016 - Title required

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-016 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP (invalid) / API negative |
| Objective | Missing, empty and whitespace-only titles are rejected and nothing is saved |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | TC-API-016a: `{}`<br>TC-API-016b: `{"title": ""}`<br>TC-API-016c: `{"title": "   "}` |
| Steps | 1. `POST /api/tasks` (TC-API-016a)<br>2. `POST /api/tasks` (TC-API-016b)<br>3. `POST /api/tasks` (TC-API-016c) |
| Expected Result | TC-API-016a: status is 400; response body is JSON (not an HTML error page); error message is "title is required"<br>TC-API-016b: status is 400; response body is JSON (not an HTML error page); error message is "title is required"<br>TC-API-016c: status is 400; response body is JSON (not an HTML error page); error message is "title is required" |
| Actual Result | TC-API-016a: 400 BAD REQUEST - all checks passed<br>TC-API-016b: 400 BAD REQUEST - all checks passed<br>TC-API-016c: 400 BAD REQUEST - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-017 - Non-JSON request body

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-017 |
| Feature/Requirement | REQ-009 |
| Technique/Test Type | EP (invalid format) / API negative |
| Objective | A form-encoded body is refused with a JSON error |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | TC-API-017: `form: title='form body'` |
| Steps | 1. `POST /api/tasks` (TC-API-017) |
| Expected Result | TC-API-017: status is 400; response body is JSON (not an HTML error page) |
| Actual Result | TC-API-017: 400 BAD REQUEST - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-018 - Wrong JSON types on create

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-018 |
| Feature/Requirement | REQ-003 / REQ-009 |
| Technique/Test Type | EP (data type) / API negative |
| Objective | Non-string title/description values are rejected with 400 JSON, not a 500 page |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | TC-API-018a: `{"title": 123}`<br>TC-API-018b: `{"title": ["a", "b"]}`<br>TC-API-018c: `{"title": "ok", "description": {"a": 1}}` |
| Steps | 1. `POST /api/tasks` (TC-API-018a)<br>2. `POST /api/tasks` (TC-API-018b)<br>3. `POST /api/tasks` (TC-API-018c) |
| Expected Result | TC-API-018a: status is 400; response body is JSON (not an HTML error page)<br>TC-API-018b: status is 400; response body is JSON (not an HTML error page)<br>TC-API-018c: status is 400; response body is JSON (not an HTML error page) |
| Actual Result | TC-API-018a: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page)<br>TC-API-018b: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page)<br>TC-API-018c: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page) |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | DEF-018 |

## TC-API-019 - Invalid due date on create

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-019 |
| Feature/Requirement | REQ-003 / REQ-006 |
| Technique/Test Type | EP (invalid) / API negative |
| Objective | A due date that is not a real YYYY-MM-DD date is rejected and does not affect other endpoints |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "99 Run last - invalid due dates" |
| Test Data | TC-API-019a: `{"title": "bad date", "due_date": "31/12/2026"}`<br>TC-API-019b: `{"title": "bad date", "due_date": "2026-02-30"}`<br>TC-API-019c: `{"title": "bad date", "due_date": "tomorrow"}` |
| Steps | 1. `POST /api/tasks` (TC-API-019a)<br>2. `GET /api/tasks` (TC-API-019a-check1)<br>3. `GET /api/dashboard` (TC-API-019a-check2)<br>4. `POST /api/tasks` (TC-API-019b)<br>5. `GET /api/tasks` (TC-API-019b-check1)<br>6. `GET /api/dashboard` (TC-API-019b-check2)<br>7. `POST /api/tasks` (TC-API-019c)<br>8. `GET /api/tasks` (TC-API-019c-check1)<br>9. `GET /api/dashboard` (TC-API-019c-check2) |
| Expected Result | TC-API-019a: status is 400; response body is JSON (not an HTML error page)<br>TC-API-019a-check1: status is 200<br>TC-API-019a-check2: status is 200<br>TC-API-019b: status is 400; response body is JSON (not an HTML error page)<br>TC-API-019b-check1: status is 200<br>TC-API-019b-check2: status is 200<br>TC-API-019c: status is 400; response body is JSON (not an HTML error page)<br>TC-API-019c-check1: status is 200<br>TC-API-019c-check2: status is 200 |
| Actual Result | TC-API-019a: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page)<br>TC-API-019a-check1: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200<br>TC-API-019a-check2: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200<br>TC-API-019b: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page)<br>TC-API-019b-check1: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200<br>TC-API-019b-check2: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200<br>TC-API-019c: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page)<br>TC-API-019c-check1: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200<br>TC-API-019c-check2: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200 |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-019-invalid-due-date-500-20261124.jpg](evidences/TC-API-019-invalid-due-date-500-20261124.jpg)<br>[TC-API-019c-036f-invalid-due-date-20261124.jpg](evidences/TC-API-019c-036f-invalid-due-date-20261124.jpg)<br>[DEF-015-user-locked-out-after-bad-date-20261124.jpg](evidences/DEF-015-user-locked-out-after-bad-date-20261124.jpg) |
| Defect ID | DEF-015 |

## TC-API-020 - Invalid category on create

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-020 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP (invalid) / API negative |
| Objective | category_id must refer to an existing category |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | TC-API-020a: `{"title": "bad category", "category_id": 999}`<br>TC-API-020b: `{"title": "bad category", "category_id": "abc"}` |
| Steps | 1. `POST /api/tasks` (TC-API-020a)<br>2. `POST /api/tasks` (TC-API-020b) |
| Expected Result | TC-API-020a: status is 400; response body is JSON (not an HTML error page)<br>TC-API-020b: status is 400; response body is JSON (not an HTML error page) |
| Actual Result | TC-API-020a: 201 CREATED - **FAILED:** status is 400<br>TC-API-020b: 201 CREATED - **FAILED:** status is 400 |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-020a-unknown-category-accepted-20261124.jpg](evidences/TC-API-020a-unknown-category-accepted-20261124.jpg) |
| Defect ID | DEF-019 |

## TC-API-021 - Urgency boundaries returned by the API

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-021 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | BVA / API |
| Objective | The API `urgency` field follows the helpers.py specification at each boundary |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | TC-API-021a: `{"title": "urgency yesterday", "due_date": "{{yesterday}}"}`<br>TC-API-021b: `{"title": "urgency today", "due_date": "{{today}}"}`<br>TC-API-021c: `{"title": "urgency plus1", "due_date": "{{plus1}}"}`<br>TC-API-021d: `{"title": "urgency plus2", "due_date": "{{plus2}}"}`<br>TC-API-021e: `{"title": "urgency plus3", "due_date": "{{plus3}}"}` |
| Steps | 1. `POST /api/tasks` (TC-API-021a)<br>2. `POST /api/tasks` (TC-API-021b)<br>3. `POST /api/tasks` (TC-API-021c)<br>4. `POST /api/tasks` (TC-API-021d)<br>5. `POST /api/tasks` (TC-API-021e) |
| Expected Result | TC-API-021a: status is 201; urgency is "Overdue"<br>TC-API-021b: status is 201; urgency is "Due Today"<br>TC-API-021c: status is 201; urgency is "Due Soon"<br>TC-API-021d: status is 201; urgency is "Due Soon"<br>TC-API-021e: status is 201; urgency is "Upcoming" |
| Actual Result | TC-API-021a: 201 CREATED - all checks passed<br>TC-API-021b: 201 CREATED - **FAILED:** urgency is "Due Today"<br>TC-API-021c: 201 CREATED - all checks passed<br>TC-API-021d: 201 CREATED - all checks passed<br>TC-API-021e: 201 CREATED - all checks passed |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-021b-due-today-overdue-20261124.jpg](evidences/TC-API-021b-due-today-overdue-20261124.jpg) |
| Defect ID | DEF-002 |

## TC-API-022 - Read own task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-022 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | API functional |
| Objective | GET by id returns the stored task |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); one task created; Postman folder "03 Create and read tasks" |
| Test Data | - |
| Steps | 1. `GET /api/tasks/{{task_full_id}}` (TC-API-022) |
| Expected Result | TC-API-022: status is 200; same task id; title is 'Prepare W4 report' |
| Actual Result | TC-API-022: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-023 - Read a non-existent task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-023 |
| Feature/Requirement | REQ-003 / REQ-009 |
| Technique/Test Type | EP (invalid id) / API negative |
| Objective | Unknown id returns 404 JSON |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | id `999999999` |
| Steps | 1. `GET /api/tasks/999999999` (TC-API-023) |
| Expected Result | TC-API-023: status is 404; response body is JSON (not an HTML error page); error message is "not found" |
| Actual Result | TC-API-023: 404 NOT FOUND - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-024 - Read another user's task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-024 |
| Feature/Requirement | REQ-008 |
| Technique/Test Type | EP (foreign id) / API negative |
| Objective | A task owned by another user is not disclosed |
| Preconditions | Users A and B registered and logged in, Postman switches between them with SETUP log-in requests; A owns one task; Postman folder "07 One user vs another user's data" |
| Test Data | A's task id |
| Steps | 1. `GET /api/tasks/{{x_id}}` (TC-API-024) |
| Expected Result | TC-API-024: status is 404; response body is JSON (not an HTML error page); error message is "not found"; owner's title is not disclosed |
| Actual Result | TC-API-024: 404 NOT FOUND - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-025 - Non-integer task id

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-025 |
| Feature/Requirement | REQ-009 |
| Technique/Test Type | EP (invalid type) / API negative |
| Objective | A non-numeric id does not match the route |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "03 Create and read tasks" |
| Test Data | `abc` |
| Steps | 1. `GET /api/tasks/abc` (TC-API-025) |
| Expected Result | TC-API-025: status is 404 |
| Actual Result | TC-API-025: 404 NOT FOUND - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-026 - Filter by category

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-026 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / API functional |
| Objective | ?category=Work returns only Work tasks |
| Preconditions | User A logged in with the five-task list dataset ([test_data.md](test_data.md#list-dataset)); Postman folder "04 List, filter, search, paging" |
| Test Data | `category=Work` |
| Steps | 1. `GET /api/tasks?category=Work` (TC-API-026) |
| Expected Result | TC-API-026: status is 200; exactly the two Work tasks |
| Actual Result | TC-API-026: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-027 - Filter by status

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-027 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / API functional |
| Objective | ?status=open and ?status=done return the right partitions |
| Preconditions | User A logged in with the five-task list dataset ([test_data.md](test_data.md#list-dataset)); Postman folder "04 List, filter, search, paging" |
| Test Data | `status=open`, `status=done` |
| Steps | 1. `GET /api/tasks?status=open` (TC-API-027a)<br>2. `GET /api/tasks?status=done` (TC-API-027b) |
| Expected Result | TC-API-027a: status is 200; exactly the four open tasks<br>TC-API-027b: status is 200; exactly the one done task |
| Actual Result | TC-API-027a: 200 OK - all checks passed<br>TC-API-027b: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-028 - Title search

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-028 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / API functional |
| Objective | ?q= returns tasks whose title contains the text |
| Preconditions | User A logged in with the five-task list dataset ([test_data.md](test_data.md#list-dataset)); Postman folder "04 List, filter, search, paging" |
| Test Data | `q=report` |
| Steps | 1. `GET /api/tasks?q=report` (TC-API-028) |
| Expected Result | TC-API-028: status is 200; both titles containing 'report' |
| Actual Result | TC-API-028: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-029 - Combined filters

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-029 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | Decision table / API functional |
| Objective | All active conditions are applied together |
| Preconditions | User A logged in with the five-task list dataset ([test_data.md](test_data.md#list-dataset)); Postman folder "04 List, filter, search, paging" |
| Test Data | `category=Work&status=open&q=report` |
| Steps | 1. `GET /api/tasks?category=Work&status=open&q=report` (TC-API-029) |
| Expected Result | TC-API-029: status is 200; only 'Weekly report' matches all three |
| Actual Result | TC-API-029: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-030 - Search text containing an apostrophe

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-030 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP (special character) / API negative |
| Objective | Search handles a quote character like any other text |
| Preconditions | User A logged in with the five-task list dataset ([test_data.md](test_data.md#list-dataset)); Postman folder "04 List, filter, search, paging" |
| Test Data | `q=O'Brien` |
| Steps | 1. `GET /api/tasks?q=O'Brien` (TC-API-030) |
| Expected Result | TC-API-030: status is 200; returns 'Call O'Brien' |
| Actual Result | TC-API-030: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200; returns 'Call O'Brien' |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-030-apostrophe-search-500-20261124.jpg](evidences/TC-API-030-apostrophe-search-500-20261124.jpg) |
| Defect ID | DEF-017 |

## TC-API-031 - Pagination

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-031 |
| Feature/Requirement | REQ-005 / REQ-009 |
| Technique/Test Type | BVA / API functional |
| Objective | page/per_page split results without overlap; default page size 10, newest first |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); three tasks created in order; Postman folder "04 List, filter, search, paging" |
| Test Data | `per_page=2&page=0`, `per_page=2&page=1`, no parameters |
| Steps | 1. `GET /api/tasks?per_page=2&page=0` (TC-API-031a)<br>2. `GET /api/tasks?per_page=2&page=1` (TC-API-031b)<br>3. `GET /api/tasks?per_page=2&page=2` (TC-API-031c)<br>4. `GET /api/tasks` (TC-API-031d) |
| Expected Result | TC-API-031a: status is 200; two newest tasks, newest first<br>TC-API-031b: status is 200; next two tasks<br>TC-API-031c: status is 200; last task<br>TC-API-031d: status is 200; all five tasks, newest first |
| Actual Result | TC-API-031a: 200 OK - all checks passed<br>TC-API-031b: 200 OK - all checks passed<br>TC-API-031c: 200 OK - all checks passed<br>TC-API-031d: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-032 - Invalid pagination parameters

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-032 |
| Feature/Requirement | REQ-009 |
| Technique/Test Type | EP + BVA (invalid) / API negative |
| Objective | Negative or non-numeric paging values are rejected |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); three tasks; Postman folder "04 List, filter, search, paging" |
| Test Data | `per_page=-1`, `page=-1`, `page=abc` |
| Steps | 1. `GET /api/tasks?per_page=-1` (TC-API-032a)<br>2. `GET /api/tasks?page=-1` (TC-API-032b)<br>3. `GET /api/tasks?page=abc` (TC-API-032c) |
| Expected Result | TC-API-032a: status is 400; response body is JSON (not an HTML error page)<br>TC-API-032b: status is 400; response body is JSON (not an HTML error page)<br>TC-API-032c: status is 400; response body is JSON (not an HTML error page) |
| Actual Result | TC-API-032a: 200 OK - **FAILED:** status is 400<br>TC-API-032b: 200 OK - **FAILED:** status is 400<br>TC-API-032c: 200 OK - **FAILED:** status is 400 |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-032a-paging-not-validated-20261124.jpg](evidences/TC-API-032a-paging-not-validated-20261124.jpg) |
| Defect ID | DEF-022 |

## TC-API-033 - Task list scoped to the user

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-033 |
| Feature/Requirement | REQ-008 |
| Technique/Test Type | EP / API |
| Objective | User B does not see user A's tasks |
| Preconditions | User A logged in with the five-task list dataset ([test_data.md](test_data.md#list-dataset)); user B logged in separately; Postman folder "07 One user vs another user's data" |
| Test Data | - |
| Steps | 1. `GET /api/tasks` (TC-API-033) |
| Expected Result | TC-API-033: status is 200; intruder sees an empty list |
| Actual Result | TC-API-033: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-034 - Partial update

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-034 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | API functional |
| Objective | PUT with one field changes only that field |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); task with all fields; Postman folder "05 Update tasks" |
| Test Data | TC-API-034: `{"title": "New"}` |
| Steps | 1. `PUT /api/tasks/{{u_id}}` (TC-API-034) |
| Expected Result | TC-API-034: status is 200; title is 'New'; description unchanged; category unchanged; due date unchanged; done is false |
| Actual Result | TC-API-034: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-035 - Complete and reopen through the API

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-035 |
| Feature/Requirement | REQ-004 |
| Technique/Test Type | State transition (Open -> Done -> Open) / API |
| Objective | done flag, completed_at and urgency change consistently |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); open task due today-3; Postman folder "05 Update tasks" |
| Test Data | TC-API-035a: `{"done": true}`<br>TC-API-035b: `{"done": false}` |
| Steps | 1. `PUT /api/tasks/{{c_id}}` (TC-API-035a)<br>2. `PUT /api/tasks/{{c_id}}` (TC-API-035b) |
| Expected Result | TC-API-035a: status is 200; done is true; completed_at is set; urgency is 'Done'<br>TC-API-035b: status is 200; done is false; completed_at is null; urgency recomputed (Overdue) |
| Actual Result | TC-API-035a: 200 OK - all checks passed<br>TC-API-035b: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-036 - Invalid values on update

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-036 |
| Feature/Requirement | REQ-003 / REQ-009 |
| Technique/Test Type | EP (invalid) / API negative |
| Objective | PUT applies the same validation as create and leaves the task unchanged on error |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); task `Stable title`; Postman folder "05 Update tasks" |
| Test Data | TC-API-036a: `{"title": ""}`<br>TC-API-036b: `{"title": "   "}`<br>TC-API-036c: `{"done": "false"}`<br>TC-API-036d: `{"title": null}`<br>TC-API-036e: `{"category_id": 999}`<br>TC-API-036f: `{"due_date": "31/12/2026"}` |
| Steps | 1. `PUT /api/tasks/{{s_id}}` (TC-API-036a)<br>2. `GET /api/tasks/{{s_id}}` (TC-API-036a-check)<br>3. `PUT /api/tasks/{{s_id}}` (TC-API-036b)<br>4. `GET /api/tasks/{{s_id}}` (TC-API-036b-check)<br>5. `PUT /api/tasks/{{s_id}}` (TC-API-036c)<br>6. `GET /api/tasks/{{s_id}}` (TC-API-036c-check)<br>7. `PUT /api/tasks/{{s_id}}` (TC-API-036d)<br>8. `GET /api/tasks/{{s_id}}` (TC-API-036d-check)<br>9. `PUT /api/tasks/{{s_id}}` (TC-API-036e)<br>10. `GET /api/tasks/{{s_id}}` (TC-API-036e-check)<br>11. `PUT /api/tasks/{{s_id}}` (TC-API-036f)<br>12. `GET /api/tasks/{{s_id}}` (TC-API-036f-check) |
| Expected Result | TC-API-036a: status is 400; response body is JSON (not an HTML error page)<br>TC-API-036a-check: status is 200; title unchanged; still open; category unchanged<br>TC-API-036b: status is 400; response body is JSON (not an HTML error page)<br>TC-API-036b-check: status is 200; title unchanged; still open; category unchanged<br>TC-API-036c: status is 400; response body is JSON (not an HTML error page)<br>TC-API-036c-check: status is 200; title unchanged; still open; category unchanged<br>TC-API-036d: status is 400; response body is JSON (not an HTML error page)<br>TC-API-036d-check: status is 200; title unchanged; still open; category unchanged<br>TC-API-036e: status is 400; response body is JSON (not an HTML error page)<br>TC-API-036e-check: status is 200; title unchanged; still open; category unchanged<br>TC-API-036f: status is 400; response body is JSON (not an HTML error page)<br>TC-API-036f-check: status is 200; due date unchanged |
| Actual Result | TC-API-036a: 200 OK - **FAILED:** status is 400<br>TC-API-036a-check: 200 OK - **FAILED:** title unchanged<br>TC-API-036b: 200 OK - **FAILED:** status is 400<br>TC-API-036b-check: 200 OK - **FAILED:** title unchanged<br>TC-API-036c: 200 OK - **FAILED:** status is 400<br>TC-API-036c-check: 200 OK - **FAILED:** still open<br>TC-API-036d: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page)<br>TC-API-036d-check: 200 OK - all checks passed<br>TC-API-036e: 200 OK - **FAILED:** status is 400<br>TC-API-036e-check: 200 OK - **FAILED:** category unchanged<br>TC-API-036f: 500 INTERNAL SERVER ERROR - **FAILED:** status is 400; response body is JSON (not an HTML error page)<br>TC-API-036f-check: 500 INTERNAL SERVER ERROR - **FAILED:** status is 200; due date unchanged |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-036a-d-update-not-validated-20261124.jpg](evidences/TC-API-036a-d-update-not-validated-20261124.jpg)<br>[TC-API-036e-update-unknown-category-20261124.jpg](evidences/TC-API-036e-update-unknown-category-20261124.jpg)<br>[TC-API-019c-036f-invalid-due-date-20261124.jpg](evidences/TC-API-019c-036f-invalid-due-date-20261124.jpg) |
| Defect ID | DEF-015, DEF-018, DEF-019, DEF-020 |

## TC-API-037 - Update another user's task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-037 |
| Feature/Requirement | REQ-008 |
| Technique/Test Type | EP (foreign id) / API negative |
| Objective | User B cannot change A's task |
| Preconditions | Users A and B registered and logged in, Postman switches between them with SETUP log-in requests; A owns one task; Postman folder "07 One user vs another user's data" |
| Test Data | TC-API-037a: `{"title": "hijacked"}` |
| Steps | 1. `PUT /api/tasks/{{x_id}}` (TC-API-037a)<br>2. `GET /api/tasks/{{x_id}}` (TC-API-037b) |
| Expected Result | TC-API-037a: status is 404; response body is JSON (not an HTML error page); error message is "not found"<br>TC-API-037b: status is 200; title unchanged |
| Actual Result | TC-API-037a: 404 NOT FOUND - all checks passed<br>TC-API-037b: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-038 - Update a non-existent task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-038 |
| Feature/Requirement | REQ-009 |
| Technique/Test Type | EP (invalid id) / API negative |
| Objective | Unknown id returns 404 |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "05 Update tasks" |
| Test Data | TC-API-038: `{"title": "x"}` |
| Steps | 1. `PUT /api/tasks/999999999` (TC-API-038) |
| Expected Result | TC-API-038: status is 404; response body is JSON (not an HTML error page); error message is "not found" |
| Actual Result | TC-API-038: 404 NOT FOUND - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-039 - Delete own task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-039 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | State transition (exists -> deleted) / API |
| Objective | Delete removes the task |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); one task; Postman folder "06 Delete tasks" |
| Test Data | - |
| Steps | 1. `DELETE /api/tasks/{{d_id}}` (TC-API-039a)<br>2. `GET /api/tasks/{{d_id}}` (TC-API-039b) |
| Expected Result | TC-API-039a: status is 200; body is {"result": "ok"}<br>TC-API-039b: status is 404 |
| Actual Result | TC-API-039a: 200 OK - all checks passed<br>TC-API-039b: 404 NOT FOUND - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-040 - Delete another user's task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-040 |
| Feature/Requirement | REQ-008 |
| Technique/Test Type | EP (foreign id) / API negative |
| Objective | User B cannot delete A's task (GET and PUT already enforce ownership) |
| Preconditions | Users A and B registered and logged in, Postman switches between them with SETUP log-in requests; A owns one task; Postman folder "07 One user vs another user's data" |
| Test Data | A's task id |
| Steps | 1. `DELETE /api/tasks/{{x_id}}` (TC-API-040a)<br>2. `GET /api/tasks/{{x_id}}` (TC-API-040b) |
| Expected Result | TC-API-040a: status is 404 (not the intruder's task)<br>TC-API-040b: status is 200 (task was not deleted) |
| Actual Result | TC-API-040a: 200 OK - **FAILED:** status is 404 (not the intruder's task)<br>TC-API-040b: 404 NOT FOUND - **FAILED:** status is 200 (task was not deleted) |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-040-cross-user-delete-20261124.jpg](evidences/TC-API-040-cross-user-delete-20261124.jpg) |
| Defect ID | DEF-014 |

## TC-API-041 - Delete a non-existent task

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-041 |
| Feature/Requirement | REQ-009 |
| Technique/Test Type | EP (invalid id) / API negative |
| Objective | Deleting nothing is reported as not found |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); Postman folder "06 Delete tasks" |
| Test Data | id `999999999` |
| Steps | 1. `DELETE /api/tasks/999999999` (TC-API-041) |
| Expected Result | TC-API-041: status is 404; response body is JSON (not an HTML error page); error message is "not found" |
| Actual Result | TC-API-041: 200 OK - **FAILED:** status is 404; error message is "not found" |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json)<br>[TC-API-041-delete-nonexistent-200-20261124.jpg](evidences/TC-API-041-delete-nonexistent-200-20261124.jpg) |
| Defect ID | DEF-021 |

## TC-API-042 - Dashboard counts with a controlled dataset

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-042 |
| Feature/Requirement | REQ-007 |
| Technique/Test Type | API functional (oracle: independent count) |
| Objective | Each counter matches an independent count of the dataset |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); [dashboard dataset](test_data.md#dashboard-dataset); Postman folder "08 Dashboard" |
| Test Data | 5 tasks: today-1, today+1, today+5, no date, one completed |
| Steps | 1. `GET /api/dashboard` (TC-API-042) |
| Expected Result | TC-API-042: status is 200; total 5, open 4, overdue 1, due_soon 1, completed_this_week 1 |
| Actual Result | TC-API-042: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-043 - Task due today is not overdue on the dashboard

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-043 |
| Feature/Requirement | REQ-006 / REQ-007 |
| Technique/Test Type | BVA / API |
| Objective | The overdue counter excludes a task due today |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); one open task due today; Postman folder "08 Dashboard" |
| Test Data | - |
| Steps | 1. `GET /api/dashboard` (TC-API-043) |
| Expected Result | TC-API-043: status is 200; total is 6; overdue is still 1 |
| Actual Result | TC-API-043: 200 OK - **FAILED:** overdue is still 1 |
| Status | Fail |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | DEF-002 |

## TC-API-044 - Dashboard scoped to the user

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-044 |
| Feature/Requirement | REQ-008 |
| Technique/Test Type | EP / API |
| Objective | User B's counters ignore A's tasks |
| Preconditions | Users A and B registered and logged in, Postman switches between them with SETUP log-in requests; A has two tasks; Postman folder "07 One user vs another user's data" |
| Test Data | - |
| Steps | 1. `GET /api/dashboard` (TC-API-044) |
| Expected Result | TC-API-044: status is 200; all counters are zero |
| Actual Result | TC-API-044: 200 OK - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

## TC-API-045 - Unsupported HTTP method

| Field | Value |
| --- | --- |
| Test Case ID | TC-API-045 |
| Feature/Requirement | REQ-009 |
| Technique/Test Type | EP (invalid method) / API negative |
| Objective | Methods not offered by the route are refused with 405 |
| Preconditions | User A logged in (Postman session from the folder's SETUP requests); one task; Postman folder "09 HTTP method" |
| Test Data | TC-API-045: `{"title": "x"}` |
| Steps | 1. `PATCH /api/tasks/{{p_id}}` (TC-API-045) |
| Expected Result | TC-API-045: status is 405 |
| Actual Result | TC-API-045: 405 METHOD NOT ALLOWED - all checks passed |
| Status | Pass |
| Evidence | [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) |
| Defect ID | - |

---

# Appendix E - Week 5 security and performance cases

**Pending.** Paste the W5 case tables here unchanged once `05_Security_Performance/` is complete and reviewed.

---

# Appendix F - Week 6 automated cases (normalised)

Source: `06_Automation_Regression/README.md`, Task 3 (traceability table) and Task 4; application commit `9cc1f34`; baseline run 2026-11-20, Edge 157 headless, run 1 (`evidences/runs/20261120-210226-edge-full-run1/`). W6 Task 3 is a traceability table, so Preconditions, Test Data and Steps are generic and the scripts hold the detail. These cases re-run W1 scope (and part of W3's GUI scope) and are not added to the 124 designed cases.

## TC-AUT-001 - test_username_length_boundaries

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-001 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-001, 002, 003, 004, 005, 006 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_01_auth.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_01_auth :: test_username_length_boundaries` |
| Expected Result | The specified result of TC-BB-001, 002, 003, 004, 005, 006; no assertion was changed to match current behaviour |
| Actual Result | 6 Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-002 - test_password_length_boundaries

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-002 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-007, 008, 009; TC-GUI-004 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_01_auth.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_01_auth :: test_password_length_boundaries` |
| Expected Result | The specified result of TC-BB-007, 008, 009; TC-GUI-004; no assertion was changed to match current behaviour |
| Actual Result | 2 Pass, TC-BB-008 Fail (known) (run 1, 2026-11-20) |
| Status | Pass and Fail (known defect) |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | DEF-001 |

## TC-AUT-003 - test_valid_registration_opens_task_list

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-003 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-010 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_01_auth.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_01_auth :: test_valid_registration_opens_task_list` |
| Expected Result | The specified result of TC-BB-010; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-004 - test_username_with_hyphen_is_rejected

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-004 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-011 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_01_auth.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_01_auth :: test_username_with_hyphen_is_rejected` |
| Expected Result | The specified result of TC-BB-011; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-005 - test_empty_registration_field_blocked_by_browser

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-005 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | EP / browser validation; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-012, 013 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_01_auth.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_01_auth :: test_empty_registration_field_blocked_by_browser` |
| Expected Result | The specified result of TC-BB-012, 013; no assertion was changed to match current behaviour |
| Actual Result | 2 Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-006 - test_login_decision_table

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-006 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | Decision table; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-014, 015, 016, 017; TC-GUI-002 (text only) |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_01_auth.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_01_auth :: test_login_decision_table` |
| Expected Result | The specified result of TC-BB-014, 015, 016, 017; TC-GUI-002 (text only); no assertion was changed to match current behaviour |
| Actual Result | 4 Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-007 - test_protected_page_redirects_when_logged_out

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-007 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | State transition; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-018 (extended to 3 pages) |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_01_auth.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_01_auth :: test_protected_page_redirects_when_logged_out` |
| Expected Result | The specified result of TC-BB-018 (extended to 3 pages); no assertion was changed to match current behaviour |
| Actual Result | 3 Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-008 - test_logout_revokes_protected_page_access

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-008 |
| Feature/Requirement | REQ-002 |
| Technique/Test Type | State transition; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-019 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_01_auth.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_01_auth :: test_logout_revokes_protected_page_access` |
| Expected Result | The specified result of TC-BB-019; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-009 - test_create_full_field_task_persists

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-009 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-020 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_create_full_field_task_persists` |
| Expected Result | The specified result of TC-BB-020; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-010 - test_create_title_only_task

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-010 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-021 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_create_title_only_task` |
| Expected Result | The specified result of TC-BB-021; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-011 - test_empty_title_blocked_by_browser

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-011 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP / browser validation; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-022 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_empty_title_blocked_by_browser` |
| Expected Result | The specified result of TC-BB-022; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-012 - test_whitespace_only_title_rejected

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-012 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | EP / input validation; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-023; TC-GUI-016 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_whitespace_only_title_rejected` |
| Expected Result | The specified result of TC-BB-023; TC-GUI-016; no assertion was changed to match current behaviour |
| Actual Result | Fail (known) (run 1, 2026-11-20) |
| Status | Fail (known defect) |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | DEF-003 |

## TC-AUT-013 - test_edit_persists_all_fields

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-013 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Functional; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-024; TC-GUI-012, 015 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_edit_persists_all_fields` |
| Expected Result | The specified result of TC-BB-024; TC-GUI-012, 015; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-014 - test_cancel_edit_preserves_saved_data

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-014 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | State transition; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-025 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_cancel_edit_preserves_saved_data` |
| Expected Result | The specified result of TC-BB-025; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-015 - test_cancel_deletion_retains_task

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-015 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | State transition; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-026; TC-GUI-013 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_cancel_deletion_retains_task` |
| Expected Result | The specified result of TC-BB-026; TC-GUI-013; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-016 - test_confirm_deletion_removes_only_that_task

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-016 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | State transition; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-027; TC-GUI-013 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_confirm_deletion_removes_only_that_task` |
| Expected Result | The specified result of TC-BB-027; TC-GUI-013; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-017 - test_complete_then_reopen_task

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-017 |
| Feature/Requirement | REQ-004 |
| Technique/Test Type | State transition; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-028, 029; TC-GUI-011 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_complete_then_reopen_task` |
| Expected Result | The specified result of TC-BB-028, 029; TC-GUI-011; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-018 - test_special_characters_preserved_in_edit_form

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-018 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Functional; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-GUI-020 (edit form) |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_special_characters_preserved_in_edit_form` |
| Expected Result | The specified result of TC-GUI-020 (edit form); no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-019 - test_special_characters_displayed_literally_in_list

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-019 |
| Feature/Requirement | REQ-003 |
| Technique/Test Type | Functional; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-GUI-020 (list) |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_special_characters_displayed_literally_in_list` |
| Expected Result | The specified result of TC-GUI-020 (list); no assertion was changed to match current behaviour |
| Actual Result | Fail (known) (run 1, 2026-11-20) |
| Status | Fail (known defect) |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | DEF-005 |

## TC-AUT-020 - test_each_account_sees_only_its_own_tasks

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-020 |
| Feature/Requirement | REQ-008 |
| Technique/Test Type | EP; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-044 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_02_tasks.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_02_tasks :: test_each_account_sees_only_its_own_tasks` |
| Expected Result | The specified result of TC-BB-044; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-021 - test_filters_return_only_matching_tasks

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-021 |
| Feature/Requirement | REQ-005 |
| Technique/Test Type | EP / decision table; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-030, 031, 032, 033, 034, 035; TC-GUI-008 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_03_filters.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_03_filters :: test_filters_return_only_matching_tasks` |
| Expected Result | The specified result of TC-BB-030, 031, 032, 033, 034, 035; TC-GUI-008; no assertion was changed to match current behaviour |
| Actual Result | 6 Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-022 - test_urgency_label

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-022 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | BVA; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-036, 037, 038, 039, 040, 041; TC-GUI-010 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_04_urgency_dashboard.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_04_urgency_dashboard :: test_urgency_label` |
| Expected Result | The specified result of TC-BB-036, 037, 038, 039, 040, 041; TC-GUI-010; no assertion was changed to match current behaviour |
| Actual Result | 5 Pass, TC-BB-038 Fail (known) (run 1, 2026-11-20) |
| Status | Pass and Fail (known defect) |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | DEF-002 |

## TC-AUT-023 - test_completion_overrides_overdue

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-023 |
| Feature/Requirement | REQ-004, REQ-006 |
| Technique/Test Type | State transition; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-042 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_04_urgency_dashboard.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_04_urgency_dashboard :: test_completion_overrides_overdue` |
| Expected Result | The specified result of TC-BB-042; no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-024 - test_dashboard_counters_unaffected_by_def002

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-024 |
| Feature/Requirement | REQ-007 |
| Technique/Test Type | Independent calculation; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-043 (Total, Open, Due Soon, Completed) |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_04_urgency_dashboard.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_04_urgency_dashboard :: test_dashboard_counters_unaffected_by_def002` |
| Expected Result | The specified result of TC-BB-043 (Total, Open, Due Soon, Completed); no assertion was changed to match current behaviour |
| Actual Result | Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-025 - test_dashboard_overdue_counter

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-025 |
| Feature/Requirement | REQ-007 |
| Technique/Test Type | Independent calculation; automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-043 (Overdue) |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_04_urgency_dashboard.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_04_urgency_dashboard :: test_dashboard_overdue_counter` |
| Expected Result | The specified result of TC-BB-043 (Overdue); no assertion was changed to match current behaviour |
| Actual Result | Fail (known) (run 1, 2026-11-20) |
| Status | Fail (known defect) |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | DEF-002 |

## TC-AUT-026 - test_username_rule

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-026 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA / EP (unit); automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-001 to 006, 010, 011 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_05_rules_unit.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_05_rules_unit :: test_username_rule` |
| Expected Result | The specified result of TC-BB-001 to 006, 010, 011; no assertion was changed to match current behaviour |
| Actual Result | 8 Pass (run 1, 2026-11-20) |
| Status | Pass |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | - |

## TC-AUT-027 - test_password_rule

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-027 |
| Feature/Requirement | REQ-001 |
| Technique/Test Type | BVA (unit); automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-007, 008, 009 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_05_rules_unit.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_05_rules_unit :: test_password_rule` |
| Expected Result | The specified result of TC-BB-007, 008, 009; no assertion was changed to match current behaviour |
| Actual Result | 2 Pass, TC-BB-008 Fail (known) (run 1, 2026-11-20) |
| Status | Pass and Fail (known defect) |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | DEF-001 |

## TC-AUT-028 - test_urgency_rule

| Field | Value |
| --- | --- |
| Test Case ID | TC-AUT-028 |
| Feature/Requirement | REQ-006 |
| Technique/Test Type | BVA (unit); automated (pytest + Selenium, or rule-level pytest) |
| Objective | Re-check the specified result of manual case(s) TC-BB-036 to 041 |
| Preconditions | Isolated `app.py` on a temporary SQLite database (port 5006); accounts and fixtures seeded through the JSON API; due dates relative to the run day |
| Test Data | Defined in `test_05_rules_unit.py` (parametrised rows use the manual case ID) |
| Steps | 1. Run `pytest` on `test_05_rules_unit :: test_urgency_rule` |
| Expected Result | The specified result of TC-BB-036 to 041; no assertion was changed to match current behaviour |
| Actual Result | 5 Pass, TC-BB-038 Fail (known) (run 1, 2026-11-20) |
| Status | Pass and Fail (known defect) |
| Evidence | `results.md`, `pytest.log` and `screenshots/` in the run folder |
| Defect ID | DEF-002 |
