# 05_Security_Performance: Week 5 security and performance tests

All scripts are already set up for **PyTodo Pro (pytodo_pro_student)**: routes, JSON fields, and the 9+ character password rule. Results from our run on 25 Nov 2026 are in `results/` and written up in `Week5_Security_Performance_Report.md`.

Run everything on your own machine against a local copy only.

## 0. Setup (once)

```bash
pip install -r ../pytodo_pro_student/requirements.txt     # the app itself
pip install pytest requests locust matplotlib bandit pip-audit
```

## 1. Start a fresh copy of PyTodo Pro

```bash
cd pytodo_pro_student
# delete or rename pytodo_pro.db so you start clean
python app.py
```
Leave this terminal open. The app runs on http://127.0.0.1:5000.

## 2. Security tests (about 5 s)

Open a second terminal:

```bash
cd 05_Security_Performance
# macOS/Linux:
export PYTODO_DB=../pytodo_pro_student/pytodo_pro.db
# Windows PowerShell:  $env:PYTODO_DB="..\pytodo_pro_student\pytodo_pro.db"

pytest test_security.py -v -rA --raw        # evidence run: every finding shows as FAILED
pytest test_security.py -v -rA              # regression run: findings show as XFAIL with DEF-ID
```

Expected today: `--raw` → **17 failed, 6 passed**; normal → **6 passed, 17 xfailed**.
An **XPASS(strict)** in the normal run means a defect was fixed, so retest and close it.

Tool scans:

```bash
bandit -r ../pytodo_pro_student
pip-audit -r ../pytodo_pro_student/requirements.txt
```

Manual check SEC-11: watch the `python app.py` terminal while you log in, fail a login and delete a task. You'll see URLs and status codes, but never the username.

### Good live-demo moments
- **SEC-07b (SQL injection):** in Postman, log in as user A and send
  `GET http://127.0.0.1:5000/api/tasks?q=%' OR user_id != 0 OR title LIKE '&per_page=100`. Every user's tasks come back.
- **SEC-12 (stored XSS):** create a task titled `<img src=x onerror="alert('XSS')">` in the browser. The alert pops up on the task list.
- **SEC-13 (debug mode):** open `http://127.0.0.1:5000/api/tasks?q='` while logged in. The Werkzeug debugger page appears.

## 3. Performance test (about 12 min)

1. Close other heavy apps and note your machine's CPU, RAM and OS (report section 7.4).
2. Seed the data (once): `python seed_data.py`
3. Smoke test (30 s, should show 0 failures):
   `locust -f locustfile.py --headless -u 2 -r 1 -t 30s`
4. Full run:
   ```bash
   bash run_load_steps.sh        # macOS / Linux / Git Bash
   .\run_load_steps.ps1          # Windows PowerShell
   ```
5. Stress run (PERF-06, 90 s, no think time):
   ```bash
   STRESS=1 locust -f locustfile.py --headless -u 50 -r 10 -t 90s --csv results/stress_50u --html results/stress_50u.html --only-summary
   # PowerShell: $env:STRESS="1"; locust ... ; Remove-Item Env:STRESS
   ```
6. Data-volume test (PERF-07, about 1 min): `python perf_scaling.py`
7. Charts: `python make_charts.py` builds `results/perf_chart.png` (3 panels: normal load, stress, data volume).

Outputs in `results/`: `perf_summary.md`, `perf_scaling.md`, `stress_50u_stats.csv`, `perf_chart.png`, and the Locust HTML reports `step_<N>u.html` / `stress_50u.html` (good for screenshots).

For a live demo, run `locust -f locustfile.py` and open http://localhost:8089 to show the live charts.

## Files

| File | Purpose |
|---|---|
| `config.py` | URLs, accounts, settings (only change `BASE_URL` if needed) |
| `client.py` | Login/create helpers |
| `test_security.py` | 23 automated security tests (SEC-01 … SEC-24) |
| `conftest.py` | Maps confirmed findings to defect IDs (strict xfail); `--raw` switch |
| `seed_data.py` | 20 users × 50 tasks for load testing |
| `locustfile.py` | Load-test workload |
| `run_load_steps.sh` / `.ps1` | 1/5/10/25/50 users × 2 min |
| `summarise_results.py` | Locust step CSVs → `perf_summary.md` table |
| `perf_scaling.py` | PERF-07 data-volume test |
| `make_charts.py` | Builds the 3-panel `perf_chart.png` |
| `Week5_Security_Performance_Report.md` | STRIDE, test cases, defects, performance results, recommendations |
| `results/` | Evidence from the 25 Nov run |
