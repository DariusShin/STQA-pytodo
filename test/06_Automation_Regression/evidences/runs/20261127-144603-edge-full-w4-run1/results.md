# Regression run 20261127-144603

| Item | Value |
| --- | --- |
| run_started | 2026-11-27T14:46:03 |
| run_finished | 2026-11-27T14:47:27 |
| wall_time_s | 84.4 |
| timezone | Malay Peninsula Standard Time |
| execution_date_used_for_due_dates | 2026-11-27 |
| app_commit | f34f7e0 |
| browser | MicrosoftEdge 158.0.4370.45 |
| headless | True |
| selenium | 4.53.0 |
| pytest | 9.2.0 |
| python | 3.14.7 |
| os | Windows 11 (10.0.26200) |
| target | isolated server on port 5006 |
| run_label | full-w4-run1 |
| marker_expression | (all) |
| defects_as_failures | False |
| pytest_exit_status | 0 |
| counts | {'Pass': 127, 'Fail (known defect)': 39} |

| Auto ID | Manual case(s) | Requirement | Known defect | Smoke | Status | Time (s) | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-AUT-001 | TC-BB-001 | REQ-001 | - |  | Pass | 0.67 |  |
| TC-AUT-001 | TC-BB-002 | REQ-001 | - |  | Pass | 0.67 |  |
| TC-AUT-001 | TC-BB-003 | REQ-001 | - |  | Pass | 0.57 |  |
| TC-AUT-001 | TC-BB-004 | REQ-001 | - |  | Pass | 0.61 |  |
| TC-AUT-001 | TC-BB-005 | REQ-001 | - |  | Pass | 0.63 |  |
| TC-AUT-001 | TC-BB-006 | REQ-001 | - |  | Pass | 0.47 |  |
| TC-AUT-002 | TC-BB-007 | REQ-001 | - |  | Pass | 0.47 |  |
| TC-AUT-002 | TC-BB-008, TC-GUI-004 | REQ-001 | DEF-001 |  | Fail (known defect) | 0.48 | AssertionError: expected the task list after registration, browser is on /register (error shown: 'Password must be at least 8 characters.') [screenshot](screenshots/test_password_length_boundaries_TC-BB-008-len8_.png) |
| TC-AUT-002 | TC-BB-009 | REQ-001 | - |  | Pass | 0.6 |  |
| TC-AUT-003 | TC-BB-010 | REQ-001 | - | Y | Pass | 0.67 |  |
| TC-AUT-004 | TC-BB-011 | REQ-001 | - |  | Pass | 0.48 |  |
| TC-AUT-005 | TC-BB-012 | REQ-001 | - |  | Pass | 0.31 |  |
| TC-AUT-005 | TC-BB-013 | REQ-001 | - |  | Pass | 0.31 |  |
| TC-AUT-006 | TC-BB-014 | REQ-002 | - | Y | Pass | 0.73 |  |
| TC-AUT-006 | TC-BB-015 | REQ-002 | - |  | Pass | 0.74 |  |
| TC-AUT-006 | TC-BB-016 | REQ-002 | - |  | Pass | 0.62 |  |
| TC-AUT-006 | TC-BB-017 | REQ-002 | - |  | Pass | 0.64 |  |
| TC-AUT-007 | TC-BB-018 | REQ-002 | - | Y | Pass | 0.1 |  |
| TC-AUT-007 | TC-BB-018 | REQ-002 | - | Y | Pass | 0.11 |  |
| TC-AUT-007 | TC-BB-018 | REQ-002 | - | Y | Pass | 0.1 |  |
| TC-AUT-008 | TC-BB-019 | REQ-002 | - | Y | Pass | 0.26 |  |
| TC-AUT-009 | TC-BB-020 | REQ-003 | - | Y | Pass | 1.55 |  |
| TC-AUT-010 | TC-BB-021 | REQ-003 | - |  | Pass | 0.4 |  |
| TC-AUT-011 | TC-BB-022 | REQ-003 | - |  | Pass | 0.39 |  |
| TC-AUT-012 | TC-BB-023, TC-GUI-016 | REQ-003 | DEF-003 |  | Fail (known defect) | 0.33 | AssertionError: whitespace-only title created 1 task(s): [''] [screenshot](screenshots/test_whitespace_only_title_rejected.png) |
| TC-AUT-013 | TC-BB-024, TC-GUI-012, TC-GUI-015 | REQ-003 | - |  | Pass | 1.69 |  |
| TC-AUT-014 | TC-BB-025 | REQ-003 | - |  | Pass | 1.35 |  |
| TC-AUT-015 | TC-BB-026, TC-GUI-013 | REQ-003 | - |  | Pass | 0.39 |  |
| TC-AUT-016 | TC-BB-027, TC-GUI-013 | REQ-003 | - | Y | Pass | 0.69 |  |
| TC-AUT-017 | TC-BB-028, TC-BB-029, TC-GUI-011 | REQ-004 | - | Y | Pass | 0.91 |  |
| TC-AUT-018 | TC-GUI-020 | REQ-003 | - |  | Pass | 0.68 |  |
| TC-AUT-019 | TC-GUI-020 | REQ-003 | DEF-005 |  | Fail (known defect) | 0.15 | AssertionError: list shows ['GUI-Special & bold "double" \'single\' Résumé 报告'] instead of the saved title [screenshot](screenshots/test_special_characters_displayed_literally_in_list.png) |
| TC-AUT-020 | TC-BB-044 | REQ-008 | - | Y | Pass | 1.97 |  |
| TC-AUT-021 | TC-BB-030 | REQ-005 | - |  | Pass | 0.52 |  |
| TC-AUT-021 | TC-BB-031 | REQ-005 | - |  | Pass | 0.47 |  |
| TC-AUT-021 | TC-BB-032 | REQ-005 | - |  | Pass | 0.38 |  |
| TC-AUT-021 | TC-BB-033 | REQ-005 | - |  | Pass | 0.58 |  |
| TC-AUT-021 | TC-BB-034 | REQ-005 | - |  | Pass | 0.39 |  |
| TC-AUT-021 | TC-BB-035, TC-GUI-008 | REQ-005 | - | Y | Pass | 0.81 |  |
| TC-AUT-022 | TC-BB-036 | REQ-006 | - |  | Pass | 0.45 |  |
| TC-AUT-022 | TC-BB-037 | REQ-006 | - |  | Pass | 0.55 |  |
| TC-AUT-022 | TC-BB-038, TC-GUI-010 | REQ-006 | DEF-002 |  | Fail (known defect) | 0.43 | AssertionError: BB-TODAY due 2026-11-27 shows 'Overdue' [screenshot](screenshots/test_urgency_label_TC-BB-038-today_.png) |
| TC-AUT-022 | TC-BB-039 | REQ-006 | - |  | Pass | 0.63 |  |
| TC-AUT-022 | TC-BB-040 | REQ-006 | - |  | Pass | 0.41 |  |
| TC-AUT-022 | TC-BB-041 | REQ-006 | - |  | Pass | 0.44 |  |
| TC-AUT-023 | TC-BB-042 | REQ-004, REQ-006 | - |  | Pass | 0.43 |  |
| TC-AUT-024 | TC-BB-043 | REQ-007 | - |  | Pass | 0.25 |  |
| TC-AUT-025 | TC-BB-043 | REQ-007 | DEF-002 |  | Fail (known defect) | 0.28 | AssertionError: Overdue counter is 2, expected 1 (only BB-YESTERDAY is overdue) [screenshot](screenshots/test_dashboard_overdue_counter.png) |
| TC-AUT-026 | TC-BB-001 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-002 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-003 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-004 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-005 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-006 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-011 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-010 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-027 | TC-BB-007 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-027 | TC-BB-008 | REQ-001 | DEF-001 |  | Fail (known defect) | 0.0 | AssertionError: assert False is True |
| TC-AUT-027 | TC-BB-009 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-036 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-037 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-038 | REQ-006 | DEF-002 |  | Fail (known defect) | 0.0 | AssertionError: assert 'Overdue' == 'Due Today' |
| TC-AUT-028 | TC-BB-039 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-040 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-041 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-029 | TC-API-001 | REQ-001 | - |  | Pass | 0.16 |  |
| TC-AUT-030 | TC-API-002 | REQ-001 | - |  | Pass | 0.14 |  |
| TC-AUT-030 | TC-API-002 | REQ-001 | - |  | Pass | 0.15 |  |
| TC-AUT-031 | TC-API-003 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-031 | TC-API-003 | REQ-001 | - |  | Pass | 0.02 |  |
| TC-AUT-031 | TC-API-003 | REQ-001 | - |  | Pass | 0.01 |  |
| TC-AUT-031 | TC-API-003 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-032 | TC-API-004 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-033 | TC-API-005 | REQ-001 | DEF-001 |  | Fail (known defect) | 0.01 | AssertionError: 8-character password: <400 application/json '{"error":"invalid password"} '> |
| TC-AUT-034 | TC-API-006 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-035 | TC-API-007 | REQ-001, REQ-009 | DEF-018 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-036 | TC-API-008 | REQ-001 | DEF-016 |  | Fail (known defect) | 0.15 | AssertionError: duplicate username 'w6_api_14460343' was accepted: <201 application/json '{"id":36,"username":"w6_api_14460343"} '> |
| TC-AUT-037 | TC-API-009 | REQ-002 | - |  | Pass | 0.16 |  |
| TC-AUT-038 | TC-API-010 | REQ-002 | - |  | Pass | 0.15 |  |
| TC-AUT-038 | TC-API-010 | REQ-002 | - |  | Pass | 0.03 |  |
| TC-AUT-038 | TC-API-010 | REQ-002 | - |  | Pass | 0.04 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.0 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-039 | TC-API-011 | REQ-002, REQ-009 | - |  | Pass | 0.0 |  |
| TC-AUT-040 | TC-API-012 | REQ-009 | DEF-023 |  | Fail (known defect) | 0.01 | AssertionError: categories without login: <200 application/json '[{"id":2,"name":"Personal"},{"id":3,"name":"Study"},{"id":4,"name":"Urgent"},{"id":1,"name":"Work"}] '> |
| TC-AUT-041 | TC-API-013 | REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-042 | TC-API-014 | REQ-003 | - |  | Pass | 0.04 |  |
| TC-AUT-043 | TC-API-015 | REQ-003 | - |  | Pass | 0.01 |  |
| TC-AUT-044 | TC-API-016 | REQ-003 | - |  | Pass | 0.01 |  |
| TC-AUT-044 | TC-API-016 | REQ-003 | - |  | Pass | 0.03 |  |
| TC-AUT-044 | TC-API-016 | REQ-003 | - |  | Pass | 0.02 |  |
| TC-AUT-045 | TC-API-017 | REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-046 | TC-API-018 | REQ-003, REQ-009 | DEF-018 |  | Fail (known defect) | 0.02 | AssertionError: expected 400 with a JSON error, got <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-046 | TC-API-018 | REQ-003, REQ-009 | DEF-018 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-046 | TC-API-018 | REQ-003, REQ-009 | DEF-018 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-047 | TC-API-019 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.07 | AssertionError: due_date '31/12/2026': create returned <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; list/dashboard then returned (500, 500) |
| TC-AUT-047 | TC-API-019 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.05 | AssertionError: due_date '2026-02-30': create returned <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; list/dashboard then returned (500, 500) |
| TC-AUT-047 | TC-API-019 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.09 | AssertionError: due_date 'tomorrow': create returned <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; list/dashboard then returned (500, 500) |
| TC-AUT-048 | TC-API-020 | REQ-003 | DEF-019 |  | Fail (known defect) | 0.02 | AssertionError: expected 400 with a JSON error, got <201 application/json '{"category":null,"category_id":999,"completed_at":null,"created_at":"2026-11-27T14:47:13.114925","description":"","done"'> |
| TC-AUT-048 | TC-API-020 | REQ-003 | DEF-019 |  | Fail (known defect) | 0.01 | AssertionError: expected 400 with a JSON error, got <201 application/json '{"category":null,"category_id":"abc","completed_at":null,"created_at":"2026-11-27T14:47:13.338160","description":"","don'> |
| TC-AUT-049 | TC-API-021 | REQ-006 | - |  | Pass | 0.01 |  |
| TC-AUT-049 | TC-API-021 | REQ-006 | DEF-002 |  | Fail (known defect) | 0.03 | AssertionError: due 2026-11-27: urgency 'Overdue' |
| TC-AUT-049 | TC-API-021 | REQ-006 | - |  | Pass | 0.01 |  |
| TC-AUT-049 | TC-API-021 | REQ-006 | - |  | Pass | 0.01 |  |
| TC-AUT-049 | TC-API-021 | REQ-006 | - |  | Pass | 0.01 |  |
| TC-AUT-050 | TC-API-022 | REQ-003 | - |  | Pass | 0.03 |  |
| TC-AUT-051 | TC-API-023 | REQ-003, REQ-009 | - |  | Pass | 0.0 |  |
| TC-AUT-052 | TC-API-024 | REQ-008 | - |  | Pass | 0.02 |  |
| TC-AUT-053 | TC-API-025 | REQ-009 | - |  | Pass | 0.0 |  |
| TC-AUT-054 | TC-API-026 | REQ-005 | - |  | Pass | 0.01 |  |
| TC-AUT-055 | TC-API-027 | REQ-005 | - |  | Pass | 0.02 |  |
| TC-AUT-055 | TC-API-027 | REQ-005 | - |  | Pass | 0.01 |  |
| TC-AUT-056 | TC-API-028 | REQ-005 | - |  | Pass | 0.02 |  |
| TC-AUT-057 | TC-API-029 | REQ-005 | - |  | Pass | 0.02 |  |
| TC-AUT-058 | TC-API-030 | REQ-005 | DEF-017 |  | Fail (known defect) | 0.01 | AssertionError: search for O'Brien: <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'> |
| TC-AUT-059 | TC-API-031 | REQ-005, REQ-009 | - |  | Pass | 0.1 |  |
| TC-AUT-060 | TC-API-032 | REQ-009 | DEF-022 |  | Fail (known defect) | 0.09 | AssertionError: expected 400 with a JSON error, got <200 application/json '[{"category":null,"category_id":null,"completed_at":null,"created_at":"2026-11-27T14:47:16.114043","description":"","don'> |
| TC-AUT-060 | TC-API-032 | REQ-009 | DEF-022 |  | Fail (known defect) | 0.06 | AssertionError: expected 400 with a JSON error, got <200 application/json '[{"category":null,"category_id":null,"completed_at":null,"created_at":"2026-11-27T14:47:16.331228","description":"","don'> |
| TC-AUT-060 | TC-API-032 | REQ-009 | DEF-022 |  | Fail (known defect) | 0.04 | AssertionError: expected 400 with a JSON error, got <200 application/json '[{"category":null,"category_id":null,"completed_at":null,"created_at":"2026-11-27T14:47:16.576460","description":"","don'> |
| TC-AUT-061 | TC-API-033 | REQ-008 | - |  | Pass | 0.19 |  |
| TC-AUT-062 | TC-API-034 | REQ-003 | - |  | Pass | 0.06 |  |
| TC-AUT-063 | TC-API-035 | REQ-004 | - |  | Pass | 0.04 |  |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-020 |  | Fail (known defect) | 0.06 | AssertionError: PUT {'title': ''}: <200 application/json '{"category":"Work","category_id":1,"completed_at":null,"created_at":"2026-11-27T14:47:17.460926","description":"","done"'>; task afterwards: 200 {'title': '', 'done': False, 'category_id': 1, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-020 |  | Fail (known defect) | 0.03 | AssertionError: PUT {'title': '   '}: <200 application/json '{"category":"Work","category_id":1,"completed_at":null,"created_at":"2026-11-27T14:47:17.672286","description":"","done"'>; task afterwards: 200 {'title': '   ', 'done': False, 'category_id': 1, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-020 |  | Fail (known defect) | 0.05 | AssertionError: PUT {'done': 'false'}: <200 application/json '{"category":"Work","category_id":1,"completed_at":"2026-11-27 14:47:17","created_at":"2026-11-27T14:47:17.892661","descr'>; task afterwards: 200 {'title': 'Stable title', 'done': True, 'category_id': 1, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-018 |  | Fail (known defect) | 0.06 | AssertionError: PUT {'title': None}: <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; task afterwards: 200 {'title': 'Stable title', 'done': False, 'category_id': 1, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-019 |  | Fail (known defect) | 0.07 | AssertionError: PUT {'category_id': 999}: <200 application/json '{"category":null,"category_id":999,"completed_at":null,"created_at":"2026-11-27T14:47:18.390530","description":"","done"'>; task afterwards: 200 {'title': 'Stable title', 'done': False, 'category_id': 999, 'due_date': '2026-12-02'} |
| TC-AUT-064 | TC-API-036 | REQ-003, REQ-009 | DEF-015 |  | Fail (known defect) | 0.08 | AssertionError: PUT {'due_date': '31/12/2026'}: <500 text/html '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server enc'>; task afterwards: 500 None |
| TC-AUT-065 | TC-API-037 | REQ-008 | - |  | Pass | 0.02 |  |
| TC-AUT-066 | TC-API-038 | REQ-009 | - |  | Pass | 0.01 |  |
| TC-AUT-067 | TC-API-039 | REQ-003 | - |  | Pass | 0.03 |  |
| TC-AUT-068 | TC-API-040 | REQ-008 | DEF-014 |  | Fail (known defect) | 0.06 | AssertionError: intruder DELETE returned 200; owner's GET afterwards returned 404 |
| TC-AUT-069 | TC-API-041 | REQ-009 | DEF-021 |  | Fail (known defect) | 0.01 | AssertionError: expected 404 with a JSON error, got <200 application/json '{"result":"ok"} '> |
| TC-AUT-070 | TC-API-042 | REQ-007 | - |  | Pass | 0.08 |  |
| TC-AUT-071 | TC-API-043 | REQ-006, REQ-007 | DEF-002 |  | Fail (known defect) | 0.08 | AssertionError: Overdue counter is 2, expected 1 |
| TC-AUT-072 | TC-API-044 | REQ-008 | - |  | Pass | 0.35 |  |
| TC-AUT-073 | TC-API-045 | REQ-009 | - |  | Pass | 0.02 |  |
| TC-AUT-074 | TC-WEB-001 | REQ-001 | - |  | Pass | 0.14 |  |
| TC-AUT-075 | TC-WEB-002 | REQ-001 | - |  | Pass | 0.01 |  |
| TC-AUT-075 | TC-WEB-002 | REQ-001 | - |  | Pass | 0.01 |  |
| TC-AUT-075 | TC-WEB-002 | REQ-001 | - |  | Pass | 0.02 |  |
| TC-AUT-076 | TC-WEB-003 | REQ-002 | - |  | Pass | 0.27 |  |
| TC-AUT-076 | TC-WEB-003 | REQ-002 | - |  | Pass | 0.27 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.01 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.0 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.02 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.02 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.01 |  |
| TC-AUT-077 | TC-WEB-004 | REQ-002 | - |  | Pass | 0.0 |  |
| TC-AUT-078 | TC-WEB-005 | REQ-003 | - |  | Pass | 0.02 |  |
| TC-AUT-079 | TC-WEB-006 | REQ-003, REQ-006 | - |  | Pass | 0.19 |  |
| TC-AUT-080 | TC-WEB-007 | REQ-003 | - |  | Pass | 0.21 |  |
| TC-AUT-081 | TC-WEB-008 | REQ-004 | - |  | Pass | 0.19 |  |
| TC-AUT-082 | TC-WEB-009 | REQ-003 | - |  | Pass | 0.2 |  |
| TC-AUT-083 | TC-WEB-010 | REQ-003 | DEF-003 |  | Fail (known defect) | 0.02 | AssertionError: server accepted the form: 302 redirect to /; saved titles: [''] |
| TC-AUT-083 | TC-WEB-010 | REQ-003 | DEF-003 |  | Fail (known defect) | 0.02 | AssertionError: server accepted the form: 302 redirect to /; saved titles: [''] |
| TC-AUT-084 | TC-WEB-011 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.03 | AssertionError: server accepted the form: 302 redirect to /; / and /dashboard then returned (500, 500) |
| TC-AUT-084 | TC-WEB-011 | REQ-003, REQ-006 | DEF-015 |  | Fail (known defect) | 0.03 | AssertionError: server accepted the form: 302 redirect to /; / and /dashboard then returned (500, 500) |
| TC-AUT-085 | TC-WEB-012 | REQ-003 | DEF-019 |  | Fail (known defect) | 0.03 | AssertionError: server accepted the form: 302 redirect to /; saved: [('bad category', 999)] |
| TC-AUT-086 | TC-WEB-013 | REQ-008 | - |  | Pass | 0.36 |  |
| TC-AUT-087 | TC-WEB-014 | REQ-007 | - |  | Pass | 0.27 |  |
| TC-AUT-088 | TC-WEB-015 | REQ-005 | - |  | Pass | 0.19 |  |
| TC-AUT-089 | TC-WEB-016 | REQ-001 | DEF-016 |  | Fail (known defect) | 0.3 | AssertionError: duplicate username 'w6_web_144603119' was accepted: 302 redirect to / |
