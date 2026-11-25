"""Small helper used by the security tests and the seed script."""
import requests
import config as C


def url(path, **kw):
    return C.BASE_URL + path.format(**kw)


def api_register(session, username, password=C.PASSWORD):
    return session.post(url(C.API_REGISTER), json={"username": username, "password": password})


def api_login(session, username, password=C.PASSWORD):
    return session.post(url(C.API_LOGIN), json={"username": username, "password": password})


def logged_in_session(username, password=C.PASSWORD):
    """Return a requests.Session logged in as username (registers once if needed).
    Note: PyTodo allows duplicate usernames (DEF-016), so we log in first and only
    register if login fails, to avoid creating duplicates."""
    s = requests.Session()
    r = api_login(s, username, password)
    if r.status_code != 200:
        r = api_register(s, username, password)
    assert r.status_code in (200, 201), f"Cannot log in/register {username}: {r.status_code} {r.text}"
    s.user_id = r.json()["id"]
    return s


def create_task(session, title="Week5 task", **extra):
    payload = {"title": title, "category_id": C.VALID_CATEGORY_ID, "due_date": C.VALID_DUE_DATE}
    payload.update(extra)
    r = session.post(url(C.API_TASKS), json=payload)
    assert r.status_code == 201, f"Create failed: {r.status_code} {r.text[:200]}"
    return r.json()["id"]


def list_tasks(session, **params):
    r = session.get(url(C.API_TASKS), params=params)
    return r.json() if r.status_code == 200 else []
