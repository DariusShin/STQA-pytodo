# Week 1 - Detailed Black-Box Test Cases

This document contains a set of 44 test cases, which have the unique identifier from `TC-BB-001` to `TC-BB-044`. Each case appears once in a table containing the required fields following the templates given in the project guideline, which same as the following:

| Field | Required Information |
| --- | --- |
| Test Case ID | Unique identifier with the format as "TC-BB-[unique value]" |
| Feature/Requirement | Feature or requirement tested |
| Technique/Test Type | e.g. EP, BVA, Decision Table, State Transition, Functional, API, GUI |
| Objective | What the test verifies |
| Preconditions | Required initial state |
| Test Data | Input value/data in JSON format which {key: values} pairs|
| Steps | Numbered procedure starting from 1 to n |
| Expected Result | Expected behaviour defined before execution |
| Actual Result | Observed behaviour |
| Status | Pass/Fail/Blocked/Not run |
| Evidence | Screenshotreference, the file will be named as "[Test Case ID].jpg" in /evidences folder |
| Defect ID | Related defect if applicable with the format as "DEF-[unique value]" |

Evidence filenames refer to screenshots stored directly in `evidences/`.

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
