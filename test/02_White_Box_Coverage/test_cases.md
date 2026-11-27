# Week 2 - White-Box Test Cases

Cases in the project Test Case Template. TC-WB-001 to 019 cover the 19 basis paths derived in [W2_Report.md](W2_Report.md#32-independent-execution-paths); TC-WB-020 to 024 are supplementary integration checks; TC-WB-025 to 028 are the `helpers.py` suites. Every case is automated: the step is the pytest node in [test_app.py](test_app.py) or [test_helpers.py](test_helpers.py).

Executed 26 October 2026 by Darius Lee Shin (combined run: 50 instances passed). Evidence for all cases: terminal run and the [HTML coverage report](htmlcov/index.html). No defects were raised in Week 2; specification mismatches found in the helper suites are existing defects DEF-001 and DEF-002 (Week 1).

## Basis-path cases (`app.py`)

| Test Case ID | Feature / unit | Technique | Objective | Preconditions and test data | Steps | Expected result | Actual result | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-WB-001 | `get_db` | Basis path DB01 | New connection is created | Fresh app context, no `_database` | `TestDatabaseHelpers::test_get_db_creates_and_reuses_connection` (first call) | Connection stored in `g`; `row_factory` is `sqlite3.Row`; named-column access works | As expected | Pass |
| TC-WB-002 | `get_db` | Basis path DB02 | Existing connection is reused | Context already holds the DB01 connection | Same test, second call | Identical object returned (`is`); no new connection | As expected | Pass |
| TC-WB-003 | `close_connection` | Basis path CL01 | Existing connection is closed | Context holds a mock connection; with and without an exception argument | `TestCloseConnection::test_closes_existing_connection`, `::test_closes_connection_when_teardown_receives_exception` | `close()` called exactly once in both scenarios | As expected | Pass |
| TC-WB-004 | `close_connection` | Basis path CL02 | Missing connection is safe | No connection in context | `TestCloseConnection::test_no_connection_is_safe` | No exception; no connection attribute added | As expected | Pass |
| TC-WB-005 | `init_db` | Basis path IN01 (zero iterations) | Schema created with no categories | Temporary DB; `DEFAULT_CATEGORIES` patched to `[]` | `TestDatabaseHelpers::test_init_db_with_no_default_categories` | Three tables exist; category count 0 | As expected | Pass |
| TC-WB-006 | `init_db` | Basis path IN02 (four iterations) | Defaults seeded and committed | Temporary DB; defaults Work, Personal, Study, Urgent | `TestDatabaseHelpers::test_init_db_creates_tables_and_commits_categories` | Four categories committed and readable from another connection | As expected | Pass |
| TC-WB-007 | `row_to_task` | Basis path RT01 | Open task gets computed urgency | `done=0`; due `2026-10-22`; urgency mock returns `Due Soon`; category `None` or `Study` | `test_row_to_task_converts_fields_and_selects_urgency` (`done=0` variants) | Urgency computed once from due date; `done` is `False`; fields mapped; input unchanged | As expected | Pass |
| TC-WB-008 | `row_to_task` | Basis path RT02 | Done task gets `Done` | `done=1`; category `None` or `Study` | Same test (`done=1` variants) | Urgency `Done`; urgency function not called; `done` is `True` | As expected | Pass |
| TC-WB-009 | `get_category_name` | Basis path CN01 | Falsy id skips the database | id `None`, `0`, `""`; mock DB | `test_missing_category_id_skips_database` (3 variants) | Returns `None`; `execute` never called | As expected | Pass |
| TC-WB-010 | `get_category_name` | Basis path CN02 | Existing id resolves | Seeded DB; id of `Study` | `TestDatabaseHelpers::test_category_lookups_find_seeded_category` | Returns `Study` | As expected | Pass |
| TC-WB-011 | `get_category_name` | Basis path CN03 | Unknown id returns nothing | Seeded DB; id `999999` | `TestDatabaseHelpers::test_category_lookups_return_none_for_missing_values` | Returns `None` | As expected | Pass |
| TC-WB-012 | `get_category_id_by_name` | Basis path CI01 | Existing name resolves | Seeded DB; name `Study` | `TestDatabaseHelpers::test_category_lookups_find_seeded_category` | Returns the queried id of `Study` | As expected | Pass |
| TC-WB-013 | `get_category_id_by_name` | Basis path CI02 | Unknown or injected name returns nothing | Names `Unknown` and `Study' OR 1=1 --` | `TestDatabaseHelpers::test_category_lookups_return_none_for_missing_values` | Returns `None` for both | As expected | Pass |
| TC-WB-014 | `login_required_web` factory | Basis path WF01 | Decorator keeps metadata | Named dummy function with docstring | `TestAuthDecorators::test_preserves_wrapped_function_metadata` (web) | Wrapper returned; name, docstring, `__wrapped__` kept | As expected | Pass |
| TC-WB-015 | `login_required_web` wrapper | Basis path WA01 | Anonymous request redirected | No `user_id`, or `0`, or `""` | `TestAuthDecorators::test_unauthenticated_request_does_not_call_function` (web) | HTTP 302 to `/login`; view not called | As expected | Pass |
| TC-WB-016 | `login_required_web` wrapper | Basis path WA02 | Signed-in request forwarded | `user_id=1`; args `7`, `category="Study"` | `TestAuthDecorators::test_authenticated_request_forwards_arguments_and_result` (web) | View called once with both args; result returned unchanged | As expected | Pass |
| TC-WB-017 | `login_required_api` factory | Basis path AF01 | Decorator keeps metadata | Named dummy function with docstring | `TestAuthDecorators::test_preserves_wrapped_function_metadata` (API) | Wrapper returned with metadata | As expected | Pass |
| TC-WB-018 | `login_required_api` wrapper | Basis path AA01 | Anonymous API call rejected | No `user_id`, or `0`, or `""` | `TestAuthDecorators::test_unauthenticated_request_does_not_call_function` (API) | `{"error": "authentication required"}`, HTTP 401; view not called | As expected | Pass |
| TC-WB-019 | `login_required_api` wrapper | Basis path AA02 | Signed-in API call forwarded | `user_id=1`; args `7`, `category="Study"` | `TestAuthDecorators::test_authenticated_request_forwards_arguments_and_result` (API) | View called once; original result returned | As expected | Pass |

## Supplementary integration cases (`app.py`)

| Test Case ID | Feature / unit | Technique | Objective | Preconditions and test data | Steps | Expected result | Actual result | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-WB-020 | `close_connection` | Integration | Real teardown closes the connection | Flask app context with temporary DB | `TestDatabaseHelpers::test_context_teardown_closes_connection` | Connection closed when the context ends | As expected | Pass |
| TC-WB-021 | `get_db` | Integration | New context gets a new connection | Two consecutive app contexts | `TestDatabaseHelpers::test_new_context_gets_new_connection` | Different connection objects | As expected | Pass |
| TC-WB-022 | `init_db` | Integration | Re-running init keeps data | Initialised DB with one user | `TestDatabaseHelpers::test_init_db_is_repeatable_and_preserves_existing_data` | No duplicate categories; user kept | As expected | Pass |
| TC-WB-023 | Auth decorators via routes | Integration | Real endpoints reject anonymous calls | No session; `GET /`, `GET /api/tasks` | `TestAuthBackendIntegration::test_backend_rejects_unauthenticated_requests` | `/` redirects (302); API returns 401 | As expected | Pass |
| TC-WB-024 | Auth decorators via routes | Integration | Real endpoints accept a session | Session with seeded user | `TestAuthBackendIntegration::test_backend_accepts_authenticated_session` | Both endpoints return 200 | As expected | Pass |

## Helper suites (`helpers.py`)

| Test Case ID | Feature / unit | Technique | Objective | Test data | Steps | Expected result | Actual result | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-WB-025 | `compute_urgency` | Statement coverage | 6 urgency outcomes | No date; past; today; +1/+2 days; later; malformed | `test_helpers.py::TestComputeUrgency` | Each class returns its label | 6 passed. The today case asserts the implementation's `Overdue`; the docstring says `Due Today` (DEF-002) | Pass |
| TC-WB-026 | `is_valid_password` | Statement coverage | Password rule | Non-string; short; long | `test_helpers.py::TestIsValidPassword` | Invalid rejected, valid accepted | 3 passed. The exact 8-character boundary is not covered; code uses `> 8` (DEF-001) | Pass |
| TC-WB-027 | `is_valid_username` | Statement coverage | Username rule | Non-string; bad characters; too short; too long; valid | `test_helpers.py::TestIsValidUsername` | Invalid rejected, valid accepted | 5 passed | Pass |
| TC-WB-028 | `completed_in_last_n_days` | Statement coverage | Recent-completion window | Missing; malformed; default now; recent; old | `test_helpers.py::TestCompletedInLastNDays` | Recent counted, old not | 6 passed. `test_completed_exactly_n_days_ago` uses 4 days with n=5, so the exact boundary is not covered | Pass |
