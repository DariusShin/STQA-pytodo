# Week 4 - Request and Test Data

This file describes the data used by the Week 4 Postman collection and explains how each value was chosen. The exact payload of every request is stored in the collection itself ([postman/PyTodo_Pro_Week4.postman_collection.json](postman/PyTodo_Pro_Week4.postman_collection.json)): open a request in Postman and look at its **Body**, **Params** and **Scripts** tabs.

## Accounts

| Item | Value | Reason |
| --- | --- | --- |
| Username pattern | `w4` + role letter + last 8 digits of the clock + 2 random digits, e.g. `w4a9888108439` (13 characters), set by each register request's pre-request script | Valid under the 3-20 character rule; unique on every run, so re-runs never collide with existing accounts |
| Password | `Test12345` (9 characters) | The same synthetic password as Weeks 1 and 3. It is valid under the stated rule (8 or more) and also under the current, defective implementation (more than 8, DEF-001), so account setup never depends on that defect |
| Roles | `user_a` (main API user), `list_user`, `dash_user`, `owner` / `intruder`, `web_user`, `web_owner` / `web_intruder`, and a fresh user per invalid-date case | Each folder registers the users it needs, so folders can be run on their own. Postman keeps one session cookie; SETUP register/log-in requests switch who the following requests run as |
| Logged-out visitor | Requests with **Settings → Disable cookie jar** | Sends no session cookie and stores none |

The recorded run started from an empty database (`pytodo_pro.db` deleted before starting the server). Every run adds `w4…` accounts and tasks; delete `pytodo_pro.db` to start clean.

## Dates

All due dates are computed at run time by the collection-level pre-request script, relative to the machine's current date: `{{minus3}}`, `{{minus2}}`, `{{yesterday}}`, `{{today}}`, `{{plus1}}` … `{{plus6}}`, `{{plus9}}` (format `YYYY-MM-DD`). The suite therefore gives the same verdicts on any day, as Week 1 did for urgency. The recorded run date was 2026-11-24.

## Input partitions and boundaries

### Registration (`POST /api/register`, `POST /register`)

| Field | Valid partitions / boundaries | Invalid partitions / boundaries | Cases |
| --- | --- | --- | --- |
| username | 3 chars (min), 11 chars (typical), 20 chars (max) | 2 chars, 21 chars, `bad-name` (illegal `-`), empty or missing, number `12345` (wrong type), existing username | TC-API-001 to 003, 007, 008; TC-WEB-001, 002, 016 |
| password | 8 chars (min) `abcd1234`, 9 chars `Test12345` | 7 chars `abc1234`, missing | TC-API-004 to 006; TC-WEB-002 |

### Login (`POST /api/login`, `POST /login`)

| Username | Password | Expected | Cases |
| --- | --- | --- | --- |
| registered | correct | 200 / redirect to `/` | TC-API-009, TC-WEB-003 |
| registered | wrong (`Wrong12345`) | 401 / error message | TC-API-010, TC-WEB-003 |
| unknown | any | 401 | TC-API-010 |
| missing | missing (`{}`) | 401 | TC-API-010 |

### Task fields (`POST /api/tasks`, `PUT /api/tasks/<id>`, `POST /tasks/new`)

| Field | Valid | Invalid | Cases |
| --- | --- | --- | --- |
| title | any text with a non-whitespace character | missing, `""`, `"   "`, `null` (PUT), number `123`, list `["a","b"]` | TC-API-014 to 016, 018, 036; TC-WEB-010 |
| description | text, or omitted (defaults to `""`) | object `{"a": 1}` | TC-API-014, 015, 018 |
| category_id | 1-4 (seeded ids, looked up by name at run time), or omitted | `999` (no such category), `"abc"` | TC-API-020, 036; TC-WEB-012 |
| due_date | `YYYY-MM-DD` of a real date, or omitted | `31/12/2026` (wrong format), `2026-02-30` (impossible date), `tomorrow`, `not-a-date` | TC-API-019, 036; TC-WEB-011 |
| done (PUT) | `true`, `false` (JSON booleans) | `"false"` (string) | TC-API-035, 036 |
| request body | JSON object | form-encoded body sent to the JSON API | TC-API-017 |

### Urgency boundaries (helpers.py specification)

| Due date | Expected urgency | Case |
| --- | --- | --- |
| today-1 | Overdue | TC-API-021 `yesterday` |
| today | Due Today | TC-API-021 `today`, TC-API-043 |
| today+1 | Due Soon | TC-API-021 `plus1` |
| today+2 | Due Soon | TC-API-021 `plus2` |
| today+3 | Upcoming | TC-API-021 `plus3` |

### Query parameters (`GET /api/tasks`, `GET /`)

| Parameter | Valid | Invalid | Cases |
| --- | --- | --- | --- |
| category | `Work` | - | TC-API-026, 029 |
| status | `open`, `done` | - | TC-API-027, 029 |
| q | `report`, `O'Brien` | - | TC-API-028 to 030, TC-WEB-015 |
| page / per_page | `page=0`, `page=1`, `page=2` with `per_page=2`; defaults | `per_page=-1`, `page=-1`, `page=abc` | TC-API-031, 032 |

### Resource ids

| Id | Meaning | Cases |
| --- | --- | --- |
| own task id | created by a SETUP request and saved in an environment variable | TC-API-022, 034, 035, 036, 039 |
| other user's task id | created by user A, requested by user B | TC-API-024, 037, 040; TC-WEB-013 |
| `999999999` | never exists | TC-API-023, 038, 041 |
| `abc` | not an integer | TC-API-025 |

## List dataset

Used by TC-API-026 to 032 (folder **04 List, filter, search, paging**). It is created for a fresh `list_user` by the folder's SETUP requests.

| Key | Title | Category | Status | Matches |
| --- | --- | --- | --- | --- |
| work_open | Weekly report | Work | Open | category=Work, status=open, q=report |
| work_done | Report archive | Work | Done | category=Work, status=done, q=report |
| personal_open | Buy groceries | Personal | Open | status=open |
| none_open | Read chapter 4 | - | Open | status=open |
| apostrophe | Call O'Brien | - | Open | status=open, q=O'Brien |

## Dashboard dataset

Used by TC-API-042 and 043 (folder **08 Dashboard**). The expected values come from counting this table by hand, independently of the application. TC-WEB-014 uses a similar four-task set and compares the web page with the API instead of a fixed count.

| Task | Due date | Status | Counts towards |
| --- | --- | --- | --- |
| 1 | today-1 | Open | total, open, overdue |
| 2 | today+1 | Open | total, open, due_soon |
| 3 | today+5 | Open | total, open |
| 4 | none | Open | total, open |
| 5 | today-2 | Completed during the run | total, completed_this_week |

Expected: total 5, open 4, overdue 1, due_soon 1, completed_this_week 1. TC-API-043 then adds one open task due **today**: expected overdue stays 1.
