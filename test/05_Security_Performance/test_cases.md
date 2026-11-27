# Week 5 - Security and Performance Test Cases

Cases in the project Test Case Template. Security cases SEC-01 to 24 were derived from the STRIDE table ([W5_Report.md section 3](W5_Report.md#3-stride-threat-table)); performance cases PERF-01 to 07 follow the workload in [section 5](W5_Report.md#5-performance-test-design).

## Security cases (SEC)

Executed 2026-11-25 by Wan Haziqah Binti Wan Hanafi (environment: W5_Report header). Common preconditions: app running at `http://127.0.0.1:5000` with a fresh database; the `user_a` / `user_b` fixtures register `sec_user_a` and `sec_user_b` (password `Passw0rd!23`) and create their tasks. Automated steps are pytest functions in [test_security.py](test_security.py) (`test_SEC_<id>_...`). Raw output: [security_run_raw.txt](evidences/security/security_run_raw.txt); regression view: [security_run.txt](evidences/security/security_run.txt).

| Test Case ID | Feature / threat | Technique | Objective | Test data / steps | Expected result | Actual result | Status | Evidence | Defect ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEC-01 | Login / TH-01 | Automated (pytest) | Login errors do not reveal which field is wrong | Login with an unknown user, then a known user with a wrong password (API and web) | Identical responses | Both 401 `invalid credentials` (API) and "Invalid username or password." (web) | Pass | raw output | — |
| SEC-02 | Login / TH-02 | Automated | Repeated failures are throttled | 20 wrong passwords, then the correct one | 429 or lockout after N failures | All 20 returned 401 at once; correct password then 200 | Fail | raw output | DEF-024 |
| SEC-03 | API auth / TH-04 | Automated | Every API endpoint needs login | 7 API calls without a cookie | 401 for all | 6 × 401; `GET /api/categories` 200 | Fail | raw output | DEF-023 |
| SEC-04 | Session / TH-04 | Automated | Cookie has protective flags | Inspect `Set-Cookie` from `/api/login` | `HttpOnly` and `SameSite` | `session=...; HttpOnly; Path=/`, no `SameSite` | Fail | raw output | DEF-025 |
| SEC-05 | Logout / TH-04 | Automated | Logout ends the session | Copy cookie, `GET /logout`, replay cookie on `/api/tasks` | 401 | 200 with the full task list | Fail | raw output | DEF-026 |
| SEC-06 | Registration / TH-03 | Automated | Common passwords refused | `POST /api/register` with password `password123` | 400 | 201 | Fail | raw output | DEF-027 |
| SEC-07a | API search / TH-06 | Automated | Quote in search does not crash | `GET /api/tasks?q=O'Brien` | 200 | 500 | Fail | raw output | DEF-017 |
| SEC-07b | API search / TH-06 | Automated | Injection cannot read other users' tasks | B owns `B_secret_...`; A searches `%' OR user_id != 0 OR title LIKE '` | Only A's tasks | B's task and every other user's returned to A | Fail | [leak](evidences/security/SEC-07b_01_sqli_leak_other_users_tasks.png), [crash](evidences/security/SEC-07b_02_sqli_crash_on_other_users_row.png) | DEF-029 |
| SEC-08 | Login / TH-07 | Automated | Injection in login does not bypass auth | Username `sec_user_a' --`, any password | 401 | 401 | Pass | raw output | — |
| SEC-09a | Web forms / TH-08 | Automated | Forms carry a CSRF token | Parse POST forms on `/` and `/login` | Token in each form | 0 of 5 forms have one | Fail | raw output | DEF-030 |
| SEC-09b | Web forms / TH-08 | Automated | Cross-site POST refused | POST `/tasks/<id>/delete` with `Origin: http://evil.example` | Refused | Task deleted | Fail | raw output | DEF-030 |
| SEC-10 | Task create / TH-09 | Automated | Owner cannot be set by the client | As A, `POST /api/tasks` with `"user_id": <B>` | Task belongs to A | Task created for A only | Pass | raw output | — |
| SEC-11 | Logging / TH-10 | Manual | Security events are logged | 1. Log in. 2. Fail a login. 3. Delete a task. 4. Read the server console | Event, user and time recorded | Only request lines such as `"POST /api/login HTTP/1.1" 200`; no username, no failed-login record | Fail | Manual observation | DEF-035 |
| SEC-12 | Task list / TH-11 | Automated | Titles are escaped | Title `<img src=x onerror="alert('...')">`, load `/` | Escaped text | Raw tag in HTML; script runs in the browser | Fail | [alert](evidences/security/SEC-12_stored_xss_alert.png) | DEF-005 |
| SEC-13 | Error handling / TH-12 | Automated | Errors show no internals | `GET /api/tasks?q='` | Generic 500 | Debugger page with traceback, SQL error, file paths | Fail | [console](evidences/security/SEC-13_01_debug_mode_on_app_window.png), [traceback](evidences/security/SEC-13_02_debugger_traceback_top.png), [debugger](evidences/security/SEC-13_03_debugger_console_offer.png) | DEF-031 |
| SEC-14 | Headers / TH-15 | Automated | Security headers present | Read headers on `/` | `X-Content-Type-Options`, `X-Frame-Options`, CSP | None present | Fail | raw output | DEF-032 |
| SEC-15 | API read / TH-13 | Automated | Another user's task cannot be read | B `GET /api/tasks/<A's id>` | 404 | 404 | Pass | raw output | — |
| SEC-16 | Task create / TH-17 | Automated | Oversized titles refused | 100,000-character title | 400/413/422 | 201, stored and rendered | Fail | raw output | DEF-033 |
| SEC-17 | Task list / TH-18 | Automated | Page size is capped | `per_page=1000000`, `per_page=-1` | Capped or 400 | Both 200; `-1` returns all tasks | Fail | raw output | DEF-034 |
| SEC-18 | API delete / TH-21 | Automated | Another user's task cannot be deleted | B `DELETE /api/tasks/<A's id>` | 403/404, task kept | 200 `{"result":"ok"}`; task gone | Fail | raw output | DEF-014 |
| SEC-19 | API update / TH-22 | Automated | Another user's task cannot be edited | B `PUT /api/tasks/<A's id>` with title "hacked" | Unchanged | 404; unchanged | Pass | raw output | — |
| SEC-20 | Session / TH-05 | Automated | Session cannot be forged | Sign `{"user_id": A}` with the key from `app.py`; call `/api/tasks` | 401 | 200 with A's private task | Fail | [forged cookie](evidences/security/SEC-20_forged_cookie_DEF-028.png) | DEF-028 |
| SEC-21 | Password storage / TH-14 | Automated | Passwords are hashed | Read `users.password_hash` from the database | Hashes only | `scrypt:32768:8:1$...` for all users | Pass | raw output | — |
| SEC-22 | Dependencies / TH-16 | Tool (pip-audit) | No known vulnerable packages | `pip-audit -r requirements.txt` | No known CVEs | Flask 3.0.3: CVE-2026-27205 (fixed in 3.1.3) | Fail | [screenshot](evidences/security/SEC-22_pip_audit.png), [output](evidences/security/pip_audit.txt) | DEF-036 |
| SEC-23 | Source / all | Tool (bandit) | No High static-analysis issues | `bandit -r` on the app source | No High issues | 1 High (B201 `debug=True`), 1 Low (B105 hard-coded key) | Fail | [issues](evidences/security/SEC-23_bandit_issues.png), [metrics](evidences/security/SEC-23_bandit_metrics.png), [output](evidences/security/bandit.txt) | DEF-031, DEF-028 |
| SEC-24 | Task create / TH-19 | Automated (re-test) | One bad date does not lock the user out | New user creates a task with `due_date: "31/12/2026"`, then `GET /api/dashboard` | 400, then 200 | Create 500 (task saved anyway); dashboard 500 | Fail | raw output | DEF-015 |

**Summary:** 24 cases, 6 Pass, 18 Fail. Screenshots of the evidence and regression runs: [test list](evidences/security/SEC_01_pytest_raw_test_list.png), [17 failed / 6 passed](evidences/security/SEC_02_pytest_raw_summary_17failed_6passed.png), [6 passed / 17 xfailed](evidences/security/SEC_03_pytest_regression_6passed_17xfailed.png). "raw output" = [security_run_raw.txt](evidences/security/security_run_raw.txt).

## Performance cases (PERF)

Executed 2026-11-27 with Apache JMeter 5.6.3 on a MacBook Air M4 (environment: W5_Report section 5.4). Common preconditions: fresh database; unchanged app on port 5015 started by `jmeter/run_perf_server.py`; setUp Thread Group seeds 20 users × 50 tasks (PERF-07: one user with N tasks). Targets set before the run: median < 200 ms, p95 < 1,000 ms, errors < 1%. Evidence folder: [evidences/performance/20261127-mac/](evidences/performance/20261127-mac/) (`<ID>.jtl.gz` raw results, `<ID>_server.log.gz`, `perf_summary.md`).

| Test Case ID | Objective | Workload / steps | Expected result | Actual result | Status | Evidence | Defect ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PERF-01 | Baseline, 1 user | `pytodo_load.jmx`, 1 user, 1-3 s think time, 120 s measured | Targets met | Median 5 ms, p95 9 ms, 0 errors | Pass | `PERF-01.jtl.gz` | — |
| PERF-02 | 5 users | As PERF-01 with 5 users | Targets met | Median 5 ms, p95 9 ms, 0 errors | Pass | `PERF-02.jtl.gz` | — |
| PERF-03 | 10 users | As PERF-01 with 10 users | Targets met | Median 5 ms, p95 8 ms, 0 errors | Pass | `PERF-03.jtl.gz` | — |
| PERF-04 | 25 users (expected small-team load) | As PERF-01 with 25 users | Targets met | Median 4 ms, p95 8 ms, 14.8 req/s, 0 errors | Pass | `PERF-04.jtl.gz` | — |
| PERF-05 | 50 users | As PERF-01 with 50 users | Targets met; observe degradation | Median 5 ms, p95 9 ms, 29.2 req/s, 0 errors; throughput in line with users | Pass | `PERF-05.jtl.gz`, [dashboard](evidences/performance/20261127-mac/PERF-05_dashboard/index.html) | — |
| PERF-06 | Find saturation and breakpoint | `pytodo_load.jmx`, no think time; 1, 5, 10, 25, 50, 100, 200 users; 10 s measured per step | Identify where throughput stops rising and p95 passes 1,000 ms | Throughput saturates at about 790 req/s from 10 users; p95 656 ms at 100 users, 1,247 ms at 200 users; no server errors up to 200 users | Pass (breakpoint found) | `PERF-06_step_*.jtl.gz`, [200-user dashboard](evidences/performance/20261127-mac/PERF-06_step_200u_dashboard/index.html), [chart](evidences/performance/20261127-mac/perf_stress_chart.png) | — |
| PERF-06b | Sustained stress | 50 users, no think time, 90 s | Errors < 1% over 90 s | 0 errors for 22 s (686 req/s, p95 303 ms); then client port exhaustion (`BindException`), 65.4% errors; 0 server errors | Blocked (test machine limit) | `PERF-06b.jtl.gz`, [dashboard](evidences/performance/20261127-mac/PERF-06b_dashboard/index.html) | — |
| PERF-07 | Data volume 50 -> 2,000 tasks | `pytodo_data_volume.jmx`, 1 user with 50, 500, 2,000 tasks; 30 sequential requests per endpoint | Response time roughly constant | Home page 2 -> 12 -> 40 ms (20×); dashboard 1 -> 3 -> 10 ms; paged API flat at 1 ms | Fail | `PERF-07_*tasks.jtl.gz`, [chart](evidences/performance/20261127-mac/perf_volume_chart.png) | DEF-037 |
