# Regression run 20261127-144931

| Item | Value |
| --- | --- |
| run_started | 2026-11-27T14:49:31 |
| run_finished | 2026-11-27T14:49:52 |
| wall_time_s | 21.4 |
| timezone | Malay Peninsula Standard Time |
| execution_date_used_for_due_dates | 2026-11-27 |
| app_commit | f34f7e0 |
| browser | none (no browser check selected) |
| headless | True |
| selenium | 4.53.0 |
| pytest | 9.2.0 |
| python | 3.14.7 |
| os | Windows 11 (10.0.26200) |
| target | isolated server on port 5006 |
| run_label | api-run3 |
| marker_expression | api |
| defects_as_failures | False |
| pytest_exit_status | 0 |
| counts | {'Pass': 69, 'Fail (known defect)': 32} |

| Auto ID | Manual case(s) | Requirement | Known defect | Smoke | Status | Time (s) | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-AUT-029 | TC-API-001 | REQ-001 | - |  | Pass | 0.16 |  |
| TC-AUT-030 | TC-API-002 | REQ-001 | - |  | Pass | 0.17 |  |
| TC-AUT-030 | TC-API-002 | REQ-001 | - |  | Pass | 0.17 |  |
| TC-AUT-031 | TC-API-003 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-031 | TC-API-003 | REQ-001 | - |  | Pass | 0.01 |  |
| TC-AUT-031 | TC-API-003 | REQ-001 | - |  | Pass | 0.01 |  |
| TC-AUT-031 | TC-API-003 | REQ-001 | - |  | Pass | 0.03 |  |
| TC-AUT-032 | TC-API-004 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-033 | TC-API-005 | REQ-001 | DEF-001 |  | Fail (known defect) | 0.01 | AssertionError: 8-character password: <400 application/json '{"error":"invalid password"} '> |
| TC-AUT-034 | TC-API-006 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-035 | TC-API-007 | REQ-001, REQ-009 | DEF-018 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-036 | TC-API-008 | REQ-001 | DEF-016 |  | Fail (known defect) | 0.15 | AssertionError: duplicate username 'w6_api_1449317' was accepted: <201 application/json '{"id":5,"username":"w6_api_1449317"} '> |
| TC-AUT-037 | TC-API-009 | REQ-002 | - |  | Pass | 0.14 |  |
| TC-AUT-038 | TC-API-010 | REQ-002 | - |  | Pass | 0.18 |  |
| TC-AUT-038 | TC-API-010 | REQ-002 | - |  | Pass | 0.03 |  |
| TC-AUT-038 | TC-API-010 | REQ-002 | - |  | Pass | 0.03 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.0 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.0 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-040 | TC-API-012 | REQ-009 | DEF-023 |  | Fail (known defect) | 0.01 | AssertionError: categories without login: <200 application/json '[{"id":2,"name":"Personal"},{"id":3,"name":"Study"},{"id":4,"name":"Urgent"},{"id":1,"name":"Work"}] '> |
| TC-AUT-041 | TC-API-013 | REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-042 | TC-API-014 | REQ-003 | - |  | Pass | 0.05 |  |
| TC-AUT-043 | TC-API-015 | REQ-003 | - |  | Pass | 0.01 |  |
| TC-AUT-044 | TC-API-016 | REQ-003 | - |  | Pass | 0.01 |  |
| TC-AUT-044 | TC-API-016 | REQ-003 | - |  | Pass | 0.04 |  |
| TC-AUT-044 | TC-API-016 | REQ-003 | - |  | Pass | 0.01 |  |
| TC-AUT-045 | TC-API-017 | REQ-009 | - |  | Pass | 0.03 |  |
| TC-AUT-046 | TC-API-018 | REQ-003, REQ-009 | DEF-018 |  | Fail (known defect) | 0.03 | AssertionError: expected 400 with a JSON error, got <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-046 | TC-API-018 | REQ-003, REQ-009 | DEF-018 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-046 | TC-API-018 | REQ-003, REQ-009 | DEF-018 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-047 | TC-API-019 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.06 | AssertionError: due_date '31/12/2026': create returned <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; list/dashboard then returned (500, 500) |
| TC-AUT-047 | TC-API-019 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.03 | AssertionError: due_date '2026-02-30': create returned <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; list/dashboard then returned (500, 500) |
| TC-AUT-047 | TC-API-019 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.08 | AssertionError: due_date 'tomorrow': create returned <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; list/dashboard then returned (500, 500) |
| TC-AUT-048 | TC-API-020 | REQ-003 | DEF-019 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <201 application/json '{"category":null,"category_id":999,"completed_at":null,"created_at":"2026-11-27T14:49:39.273989","description":"","done"'> |
| TC-AUT-048 | TC-API-020 | REQ-003 | DEF-019 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <201 application/json '{"category":null,"category_id":"abc","completed_at":null,"created_at":"2026-11-27T14:49:39.481725","description":"","don'> |
| TC-AUT-049 | TC-API-021 | REQ-006 | - |  | Pass | 0.01 |  |
| TC-AUT-049 | TC-API-021 | REQ-006 | DEF-002 |  | Fail (known defect) | 0.01 | AssertionError: due 2026-11-27: urgency 'Overdue' |
| TC-AUT-049 | TC-API-021 | REQ-006 | - |  | Pass | 0.01 |  |
| TC-AUT-049 | TC-API-021 | REQ-006 | - |  | Pass | 0.02 |  |
| TC-AUT-049 | TC-API-021 | REQ-006 | - |  | Pass | 0.03 |  |
| TC-AUT-050 | TC-API-022 | REQ-003 | - |  | Pass | 0.03 |  |
| TC-AUT-051 | TC-API-023 | REQ-003, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-052 | TC-API-024 | REQ-008 | - |  | Pass | 0.03 |  |
| TC-AUT-053 | TC-API-025 | REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-054 | TC-API-026 | REQ-005 | - |  | Pass | 0.01 |  |
| TC-AUT-055 | TC-API-027 | REQ-005 | - |  | Pass | 0.01 |  |
| TC-AUT-055 | TC-API-027 | REQ-005 | - |  | Pass | 0.01 |  |
| TC-AUT-056 | TC-API-028 | REQ-005 | - |  | Pass | 0.01 |  |
| TC-AUT-057 | TC-API-029 | REQ-005 | - |  | Pass | 0.01 |  |
| TC-AUT-058 | TC-API-030 | REQ-005 | DEF-017 |  | Fail (known defect) | 0.01 | AssertionError: search for O'Brien: <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-059 | TC-API-031 | REQ-005, REQ-009 | - |  | Pass | 0.11 |  |
| TC-AUT-060 | TC-API-032 | REQ-009 | DEF-022 |  | Fail (known defect) | 0.04 | AssertionError: expected 400 with a JSON error, got <200 application/json '[{"category":null,"category_id":null,"completed_at":null,"created_at":"2026-11-27T14:49:42.383435","description":"","don'> |
| TC-AUT-060 | TC-API-032 | REQ-009 | DEF-022 |  | Fail (known defect) | 0.1 | AssertionError: expected 400 with a JSON error, got <200 application/json '[{"category":null,"category_id":null,"completed_at":null,"created_at":"2026-11-27T14:49:42.655235","description":"","don'> |
| TC-AUT-060 | TC-API-032 | REQ-009 | DEF-022 |  | Fail (known defect) | 0.06 | AssertionError: expected 400 with a JSON error, got <200 application/json '[{"category":null,"category_id":null,"completed_at":null,"created_at":"2026-11-27T14:49:42.904400","description":"","don'> |
| TC-AUT-061 | TC-API-033 | REQ-008 | - |  | Pass | 0.18 |  |
| TC-AUT-062 | TC-API-034 | REQ-003 | - |  | Pass | 0.05 |  |
| TC-AUT-063 | TC-API-035 | REQ-004 | - |  | Pass | 0.06 |  |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-020 |  | Fail (known defect) | 0.07 | AssertionError: PUT {'title': ''}: <200 application/json '{"category":"Work","category_id":1,"completed_at":null,"created_at":"2026-11-27T14:49:43.767373","description":"","done"'>; task afterwards: 200 {'title': '', 'done': False, 'category_id': 1, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-020 |  | Fail (known defect) | 0.06 | AssertionError: PUT {'title': '   '}: <200 application/json '{"category":"Work","category_id":1,"completed_at":null,"created_at":"2026-11-27T14:49:44.049543","description":"","done"'>; task afterwards: 200 {'title': '   ', 'done': False, 'category_id': 1, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-020 |  | Fail (known defect) | 0.04 | AssertionError: PUT {'done': 'false'}: <200 application/json '{"category":"Work","category_id":1,"completed_at":"2026-11-27 14:49:44","created_at":"2026-11-27T14:49:44.291687","descr'>; task afterwards: 200 {'title': 'Stable title', 'done': True, 'category_id': 1, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-018 |  | Fail (known defect) | 0.05 | AssertionError: PUT {'title': None}: <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; task afterwards: 200 {'title': 'Stable title', 'done': False, 'category_id': 1, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-019 |  | Fail (known defect) | 0.03 | AssertionError: PUT {'category_id': 999}: <200 application/json '{"category":null,"category_id":999,"completed_at":null,"created_at":"2026-11-27T14:49:44.749558","description":"","done"'>; task afterwards: 200 {'title': 'Stable title', 'done': False, 'category_id': 999, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-015 |  | Fail (known defect) | 0.07 | AssertionError: PUT {'due_date': '31/12/2026'}: <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; task afterwards: 500 None |
| TC-AUT-065 | TC-API-037 | REQ-008 | - |  | Pass | 0.06 |  |
| TC-AUT-066 | TC-API-038 | REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-067 | TC-API-039 | REQ-003 | - |  | Pass | 0.06 |  |
| TC-AUT-068 | TC-API-040 | REQ-008 | DEF-014 |  | Fail (known defect) | 0.04 | AssertionError: intruder DELETE returned 200; owner's GET afterwards returned 404 |
| TC-AUT-069 | TC-API-041 | REQ-009 | DEF-021 |  | Fail (known defect) | 0.03 | AssertionError: expected 404 with a JSON error, got <200 application/json '{"result":"ok"} '> |
| TC-AUT-070 | TC-API-042 | REQ-007 | - |  | Pass | 0.1 |  |
| TC-AUT-071 | TC-API-043 | REQ-006, REQ-007 | DEF-002 |  | Fail (known defect) | 0.12 | AssertionError: Overdue counter is 2, expected 1 |
| TC-AUT-072 | TC-API-044 | REQ-008 | - |  | Pass | 0.38 |  |
| TC-AUT-073 | TC-API-045 | REQ-009 | - |  | Pass | 0.02 |  |
| TC-AUT-074 | TC-WEB-001 | REQ-001 | - |  | Pass | 0.17 |  |
| TC-AUT-075 | TC-WEB-002 | REQ-001 | - |  | Pass | 0.01 |  |
| TC-AUT-075 | TC-WEB-002 | REQ-001 | - |  | Pass | 0.02 |  |
| TC-AUT-075 | TC-WEB-002 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-076 | TC-WEB-003 | REQ-002 | - |  | Pass | 0.32 |  |
| TC-AUT-076 | TC-WEB-003 | REQ-002 | - |  | Pass | 0.32 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.01 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.0 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.0 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.01 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.01 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.0 |  |
| TC-AUT-078 | TC-WEB-005 | REQ-003 | - |  | Pass | 0.03 |  |
| TC-AUT-079 | TC-WEB-006 | REQ-003, REQ-006 | - |  | Pass | 0.23 |  |
| TC-AUT-080 | TC-WEB-007 | REQ-003 | - |  | Pass | 0.21 |  |
| TC-AUT-081 | TC-WEB-008 | REQ-004 | - |  | Pass | 0.24 |  |
| TC-AUT-082 | TC-WEB-009 | REQ-003 | - |  | Pass | 0.2 |  |
| TC-AUT-083 | TC-WEB-010 | REQ-003 | DEF-003 |  | Fail (known defect) | 0.02 | AssertionError: server accepted the form: 302 redirect to /; saved titles: [''] |
| TC-AUT-083 | TC-WEB-010 | REQ-003 | DEF-003 |  | Fail (known defect) | 0.02 | AssertionError: server accepted the form: 302 redirect to /; saved titles: [''] |
| TC-AUT-084 | TC-WEB-011 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.07 | AssertionError: server accepted the form: 302 redirect to /; / and /dashboard then returned (500, 500) |
| TC-AUT-084 | TC-WEB-011 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.05 | AssertionError: server accepted the form: 302 redirect to /; / and /dashboard then returned (500, 500) |
| TC-AUT-085 | TC-WEB-012 | REQ-003 | DEF-019 |  | Fail (known defect) | 0.04 | AssertionError: server accepted the form: 302 redirect to /; saved: [('bad category', 999)] |
| TC-AUT-086 | TC-WEB-013 | REQ-008 | - |  | Pass | 0.46 |  |
| TC-AUT-087 | TC-WEB-014 | REQ-007 | - |  | Pass | 0.26 |  |
| TC-AUT-088 | TC-WEB-015 | REQ-005 | - |  | Pass | 0.22 |  |
| TC-AUT-089 | TC-WEB-016 | REQ-001 | DEF-016 |  | Fail (known defect) | 0.31 | AssertionError: duplicate username 'w6_web_14493183' was accepted: 302 redirect to / |
