"""REQ-003 Task CRUD, REQ-004 Complete/reopen and REQ-008 Account separation.

Automates Week 1 cases TC-BB-020 to TC-BB-029 and TC-BB-044, plus Week 3
TC-GUI-020 (DEF-005). Preconditions are seeded through the API so each check
exercises only the UI behaviour it is about; results are cross-checked through
the API where the page itself could hide a problem.
"""

import pytest

from conftest import iso_in

SPECIAL_TITLE = "GUI-Special & <b>bold</b> \"double\" 'single' Résumé 报告"


@pytest.mark.smoke
@pytest.mark.auto("TC-AUT-009")
@pytest.mark.manual("TC-BB-020")
@pytest.mark.req("REQ-003")
def test_create_full_field_task_persists(ui, logged_in):
    due = iso_in(3)
    ui.create_task("BB-CRUD-Original", "Week 1 full-field task", "Work", due)
    assert ui.path == "/"
    row = ui.row("BB-CRUD-Original")
    assert (row["category"], row["due_date"], row["urgency"]) == ("Work", due, "Upcoming")
    ui.open_edit("BB-CRUD-Original")
    assert ui.task_form_values() == {
        "title": "BB-CRUD-Original", "description": "Week 1 full-field task",
        "category": "Work", "due_date": due,
    }


@pytest.mark.auto("TC-AUT-010")
@pytest.mark.manual("TC-BB-021")
@pytest.mark.req("REQ-003")
def test_create_title_only_task(ui, logged_in):
    ui.create_task("BB-MINIMAL")
    row = ui.row("BB-MINIMAL")
    assert (row["category"], row["due_date"], row["urgency"]) == ("—", "—", "No due date")


@pytest.mark.auto("TC-AUT-011")
@pytest.mark.manual("TC-BB-022")
@pytest.mark.req("REQ-003")
def test_empty_title_blocked_by_browser(ui, logged_in):
    ui.create_task("", description="no title", wait=False)
    state = ui.validation_state("title")
    assert state["valueMissing"] and state["message"], f"title not flagged as missing: {state}"
    assert ui.path == "/tasks/new" and ui.heading() == "New Task"
    assert logged_in["api"].tasks() == [], "no task may be created"


@pytest.mark.auto("TC-AUT-012")
@pytest.mark.manual("TC-BB-023", "TC-GUI-016")
@pytest.mark.req("REQ-003")
@pytest.mark.known_defect("DEF-003")
def test_whitespace_only_title_rejected(ui, logged_in):
    ui.open("/tasks/new")
    ui.fill_task_form(title="   ")
    ui.submit_form_if_accepted()
    created = logged_in["api"].tasks()
    assert created == [], f"whitespace-only title created {len(created)} task(s): " \
                          f"{[t['title'] for t in created]!r}"
    assert ui.path == "/tasks/new", "the form should stay open with a validation message"


@pytest.mark.auto("TC-AUT-013")
@pytest.mark.manual("TC-BB-024", "TC-GUI-012", "TC-GUI-015")
@pytest.mark.req("REQ-003")
def test_edit_persists_all_fields(ui, logged_in):
    original_due, new_due = iso_in(3), iso_in(2)
    logged_in["api"].create_task("BB-CRUD-Original", "Week 1 full-field task", "Work", original_due)
    ui.open("/")
    ui.open_edit("BB-CRUD-Original")
    assert ui.heading() == "Edit Task"
    assert ui.task_form_values()["due_date"] == original_due  # pre-filled (TC-GUI-012)
    ui.fill_task_form("BB-CRUD-Edited", "Week 1 edited description", "Study", new_due)
    ui.submit_form()
    assert ui.titles() == ["BB-CRUD-Edited"]
    ui.open_edit("BB-CRUD-Edited")
    assert ui.task_form_values() == {
        "title": "BB-CRUD-Edited", "description": "Week 1 edited description",
        "category": "Study", "due_date": new_due,
    }


@pytest.mark.auto("TC-AUT-014")
@pytest.mark.manual("TC-BB-025")
@pytest.mark.req("REQ-003")
def test_cancel_edit_preserves_saved_data(ui, logged_in):
    logged_in["api"].create_task("BB-CRUD-Edited", "Week 1 edited description", "Study", iso_in(2))
    ui.open("/")
    ui.open_edit("BB-CRUD-Edited")
    saved = ui.task_form_values()
    ui.fill_task_form("BB-UNSAVED-DRAFT", "unsaved draft", "Urgent", iso_in(9))
    ui.cancel_task_form()
    assert ui.path == "/"
    assert ui.titles() == ["BB-CRUD-Edited"]
    ui.open_edit("BB-CRUD-Edited")
    assert ui.task_form_values() == saved


@pytest.mark.auto("TC-AUT-015")
@pytest.mark.manual("TC-BB-026", "TC-GUI-013")
@pytest.mark.req("REQ-003")
def test_cancel_deletion_retains_task(ui, logged_in):
    logged_in["api"].create_task("BB-MINIMAL")
    ui.open("/")
    dialog = ui.delete("BB-MINIMAL", confirm=False)
    assert dialog == "Delete this task?"
    ui.open("/")
    assert ui.titles() == ["BB-MINIMAL"]


@pytest.mark.smoke
@pytest.mark.auto("TC-AUT-016")
@pytest.mark.manual("TC-BB-027", "TC-GUI-013")
@pytest.mark.req("REQ-003")
def test_confirm_deletion_removes_only_that_task(ui, logged_in):
    api = logged_in["api"]
    api.create_task("BB-KEEP")
    api.create_task("BB-MINIMAL")
    ui.open("/")
    ui.delete("BB-MINIMAL", confirm=True)
    assert ui.titles() == ["BB-KEEP"]
    ui.driver.refresh()
    assert ui.titles() == ["BB-KEEP"], "deleted task reappeared after refresh"
    assert [t["title"] for t in api.tasks()] == ["BB-KEEP"]


@pytest.mark.smoke
@pytest.mark.auto("TC-AUT-017")
@pytest.mark.manual("TC-BB-028", "TC-BB-029", "TC-GUI-011")
@pytest.mark.req("REQ-004")
def test_complete_then_reopen_task(ui, logged_in):
    logged_in["api"].create_task("BB-CRUD-Edited", category="Study", due_date=iso_in(2))
    ui.open("/")
    before = ui.row("BB-CRUD-Edited")
    assert (before["toggle"], before["urgency"], before["done"]) == ("○", "Due Soon", False)

    ui.toggle("BB-CRUD-Edited")                       # TC-BB-028 Open -> Done
    done = ui.row("BB-CRUD-Edited")
    assert (done["toggle"], done["urgency"], done["done"]) == ("✓", "Done", True)

    ui.toggle("BB-CRUD-Edited")                       # TC-BB-029 Done -> Open
    reopened = ui.row("BB-CRUD-Edited")
    assert (reopened["toggle"], reopened["urgency"], reopened["done"]) == ("○", "Due Soon", False)


@pytest.mark.auto("TC-AUT-018")
@pytest.mark.manual("TC-GUI-020")
@pytest.mark.req("REQ-003")
def test_special_characters_preserved_in_edit_form(ui, logged_in):
    logged_in["api"].create_task(SPECIAL_TITLE)
    ui.open("/")
    ui.open_edit(ui.titles()[0])
    assert ui.task_form_values()["title"] == SPECIAL_TITLE


@pytest.mark.auto("TC-AUT-019")
@pytest.mark.manual("TC-GUI-020")
@pytest.mark.req("REQ-003")
@pytest.mark.known_defect("DEF-005")
def test_special_characters_displayed_literally_in_list(ui, logged_in):
    logged_in["api"].create_task(SPECIAL_TITLE)
    ui.open("/")
    shown = ui.titles()
    assert shown == [SPECIAL_TITLE], f"list shows {shown!r} instead of the saved title"


@pytest.mark.smoke
@pytest.mark.auto("TC-AUT-020")
@pytest.mark.manual("TC-BB-044")
@pytest.mark.req("REQ-008")
def test_each_account_sees_only_its_own_tasks(ui, new_account):
    account_a, account_b = new_account("a"), new_account("b")
    account_a["api"].create_task("BB-ACCOUNT-A-ONLY", category="Work")
    account_a["api"].create_task("BB-ACCOUNT-A-SECOND")
    account_b["api"].create_task("BB-ACCOUNT-B-ONLY", category="Personal")

    ui.login(account_b["username"], account_b["password"])
    assert ui.titles() == ["BB-ACCOUNT-B-ONLY"]
    ui.logout()
    ui.login(account_a["username"], account_a["password"])
    assert sorted(ui.titles()) == ["BB-ACCOUNT-A-ONLY", "BB-ACCOUNT-A-SECOND"]
