# Week 4 - Defects

Defects first found in Week 4, in the project Defect Report Template, followed by earlier defects re-tested this week. Environment for all records: Windows 11 25H2, Python 3.14, Flask 3.0.3, `python app.py` at `http://127.0.0.1:5000`, Postman 12.38.2; 2026-11-24. Every defect was seen in the full run and again in the screenshot re-run.

| Defect | Title | Severity / Priority | Status |
| --- | --- | --- | --- |
| [DEF-014](#def-014---any-logged-in-user-can-delete-another-users-task-through-the-api) | Any logged-in user can delete another user's task through the API | Critical / High | Open |
| [DEF-015](#def-015---an-invalid-due-date-is-saved-and-then-breaks-that-users-task-list-and-dashboard) | An invalid due date is saved and then breaks that user's task list and dashboard | Critical / High | Open |
| [DEF-016](#def-016---registration-accepts-a-username-that-already-exists) | Registration accepts a username that already exists | Major / High | Open |
| [DEF-017](#def-017---api-search-text-containing-an-apostrophe-causes-a-500-error) | API search text containing an apostrophe causes a 500 error | Major / High | Open |
| [DEF-018](#def-018---wrong-json-data-types-cause-500-errors-instead-of-400) | Wrong JSON data types cause 500 errors instead of 400 | Moderate / Medium | Open |
| [DEF-019](#def-019---task-createupdate-accepts-a-category-that-does-not-exist) | Task create/update accepts a category that does not exist | Moderate / Medium | Open |
| [DEF-020](#def-020---task-update-skips-title-validation-and-treats-the-text-false-as-done) | Task update skips title validation and treats the text "false" as done | Moderate / Medium | Open |
| [DEF-021](#def-021---deleting-a-task-that-does-not-exist-reports-success) | Deleting a task that does not exist reports success | Minor / Low | Open |
| [DEF-022](#def-022---invalid-paging-values-are-not-rejected) | Invalid paging values are not rejected | Minor / Low | Open |
| [DEF-023](#def-023---apicategories-works-without-login-contrary-to-the-readme) | `/api/categories` works without login, contrary to the README | Minor / Low | Open |

## DEF-014 - Any logged-in user can delete another user's task through the API

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-014 |
| Title | `DELETE /api/tasks/<id>` deletes any user's task |
| Affected Feature | REST API - delete task; REQ-008 user separation |
| Environment | See above |
| Preconditions | Users A and B exist; user A owns task N |
| Steps to Reproduce | 1. Logged in as user B, send `DELETE /api/tasks/N`.<br>2. Log in as user A and send `GET /api/tasks/N`. |
| Expected Result | Step 1 returns 404 (as `GET` and `PUT` do for another user's task) and A's task is kept |
| Actual Result | Step 1 returns `200 {"result": "ok"}`; step 2 returns 404, so user A's task was deleted by user B. The web delete is not affected (TC-WEB-013). Code: `api_delete_task` deletes `WHERE id = ?` without checking `user_id` (`app.py`, about line 459). |
| Severity | Critical |
| Priority | High |
| Evidence | TC-API-040a/b; [TC-API-040-cross-user-delete-20261124.jpg](evidences/TC-API-040-cross-user-delete-20261124.jpg) |
| Status | Open |

## DEF-015 - An invalid due date is saved and then breaks that user's task list and dashboard

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-015 |
| Title | Due date is not validated; one bad value breaks every task view for that user |
| Affected Feature | Create/update task (API and web form), task list, dashboard; REQ-003, REQ-006, REQ-007 |
| Environment | See above |
| Preconditions | User logged in |
| Steps to Reproduce | 1. `POST /api/tasks` with `{"title": "bad date", "due_date": "31/12/2026"}` (or submit the web form with text in the due date).<br>2. `GET /api/tasks` and `GET /api/dashboard`, or open `/` and `/dashboard`. |
| Expected Result | Step 1 rejected with 400 and nothing saved; step 2 loads normally |
| Actual Result | Step 1 returns 500 (API) or 302 (web), **but the task is saved**. Every request in step 2 then returns 500 for that user (`ValueError: time data ... does not match format '%Y-%m-%d'`). `PUT` with a bad date, `2026-02-30` and `tomorrow` behave the same. The UI gives the user no way to fix it. |
| Severity | Critical - the user loses access to their task list and dashboard |
| Priority | High |
| Evidence | TC-API-019a-c, 036f, TC-WEB-011a-b; [TC-API-019](evidences/TC-API-019-invalid-due-date-500-20261124.jpg), [TC-API-019c/036f](evidences/TC-API-019c-036f-invalid-due-date-20261124.jpg), [TC-WEB-011](evidences/TC-WEB-011-web-bad-date-500-20261124.jpg), [user locked out](evidences/DEF-015-user-locked-out-after-bad-date-20261124.jpg) |
| Status | Open |

## DEF-016 - Registration accepts a username that already exists

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-016 |
| Title | Duplicate usernames can be registered (API and web) |
| Affected Feature | Registration; REQ-001 |
| Environment | See above |
| Preconditions | Account `X` exists |
| Steps to Reproduce | 1. `POST /api/register` with username `X` and password `Different99` (or use the web registration form). |
| Expected Result | Refused: 409 or 400 (API) / form shown again with an error (web) |
| Actual Result | API: 201 with a new id and the same username. Web: 302, logged in as the new account. Login always matches the first account named `X`, so the second account cannot log in again after its session ends. |
| Severity | Major |
| Priority | High |
| Evidence | TC-API-008a, TC-WEB-016; [TC-API-008](evidences/TC-API-008-duplicate-username-accepted-20261124.jpg), [TC-WEB-010/012/016](evidences/TC-WEB-010-012-016-web-form-validation-20261124.jpg) |
| Status | Open |

## DEF-017 - API search text containing an apostrophe causes a 500 error

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-017 |
| Title | `GET /api/tasks?q=O'Brien` returns 500 |
| Affected Feature | API task search; REQ-005 |
| Environment | See above |
| Preconditions | User logged in with a task titled `Call O'Brien` |
| Steps to Reproduce | 1. `GET /api/tasks?q=O'Brien` |
| Expected Result | 200 with the matching task (the web search does this, TC-WEB-015) |
| Actual Result | 500; the error page shows `sqlite3.OperationalError: near "Brien": syntax error`. The search text is inserted into the SQL string with an f-string (`app.py`, about line 379) instead of a `?` parameter. |
| Severity | Major - ordinary text breaks search, and the cause allows SQL injection (confirmed in Week 5, DEF-029) |
| Priority | High |
| Evidence | TC-API-030; [TC-API-030](evidences/TC-API-030-apostrophe-search-500-20261124.jpg) |
| Status | Open |

## DEF-018 - Wrong JSON data types cause 500 errors instead of 400

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-018 |
| Title | Non-text field values crash the API |
| Affected Feature | `POST /api/register`, `POST /api/tasks`, `PUT /api/tasks/<id>`; REQ-009 |
| Environment | See above |
| Preconditions | User logged in (task endpoints) |
| Steps to Reproduce | 1. `POST /api/register` with `{"username": 12345, ...}`.<br>2. `POST /api/tasks` with `{"title": 123}`, `{"title": ["a","b"]}` or `{"title": "ok", "description": {"a": 1}}`.<br>3. `PUT /api/tasks/<id>` with `{"title": null}`. |
| Expected Result | 400 with a JSON error; nothing saved |
| Actual Result | 500 with an HTML error page each time (e.g. `AttributeError: 'int' object has no attribute 'strip'`) |
| Severity | Moderate |
| Priority | Medium |
| Evidence | TC-API-007, 018a-c, 036d; [TC-API-007](evidences/TC-API-007-username-number-500-20261124.jpg), [TC-API-036a-d](evidences/TC-API-036a-d-update-not-validated-20261124.jpg) |
| Status | Open |

## DEF-019 - Task create/update accepts a category that does not exist

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-019 |
| Title | `category_id` is not validated |
| Affected Feature | Create/update task (API and web form); REQ-003 |
| Environment | See above |
| Preconditions | User logged in |
| Steps to Reproduce | 1. `POST /api/tasks` with `{"title": "bad category", "category_id": 999}` (also `"abc"`), or the web form with `category_id=999`. |
| Expected Result | Rejected (400 / form error) |
| Actual Result | Saved (201 / 302) with `category_id: 999` and `category: null`; the task then matches no category filter. `PUT` with `999` is also accepted. |
| Severity | Moderate |
| Priority | Medium |
| Evidence | TC-API-020a-b, 036e, TC-WEB-012; [TC-API-020a](evidences/TC-API-020a-unknown-category-accepted-20261124.jpg), [TC-API-036e](evidences/TC-API-036e-update-unknown-category-20261124.jpg) |
| Status | Open |

## DEF-020 - Task update skips title validation and treats the text "false" as done

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-020 |
| Title | `PUT /api/tasks/<id>` does not apply the create rules |
| Affected Feature | API update task; REQ-003, REQ-004 |
| Environment | See above |
| Preconditions | User owns an open task titled `Stable title` |
| Steps to Reproduce | 1. `PUT /api/tasks/<id>` with `{"title": ""}` (also `"   "`).<br>2. On a fresh open task, `PUT` with `{"done": "false"}`. |
| Expected Result | 400 and the task unchanged in both steps |
| Actual Result | Step 1: 200 and the title becomes blank, although `POST` rejects the same value (TC-API-016). Step 2: 200 and the task is marked **done**, because any non-empty text counts as true. |
| Severity | Moderate |
| Priority | Medium |
| Evidence | TC-API-036a-c; [TC-API-036a-d](evidences/TC-API-036a-d-update-not-validated-20261124.jpg) |
| Status | Open |

## DEF-021 - Deleting a task that does not exist reports success

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-021 |
| Title | `DELETE /api/tasks/999999999` returns 200 |
| Affected Feature | API delete task; REQ-009 |
| Environment | See above |
| Preconditions | User logged in |
| Steps to Reproduce | 1. `DELETE /api/tasks/999999999` |
| Expected Result | 404 `{"error": "not found"}`, like `GET` and `PUT` |
| Actual Result | 200 `{"result": "ok"}`; a client cannot tell whether anything was deleted (this also hides DEF-014) |
| Severity | Minor |
| Priority | Low |
| Evidence | TC-API-041; [TC-API-041](evidences/TC-API-041-delete-nonexistent-200-20261124.jpg) |
| Status | Open |

## DEF-022 - Invalid paging values are not rejected

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-022 |
| Title | `page` / `per_page` accept negative and non-numeric values |
| Affected Feature | API task list; REQ-005 |
| Environment | See above |
| Preconditions | User logged in with tasks |
| Steps to Reproduce | 1. `GET /api/tasks?per_page=-1`<br>2. `GET /api/tasks?page=-1`<br>3. `GET /api/tasks?page=abc` |
| Expected Result | 400 JSON error for each |
| Actual Result | 200 for each. `per_page=-1` removes the page limit and returns every task; `page=-1` and `page=abc` return the first page. |
| Severity | Minor |
| Priority | Low |
| Evidence | TC-API-032a-c; [TC-API-032a](evidences/TC-API-032a-paging-not-validated-20261124.png) |
| Status | Open |

## DEF-023 - `/api/categories` works without login, contrary to the README

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-023 |
| Title | Categories endpoint has no authentication check |
| Affected Feature | API categories; REQ-009 |
| Environment | See above |
| Preconditions | Not logged in |
| Steps to Reproduce | 1. `GET /api/categories` with no session cookie |
| Expected Result | 401, per the README ("session-cookie authentication except register and login") |
| Actual Result | 200 with the four categories. The data is not sensitive, but the code and the documentation disagree. |
| Severity | Minor |
| Priority | Low |
| Evidence | TC-API-012; [TC-API-012](evidences/TC-API-012-categories-without-login-20261124.jpg) |
| Status | Open |

## Re-tested defects

| Defect | Original record | Re-tested by | Result (2026-11-24) | Severity change |
| --- | --- | --- | --- | --- |
| DEF-001 | [Week 1](../01_Black_Box/defects.md#def-001---eight-character-password-is-rejected) | TC-API-005 | Still fails: the API returns 400 `invalid password` for `abcd1234` ([jpg](evidences/TC-API-005-password-8-chars-rejected-20261124.jpg)) | None |
| DEF-002 | [Week 1](../01_Black_Box/defects.md#def-002---today-is-classified-and-counted-as-overdue) | TC-API-021b, 043 | Still fails: API returns `"urgency": "Overdue"` and the API dashboard counts it as overdue ([jpg](evidences/TC-API-021b-due-today-overdue-20261124.jpg)) | None |
| DEF-003 | [Week 1](../01_Black_Box/defects.md#def-003---whitespace-only-title-creates-a-task-with-a-blank-displayed-title) | TC-WEB-010 | Still fails, and wider: an **empty** title is also saved when `required` is bypassed. The API rejects both (TC-API-016), so the rule is missing only on the web side ([jpg](evidences/TC-WEB-010-012-016-web-form-validation-20261124.jpg)) | None |
