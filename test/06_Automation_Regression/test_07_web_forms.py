"""Week 4 web cases TC-WEB-001 to TC-WEB-016, automated without a browser.

One test per Week 4 case (TC-AUT-074 to TC-AUT-089 = TC-WEB-001 to 016). As in
Week 4, the checks send the same form fields a browser sends to the real web
routes, including values the browser would normally block (an empty
`required` field, text in the date field, a category the drop-down does not
offer), because the server must validate its input on its own. Results are
then read back through the JSON API, which is what makes these UI-versus-API
comparisons. Redirects are not followed, so the 302 and its target are
asserted directly. Pages are read with the standard-library HTML parser.

Expected results are the checks in the Week 4 Postman collection
(test/04_Web_API/test_cases.md); they are not adjusted to current behaviour.
"""

import pytest

from api_checks import (expect_not_accepted, expect_redirect, page_dashboard, page_error,
                        page_task_rows, titles)
from api_client import ApiClient
from conftest import PASSWORD, iso_in, unique_username

USERNAME_RULE = "Username must be 3-20 characters"
PASSWORD_RULE = "Password must be at least 8 characters"
LOGIN_ERROR = "Invalid username or password."


@pytest.fixture
def anon(base_url):
    return ApiClient(base_url)


@pytest.fixture
def web_user(base_url):
    """A user registered and logged in through the web form POST /register."""
    client = ApiClient(base_url)
    username = unique_username("web")
    expect_redirect(client.web_post("/register", {"username": username, "password": PASSWORD}), "/")
    return {"username": username, "client": client}


@pytest.fixture
def client(web_user):
    return web_user["client"]


def blank_task_form(**fields):
    form = {"title": "", "description": "", "category_id": "", "due_date": ""}
    form.update(fields)
    return form


# ---------------------------------------------------------------------------
# Registration and login (REQ-001, REQ-002)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-074")
@pytest.mark.manual("TC-WEB-001")
@pytest.mark.req("REQ-001")
def test_web_register_through_form(anon):
    username = unique_username("web")
    expect_redirect(anon.web_post("/register", {"username": username, "password": PASSWORD}), "/")
    page = anon.web_get("/")
    assert page.status == 200, page
    assert "My Tasks" in page.text
    assert username in page.text, "the task list does not show the new username"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-075")
@pytest.mark.manual("TC-WEB-002")
@pytest.mark.req("REQ-001")
@pytest.mark.parametrize("variant, rule", [
    pytest.param("empty-username", USERNAME_RULE, id="TC-WEB-002a-empty-username"),
    pytest.param("bad-name", USERNAME_RULE, id="TC-WEB-002b-illegal-character"),
    pytest.param("password-7", PASSWORD_RULE, id="TC-WEB-002c-password-7"),
])
def test_web_registration_validated_on_server(anon, variant, rule):
    form = {
        "empty-username": {"username": "", "password": PASSWORD},
        "bad-name": {"username": "bad-name", "password": PASSWORD},
        "password-7": {"username": unique_username("web"), "password": "abc1234"},
    }[variant]
    resp = anon.web_post("/register", form)
    assert resp.status == 200, f"expected the form again with an error, got {resp.status} -> {resp.location}"
    error = page_error(resp.text)
    assert error and rule in error, f"error shown: {error!r}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-076")
@pytest.mark.manual("TC-WEB-003")
@pytest.mark.req("REQ-002")
@pytest.mark.parametrize("password, accepted", [
    pytest.param(PASSWORD, True, id="TC-WEB-003a-valid"),
    pytest.param("Wrong12345", False, id="TC-WEB-003b-wrong-password"),
])
def test_web_login_through_form(new_account, anon, password, accepted):
    account = new_account("web")
    resp = anon.web_post("/login", {"username": account["username"], "password": password})
    if accepted:
        expect_redirect(resp, "/")
    else:
        assert resp.status == 200, f"expected the login form again, got {resp.status} -> {resp.location}"
        assert page_error(resp.text) == LOGIN_ERROR


@pytest.mark.api
@pytest.mark.auto("TC-AUT-077")
@pytest.mark.manual("TC-WEB-004")
@pytest.mark.req("REQ-002")
@pytest.mark.parametrize("method, path", [
    pytest.param("GET", "/", id="TC-WEB-004a-list"),
    pytest.param("GET", "/tasks/new", id="TC-WEB-004b-new"),
    pytest.param("GET", "/tasks/1/edit", id="TC-WEB-004c-edit"),
    pytest.param("GET", "/dashboard", id="TC-WEB-004d-dashboard"),
    pytest.param("POST", "/tasks/1/toggle", id="TC-WEB-004e-toggle"),
    pytest.param("POST", "/tasks/1/delete", id="TC-WEB-004f-delete"),
])
def test_web_protected_pages_redirect_when_logged_out(anon, method, path):
    resp = anon.web_get(path) if method == "GET" else anon.web_post(path)
    expect_redirect(resp, "/login")


# ---------------------------------------------------------------------------
# Web <-> API consistency (REQ-003, REQ-004, REQ-006)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-078")
@pytest.mark.manual("TC-WEB-005")
@pytest.mark.req("REQ-003")
def test_web_created_task_matches_api(client):
    personal = client.categories()["Personal"]
    expect_redirect(client.web_post("/tasks/new", blank_task_form(
        title="Web-created task", description="via form", category_id=str(personal), due_date=iso_in(6))), "/")
    resp = client.request("GET", "/api/tasks", params={"q": "Web-created"})
    assert resp.status == 200, resp
    assert len(resp.json) == 1, resp.json
    t = resp.json[0]
    assert (t["title"], t["description"], t["category"], t["due_date"]) == \
           ("Web-created task", "via form", "Personal", iso_in(6))


@pytest.mark.api
@pytest.mark.auto("TC-AUT-079")
@pytest.mark.manual("TC-WEB-006")
@pytest.mark.req("REQ-003", "REQ-006")
def test_api_created_task_matches_web_list(new_account):
    api = new_account("web")["api"]
    api.create_task("API-created task", category="Study", due_date=iso_in(1))
    page = api.web_get("/")
    assert page.status == 200, page
    rows = [r for r in page_task_rows(page.text) if r["title"] == "API-created task"]
    assert len(rows) == 1, page_task_rows(page.text)
    assert (rows[0]["category"], rows[0]["due_date"], rows[0]["urgency"]) == ("Study", iso_in(1), "Due Soon")


@pytest.mark.api
@pytest.mark.auto("TC-AUT-080")
@pytest.mark.manual("TC-WEB-007")
@pytest.mark.req("REQ-003")
def test_web_edit_matches_api(new_account):
    api = new_account("web")["api"]
    task = api.create_task("Before edit", category="Work", due_date=iso_in(3))
    urgent = api.categories()["Urgent"]
    expect_redirect(api.web_post(f"/tasks/{task['id']}/edit", blank_task_form(
        title="After edit", description="edited on web", category_id=str(urgent), due_date=iso_in(9))), "/")
    resp = api.request("GET", f"/api/tasks/{task['id']}")
    assert resp.status == 200, resp
    t = resp.json
    assert (t["title"], t["description"], t["category_id"], t["due_date"]) == \
           ("After edit", "edited on web", urgent, iso_in(9))


@pytest.mark.api
@pytest.mark.auto("TC-AUT-081")
@pytest.mark.manual("TC-WEB-008")
@pytest.mark.req("REQ-004")
def test_web_toggle_matches_api(new_account):
    api = new_account("web")["api"]
    task = api.create_task("Toggle me")
    expect_redirect(api.web_post(f"/tasks/{task['id']}/toggle"), "/")
    done = api.request("GET", f"/api/tasks/{task['id']}").json
    assert done["done"] is True and done["completed_at"], done
    expect_redirect(api.web_post(f"/tasks/{task['id']}/toggle"), "/")
    reopened = api.request("GET", f"/api/tasks/{task['id']}").json
    assert (reopened["done"], reopened["completed_at"]) == (False, None), reopened


@pytest.mark.api
@pytest.mark.auto("TC-AUT-082")
@pytest.mark.manual("TC-WEB-009")
@pytest.mark.req("REQ-003")
def test_web_delete_matches_api(new_account):
    api = new_account("web")["api"]
    task = api.create_task("Delete on web")
    expect_redirect(api.web_post(f"/tasks/{task['id']}/delete"), "/")
    assert api.request("GET", f"/api/tasks/{task['id']}").status == 404


# ---------------------------------------------------------------------------
# Server-side validation of the web forms (REQ-001, REQ-003, REQ-006)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-083")
@pytest.mark.manual("TC-WEB-010")
@pytest.mark.req("REQ-003")
@pytest.mark.parametrize("title", [
    pytest.param("", marks=pytest.mark.known_defect("DEF-003"), id="TC-WEB-010a-empty"),
    pytest.param("   ", marks=pytest.mark.known_defect("DEF-003"), id="TC-WEB-010b-spaces"),
])
def test_web_blank_title_validated_on_server(client, title):
    resp = client.web_post("/tasks/new", blank_task_form(title=title))
    saved = client.tasks()
    expect_not_accepted(resp, f"saved titles: {titles(saved)}")
    assert saved == [], f"a task with title {title!r} was saved: {titles(saved)}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-084")
@pytest.mark.manual("TC-WEB-011")
@pytest.mark.req("REQ-003", "REQ-006")
@pytest.mark.parametrize("due_date", [
    pytest.param("31/12/2026", marks=pytest.mark.known_defect("DEF-015"), id="TC-WEB-011a-wrong-format"),
    pytest.param("not-a-date", marks=pytest.mark.known_defect("DEF-015"), id="TC-WEB-011b-text"),
])
def test_web_due_date_validated_on_server(client, due_date):
    resp = client.web_post("/tasks/new", blank_task_form(title="bad date", due_date=due_date))
    pages = (client.web_get("/").status, client.web_get("/dashboard").status)
    expect_not_accepted(resp, f"/ and /dashboard then returned {pages}")
    assert pages == (200, 200), f"/ and /dashboard afterwards returned {pages}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-085")
@pytest.mark.manual("TC-WEB-012")
@pytest.mark.req("REQ-003")
@pytest.mark.known_defect("DEF-019")
def test_web_category_validated_on_server(client):
    resp = client.web_post("/tasks/new", blank_task_form(title="bad category", category_id="999"))
    saved = client.tasks()
    expect_not_accepted(resp, f"saved: {[(t['title'], t['category_id']) for t in saved]}")
    assert saved == [], f"a task with category_id 999 was saved: {titles(saved)}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-086")
@pytest.mark.manual("TC-WEB-013")
@pytest.mark.req("REQ-008")
def test_web_actions_on_another_users_task(new_account):
    owner, intruder = new_account("own")["api"], new_account("intr")["api"]
    task = owner.create_task("Owner's web task", category="Work")
    intruder.web_post(f"/tasks/{task['id']}/edit", blank_task_form(title="hijacked"))
    intruder.web_post(f"/tasks/{task['id']}/toggle")
    intruder.web_post(f"/tasks/{task['id']}/delete")
    check = owner.request("GET", f"/api/tasks/{task['id']}")
    assert check.status == 200, f"owner's task is gone: {check!r}"
    assert (check.json["title"], check.json["done"]) == ("Owner's web task", False), check.json


@pytest.mark.api
@pytest.mark.auto("TC-AUT-087")
@pytest.mark.manual("TC-WEB-014")
@pytest.mark.req("REQ-007")
def test_web_dashboard_matches_api(new_account):
    api = new_account("web")["api"]
    for title, offset, done in [("W overdue", -1, False), ("W soon", 1, False),
                                ("W no date", None, False), ("W completed", -2, True)]:
        api.create_task(title, due_date=iso_in(offset), done=done)
    page = api.web_get("/dashboard")
    assert page.status == 200, page
    resp = api.request("GET", "/api/dashboard")
    assert resp.status == 200, resp
    assert page_dashboard(page.text) == resp.json


@pytest.mark.api
@pytest.mark.auto("TC-AUT-088")
@pytest.mark.manual("TC-WEB-015")
@pytest.mark.req("REQ-005")
def test_web_search_with_apostrophe(new_account):
    api = new_account("web")["api"]
    api.create_task("Call O'Brien")
    api.create_task("Other")
    page = api.web_get("/", params={"q": "O'Brien"})
    assert page.status == 200, page
    assert [r["title"] for r in page_task_rows(page.text)] == ["Call O'Brien"]


@pytest.mark.api
@pytest.mark.auto("TC-AUT-089")
@pytest.mark.manual("TC-WEB-016")
@pytest.mark.req("REQ-001")
@pytest.mark.known_defect("DEF-016")
def test_web_duplicate_username_rejected(new_account, anon):
    existing = new_account("web")["username"]
    resp = anon.web_post("/register", {"username": existing, "password": "Different99"})
    assert resp.status == 200, \
        f"duplicate username {existing!r} was accepted: {resp.status} redirect to {resp.location}"
    assert page_error(resp.text), "no error message shown"
