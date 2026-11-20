# Regression run 20261120-210434

| Item | Value |
| --- | --- |
| run_started | 2026-11-20T21:04:34 |
| run_finished | 2026-11-20T21:05:08 |
| wall_time_s | 34.4 |
| timezone | Malay Peninsula Standard Time |
| execution_date_used_for_due_dates | 2026-11-20 |
| app_commit | 9cc1f34 |
| browser | MicrosoftEdge 157.0.4341.60 |
| headless | True |
| selenium | 4.53.0 |
| pytest | 9.2.0 |
| python | 3.14.7 |
| os | Windows 11 (10.0.26200) |
| target | isolated server on port 5006 |
| run_label | defects-as-failures |
| marker_expression | (all) |
| defects_as_failures | True |
| pytest_exit_status | 1 |
| counts | {'Pass': 58, 'Fail': 7} |

| Auto ID | Manual case(s) | Requirement | Known defect | Smoke | Status | Time (s) | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-AUT-001 | TC-BB-001 | REQ-001 | - |  | Pass | 0.22 |  |
| TC-AUT-001 | TC-BB-002 | REQ-001 | - |  | Pass | 0.33 |  |
| TC-AUT-001 | TC-BB-003 | REQ-001 | - |  | Pass | 0.28 |  |
| TC-AUT-001 | TC-BB-004 | REQ-001 | - |  | Pass | 0.3 |  |
| TC-AUT-001 | TC-BB-005 | REQ-001 | - |  | Pass | 0.3 |  |
| TC-AUT-001 | TC-BB-006 | REQ-001 | - |  | Pass | 0.23 |  |
| TC-AUT-002 | TC-BB-007 | REQ-001 | - |  | Pass | 0.21 |  |
| TC-AUT-002 | TC-BB-008, TC-GUI-004 | REQ-001 | DEF-001 |  | Fail | 0.21 | AssertionError: expected the task list after registration, browser is on /register (error shown: 'Password must be at least 8 characters.') [screenshot](screenshots/test_password_length_boundaries_TC-BB-008-len8_.png) |
| TC-AUT-002 | TC-BB-009 | REQ-001 | - |  | Pass | 0.3 |  |
| TC-AUT-003 | TC-BB-010 | REQ-001 | - | Y | Pass | 0.34 |  |
| TC-AUT-004 | TC-BB-011 | REQ-001 | - |  | Pass | 0.23 |  |
| TC-AUT-005 | TC-BB-012 | REQ-001 | - |  | Pass | 0.15 |  |
| TC-AUT-005 | TC-BB-013 | REQ-001 | - |  | Pass | 0.14 |  |
| TC-AUT-006 | TC-BB-014 | REQ-002 | - | Y | Pass | 0.41 |  |
| TC-AUT-006 | TC-BB-015 | REQ-002 | - |  | Pass | 0.41 |  |
| TC-AUT-006 | TC-BB-016 | REQ-002 | - |  | Pass | 0.35 |  |
| TC-AUT-006 | TC-BB-017 | REQ-002 | - |  | Pass | 0.39 |  |
| TC-AUT-007 | TC-BB-018 | REQ-002 | - | Y | Pass | 0.05 |  |
| TC-AUT-007 | TC-BB-018 | REQ-002 | - | Y | Pass | 0.05 |  |
| TC-AUT-007 | TC-BB-018 | REQ-002 | - | Y | Pass | 0.05 |  |
| TC-AUT-008 | TC-BB-019 | REQ-002 | - | Y | Pass | 0.18 |  |
| TC-AUT-009 | TC-BB-020 | REQ-003 | - | Y | Pass | 0.71 |  |
| TC-AUT-010 | TC-BB-021 | REQ-003 | - |  | Pass | 0.22 |  |
| TC-AUT-011 | TC-BB-022 | REQ-003 | - |  | Pass | 0.19 |  |
| TC-AUT-012 | TC-BB-023, TC-GUI-016 | REQ-003 | DEF-003 |  | Fail | 0.17 | AssertionError: whitespace-only title created 1 task(s): [''] [screenshot](screenshots/test_whitespace_only_title_rejected.png) |
| TC-AUT-013 | TC-BB-024, TC-GUI-012, TC-GUI-015 | REQ-003 | - |  | Pass | 0.69 |  |
| TC-AUT-014 | TC-BB-025 | REQ-003 | - |  | Pass | 0.7 |  |
| TC-AUT-015 | TC-BB-026, TC-GUI-013 | REQ-003 | - |  | Pass | 0.25 |  |
| TC-AUT-016 | TC-BB-027, TC-GUI-013 | REQ-003 | - | Y | Pass | 0.38 |  |
| TC-AUT-017 | TC-BB-028, TC-BB-029, TC-GUI-011 | REQ-004 | - | Y | Pass | 0.38 |  |
| TC-AUT-018 | TC-GUI-020 | REQ-003 | - |  | Pass | 0.24 |  |
| TC-AUT-019 | TC-GUI-020 | REQ-003 | DEF-005 |  | Fail | 0.07 | AssertionError: list shows ['GUI-Special & bold "double" \'single\' Résumé 报告'] instead of the saved title [screenshot](screenshots/test_special_characters_displayed_literally_in_list.png) |
| TC-AUT-020 | TC-BB-044 | REQ-008 | - | Y | Pass | 1.01 |  |
| TC-AUT-021 | TC-BB-030 | REQ-005 | - |  | Pass | 0.24 |  |
| TC-AUT-021 | TC-BB-031 | REQ-005 | - |  | Pass | 0.26 |  |
| TC-AUT-021 | TC-BB-032 | REQ-005 | - |  | Pass | 0.19 |  |
| TC-AUT-021 | TC-BB-033 | REQ-005 | - |  | Pass | 0.28 |  |
| TC-AUT-021 | TC-BB-034 | REQ-005 | - |  | Pass | 0.18 |  |
| TC-AUT-021 | TC-BB-035, TC-GUI-008 | REQ-005 | - | Y | Pass | 0.37 |  |
| TC-AUT-022 | TC-BB-036 | REQ-006 | - |  | Pass | 0.21 |  |
| TC-AUT-022 | TC-BB-037 | REQ-006 | - |  | Pass | 0.19 |  |
| TC-AUT-022 | TC-BB-038, TC-GUI-010 | REQ-006 | DEF-002 |  | Fail | 0.19 | AssertionError: BB-TODAY due 2026-11-20 shows 'Overdue' [screenshot](screenshots/test_urgency_label_TC-BB-038-today_.png) |
| TC-AUT-022 | TC-BB-039 | REQ-006 | - |  | Pass | 0.19 |  |
| TC-AUT-022 | TC-BB-040 | REQ-006 | - |  | Pass | 0.19 |  |
| TC-AUT-022 | TC-BB-041 | REQ-006 | - |  | Pass | 0.19 |  |
| TC-AUT-023 | TC-BB-042 | REQ-004, REQ-006 | - |  | Pass | 0.2 |  |
| TC-AUT-024 | TC-BB-043 | REQ-007 | - |  | Pass | 0.13 |  |
| TC-AUT-025 | TC-BB-043 | REQ-007 | DEF-002 |  | Fail | 0.12 | AssertionError: Overdue counter is 2, expected 1 (only BB-YESTERDAY is overdue) [screenshot](screenshots/test_dashboard_overdue_counter.png) |
| TC-AUT-026 | TC-BB-001 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-002 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-003 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-004 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-005 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-006 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-011 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-026 | TC-BB-010 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-027 | TC-BB-007 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-027 | TC-BB-008 | REQ-001 | DEF-001 |  | Fail | 0.0 | AssertionError: assert False is True |
| TC-AUT-027 | TC-BB-009 | REQ-001 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-036 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-037 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-038 | REQ-006 | DEF-002 |  | Fail | 0.0 | AssertionError: assert 'Overdue' == 'Due Today' |
| TC-AUT-028 | TC-BB-039 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-040 | REQ-006 | - |  | Pass | 0.0 |  |
| TC-AUT-028 | TC-BB-041 | REQ-006 | - |  | Pass | 0.0 |  |
