# Week 5 - Defects

Defects first found in Week 5, in the project Defect Report Template, followed by earlier defects re-tested this week. Status: Open for all.

- **Security defects (DEF-024 to DEF-036):** found 2026-11-25 by SEC cases; environment: desktop PC, AMD Ryzen 5 5500, Windows 64-bit, Python 3.12.10, app run with `python app.py` on a fresh database, requests sent with Python `requests`.
- **Performance defect (DEF-037):** found 2026-11-27 by PERF-07; environment: MacBook Air M4, macOS 26.5.2, JMeter 5.6.3, app on port 5015.

| Defect | Title | Severity / Priority | Test |
| --- | --- | --- | --- |
| [DEF-024](#def-024---no-throttling-of-failed-logins) | No throttling of failed logins | Moderate / Medium | SEC-02 |
| [DEF-025](#def-025---session-cookie-has-no-samesite-attribute) | Session cookie has no SameSite attribute | Minor / Low | SEC-04 |
| [DEF-026](#def-026---session-cookie-still-valid-after-logout) | Session cookie still valid after logout | Moderate / Medium | SEC-05 |
| [DEF-027](#def-027---common-passwords-accepted) | Common passwords accepted | Minor / Low | SEC-06 |
| [DEF-028](#def-028---hard-coded-secret_key-allows-forging-a-session-for-any-user) | Hard-coded SECRET_KEY allows forging a session for any user | **Critical / High** | SEC-20 |
| [DEF-029](#def-029---sql-injection-in-api-search-exposes-all-users-tasks) | SQL injection in API search exposes all users' tasks | **Critical / High** | SEC-07b |
| [DEF-030](#def-030---no-csrf-protection-on-web-forms) | No CSRF protection on web forms | Moderate / Medium | SEC-09a/b |
| [DEF-031](#def-031---debugtrue-exposes-tracebacks-and-the-werkzeug-debugger) | debug=True exposes tracebacks and the Werkzeug debugger | Major / High | SEC-13, SEC-23 |
| [DEF-032](#def-032---security-headers-missing) | Security headers missing | Minor / Low | SEC-14 |
| [DEF-033](#def-033---no-maximum-title-length) | No maximum title length | Moderate / Medium | SEC-16 |
| [DEF-034](#def-034---per_page-not-capped--1-returns-everything) | `per_page` not capped; `-1` returns everything | Moderate / Low | SEC-17 |
| [DEF-035](#def-035---no-audit-log-of-security-events) | No audit log of security events | Minor / Low | SEC-11 |
| [DEF-036](#def-036---flask-303-has-a-known-vulnerability) | Flask 3.0.3 has a known vulnerability | Minor / Low | SEC-22 |
| [DEF-037](#def-037---home-page-and-dashboard-slow-down-linearly-with-a-users-task-count) | Home page and dashboard slow down linearly with a user's task count | Moderate / Low | PERF-07 |

## DEF-024 - No throttling of failed logins

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-024 |
| Title | Unlimited failed login attempts are accepted without delay or lockout |
| Affected Feature | Login (`/login`, `/api/login`) |
| Environment | Security environment (above) |
| Preconditions | `sec_user_a` exists |
| Steps to Reproduce | 1. Send 20 `POST /api/login` requests for `sec_user_a` with wrong passwords.<br>2. Send one with the correct password. |
| Expected Result | 429 or a temporary lockout after a small number of failures |
| Actual Result | All 20 return 401 immediately; the correct password then returns 200 |
| Severity | Moderate - passwords can be guessed without limit |
| Priority | Medium |
| Evidence | SEC-02 in [security_run_raw.txt](evidences/security/security_run_raw.txt) |
| Status | Open |

## DEF-025 - Session cookie has no SameSite attribute

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-025 |
| Title | Session cookie is set without `SameSite` |
| Affected Feature | Sessions |
| Environment | Security environment (above) |
| Preconditions | `sec_user_a` exists |
| Steps to Reproduce | 1. `POST /api/login` as `sec_user_a`.<br>2. Read the `Set-Cookie` header. |
| Expected Result | `HttpOnly` and `SameSite=Lax` (or stricter) |
| Actual Result | `session=...; HttpOnly; Path=/` with no `SameSite` |
| Severity | Minor - weakens CSRF defence (DEF-030); Chrome and Edge default to `Lax`, other browsers are less consistent |
| Priority | Low |
| Evidence | SEC-04 in [security_run_raw.txt](evidences/security/security_run_raw.txt) |
| Status | Open |

## DEF-026 - Session cookie still valid after logout

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-026 |
| Title | Logging out does not invalidate a copied session cookie |
| Affected Feature | Logout / sessions |
| Environment | Security environment (above) |
| Preconditions | Logged in as `sec_user_a` |
| Steps to Reproduce | 1. Copy the session cookie.<br>2. `GET /logout`.<br>3. Send `GET /api/tasks` with the copied cookie. |
| Expected Result | 401 |
| Actual Result | 200 with the full task list; the cookie is signed client-side and logout clears only the browser's copy |
| Severity | Moderate - a stolen cookie stays usable after the user logs out |
| Priority | Medium |
| Evidence | SEC-05 in [security_run_raw.txt](evidences/security/security_run_raw.txt) |
| Status | Open |

## DEF-027 - Common passwords accepted

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-027 |
| Title | Registration accepts well-known weak passwords |
| Affected Feature | Registration |
| Environment | Security environment (above) |
| Preconditions | Username not yet registered |
| Steps to Reproduce | 1. `POST /api/register` with password `password123`. |
| Expected Result | Rejected (400) |
| Actual Result | 201; only length is checked |
| Severity | Minor |
| Priority | Low |
| Evidence | SEC-06 in [security_run_raw.txt](evidences/security/security_run_raw.txt) |
| Status | Open |

## DEF-028 - Hard-coded SECRET_KEY allows forging a session for any user

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-028 |
| Title | Anyone who reads `app.py` can sign a valid session cookie for any user |
| Affected Feature | Authentication / sessions (`app.py` line 28) |
| Environment | Security environment (above) |
| Preconditions | User A exists and has tasks; A's numeric id is known (ids are sequential) |
| Steps to Reproduce | 1. Create a Flask object with `secret_key = "pytodo-pro-dev-secret"`.<br>2. Sign `{"user_id": <A>, "username": "sec_user_a"}` with `SecureCookieSessionInterface().get_signing_serializer()`.<br>3. Send `GET /api/tasks` with `Cookie: session=<signed value>`. |
| Expected Result | 401: a cookie not issued by the server is rejected |
| Actual Result | 200 with A's private tasks: full access to any account without a password |
| Severity | Critical |
| Priority | High |
| Evidence | SEC-20; [SEC-20_forged_cookie_DEF-028.png](evidences/security/SEC-20_forged_cookie_DEF-028.png); bandit B105 ([bandit.txt](evidences/security/bandit.txt)) |
| Status | Open |

## DEF-029 - SQL injection in API search exposes all users' tasks

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-029 |
| Title | `GET /api/tasks?q=` builds SQL from user input |
| Affected Feature | API search (`api_list_tasks`, f-string `LIKE` clause) |
| Environment | Security environment (above) |
| Preconditions | Users A and B each have tasks |
| Steps to Reproduce | 1. Log in as A.<br>2. `GET /api/tasks?q=%' OR user_id != 0 OR title LIKE '&per_page=100` |
| Expected Result | Only A's matching tasks (or none) |
| Actual Result | Tasks of every user are returned. Same root cause as DEF-017 (crash on `'`), but the impact is a data breach. |
| Severity | Critical |
| Priority | High |
| Evidence | SEC-07b; [leak](evidences/security/SEC-07b_01_sqli_leak_other_users_tasks.png); [crash on another user's row](evidences/security/SEC-07b_02_sqli_crash_on_other_users_row.png) |
| Status | Open |

## DEF-030 - No CSRF protection on web forms

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-030 |
| Title | Web forms have no CSRF token and the server does not check the request origin |
| Affected Feature | Web task actions and login |
| Environment | Security environment (above) |
| Preconditions | Logged in as `sec_user_a` with a task |
| Steps to Reproduce | 1. Inspect the POST forms on `/` and `/login`.<br>2. Send `POST /tasks/<id>/delete` with the session cookie and `Origin: http://evil.example`. |
| Expected Result | Each form has a token; the cross-origin request is refused |
| Actual Result | 0 of 5 forms have a token; the task is deleted |
| Severity | Moderate - another site could trigger actions for a logged-in user (partly limited by browsers' default `SameSite=Lax`) |
| Priority | Medium |
| Evidence | SEC-09a, SEC-09b in [security_run_raw.txt](evidences/security/security_run_raw.txt) |
| Status | Open |

## DEF-031 - debug=True exposes tracebacks and the Werkzeug debugger

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-031 |
| Title | Server errors show the interactive Werkzeug debugger |
| Affected Feature | Error handling (`app.run(debug=True)`, `app.py` line 482) |
| Environment | Security environment (above) |
| Preconditions | Logged in |
| Steps to Reproduce | 1. `GET /api/tasks?q='` |
| Expected Result | Generic 500 message |
| Actual Result | Debugger page with stack trace, SQL error text and source paths. Its console can run Python code if its PIN is obtained (not attempted). |
| Severity | Major |
| Priority | High |
| Evidence | SEC-13; [console](evidences/security/SEC-13_01_debug_mode_on_app_window.png), [traceback](evidences/security/SEC-13_02_debugger_traceback_top.png), [debugger](evidences/security/SEC-13_03_debugger_console_offer.png); bandit B201 High |
| Status | Open |

## DEF-032 - Security headers missing

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-032 |
| Title | Responses have no clickjacking, MIME-sniffing or content-security headers |
| Affected Feature | All pages |
| Environment | Security environment (above) |
| Preconditions | Logged in |
| Steps to Reproduce | 1. `GET /` and read the response headers. |
| Expected Result | `X-Content-Type-Options`, `X-Frame-Options` (or CSP `frame-ancestors`) and `Content-Security-Policy` |
| Actual Result | None present |
| Severity | Minor |
| Priority | Low |
| Evidence | SEC-14 in [security_run_raw.txt](evidences/security/security_run_raw.txt) |
| Status | Open |

## DEF-033 - No maximum title length

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-033 |
| Title | Task titles of any length are stored and rendered |
| Affected Feature | Create task (API) |
| Environment | Security environment (above) |
| Preconditions | Logged in |
| Steps to Reproduce | 1. `POST /api/tasks` with a 100,000-character title. |
| Expected Result | 400, 413 or 422 |
| Actual Result | 201; the title is stored and rendered in full |
| Severity | Moderate - large payloads can bloat the database and slow pages |
| Priority | Medium |
| Evidence | SEC-16 in [security_run_raw.txt](evidences/security/security_run_raw.txt) |
| Status | Open |

## DEF-034 - `per_page` not capped; `-1` returns everything

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-034 |
| Title | Page size is used as-is in the SQL `LIMIT` |
| Affected Feature | Task list API |
| Environment | Security environment (above) |
| Preconditions | Logged in with tasks |
| Steps to Reproduce | 1. `GET /api/tasks?per_page=1000000`<br>2. `GET /api/tasks?per_page=-1` |
| Expected Result | Value capped (e.g. 100) or 400 |
| Actual Result | Both 200; `-1` returns every task with no limit. Related to DEF-022 (Week 4), with the resource-exhaustion angle. |
| Severity | Moderate |
| Priority | Low |
| Evidence | SEC-17 in [security_run_raw.txt](evidences/security/security_run_raw.txt) |
| Status | Open |

## DEF-035 - No audit log of security events

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-035 |
| Title | Logins, failed logins and deletions are not logged with the user |
| Affected Feature | Logging |
| Environment | Security environment (above) |
| Preconditions | Server console visible |
| Steps to Reproduce | 1. Log in.<br>2. Fail a login.<br>3. Delete a task.<br>4. Read the server console. |
| Expected Result | Each event recorded with user and time |
| Actual Result | Only request lines such as `"POST /api/login HTTP/1.1" 200`; no username and no failed-login record |
| Severity | Minor - actions cannot be traced to a user |
| Priority | Low |
| Evidence | SEC-11 (manual observation) |
| Status | Open |

## DEF-036 - Flask 3.0.3 has a known vulnerability

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-036 |
| Title | Pinned Flask version has CVE-2026-27205 |
| Affected Feature | Dependencies (`requirements.txt`) |
| Environment | Security environment (above) |
| Preconditions | - |
| Steps to Reproduce | 1. `pip-audit -r requirements.txt` |
| Expected Result | No known vulnerabilities |
| Actual Result | Flask 3.0.3: PYSEC-2026-2151 / CVE-2026-27205 (missing `Vary: Cookie` in some cases; needs a caching proxy to matter), fixed in 3.1.3 |
| Severity | Minor |
| Priority | Low |
| Evidence | SEC-22; [screenshot](evidences/security/SEC-22_pip_audit.png), [pip_audit.txt](evidences/security/pip_audit.txt) |
| Status | Open |

## DEF-037 - Home page and dashboard slow down linearly with a user's task count

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-037 |
| Title | `GET /` and `GET /api/dashboard` response time grows with the number of tasks a user owns |
| Affected Feature | Task list page (`index()`, `row_to_task()`), dashboard |
| Environment | Performance environment (above); JMeter plan `pytodo_data_volume.jmx` |
| Preconditions | Fresh database; one user (`volume_user`) with 50, 500 or 2,000 tasks |
| Steps to Reproduce | 1. `python jmeter/run_performance.py --out <dir>` (PERF-07 runs at the end), or run `pytodo_data_volume.jmx` with `-Jseed_tasks=2000`.<br>2. Compare the median of `GET /` at 50 and 2,000 tasks. |
| Expected Result | Roughly constant response time (the page should be paged) |
| Actual Result | Home page median 2 ms at 50 tasks, 12 ms at 500, 40 ms at 2,000 (20×); dashboard 1 -> 10 ms; the paged API stays at 1 ms. `index()` has no paging and `row_to_task()` runs one category query per task (N+1). Under stress the home page is also the first endpoint to miss the p95 target (1,019 ms at 100 users, PERF-06). |
| Severity | Moderate |
| Priority | Low - only heavy users are affected at current sizes |
| Evidence | PERF-07; [perf_summary.md](evidences/performance/20261127-mac/perf_summary.md), [chart](evidences/performance/20261127-mac/perf_volume_chart.png), `PERF-07_*tasks.jtl.gz` |
| Status | Open |

## Re-tested defects

| Defect | Original record | Re-tested by | Result | Severity change |
| --- | --- | --- | --- | --- |
| DEF-005 | [Week 3](../03_Special_Testing/defects.md#def-005---task-title-html-is-rendered-as-markup) | SEC-12 | Still fails, and worse: a script payload in a title executes when the list loads (stored XSS). Combined with DEF-030 or DEF-028, an attacker can plant it in another user's list | Moderate / High -> **Major / High** |
| DEF-014 | [Week 4](../04_Web_API/defects.md#def-014---any-logged-in-user-can-delete-another-users-task-through-the-api) | SEC-18 | Still fails: B deletes A's task (200) | None (Critical) |
| DEF-015 | [Week 4](../04_Web_API/defects.md#def-015---an-invalid-due-date-is-saved-and-then-breaks-that-users-task-list-and-dashboard) | SEC-24 | Still fails: bad date saved, dashboard 500 | None (Critical) |
| DEF-017 | [Week 4](../04_Web_API/defects.md#def-017---api-search-text-containing-an-apostrophe-causes-a-500-error) | SEC-07a | Still fails: 500 on `O'Brien`; root cause confirmed as SQL injection (DEF-029) | None |
| DEF-023 | [Week 4](../04_Web_API/defects.md#def-023---apicategories-works-without-login-contrary-to-the-readme) | SEC-03 | Still fails: `/api/categories` 200 without login | None |
