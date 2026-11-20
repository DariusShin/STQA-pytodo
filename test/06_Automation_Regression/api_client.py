"""Minimal JSON API client used only for test setup and independent checks.

Seeding data through the API keeps each UI test focused on the behaviour it
verifies (for example, a filter test does not also re-test task creation), and
counting tasks through the API gives an oracle that is independent of the page
under test. Standard library only.
"""

import http.cookiejar
import json
import logging
import urllib.error
import urllib.request

log = logging.getLogger("w6.api")


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self._opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
        )

    def call(self, method, path, payload=None):
        body = None if payload is None else json.dumps(payload).encode()
        req = urllib.request.Request(
            self.base_url + path, data=body, method=method,
            headers={"Content-Type": "application/json"},
        )
        try:
            with self._opener.open(req, timeout=10) as resp:
                status, raw = resp.status, resp.read()
        except urllib.error.HTTPError as err:
            status, raw = err.code, err.read()
        log.info("API %s %s -> %s", method, path, status)
        return status, (json.loads(raw) if raw else None)

    # -- convenience wrappers -------------------------------------------------

    def register(self, username, password):
        status, body = self.call("POST", "/api/register", {"username": username, "password": password})
        assert status == 201, f"setup: could not register {username!r}: {status} {body}"
        return body

    def login(self, username, password):
        status, body = self.call("POST", "/api/login", {"username": username, "password": password})
        assert status == 200, f"setup: could not log in {username!r}: {status} {body}"
        return body

    def categories(self):
        status, body = self.call("GET", "/api/categories")
        assert status == 200
        return {c["name"]: c["id"] for c in body}

    def create_task(self, title, description="", category=None, due_date=None, done=False):
        category_id = self.categories()[category] if category else None
        status, task = self.call("POST", "/api/tasks", {
            "title": title, "description": description,
            "category_id": category_id, "due_date": due_date,
        })
        assert status == 201, f"setup: could not create task {title!r}: {status} {task}"
        if done:
            status, task = self.call("PUT", f"/api/tasks/{task['id']}", {"done": True})
            assert status == 200
        return task

    def tasks(self):
        status, body = self.call("GET", "/api/tasks?per_page=1000")
        assert status == 200
        return body
