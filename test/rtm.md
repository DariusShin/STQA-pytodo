# Requirements Traceability Matrix

Built in Week 7 from the [master test-case repository](master_test_cases.md). Result counts are cases (Pass / Fail / Blocked).

## Requirements

| ID | Requirement / feature | Expected behaviour | Defined in |
| --- | --- | --- | --- |
| REQ-001 | Registration | Valid details are accepted; invalid usernames and passwords are rejected | Week 1 |
| REQ-002 | Login, logout and protected pages | Valid credentials give access; logout and missing sessions deny it | Week 1 |
| REQ-003 | Create, view, edit and delete tasks | Saved task data persists; invalid task data is rejected | Week 1 |
| REQ-004 | Complete and reopen tasks | State changes and urgency stay consistent | Week 1 |
| REQ-005 | Filters and title search | Results satisfy every active condition | Week 1 |
| REQ-006 | Due-date urgency | Each task gets the documented urgency class | Week 1 |
| REQ-007 | Dashboard | Counters match the user's task data | Week 1 |
| REQ-008 | User task separation | Each user can see and change only their own tasks | Week 1 |
| REQ-009 | JSON REST API contract | Correct status codes, session authentication and JSON errors for invalid input | Week 4 |
| REQ-010 | GUI and compatibility | Pages present consistent controls, labels and messages and work on the selected browsers and viewports | Week 7 (from Week 3) |
| REQ-011 | Usability | Navigation, feedback, consistency, error prevention and understandability | Week 7 (from Week 3) |
| REQ-012 | Accessibility | Pages meet the selected WCAG 2.2 Level A/AA criteria | Week 7 (from Week 3) |
| REQ-013 | Security | STRIDE threats to accounts, sessions and task data are mitigated | Week 7 (from Week 5) |
| REQ-014 | Performance | Response time and error targets are met at expected load; the app degrades gracefully under stress | Week 7 (from Week 5) |

## Traceability

| Requirement/Feature | Test Scenario | Test Case ID(s) | Test Type/Technique | Result | Defect ID |
| --- | --- | --- | --- | --- | --- |
| REQ-001 Registration | Week 1 Black-box | TC-BB-001 to 013 | BVA, Browser validation, EP, Functional | 12 / 1 / 0 | DEF-001 |
| REQ-001 Registration | Week 2 White-box | TC-WB-026, 027 | Statement coverage | 2 / 0 / 0 | — |
| REQ-001 Registration | Week 3 GUI | TC-GUI-003, 004 | GUI checklist | 1 / 1 / 0 | DEF-001 |
| REQ-001 Registration | Week 3 Compatibility | TC-CMP-001 | Compatibility | 1 / 0 / 0 | — |
| REQ-001 Registration | Week 4 Web and API | TC-WEB-001, 002, 016; TC-API-001 to 008 | API, API functional, API negative, BVA, Client-server validation ... | 7 / 4 / 0 | DEF-001, DEF-016, DEF-018 |
| REQ-001 Registration | Week 6 Automation and regression | TC-AUT-001 to 005, 026, 027, 029 to 036, 074, 075, 089 | API, API functional, API negative, BVA, BVA (unit) ... | 12 / 6 / 0 | DEF-001, DEF-016, DEF-018 |
| REQ-002 Login, logout and protected pages | Week 1 Black-box | TC-BB-014 to 019 | Decision table, Functional, State transition | 6 / 0 / 0 | — |
| REQ-002 Login, logout and protected pages | Week 2 White-box | TC-WB-014 to 019, 023, 024 | Basis path AA01, Basis path AA02, Basis path AF01, Basis path WA01, Basis path WA02 ... | 8 / 0 / 0 | — |
| REQ-002 Login, logout and protected pages | Week 3 GUI | TC-GUI-001, 002, 005, 006 | GUI checklist | 3 / 1 / 0 | DEF-004 |
| REQ-002 Login, logout and protected pages | Week 3 Compatibility | TC-CMP-001, 007 | Compatibility | 1 / 1 / 0 | DEF-006 |
| REQ-002 Login, logout and protected pages | Week 4 Web and API | TC-WEB-003, 004; TC-API-009 to 011 | API, API negative, Decision table, Decision table (valid, EP (unauthenticated) ... | 5 / 0 / 0 | — |
| REQ-002 Login, logout and protected pages | Week 6 Automation and regression | TC-AUT-006 to 008, 037 to 039, 076, 077 | API, API negative, Decision table, Decision table (valid, EP (unauthenticated) ... | 8 / 0 / 0 | — |
| REQ-003 Create, view, edit and delete tasks | Week 1 Black-box | TC-BB-020 to 027 | Browser validation, EP, Functional, Input validation, State transition | 7 / 1 / 0 | DEF-003 |
| REQ-003 Create, view, edit and delete tasks | Week 2 White-box | TC-WB-001 to 013, 020 to 022 | Basis path CI01, Basis path CI02, Basis path CL01, Basis path CL02, Basis path CN01 ... | 16 / 0 / 0 | — |
| REQ-003 Create, view, edit and delete tasks | Week 3 GUI | TC-GUI-007, 009, 012 to 017, 019, 020 | GUI checklist, Usability heuristic | 7 / 3 / 0 | DEF-003, DEF-005 |
| REQ-003 Create, view, edit and delete tasks | Week 3 Compatibility | TC-CMP-002, 005 to 007 | Compatibility | 3 / 1 / 0 | DEF-006 |
| REQ-003 Create, view, edit and delete tasks | Week 4 Web and API | TC-WEB-005 to 007, 009 to 012; TC-API-014 to 016, 018 to 020, 022, 023, 034, 036, 039 | API, API functional, API negative, API vs UI comparison, Client-server validation ... | 11 / 7 / 0 | DEF-003, DEF-015, DEF-018, DEF-019, DEF-020 |
| REQ-003 Create, view, edit and delete tasks | Week 6 Automation and regression | TC-AUT-009 to 016, 018, 019, 042 to 044, 046 to 048, 050, 051, 062, 064, 067, 078 to 080, 082 to 085 | API, API functional, API negative, API vs UI comparison, Client-server validation ... | 19 / 9 / 0 | DEF-003, DEF-005, DEF-015, DEF-018, DEF-019, DEF-020 |
| REQ-004 Complete and reopen tasks | Week 1 Black-box | TC-BB-028, 029, 042 | Functional, State transition | 3 / 0 / 0 | — |
| REQ-004 Complete and reopen tasks | Week 3 GUI | TC-GUI-011, 017 | GUI checklist, Usability heuristic | 1 / 1 / 0 | — |
| REQ-004 Complete and reopen tasks | Week 3 Compatibility | TC-CMP-004 | Compatibility | 1 / 0 / 0 | — |
| REQ-004 Complete and reopen tasks | Week 4 Web and API | TC-WEB-008; TC-API-035 | API, State transition, State transition (Open -> Done -> Open), UI vs API comparison | 2 / 0 / 0 | — |
| REQ-004 Complete and reopen tasks | Week 6 Automation and regression | TC-AUT-017, 023, 063, 081 | API, State transition, State transition (Open -> Done -> Open), UI vs API comparison | 4 / 0 / 0 | — |
| REQ-005 Filters and title search | Week 1 Black-box | TC-BB-030 to 035 | Decision table, EP, Functional | 6 / 0 / 0 | — |
| REQ-005 Filters and title search | Week 3 GUI | TC-GUI-008, 009 | GUI checklist | 2 / 0 / 0 | — |
| REQ-005 Filters and title search | Week 3 Compatibility | TC-CMP-003 | Compatibility | 1 / 0 / 0 | — |
| REQ-005 Filters and title search | Week 4 Web and API | TC-WEB-015; TC-API-026 to 031 | API functional, API negative, BVA, Decision table, EP ... | 6 / 1 / 0 | DEF-017 |
| REQ-005 Filters and title search | Week 6 Automation and regression | TC-AUT-021, 054 to 059, 088 | API functional, API negative, BVA, Decision table, EP ... | 7 / 1 / 0 | DEF-017 |
| REQ-006 Due-date urgency | Week 1 Black-box | TC-BB-036 to 042 | BVA, EP, Functional, State transition | 6 / 1 / 0 | DEF-002 |
| REQ-006 Due-date urgency | Week 2 White-box | TC-WB-025 | Statement coverage | 1 / 0 / 0 | — |
| REQ-006 Due-date urgency | Week 3 GUI | TC-GUI-010 | GUI checklist | 0 / 1 / 0 | DEF-002 |
| REQ-006 Due-date urgency | Week 3 Compatibility | TC-CMP-002 | Compatibility | 1 / 0 / 0 | — |
| REQ-006 Due-date urgency | Week 4 Web and API | TC-WEB-006, 011; TC-API-019, 021, 043 | API, API negative, API vs UI comparison, BVA, Client-server validation ... | 1 / 4 / 0 | DEF-002, DEF-015 |
| REQ-006 Due-date urgency | Week 6 Automation and regression | TC-AUT-022, 023, 028, 047, 049, 071, 079, 084 | API, API negative, API vs UI comparison, BVA, BVA (unit) ... | 2 / 6 / 0 | DEF-002, DEF-015 |
| REQ-007 Dashboard | Week 1 Black-box | TC-BB-043 | Functional, Independent calculation | 0 / 1 / 0 | DEF-002 |
| REQ-007 Dashboard | Week 2 White-box | TC-WB-028 | Statement coverage | 1 / 0 / 0 | — |
| REQ-007 Dashboard | Week 3 GUI | TC-GUI-018 | GUI checklist | 0 / 1 / 0 | — |
| REQ-007 Dashboard | Week 3 Compatibility | TC-CMP-008 | Compatibility | 1 / 0 / 0 | — |
| REQ-007 Dashboard | Week 4 Web and API | TC-WEB-014; TC-API-042, 043 | API, API functional (oracle: independent count), BVA, UI vs API comparison | 2 / 1 / 0 | DEF-002 |
| REQ-007 Dashboard | Week 6 Automation and regression | TC-AUT-024, 025, 070, 071, 087 | API, API functional (oracle: independent count), BVA, Independent calculation, UI vs API comparison | 3 / 2 / 0 | DEF-002 |
| REQ-008 User task separation | Week 1 Black-box | TC-BB-044 | EP, Functional | 1 / 0 / 0 | — |
| REQ-008 User task separation | Week 4 Web and API | TC-WEB-013; TC-API-024, 033, 037, 040, 044 | API, API negative, EP, EP (foreign id), UI vs API comparison | 5 / 1 / 0 | DEF-014 |
| REQ-008 User task separation | Week 6 Automation and regression | TC-AUT-020, 052, 061, 065, 068, 072, 086 | API, API negative, EP, EP (foreign id), UI vs API comparison | 6 / 1 / 0 | DEF-014 |
| REQ-009 JSON REST API contract | Week 4 Web and API | TC-API-007, 011 to 013, 017, 018, 023, 025, 031, 032, 036, 038, 041, 045 | API functional, API negative, BVA, EP (data type), EP (invalid format) ... | 8 / 6 / 0 | DEF-015, DEF-018, DEF-019, DEF-020, DEF-021, DEF-022, DEF-023 |
| REQ-009 JSON REST API contract | Week 6 Automation and regression | TC-AUT-035, 039 to 041, 045, 046, 051, 053, 059, 060, 064, 066, 069, 073 | API functional, API negative, BVA, EP (data type), EP (invalid format) ... | 8 / 6 / 0 | DEF-015, DEF-018, DEF-019, DEF-020, DEF-021, DEF-022, DEF-023 |
| REQ-010 GUI and compatibility | Week 3 GUI | TC-GUI-001 to 022 | GUI checklist, Usability heuristic | 14 / 8 / 0 | DEF-001, DEF-002, DEF-003, DEF-004, DEF-005 |
| REQ-010 GUI and compatibility | Week 3 Compatibility | TC-CMP-001 to 008 | Compatibility | 7 / 1 / 0 | DEF-006 |
| REQ-011 Usability | Week 3 usability session | USA-OBS-001 to 004 | Usability session, Nielsen heuristics | 4 observations (2 × 1 Cosmetic, 2 × 2 Minor); none at severity 3-4 | — |
| REQ-012 Accessibility | Week 3 Accessibility | TC-A11Y-001 to 018 | Accessibility (WCAG) - automated scan, Accessibility (WCAG) - inspection, Accessibility (WCAG) - keyboard, Accessibility (WCAG) - keyboard and inspection, Accessibility (WCAG) - measurement ... | 7 / 11 / 0 | DEF-004, DEF-007, DEF-008, DEF-009, DEF-010, DEF-011, DEF-012, DEF-013 |
| REQ-013 Security | Week 5 Security and performance | SEC-01 to 24 | Automated, Automated (re-test), Manual, Tool (bandit), Tool (pip-audit) | 6 / 18 / 0 | DEF-005, DEF-014, DEF-015, DEF-017, DEF-023, DEF-024, DEF-025, DEF-026, DEF-027, DEF-028, DEF-029, DEF-030, DEF-031, DEF-032, DEF-033, DEF-034, DEF-035, DEF-036 |
| REQ-014 Performance | Week 5 Security and performance | PERF-01 to 07; PERF-06b | Performance (JMeter) | 6 / 1 / 1 | DEF-037 |

## Coverage check

| Requirement | Cases | Pass | Fail | Blocked | Open defects |
| --- | ---: | ---: | ---: | ---: | ---: |
| REQ-001 Registration | 47 | 35 | 12 | 0 | 3 |
| REQ-002 Login, logout and protected pages | 33 | 31 | 2 | 0 | 2 |
| REQ-003 Create, view, edit and delete tasks | 84 | 63 | 21 | 0 | 7 |
| REQ-004 Complete and reopen tasks | 12 | 11 | 1 | 0 | 0 |
| REQ-005 Filters and title search | 24 | 22 | 2 | 0 | 1 |
| REQ-006 Due-date urgency | 23 | 11 | 12 | 0 | 2 |
| REQ-007 Dashboard | 12 | 7 | 5 | 0 | 1 |
| REQ-008 User task separation | 14 | 12 | 2 | 0 | 1 |
| REQ-009 JSON REST API contract | 28 | 16 | 12 | 0 | 7 |
| REQ-010 GUI and compatibility | 30 | 21 | 9 | 0 | 6 |
| REQ-011 Usability | 4 observations | - | - | - | 0 |
| REQ-012 Accessibility | 18 | 7 | 11 | 0 | 8 |
| REQ-013 Security | 24 | 6 | 18 | 0 | 18 |
| REQ-014 Performance | 8 | 6 | 1 | 1 | 1 |

Every requirement is covered by executed cases (REQ-011 by the usability session), and every case traces to at least one requirement.
