"""
Create the accounts and tasks the load test uses, so every run starts from the same data.
Run once before the performance test:   python seed_data.py
"""
import config as C
from client import logged_in_session, create_task, list_tasks

for i in range(C.PERF_USERS):
    name = f"{C.PERF_USER_PREFIX}{i:02d}"
    s = logged_in_session(name)
    have = len(list_tasks(s, per_page=1000))
    for n in range(have, C.TASKS_PER_PERF_USER):
        create_task(s, title=f"Perf task {n:03d} report meeting")
    print(f"{name}: ready ({C.TASKS_PER_PERF_USER} tasks)")
print("Seeding done.")
