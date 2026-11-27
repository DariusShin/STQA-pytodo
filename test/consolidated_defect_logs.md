# Consolidated Defect Log

All defects of Weeks 1-6 in one table, consolidated in Week 7 from the weekly `defects.md` files and the test cases that reference each defect. Full records (environment, steps, expected and actual results, evidence) are linked from the ID.

**37 defects:** 4 Critical, 6 Major, 16 Moderate, 11 Minor. All are **Open**: the project does not modify the application, so no fix has been delivered for retest.

| Defect | Title | Module | Found in | Found by | Severity | Priority | Status | Re-tested in | Linked cases |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| [DEF-001](01_Black_Box/defects.md#def-001---eight-character-password-is-rejected) | Eight-character password is rejected | Registration and login | Week 1 | TC-BB-008 | Moderate | Medium | Open | Week 3, Week 4, Week 6 | 6 |
| [DEF-002](01_Black_Box/defects.md#def-002---today-is-classified-and-counted-as-overdue) | Today is classified and counted as overdue | Urgency and dashboard | Week 1 | TC-BB-038, 043 | Moderate | High | Open | Week 3, Week 4, Week 6 | 10 |
| [DEF-003](01_Black_Box/defects.md#def-003---whitespace-only-title-creates-a-task-with-a-blank-displayed-title) | Whitespace-only title creates a task with a blank displayed title | Task input validation | Week 1 | TC-BB-023 | Moderate | Medium | Open | Week 3, Week 4, Week 6 | 5 |
| [DEF-004](03_Special_Testing/defects.md#def-004---navigation-bar-breaks-at-a-narrow-viewport) | Navigation bar breaks at a narrow viewport | Layout and responsiveness | Week 3 | TC-GUI-005; TC-A11Y-012 | Moderate | Medium | Open | — | 2 |
| [DEF-005](03_Special_Testing/defects.md#def-005---task-title-html-is-rendered-as-markup) | Task title HTML is rendered as markup | Output rendering | Week 3 | TC-GUI-020 | Major (a) | High | Open | Week 5, Week 6 | 3 |
| [DEF-006](03_Special_Testing/defects.md#def-006---desktop-layout-scaled-down-on-tablets-and-phones) | Desktop layout scaled down on tablets and phones | Layout and responsiveness | Week 3 | TC-CMP-007 | Moderate | Medium | Open | — | 1 |
| [DEF-007](03_Special_Testing/defects.md#def-007---form-fields-have-no-programmatic-labels) | Form fields have no programmatic labels | Accessibility | Week 3 | TC-A11Y-005, 006 | Major | High | Open | — | 2 |
| [DEF-008](03_Special_Testing/defects.md#def-008---completereopen-button-has-no-meaningful-name) | Complete/reopen button has no meaningful name | Accessibility | Week 3 | TC-A11Y-001, 007 | Major | High | Open | — | 2 |
| [DEF-009](03_Special_Testing/defects.md#def-009---low-contrast-text) | Low-contrast text | Accessibility | Week 3 | TC-A11Y-004 | Moderate | Medium | Open | — | 1 |
| [DEF-010](03_Special_Testing/defects.md#def-010---no-main-landmark-or-skip-link) | No main landmark or skip link | Accessibility | Week 3 | TC-A11Y-002, 009 | Minor | Low | Open | — | 2 |
| [DEF-011](03_Special_Testing/defects.md#def-011---errors-not-announced) | Errors not announced | Accessibility | Week 3 | TC-A11Y-015 | Moderate | Medium | Open | — | 1 |
| [DEF-012](03_Special_Testing/defects.md#def-012---small-crowded-targets) | Small, crowded targets | Accessibility | Week 3 | TC-A11Y-016 | Minor | Low | Open | — | 1 |
| [DEF-013](03_Special_Testing/defects.md#def-013---empty-column-headers) | Empty column headers | Accessibility | Week 3 | TC-A11Y-017 | Minor | Low | Open | — | 1 |
| [DEF-014](04_Web_API/defects.md#def-014---any-logged-in-user-can-delete-another-users-task-through-the-api) | Any logged-in user can delete another user's task through the API | Task ownership | Week 4 | TC-API-040 | Critical | High | Open | Week 5, Week 6 | 3 |
| [DEF-015](04_Web_API/defects.md#def-015---an-invalid-due-date-is-saved-and-then-breaks-that-users-task-list-and-dashboard) | An invalid due date is saved and then breaks that user's task list and dashboard | Task input validation | Week 4 | TC-WEB-011; TC-API-019, 036 | Critical | High | Open | Week 5, Week 6 | 7 |
| [DEF-016](04_Web_API/defects.md#def-016---registration-accepts-a-username-that-already-exists) | Registration accepts a username that already exists | Registration and login | Week 4 | TC-WEB-016; TC-API-008 | Major | High | Open | Week 6 | 4 |
| [DEF-017](04_Web_API/defects.md#def-017---api-search-text-containing-an-apostrophe-causes-a-500-error) | API search text containing an apostrophe causes a 500 error | Task list, search and paging | Week 4 | TC-API-030 | Major | High | Open | Week 5, Week 6 | 3 |
| [DEF-018](04_Web_API/defects.md#def-018---wrong-json-data-types-cause-500-errors-instead-of-400) | Wrong JSON data types cause 500 errors instead of 400 | Task input validation | Week 4 | TC-API-007, 018, 036 | Moderate | Medium | Open | Week 6 | 6 |
| [DEF-019](04_Web_API/defects.md#def-019---task-createupdate-accepts-a-category-that-does-not-exist) | Task create/update accepts a category that does not exist | Task input validation | Week 4 | TC-WEB-012; TC-API-020, 036 | Moderate | Medium | Open | Week 6 | 6 |
| [DEF-020](04_Web_API/defects.md#def-020---task-update-skips-title-validation-and-treats-the-text-false-as-done) | Task update skips title validation and treats the text "false" as done | Task input validation | Week 4 | TC-API-036 | Moderate | Medium | Open | Week 6 | 2 |
| [DEF-021](04_Web_API/defects.md#def-021---deleting-a-task-that-does-not-exist-reports-success) | Deleting a task that does not exist reports success | API contract | Week 4 | TC-API-041 | Minor | Low | Open | Week 6 | 2 |
| [DEF-022](04_Web_API/defects.md#def-022---invalid-paging-values-are-not-rejected) | Invalid paging values are not rejected | Task list, search and paging | Week 4 | TC-API-032 | Minor | Low | Open | Week 6 | 2 |
| [DEF-023](04_Web_API/defects.md#def-023---apicategories-works-without-login-contrary-to-the-readme) | `/api/categories` works without login, contrary to the README | Sessions and access control | Week 4 | TC-API-012 | Minor | Low | Open | Week 5, Week 6 | 3 |
| [DEF-024](05_Security_Performance/defects.md#def-024---no-throttling-of-failed-logins) | No throttling of failed logins | Registration and login | Week 5 | SEC-02 | Moderate | Medium | Open | — | 1 |
| [DEF-025](05_Security_Performance/defects.md#def-025---session-cookie-has-no-samesite-attribute) | Session cookie has no SameSite attribute | Sessions and access control | Week 5 | SEC-04 | Minor | Low | Open | — | 1 |
| [DEF-026](05_Security_Performance/defects.md#def-026---session-cookie-still-valid-after-logout) | Session cookie still valid after logout | Sessions and access control | Week 5 | SEC-05 | Moderate | Medium | Open | — | 1 |
| [DEF-027](05_Security_Performance/defects.md#def-027---common-passwords-accepted) | Common passwords accepted | Registration and login | Week 5 | SEC-06 | Minor | Low | Open | — | 1 |
| [DEF-028](05_Security_Performance/defects.md#def-028---hard-coded-secret_key-allows-forging-a-session-for-any-user) | Hard-coded SECRET_KEY allows forging a session for any user | Sessions and access control | Week 5 | SEC-20, 23 | Critical | High | Open | — | 2 |
| [DEF-029](05_Security_Performance/defects.md#def-029---sql-injection-in-api-search-exposes-all-users-tasks) | SQL injection in API search exposes all users' tasks | Task list, search and paging | Week 5 | SEC-07 | Critical | High | Open | — | 1 |
| [DEF-030](05_Security_Performance/defects.md#def-030---no-csrf-protection-on-web-forms) | No CSRF protection on web forms | Sessions and access control | Week 5 | SEC-09 | Moderate | Medium | Open | — | 1 |
| [DEF-031](05_Security_Performance/defects.md#def-031---debugtrue-exposes-tracebacks-and-the-werkzeug-debugger) | debug=True exposes tracebacks and the Werkzeug debugger | Configuration, logging and dependencies | Week 5 | SEC-13, 23 | Major | High | Open | — | 2 |
| [DEF-032](05_Security_Performance/defects.md#def-032---security-headers-missing) | Security headers missing | Configuration, logging and dependencies | Week 5 | SEC-14 | Minor | Low | Open | — | 1 |
| [DEF-033](05_Security_Performance/defects.md#def-033---no-maximum-title-length) | No maximum title length | Task input validation | Week 5 | SEC-16 | Moderate | Medium | Open | — | 1 |
| [DEF-034](05_Security_Performance/defects.md#def-034---per_page-not-capped--1-returns-everything) | `per_page` not capped; `-1` returns everything | Task list, search and paging | Week 5 | SEC-17 | Moderate | Low | Open | — | 1 |
| [DEF-035](05_Security_Performance/defects.md#def-035---no-audit-log-of-security-events) | No audit log of security events | Configuration, logging and dependencies | Week 5 | SEC-11 | Minor | Low | Open | — | 1 |
| [DEF-036](05_Security_Performance/defects.md#def-036---flask-303-has-a-known-vulnerability) | Flask 3.0.3 has a known vulnerability | Configuration, logging and dependencies | Week 5 | SEC-22 | Minor | Low | Open | — | 1 |
| [DEF-037](05_Security_Performance/defects.md#def-037---home-page-and-dashboard-slow-down-linearly-with-a-users-task-count) | Home page and dashboard slow down linearly with a user's task count | Performance | Week 5 | PERF-07 | Moderate | Low | Open | — | 1 |

(a) DEF-005: Upgraded from Moderate in Week 5 (stored XSS confirmed).
