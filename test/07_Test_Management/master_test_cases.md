# Master Test-Case Repository

Consolidated test cases for **PyTodo Pro** (Weeks 1-6), in the course 12-field test-case template (`Test Case ID`, `Feature/Requirement`, `Technique/Test Type`, `Objective`, `Preconditions`, `Test Data`, `Steps`, `Expected Result`, `Actual Result`, `Status`, `Evidence`, `Defect ID`).

**Rule: results are never edited here.** A correction is made in the source week's file and then copied again. Appendices A and D are verbatim copies; Appendices B and F were normalised to the template (original IDs kept in a `Source ID` column).

## 1. Repository summary

| Week | Phase | Source file | ID range | Designed cases | Execution units | Status of this repository |
| --- | --- | --- | --- | --- | --- | --- |
| W1 | Black-box | `01_Black_Box/test_cases.md` | `TC-BB-001` to `044` | 44 | 44 (40 Pass, 4 Fail) | Copied verbatim (Appendix A) |
| W2 | White-box | `02_White_Box_Coverage/README.md`, Tables 4-6a | `TC-WB-*` (19 basis-path cases) | 19 | 50 pytest instances (all Pass): 30 backend + 20 helper | Normalised (Appendix B) |
| W3 | GUI, compatibility, usability, accessibility | `03_Special_Testing/` | `TC-GUI-001` to `022`, `TC-CMP-001` to `008`, `TC-USA-001` to `005`, `TC-A11Y-001` to `018` | 53 (to verify) | TBD | **Pending**: not complete (Appendix C) |
| W4 | Web and API | `04_Web_API/test_cases.md` | `TC-WEB-001` to `016`, `TC-API-001` to `045` | 61 | 61 (43 Pass, 18 Fail) | Copied verbatim (Appendix D) |
| W5 | Security and performance | `05_Security_Performance/` | TBD | TBD | TBD | **Pending**: not complete (Appendix E) |
| W6 | Automation and regression | `06_Automation_Regression/README.md`, Task 3 | `TC-AUT-001` to `028` | 28 (not counted as new scope) | 65 pytest checks (58 Pass, 7 Fail known) | Normalised (Appendix F) |
| **Total (W1, W2, W4)** | | | | **124 designed** | **155 execution units** (44 + 50 + 61); W6's 65 checks are reported separately | In progress until W3 and W5 are merged |

The 155 figure counts execution units because W2's 19 designed path cases run as 50 pytest instances. The index below lists the 124 designed cases (44 + 19 + 61) plus the 28 W6 automated cases.

**Source commits.** Record the commit of each source file when it is copied: W1 `TBD`, W2 `TBD`, W4 `TBD`, W6 `TBD` (`git rev-parse --short HEAD` on the source branch). Application commits tested: W4 `fc0767f`, W6 `9cc1f34`.

## 2. Master index

Status values: Pass, Fail, Blocked, Not Run. Requirement mapping for W2 was made by the Defect & Metrics Coordinator (the W2 report names none) and needs W2 author sign-off.

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

Pending. 53 cases to merge (`TC-GUI-001` to `022`, `TC-CMP-001` to `008`, `TC-USA-001` to `005`, `TC-A11Y-001` to `018`). Week 6 records TC-USA-001 to 005 as Not Run (human review) and only compatibility configurations C01-C04 as executed; confirm against the W3 report.

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

### 2.6 Week 6 - Automated regression cases (Appendix F; not counted in the 124)

| Case ID | Script :: test | Manual case(s) covered | Requirement | Checks | Status | Defect |
| --- | --- | --- | --- | --- | --- | --- |
| [TC-AUT-001](#tc-aut-001) | test_01_auth :: test_username_length_boundaries | TC-BB-001, 002, 003, 004, 005, 006 | REQ-001 |  | Pass | 6 Pass |
| [TC-AUT-002](#tc-aut-002) | test_01_auth :: test_password_length_boundaries | TC-BB-007, 008, 009; TC-GUI-004 | REQ-001 |  | Pass and Fail (known defect) | 2 Pass, TC-BB-008 Fail (known) |
| [TC-AUT-003](#tc-aut-003) | test_01_auth :: test_valid_registration_opens_task_list | TC-BB-010 | REQ-001 | S | Pass | Pass |
| [TC-AUT-004](#tc-aut-004) | test_01_auth :: test_username_with_hyphen_is_rejected | TC-BB-011 | REQ-001 |  | Pass | Pass |
| [TC-AUT-005](#tc-aut-005) | test_01_auth :: test_empty_registration_field_blocked_by_browser | TC-BB-012, 013 | REQ-001 |  | Pass | 2 Pass |
| [TC-AUT-006](#tc-aut-006) | test_01_auth :: test_login_decision_table | TC-BB-014, 015, 016, 017; TC-GUI-002 (text only) | REQ-002 | S (rule 1) | Pass | 4 Pass |
| [TC-AUT-007](#tc-aut-007) | test_01_auth :: test_protected_page_redirects_when_logged_out | TC-BB-018 (extended to 3 pages) | REQ-002 | S | Pass | 3 Pass |
| [TC-AUT-008](#tc-aut-008) | test_01_auth :: test_logout_revokes_protected_page_access | TC-BB-019 | REQ-002 | S | Pass | Pass |
| [TC-AUT-009](#tc-aut-009) | test_02_tasks :: test_create_full_field_task_persists | TC-BB-020 | REQ-003 | S | Pass | Pass |
| [TC-AUT-010](#tc-aut-010) | test_02_tasks :: test_create_title_only_task | TC-BB-021 | REQ-003 |  | Pass | Pass |
| [TC-AUT-011](#tc-aut-011) | test_02_tasks :: test_empty_title_blocked_by_browser | TC-BB-022 | REQ-003 |  | Pass | Pass |
| [TC-AUT-012](#tc-aut-012) | test_02_tasks :: test_whitespace_only_title_rejected | TC-BB-023; TC-GUI-016 | REQ-003 |  | Fail (known defect) | Fail (known) |
| [TC-AUT-013](#tc-aut-013) | test_02_tasks :: test_edit_persists_all_fields | TC-BB-024; TC-GUI-012, 015 | REQ-003 |  | Pass | Pass |
| [TC-AUT-014](#tc-aut-014) | test_02_tasks :: test_cancel_edit_preserves_saved_data | TC-BB-025 | REQ-003 |  | Pass | Pass |
| [TC-AUT-015](#tc-aut-015) | test_02_tasks :: test_cancel_deletion_retains_task | TC-BB-026; TC-GUI-013 | REQ-003 |  | Pass | Pass |
| [TC-AUT-016](#tc-aut-016) | test_02_tasks :: test_confirm_deletion_removes_only_that_task | TC-BB-027; TC-GUI-013 | REQ-003 | S | Pass | Pass |
| [TC-AUT-017](#tc-aut-017) | test_02_tasks :: test_complete_then_reopen_task | TC-BB-028, 029; TC-GUI-011 | REQ-004 | S | Pass | Pass |
| [TC-AUT-018](#tc-aut-018) | test_02_tasks :: test_special_characters_preserved_in_edit_form | TC-GUI-020 (edit form) | REQ-003 |  | Pass | Pass |
| [TC-AUT-019](#tc-aut-019) | test_02_tasks :: test_special_characters_displayed_literally_in_list | TC-GUI-020 (list) | REQ-003 |  | Fail (known defect) | Fail (known) |
| [TC-AUT-020](#tc-aut-020) | test_02_tasks :: test_each_account_sees_only_its_own_tasks | TC-BB-044 | REQ-008 | S | Pass | Pass |
| [TC-AUT-021](#tc-aut-021) | test_03_filters :: test_filters_return_only_matching_tasks | TC-BB-030, 031, 032, 033, 034, 035; TC-GUI-008 | REQ-005 | S (035) | Pass | 6 Pass |
| [TC-AUT-022](#tc-aut-022) | test_04_urgency_dashboard :: test_urgency_label | TC-BB-036, 037, 038, 039, 040, 041; TC-GUI-010 | REQ-006 |  | Pass and Fail (known defect) | 5 Pass, TC-BB-038 Fail (known) |
| [TC-AUT-023](#tc-aut-023) | test_04_urgency_dashboard :: test_completion_overrides_overdue | TC-BB-042 | REQ-004, REQ-006 |  | Pass | Pass |
| [TC-AUT-024](#tc-aut-024) | test_04_urgency_dashboard :: test_dashboard_counters_unaffected_by_def002 | TC-BB-043 (Total, Open, Due Soon, Completed) | REQ-007 |  | Pass | Pass |
| [TC-AUT-025](#tc-aut-025) | test_04_urgency_dashboard :: test_dashboard_overdue_counter | TC-BB-043 (Overdue) | REQ-007 |  | Fail (known defect) | Fail (known) |
| [TC-AUT-026](#tc-aut-026) | test_05_rules_unit :: test_username_rule | TC-BB-001 to 006, 010, 011 | REQ-001 |  | Pass | 8 Pass |
| [TC-AUT-027](#tc-aut-027) | test_05_rules_unit :: test_password_rule | TC-BB-007, 008, 009 | REQ-001 |  | Pass and Fail (known defect) | 2 Pass, TC-BB-008 Fail (known) |
| [TC-AUT-028](#tc-aut-028) | test_05_rules_unit :: test_urgency_rule | TC-BB-036 to 041 | REQ-006 |  | Pass and Fail (known defect) | 5 Pass, TC-BB-038 Fail (known) |

Counts by status (designed cases W1, W2, W4): **Pass 102, Fail 22, Blocked 0, Not Run 0** of 124.

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

# Appendix C - Week 3 special-testing cases

**Pending.** Paste the W3 case tables here unchanged once `03_Special_Testing/` is complete and reviewed.

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
| Defect ID | 6 Pass |

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
| Defect ID | 2 Pass, TC-BB-008 Fail (known) |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | 2 Pass |

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
| Defect ID | 4 Pass |

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
| Defect ID | 3 Pass |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Fail (known) |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Fail (known) |

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
| Defect ID | Pass |

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
| Defect ID | 6 Pass |

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
| Defect ID | 5 Pass, TC-BB-038 Fail (known) |

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
| Defect ID | Pass |

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
| Defect ID | Pass |

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
| Defect ID | Fail (known) |

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
| Defect ID | 8 Pass |

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
| Defect ID | 2 Pass, TC-BB-008 Fail (known) |

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
| Defect ID | 5 Pass, TC-BB-038 Fail (known) |
