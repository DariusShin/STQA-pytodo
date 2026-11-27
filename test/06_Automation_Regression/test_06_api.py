"""Week 4 REST API cases TC-API-001 to TC-API-045, automated without a browser.

One test per Week 4 case (TC-AUT-029 to TC-AUT-073 = TC-API-001 to 045); the
lettered variants of a case (TC-API-036a, b, ...) are parametrize rows with the
variant as the row ID. Expected results are the checks written in the Week 4
Postman collection before execution (test/04_Web_API/test_cases.md); they are
not adjusted to the current behaviour. Failing Week 4 cases are marked
known_defect and run as strict xfail.

Every test works on fresh accounts, so the cases that leave a user unable to
load their list (DEF-015) cannot affect any other check, and the "run last"
ordering that the Postman collection needed is not required here.
"""

import pytest

from api_checks import expect_json_error, sized_username, titles
from api_client import ApiClient
from conftest import PASSWORD, iso_in, unique_username

MISSING = 999999999  # an id that never exists


@pytest.fixture
def anon(base_url):
    """A client with no session cookie."""
    return ApiClient(base_url)


@pytest.fixture
def user(new_account):
    """A fresh registered and logged-in API user."""
    return new_account("api")


@pytest.fixture
def api(user):
    return user["api"]


@pytest.fixture
def owner_and_intruder(new_account):
    """User A owns one task; user B is a separate logged-in user."""
    owner, intruder = new_account("own"), new_account("intr")
    task = owner["api"].create_task("Owner's private task", category="Work", due_date=iso_in(4))
    return owner["api"], intruder["api"], task


# ---------------------------------------------------------------------------
# 01 Registration and login (REQ-001, REQ-002)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-029")
@pytest.mark.manual("TC-API-001")
@pytest.mark.req("REQ-001")
def test_api_register_valid_account(anon):
    username = unique_username("reg")
    resp = anon.request("POST", "/api/register", {"username": username, "password": PASSWORD})
    assert resp.status == 201, resp
    body = resp.json
    assert isinstance(body["id"], int)
    assert body["username"] == username
    assert anon.request("GET", "/api/tasks").status == 200, "registration did not start a session"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-030")
@pytest.mark.manual("TC-API-002")
@pytest.mark.req("REQ-001")
@pytest.mark.parametrize("length", [pytest.param(3, id="TC-API-002a-len3"),
                                    pytest.param(20, id="TC-API-002b-len20")])
def test_api_username_valid_length_boundaries(anon, length):
    username = sized_username(length)
    assert len(username) == length
    resp = anon.request("POST", "/api/register", {"username": username, "password": PASSWORD})
    assert resp.status == 201, resp


@pytest.mark.api
@pytest.mark.auto("TC-AUT-031")
@pytest.mark.manual("TC-API-003")
@pytest.mark.req("REQ-001")
@pytest.mark.parametrize("payload", [
    pytest.param({"username": "ab", "password": PASSWORD}, id="TC-API-003a-len2"),
    pytest.param({"username": "w" * 21, "password": PASSWORD}, id="TC-API-003b-len21"),
    pytest.param({"username": "bad-name", "password": PASSWORD}, id="TC-API-003c-hyphen"),
    pytest.param({"password": PASSWORD}, id="TC-API-003d-missing"),
])
def test_api_invalid_username_partitions(anon, payload):
    expect_json_error(anon.request("POST", "/api/register", payload), 400, "invalid username")


@pytest.mark.api
@pytest.mark.auto("TC-AUT-032")
@pytest.mark.manual("TC-API-004")
@pytest.mark.req("REQ-001")
def test_api_password_length_7_rejected(anon):
    resp = anon.request("POST", "/api/register",
                        {"username": unique_username("pw7"), "password": "abc1234"})
    expect_json_error(resp, 400, "invalid password")


@pytest.mark.api
@pytest.mark.auto("TC-AUT-033")
@pytest.mark.manual("TC-API-005")
@pytest.mark.req("REQ-001")
@pytest.mark.known_defect("DEF-001")
def test_api_password_length_8_accepted(anon):
    resp = anon.request("POST", "/api/register",
                        {"username": unique_username("pw8"), "password": "abcd1234"})
    assert resp.status == 201, f"8-character password: {resp!r}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-034")
@pytest.mark.manual("TC-API-006")
@pytest.mark.req("REQ-001")
def test_api_missing_password_rejected(anon):
    expect_json_error(anon.request("POST", "/api/register", {"username": unique_username("nopw")}), 400)


@pytest.mark.api
@pytest.mark.auto("TC-AUT-035")
@pytest.mark.manual("TC-API-007")
@pytest.mark.req("REQ-001", "REQ-009")
@pytest.mark.known_defect("DEF-018")
def test_api_username_wrong_json_type(anon):
    expect_json_error(anon.request("POST", "/api/register", {"username": 12345, "password": PASSWORD}), 400)


@pytest.mark.api
@pytest.mark.auto("TC-AUT-036")
@pytest.mark.manual("TC-API-008")
@pytest.mark.req("REQ-001")
@pytest.mark.known_defect("DEF-016")
def test_api_duplicate_username_rejected(user, anon):
    resp = anon.request("POST", "/api/register", {"username": user["username"], "password": "Different99"})
    assert resp.status in (400, 409), f"duplicate username {user['username']!r} was accepted: {resp!r}"
    assert resp.is_json
    login = ApiClient(anon.base_url).request(
        "POST", "/api/login", {"username": user["username"], "password": PASSWORD})
    assert login.status == 200, login


@pytest.mark.api
@pytest.mark.auto("TC-AUT-037")
@pytest.mark.manual("TC-API-009")
@pytest.mark.req("REQ-002")
def test_api_login_valid_credentials(user, anon):
    resp = anon.request("POST", "/api/login", {"username": user["username"], "password": PASSWORD})
    assert resp.status == 200, resp
    assert resp.json["username"] == user["username"]
    assert anon.request("GET", "/api/tasks").status == 200, "login did not start a session"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-038")
@pytest.mark.manual("TC-API-010")
@pytest.mark.req("REQ-002")
@pytest.mark.parametrize("variant", [
    pytest.param("wrong-password", id="TC-API-010a-wrong-password"),
    pytest.param("unknown-user", id="TC-API-010b-unknown-user"),
    pytest.param("empty-body", id="TC-API-010c-empty-body"),
])
def test_api_login_invalid_credentials(user, anon, variant):
    payload = {
        "wrong-password": {"username": user["username"], "password": "Wrong12345"},
        "unknown-user": {"username": "w6nobody000000", "password": PASSWORD},
        "empty-body": {},
    }[variant]
    expect_json_error(anon.request("POST", "/api/login", payload), 401, "invalid credentials")
    assert anon.request("GET", "/api/tasks").status == 401, "a failed login started a session"


# ---------------------------------------------------------------------------
# 02 Authentication required (REQ-002, REQ-009)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-039")
@pytest.mark.manual("TC-API-011")
@pytest.mark.req("REQ-002", "REQ-009")
@pytest.mark.parametrize("method, path, payload", [
    pytest.param("GET", "/api/tasks", None, id="TC-API-011a-list"),
    pytest.param("POST", "/api/tasks", {"title": "x"}, id="TC-API-011b-create"),
    pytest.param("GET", "/api/tasks/1", None, id="TC-API-011c-read"),
    pytest.param("PUT", "/api/tasks/1", {"title": "x"}, id="TC-API-011d-update"),
    pytest.param("DELETE", "/api/tasks/1", None, id="TC-API-011e-delete"),
    pytest.param("GET", "/api/dashboard", None, id="TC-API-011f-dashboard"),
])
def test_api_protected_endpoints_require_session(anon, method, path, payload):
    expect_json_error(anon.request(method, path, payload), 401, "authentication required")


@pytest.mark.api
@pytest.mark.auto("TC-AUT-040")
@pytest.mark.manual("TC-API-012")
@pytest.mark.req("REQ-009")
@pytest.mark.known_defect("DEF-023")
def test_api_categories_require_session(anon):
    resp = anon.request("GET", "/api/categories")
    assert resp.status == 401, f"categories without login: {resp!r}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-041")
@pytest.mark.manual("TC-API-013")
@pytest.mark.req("REQ-009")
def test_api_list_categories(api):
    resp = api.request("GET", "/api/categories")
    assert resp.status == 200, resp
    names = [c["name"] for c in resp.json]
    assert names == ["Personal", "Study", "Urgent", "Work"], names


# ---------------------------------------------------------------------------
# 03 Create and read tasks (REQ-003, REQ-006, REQ-009)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-042")
@pytest.mark.manual("TC-API-014")
@pytest.mark.req("REQ-003")
def test_api_create_task_with_all_fields(api):
    work = api.categories()["Work"]
    resp = api.request("POST", "/api/tasks", {"title": "Prepare W4 report", "description": "API section",
                                              "category_id": work, "due_date": iso_in(5)})
    assert resp.status == 201, resp
    t = resp.json
    assert (t["title"], t["description"], t["category_id"], t["category"], t["due_date"]) == \
           ("Prepare W4 report", "API section", work, "Work", iso_in(5))
    assert t["done"] is False and t["completed_at"] is None
    assert t["urgency"] == "Upcoming"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-043")
@pytest.mark.manual("TC-API-015")
@pytest.mark.req("REQ-003")
def test_api_create_title_only_task(api):
    resp = api.request("POST", "/api/tasks", {"title": "Title only"})
    assert resp.status == 201, resp
    t = resp.json
    assert (t["description"], t["category_id"], t["category"], t["due_date"]) == ("", None, None, None)
    assert t["urgency"] == "No due date"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-044")
@pytest.mark.manual("TC-API-016")
@pytest.mark.req("REQ-003")
@pytest.mark.parametrize("payload", [
    pytest.param({}, id="TC-API-016a-missing"),
    pytest.param({"title": ""}, id="TC-API-016b-empty"),
    pytest.param({"title": "   "}, id="TC-API-016c-spaces"),
])
def test_api_title_required(api, payload):
    expect_json_error(api.request("POST", "/api/tasks", payload), 400, "title is required")
    assert api.tasks() == [], "a rejected task was saved"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-045")
@pytest.mark.manual("TC-API-017")
@pytest.mark.req("REQ-009")
def test_api_non_json_body_rejected(api):
    expect_json_error(api.request("POST", "/api/tasks", form={"title": "form body"}), 400)


@pytest.mark.api
@pytest.mark.auto("TC-AUT-046")
@pytest.mark.manual("TC-API-018")
@pytest.mark.req("REQ-003", "REQ-009")
@pytest.mark.parametrize("payload", [
    pytest.param({"title": 123}, marks=pytest.mark.known_defect("DEF-018"), id="TC-API-018a-title-number"),
    pytest.param({"title": ["a", "b"]}, marks=pytest.mark.known_defect("DEF-018"), id="TC-API-018b-title-list"),
    pytest.param({"title": "ok", "description": {"a": 1}}, marks=pytest.mark.known_defect("DEF-018"),
                 id="TC-API-018c-description-object"),
])
def test_api_wrong_json_types_on_create(api, payload):
    expect_json_error(api.request("POST", "/api/tasks", payload), 400)


@pytest.mark.api
@pytest.mark.auto("TC-AUT-047")
@pytest.mark.manual("TC-API-019")
@pytest.mark.req("REQ-003", "REQ-006")
@pytest.mark.parametrize("due_date", [
    pytest.param("31/12/2026", marks=pytest.mark.known_defect("DEF-015"), id="TC-API-019a-wrong-format"),
    pytest.param("2026-02-30", marks=pytest.mark.known_defect("DEF-015"), id="TC-API-019b-impossible-date"),
    pytest.param("tomorrow", marks=pytest.mark.known_defect("DEF-015"), id="TC-API-019c-text"),
])
def test_api_invalid_due_date_on_create(api, due_date):
    create = api.request("POST", "/api/tasks", {"title": "bad date", "due_date": due_date})
    after = (api.request("GET", "/api/tasks").status, api.request("GET", "/api/dashboard").status)
    assert (create.status, create.is_json) == (400, True), \
        f"due_date {due_date!r}: create returned {create!r}; list/dashboard then returned {after}"
    assert after == (200, 200), f"list/dashboard after the rejected create returned {after}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-048")
@pytest.mark.manual("TC-API-020")
@pytest.mark.req("REQ-003")
@pytest.mark.parametrize("category_id", [
    pytest.param(999, marks=pytest.mark.known_defect("DEF-019"), id="TC-API-020a-unknown-id"),
    pytest.param("abc", marks=pytest.mark.known_defect("DEF-019"), id="TC-API-020b-text"),
])
def test_api_invalid_category_on_create(api, category_id):
    expect_json_error(api.request("POST", "/api/tasks", {"title": "bad category", "category_id": category_id}), 400)


@pytest.mark.api
@pytest.mark.auto("TC-AUT-049")
@pytest.mark.manual("TC-API-021")
@pytest.mark.req("REQ-006")
@pytest.mark.parametrize("offset, expected", [
    pytest.param(-1, "Overdue", id="TC-API-021a-yesterday"),
    pytest.param(0, "Due Today", marks=pytest.mark.known_defect("DEF-002"), id="TC-API-021b-today"),
    pytest.param(1, "Due Soon", id="TC-API-021c-plus1"),
    pytest.param(2, "Due Soon", id="TC-API-021d-plus2"),
    pytest.param(3, "Upcoming", id="TC-API-021e-plus3"),
])
def test_api_urgency_boundaries(api, offset, expected):
    resp = api.request("POST", "/api/tasks", {"title": f"urgency {offset:+d}", "due_date": iso_in(offset)})
    assert resp.status == 201, resp
    assert resp.json["urgency"] == expected, f"due {iso_in(offset)}: urgency {resp.json['urgency']!r}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-050")
@pytest.mark.manual("TC-API-022")
@pytest.mark.req("REQ-003")
def test_api_read_own_task(api):
    task = api.create_task("Prepare W4 report", description="API section", category="Work", due_date=iso_in(5))
    resp = api.request("GET", f"/api/tasks/{task['id']}")
    assert resp.status == 200, resp
    assert (resp.json["id"], resp.json["title"]) == (task["id"], "Prepare W4 report")


@pytest.mark.api
@pytest.mark.auto("TC-AUT-051")
@pytest.mark.manual("TC-API-023")
@pytest.mark.req("REQ-003", "REQ-009")
def test_api_read_missing_task(api):
    expect_json_error(api.request("GET", f"/api/tasks/{MISSING}"), 404, "not found")


@pytest.mark.api
@pytest.mark.auto("TC-AUT-052")
@pytest.mark.manual("TC-API-024")
@pytest.mark.req("REQ-008")
def test_api_read_another_users_task(owner_and_intruder):
    _, intruder, task = owner_and_intruder
    resp = intruder.request("GET", f"/api/tasks/{task['id']}")
    expect_json_error(resp, 404, "not found")
    assert task["title"] not in resp.text, "the owner's title was disclosed"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-053")
@pytest.mark.manual("TC-API-025")
@pytest.mark.req("REQ-009")
def test_api_non_integer_task_id(api):
    assert api.request("GET", "/api/tasks/abc").status == 404


# ---------------------------------------------------------------------------
# 04 List, filter, search, paging (REQ-005, REQ-009) - Week 4 list dataset
# ---------------------------------------------------------------------------

LIST_DATASET = [  # title, category, done
    ("Weekly report", "Work", False),
    ("Report archive", "Work", True),
    ("Buy groceries", "Personal", False),
    ("Read chapter 4", None, False),
    ("Call O'Brien", None, False),
]


@pytest.fixture(scope="module")
def list_user(base_url):
    """One account holding exactly the five-task list dataset (read-only for these tests)."""
    api = ApiClient(base_url)
    api.register(unique_username("list"), PASSWORD)
    for title, category, done in LIST_DATASET:
        api.create_task(title, category=category, done=done)
    return api


def _list(api, **params):
    resp = api.request("GET", "/api/tasks", params=params)
    assert resp.status == 200, f"GET /api/tasks {params}: {resp!r}"
    return resp.json


@pytest.mark.api
@pytest.mark.auto("TC-AUT-054")
@pytest.mark.manual("TC-API-026")
@pytest.mark.req("REQ-005")
def test_api_filter_by_category(list_user):
    assert titles(_list(list_user, category="Work")) == ["Report archive", "Weekly report"]


@pytest.mark.api
@pytest.mark.auto("TC-AUT-055")
@pytest.mark.manual("TC-API-027")
@pytest.mark.req("REQ-005")
@pytest.mark.parametrize("status, expected", [
    pytest.param("open", ["Buy groceries", "Call O'Brien", "Read chapter 4", "Weekly report"], id="TC-API-027a-open"),
    pytest.param("done", ["Report archive"], id="TC-API-027b-done"),
])
def test_api_filter_by_status(list_user, status, expected):
    assert titles(_list(list_user, status=status)) == expected


@pytest.mark.api
@pytest.mark.auto("TC-AUT-056")
@pytest.mark.manual("TC-API-028")
@pytest.mark.req("REQ-005")
def test_api_title_search(list_user):
    assert titles(_list(list_user, q="report")) == ["Report archive", "Weekly report"]


@pytest.mark.api
@pytest.mark.auto("TC-AUT-057")
@pytest.mark.manual("TC-API-029")
@pytest.mark.req("REQ-005")
def test_api_combined_filters(list_user):
    assert titles(_list(list_user, category="Work", status="open", q="report")) == ["Weekly report"]


@pytest.mark.api
@pytest.mark.auto("TC-AUT-058")
@pytest.mark.manual("TC-API-030")
@pytest.mark.req("REQ-005")
@pytest.mark.known_defect("DEF-017")
def test_api_search_with_apostrophe(list_user):
    resp = list_user.request("GET", "/api/tasks", params={"q": "O'Brien"})
    assert resp.status == 200, f"search for O'Brien: {resp!r}"
    assert titles(resp.json) == ["Call O'Brien"]


@pytest.mark.api
@pytest.mark.auto("TC-AUT-059")
@pytest.mark.manual("TC-API-031")
@pytest.mark.req("REQ-005", "REQ-009")
def test_api_pagination(api):
    ids = [api.create_task(f"Page task {i}")["id"] for i in range(1, 6)]
    newest_first = ids[::-1]
    pages = [[t["id"] for t in _list(api, per_page=2, page=p)] for p in (0, 1, 2)]
    assert pages == [newest_first[0:2], newest_first[2:4], newest_first[4:5]], pages
    assert [t["id"] for t in _list(api)] == newest_first


@pytest.mark.api
@pytest.mark.auto("TC-AUT-060")
@pytest.mark.manual("TC-API-032")
@pytest.mark.req("REQ-009")
@pytest.mark.parametrize("params", [
    pytest.param({"per_page": "-1"}, marks=pytest.mark.known_defect("DEF-022"), id="TC-API-032a-per-page-negative"),
    pytest.param({"page": "-1"}, marks=pytest.mark.known_defect("DEF-022"), id="TC-API-032b-page-negative"),
    pytest.param({"page": "abc"}, marks=pytest.mark.known_defect("DEF-022"), id="TC-API-032c-page-text"),
])
def test_api_invalid_pagination(api, params):
    for i in range(3):
        api.create_task(f"Paging {i}")
    expect_json_error(api.request("GET", "/api/tasks", params=params), 400)


@pytest.mark.api
@pytest.mark.auto("TC-AUT-061")
@pytest.mark.manual("TC-API-033")
@pytest.mark.req("REQ-008")
def test_api_task_list_scoped_to_user(list_user, new_account):
    assert len(list_user.tasks()) == len(LIST_DATASET), "precondition: owner has the list dataset"
    assert _list(new_account("intr")["api"]) == []


# ---------------------------------------------------------------------------
# 05 Update tasks (REQ-003, REQ-004, REQ-009)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-062")
@pytest.mark.manual("TC-API-034")
@pytest.mark.req("REQ-003")
def test_api_partial_update(api):
    before = api.create_task("Old", description="keep me", category="Study", due_date=iso_in(4))
    resp = api.request("PUT", f"/api/tasks/{before['id']}", {"title": "New"})
    assert resp.status == 200, resp
    t = resp.json
    assert t["title"] == "New"
    assert (t["description"], t["category_id"], t["due_date"]) == \
           (before["description"], before["category_id"], before["due_date"])
    assert t["done"] is False


@pytest.mark.api
@pytest.mark.auto("TC-AUT-063")
@pytest.mark.manual("TC-API-035")
@pytest.mark.req("REQ-004")
def test_api_complete_and_reopen(api):
    task = api.create_task("Complete me", due_date=iso_in(-3))
    done = api.request("PUT", f"/api/tasks/{task['id']}", {"done": True})
    assert done.status == 200, done
    assert (done.json["done"], done.json["urgency"]) == (True, "Done")
    assert done.json["completed_at"], "completed_at was not set"
    reopened = api.request("PUT", f"/api/tasks/{task['id']}", {"done": False})
    assert reopened.status == 200, reopened
    assert (reopened.json["done"], reopened.json["completed_at"], reopened.json["urgency"]) == \
           (False, None, "Overdue")


@pytest.mark.api
@pytest.mark.auto("TC-AUT-064")
@pytest.mark.manual("TC-API-036")
@pytest.mark.req("REQ-003", "REQ-009")
@pytest.mark.parametrize("payload", [
    pytest.param({"title": ""}, marks=pytest.mark.known_defect("DEF-020"), id="TC-API-036a-title-empty"),
    pytest.param({"title": "   "}, marks=pytest.mark.known_defect("DEF-020"), id="TC-API-036b-title-spaces"),
    pytest.param({"done": "false"}, marks=pytest.mark.known_defect("DEF-020"), id="TC-API-036c-done-text"),
    pytest.param({"title": None}, marks=pytest.mark.known_defect("DEF-018"), id="TC-API-036d-title-null"),
    pytest.param({"category_id": 999}, marks=pytest.mark.known_defect("DEF-019"), id="TC-API-036e-unknown-category"),
    pytest.param({"due_date": "31/12/2026"}, marks=pytest.mark.known_defect("DEF-015"), id="TC-API-036f-bad-due-date"),
])
def test_api_invalid_values_on_update(api, payload):
    before = api.create_task("Stable title", category="Work", due_date=iso_in(5))
    resp = api.request("PUT", f"/api/tasks/{before['id']}", payload)
    check = api.request("GET", f"/api/tasks/{before['id']}")
    after = check.json if check.is_json else None
    stored = None if after is None else \
        {k: after.get(k) for k in ("title", "done", "category_id", "due_date")}
    expected = {k: before[k] for k in ("title", "done", "category_id", "due_date")}
    assert (resp.status, resp.is_json) == (400, True), \
        f"PUT {payload}: {resp!r}; task afterwards: {check.status} {stored}"
    assert check.status == 200 and stored == expected, f"task changed: {stored}, expected {expected}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-065")
@pytest.mark.manual("TC-API-037")
@pytest.mark.req("REQ-008")
def test_api_update_another_users_task(owner_and_intruder):
    owner, intruder, task = owner_and_intruder
    expect_json_error(intruder.request("PUT", f"/api/tasks/{task['id']}", {"title": "hijacked"}), 404, "not found")
    check = owner.request("GET", f"/api/tasks/{task['id']}")
    assert check.status == 200 and check.json["title"] == task["title"], check


@pytest.mark.api
@pytest.mark.auto("TC-AUT-066")
@pytest.mark.manual("TC-API-038")
@pytest.mark.req("REQ-009")
def test_api_update_missing_task(api):
    expect_json_error(api.request("PUT", f"/api/tasks/{MISSING}", {"title": "x"}), 404, "not found")


# ---------------------------------------------------------------------------
# 06 Delete tasks (REQ-003, REQ-008, REQ-009)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-067")
@pytest.mark.manual("TC-API-039")
@pytest.mark.req("REQ-003")
def test_api_delete_own_task(api):
    task = api.create_task("Delete me")
    resp = api.request("DELETE", f"/api/tasks/{task['id']}")
    assert resp.status == 200 and resp.json == {"result": "ok"}, resp
    assert api.request("GET", f"/api/tasks/{task['id']}").status == 404


@pytest.mark.api
@pytest.mark.auto("TC-AUT-068")
@pytest.mark.manual("TC-API-040")
@pytest.mark.req("REQ-008")
@pytest.mark.known_defect("DEF-014")
def test_api_delete_another_users_task(owner_and_intruder):
    owner, intruder, task = owner_and_intruder
    delete = intruder.request("DELETE", f"/api/tasks/{task['id']}")
    check = owner.request("GET", f"/api/tasks/{task['id']}")
    assert (delete.status, check.status) == (404, 200), \
        f"intruder DELETE returned {delete.status}; owner's GET afterwards returned {check.status}"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-069")
@pytest.mark.manual("TC-API-041")
@pytest.mark.req("REQ-009")
@pytest.mark.known_defect("DEF-021")
def test_api_delete_missing_task(api):
    expect_json_error(api.request("DELETE", f"/api/tasks/{MISSING}"), 404, "not found")


# ---------------------------------------------------------------------------
# 08 Dashboard (REQ-006, REQ-007, REQ-008) - Week 4 dashboard dataset
# ---------------------------------------------------------------------------

def seed_dashboard_dataset(api):
    """today-1, today+1, today+5, no date (open) and one completed task due today-2."""
    for title, offset, done in [("D overdue", -1, False), ("D soon", 1, False), ("D later", 5, False),
                                ("D no date", None, False), ("D completed", -2, True)]:
        api.create_task(title, due_date=iso_in(offset), done=done)


def _dashboard(api):
    resp = api.request("GET", "/api/dashboard")
    assert resp.status == 200, resp
    return resp.json


@pytest.mark.api
@pytest.mark.auto("TC-AUT-070")
@pytest.mark.manual("TC-API-042")
@pytest.mark.req("REQ-007")
def test_api_dashboard_counts(api):
    seed_dashboard_dataset(api)
    assert _dashboard(api) == {"total": 5, "open": 4, "overdue": 1, "due_soon": 1, "completed_this_week": 1}


@pytest.mark.api
@pytest.mark.auto("TC-AUT-071")
@pytest.mark.manual("TC-API-043")
@pytest.mark.req("REQ-006", "REQ-007")
@pytest.mark.known_defect("DEF-002")
def test_api_dashboard_due_today_not_overdue(api):
    seed_dashboard_dataset(api)
    api.create_task("D today", due_date=iso_in(0))
    counts = _dashboard(api)
    assert counts["total"] == 6
    assert counts["overdue"] == 1, f"Overdue counter is {counts['overdue']}, expected 1"


@pytest.mark.api
@pytest.mark.auto("TC-AUT-072")
@pytest.mark.manual("TC-API-044")
@pytest.mark.req("REQ-008")
def test_api_dashboard_scoped_to_user(new_account):
    owner, intruder = new_account("own")["api"], new_account("intr")["api"]
    owner.create_task("A overdue", due_date=iso_in(-1))
    owner.create_task("A soon", due_date=iso_in(1))
    assert _dashboard(intruder) == {"total": 0, "open": 0, "overdue": 0, "due_soon": 0, "completed_this_week": 0}


# ---------------------------------------------------------------------------
# 09 HTTP method (REQ-009)
# ---------------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.auto("TC-AUT-073")
@pytest.mark.manual("TC-API-045")
@pytest.mark.req("REQ-009")
def test_api_unsupported_method(api):
    task = api.create_task("Patch target")
    assert api.request("PATCH", f"/api/tasks/{task['id']}", {"title": "x"}).status == 405
