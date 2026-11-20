"""REQ-001 Registration and REQ-002 Login/logout/protected pages.

Automates Week 1 cases TC-BB-001 to TC-BB-019 (and re-checks DEF-001, also
reproduced by TC-GUI-004). Expected results are the Week 1 specification-based
expectations; they are not adjusted to current behaviour.
"""

import pytest

from conftest import PASSWORD, RUN_STARTED, _counter

USERNAME_RULE = "Username must be 3-20 characters"
PASSWORD_RULE = "Password must be at least 8 characters"


def username_of_length(n):
    """A unique, valid-character username of exactly n characters."""
    _counter["n"] += 1
    seed = f"r{RUN_STARTED:%H%M%S}{_counter['n']}"
    return (seed + "a" * n)[:n]


def assert_registered(ui, username):
    assert ui.path == "/", f"expected the task list after registration, browser is on {ui.path} " \
                           f"(error shown: {ui.error_text()!r})"
    assert ui.heading() == "My Tasks"
    assert ui.nav_username() == username


def assert_rejected(ui, rule_text):
    assert ui.path == "/register", f"expected to stay on /register, browser is on {ui.path}"
    assert ui.error_text() and rule_text in ui.error_text(), f"error shown: {ui.error_text()!r}"


# ---------------------------------------------------------------------------
# REQ-001 Registration
# ---------------------------------------------------------------------------

@pytest.mark.auto("TC-AUT-001")
@pytest.mark.req("REQ-001")
@pytest.mark.parametrize("length, accepted", [
    pytest.param(2, False, marks=pytest.mark.manual("TC-BB-001"), id="TC-BB-001-len2"),
    pytest.param(3, True, marks=pytest.mark.manual("TC-BB-002"), id="TC-BB-002-len3"),
    pytest.param(4, True, marks=pytest.mark.manual("TC-BB-003"), id="TC-BB-003-len4"),
    pytest.param(19, True, marks=pytest.mark.manual("TC-BB-004"), id="TC-BB-004-len19"),
    pytest.param(20, True, marks=pytest.mark.manual("TC-BB-005"), id="TC-BB-005-len20"),
    pytest.param(21, False, marks=pytest.mark.manual("TC-BB-006"), id="TC-BB-006-len21"),
])
def test_username_length_boundaries(ui, length, accepted):
    username = username_of_length(length)
    ui.register(username, PASSWORD)
    if accepted:
        assert_registered(ui, username)
    else:
        assert_rejected(ui, USERNAME_RULE)


@pytest.mark.auto("TC-AUT-002")
@pytest.mark.req("REQ-001")
@pytest.mark.parametrize("password, accepted", [
    pytest.param("Test123", False, marks=pytest.mark.manual("TC-BB-007"), id="TC-BB-007-len7"),
    pytest.param("Test1234", True, marks=[pytest.mark.manual("TC-BB-008", "TC-GUI-004"),
                                          pytest.mark.known_defect("DEF-001")], id="TC-BB-008-len8"),
    pytest.param("Test12345", True, marks=pytest.mark.manual("TC-BB-009"), id="TC-BB-009-len9"),
])
def test_password_length_boundaries(ui, password, accepted):
    username = username_of_length(12)
    ui.register(username, password)
    if accepted:
        assert_registered(ui, username)
    else:
        assert_rejected(ui, PASSWORD_RULE)


@pytest.mark.smoke
@pytest.mark.auto("TC-AUT-003")
@pytest.mark.manual("TC-BB-010")
@pytest.mark.req("REQ-001")
def test_valid_registration_opens_task_list(ui):
    username = "w6_a_" + username_of_length(8)  # letters, digits and underscore
    ui.register(username, PASSWORD)
    assert_registered(ui, username)
    assert ui.empty_message() == "No tasks match your filters."  # a new account has no tasks


@pytest.mark.auto("TC-AUT-004")
@pytest.mark.manual("TC-BB-011")
@pytest.mark.req("REQ-001")
def test_username_with_hyphen_is_rejected(ui):
    ui.register("w6-d", PASSWORD)
    assert_rejected(ui, USERNAME_RULE)


@pytest.mark.auto("TC-AUT-005")
@pytest.mark.req("REQ-001")
@pytest.mark.parametrize("empty_field", [
    pytest.param("username", marks=pytest.mark.manual("TC-BB-012"), id="TC-BB-012-empty-username"),
    pytest.param("password", marks=pytest.mark.manual("TC-BB-013"), id="TC-BB-013-empty-password"),
])
def test_empty_registration_field_blocked_by_browser(ui, empty_field):
    username = "" if empty_field == "username" else username_of_length(12)
    password = "" if empty_field == "password" else PASSWORD
    ui.register(username, password, wait=False)
    state = ui.validation_state(empty_field)
    assert state["valueMissing"], f"{empty_field} is not flagged as missing: {state}"
    assert state["message"], "browser shows no validation message"
    assert ui.path == "/register" and ui.heading() == "Create an account"


# ---------------------------------------------------------------------------
# REQ-002 Login, logout and protected pages
# ---------------------------------------------------------------------------

@pytest.mark.auto("TC-AUT-006")
@pytest.mark.req("REQ-002")
@pytest.mark.parametrize("known_user, right_password, allowed", [
    pytest.param(True, True, True, marks=[pytest.mark.manual("TC-BB-014"), pytest.mark.smoke],
                 id="TC-BB-014-rule1-valid"),
    pytest.param(True, False, False, marks=pytest.mark.manual("TC-BB-015"), id="TC-BB-015-rule2-wrong-pw"),
    pytest.param(False, True, False, marks=pytest.mark.manual("TC-BB-016"), id="TC-BB-016-rule3-unknown-user"),
    pytest.param(False, False, False, marks=pytest.mark.manual("TC-BB-017"), id="TC-BB-017-rule4-both-wrong"),
])
def test_login_decision_table(ui, new_account, known_user, right_password, allowed):
    baseline = new_account("dt")
    username = baseline["username"] if known_user else "w6_unknown_" + baseline["username"][-6:]
    password = baseline["password"] if right_password else "WrongPass1"
    ui.login(username, password)
    if allowed:
        assert ui.path == "/" and ui.heading() == "My Tasks"
        assert ui.nav_username() == baseline["username"]
    else:
        assert ui.path == "/login", f"expected to stay on /login, browser is on {ui.path}"
        assert ui.error_text() == "Invalid username or password."
        ui.open("/")
        assert ui.path == "/login", "rejected login must not grant access to protected pages"


@pytest.mark.smoke
@pytest.mark.auto("TC-AUT-007")
@pytest.mark.manual("TC-BB-018")
@pytest.mark.req("REQ-002")
@pytest.mark.parametrize("path", ["/", "/dashboard", "/tasks/new"], ids=["list", "dashboard", "new-task"])
def test_protected_page_redirects_when_logged_out(ui, path):
    ui.open(path)
    assert ui.path == "/login"
    assert ui.heading() == "Log in"


@pytest.mark.smoke
@pytest.mark.auto("TC-AUT-008")
@pytest.mark.manual("TC-BB-019")
@pytest.mark.req("REQ-002")
def test_logout_revokes_protected_page_access(ui, logged_in):
    assert ui.nav_username() == logged_in["username"]
    ui.logout()
    assert ui.path == "/login"
    ui.open("/")
    assert ui.path == "/login", "after logout, / must require login again"
