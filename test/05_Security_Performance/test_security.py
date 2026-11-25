"""
Week 5 - Security tests for PyTodo Pro (safe, local only).

Each test asserts the SECURE behaviour, so a failing assertion is a security finding.
Confirmed findings are listed in conftest.py (KNOWN_DEFECTS) and reported as XFAIL with
their defect ID, which keeps the suite usable as a regression suite (an XPASS means fixed).

    pytest test_security.py -v -rA            # regression view (confirmed defects = XFAIL)
    pytest test_security.py -v -rA --raw      # raw view (every finding shows as FAILED)

Only run against your own local copy (127.0.0.1).
"""
import os
import re
import sqlite3
import uuid

import pytest
import requests

import config as C
from client import url, api_login, api_register, logged_in_session, create_task, list_tasks

assert "127.0.0.1" in C.BASE_URL or "localhost" in C.BASE_URL, \
    "Security tests must only run against a local copy of PyTodo Pro"


@pytest.fixture(scope="module")
def user_a():
    return logged_in_session(C.USER_A)


@pytest.fixture(scope="module")
def user_b():
    return logged_in_session(C.USER_B)


def unique(prefix="t"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def fresh_user():
    s = requests.Session()
    name = unique("u")[:20]
    r = api_register(s, name)
    s.user_id = r.json()["id"]
    return s, name


# ======================= S - SPOOFING =======================

def test_SEC_01_login_error_does_not_reveal_which_field_is_wrong(user_a):
    """Unknown username vs wrong password must give the same response (web and API)."""
    r1 = api_login(requests.Session(), unique("nobody"), "whatever1234")
    r2 = api_login(requests.Session(), C.USER_A, "wrong-password-1")
    assert (r1.status_code, r1.text) == (r2.status_code, r2.text)
    w1 = requests.post(url(C.LOGIN_URL), data={"username": unique("nobody"), "password": "x" * 9})
    w2 = requests.post(url(C.LOGIN_URL), data={"username": C.USER_A, "password": "x" * 9})
    assert "Invalid username or password" in w1.text and "Invalid username or password" in w2.text


def test_SEC_02_repeated_failed_logins_are_throttled():
    """After 20 wrong passwords the app should lock, delay, or return 429."""
    _, name = fresh_user()
    s = requests.Session()
    codes = [api_login(s, name, f"wrongpass{i}").status_code for i in range(20)]
    final = api_login(s, name, C.PASSWORD)
    assert 429 in codes or final.status_code in (423, 429), \
        f"20 failed logins in a row, no throttling; correct password then gave {final.status_code}"


def test_SEC_03_api_requires_login():
    """Every API endpoint except register/login should refuse an anonymous request (401)."""
    anon = requests.Session()
    checks = [("GET", C.API_TASKS), ("POST", C.API_TASKS), ("GET", C.API_DASHBOARD),
              ("GET", C.API_CATEGORIES), ("GET", C.API_TASK.format(id=1)),
              ("PUT", C.API_TASK.format(id=1)), ("DELETE", C.API_TASK.format(id=1))]
    open_ = [f"{m} {p} -> {r.status_code}"
             for m, p in checks
             if (r := anon.request(m, C.BASE_URL + p, json={"title": "x"})).status_code != 401]
    assert not open_, "Reachable without login: " + "; ".join(open_)


def test_SEC_04_session_cookie_flags(user_a):
    """Session cookie should be HttpOnly and have an explicit SameSite attribute."""
    r = api_login(requests.Session(), C.USER_A)
    header = r.headers.get("Set-Cookie", "").lower()
    assert "httponly" in header, f"Missing HttpOnly: {header}"
    assert "samesite" in header, f"Missing SameSite: {header}"


def test_SEC_05_old_session_cookie_rejected_after_logout():
    """Copy the cookie, log out, replay it. Secure: replay rejected."""
    s = logged_in_session(C.USER_A)
    stolen = s.cookies.get_dict()
    s.get(url(C.LOGOUT_URL))
    attacker = requests.Session()
    attacker.cookies.update(stolen)
    r = attacker.get(url(C.API_TASKS))
    assert r.status_code == 401, "Cookie copied before logout still works after logout"


def test_SEC_06_common_password_rejected():
    """A very common password (password123) should be refused."""
    r = api_register(requests.Session(), unique("weak")[:20], "password123")
    assert r.status_code == 400, f"Registered with 'password123' ({r.status_code})"


def test_SEC_20_session_cannot_be_forged_with_source_secret_key(user_a):
    """The SECRET_KEY is hard-coded in app.py. If it still works, anyone who has read the
    source can sign a session cookie for any user_id and log in as them without a password."""
    from flask import Flask
    from flask.sessions import SecureCookieSessionInterface
    secret = unique("A_private")
    create_task(user_a, title=secret)
    fake = Flask("forge")
    fake.secret_key = C.SECRET_KEY_IN_SOURCE
    signer = SecureCookieSessionInterface().get_signing_serializer(fake)
    cookie = signer.dumps({"user_id": user_a.user_id, "username": C.USER_A})
    attacker = requests.Session()
    attacker.cookies.set("session", cookie)
    r = attacker.get(url(C.API_TASKS), params={"per_page": 100})
    assert not (r.status_code == 200 and secret in r.text), \
        "Forged cookie signed with the key from app.py logged in as user A"


# ======================= T - TAMPERING =======================

def test_SEC_07a_search_with_quote_does_not_crash(user_a):
    """A single apostrophe in search must not break the SQL query (DEF-017)."""
    r = user_a.get(url(C.API_TASKS), params={C.SEARCH_PARAM: "O'Brien"})
    assert r.status_code == 200, f"Search with apostrophe returned {r.status_code}"


def test_SEC_07b_sql_injection_in_search_cannot_read_other_users(user_a, user_b):
    """Detection payload: widens the WHERE clause. Secure: only A's own tasks come back."""
    secret = unique("B_secret")
    create_task(user_b, title=secret)
    payload = "%' OR user_id != 0 OR title LIKE '"
    r = user_a.get(url(C.API_TASKS), params={C.SEARCH_PARAM: payload, "per_page": 100})
    assert r.status_code != 500
    assert secret not in r.text, "SQL injection in search returned user B's task to user A"


def test_SEC_08_sql_injection_in_login_does_not_bypass_auth():
    r = api_login(requests.Session(), f"{C.USER_A}' --", "anything")
    assert r.status_code == 401


def test_SEC_09a_forms_have_csrf_token(user_a):
    """Every state-changing (POST) form should carry a CSRF token."""
    create_task(user_a, title="csrf form check")
    html = user_a.get(url(C.HOME_URL)).text + requests.get(url(C.LOGIN_URL)).text
    forms = re.findall(r"<form[^>]*method=\"post\"[^>]*>.*?</form>", html, re.S | re.I)
    assert forms, "No POST forms found"
    missing = [f for f in forms if not re.search(r"csrf", f, re.I)]
    assert not missing, f"{len(missing)} of {len(forms)} POST forms have no CSRF token"


def test_SEC_09b_cross_site_post_is_refused(user_a):
    """Simulate a forged request from another site (Origin/Referer = evil site)."""
    tid = create_task(user_a, title=unique("csrf_victim"))
    user_a.post(url("/tasks/{id}/delete", id=tid),
                headers={"Origin": "http://evil.example", "Referer": "http://evil.example/x"},
                allow_redirects=False)
    still_there = user_a.get(url(C.API_TASK, id=tid)).status_code == 200
    assert still_there, "Task deleted by a request claiming to come from another site"


def test_SEC_10_mass_assignment_cannot_set_owner(user_a, user_b):
    """Sending user_id in the body must not create a task in someone else's account."""
    title = unique("mass")
    user_a.post(url(C.API_TASKS), json={"title": title, "user_id": user_b.user_id})
    assert title not in str(list_tasks(user_b, per_page=100))


# ======================= R - REPUDIATION =======================
# SEC-11 (no audit trail of logins / deletes) is a review check. See the report.


# ======================= I - INFORMATION DISCLOSURE =======================

def test_SEC_12_stored_xss_title_is_escaped(user_a):
    """A script payload in a title must be shown as text (lead: DEF-005)."""
    payload = f'<img src=x onerror="alert(\'{unique("xss")}\')">'
    create_task(user_a, title=payload)
    html = user_a.get(url(C.HOME_URL)).text
    assert payload not in html, "Raw <img onerror> rendered on the task list: stored XSS"


def test_SEC_13_errors_do_not_show_tracebacks(user_a):
    """Trigger a known 500 and check no stack trace / debugger is returned."""
    r = user_a.get(url(C.API_TASKS), params={C.SEARCH_PARAM: "'"})
    leaks = [k for k in ("Traceback", "Werkzeug Debugger", "sqlite3.OperationalError", "app.py")
             if k in r.text]
    assert not leaks, f"HTTP {r.status_code}; response exposes: {leaks}"


def test_SEC_14_security_headers_present(user_a):
    r = user_a.get(url(C.HOME_URL))
    missing = [h for h in ("X-Content-Type-Options", "X-Frame-Options", "Content-Security-Policy")
               if h not in r.headers]
    assert not missing, f"Missing headers: {missing}"


def test_SEC_15_another_users_task_cannot_be_read(user_a, user_b):
    tid = create_task(user_a, title=unique("private"))
    assert user_b.get(url(C.API_TASK, id=tid)).status_code == 404


def test_SEC_21_passwords_are_hashed():
    """Inspect the database directly (set PYTODO_DB to the .db path)."""
    path = os.environ.get("PYTODO_DB")
    if not path or not os.path.exists(path):
        pytest.skip("Set PYTODO_DB=<path to pytodo_pro.db> to run this check")
    rows = sqlite3.connect(path).execute("SELECT password_hash FROM users LIMIT 20").fetchall()
    assert rows and all(re.match(r"^(scrypt|pbkdf2):", h) for (h,) in rows)


# ======================= D - DENIAL OF SERVICE =======================

def test_SEC_16_huge_title_rejected(user_a):
    r = user_a.post(url(C.API_TASKS), json={"title": "A" * 100_000})
    if r.status_code == 201:
        user_a.delete(url(C.API_TASK, id=r.json()["id"]))
    assert r.status_code in (400, 413, 422), f"100 000-character title accepted ({r.status_code})"


def test_SEC_17_page_size_is_capped(user_a):
    for _ in range(3):
        create_task(user_a, title="page size filler")
    for value in (1_000_000, -1):
        r = user_a.get(url(C.API_TASKS), params={C.PER_PAGE_PARAM: value})
        assert r.status_code in (200, 400)
        if r.status_code == 200:
            assert len(r.json()) <= 100 and value != -1, \
                f"per_page={value} accepted, returned {len(r.json())} tasks (no cap)"


def test_SEC_24_one_bad_due_date_does_not_lock_user_out():
    """Retest DEF-015 with a throwaway user: invalid date should be refused, dashboard still works."""
    s, _ = fresh_user()
    r = s.post(url(C.API_TASKS), json={"title": "bad date", "due_date": "31/12/2026"})
    dash = s.get(url(C.API_DASHBOARD))
    assert r.status_code == 400 and dash.status_code == 200, \
        f"Create returned {r.status_code}; dashboard afterwards returned {dash.status_code}"


# ======================= E - ELEVATION OF PRIVILEGE =======================

def test_SEC_18_another_users_task_cannot_be_deleted(user_a, user_b):
    tid = create_task(user_a, title=unique("victim"))
    r = user_b.delete(url(C.API_TASK, id=tid))
    still_there = user_a.get(url(C.API_TASK, id=tid)).status_code == 200
    assert still_there, f"User B deleted user A's task (DELETE returned {r.status_code})"


def test_SEC_19_another_users_task_cannot_be_edited(user_a, user_b):
    tid = create_task(user_a, title=unique("orig"))
    user_b.put(url(C.API_TASK, id=tid), json={"title": "hacked"})
    assert "hacked" not in user_a.get(url(C.API_TASK, id=tid)).text
