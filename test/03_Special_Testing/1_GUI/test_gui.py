"""Task 1 - GUI checklist cases TC-GUI-001 to 022 (see test_cases.md).

Each test performs the case's steps, checks the expected result written in
test_cases.md before execution, and saves evidence to 1_GUI/evidences/.
Checks that need visual judgement (spacing, readability) are recorded as
notes and judged from the captured screenshot.
"""

from urllib.parse import urlparse

import pytest

from conftest import (
    BASE_URL, case_data, computed, create_task_ui, has_horizontal_scroll, listed_titles,
    login, nav_layout, row_for, text_lines, username_for,
)


@pytest.fixture(autouse=True)
def baseline_only(w3_config):
    if w3_config["id"] != "C01":
        pytest.skip("GUI cases run on the C01 baseline only; other configurations use TC-CMP")


def is_path(page, path):
    return urlparse(page.url).path == path


@pytest.mark.case("TC-GUI-001")
def test_gui_001_login_page_layout(page, rec):
    page.goto("/login")
    card = page.locator(".auth-card")
    heading = card.locator("h1").inner_text()
    rec.expect(heading == "Log in", "heading is 'Log in'", heading)
    for label_text, field in (("Username", "username"), ("Password", "password")):
        label_box = card.locator("label", has_text=label_text).bounding_box()
        input_box = card.locator(f"input[name={field}]").bounding_box()
        gap = round(input_box["y"] - (label_box["y"] + label_box["height"]), 1)
        rec.expect(0 <= gap <= 16 and abs(label_box["x"] - input_box["x"]) <= 2,
                   f"'{label_text}' label sits directly above its input", f"gap {gap}px")
    rec.expect(card.get_by_role("button", name="Log in").count() == 1, "'Log in' button present")
    muted = card.locator("p.muted")
    register = muted.get_by_role("link", name="Register")
    rec.expect("No account?" in muted.inner_text() and register.get_attribute("href") == "/register",
               "'No account? Register' links to /register", muted.inner_text())
    page.fill("input[name=password]", case_data("TC-GUI-001")["password"])
    rec.expect(page.get_attribute("input[name=password]", "type") == "password", "password characters are masked")
    rec.expect(card.locator("input, button, a").count() == 4, "all elements are inside one card",
               card.locator("input, button, a").count())
    rec.note("Spacing consistency judged from the screenshot.")
    rec.capture(page, "login-layout")
    rec.assert_all()


@pytest.mark.case("TC-GUI-002")
def test_gui_002_login_error_message(page, rec, account_a):
    page.goto("/login")
    page.fill("input[name=username]", account_a["username"])
    page.fill("input[name=password]", case_data("TC-GUI-002")["password"])
    with page.expect_navigation():
        page.click("button[type=submit]")
    rec.expect(is_path(page, "/login"), "browser stays on /login", page.url)
    error = page.locator(".auth-card .error")
    visible = error.count() == 1 and error.is_visible()
    rec.expect(visible, "an error message is shown")
    if visible:
        text = error.inner_text()
        box = error.bounding_box()
        form_box = page.locator(".auth-card form").bounding_box()
        rec.expect(box["y"] < form_box["y"], "error is above the form", text)
        bg = computed(error, "backgroundColor")["backgroundColor"]
        card_bg = computed(page.locator(".auth-card"), "backgroundColor")["backgroundColor"]
        rec.expect(bg != card_bg, "error box is visually distinct from the card", bg)
        lower = text.lower()
        rec.expect(("username" in lower) == ("password" in lower),
                   "message does not reveal which field was wrong", text)
    retained = page.input_value("input[name=username]")
    rec.note(f"Observation for Task 3: username field after the error contains '{retained}'.")
    rec.capture(page, "login-error")
    rec.assert_all()


@pytest.mark.case("TC-GUI-003")
def test_gui_003_registration_hints(page, rec):
    page.goto("/register")
    card = page.locator(".auth-card")
    heading = card.locator("h1").inner_text()
    rec.expect(heading == "Create an account", "heading is 'Create an account'", heading)
    for label_text, hint in (("Username", "(3-20 chars, letters/numbers/underscore)"),
                             ("Password", "(min 8 characters)")):
        label = card.locator("label", has_text=label_text)
        rec.expect(hint in label.inner_text(), f"{label_text} label shows the hint {hint}", label.inner_text())
        size = computed(label.locator(".hint"), "fontSize")["fontSize"]
        rec.note(f"{label_text} hint font size {size}; readability judged from the screenshot.")
    rec.expect(card.get_by_role("button", name="Register").count() == 1, "'Register' button present")
    rec.expect(card.get_by_role("link", name="Log in").get_attribute("href") == "/login", "'Log in' link to /login")
    rec.capture(page, "register-hints")
    rec.assert_all()


@pytest.mark.case("TC-GUI-004")
def test_gui_004_registration_error_messages(page, rec):
    data = case_data("TC-GUI-004")
    submissions = [
        ("s1", data["submission1"]["username"], data["submission1"]["password"]),
        ("s2", username_for(data["submission2"]["username_purpose"]), data["submission2"]["password"]),
        ("s3", username_for(data["submission3"]["username_purpose"]), data["submission3"]["password"]),
    ]
    login_error_style = None
    for label, username, password in submissions:
        page.goto("/register")
        page.fill("input[name=username]", username)
        page.fill("input[name=password]", password)
        with page.expect_navigation():
            page.click("button[type=submit]")
        error = page.locator(".auth-card .error")
        message = error.inner_text() if error.count() else None
        if label == "s1":
            rec.expect(is_path(page, "/register") and message and "3-20" in message,
                       "s1: stays on /register with the username rule", message)
        elif label == "s2":
            rec.expect(is_path(page, "/register") and message and "8" in message,
                       "s2 (7 chars): stays on /register with the 8-character minimum", message)
        else:
            heading = page.locator("h1").inner_text()
            rec.expect(is_path(page, "/") and heading == "My Tasks",
                       "s3 (8 chars): accepted and shows My Tasks", message or heading)
        if message:
            style = computed(error, "backgroundColor", "color")
            login_error_style = login_error_style or style
            rec.note(f"{label}: username field kept '{page.input_value('input[name=username]')}', "
                     f"password field kept {len(page.input_value('input[name=password]'))} characters.")
        rec.capture(page, f"register-errors-{label}")
    page.goto("/logout")
    page.goto("/login")
    page.fill("input[name=username]", "nobody_w3")
    page.fill("input[name=password]", "WrongPass1")
    with page.expect_navigation():
        page.click("button[type=submit]")
    login_style = computed(page.locator(".auth-card .error"), "backgroundColor", "color")
    rec.expect(login_error_style == login_style, "register messages use the same style as the login error",
               {"register": login_error_style, "login": login_style})
    rec.assert_all()


@pytest.mark.case("TC-GUI-005")
def test_gui_005_navigation_bar(page, rec, account_a):
    page.goto("/login")
    rec.expect(page.locator("nav.topnav .nav-links").count() == 0
               and page.locator("nav.topnav .brand").inner_text() == "PyTodo Pro",
               "logged out: brand only")
    rec.capture(page, "nav-logged-out")
    login(page, account_a)
    expected = ["Tasks", "Dashboard", account_a["username"], "Log out"]
    narrow = case_data("TC-GUI-005")["narrow_viewport"]
    for width_label, viewport in (("1440", {"width": 1440, "height": 900}), ("390", narrow)):
        page.set_viewport_size(viewport)
        for path in ("/", "/tasks/new", "/dashboard"):
            page.goto(path)
            items = [t.strip() for t in page.locator("nav.topnav .nav-links > *").all_inner_texts()]
            rec.expect(items == expected, f"{width_label}px {path}: nav shows {expected}", items)
            layout, overlaps = nav_layout(page)
            wrapped = [f"{i['text']} ({i['lines']} lines)" for i in layout if i["lines"] > 1]
            rec.expect(not wrapped, f"{width_label}px {path}: every nav item on one line", wrapped)
            rec.expect(not overlaps, f"{width_label}px {path}: no nav items overlap", overlaps)
        rec.capture(page, f"nav-{width_label}", full_page=False)
    rec.assert_all()


@pytest.mark.case("TC-GUI-006")
def test_gui_006_brand_link(page, rec, account_a):
    login(page, account_a)
    page.goto("/dashboard")
    with page.expect_navigation():
        page.click("nav.topnav .brand")
    rec.expect(is_path(page, "/"), "logged in: brand opens the task list /", page.url)
    with page.expect_navigation():
        page.get_by_role("link", name="Log out").click()
    with page.expect_navigation():
        page.click("nav.topnav .brand")
    rec.expect(is_path(page, "/login"), "logged out: brand stays on /login", page.url)
    rec.capture(page, "brand-link")
    rec.assert_all()


@pytest.mark.case("TC-GUI-007")
def test_gui_007_task_list_header(page, rec, account_a):
    login(page, account_a)
    page.goto("/")
    heading = page.locator(".page-header h1")
    button = page.locator(".page-header a.btn")
    hb, bb = heading.bounding_box(), button.bounding_box()
    rec.expect(heading.inner_text() == "My Tasks", "heading 'My Tasks'", heading.inner_text())
    rec.expect(button.inner_text().strip() == "+ New Task", "'+ New Task' button", button.inner_text())
    same_row = abs((hb["y"] + hb["height"] / 2) - (bb["y"] + bb["height"] / 2)) <= 12
    rec.expect(same_row and hb["x"] < bb["x"], "heading on the left, button on the right of the same row")
    rec.capture(page, "list-header", full_page=False)
    with page.expect_navigation():
        button.click()
    rec.expect(is_path(page, "/tasks/new") and page.locator("h1").inner_text() == "New Task",
               "'+ New Task' opens /tasks/new with heading 'New Task'", page.url)
    rec.assert_all()


@pytest.mark.case("TC-GUI-008")
def test_gui_008_filter_controls(page, rec, account_a):
    data = case_data("TC-GUI-008")
    login(page, account_a)
    page.goto("/")
    try:
        with page.expect_navigation(timeout=5000):
            page.select_option("select[name=category]", data["category"])
        rec.expect(True, "category applies on change, without Filter")
    except Exception:
        rec.expect(False, "category applies on change, without Filter", "no reload")
    try:
        with page.expect_navigation(timeout=5000):
            page.select_option("select[name=status]", data["status"])
        rec.expect(True, "status applies on change, without Filter")
    except Exception:
        rec.expect(False, "status applies on change, without Filter", "no reload")
    page.fill("input[name=q]", data["q"])
    with page.expect_navigation():
        page.press("input[name=q]", "Enter")
    titles = listed_titles(page)
    rec.expect(titles == data["expected_titles"], "after Enter: only F1 is listed", titles)
    rec.expect(page.input_value("select[name=category]") == data["category"]
               and page.input_value("select[name=status]") == data["status"]
               and page.input_value("input[name=q]") == data["q"],
               "controls still show Work / Open / GUI after reload")
    rec.capture(page, "filters-applied")
    page.fill("input[name=q]", "")
    with page.expect_navigation():
        page.click("form.filters button[type=submit]")
    rec.expect("q=" in page.url and page.input_value("input[name=q]") == "", "Filter button applies the search")
    page.reload()
    rec.expect(page.input_value("select[name=category]") == data["category"]
               and page.input_value("select[name=status]") == data["status"],
               "category and status persist after a page reload")
    labels = page.locator("form.filters label").count()
    rec.note(f"Input for TC-A11Y-006: the filter form has {labels} visible <label> elements; "
             f"search placeholder is '{page.get_attribute('input[name=q]', 'placeholder')}'.")
    rec.assert_all()


@pytest.mark.case("TC-GUI-009")
def test_gui_009_task_table_and_empty_state(page, rec, account_a, account_c, browser):
    login(page, account_a)
    page.goto("/")
    headers = [h.strip() for h in page.locator("table.task-table thead th").all_inner_texts()]
    rec.expect(all(h in headers for h in ("Title", "Category", "Due Date", "Urgency")),
               "Title, Category, Due Date and Urgency have headers", headers)
    first_col = page.locator("table.task-table tbody tr td:first-child button.check-btn").count()
    last_col = page.locator("table.task-table tbody tr td:last-child", has_text="Edit").count()
    rows = page.locator("table.task-table tbody tr").count()
    rec.expect(first_col == rows and last_col == rows, "control columns identifiable by their controls",
               {"rows": rows, "toggle buttons": first_col, "edit/delete cells": last_col})
    rec.note(f"Header texts of the control columns: first '{headers[0]}', last '{headers[-1]}'.")
    page.goto("/?q=" + case_data("TC-GUI-009")["q"])
    body_rows = page.locator("table.task-table tbody tr")
    message = body_rows.first.inner_text().strip()
    rec.expect(body_rows.count() == 1 and "no tasks match" in message.lower(),
               "no-match search shows a single 'no tasks match' message", message)
    rec.capture(page, "empty-search")
    context = browser.new_context(base_url=BASE_URL, viewport={"width": 1440, "height": 900})
    page_c = context.new_page()
    login(page_c, account_c)
    page_c.goto("/")
    body_rows = page_c.locator("table.task-table tbody tr")
    message = body_rows.first.inner_text().strip()
    rec.expect(body_rows.count() == 1 and "no tasks match" in message.lower(),
               "empty account shows a single 'no tasks match' message", message)
    rec.capture(page_c, "empty-account")
    context.close()
    rec.assert_all()


@pytest.mark.case("TC-GUI-010")
def test_gui_010_urgency_badges(page, rec, account_a):
    expected = case_data("TC-GUI-010")["expected"]
    login(page, account_a)
    page.goto("/")
    styles = {}
    for fixture_id, urgency in expected.items():
        title = account_a["tasks"][fixture_id]["title"]
        badge = row_for(page, title).locator(".badge")
        text = badge.inner_text().strip()
        rec.expect(text == urgency, f"{fixture_id} badge reads '{urgency}'", text)
        # Key by the text actually shown: a misclassified badge must not be compared as another class.
        styles.setdefault(text, tuple(computed(badge, "backgroundColor", "color").values()))
    distinct = [u for u in ("Overdue", "Due Today", "Due Soon", "Upcoming") if u in styles]
    clashes = [(a, b) for i, a in enumerate(distinct) for b in distinct[i + 1:] if styles[a] == styles[b]]
    rec.expect(not clashes, "the urgency classes displayed look different from each other", clashes)
    missing = [u for u in ("Overdue", "Due Today", "Due Soon", "Upcoming") if u not in styles]
    if missing:
        rec.note(f"Not displayed for any fixture, so their appearance could not be compared: {missing}")
    rec.note(f"Badge colours (background, text) by displayed class: {styles}")
    rec.capture(page, "badges")
    rec.assert_all()


@pytest.mark.case("TC-GUI-011")
def test_gui_011_complete_and_reopen_button(page, rec, account_a):
    title = account_a["tasks"]["F3"]["title"]
    login(page, account_a)
    page.goto("/")

    def state():
        row = row_for(page, title)
        return {
            "button": row.locator("button.check-btn").inner_text().strip(),
            "strike": "line-through" in computed(row.locator("td.title-cell"), "textDecorationLine")["textDecorationLine"],
            "badge": row.locator(".badge").inner_text().strip(),
        }

    with page.expect_navigation():
        row_for(page, title).locator("button.check-btn").click()
    after_complete = state()
    rec.expect(after_complete == {"button": "✓", "strike": True, "badge": "Done"},
               "after completing: ✓, struck through, Done", after_complete)
    rec.capture(page, "toggle-done")
    with page.expect_navigation():
        row_for(page, title).locator("button.check-btn").click()
    after_reopen = state()
    rec.expect(after_reopen == {"button": "○", "strike": False, "badge": "Due Soon"},
               "after reopening: ○, no strikethrough, Due Soon", after_reopen)
    rec.capture(page, "toggle-open")
    rec.assert_all()


@pytest.mark.case("TC-GUI-012")
def test_gui_012_edit_link_prefills_form(page, rec, account_a):
    f3 = account_a["tasks"]["F3"]
    login(page, account_a)
    page.goto("/")
    with page.expect_navigation():
        row_for(page, f3["title"]).get_by_role("link", name="Edit").click()
    values = {
        "title": page.input_value("input[name=title]"),
        "description": page.input_value("textarea[name=description]"),
        "category": page.locator("select[name=category_id] option:checked").inner_text().strip(),
        "due_date": page.input_value("input[name=due_date]"),
    }
    want = {"title": f3["title"], "description": f3["description"], "category": f3["category"],
            "due_date": f3["due_date"]}
    rec.expect(values == want, "form pre-filled with F3's saved values", values)
    rec.capture(page, "edit-prefill")
    rec.assert_all()


@pytest.mark.case("TC-GUI-013")
def test_gui_013_delete_confirmation(page, rec, account_a):
    title = case_data("TC-GUI-013")["title"]
    login(page, account_a)
    create_task_ui(page, title)
    others_before = [t for t in listed_titles(page) if t != title]
    rec.capture(page, "before-delete")
    dialogs = []

    def answer(accept):
        def handler(dialog):
            dialogs.append({"type": dialog.type, "message": dialog.message})
            dialog.accept() if accept else dialog.dismiss()
        return handler

    page.once("dialog", answer(False))
    row_for(page, title).get_by_role("button", name="Delete").click()
    page.wait_for_timeout(300)
    rec.expect(dialogs and dialogs[0]["type"] == "confirm" and "delete" in dialogs[0]["message"].lower(),
               "a confirmation dialog asks whether to delete (OK/Cancel)", dialogs)
    rec.expect(row_for(page, title).count() == 1, "after Cancel the task is still listed")
    page.once("dialog", answer(True))
    with page.expect_navigation():
        row_for(page, title).get_by_role("button", name="Delete").click()
    rec.expect(row_for(page, title).count() == 0, "after OK the task is removed")
    rec.expect(listed_titles(page) == others_before, "all other tasks unchanged")
    rec.note(f"Native dialog text recorded by Playwright (dialogs are not drawn in page screenshots): {dialogs}")
    rec.capture(page, "after-delete")
    rec.assert_all()


@pytest.mark.case("TC-GUI-014")
def test_gui_014_new_task_form(page, rec, account_a):
    data = case_data("TC-GUI-014")
    login(page, account_a)
    page.goto("/tasks/new")
    form = page.locator("form.task-form")
    rec.expect(page.locator("h1").inner_text() == "New Task", "heading 'New Task'")
    labels = [t.strip() for t in form.locator("label").all_inner_texts()]
    rec.expect(labels == ["Title", "Description", "Category", "Due Date"], "four labelled fields", labels)
    rec.expect(form.locator("textarea[name=description]").count() == 1, "Description is multi-line")
    options = [o.strip() for o in form.locator("select[name=category_id] option").all_inner_texts()]
    rec.expect(options[0] == "None" and sorted(options[1:]) == sorted(data["expected_categories"]),
               "Category offers None plus Work, Personal, Study, Urgent", options)
    rec.expect(form.locator("input[name=due_date]").get_attribute("type") == "date",
               "Due Date is a date control (opens the browser's date picker)")
    rec.note("The native date picker cannot be opened or captured by automation; the control type is checked instead.")
    primary = form.get_by_role("button", name="Create Task")
    secondary = form.get_by_role("link", name="Cancel")
    rec.expect(primary.count() == 1 and secondary.count() == 1, "Create Task and Cancel present")
    p_bg = computed(primary, "backgroundColor")["backgroundColor"]
    s_bg = computed(secondary, "backgroundColor")["backgroundColor"]
    rec.expect(p_bg != s_bg, "Create Task styled as primary, Cancel as secondary", {"primary": p_bg, "secondary": s_bg})
    rec.capture(page, "new-form")
    page.fill("input[name=title]", data["title"])
    with page.expect_navigation():
        secondary.click()
    rec.expect(is_path(page, "/") and data["title"] not in listed_titles(page),
               "Cancel returns to / without creating the task", page.url)
    rec.assert_all()


@pytest.mark.case("TC-GUI-015")
def test_gui_015_edit_task_form(page, rec, account_a):
    data = case_data("TC-GUI-015")
    original = account_a["tasks"][data["fixture"]]["title"]
    login(page, account_a)

    def open_edit(title):
        page.goto("/")
        with page.expect_navigation():
            row_for(page, title).get_by_role("link", name="Edit").click()

    open_edit(original)
    rec.expect(page.locator("h1").inner_text() == "Edit Task", "heading 'Edit Task'")
    rec.expect(page.get_by_role("button", name="Save Changes").count() == 1
               and page.get_by_role("button", name="Create Task").count() == 0,
               "'Save Changes' replaces 'Create Task'")
    rec.capture(page, "edit-form")
    page.fill("input[name=title]", data["new_title"])
    with page.expect_navigation():
        page.get_by_role("link", name="Cancel").click()
    rec.expect(original in listed_titles(page) and data["new_title"] not in listed_titles(page),
               "after Cancel the title is unchanged")
    open_edit(original)
    page.fill("input[name=title]", data["new_title"])
    with page.expect_navigation():
        page.get_by_role("button", name="Save Changes").click()
    rec.expect(data["new_title"] in listed_titles(page), "after Save the new title is listed")
    rec.capture(page, "after-save")
    open_edit(data["new_title"])
    page.fill("input[name=title]", original)
    with page.expect_navigation():
        page.get_by_role("button", name="Save Changes").click()
    rec.note("F4 title restored to its fixture value after the case.")
    rec.assert_all()


@pytest.mark.case("TC-GUI-016")
def test_gui_016_required_title(page, rec, account_a, api_as):
    login(page, account_a)
    page.goto("/")
    rows_before = len(listed_titles(page))
    page.goto("/tasks/new")
    page.click("form.task-form button[type=submit]")
    page.wait_for_timeout(300)
    validity = page.locator("input[name=title]").evaluate(
        "el => ({missing: el.validity.valueMissing, message: el.validationMessage})")
    rec.expect(validity["missing"] and validity["message"] and is_path(page, "/tasks/new"),
               "empty title: blocked with a validation message on Title", validity)
    rec.note("The browser's validation bubble is not drawn in page screenshots; its text is recorded instead.")
    rec.capture(page, "empty-title")
    page.fill("input[name=title]", "   ")
    page.click("form.task-form button[type=submit]")
    page.wait_for_load_state()
    page.wait_for_timeout(300)
    blocked = is_path(page, "/tasks/new")
    page.goto("/")
    rows_after = len(listed_titles(page))
    rec.expect(blocked and rows_after == rows_before,
               "whitespace-only title: blocked and no task created",
               {"stayed on form": blocked, "rows before": rows_before, "rows after": rows_after})
    rec.capture(page, "whitespace-title")
    api = api_as(account_a)
    for task in api.get("/api/tasks?per_page=100").json():
        if not task["title"].strip():
            api.delete(f"/api/tasks/{task['id']}")
            rec.note(f"Cleanup: removed blank-title task {task['id']} created by this case.")
    rec.assert_all()


FEEDBACK_JS = """() => {
  const sel = '[role=status],[role=alert],.flash,.flashes,.alert,.message,.notice,.success,.toast';
  const el = [...document.querySelectorAll(sel)].find(e => e.offsetParent !== null && e.innerText.trim());
  return el ? el.innerText.trim() : null;
}"""


@pytest.mark.case("TC-GUI-017")
def test_gui_017_feedback_after_actions(page, rec, account_a):
    data = case_data("TC-GUI-017")
    login(page, account_a)

    def feedback(action, title=None):
        message = page.evaluate(FEEDBACK_JS)
        highlighted = False
        if title and row_for(page, title).count():
            row_bg = computed(row_for(page, title), "backgroundColor")["backgroundColor"]
            other = page.locator("table.task-table tbody tr").filter(has_not_text=title).first
            highlighted = row_bg != computed(other, "backgroundColor")["backgroundColor"]
        rec.expect(bool(message) or highlighted, f"after {action}: confirmation message or highlighted task",
                   {"message": message, "highlighted": highlighted})
        rec.capture(page, f"feedback-{action}")

    create_task_ui(page, data["title"])
    feedback("create", data["title"])
    with page.expect_navigation():
        row_for(page, data["title"]).get_by_role("link", name="Edit").click()
    page.fill("input[name=title]", data["edited_title"])
    with page.expect_navigation():
        page.get_by_role("button", name="Save Changes").click()
    feedback("edit", data["edited_title"])
    with page.expect_navigation():
        row_for(page, data["edited_title"]).locator("button.check-btn").click()
    feedback("complete", data["edited_title"])
    page.once("dialog", lambda d: d.accept())
    with page.expect_navigation():
        row_for(page, data["edited_title"]).get_by_role("button", name="Delete").click()
    feedback("delete")
    rec.note("No stated requirement covers this case; a failure is logged as a USA-OBS item, not a DEF.")
    rec.assert_all()


@pytest.mark.case("TC-GUI-018")
def test_gui_018_dashboard_cards(page, rec, account_a):
    login(page, account_a)
    page.goto("/")
    badge_colours = {}
    for cls in ("overdue", "due-soon", "done"):
        badge = page.locator(f".badge-{cls}").first
        if badge.count():
            badge_colours[cls] = computed(badge, "color")["color"]
    page.goto("/dashboard")
    rec.expect(page.locator("h1").inner_text() == "Dashboard", "heading 'Dashboard'")
    labels = [t.strip() for t in page.locator(".stat-card .stat-label").all_inner_texts()]
    rec.expect(labels == case_data("TC-GUI-018")["labels"], "five cards with the expected labels", labels)
    cards = page.locator(".stat-card")
    above = all(
        cards.nth(i).locator(".stat-value").bounding_box()["y"] < cards.nth(i).locator(".stat-label").bounding_box()["y"]
        for i in range(cards.count())
    )
    rec.expect(above, "each number sits above its label")
    pairs = {"Overdue": "overdue", "Due Soon": "due-soon", "Completed (last 7 days)": "done"}
    for label, cls in pairs.items():
        card_colour = computed(cards.filter(has_text=label).locator(".stat-value"), "color")["color"]
        rec.expect(card_colour == badge_colours.get(cls), f"'{label}' card uses the colour of the {cls} badge",
                   {"card": card_colour, "badge": badge_colours.get(cls)})
    rec.note("Counter values are not judged here (REQ-007 is covered in Week 1).")
    rec.capture(page, "dashboard")
    rec.assert_all()


@pytest.mark.case("TC-GUI-019")
def test_gui_019_long_content(page, rec, account_a):
    login(page, account_a)
    page.goto("/")
    f7 = row_for(page, account_a["tasks"]["F7"]["title"][:30]).locator("td.title-cell")
    f8 = row_for(page, account_a["tasks"]["F8"]["title"]).locator("td.title-cell")
    rec.expect(text_lines(f7) > 1, "F7 wraps within the Title cell", f"{text_lines(f7)} lines")
    table = page.locator("table.task-table").bounding_box()
    container = page.locator(".container").bounding_box()
    padding = float(computed(page.locator(".container"), "paddingRight")["paddingRight"].removesuffix("px"))
    inner_right = container["x"] + container["width"] - padding
    rec.expect(table["x"] + table["width"] <= inner_right + 1, "table stays inside the page container",
               {"table right": round(table["x"] + table["width"]), "container right": round(inner_right)})
    f8_box = f8.bounding_box()
    rec.note(f"F8 title cell width {round(f8_box['width'])}px, {text_lines(f8)} line(s).")
    scroll = has_horizontal_scroll(page)
    rec.expect(not scroll, "no horizontal page scroll at 1440px", scroll)
    rec.capture(page, "long-content")
    rec.assert_all()


@pytest.mark.case("TC-GUI-020")
def test_gui_020_special_characters(page, rec, account_a):
    f9 = account_a["tasks"]["F9"]
    login(page, account_a)
    page.goto("/")
    cell = row_for(page, "GUI-Special").locator("td.title-cell")
    shown = cell.inner_text().strip()
    markup = cell.locator("b").count()
    rec.expect(shown == f9["title"], "list shows the exact title, including the literal <b>bold</b> text", shown)
    rec.expect(markup == 0, "no bold formatting applied", f"{markup} <b> element(s)")
    rec.capture(page, "special-list")
    with page.expect_navigation():
        row_for(page, "GUI-Special").get_by_role("link", name="Edit").click()
    value = page.input_value("input[name=title]")
    rec.expect(value == f9["title"], "edit form shows the exact title", value)
    rec.capture(page, "special-edit")
    if markup:
        rec.note("Tags rendered as markup: add to the Week 5 STRIDE table (H9). No script payloads were used.")
    rec.assert_all()


@pytest.mark.case("TC-GUI-021")
def test_gui_021_page_titles(page, rec, account_a):
    pages = [("/login", "log in"), ("/register", "register")]
    titles = {}
    for path, _ in pages:
        page.goto(path)
        titles[path] = page.title()
    login(page, account_a)
    edit_path = f"/tasks/{account_a['tasks']['F3']['task_id']}/edit"
    for path, keyword in (("/", "task"), ("/tasks/new", "new task"), (edit_path, "edit task"), ("/dashboard", "dashboard")):
        pages.append((path, keyword))
        page.goto(path)
        titles[path] = page.title()
    rec.expect(len(set(titles.values())) == 6, "six different titles", titles)
    for path, keyword in pages:
        title = titles[path]
        rec.expect(keyword in title.lower() and "pytodo pro" in title.lower(),
                   f"{path} title names its page and the application", title)
    rec.note(f"Recorded titles: {titles}")
    rec.assert_all()


@pytest.mark.case("TC-GUI-022")
def test_gui_022_visual_consistency(page, rec, account_a):
    props = ("backgroundColor", "color", "borderRadius", "fontSize")
    styles = {}
    page.goto("/login")
    styles["Log in button"] = computed(page.get_by_role("button", name="Log in"), *props)
    login_h1 = computed(page.locator("h1"), "fontSize")["fontSize"]
    auth_link = computed(page.get_by_role("link", name="Register"), "color")["color"]
    auth_radius = computed(page.locator(".auth-card"), "borderRadius")["borderRadius"]
    rec.capture(page, "consistency-login")
    page.goto("/register")
    styles["Register button"] = computed(page.get_by_role("button", name="Register"), *props)
    rec.capture(page, "consistency-register")
    login(page, account_a)
    page.goto("/")
    styles["+ New Task"] = computed(page.locator(".page-header a.btn"), *props)
    styles["Filter"] = computed(page.locator("form.filters button"), *props)
    list_h1 = computed(page.locator("h1"), "fontSize")["fontSize"]
    edit_link = computed(page.get_by_role("link", name="Edit").first, "color")["color"]
    delete_btn = computed(page.get_by_role("button", name="Delete").first, "color")["color"]
    rec.capture(page, "consistency-list")
    page.goto("/tasks/new")
    styles["Create Task"] = computed(page.get_by_role("button", name="Create Task"), *props)
    form_radius = computed(page.locator("form.task-form"), "borderRadius")["borderRadius"]
    rec.capture(page, "consistency-new")
    page.goto(f"/tasks/{account_a['tasks']['F3']['task_id']}/edit")
    styles["Save Changes"] = computed(page.get_by_role("button", name="Save Changes"), *props)
    rec.capture(page, "consistency-edit")
    page.goto("/dashboard")
    card_radius = computed(page.locator(".stat-card").first, "borderRadius")["borderRadius"]
    rec.capture(page, "consistency-dashboard")

    variants = {}
    for name, style in styles.items():
        variants.setdefault(tuple(style.values()), []).append(name)
    rec.expect(len(variants) == 1, "all primary actions share one style",
               {", ".join(names): dict(zip(props, key)) for key, names in variants.items()})
    rec.expect(len({edit_link, delete_btn, auth_link}) == 1, "text-style actions look alike",
               {"Edit": edit_link, "Delete": delete_btn, "Register link": auth_link})
    rec.expect(login_h1 == list_h1, "top-level headings have the same size", {"login": login_h1, "task list": list_h1})
    rec.expect(len({auth_radius, form_radius, card_radius}) == 1, "cards share one style (corner radius)",
               {"auth card": auth_radius, "task form": form_radius, "stat card": card_radius})
    rec.note("Only one secondary action (Cancel) exists, on both task forms, so it is consistent by construction.")
    rec.assert_all()
