"""Minimal HTTP client for the JSON API and the web form routes.

Used in two ways:
  * test setup and independent checks for the browser tests (seeding data
    through the API keeps each UI test focused on the behaviour it verifies,
    and counting tasks through the API gives an oracle that is independent of
    the page under test);
  * the Week 4 Web/API checks (test_06_api.py, test_07_web_forms.py), which
    send requests directly, without a browser.

Redirects are never followed, so a web form's 302 and its Location can be
asserted. A response body is parsed as JSON only when the server says it is
JSON, so a 500 HTML error page is reported as a failed check (AssertionError)
rather than a JSON decoding error. Standard library only.
"""

import http.cookiejar
import json
import logging
import urllib.error
import urllib.parse
import urllib.request

log = logging.getLogger("w6.api")


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # urllib then raises HTTPError, which call() turns into a Response


class Response:
    def __init__(self, status, headers, raw):
        self.status = status
        self.headers = headers
        self.text = raw.decode("utf-8", errors="replace")
        self.content_type = (headers.get("Content-Type") or "").split(";")[0].strip()

    @property
    def is_json(self):
        return self.content_type == "application/json"

    @property
    def json(self):
        return json.loads(self.text) if self.is_json and self.text else None

    @property
    def body(self):
        """JSON value for a JSON response, otherwise the text (or None if empty)."""
        return self.json if self.is_json else (self.text or None)

    @property
    def location(self):
        """Path of the redirect target, e.g. '/login', or None."""
        loc = self.headers.get("Location")
        return urllib.parse.urlsplit(loc).path if loc else None

    def __repr__(self):
        snippet = self.text[:120].replace("\n", " ")
        return f"<{self.status} {self.content_type or '-'} {snippet!r}>"


class ApiClient:
    """One client = one cookie jar = one user session (or none)."""

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self._opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()), _NoRedirect()
        )

    def request(self, method, path, json_body=None, form=None, params=None):
        url = self.base_url + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        headers, body = {}, None
        if form is not None:
            body = urllib.parse.urlencode(form).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        elif json_body is not None:
            body = json.dumps(json_body).encode()
            headers["Content-Type"] = "application/json"
        elif method in ("POST", "PUT", "PATCH"):
            body = b""
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=body, method=method, headers=headers)
        try:
            with self._opener.open(req, timeout=10) as resp:
                result = Response(resp.status, resp.headers, resp.read())
        except urllib.error.HTTPError as err:
            result = Response(err.code, err.headers, err.read())
        shown = path + ("?" + urllib.parse.urlencode(params) if params else "")
        log.info("%s %s %s -> %s%s", "WEB" if form is not None else "API", method, shown, result.status,
                 f" (Location {result.location})" if result.location else "")
        return result

    def call(self, method, path, payload=None):
        """JSON request; returns (status, parsed body)."""
        resp = self.request(method, path, json_body=payload)
        return resp.status, resp.body

    # -- web form routes ------------------------------------------------------

    def web_get(self, path, params=None):
        return self.request("GET", path, params=params)

    def web_post(self, path, form=None):
        return self.request("POST", path, form=form or {})

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
        assert status == 200, f"could not list tasks: {status} {str(body)[:200]}"
        return body
