# Week 4 - Web and API Testing

| Item | Recorded value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / Lab Group | September 2026 / Wednesday Lab - Group 2 |
| Phase owner | Mohamad Shukri Bin Abd Ajed |
| Phase status | Executed 2026-11-24 with Postman (61 cases, 190 requests, 339 checks); ready for peer review |

## Deliverable Checklist

- [ ] [Task 1](#task-1) - Web test scenarios. 16 cases (TC-WEB-001 to 016): web workflows, server-side validation of the web forms, and UI-versus-API comparison.
- [ ] [Task 2](#task-2) - API test suite. 45 cases (TC-API-001 to 045) over all 9 REST endpoints, as a Postman collection.
- [ ] [Task 3](#task-3) - Request/test data. Accounts, partitions, boundaries and datasets.
- [ ] [Task 4](#task-4) - Expected versus actual status/response. Every failing case, plus the UI-versus-API comparison.
- [ ] [Task 5](#task-5) - Execution evidence and defects. 43 Pass / 18 Fail; 10 new defects (DEF-014 to DEF-023) and 3 Week 1 defects reproduced.

Tick a task only after its results, evidence and peer review are complete.

## Deliverable structure

This README is the phase report. Detailed cases, data and evidence are in the files it links to.

```
04_Web_API/
├── README.md               <- this report
├── test_cases.md           <- 61 cases in the course template (expected, actual, status, evidence, defect)
├── test_data.md            <- accounts, partitions, boundaries, datasets
├── postman/
│   ├── PyTodo_Pro_Week4.postman_collection.json   <- the API and web test suite (190 requests)
│   └── PyTodo_Local.postman_environment.json      <- base_url and password
└── evidences/
    ├── postman-run-full-20261124.json             <- full Collection Runner result (every check, pass/fail, status code)
    ├── full-run-summary-276-pass-63-fail-20261124.jpg
    └── TC-...-20261124.jpg                        <- one screenshot per defect
```

| Deliverable (guideline) | Report section | Detail | Evidence |
| --- | --- | --- | --- |
| Web test scenarios | [Task 1](#task-1) | [test_cases.md](test_cases.md) TC-WEB-* | Runner result, TC-WEB screenshots |
| API test suite | [Task 2](#task-2) | [postman/](postman/), [test_cases.md](test_cases.md) TC-API-* | Runner result |
| Request/test data | [Task 3](#task-3) | [test_data.md](test_data.md) | Request bodies inside the collection |
| Expected versus actual status/response | [Task 4](#task-4) | [test_cases.md](test_cases.md) | Runner result, screenshots |
| Execution evidence and defects | [Task 5](#task-5) | Defect records below | Linked from each defect |

## Task 0 - Phase plan

### 0.1 Required activities from the project guideline

| Activity | Where it is done |
| --- | --- |
| Test major web workflows and client-server validation | Task 1, TC-WEB-001 to 016 |
| Identify important REST API endpoints | Task 2, [endpoint inventory](#21-endpoint-inventory-and-priority) |
| Test valid requests and expected responses | TC-API-001, 002, 009, 013 to 015, 021, 022, 026 to 031, 034, 035, 039, 042 |
| Test invalid inputs, missing data, incorrect data types and edge conditions | TC-API-003 to 008, 010 to 012, 016 to 020, 023 to 025, 032, 036 to 038, 040, 041, 045 |
| Validate HTTP status codes and response content | Every request has checks on its status code and body |
| Compare UI and server-side/API behaviour | [Task 4.2](#42-ui-versus-api-comparison), TC-WEB-005 to 016 |

### 0.2 Scope

In scope: all nine JSON endpoints under `/api`, and the web routes that change data (`/register`, `/login`, `/tasks/new`, `/tasks/<id>/edit`, `/tasks/<id>/toggle`, `/tasks/<id>/delete`) plus `/` and `/dashboard` as read views.

Out of scope: page layout, compatibility and accessibility (Week 3); attack payloads, CSRF and session security (Week 5); response times and load (Week 5); code coverage (Week 2).

### 0.3 Test basis

| Source | Used for |
| --- | --- |
| Application `README.md`, API section | Endpoints, payload fields, "session-cookie authentication except register and login", `due_date` format `YYYY-MM-DD` |
| `helpers.py` docstring specifications | Username and password rules, urgency classes |
| Week 1 agreed assumptions | A title needs at least one non-whitespace character; a task due today is "Due Today", not "Overdue" |
| HTTP conventions (team assumption, because the README defines no error contract) | Invalid input -> `400` with a JSON `{"error": ...}` body; missing or someone else's resource -> `404`; not logged in -> `401`; unsupported method -> `405`; a `500` is never an acceptable answer to client input; a request that fails must not change stored data |
| `templates/*.html` | Browser-side checks the server must not rely on: `required` on username, password and title; `type="date"` on due date; the category `<select>` |

### 0.4 ID conventions

| Prefix | Meaning |
| --- | --- |
| `TC-WEB-nnn` | Web workflow, server-side validation and UI-versus-API cases |
| `TC-API-nnn` | REST API cases. A letter suffix (`TC-API-036a`) marks one variant of a case; `-check` marks the request that verifies the result |
| `DEF-nnn` | Shared defect series. Weeks 1-3 used DEF-001 to DEF-013, so Week 4 continues at DEF-014 |
| `REQ-nnn` | Week 1 requirements REQ-001 to REQ-008, plus **REQ-009** added this week: *JSON REST API contract - correct HTTP status codes, session authentication and JSON error bodies for invalid input* |

### 0.5 Environment

| Component | Value |
| --- | --- |
| Operating system | Windows 11 25H2 |
| Python | 3.14 (team virtual environment in `test/02_White_Box_Coverage/.venv`) |
| Flask | 3.0.3 (from `requirements.txt`) |
| Server | `python -B ../../app.py` development server at `http://127.0.0.1:5000`, started on an empty database |
| Test tool | Postman desktop 12.38.2, Collection Runner, 1 iteration |
| Application commit | `fc0767f` (main) |
| Full run | 2026-11-24 13:41:20 (+08:00), duration 23 s 139 ms |
| Screenshot re-runs | 2026-11-24 18:45-19:03 (+08:00): single requests and folders 05, 07, 10 and 99 re-run to capture each defect |

### 0.6 Entry and exit criteria

| Entry criteria | Exit criteria |
| --- | --- |
| Application starts and `/login` returns 200 | Every case is Pass, Fail, Blocked or Not Run |
| Expected results written as Postman checks before the run | Every Fail links to a defect |
| Weeks 1-3 defect IDs checked so new IDs do not clash | Every defect reproduced at least twice (full run + screenshot re-run) |
| Empty database before the recorded run | Runner result and screenshots saved in `evidences/` |

Status at exit: 61 cases executed, 0 Blocked, 0 Not Run. All 18 failing cases link to defects, and each failure was seen again in the screenshot re-runs.

### 0.7 How to re-run the suite

1. Delete `pytodo_pro.db` in the repository root, then start the app: from `test/02_White_Box_Coverage` with the virtual environment active, run `python -B ../../app.py`.
2. In Postman: **Import** both files from `postman/`, and select the **PyTodo Local** environment (top right).
3. Collection **…** -> **Run collection**: all requests, 1 iteration, in order.

Expected result on the current code: 339 checks, 276 passed, 63 failed. Folder **99** runs last on purpose: its cases can leave a test user unable to load their task list (DEF-015). Each folder registers its own users, so a single folder can also be run on its own.

Command-line alternative (free, no Postman account): `npm install -g newman`, then `newman run postman/PyTodo_Pro_Week4.postman_collection.json -e postman/PyTodo_Local.postman_environment.json`.

## Task 1

### Web test scenarios

The web cases send the same form fields a browser sends to the real web routes, then check the result through the API. They also send values the browser would normally block (an empty `required` field, text in the date picker, a category the drop-down does not offer). The browser's checks only help honest users, so the **server** must still validate its input; these cases test exactly that.

| Case | Scenario | Type | Result | Defect |
| --- | --- | --- | --- | --- |
| TC-WEB-001 | Register through the form, land on the task list | Workflow | Pass | - |
| TC-WEB-002 | Registration re-checked on the server: empty username with `required` bypassed, illegal character, 7-character password | Server-side validation | Pass | - |
| TC-WEB-003 | Login with valid and wrong password | Workflow / decision table | Pass | - |
| TC-WEB-004 | Six protected pages and actions redirect to `/login` when logged out | Access control | Pass | - |
| TC-WEB-005 | Task created on the web is returned identically by the API | UI -> API | Pass | - |
| TC-WEB-006 | Task created through the API shows on the web list with the same category and urgency | API -> UI | Pass | - |
| TC-WEB-007 | Web edit is returned by the API | UI -> API | Pass | - |
| TC-WEB-008 | Web complete/reopen sets `done` and `completed_at` as the API reports | UI -> API, state transition | Pass | - |
| TC-WEB-009 | Web delete removes the task from the API | UI -> API | Pass | - |
| TC-WEB-010 | Blank title (empty with `required` bypassed, or spaces) rejected by the server | Server-side validation | **Fail** | DEF-003 |
| TC-WEB-011 | Due date that is not a date (date picker bypassed) rejected by the server | Server-side validation | **Fail** | DEF-015 |
| TC-WEB-012 | Category id the drop-down does not offer rejected by the server | Server-side validation | **Fail** | DEF-019 |
| TC-WEB-013 | Another user's edit, toggle and delete on a task change nothing | Ownership | Pass | - |
| TC-WEB-014 | Web dashboard numbers equal the API dashboard | UI vs API | Pass | - |
| TC-WEB-015 | Web search for `O'Brien` works | UI vs API | Pass | - |
| TC-WEB-016 | Web form refuses an existing username | Validation | **Fail** | DEF-016 |

Summary: 16 cases, 12 Pass, 4 Fail. The normal workflows behave the same on the web and in the API. All four failures are missing server-side checks: three only show when the browser's own checks are bypassed, and the fourth (duplicate username) is something no browser check can catch.

## Task 2

### API test suite

The suite is a Postman collection ([postman/](postman/)) of 190 requests in 10 folders: 61 test cases plus SETUP requests that create users and data. Each request has checks (Postman post-response scripts) written from the expected result, so a failing check is the evidence of a defect. Dates are computed by a collection-level script, and every folder registers its own fresh users, so the suite can be re-run on any day and in any order of folders.

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

### 2.1 Endpoint inventory and priority

| Method and path | Login needed (README / code) | Purpose | Priority | Reason | Cases |
| --- | --- | --- | --- | --- | --- |
| `POST /api/register` | No / No | Create account and log it in | High | Writes data; entry point; account rules | TC-API-001 to 008 |
| `POST /api/login` | No / No | Start a session | High | Gate to all user data | TC-API-009, 010 |
| `GET /api/tasks` | Yes / Yes | List with category, status, search, paging | High | Most-used read; four user-controlled query values | TC-API-011, 026 to 033 |
| `POST /api/tasks` | Yes / Yes | Create a task | High | Main write path; every field is user input | TC-API-011, 014 to 021 |
| `GET /api/tasks/<id>` | Yes / Yes | Read one task | Medium | Must not reveal another user's task | TC-API-011, 022 to 025 |
| `PUT /api/tasks/<id>` | Yes / Yes | Partial update, complete/reopen | High | Changes data and task state | TC-API-011, 034 to 038 |
| `DELETE /api/tasks/<id>` | Yes / Yes | Delete a task | High | Irreversible; must only delete your own | TC-API-011, 039 to 041 |
| `GET /api/dashboard` | Yes / Yes | Summary counters | Medium | Derived numbers depend on the urgency rules | TC-API-011, 042 to 044 |
| `GET /api/categories` | Yes / **No** | List the 4 categories | Low | Read-only reference data; README and code disagree | TC-API-012, 013 |

There is no `/api/logout`; an API client can only end its session by dropping the cookie (see [observations](#54-observations-not-logged-as-defects)).

### 2.2 Requirements traceability (Week 4 rows)

| Requirement/Feature | Test Scenario | Test Case ID(s) | Test Type/Technique | Result | Defect ID |
| --- | --- | --- | --- | --- | --- |
| REQ-001 Registration | Valid account, username length 3 and 20 | TC-API-001, 002 | EP, BVA / API | Pass | - |
| REQ-001 Registration | Invalid usernames, 7-char and missing password | TC-API-003, 004, 006 | EP, BVA / API negative | Pass | - |
| REQ-001 Registration | 8-character password | TC-API-005 | BVA / API | Fail | DEF-001 |
| REQ-001 Registration | Username of the wrong type | TC-API-007 | EP (data type) | Fail | DEF-018 |
| REQ-001 Registration | Duplicate username (API and web) | TC-API-008, TC-WEB-016 | EP | Fail | DEF-016 |
| REQ-001 Registration | Web registration and server-side re-check | TC-WEB-001, 002 | Workflow, server-side validation | Pass | - |
| REQ-002 Login and access | Login valid/invalid (API and web) | TC-API-009, 010, TC-WEB-003 | Decision table | Pass | - |
| REQ-002 Login and access | Not logged in: protected endpoints and pages | TC-API-011, TC-WEB-004 | EP / access control | Pass | - |
| REQ-003 Task CRUD | Valid create, read, update, delete | TC-API-014, 015, 022, 023, 025, 034, 038, 039 | EP / API functional | Pass | - |
| REQ-003 Task CRUD | Missing/blank title, non-JSON body | TC-API-016, 017 | EP / API negative | Pass | - |
| REQ-003 Task CRUD | Wrong data types | TC-API-018 | EP (data type) | Fail | DEF-018 |
| REQ-003 Task CRUD | Invalid due date (API and web) | TC-API-019, TC-WEB-011 | EP / server-side validation | Fail | DEF-015 |
| REQ-003 Task CRUD | Unknown category (API and web) | TC-API-020, TC-WEB-012 | EP / server-side validation | Fail | DEF-019 |
| REQ-003 Task CRUD | Invalid values on update | TC-API-036 | EP / API negative | Fail | DEF-015, 018, 019, 020 |
| REQ-003 Task CRUD | Blank title on the web form | TC-WEB-010 | Server-side validation | Fail | DEF-003 |
| REQ-003 Task CRUD | Delete a task that does not exist | TC-API-041 | EP / API negative | Fail | DEF-021 |
| REQ-003 Task CRUD | Web create/edit/delete consistent with API | TC-WEB-005 to 007, 009 | Workflow / UI vs API | Pass | - |
| REQ-004 Complete/reopen | API and web state transitions | TC-API-035, TC-WEB-008 | State transition | Pass | - |
| REQ-005 Filter and search | Category, status, search, combined, paging | TC-API-026 to 029, 031 | EP, decision table, BVA | Pass | - |
| REQ-005 Filter and search | Search with an apostrophe (API / web) | TC-API-030 / TC-WEB-015 | EP (special character) | Fail / Pass | DEF-017 |
| REQ-005 Filter and search | Invalid paging values | TC-API-032 | EP, BVA / API negative | Fail | DEF-022 |
| REQ-006 Urgency | Yesterday, +1, +2, +3 days | TC-API-021a, c to e | BVA / API | Pass | - |
| REQ-006 Urgency | Due today | TC-API-021b, 043 | BVA / API | Fail | DEF-002 |
| REQ-006 Urgency | API urgency shown on the web list | TC-WEB-006 | API -> UI | Pass | - |
| REQ-007 Dashboard | Controlled dataset; web equals API | TC-API-042, TC-WEB-014 | Independent count / UI vs API | Pass | - |
| REQ-008 User separation | Read, update, list, dashboard of another user | TC-API-024, 033, 037, 044, TC-WEB-013 | EP (foreign id) | Pass | - |
| REQ-008 User separation | Delete another user's task via the API | TC-API-040 | EP (foreign id) | Fail | DEF-014 |
| REQ-009 API contract | Categories list, non-numeric id, unsupported method | TC-API-013, 025, 045 | API functional / negative | Pass | - |
| REQ-009 API contract | Categories without login | TC-API-012 | EP / API negative | Fail | DEF-023 |

## Task 3

### Request/test data

[test_data.md](test_data.md) lists the accounts, the valid and invalid values for every field and query parameter, and the datasets used for filtering and the dashboard. In short:

- Each folder registers fresh, uniquely named users (`w4` + letter + digits, e.g. `w4a9888108439`) with the team's synthetic password `Test12345`, so cases do not depend on each other or on existing data.
- Due dates are computed at run time (`{{today}}`, `{{plus1}}`, …), so urgency results hold on any day.
- The exact body of every request is stored in the Postman collection.

## Task 4

### 4.1 Expected versus actual status and response

Full expected and actual results for all 61 cases are in [test_cases.md](test_cases.md). Every passing case returned the expected status and body. The failures:

| Case | Request | Expected | Actual | Defect |
| --- | --- | --- | --- | --- |
| TC-API-005 | `POST /api/register`, password `abcd1234` (8 chars) | 201 | 400 `invalid password` | DEF-001 |
| TC-API-007 | `POST /api/register`, username `12345` (number) | 400 JSON | 500 HTML error page (`AttributeError`) | DEF-018 |
| TC-API-008a | `POST /api/register`, existing username | 409 or 400 | 201, a second account with the same name | DEF-016 |
| TC-API-012 | `GET /api/categories` without login | 401 | 200 with the category list | DEF-023 |
| TC-API-018a-c | `POST /api/tasks`, title `123`, title list, description object | 400 JSON | 500 HTML (all three) | DEF-018 |
| TC-API-019a-c | `POST /api/tasks`, due `31/12/2026`, `2026-02-30`, `tomorrow` | 400; list and dashboard still 200 | 500, but the task **is saved**; afterwards `GET /api/tasks` and `/api/dashboard` return 500 | DEF-015 |
| TC-API-020a-b | `POST /api/tasks`, category `999`, `"abc"` | 400 | 201, saved with `category: null` | DEF-019 |
| TC-API-021b | `POST /api/tasks`, due today | urgency `Due Today` | `Overdue` | DEF-002 |
| TC-API-030 | `GET /api/tasks?q=O'Brien` | 200 with the matching task | 500 (`sqlite3.OperationalError: near "Brien"`) | DEF-017 |
| TC-API-032a-c | `?per_page=-1`, `?page=-1`, `?page=abc` | 400 | 200 | DEF-022 |
| TC-API-036a-b | `PUT` title `""` / `"   "` | 400, task unchanged | 200, blank title saved | DEF-020 |
| TC-API-036c | `PUT` done `"false"` (text) | 400, task unchanged | 200, task marked **done** | DEF-020 |
| TC-API-036d | `PUT` title `null` | 400 JSON | 500 HTML | DEF-018 |
| TC-API-036e | `PUT` category `999` | 400, task unchanged | 200, category 999 saved | DEF-019 |
| TC-API-036f | `PUT` due `31/12/2026` | 400, task unchanged | 500, change **saved**, task can no longer be read (500) | DEF-015 |
| TC-API-040 | `DELETE` user A's task as user B | 404, task kept | 200; user A then gets 404 - **task deleted** | DEF-014 |
| TC-API-041 | `DELETE /api/tasks/999999999` | 404 | 200 `{"result": "ok"}` | DEF-021 |
| TC-API-043 | `GET /api/dashboard` after adding a task due today | overdue stays 1 | overdue 2 | DEF-002 |
| TC-WEB-010a-b | `POST /tasks/new`, title `""` / `"   "` | rejected, nothing saved | 302, task with a blank title saved | DEF-003 |
| TC-WEB-011a-b | `POST /tasks/new`, due `31/12/2026` / `not-a-date` | rejected; pages still load | 302 saved; `/` and `/dashboard` then return 500 | DEF-015 |
| TC-WEB-012 | `POST /tasks/new`, category `999` | rejected | 302, task saved | DEF-019 |
| TC-WEB-016 | `POST /register`, existing username | 200 with an error | 302, logged in as a new account | DEF-016 |

### 4.2 UI versus API comparison

| Behaviour | Web UI | API | Same? | Cases |
| --- | --- | --- | --- | --- |
| Create, edit, complete/reopen, delete | Stored and shown correctly | Same data | Yes | TC-WEB-005 to 009 |
| Urgency labels and dashboard numbers | Same values as the API | Same | Yes | TC-WEB-006, 014 |
| Blank title | **Accepted** when the browser check is bypassed | Rejected (400) | **No** - the rule exists only in the API | TC-WEB-010 / TC-API-016 |
| Delete another user's task | Refused | **Allowed** | **No** - the API is weaker | TC-WEB-013 / TC-API-040 |
| Edit or complete another user's task | Refused | Refused (404) | Yes | TC-WEB-013 / TC-API-037 |
| Search containing `'` | Works | **500** | **No** | TC-WEB-015 / TC-API-030 |
| Invalid due date | Saved, pages then 500 | Saved, API then 500 | Both wrong | TC-WEB-011 / TC-API-019 |
| Unknown category id | Saved | Saved | Both wrong | TC-WEB-012 / TC-API-020 |
| Duplicate username | Accepted | Accepted | Both wrong | TC-WEB-016 / TC-API-008 |
| Not logged in | Redirect to `/login` | 401 JSON (except categories) | Yes, apart from DEF-023 | TC-WEB-004 / TC-API-011, 012 |

The web pages and the API are two separate implementations of the same operations, and they have drifted apart: each gets right something the other gets wrong (the API checks the title; the web pages scope delete to the owner and build the search query safely). Validation and data-access code shared by both would remove this whole class of defect.

## Task 5

### 5.1 Execution summary

Full run, 2026-11-24 13:41 (+08:00): 190 requests, **339 checks, 276 passed, 63 failed**, 0 errors.

| Suite | Cases | Pass | Fail | Blocked | Not Run | Pass rate |
| --- | --- | --- | --- | --- | --- | --- |
| Web (TC-WEB) | 16 | 12 | 4 | 0 | 0 | 75% |
| API (TC-API) | 45 | 31 | 14 | 0 | 0 | 69% |
| **Total** | **61** | **43** | **18** | **0** | **0** | **70%** |

Evidence: the full runner result [postman-run-full-20261124.json](evidences/postman-run-full-20261124.json) (every check with pass/fail and status code), the [run summary screenshot](evidences/full-run-summary-276-pass-63-fail-20261124.jpg), and one screenshot per defect (linked below).

### 5.2 Defect summary

| Defect ID | Title | Cases | Severity | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| DEF-001 | Registration rejects the stated minimum-length (8) password (Week 1) | TC-API-005 | Moderate | Medium | Open - also reproduced through the API |
| DEF-002 | A task due today shows Overdue (Week 1) | TC-API-021b, 043 | Moderate | High | Open - also reproduced through the API and API dashboard |
| DEF-003 | A blank title creates a task on the web (Week 1) | TC-WEB-010 | Moderate | Medium | Open - extended: an empty title also saves when `required` is bypassed |
| DEF-014 | Any logged-in user can delete another user's task through the API | TC-API-040 | Critical | High | Open |
| DEF-015 | An invalid due date is saved and then makes that user's task list and dashboard return 500 | TC-API-019, 036f, TC-WEB-011 | Critical | High | Open |
| DEF-016 | Registration accepts a username that already exists | TC-API-008, TC-WEB-016 | Major | High | Open |
| DEF-017 | API search text containing an apostrophe causes a 500 error | TC-API-030 | Major | High | Open |
| DEF-018 | Wrong JSON data types cause 500 errors instead of 400 | TC-API-007, 018, 036d | Moderate | Medium | Open |
| DEF-019 | Task create/update accepts a category that does not exist | TC-API-020, 036e, TC-WEB-012 | Moderate | Medium | Open |
| DEF-020 | Task update skips title validation and treats the text "false" as done | TC-API-036a-c | Moderate | Medium | Open |
| DEF-021 | Deleting a task that does not exist reports success | TC-API-041 | Minor | Low | Open |
| DEF-022 | Invalid paging values are not rejected | TC-API-032 | Minor | Low | Open |
| DEF-023 | `/api/categories` works without login, contrary to the README | TC-API-012 | Minor | Low | Open |

Severity reflects impact: Critical = data loss, or a user loses access to their own data; Major = account integrity broken, or a server error on ordinary input; Moderate = wrong behaviour or a crash on unusual input; Minor = wrong status code or documentation mismatch with little consequence. Priority reflects how likely and visible the problem is.

### 5.3 Defect records

Common environment for all records: see [0.5](#05-environment). Every defect was seen in the full run and again in the screenshot re-run.

#### DEF-014 - Any logged-in user can delete another user's task through the API

| Field | Value |
| --- | --- |
| Defect ID | DEF-014 |
| Title | `DELETE /api/tasks/<id>` deletes any user's task |
| Affected Feature | REST API - delete task; REQ-008 user separation |
| Environment | See 0.5 |
| Preconditions | Users A and B exist; user A owns task N |
| Steps to Reproduce | 1. Logged in as user B, send `DELETE /api/tasks/N`.<br>2. Log in as user A and send `GET /api/tasks/N`. |
| Expected Result | Step 1 returns 404 (as `GET` and `PUT` already do for another user's task) and A's task is kept |
| Actual Result | Step 1 returns `200 {"result": "ok"}`; step 2 returns 404 - user A's task has been deleted by user B. The web delete is not affected (TC-WEB-013) |
| Severity | Critical |
| Priority | High |
| Evidence | TC-API-040a/b; [TC-API-040-cross-user-delete-20261124.jpg](evidences/TC-API-040-cross-user-delete-20261124.jpg). By code inspection: `api_delete_task` deletes `WHERE id = ?` without checking `user_id` (`app.py`, near line 459) |
| Status | Open |

#### DEF-015 - An invalid due date is saved and then makes that user's task list and dashboard return 500

| Field | Value |
| --- | --- |
| Defect ID | DEF-015 |
| Title | Due date is not validated; one bad value breaks every task view for that user |
| Affected Feature | Create/update task (API and web form), task list, dashboard; REQ-003, REQ-006, REQ-007 |
| Environment | See 0.5 |
| Preconditions | User logged in |
| Steps to Reproduce | 1. `POST /api/tasks` with `{"title": "bad date", "due_date": "31/12/2026"}` (or submit the web form with text in the due date).<br>2. `GET /api/tasks` and `GET /api/dashboard`, or open `/` and `/dashboard`. |
| Expected Result | Step 1 rejected with 400 and nothing saved; step 2 loads normally |
| Actual Result | Step 1 returns 500 through the API (302 on the web), **but the task is saved**. From then on every request in step 2 returns 500 Internal Server Error for that user (`ValueError: time data ... does not match format '%Y-%m-%d'`). `PUT` with a bad date behaves the same. `2026-02-30` and `tomorrow` behave the same. The normal UI gives the user no way to fix it |
| Severity | Critical - the user loses access to their task list and dashboard |
| Priority | High |
| Evidence | TC-API-019a-c, 036f, TC-WEB-011a-b; [TC-API-019-invalid-due-date-500](evidences/TC-API-019-invalid-due-date-500-20261124.jpg), [TC-API-019c-036f-invalid-due-date](evidences/TC-API-019c-036f-invalid-due-date-20261124.jpg), [TC-WEB-011-web-bad-date-500](evidences/TC-WEB-011-web-bad-date-500-20261124.jpg), [DEF-015-user-locked-out-after-bad-date](evidences/DEF-015-user-locked-out-after-bad-date-20261124.jpg) (a later, unrelated request by the same user also returns 500, with the traceback) |
| Status | Open |

#### DEF-016 - Registration accepts a username that already exists

| Field | Value |
| --- | --- |
| Defect ID | DEF-016 |
| Title | Duplicate usernames can be registered (API and web) |
| Affected Feature | Registration; REQ-001 |
| Environment | See 0.5 |
| Preconditions | Account `X` exists |
| Steps to Reproduce | 1. `POST /api/register` with username `X` and password `Different99` (or the web registration form). |
| Expected Result | Refused: 409 or 400 (API) / form shown again with an error (web) |
| Actual Result | API: 201 with a new id and the same username. Web: 302, logged in as the new account. By code inspection, login always matches the first account named `X`, so the second account cannot log in again after its session ends |
| Severity | Major |
| Priority | High |
| Evidence | TC-API-008a, TC-WEB-016; [TC-API-008-duplicate-username-accepted](evidences/TC-API-008-duplicate-username-accepted-20261124.jpg), [TC-WEB-010-012-016-web-form-validation](evidences/TC-WEB-010-012-016-web-form-validation-20261124.jpg) |
| Status | Open |

#### DEF-017 - API search text containing an apostrophe causes a 500 error

| Field | Value |
| --- | --- |
| Defect ID | DEF-017 |
| Title | `GET /api/tasks?q=O'Brien` returns 500 |
| Affected Feature | API task search; REQ-005 |
| Environment | See 0.5 |
| Preconditions | User logged in with a task titled `Call O'Brien` |
| Steps to Reproduce | 1. `GET /api/tasks?q=O'Brien` |
| Expected Result | 200 with the matching task (the web search does this, TC-WEB-015) |
| Actual Result | 500; the error page shows `sqlite3.OperationalError: near "Brien": syntax error` |
| Severity | Major - ordinary text breaks search, and the cause points to SQL injection (see Week 5 hand-off) |
| Priority | High |
| Evidence | TC-API-030; [TC-API-030-apostrophe-search-500](evidences/TC-API-030-apostrophe-search-500-20261124.jpg). By code inspection: the search text is put into the SQL string with an f-string (`app.py`, near line 379) instead of a `?` parameter |
| Status | Open |

#### DEF-018 - Wrong JSON data types cause 500 errors instead of 400

| Field | Value |
| --- | --- |
| Defect ID | DEF-018 |
| Title | Non-text field values crash the API |
| Affected Feature | `POST /api/register`, `POST /api/tasks`, `PUT /api/tasks/<id>`; REQ-009 |
| Environment | See 0.5 |
| Preconditions | User logged in (task endpoints) |
| Steps to Reproduce | 1. `POST /api/register` with `{"username": 12345, ...}`.<br>2. `POST /api/tasks` with `{"title": 123}`, `{"title": ["a","b"]}` or `{"title": "ok", "description": {"a": 1}}`.<br>3. `PUT /api/tasks/<id>` with `{"title": null}`. |
| Expected Result | 400 with a JSON error; nothing saved |
| Actual Result | 500 with an HTML error page every time (e.g. `AttributeError: 'int' object has no attribute 'strip'`) |
| Severity | Moderate |
| Priority | Medium |
| Evidence | TC-API-007, 018a-c, 036d; [TC-API-007-username-number-500](evidences/TC-API-007-username-number-500-20261124.jpg), [TC-API-036a-d-update-not-validated](evidences/TC-API-036a-d-update-not-validated-20261124.jpg) |
| Status | Open |

#### DEF-019 - Task create/update accepts a category that does not exist

| Field | Value |
| --- | --- |
| Defect ID | DEF-019 |
| Title | `category_id` is not validated |
| Affected Feature | Create/update task (API and web form); REQ-003 |
| Environment | See 0.5 |
| Preconditions | User logged in |
| Steps to Reproduce | 1. `POST /api/tasks` with `{"title": "bad category", "category_id": 999}` (also `"abc"`), or the web form with `category_id=999`. |
| Expected Result | Rejected (400 / form error) |
| Actual Result | Saved (201 / 302) with `category_id: 999` and `category: null`; the task then matches no category filter. `PUT` with `999` is also accepted |
| Severity | Moderate |
| Priority | Medium |
| Evidence | TC-API-020a-b, 036e, TC-WEB-012; [TC-API-020a-unknown-category-accepted](evidences/TC-API-020a-unknown-category-accepted-20261124.jpg), [TC-API-036e-update-unknown-category](evidences/TC-API-036e-update-unknown-category-20261124.jpg) |
| Status | Open |

#### DEF-020 - Task update skips title validation and treats the text "false" as done

| Field | Value |
| --- | --- |
| Defect ID | DEF-020 |
| Title | `PUT /api/tasks/<id>` does not apply the create rules |
| Affected Feature | API update task; REQ-003, REQ-004 |
| Environment | See 0.5 |
| Preconditions | User owns an open task titled `Stable title` |
| Steps to Reproduce | 1. `PUT /api/tasks/<id>` with `{"title": ""}` (also `"   "`).<br>2. On a fresh open task, `PUT` with `{"done": "false"}`. |
| Expected Result | 400 and the task unchanged in both steps |
| Actual Result | Step 1: 200 and the title becomes blank, although `POST` rejects the same value (TC-API-016). Step 2: 200 and the task is marked **done**, because any non-empty text counts as true |
| Severity | Moderate |
| Priority | Medium |
| Evidence | TC-API-036a-c; [TC-API-036a-d-update-not-validated](evidences/TC-API-036a-d-update-not-validated-20261124.jpg) |
| Status | Open |

#### DEF-021 - Deleting a task that does not exist reports success

| Field | Value |
| --- | --- |
| Defect ID | DEF-021 |
| Title | `DELETE /api/tasks/999999999` returns 200 |
| Affected Feature | API delete task; REQ-009 |
| Environment | See 0.5 |
| Preconditions | User logged in |
| Steps to Reproduce | 1. `DELETE /api/tasks/999999999` |
| Expected Result | 404 `{"error": "not found"}`, like `GET` and `PUT` |
| Actual Result | 200 `{"result": "ok"}`; a client cannot tell whether anything was deleted (this also hides DEF-014) |
| Severity | Minor |
| Priority | Low |
| Evidence | TC-API-041; [TC-API-041-delete-nonexistent-200](evidences/TC-API-041-delete-nonexistent-200-20261124.jpg) |
| Status | Open |

#### DEF-022 - Invalid paging values are not rejected

| Field | Value |
| --- | --- |
| Defect ID | DEF-022 |
| Title | `page` / `per_page` accept negative and non-numeric values |
| Affected Feature | API task list; REQ-005 |
| Environment | See 0.5 |
| Preconditions | User logged in with tasks |
| Steps to Reproduce | 1. `GET /api/tasks?per_page=-1`<br>2. `GET /api/tasks?page=-1`<br>3. `GET /api/tasks?page=abc` |
| Expected Result | 400 JSON error for each |
| Actual Result | 200 for each. `per_page=-1` removes the page limit (returns every task); `page=-1` and `page=abc` silently return the first page |
| Severity | Minor - `per_page=-1` allows unlimited result sets (relevant to Week 5 performance) |
| Priority | Low |
| Evidence | TC-API-032a-c; [TC-API-032a-paging-not-validated](evidences/TC-API-032a-paging-not-validated-20261124.jpg) |
| Status | Open |

#### DEF-023 - `/api/categories` works without login, contrary to the README

| Field | Value |
| --- | --- |
| Defect ID | DEF-023 |
| Title | Categories endpoint has no authentication check |
| Affected Feature | API categories; REQ-009 |
| Environment | See 0.5 |
| Preconditions | Not logged in |
| Steps to Reproduce | 1. `GET /api/categories` with no session cookie |
| Expected Result | 401, per the README ("session-cookie authentication except register and login") |
| Actual Result | 200 with the four categories. The data is not sensitive; the defect is that the code and the documentation disagree, so one of them should change |
| Severity | Minor |
| Priority | Low |
| Evidence | TC-API-012; [TC-API-012-categories-without-login](evidences/TC-API-012-categories-without-login-20261124.jpg) |
| Status | Open |

#### Week 1 defects reproduced this week

| Defect | Week 4 observation | Evidence |
| --- | --- | --- |
| DEF-001 | `POST /api/register` with the 8-character password `abcd1234` returns 400 `invalid password` - the API has the same off-by-one as the web form | [TC-API-005](evidences/TC-API-005-password-8-chars-rejected-20261124.jpg) |
| DEF-002 | A task due today is returned with `"urgency": "Overdue"`, and the API dashboard counts it as overdue (TC-API-043) | [TC-API-021b](evidences/TC-API-021b-due-today-overdue-20261124.jpg) |
| DEF-003 | Extended: besides spaces, an **empty** title is also saved when the browser's `required` check is bypassed. The API rejects both (TC-API-016), so the rule is missing only on the web side | [TC-WEB-010-012-016](evidences/TC-WEB-010-012-016-web-form-validation-20261124.jpg) |

### 5.4 Observations (not logged as defects)

| ID | Observation | Why not a defect |
| --- | --- | --- |
| OBS-W4-01 | There is no `/api/logout`; an API client ends a session only by dropping the cookie | Not documented as a feature |
| OBS-W4-02 | 404 and 405 responses for unknown API routes and methods are HTML pages, while the app's own errors are JSON | Status codes are correct; only the body format differs |
| OBS-W4-03 | Paging starts at `page=0`; the README does not say so | Behaviour is consistent; documentation gap |
| OBS-W4-04 | Editing, completing or deleting someone else's task on the web silently redirects to `/` with no message | Secure outcome (TC-WEB-013 passes); usability note for Week 3 |
| OBS-W4-05 | 500 responses show the full Python traceback with file paths, because the server runs with `debug=True` | Information disclosure; handed to Week 5 (below) |

### 5.5 Recommendations for Week 6 (automation in pytest)

The Week 6 owner should automate the API checks first: they have clear status codes and JSON to assert, they are fast and stable, and they cover the most serious defects. Recommended approach: the same pattern Week 2 uses (Flask `app.test_client()` with a temporary database), so no server is needed and the real database is never touched. One pytest test per Week 4 case ID keeps the manual-to-automated traceability the brief asks for.

| Priority | Week 4 cases | What the automated test should check | Why automate |
| --- | --- | --- | --- |
| 1 | TC-API-040, 024, 033, 037, 044, TC-WEB-013 | One user can never read, change, list or delete another user's task | Critical (DEF-014); a regression here leaks or destroys data |
| 1 | TC-API-011, 012, TC-WEB-004 | Every protected endpoint and page refuses a visitor who is not logged in | Critical path, cheap to run after every change |
| 1 | All 18 failing cases | The expected behaviour, marked `@pytest.mark.xfail(strict=True, reason="DEF-0xx")` | The suite stays green while defects are open and fails loudly the day a fix lands, prompting the test update; proves each fix |
| 2 | TC-API-003 to 007, 016 to 020, 036 | Input validation for every field: valid and invalid partitions, wrong types, nothing saved after a rejection | Many similar inputs - ideal for `@pytest.mark.parametrize`; high regression value |
| 2 | TC-API-021, 042, 043 | Urgency boundaries and dashboard counts with dates computed relative to today | Date logic breaks easily; compute dates in the test (or freeze time) so results are stable |
| 3 | TC-API-014, 015, 022, 034, 035, 039, TC-WEB-005 to 009, 014 | Create/read/update/delete round trips and web-API consistency | Core workflow smoke tests |
| Do not automate in pytest | TC-WEB-010 to 012 browser screenshots | Manual DevTools evidence | Needs a real browser; belongs with Week 3's Playwright scripts if needed |

Until the pytest suite exists, the Postman collection can already serve as a regression run from the command line with Newman (see [0.7](#07-how-to-re-run-the-suite)).

### 5.6 Hand-offs to other phases

| Phase | Item |
| --- | --- |
| Week 5 - Security | DEF-017: search text is built into SQL (`app.py` near line 379) - assess SQL injection safely on a local copy. DEF-014: broken authorisation (Tampering / Elevation of privilege in STRIDE). OBS-W4-05: `debug=True` exposes tracebacks and file paths. DEF-016: duplicate usernames (Spoofing). Web forms have no CSRF token |
| Week 5 - Performance | Busiest endpoints: `GET /api/tasks` and `GET /api/dashboard` (urgency is computed for every task on every call). DEF-022: `per_page=-1` returns the whole list |
| Week 6 - Automation | Section 5.5 |
| Week 7 - Test management | Add REQ-009 and the rows in [2.2](#22-requirements-traceability-week-4-rows) to the master RTM; add DEF-014 to DEF-023 to the consolidated defect log |
| Week 8 - Metrics | Counts in [5.1](#51-execution-summary). New defects by severity: 2 Critical, 2 Major, 3 Moderate, 3 Minor. All 10 new defects affect the API; 3 of them (DEF-015, 016, 019) also affect the web forms |

### 5.7 Limitations

- The web cases send real form submissions to the server but do not render pages in a browser; layout and browser behaviour were covered in Weeks 1 and 3.
- One recorded full run on one Windows machine, plus targeted re-runs for screenshots.
- Expected error codes (400 / 404 / 409) are a team assumption, because the README does not define an error contract ([0.3](#03-test-basis)).
- Not tested this week: concurrent requests, very large payloads, non-ASCII input, session expiry and attack payloads (Week 5).
