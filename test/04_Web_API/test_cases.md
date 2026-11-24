# Week 4 - Detailed Web and API Test Cases

Every case uses the course test-case template. Each case is one or more requests in the Postman collection (`postman/PyTodo_Pro_Week4.postman_collection.json`); the request names start with the case ID. **Expected Result** lists the checks written in the collection before execution. **Actual Result** and **Status** come from the full Collection Runner run on 2026-11-24 13:41 (+08:00), saved as [`evidences/postman-run-full-20261124.json`](evidences/postman-run-full-20261124.json). A case fails if any of its checks fails.

**61 cases: 43 Pass, 18 Fail, 0 Blocked, 0 Not Run.**

## Index

| Case | Title | Postman folder | Status | Defect |
| --- | --- | --- | --- | --- |
| [TC-WEB-001](#tc-web-001---register-through-the-web-form) | Register through the web form | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-002](#tc-web-002---registration-validated-on-the-server) | Registration validated on the server | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-003](#tc-web-003---login-through-the-web-form) | Login through the web form | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-004](#tc-web-004---protected-pages-redirect-when-logged-out) | Protected pages redirect when logged out | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-005](#tc-web-005---web-created-task-matches-the-api) | Web-created task matches the API | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-006](#tc-web-006---api-created-task-matches-the-web-list) | API-created task matches the web list | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-007](#tc-web-007---web-edit-matches-the-api) | Web edit matches the API | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-008](#tc-web-008---web-toggle-matches-the-api) | Web toggle matches the API | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-009](#tc-web-009---web-delete-matches-the-api) | Web delete matches the API | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-010](#tc-web-010---blank-title-validated-on-the-server) | Blank title validated on the server | 10 Web forms (server-side validation, UI vs API) | Fail | DEF-003 |
| [TC-WEB-011](#tc-web-011---due-date-validated-on-the-server) | Due date validated on the server | 99 Run last - invalid due dates | Fail | DEF-015 |
| [TC-WEB-012](#tc-web-012---category-validated-on-the-server) | Category validated on the server | 10 Web forms (server-side validation, UI vs API) | Fail | DEF-019 |
| [TC-WEB-013](#tc-web-013---web-actions-on-another-users-task) | Web actions on another user's task | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-014](#tc-web-014---web-dashboard-matches-the-api-dashboard) | Web dashboard matches the API dashboard | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-015](#tc-web-015---web-search-with-an-apostrophe) | Web search with an apostrophe | 10 Web forms (server-side validation, UI vs API) | Pass | - |
| [TC-WEB-016](#tc-web-016---duplicate-username-on-the-web-form) | Duplicate username on the web form | 10 Web forms (server-side validation, UI vs API) | Fail | DEF-016 |
| [TC-API-001](#tc-api-001---register-a-valid-account) | Register a valid account | 01 Registration and login | Pass | - |
| [TC-API-002](#tc-api-002---username-valid-length-boundaries-3-20) | Username valid length boundaries (3, 20) | 01 Registration and login | Pass | - |
| [TC-API-003](#tc-api-003---invalid-username-partitions) | Invalid username partitions | 01 Registration and login | Pass | - |
| [TC-API-004](#tc-api-004---password-length-7-rejected) | Password length 7 rejected | 01 Registration and login | Pass | - |
| [TC-API-005](#tc-api-005---password-length-8-accepted) | Password length 8 accepted | 01 Registration and login | Fail | DEF-001 |
| [TC-API-006](#tc-api-006---missing-password-rejected) | Missing password rejected | 01 Registration and login | Pass | - |
| [TC-API-007](#tc-api-007---username-of-the-wrong-json-type) | Username of the wrong JSON type | 01 Registration and login | Fail | DEF-018 |
| [TC-API-008](#tc-api-008---duplicate-username-rejected) | Duplicate username rejected | 01 Registration and login | Fail | DEF-016 |
| [TC-API-009](#tc-api-009---login-with-valid-credentials) | Login with valid credentials | 01 Registration and login | Pass | - |
| [TC-API-010](#tc-api-010---login-with-invalid-credentials) | Login with invalid credentials | 01 Registration and login | Pass | - |
| [TC-API-011](#tc-api-011---protected-endpoints-require-a-session) | Protected endpoints require a session | 02 Authentication required | Pass | - |
| [TC-API-012](#tc-api-012---categories-endpoint-requires-a-session) | Categories endpoint requires a session | 02 Authentication required | Fail | DEF-023 |
| [TC-API-013](#tc-api-013---list-categories) | List categories | 02 Authentication required | Pass | - |
| [TC-API-014](#tc-api-014---create-a-task-with-all-fields) | Create a task with all fields | 03 Create and read tasks | Pass | - |
| [TC-API-015](#tc-api-015---create-a-title-only-task) | Create a title-only task | 03 Create and read tasks | Pass | - |
| [TC-API-016](#tc-api-016---title-required) | Title required | 03 Create and read tasks | Pass | - |
| [TC-API-017](#tc-api-017---non-json-request-body) | Non-JSON request body | 03 Create and read tasks | Pass | - |
| [TC-API-018](#tc-api-018---wrong-json-types-on-create) | Wrong JSON types on create | 03 Create and read tasks | Fail | DEF-018 |
| [TC-API-019](#tc-api-019---invalid-due-date-on-create) | Invalid due date on create | 99 Run last - invalid due dates | Fail | DEF-015 |
| [TC-API-020](#tc-api-020---invalid-category-on-create) | Invalid category on create | 03 Create and read tasks | Fail | DEF-019 |
| [TC-API-021](#tc-api-021---urgency-boundaries-returned-by-the-api) | Urgency boundaries returned by the API | 03 Create and read tasks | Fail | DEF-002 |
| [TC-API-022](#tc-api-022---read-own-task) | Read own task | 03 Create and read tasks | Pass | - |
| [TC-API-023](#tc-api-023---read-a-non-existent-task) | Read a non-existent task | 03 Create and read tasks | Pass | - |
| [TC-API-024](#tc-api-024---read-another-users-task) | Read another user's task | 07 One user vs another user's data | Pass | - |
| [TC-API-025](#tc-api-025---non-integer-task-id) | Non-integer task id | 03 Create and read tasks | Pass | - |
| [TC-API-026](#tc-api-026---filter-by-category) | Filter by category | 04 List, filter, search, paging | Pass | - |
| [TC-API-027](#tc-api-027---filter-by-status) | Filter by status | 04 List, filter, search, paging | Pass | - |
| [TC-API-028](#tc-api-028---title-search) | Title search | 04 List, filter, search, paging | Pass | - |
| [TC-API-029](#tc-api-029---combined-filters) | Combined filters | 04 List, filter, search, paging | Pass | - |
| [TC-API-030](#tc-api-030---search-text-containing-an-apostrophe) | Search text containing an apostrophe | 04 List, filter, search, paging | Fail | DEF-017 |
| [TC-API-031](#tc-api-031---pagination) | Pagination | 04 List, filter, search, paging | Pass | - |
| [TC-API-032](#tc-api-032---invalid-pagination-parameters) | Invalid pagination parameters | 04 List, filter, search, paging | Fail | DEF-022 |
| [TC-API-033](#tc-api-033---task-list-scoped-to-the-user) | Task list scoped to the user | 07 One user vs another user's data | Pass | - |
| [TC-API-034](#tc-api-034---partial-update) | Partial update | 05 Update tasks | Pass | - |
| [TC-API-035](#tc-api-035---complete-and-reopen-through-the-api) | Complete and reopen through the API | 05 Update tasks | Pass | - |
| [TC-API-036](#tc-api-036---invalid-values-on-update) | Invalid values on update | 05 Update tasks | Fail | DEF-015, DEF-018, DEF-019, DEF-020 |
| [TC-API-037](#tc-api-037---update-another-users-task) | Update another user's task | 07 One user vs another user's data | Pass | - |
| [TC-API-038](#tc-api-038---update-a-non-existent-task) | Update a non-existent task | 05 Update tasks | Pass | - |
| [TC-API-039](#tc-api-039---delete-own-task) | Delete own task | 06 Delete tasks | Pass | - |
| [TC-API-040](#tc-api-040---delete-another-users-task) | Delete another user's task | 07 One user vs another user's data | Fail | DEF-014 |
| [TC-API-041](#tc-api-041---delete-a-non-existent-task) | Delete a non-existent task | 06 Delete tasks | Fail | DEF-021 |
| [TC-API-042](#tc-api-042---dashboard-counts-with-a-controlled-dataset) | Dashboard counts with a controlled dataset | 08 Dashboard | Pass | - |
| [TC-API-043](#tc-api-043---task-due-today-is-not-overdue-on-the-dashboard) | Task due today is not overdue on the dashboard | 08 Dashboard | Fail | DEF-002 |
| [TC-API-044](#tc-api-044---dashboard-scoped-to-the-user) | Dashboard scoped to the user | 07 One user vs another user's data | Pass | - |
| [TC-API-045](#tc-api-045---unsupported-http-method) | Unsupported HTTP method | 09 HTTP method | Pass | - |

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
