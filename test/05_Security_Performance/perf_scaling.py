"""
PERF-07 data-volume test: how do the dashboard and home page scale with the number of tasks
a user has? Creates users with 50, 500 and 2000 tasks, then times 30 sequential requests
per endpoint (1 user, no concurrency). Output: results/perf_scaling.md
"""
import statistics
import time
import requests
import config as C
from client import logged_in_session, list_tasks, url

SIZES = [50, 500, 2000]
ENDPOINTS = [("GET /api/dashboard", C.API_DASHBOARD), ("GET / (HTML)", C.HOME_URL),
             ("GET /api/tasks (10/page)", C.API_TASKS)]
lines = ["| Tasks per user | Endpoint | Median (ms) | p95 (ms) |", "|---|---|---|---|"]
for n in SIZES:
    s = logged_in_session(f"scale_{n}")
    have = len(list_tasks(s, per_page=-1))
    for i in range(have, n):
        s.post(url(C.API_TASKS), json={"title": f"scale task {i}", "category_id": 1,
                                       "due_date": C.VALID_DUE_DATE})
    for label, path in ENDPOINTS:
        times = []
        for _ in range(30):
            t0 = time.perf_counter()
            assert s.get(url(path)).status_code == 200
            times.append((time.perf_counter() - t0) * 1000)
        times.sort()
        lines.append(f"| {n} | {label} | {statistics.median(times):.0f} | {times[int(0.95*len(times))-1]:.0f} |")
        print(lines[-1])
open("results/perf_scaling.md", "w").write("\n".join(lines) + "\n")
