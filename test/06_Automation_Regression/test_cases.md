# Week 6 - Automated Test Cases

89 automated test cases, TC-AUT-001 to TC-AUT-089, each traced to the manual case(s) it automates. Expected results are those of the manual cases; the step is the pytest function named in the second column. Status meanings: Pass; **Fail (known)** = the check failed with the documented defect symptom and is reported as strict xfail. **S** = in the smoke subset.

## Week 1 and Week 3 cases (browser and rule checks)

Results from the baseline run on 2026-11-20 ([run 1](evidences/runs/20261120-210226-edge-full-run1/results.md)), Microsoft Edge 157 headless.

| Auto ID | Script :: test | Manual case(s) | Requirement | Technique | Checks | S | Defect | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-AUT-001 | test_01_auth :: test_username_length_boundaries | TC-BB-001, 002, 003, 004, 005, 006 | REQ-001 | BVA | 6 | | - | 6 Pass |
| TC-AUT-002 | test_01_auth :: test_password_length_boundaries | TC-BB-007, 008, 009; TC-GUI-004 | REQ-001 | BVA | 3 | | DEF-001 | 2 Pass, TC-BB-008 Fail (known) |
| TC-AUT-003 | test_01_auth :: test_valid_registration_opens_task_list | TC-BB-010 | REQ-001 | EP | 1 | S | - | Pass |
| TC-AUT-004 | test_01_auth :: test_username_with_hyphen_is_rejected | TC-BB-011 | REQ-001 | EP | 1 | | - | Pass |
| TC-AUT-005 | test_01_auth :: test_empty_registration_field_blocked_by_browser | TC-BB-012, 013 | REQ-001 | EP / browser validation | 2 | | - | 2 Pass |
| TC-AUT-006 | test_01_auth :: test_login_decision_table | TC-BB-014, 015, 016, 017; TC-GUI-002 (text only) | REQ-002 | Decision table | 4 | S (rule 1) | - | 4 Pass |
| TC-AUT-007 | test_01_auth :: test_protected_page_redirects_when_logged_out | TC-BB-018 (extended to 3 pages) | REQ-002 | State transition | 3 | S | - | 3 Pass |
| TC-AUT-008 | test_01_auth :: test_logout_revokes_protected_page_access | TC-BB-019 | REQ-002 | State transition | 1 | S | - | Pass |
| TC-AUT-009 | test_02_tasks :: test_create_full_field_task_persists | TC-BB-020 | REQ-003 | EP | 1 | S | - | Pass |
| TC-AUT-010 | test_02_tasks :: test_create_title_only_task | TC-BB-021 | REQ-003 | EP | 1 | | - | Pass |
| TC-AUT-011 | test_02_tasks :: test_empty_title_blocked_by_browser | TC-BB-022 | REQ-003 | EP / browser validation | 1 | | - | Pass |
| TC-AUT-012 | test_02_tasks :: test_whitespace_only_title_rejected | TC-BB-023; TC-GUI-016 | REQ-003 | EP / input validation | 1 | | DEF-003 | Fail (known) |
| TC-AUT-013 | test_02_tasks :: test_edit_persists_all_fields | TC-BB-024; TC-GUI-012, 015 | REQ-003 | Functional | 1 | | - | Pass |
| TC-AUT-014 | test_02_tasks :: test_cancel_edit_preserves_saved_data | TC-BB-025 | REQ-003 | State transition | 1 | | - | Pass |
| TC-AUT-015 | test_02_tasks :: test_cancel_deletion_retains_task | TC-BB-026; TC-GUI-013 | REQ-003 | State transition | 1 | | - | Pass |
| TC-AUT-016 | test_02_tasks :: test_confirm_deletion_removes_only_that_task | TC-BB-027; TC-GUI-013 | REQ-003 | State transition | 1 | S | - | Pass |
| TC-AUT-017 | test_02_tasks :: test_complete_then_reopen_task | TC-BB-028, 029; TC-GUI-011 | REQ-004 | State transition | 1 | S | - | Pass |
| TC-AUT-018 | test_02_tasks :: test_special_characters_preserved_in_edit_form | TC-GUI-020 (edit form) | REQ-003 | Functional | 1 | | - | Pass |
| TC-AUT-019 | test_02_tasks :: test_special_characters_displayed_literally_in_list | TC-GUI-020 (list) | REQ-003 | Functional | 1 | | DEF-005 | Fail (known) |
| TC-AUT-020 | test_02_tasks :: test_each_account_sees_only_its_own_tasks | TC-BB-044 | REQ-008 | EP | 1 | S | - | Pass |
| TC-AUT-021 | test_03_filters :: test_filters_return_only_matching_tasks | TC-BB-030, 031, 032, 033, 034, 035; TC-GUI-008 | REQ-005 | EP / decision table | 6 | S (035) | - | 6 Pass |
| TC-AUT-022 | test_04_urgency_dashboard :: test_urgency_label | TC-BB-036, 037, 038, 039, 040, 041; TC-GUI-010 | REQ-006 | BVA | 6 | | DEF-002 | 5 Pass, TC-BB-038 Fail (known) |
| TC-AUT-023 | test_04_urgency_dashboard :: test_completion_overrides_overdue | TC-BB-042 | REQ-004, REQ-006 | State transition | 1 | | - | Pass |
| TC-AUT-024 | test_04_urgency_dashboard :: test_dashboard_counters_unaffected_by_def002 | TC-BB-043 (Total, Open, Due Soon, Completed) | REQ-007 | Independent calculation | 1 | | - | Pass |
| TC-AUT-025 | test_04_urgency_dashboard :: test_dashboard_overdue_counter | TC-BB-043 (Overdue) | REQ-007 | Independent calculation | 1 | | DEF-002 | Fail (known) |
| TC-AUT-026 | test_05_rules_unit :: test_username_rule | TC-BB-001 to 006, 010, 011 | REQ-001 | BVA / EP (unit) | 8 | | - | 8 Pass |
| TC-AUT-027 | test_05_rules_unit :: test_password_rule | TC-BB-007, 008, 009 | REQ-001 | BVA (unit) | 3 | | DEF-001 | 2 Pass, TC-BB-008 Fail (known) |
| TC-AUT-028 | test_05_rules_unit :: test_urgency_rule | TC-BB-036 to 041 | REQ-006 | BVA (unit) | 6 | | DEF-002 | 5 Pass, TC-BB-038 Fail (known) |
| **Total** | | | | | **65** | 11 | | **58 Pass, 7 Fail (known)** |

### Deviations from the manual procedure

| Case | Difference from the manual case | Why it does not weaken the check |
| --- | --- | --- |
| All | Accounts and fixtures are created through the API, not the UI | Creation through the UI has its own checks (TC-AUT-003, 009, 010). |
| TC-BB-031 | Expects 3 Open rows, where Week 1 expected 5 | Week 1's account also held its CRUD tasks. Here the account holds only F1-F4, so the expected set is exact. |
| TC-BB-036 to 043 | Due dates are offsets from the run day, where Week 1 used fixed October 2026 dates | The boundaries tested are the same (D-1, D, D+1, D+2, D+3). |
| Date fields | The ISO value is set via JavaScript plus `input`/`change` events, and is not typed into the date picker | Typed dates depend on the browser locale. The date picker itself is a Week 3 usability concern. |
| TC-BB-012, 013, 022 | Assert `validity.valueMissing` and that a message exists, not the message text | The message wording belongs to the browser and differs by locale. |
| TC-BB-018 | Also checks `/dashboard` and `/tasks/new` | Adds coverage at no extra cost. |

## Week 4 cases (Web/API checks over HTTP)

Results from the full run on 2026-11-27 ([run 7](evidences/runs/20261127-144603-edge-full-w4-run1/results.md)). They match the Week 4 Postman result for every case and variant: exactly the 32 variants that failed in Week 4 fail here, with the same symptom. These checks run as their own tier with `-m api`.

| Auto ID | Script :: test | Manual case(s) | Requirement | Technique | Checks | Defect | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-AUT-029 | test_06_api :: test_api_register_valid_account | TC-API-001 | REQ-001 | EP / API functional | 1 | - | Pass |
| TC-AUT-030 | test_06_api :: test_api_username_valid_length_boundaries | TC-API-002 | REQ-001 | BVA / API | 2 | - | 2 Pass |
| TC-AUT-031 | test_06_api :: test_api_invalid_username_partitions | TC-API-003 | REQ-001 | EP + BVA / API negative | 4 | - | 4 Pass |
| TC-AUT-032 | test_06_api :: test_api_password_length_7_rejected | TC-API-004 | REQ-001 | BVA / API negative | 1 | - | Pass |
| TC-AUT-033 | test_06_api :: test_api_password_length_8_accepted | TC-API-005 | REQ-001 | BVA / API | 1 | DEF-001 | Fail (known) |
| TC-AUT-034 | test_06_api :: test_api_missing_password_rejected | TC-API-006 | REQ-001 | EP / API negative | 1 | - | Pass |
| TC-AUT-035 | test_06_api :: test_api_username_wrong_json_type | TC-API-007 | REQ-001, REQ-009 | EP (data type) / API negative | 1 | DEF-018 | Fail (known) |
| TC-AUT-036 | test_06_api :: test_api_duplicate_username_rejected | TC-API-008 | REQ-001 | EP / API negative | 1 | DEF-016 | Fail (known) |
| TC-AUT-037 | test_06_api :: test_api_login_valid_credentials | TC-API-009 | REQ-002 | Decision table (valid/valid) / API | 1 | - | Pass |
| TC-AUT-038 | test_06_api :: test_api_login_invalid_credentials | TC-API-010 | REQ-002 | Decision table / API negative | 3 | - | 3 Pass |
| TC-AUT-039 | test_06_api :: test_api_protected_endpoints_require_session | TC-API-011 | REQ-002, REQ-009 | EP (unauthenticated) / API negative | 6 | - | 6 Pass |
| TC-AUT-040 | test_06_api :: test_api_categories_require_session | TC-API-012 | REQ-009 | EP (unauthenticated) / API negative | 1 | DEF-023 | Fail (known) |
| TC-AUT-041 | test_06_api :: test_api_list_categories | TC-API-013 | REQ-009 | API functional | 1 | - | Pass |
| TC-AUT-042 | test_06_api :: test_api_create_task_with_all_fields | TC-API-014 | REQ-003 | EP (valid) / API functional | 1 | - | Pass |
| TC-AUT-043 | test_06_api :: test_api_create_title_only_task | TC-API-015 | REQ-003 | EP (valid, optional fields omitted) / API | 1 | - | Pass |
| TC-AUT-044 | test_06_api :: test_api_title_required | TC-API-016 | REQ-003 | EP (invalid) / API negative | 3 | - | 3 Pass |
| TC-AUT-045 | test_06_api :: test_api_non_json_body_rejected | TC-API-017 | REQ-009 | EP (invalid format) / API negative | 1 | - | Pass |
| TC-AUT-046 | test_06_api :: test_api_wrong_json_types_on_create | TC-API-018 | REQ-003, REQ-009 | EP (data type) / API negative | 3 | DEF-018 | 3 Fail (known) |
| TC-AUT-047 | test_06_api :: test_api_invalid_due_date_on_create | TC-API-019 | REQ-003, REQ-006 | EP (invalid) / API negative | 3 | DEF-015 | 3 Fail (known) |
| TC-AUT-048 | test_06_api :: test_api_invalid_category_on_create | TC-API-020 | REQ-003 | EP (invalid) / API negative | 2 | DEF-019 | 2 Fail (known) |
| TC-AUT-049 | test_06_api :: test_api_urgency_boundaries | TC-API-021 | REQ-006 | BVA / API | 5 | DEF-002 | 4 Pass, TC-API-021b Fail (known) |
| TC-AUT-050 | test_06_api :: test_api_read_own_task | TC-API-022 | REQ-003 | API functional | 1 | - | Pass |
| TC-AUT-051 | test_06_api :: test_api_read_missing_task | TC-API-023 | REQ-003, REQ-009 | EP (invalid id) / API negative | 1 | - | Pass |
| TC-AUT-052 | test_06_api :: test_api_read_another_users_task | TC-API-024 | REQ-008 | EP (foreign id) / API negative | 1 | - | Pass |
| TC-AUT-053 | test_06_api :: test_api_non_integer_task_id | TC-API-025 | REQ-009 | EP (invalid type) / API negative | 1 | - | Pass |
| TC-AUT-054 | test_06_api :: test_api_filter_by_category | TC-API-026 | REQ-005 | EP / API functional | 1 | - | Pass |
| TC-AUT-055 | test_06_api :: test_api_filter_by_status | TC-API-027 | REQ-005 | EP / API functional | 2 | - | 2 Pass |
| TC-AUT-056 | test_06_api :: test_api_title_search | TC-API-028 | REQ-005 | EP / API functional | 1 | - | Pass |
| TC-AUT-057 | test_06_api :: test_api_combined_filters | TC-API-029 | REQ-005 | Decision table / API functional | 1 | - | Pass |
| TC-AUT-058 | test_06_api :: test_api_search_with_apostrophe | TC-API-030 | REQ-005 | EP (special character) / API negative | 1 | DEF-017 | Fail (known) |
| TC-AUT-059 | test_06_api :: test_api_pagination | TC-API-031 | REQ-005, REQ-009 | BVA / API functional | 1 | - | Pass |
| TC-AUT-060 | test_06_api :: test_api_invalid_pagination | TC-API-032 | REQ-009 | EP + BVA (invalid) / API negative | 3 | DEF-022 | 3 Fail (known) |
| TC-AUT-061 | test_06_api :: test_api_task_list_scoped_to_user | TC-API-033 | REQ-008 | EP / API | 1 | - | Pass |
| TC-AUT-062 | test_06_api :: test_api_partial_update | TC-API-034 | REQ-003 | API functional | 1 | - | Pass |
| TC-AUT-063 | test_06_api :: test_api_complete_and_reopen | TC-API-035 | REQ-004 | State transition (Open -> Done -> Open) / API | 1 | - | Pass |
| TC-AUT-064 | test_06_api :: test_api_invalid_values_on_update | TC-API-036 | REQ-003, REQ-009 | EP (invalid) / API negative | 6 | DEF-015, DEF-018, DEF-019, DEF-020 | 6 Fail (known) |
| TC-AUT-065 | test_06_api :: test_api_update_another_users_task | TC-API-037 | REQ-008 | EP (foreign id) / API negative | 1 | - | Pass |
| TC-AUT-066 | test_06_api :: test_api_update_missing_task | TC-API-038 | REQ-009 | EP (invalid id) / API negative | 1 | - | Pass |
| TC-AUT-067 | test_06_api :: test_api_delete_own_task | TC-API-039 | REQ-003 | State transition (exists -> deleted) / API | 1 | - | Pass |
| TC-AUT-068 | test_06_api :: test_api_delete_another_users_task | TC-API-040 | REQ-008 | EP (foreign id) / API negative | 1 | DEF-014 | Fail (known) |
| TC-AUT-069 | test_06_api :: test_api_delete_missing_task | TC-API-041 | REQ-009 | EP (invalid id) / API negative | 1 | DEF-021 | Fail (known) |
| TC-AUT-070 | test_06_api :: test_api_dashboard_counts | TC-API-042 | REQ-007 | API functional (oracle: independent count) | 1 | - | Pass |
| TC-AUT-071 | test_06_api :: test_api_dashboard_due_today_not_overdue | TC-API-043 | REQ-006, REQ-007 | BVA / API | 1 | DEF-002 | Fail (known) |
| TC-AUT-072 | test_06_api :: test_api_dashboard_scoped_to_user | TC-API-044 | REQ-008 | EP / API | 1 | - | Pass |
| TC-AUT-073 | test_06_api :: test_api_unsupported_method | TC-API-045 | REQ-009 | EP (invalid method) / API negative | 1 | - | Pass |
| TC-AUT-074 | test_07_web_forms :: test_web_register_through_form | TC-WEB-001 | REQ-001 | Workflow / web | 1 | - | Pass |
| TC-AUT-075 | test_07_web_forms :: test_web_registration_validated_on_server | TC-WEB-002 | REQ-001 | Client-server validation / EP | 3 | - | 3 Pass |
| TC-AUT-076 | test_07_web_forms :: test_web_login_through_form | TC-WEB-003 | REQ-002 | Decision table / web | 2 | - | 2 Pass |
| TC-AUT-077 | test_07_web_forms :: test_web_protected_pages_redirect_when_logged_out | TC-WEB-004 | REQ-002 | EP (unauthenticated) / web | 6 | - | 6 Pass |
| TC-AUT-078 | test_07_web_forms :: test_web_created_task_matches_api | TC-WEB-005 | REQ-003 | Workflow / UI vs API comparison | 1 | - | Pass |
| TC-AUT-079 | test_07_web_forms :: test_api_created_task_matches_web_list | TC-WEB-006 | REQ-003, REQ-006 | Workflow / API vs UI comparison | 1 | - | Pass |
| TC-AUT-080 | test_07_web_forms :: test_web_edit_matches_api | TC-WEB-007 | REQ-003 | Workflow / UI vs API comparison | 1 | - | Pass |
| TC-AUT-081 | test_07_web_forms :: test_web_toggle_matches_api | TC-WEB-008 | REQ-004 | State transition / UI vs API comparison | 1 | - | Pass |
| TC-AUT-082 | test_07_web_forms :: test_web_delete_matches_api | TC-WEB-009 | REQ-003 | Workflow / UI vs API comparison | 1 | - | Pass |
| TC-AUT-083 | test_07_web_forms :: test_web_blank_title_validated_on_server | TC-WEB-010 | REQ-003 | Client-server validation / EP | 2 | DEF-003 | 2 Fail (known) |
| TC-AUT-084 | test_07_web_forms :: test_web_due_date_validated_on_server | TC-WEB-011 | REQ-003, REQ-006 | Client-server validation / EP | 2 | DEF-015 | 2 Fail (known) |
| TC-AUT-085 | test_07_web_forms :: test_web_category_validated_on_server | TC-WEB-012 | REQ-003 | Client-server validation / EP | 1 | DEF-019 | Fail (known) |
| TC-AUT-086 | test_07_web_forms :: test_web_actions_on_another_users_task | TC-WEB-013 | REQ-008 | EP (foreign id) / UI vs API comparison | 1 | - | Pass |
| TC-AUT-087 | test_07_web_forms :: test_web_dashboard_matches_api | TC-WEB-014 | REQ-007 | UI vs API comparison | 1 | - | Pass |
| TC-AUT-088 | test_07_web_forms :: test_web_search_with_apostrophe | TC-WEB-015 | REQ-005 | EP (special character) / UI vs API comparison | 1 | - | Pass |
| TC-AUT-089 | test_07_web_forms :: test_web_duplicate_username_rejected | TC-WEB-016 | REQ-001 | EP / web negative | 1 | DEF-016 | Fail (known) |
| **Total** | | | | | **101** | | **69 Pass, 32 Fail (known)** |

### Deviations from the Week 4 procedure

| Case | Difference from the Postman case | Why it does not weaken the check |
| --- | --- | --- |
| All | Each check registers its own users, instead of one set of users per Postman folder | Removes the order dependence that DEF-015 forced on Week 4 (folder 99 had to run last). |
| TC-API-019, 036f; TC-WEB-011 | Fresh users per invalid-date variant, so each variant starts from a user whose list still loads | In Week 4, variants b and c ran on a user already broken by variant a. Here each variant shows the full symptom on its own. |
| TC-API-010, TC-API-001, TC-API-009 | Also check whether a session was started (`GET /api/tasks` is 200 after a valid login and 401 after a failed one) | Adds the "starts a session" / "no session" part of the Week 4 objective at no extra cost. |
| TC-API-031 | Five tasks created by the check itself | The Week 4 precondition says three tasks, but its expected results (pages of 2, 2 and 1, "all five tasks") need five. |
| TC-WEB-014 | A four-task set (today-1, today+1, no date, one completed) compared between the web page and the API | Week 4 used "a similar four-task set". No task is due today, so the comparison does not depend on DEF-002. |
| TC-API-002a | The 3-character username comes from a per-run counter (`u` + two base-36 characters) | A 3-character name cannot include the time. It is unique within a run on the isolated database. |
