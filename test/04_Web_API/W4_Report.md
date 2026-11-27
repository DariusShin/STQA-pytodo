# Week 4 - Web and API Testing

| Item | Value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance, September 2026 |
| Lab group | Wednesday Lab - Group 2 |
| Phase owner | Mohamad Shukri Bin Abdul Ajed |
| Execution date | 2026-11-24: full run 13:41 (+08:00, 23 s); defect screenshots re-run 18:45-19:03 |
| Environment | Windows 11 25H2; Python 3.14; Flask 3.0.3; app served by `python app.py` at `http://127.0.0.1:5000` on an empty database; Postman 12.38.2 Collection Runner, 1 iteration |

## Deliverable checklist

- [x] [Web test scenarios](#2-web-test-scenarios) - 16 cases, TC-WEB-001 to 016
- [x] [API test suite](#3-api-test-suite) - 45 cases, TC-API-001 to 045, as a [Postman collection](postman/)
- [x] [Request/test data](#4-requesttest-data) - [test_data.md](test_data.md)
- [x] [Expected versus actual status/response](#5-expected-versus-actual-status-and-response) - all 61 cases in [test_cases.md](test_cases.md)
- [x] [Execution evidence and defects](#6-execution-evidence-and-defects) - 43 Pass / 18 Fail; DEF-014 to DEF-023 in [defects.md](defects.md)

## 1. Scope, test basis and environment

**In scope:** all nine JSON endpoints under `/api`, the web routes that change data (`/register`, `/login`, `/tasks/new`, `/tasks/<id>/edit`, `/tasks/<id>/toggle`, `/tasks/<id>/delete`), and `/` and `/dashboard` as read views.
**Out of scope:** layout, compatibility and accessibility (Week 3); attack payloads, CSRF, session security and load (Week 5); code coverage (Week 2).

| Test basis | Used for |
| --- | --- |
| Application `README.md`, API section | Endpoints, payload fields, "session-cookie authentication except register and login", `due_date` format `YYYY-MM-DD` |
| `helpers.py` docstrings | Username and password rules, urgency classes |
| Week 1 assumptions | A title needs a non-whitespace character; a task due today is "Due Today" |
| HTTP conventions (team decision; the README defines no error contract) | Invalid input -> `400` with a JSON `{"error": ...}`; missing or another user's resource -> `404`; not logged in -> `401`; unsupported method -> `405`; `500` is never acceptable for client input; a failed request must not change stored data |
| `templates/*.html` | Browser-side checks the server must not rely on: `required` fields, `type="date"`, the category `<select>` |

New requirement this week: **REQ-009 JSON REST API contract** - correct HTTP status codes, session authentication and JSON error bodies for invalid input. A letter suffix (`TC-API-036a`) marks a variant of a case.

| Entry criteria | Exit criteria |
| --- | --- |
| App starts and `/login` returns 200 on an empty database | Every case is Pass, Fail, Blocked or Not Run |
| Expected results written as Postman checks before the run | Every Fail links to a defect |
| Earlier defect IDs checked so new IDs do not clash | Every defect reproduced twice (full run and screenshot re-run) |

All exit criteria were met: 61 cases executed, 0 Blocked, 0 Not Run.

## 2. Web test scenarios

The web cases send the form fields a browser sends to the real web routes, then check the result through the API. They also send values the browser would normally block (an empty `required` field, text in the date field, a category the drop-down does not offer), because the server must validate its own input.

| Case | Scenario | Type | Result | Defect |
| --- | --- | --- | --- | --- |
| TC-WEB-001 | Register through the form, land on the task list | Workflow | Pass | - |
| TC-WEB-002 | Registration re-checked on the server: empty username, illegal character, 7-character password | Server-side validation | Pass | - |
| TC-WEB-003 | Login with valid and wrong password | Workflow / decision table | Pass | - |
| TC-WEB-004 | Six protected pages and actions redirect to `/login` when logged out | Access control | Pass | - |
| TC-WEB-005 | Task created on the web is returned identically by the API | UI -> API | Pass | - |
| TC-WEB-006 | Task created through the API shows on the web list with the same category and urgency | API -> UI | Pass | - |
| TC-WEB-007 | Web edit is returned by the API | UI -> API | Pass | - |
| TC-WEB-008 | Web complete/reopen sets `done` and `completed_at` as the API reports | UI -> API, state transition | Pass | - |
| TC-WEB-009 | Web delete removes the task from the API | UI -> API | Pass | - |
| TC-WEB-010 | Blank title (empty or spaces) rejected by the server | Server-side validation | **Fail** | DEF-003 |
| TC-WEB-011 | Due date that is not a date rejected by the server | Server-side validation | **Fail** | DEF-015 |
| TC-WEB-012 | Category id not offered by the drop-down rejected by the server | Server-side validation | **Fail** | DEF-019 |
| TC-WEB-013 | Another user's edit, toggle and delete change nothing | Ownership | Pass | - |
| TC-WEB-014 | Web dashboard numbers equal the API dashboard | UI vs API | Pass | - |
| TC-WEB-015 | Web search for `O'Brien` works | UI vs API | Pass | - |
| TC-WEB-016 | Web form refuses an existing username | Validation | **Fail** | DEF-016 |

16 cases, 12 Pass, 4 Fail. Normal workflows behave the same on the web and in the API. All four failures are missing server-side checks; three appear only when the browser's checks are bypassed, and the duplicate username cannot be caught by any browser check.

## 3. API test suite

The suite is a Postman collection ([postman/](postman/)) of 190 requests in 10 folders: 61 cases plus SETUP requests that create users and data. Every request has post-response checks written from the expected result. Dates are computed by a collection-level script and each folder registers its own users, so the suite gives the same verdicts on any day and folders can run independently.

| Folder | Cases |
| --- | --- |
| 01 Registration and login | TC-API-001 to 010 |
| 02 Authentication required | TC-API-011 to 013 |
| 03 Create and read tasks | TC-API-014 to 018, 020 to 023, 025 |
| 04 List, filter, search, paging | TC-API-026 to 032 |
| 05 Update tasks | TC-API-034 to 036e, 038 |
| 06 Delete tasks | TC-API-039, 041 |
| 07 One user vs another user's data | TC-API-024, 033, 037, 040, 044 |
| 08 Dashboard | TC-API-042, 043 |
| 09 HTTP method | TC-API-045 |
| 10 Web forms | TC-WEB-001 to 016 (except 011) |
| 99 Run last - invalid due dates | TC-API-019, 036f, TC-WEB-011 |

Folder 99 runs last because its cases leave the test user unable to load their task list (DEF-015).

### 3.1 Endpoint inventory and priority

| Method and path | Login needed (README / code) | Purpose | Priority | Reason | Cases |
| --- | --- | --- | --- | --- | --- |
| `POST /api/register` | No / No | Create account and log in | High | Writes data; account rules | TC-API-001 to 008 |
| `POST /api/login` | No / No | Start a session | High | Gate to all user data | TC-API-009, 010 |
| `GET /api/tasks` | Yes / Yes | List with category, status, search, paging | High | Most-used read; four user-controlled values | TC-API-011, 026 to 033 |
| `POST /api/tasks` | Yes / Yes | Create a task | High | Main write path | TC-API-011, 014 to 021 |
| `GET /api/tasks/<id>` | Yes / Yes | Read one task | Medium | Must not reveal another user's task | TC-API-011, 022 to 025 |
| `PUT /api/tasks/<id>` | Yes / Yes | Partial update, complete/reopen | High | Changes data and state | TC-API-011, 034 to 038 |
| `DELETE /api/tasks/<id>` | Yes / Yes | Delete a task | High | Irreversible; own tasks only | TC-API-011, 039 to 041 |
| `GET /api/dashboard` | Yes / Yes | Summary counters | Medium | Depends on urgency rules | TC-API-011, 042 to 044 |
| `GET /api/categories` | Yes / **No** | List the 4 categories | Low | README and code disagree | TC-API-012, 013 |

### 3.2 Requirements traceability (Week 4 rows)

| Requirement/Feature | Test Scenario | Test Case ID(s) | Technique | Result | Defect ID |
| --- | --- | --- | --- | --- | --- |
| REQ-001 Registration | Valid account, username length 3 and 20 | TC-API-001, 002 | EP, BVA | Pass | - |
| REQ-001 Registration | Invalid usernames, 7-char and missing password | TC-API-003, 004, 006 | EP, BVA | Pass | - |
| REQ-001 Registration | 8-character password | TC-API-005 | BVA | Fail | DEF-001 |
| REQ-001 Registration | Username of the wrong type | TC-API-007 | EP (data type) | Fail | DEF-018 |
| REQ-001 Registration | Duplicate username (API and web) | TC-API-008, TC-WEB-016 | EP | Fail | DEF-016 |
| REQ-001 Registration | Web registration and server-side re-check | TC-WEB-001, 002 | Workflow, server validation | Pass | - |
| REQ-002 Login and access | Login valid/invalid (API and web) | TC-API-009, 010, TC-WEB-003 | Decision table | Pass | - |
| REQ-002 Login and access | Not logged in: protected endpoints and pages | TC-API-011, TC-WEB-004 | EP / access control | Pass | - |
| REQ-003 Task CRUD | Valid create, read, update, delete | TC-API-014, 015, 022, 023, 025, 034, 038, 039 | EP / functional | Pass | - |
| REQ-003 Task CRUD | Missing/blank title, non-JSON body | TC-API-016, 017 | EP / negative | Pass | - |
| REQ-003 Task CRUD | Wrong data types | TC-API-018 | EP (data type) | Fail | DEF-018 |
| REQ-003 Task CRUD | Invalid due date (API and web) | TC-API-019, TC-WEB-011 | EP / server validation | Fail | DEF-015 |
| REQ-003 Task CRUD | Unknown category (API and web) | TC-API-020, TC-WEB-012 | EP / server validation | Fail | DEF-019 |
| REQ-003 Task CRUD | Invalid values on update | TC-API-036 | EP / negative | Fail | DEF-015, 018, 019, 020 |
| REQ-003 Task CRUD | Blank title on the web form | TC-WEB-010 | Server validation | Fail | DEF-003 |
| REQ-003 Task CRUD | Delete a task that does not exist | TC-API-041 | EP / negative | Fail | DEF-021 |
| REQ-003 Task CRUD | Web create/edit/delete consistent with API | TC-WEB-005 to 007, 009 | UI vs API | Pass | - |
| REQ-004 Complete/reopen | API and web state transitions | TC-API-035, TC-WEB-008 | State transition | Pass | - |
| REQ-005 Filter and search | Category, status, search, combined, paging | TC-API-026 to 029, 031 | EP, decision table, BVA | Pass | - |
| REQ-005 Filter and search | Search with an apostrophe (API / web) | TC-API-030 / TC-WEB-015 | EP (special character) | Fail / Pass | DEF-017 |
| REQ-005 Filter and search | Invalid paging values | TC-API-032 | EP, BVA | Fail | DEF-022 |
| REQ-006 Urgency | Yesterday, +1, +2, +3 days | TC-API-021a, c to e | BVA | Pass | - |
| REQ-006 Urgency | Due today | TC-API-021b, 043 | BVA | Fail | DEF-002 |
| REQ-006 Urgency | API urgency shown on the web list | TC-WEB-006 | API -> UI | Pass | - |
| REQ-007 Dashboard | Controlled dataset; web equals API | TC-API-042, TC-WEB-014 | Independent count / UI vs API | Pass | - |
| REQ-008 User separation | Read, update, list, dashboard of another user | TC-API-024, 033, 037, 044, TC-WEB-013 | EP (foreign id) | Pass | - |
| REQ-008 User separation | Delete another user's task via the API | TC-API-040 | EP (foreign id) | Fail | DEF-014 |
| REQ-009 API contract | Categories list, non-numeric id, unsupported method | TC-API-013, 025, 045 | Functional / negative | Pass | - |
| REQ-009 API contract | Categories without login | TC-API-012 | EP / negative | Fail | DEF-023 |

## 4. Request/test data

Full partitions, boundaries and datasets: [test_data.md](test_data.md). In short:

- Each folder registers fresh users (`w4` + role letter + digits, e.g. `w4a9888108439`) with the synthetic password `Test12345`, so cases do not depend on each other or on existing data.
- Due dates are computed at run time (`{{today}}`, `{{plus1}}`, ...), so urgency results hold on any day.
- The exact body of every request is stored in the Postman collection.

## 5. Expected versus actual status and response

### 5.1 Failing cases

Expected and actual results for all 61 cases are in [test_cases.md](test_cases.md). Every passing case returned the expected status and body.

| Case | Request | Expected | Actual | Defect |
| --- | --- | --- | --- | --- |
| TC-API-005 | `POST /api/register`, password `abcd1234` (8 chars) | 201 | 400 `invalid password` | DEF-001 |
| TC-API-007 | `POST /api/register`, username `12345` (number) | 400 JSON | 500 HTML (`AttributeError`) | DEF-018 |
| TC-API-008a | `POST /api/register`, existing username | 409 or 400 | 201, second account with the same name | DEF-016 |
| TC-API-012 | `GET /api/categories` without login | 401 | 200 with the list | DEF-023 |
| TC-API-018a-c | `POST /api/tasks`, title `123`, title list, description object | 400 JSON | 500 HTML (all three) | DEF-018 |
| TC-API-019a-c | `POST /api/tasks`, due `31/12/2026`, `2026-02-30`, `tomorrow` | 400; list and dashboard still 200 | 500, but the task **is saved**; list and dashboard then return 500 | DEF-015 |
| TC-API-020a-b | `POST /api/tasks`, category `999`, `"abc"` | 400 | 201, saved with `category: null` | DEF-019 |
| TC-API-021b | `POST /api/tasks`, due today | urgency `Due Today` | `Overdue` | DEF-002 |
| TC-API-030 | `GET /api/tasks?q=O'Brien` | 200 with the matching task | 500 (`sqlite3.OperationalError`) | DEF-017 |
| TC-API-032a-c | `?per_page=-1`, `?page=-1`, `?page=abc` | 400 | 200 | DEF-022 |
| TC-API-036a-b | `PUT` title `""` / `"   "` | 400, unchanged | 200, blank title saved | DEF-020 |
| TC-API-036c | `PUT` done `"false"` (text) | 400, unchanged | 200, task marked **done** | DEF-020 |
| TC-API-036d | `PUT` title `null` | 400 JSON | 500 HTML | DEF-018 |
| TC-API-036e | `PUT` category `999` | 400, unchanged | 200, category 999 saved | DEF-019 |
| TC-API-036f | `PUT` due `31/12/2026` | 400, unchanged | 500, change **saved**; task can no longer be read | DEF-015 |
| TC-API-040 | `DELETE` user A's task as user B | 404, task kept | 200; **task deleted** | DEF-014 |
| TC-API-041 | `DELETE /api/tasks/999999999` | 404 | 200 `{"result": "ok"}` | DEF-021 |
| TC-API-043 | `GET /api/dashboard` after adding a task due today | overdue stays 1 | overdue 2 | DEF-002 |
| TC-WEB-010a-b | `POST /tasks/new`, title `""` / `"   "` | rejected | 302, blank title saved | DEF-003 |
| TC-WEB-011a-b | `POST /tasks/new`, due `31/12/2026` / `not-a-date` | rejected; pages still load | 302 saved; `/` and `/dashboard` then 500 | DEF-015 |
| TC-WEB-012 | `POST /tasks/new`, category `999` | rejected | 302, saved | DEF-019 |
| TC-WEB-016 | `POST /register`, existing username | 200 with an error | 302, logged in as a new account | DEF-016 |

### 5.2 UI versus API comparison

| Behaviour | Web UI | API | Same? | Cases |
| --- | --- | --- | --- | --- |
| Create, edit, complete/reopen, delete | Correct | Same data | Yes | TC-WEB-005 to 009 |
| Urgency labels and dashboard numbers | Same values | Same | Yes | TC-WEB-006, 014 |
| Blank title | **Accepted** when the browser check is bypassed | Rejected (400) | **No** | TC-WEB-010 / TC-API-016 |
| Delete another user's task | Refused | **Allowed** | **No** | TC-WEB-013 / TC-API-040 |
| Edit or complete another user's task | Refused | Refused (404) | Yes | TC-WEB-013 / TC-API-037 |
| Search containing `'` | Works | **500** | **No** | TC-WEB-015 / TC-API-030 |
| Invalid due date | Saved, pages then 500 | Saved, API then 500 | Both wrong | TC-WEB-011 / TC-API-019 |
| Unknown category id | Saved | Saved | Both wrong | TC-WEB-012 / TC-API-020 |
| Duplicate username | Accepted | Accepted | Both wrong | TC-WEB-016 / TC-API-008 |
| Not logged in | Redirect to `/login` | 401 JSON (except categories) | Yes, apart from DEF-023 | TC-WEB-004 / TC-API-011, 012 |

The web pages and the API are separate implementations of the same operations and have drifted apart: each gets right something the other gets wrong (the API checks the title; the web pages scope delete to the owner and build the search query safely). Validation and data-access code shared by both would remove this class of defect.

## 6. Execution evidence and defects

Full run 2026-11-24 13:41 (+08:00): 190 requests, **339 checks, 276 passed, 63 failed**, 0 errors.

| Suite | Cases | Pass | Fail | Blocked | Not Run | Pass rate |
| --- | --- | --- | --- | --- | --- | --- |
| Web (TC-WEB) | 16 | 12 | 4 | 0 | 0 | 75% |
| API (TC-API) | 45 | 31 | 14 | 0 | 0 | 69% |
| **Total** | **61** | **43** | **18** | **0** | **0** | **70%** |

Evidence: the full runner result [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) (every check with pass/fail and status code), the [run summary](evidences/full-run-summary-276-pass-63-fail-20261124.jpg) and one screenshot per defect in [`evidences/`](evidences/).

### 6.1 Defects

Full records: [defects.md](defects.md). Severity: Critical = data loss or a user loses access to their own data; Major = account integrity broken, or a server error on ordinary input; Moderate = wrong behaviour or a crash on unusual input; Minor = wrong status code or documentation mismatch.

| Defect ID | Title | Cases | Severity / Priority |
| --- | --- | --- | --- |
| DEF-014 | Any logged-in user can delete another user's task through the API | TC-API-040 | Critical / High |
| DEF-015 | An invalid due date is saved and then breaks that user's task list and dashboard | TC-API-019, 036f, TC-WEB-011 | Critical / High |
| DEF-016 | Registration accepts a username that already exists | TC-API-008, TC-WEB-016 | Major / High |
| DEF-017 | API search text containing an apostrophe causes a 500 error | TC-API-030 | Major / High |
| DEF-018 | Wrong JSON data types cause 500 errors instead of 400 | TC-API-007, 018, 036d | Moderate / Medium |
| DEF-019 | Task create/update accepts a category that does not exist | TC-API-020, 036e, TC-WEB-012 | Moderate / Medium |
| DEF-020 | Task update skips title validation and treats the text "false" as done | TC-API-036a-c | Moderate / Medium |
| DEF-021 | Deleting a task that does not exist reports success | TC-API-041 | Minor / Low |
| DEF-022 | Invalid paging values are not rejected | TC-API-032 | Minor / Low |
| DEF-023 | `/api/categories` works without login, contrary to the README | TC-API-012 | Minor / Low |

New defects by severity: 2 Critical, 2 Major, 3 Moderate, 3 Minor. All 10 affect the API; DEF-015, 016 and 019 also affect the web forms. DEF-001, DEF-002 and DEF-003 (Week 1) were reproduced through the API and web forms.

### 6.2 Observations (not logged as defects)

| ID | Observation | Why not a defect |
| --- | --- | --- |
| OBS-W4-01 | No `/api/logout`; an API client ends a session only by dropping the cookie | Not documented as a feature |
| OBS-W4-02 | 404 and 405 responses for unknown routes/methods are HTML, while the app's own errors are JSON | Status codes are correct |
| OBS-W4-03 | Paging starts at `page=0`; the README does not say so | Consistent behaviour; documentation gap |
| OBS-W4-04 | Editing, completing or deleting another user's task on the web silently redirects to `/` | Secure outcome (TC-WEB-013 passes) |
| OBS-W4-05 | 500 responses show the full Python traceback, because the server runs with `debug=True` | Information disclosure; assessed in Week 5 (DEF-031) |

## 7. Limitations

- Web cases send real form submissions but do not render pages; layout and browser behaviour were covered in Weeks 1 and 3.
- One recorded full run on one Windows machine, plus targeted re-runs for screenshots.
- Expected error codes (400 / 404 / 409) are a team decision, because the README defines no error contract.
- Not tested this week: concurrent requests, very large payloads, non-ASCII input, session expiry and attack payloads (Week 5).
