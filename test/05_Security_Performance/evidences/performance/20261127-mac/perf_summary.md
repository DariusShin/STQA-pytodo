# Week 5 performance results (JMeter)

Run: 2026-11-27T15:40:18+08:00 on Apple M4, Darwin 26.5.2 (arm64). Measured window excludes ramp-up.

## Overall, per test

| Test | Users | Think time | Requests | Req/s | Successful req/s | Median (ms) | p95 (ms) | p99 (ms) | Max (ms) | Errors |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PERF-01 | 1 | 1-3 s | 65 | 0.5 | 0.5 | 5 | 9 | 23 | 23 | 0 (0.0%) |
| PERF-02 | 5 | 1-3 s | 340 | 2.8 | 2.8 | 5 | 9 | 12 | 23 | 0 (0.0%) |
| PERF-03 | 10 | 1-3 s | 705 | 5.9 | 5.9 | 5 | 8 | 11 | 51 | 0 (0.0%) |
| PERF-04 | 25 | 1-3 s | 1770 | 14.8 | 14.8 | 4 | 8 | 11 | 34 | 0 (0.0%) |
| PERF-05 | 50 | 1-3 s | 3500 | 29.2 | 29.2 | 5 | 9 | 13 | 31 | 0 (0.0%) |
| PERF-06b | 50 | none | 128474 | 1427.5 | 494.0 | 9 | 166 | 388 | 37901 | 84011 (65.39%) |
| PERF-06_step_001u | 1 | none | 16658 | 1665.8 | 967.3 | 1 | 1 | 2 | 16 | 6985 (41.93%) |
| PERF-06_step_005u | 5 | none | 12382 | 1238.2 | 990.0 | 2 | 14 | 24 | 165 | 2482 (20.05%) |
| PERF-06_step_010u | 10 | none | 7923 | 792.3 | 792.3 | 7 | 47 | 72 | 202 | 0 (0.0%) |
| PERF-06_step_025u | 25 | none | 7144 | 714.4 | 714.4 | 17 | 139 | 218 | 367 | 0 (0.0%) |
| PERF-06_step_050u | 50 | none | 6818 | 681.8 | 681.8 | 31 | 305 | 457 | 815 | 0 (0.0%) |
| PERF-06_step_100u | 100 | none | 6100 | 610.0 | 610.0 | 71 | 656 | 1007 | 1984 | 0 (0.0%) |
| PERF-06_step_200u | 200 | none | 6550 | 655.0 | 655.0 | 123 | 1247 | 1902 | 3168 | 0 (0.0%) |

## Per endpoint

| Test | Endpoint | Requests | Req/s | Median (ms) | p95 (ms) | p99 (ms) | Max (ms) | Errors |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| PERF-01 | DELETE /api/tasks/[id] | 4 | 0.0 | 4 | 7 | 7 | 7 | 0 (0.0%) |
| PERF-01 | GET / (HTML) | 9 | 0.1 | 9 | 23 | 23 | 23 | 0 (0.0%) |
| PERF-01 | GET /api/dashboard | 21 | 0.2 | 5 | 7 | 8 | 8 | 0 (0.0%) |
| PERF-01 | GET /api/tasks | 12 | 0.1 | 5 | 7 | 7 | 7 | 0 (0.0%) |
| PERF-01 | GET /api/tasks?q= | 11 | 0.1 | 4 | 7 | 7 | 7 | 0 (0.0%) |
| PERF-01 | POST /api/tasks | 4 | 0.0 | 7 | 8 | 8 | 8 | 0 (0.0%) |
| PERF-01 | PUT /api/tasks/[id] | 4 | 0.0 | 4 | 8 | 8 | 8 | 0 (0.0%) |
| PERF-01 | ALL | 65 | 0.5 | 5 | 9 | 23 | 23 | 0 (0.0%) |
| PERF-02 | DELETE /api/tasks/[id] | 24 | 0.2 | 4 | 7 | 9 | 9 | 0 (0.0%) |
| PERF-02 | GET / (HTML) | 54 | 0.5 | 8 | 11 | 23 | 23 | 0 (0.0%) |
| PERF-02 | GET /api/dashboard | 73 | 0.6 | 5 | 7 | 13 | 13 | 0 (0.0%) |
| PERF-02 | GET /api/tasks | 100 | 0.8 | 5 | 6 | 7 | 7 | 0 (0.0%) |
| PERF-02 | GET /api/tasks?q= | 41 | 0.3 | 5 | 7 | 13 | 13 | 0 (0.0%) |
| PERF-02 | POST /api/tasks | 24 | 0.2 | 6 | 8 | 9 | 9 | 0 (0.0%) |
| PERF-02 | PUT /api/tasks/[id] | 24 | 0.2 | 5 | 8 | 9 | 9 | 0 (0.0%) |
| PERF-02 | ALL | 340 | 2.8 | 5 | 9 | 12 | 23 | 0 (0.0%) |
| PERF-03 | DELETE /api/tasks/[id] | 53 | 0.4 | 4 | 5 | 8 | 8 | 0 (0.0%) |
| PERF-03 | GET / (HTML) | 102 | 0.8 | 8 | 10 | 21 | 27 | 0 (0.0%) |
| PERF-03 | GET /api/dashboard | 141 | 1.2 | 5 | 7 | 22 | 29 | 0 (0.0%) |
| PERF-03 | GET /api/tasks | 214 | 1.8 | 4 | 6 | 8 | 10 | 0 (0.0%) |
| PERF-03 | GET /api/tasks?q= | 89 | 0.7 | 4 | 6 | 51 | 51 | 0 (0.0%) |
| PERF-03 | POST /api/tasks | 53 | 0.4 | 5 | 7 | 12 | 12 | 0 (0.0%) |
| PERF-03 | PUT /api/tasks/[id] | 53 | 0.4 | 4 | 6 | 7 | 7 | 0 (0.0%) |
| PERF-03 | ALL | 705 | 5.9 | 5 | 8 | 11 | 51 | 0 (0.0%) |
| PERF-04 | DELETE /api/tasks/[id] | 135 | 1.1 | 4 | 6 | 10 | 11 | 0 (0.0%) |
| PERF-04 | GET / (HTML) | 252 | 2.1 | 7 | 10 | 16 | 18 | 0 (0.0%) |
| PERF-04 | GET /api/dashboard | 363 | 3.0 | 4 | 7 | 13 | 34 | 0 (0.0%) |
| PERF-04 | GET /api/tasks | 502 | 4.2 | 4 | 6 | 8 | 13 | 0 (0.0%) |
| PERF-04 | GET /api/tasks?q= | 248 | 2.1 | 4 | 6 | 9 | 22 | 0 (0.0%) |
| PERF-04 | POST /api/tasks | 135 | 1.1 | 5 | 8 | 9 | 25 | 0 (0.0%) |
| PERF-04 | PUT /api/tasks/[id] | 135 | 1.1 | 4 | 7 | 7 | 10 | 0 (0.0%) |
| PERF-04 | ALL | 1770 | 14.8 | 4 | 8 | 11 | 34 | 0 (0.0%) |
| PERF-05 | DELETE /api/tasks/[id] | 260 | 2.2 | 4 | 5 | 7 | 16 | 0 (0.0%) |
| PERF-05 | GET / (HTML) | 502 | 4.2 | 8 | 12 | 16 | 31 | 0 (0.0%) |
| PERF-05 | GET /api/dashboard | 746 | 6.2 | 5 | 6 | 8 | 16 | 0 (0.0%) |
| PERF-05 | GET /api/tasks | 1009 | 8.4 | 4 | 6 | 9 | 17 | 0 (0.0%) |
| PERF-05 | GET /api/tasks?q= | 463 | 3.9 | 4 | 6 | 8 | 10 | 0 (0.0%) |
| PERF-05 | POST /api/tasks | 260 | 2.2 | 5 | 7 | 15 | 20 | 0 (0.0%) |
| PERF-05 | PUT /api/tasks/[id] | 260 | 2.2 | 4 | 7 | 9 | 15 | 0 (0.0%) |
| PERF-05 | ALL | 3500 | 29.2 | 5 | 9 | 13 | 31 | 0 (0.0%) |
| PERF-06b | DELETE /api/tasks/[id] | 3231 | 35.9 | 3 | 41 | 114 | 1408 | 10 (0.31%) |
| PERF-06b | GET / (HTML) | 20126 | 223.6 | 10 | 391 | 660 | 37901 | 13743 (68.28%) |
| PERF-06b | GET /api/dashboard | 30673 | 340.8 | 8 | 51 | 110 | 4704 | 21128 (68.88%) |
| PERF-06b | GET /api/tasks | 40519 | 450.2 | 9 | 125 | 230 | 6142 | 27998 (69.1%) |
| PERF-06b | GET /api/tasks?q= | 20557 | 228.4 | 9 | 110 | 206 | 4842 | 14217 (69.16%) |
| PERF-06b | POST /api/tasks | 10139 | 112.7 | 8 | 51 | 130 | 4708 | 6909 (68.14%) |
| PERF-06b | PUT /api/tasks/[id] | 3229 | 35.9 | 6 | 67 | 159 | 689 | 6 (0.19%) |
| PERF-06b | ALL | 128474 | 1427.5 | 9 | 166 | 388 | 37901 | 84011 (65.39%) |
| PERF-06_step_001u | DELETE /api/tasks/[id] | 679 | 67.9 | 1 | 1 | 1 | 1 | 0 (0.0%) |
| PERF-06_step_001u | GET / (HTML) | 2630 | 263.0 | 1 | 2 | 2 | 16 | 1192 (45.32%) |
| PERF-06_step_001u | GET /api/dashboard | 3763 | 376.3 | 1 | 1 | 1 | 9 | 1741 (46.27%) |
| PERF-06_step_001u | GET /api/tasks | 5034 | 503.4 | 0 | 1 | 1 | 9 | 2324 (46.17%) |
| PERF-06_step_001u | GET /api/tasks?q= | 2625 | 262.5 | 0 | 1 | 1 | 10 | 1159 (44.15%) |
| PERF-06_step_001u | POST /api/tasks | 1248 | 124.8 | 1 | 1 | 1 | 1 | 569 (45.59%) |
| PERF-06_step_001u | PUT /api/tasks/[id] | 679 | 67.9 | 1 | 1 | 1 | 2 | 0 (0.0%) |
| PERF-06_step_001u | ALL | 16658 | 1665.8 | 1 | 1 | 2 | 16 | 6985 (41.93%) |
| PERF-06_step_005u | DELETE /api/tasks/[id] | 673 | 67.3 | 1 | 3 | 7 | 12 | 0 (0.0%) |
| PERF-06_step_005u | GET / (HTML) | 1809 | 180.9 | 11 | 25 | 40 | 165 | 415 (22.94%) |
| PERF-06_step_005u | GET /api/dashboard | 2782 | 278.2 | 3 | 6 | 10 | 44 | 631 (22.68%) |
| PERF-06_step_005u | GET /api/tasks | 3649 | 364.9 | 2 | 9 | 16 | 44 | 842 (23.07%) |
| PERF-06_step_005u | GET /api/tasks?q= | 1930 | 193.0 | 2 | 8 | 14 | 52 | 401 (20.78%) |
| PERF-06_step_005u | POST /api/tasks | 866 | 86.6 | 2 | 5 | 12 | 62 | 193 (22.29%) |
| PERF-06_step_005u | PUT /api/tasks/[id] | 673 | 67.3 | 1 | 4 | 8 | 25 | 0 (0.0%) |
| PERF-06_step_005u | ALL | 12382 | 1238.2 | 2 | 14 | 24 | 165 | 2482 (20.05%) |
| PERF-06_step_010u | DELETE /api/tasks/[id] | 547 | 54.7 | 1 | 4 | 13 | 26 | 0 (0.0%) |
| PERF-06_step_010u | GET / (HTML) | 1163 | 116.3 | 37 | 77 | 95 | 176 | 0 (0.0%) |
| PERF-06_step_010u | GET /api/dashboard | 1671 | 167.1 | 8 | 25 | 42 | 77 | 0 (0.0%) |
| PERF-06_step_010u | GET /api/tasks | 2290 | 229.0 | 9 | 27 | 46 | 102 | 0 (0.0%) |
| PERF-06_step_010u | GET /api/tasks?q= | 1159 | 115.9 | 6 | 22 | 38 | 202 | 0 (0.0%) |
| PERF-06_step_010u | POST /api/tasks | 546 | 54.6 | 4 | 15 | 27 | 91 | 0 (0.0%) |
| PERF-06_step_010u | PUT /api/tasks/[id] | 547 | 54.7 | 2 | 7 | 26 | 62 | 0 (0.0%) |
| PERF-06_step_010u | ALL | 7923 | 792.3 | 7 | 47 | 72 | 202 | 0 (0.0%) |
| PERF-06_step_025u | DELETE /api/tasks/[id] | 531 | 53.1 | 2 | 11 | 39 | 148 | 0 (0.0%) |
| PERF-06_step_025u | GET / (HTML) | 1041 | 104.1 | 111 | 227 | 278 | 367 | 0 (0.0%) |
| PERF-06_step_025u | GET /api/dashboard | 1546 | 154.6 | 12 | 64 | 87 | 238 | 0 (0.0%) |
| PERF-06_step_025u | GET /api/tasks | 1938 | 193.8 | 24 | 92 | 143 | 224 | 0 (0.0%) |
| PERF-06_step_025u | GET /api/tasks?q= | 1030 | 103.0 | 19 | 83 | 139 | 203 | 0 (0.0%) |
| PERF-06_step_025u | POST /api/tasks | 529 | 52.9 | 7 | 48 | 85 | 125 | 0 (0.0%) |
| PERF-06_step_025u | PUT /api/tasks/[id] | 529 | 52.9 | 3 | 17 | 46 | 102 | 0 (0.0%) |
| PERF-06_step_025u | ALL | 7144 | 714.4 | 17 | 139 | 218 | 367 | 0 (0.0%) |
| PERF-06_step_050u | DELETE /api/tasks/[id] | 478 | 47.8 | 3 | 32 | 97 | 360 | 0 (0.0%) |
| PERF-06_step_050u | GET / (HTML) | 945 | 94.5 | 246 | 473 | 610 | 815 | 0 (0.0%) |
| PERF-06_step_050u | GET /api/dashboard | 1475 | 147.5 | 16 | 98 | 160 | 583 | 0 (0.0%) |
| PERF-06_step_050u | GET /api/tasks | 1943 | 194.3 | 54 | 197 | 305 | 485 | 0 (0.0%) |
| PERF-06_step_050u | GET /api/tasks?q= | 1021 | 102.1 | 35 | 179 | 255 | 388 | 0 (0.0%) |
| PERF-06_step_050u | POST /api/tasks | 478 | 47.8 | 14 | 93 | 143 | 195 | 0 (0.0%) |
| PERF-06_step_050u | PUT /api/tasks/[id] | 478 | 47.8 | 5 | 68 | 134 | 157 | 0 (0.0%) |
| PERF-06_step_050u | ALL | 6818 | 681.8 | 31 | 305 | 457 | 815 | 0 (0.0%) |
| PERF-06_step_100u | DELETE /api/tasks/[id] | 413 | 41.3 | 13 | 186 | 704 | 1120 | 0 (0.0%) |
| PERF-06_step_100u | GET / (HTML) | 883 | 88.3 | 520 | 1019 | 1524 | 1984 | 0 (0.0%) |
| PERF-06_step_100u | GET /api/dashboard | 1394 | 139.4 | 20 | 127 | 357 | 1191 | 0 (0.0%) |
| PERF-06_step_100u | GET /api/tasks | 1756 | 175.6 | 115 | 367 | 667 | 1366 | 0 (0.0%) |
| PERF-06_step_100u | GET /api/tasks?q= | 826 | 82.6 | 87 | 319 | 547 | 1047 | 0 (0.0%) |
| PERF-06_step_100u | POST /api/tasks | 413 | 41.3 | 29 | 395 | 886 | 1110 | 0 (0.0%) |
| PERF-06_step_100u | PUT /api/tasks/[id] | 415 | 41.5 | 28 | 183 | 488 | 1584 | 0 (0.0%) |
| PERF-06_step_100u | ALL | 6100 | 610.0 | 71 | 656 | 1007 | 1984 | 0 (0.0%) |
| PERF-06_step_200u | DELETE /api/tasks/[id] | 477 | 47.7 | 17 | 790 | 2074 | 2335 | 0 (0.0%) |
| PERF-06_step_200u | GET / (HTML) | 967 | 96.7 | 955 | 1915 | 2549 | 3168 | 0 (0.0%) |
| PERF-06_step_200u | GET /api/dashboard | 1407 | 140.7 | 23 | 169 | 494 | 1418 | 0 (0.0%) |
| PERF-06_step_200u | GET /api/tasks | 1803 | 180.3 | 196 | 653 | 1048 | 2118 | 0 (0.0%) |
| PERF-06_step_200u | GET /api/tasks?q= | 933 | 93.3 | 151 | 556 | 1055 | 2034 | 0 (0.0%) |
| PERF-06_step_200u | POST /api/tasks | 485 | 48.5 | 57 | 899 | 1538 | 1831 | 0 (0.0%) |
| PERF-06_step_200u | PUT /api/tasks/[id] | 478 | 47.8 | 46 | 896 | 1938 | 2449 | 0 (0.0%) |
| PERF-06_step_200u | ALL | 6550 | 655.0 | 123 | 1247 | 1902 | 3168 | 0 (0.0%) |

## PERF-07 data volume (1 user, 30 sequential requests each)

| Tasks per user | Endpoint | Median (ms) | p95 (ms) | Errors |
|---:|---|---:|---:|---:|
| 50 | GET /api/dashboard | 1 | 1 | 0 |
| 50 | GET / (HTML) | 2 | 4 | 0 |
| 50 | GET /api/tasks (10 per page) | 1 | 1 | 0 |
| 500 | GET /api/dashboard | 3 | 4 | 0 |
| 500 | GET / (HTML) | 12 | 16 | 0 |
| 500 | GET /api/tasks (10 per page) | 1 | 10 | 0 |
| 2000 | GET /api/dashboard | 10 | 12 | 0 |
| 2000 | GET / (HTML) | 40 | 53 | 0 |
| 2000 | GET /api/tasks (10 per page) | 1 | 1 | 0 |

### PERF-06b errors

| Count | Sample: code and message |
|---:|---|
| 27998 | GET /api/tasks: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 21128 | GET /api/dashboard: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 14217 | GET /api/tasks?q=: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 13743 | GET / (HTML): Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 6909 | POST /api/tasks: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 10 | DELETE /api/tasks/[id]: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 6 | PUT /api/tasks/[id]: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |

### PERF-06_step_001u errors

| Count | Sample: code and message |
|---:|---|
| 2324 | GET /api/tasks: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 1741 | GET /api/dashboard: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 1192 | GET / (HTML): Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 1159 | GET /api/tasks?q=: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 569 | POST /api/tasks: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |

### PERF-06_step_005u errors

| Count | Sample: code and message |
|---:|---|
| 842 | GET /api/tasks: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 631 | GET /api/dashboard: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 415 | GET / (HTML): Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 401 | GET /api/tasks?q=: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
| 193 | POST /api/tasks: Non HTTP response code: java.net.BindException Non HTTP response message: Can't assign requested address |
