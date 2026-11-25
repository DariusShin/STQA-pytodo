| Tasks per user | Endpoint | Median (ms) | p95 (ms) |
|---|---|---|---|
| 50 | GET /api/dashboard | 3 | 3 |
| 50 | GET / (HTML) | 8 | 8 |
| 50 | GET /api/tasks (10/page) | 3 | 5 |
| 500 | GET /api/dashboard | 9 | 10 |
| 500 | GET / (HTML) | 54 | 80 |
| 500 | GET /api/tasks (10/page) | 3 | 4 |
| 2000 | GET /api/dashboard | 29 | 34 |
| 2000 | GET / (HTML) | 210 | 261 |
| 2000 | GET /api/tasks (10/page) | 3 | 4 |
