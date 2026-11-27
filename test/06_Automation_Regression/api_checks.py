"""Shared data helpers and assertions for the Week 4 Web/API checks.

Expected results follow Week 4's test basis (test/04_Web_API/README.md, 0.3):
invalid input -> 400 with a JSON {"error": ...} body; missing or another
user's resource -> 404; not logged in -> 401; unsupported method -> 405; a 500
is never an acceptable answer to client input; a failed request changes
nothing.
"""

from html.parser import HTMLParser

from conftest import RUN_STARTED, _counter

DASHBOARD_LABELS = {
    "Total Tasks": "total",
    "Open": "open",
    "Overdue": "overdue",
    "Due Soon": "due_soon",
    "Completed (last 7 days)": "completed_this_week",
}

_B36 = "0123456789abcdefghijklmnopqrstuvwxyz"


def sized_username(n):
    """A valid username of exactly n characters (3-20) that is unique within the run.

    The 3-character form uses a base-36 counter, so it is unique within one run;
    the longer forms also include the run start time.
    """
    _counter["n"] += 1
    k = _counter["n"]
    tag = _B36[(k // 36) % 36] + _B36[k % 36]
    if n == 3:
        return "u" + tag
    return (f"u{tag}{RUN_STARTED:%H%M%S}" + "x" * 20)[:n]


# ---------------------------------------------------------------------------
# Assertions
# ---------------------------------------------------------------------------

def expect_json_error(resp, status, message=None):
    """Status, JSON body (not an HTML error page) and, optionally, the error text."""
    assert resp.status == status, f"expected {status} with a JSON error, got {resp!r}"
    assert resp.is_json, f"expected a JSON body, got Content-Type {resp.content_type!r}"
    if message is not None:
        body = resp.json
        assert isinstance(body, dict) and body.get("error") == message, \
            f"expected error {message!r}, got {body!r}"


def expect_redirect(resp, path):
    assert resp.status == 302 and resp.location == path, \
        f"expected a 302 redirect to {path}, got {resp.status} (Location {resp.location})"


def expect_not_accepted(resp, afterwards=""):
    """A web form submission the server should refuse: no redirect to the task list."""
    assert not (resp.status == 302 and resp.location == "/"), \
        f"server accepted the form: {resp.status} redirect to {resp.location}" + \
        (f"; {afterwards}" if afterwards else "")


def titles(tasks):
    return sorted(t["title"] for t in tasks)


# ---------------------------------------------------------------------------
# HTML readers for the web pages (standard library parser, no browser)
# ---------------------------------------------------------------------------

class _PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows, self.errors, self.stats = [], [], []
        self._in_tbody = False
        self._row = None
        self._cell = None
        self._capture = None  # ("error" | "stat-value" | "stat-label", buffer)

    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class") or ""
        if tag == "tbody":
            self._in_tbody = True
        elif tag == "tr" and self._in_tbody:
            self._row = []
        elif tag == "td" and self._row is not None:
            self._cell = []
        elif tag == "p" and "error" in cls.split():
            self._capture = ("error", [])
        elif tag == "div" and cls in ("stat-value", "stat-label"):
            self._capture = (cls, [])

    def handle_endtag(self, tag):
        if tag == "tbody":
            self._in_tbody = False
        elif tag == "td" and self._cell is not None:
            self._row.append(" ".join("".join(self._cell).split()))
            self._cell = None
        elif tag == "tr" and self._row is not None:
            if len(self._row) >= 5:  # skip the "No tasks match" placeholder row
                self.rows.append({"title": self._row[1], "category": self._row[2],
                                  "due_date": self._row[3], "urgency": self._row[4]})
            self._row = None
        elif self._capture and tag in ("p", "div"):
            kind, buf = self._capture
            text = " ".join("".join(buf).split())
            if kind == "error":
                self.errors.append(text)
            else:
                self.stats.append((kind, text))
            self._capture = None

    def handle_data(self, data):
        if self._cell is not None:
            self._cell.append(data)
        if self._capture:
            self._capture[1].append(data)


def _parse(html):
    parser = _PageParser()
    parser.feed(html)
    return parser


def page_task_rows(html):
    """Rows of the task table on '/': title, category, due_date, urgency (as displayed)."""
    return _parse(html).rows


def page_error(html):
    errors = _parse(html).errors
    return errors[0] if errors else None


def page_dashboard(html):
    """Dashboard counters keyed like the API dashboard (total, open, ...)."""
    stats = _parse(html).stats
    values = [int(t) for k, t in stats if k == "stat-value"]
    labels = [t for k, t in stats if k == "stat-label"]
    return {DASHBOARD_LABELS[label]: value for label, value in zip(labels, values)}
