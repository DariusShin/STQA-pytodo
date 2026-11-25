"""
Week 5 - Controlled performance test for PyTodo Pro (Locust).

Workload model: each virtual user = one logged-in PyTodo user who mostly reads
(list, dashboard, search, home page) and sometimes writes (create + complete + delete).
Mix per user (weights): list 4, dashboard 3, home page 2, search 2, create/update/delete cycle 1.
Think time: 1-3 s between actions.

Do not run this yourself step by step; use run_load_steps.sh (or .ps1), which runs
1, 5, 10, 25 and 50 users for 2 minutes each and saves CSVs into results/.
"""
import os
import random
from locust import HttpUser, task, between, constant

import config as C


class PyTodoUser(HttpUser):
    host = C.BASE_URL
    # STRESS=1 removes think time (each user fires requests back-to-back) for PERF-06
    wait_time = constant(0) if os.environ.get("STRESS") == "1" else between(1, 3)

    def on_start(self):
        n = random.randrange(C.PERF_USERS)
        name = f"{C.PERF_USER_PREFIX}{n:02d}"
        self.client.post(C.API_LOGIN, json={"username": name, "password": C.PASSWORD},
                         name="POST /api/login")

    @task(4)
    def list_tasks(self):
        self.client.get(C.API_TASKS, name="GET /api/tasks")

    @task(3)
    def dashboard(self):
        self.client.get(C.API_DASHBOARD, name="GET /api/dashboard")

    @task(2)
    def home_page(self):
        self.client.get(C.HOME_URL, name="GET / (HTML)")

    @task(2)
    def search(self):
        term = random.choice(["report", "meeting", "task", "zzz"])
        self.client.get(C.API_TASKS, params={C.SEARCH_PARAM: term}, name="GET /api/tasks?q=")

    @task(1)
    def write_cycle(self):
        r = self.client.post(C.API_TASKS, name="POST /api/tasks",
                             json={"title": "load test task", "category_id": C.VALID_CATEGORY_ID,
                                   "due_date": C.VALID_DUE_DATE})
        if r.status_code not in (200, 201):
            return
        tid = r.json()["id"]
        path = C.API_TASK.format(id=tid)
        self.client.put(path, json={"done": True}, name="PUT /api/tasks/[id]")
        self.client.delete(path, name="DELETE /api/tasks/[id]")
