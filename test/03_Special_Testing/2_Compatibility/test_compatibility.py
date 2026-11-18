"""Task 2 - Compatibility smoke scenarios TC-CMP-001 to 008 (see test_cases.md).

Run once per configuration with `--w3-config <ID>`; evidence goes to
2_Compatibility/evidences/<os>-<browser>/<viewport>/ for that configuration.
The cases run in file order: TC-CMP-002 creates the task that 005 edits and
006 deletes.
"""

import json
from urllib.parse import urlparse

import pytest

from conftest import (
    PHASE_DIR, RUN_DATE, case_data, computed, create_task_ui, has_horizontal_scroll,
    iso_in, listed_titles, login, nav_layout, row_for, boxes_overlap, username_for,
)

shared = {}


def is_path(page, path):
    return urlparse(page.url).path == path


@pytest.mark.case("TC-CMP-001")
def test_cmp_001_register_login_logout(page, rec, w3_config):
    username = username_for(w3_config["id"].lower())
    password = "Test12345"
    page.goto("/register")
    page.fill("input[name=username]", username)
    page.fill("input[name=password]", password)
    with page.expect_navigation():
        page.click("button[type=submit]")
    nav_user = page.locator(".nav-user")
    rec.expect(is_path(page, "/") and page.locator("h1").inner_text() == "My Tasks"
               and nav_user.count() and nav_user.inner_text() == username,
               "register opens My Tasks with the username in the navigation bar", page.url)
    rec.capture(page, "registered")
    with page.expect_navigation():
        page.get_by_role("link", name="Log out").click()
    rec.expect(is_path(page, "/login"), "log out returns to /login", page.url)
    login(page, {"username": username, "password": password})
    rec.expect(is_path(page, "/") and page.locator("h1").inner_text() == "My Tasks", "log in opens My Tasks", page.url)
    rec.capture(page, "logged-in")
    rec.assert_all()


@pytest.mark.case("TC-CMP-002")
def test_cmp_002_create_task_with_date(page, rec, account_a):
    data = case_data("TC-CMP-002")
    due = iso_in(data["due_offset_days"])
    login(page, account_a)
    page.goto("/tasks/new")
    rec.expect(page.get_attribute("input[name=due_date]", "type") == "date", "due date is a native date control")
    rec.note("Automation enters the date through the control's value; the native picker UI cannot be "
             "driven or captured by Playwright, so picker usability is not covered by this run.")
    create_task_ui(page, data["title"], category=data["category"], due_date=due)
    row = row_for(page, data["title"])
    cells = [c.strip() for c in row.locator("td").all_inner_texts()]
    shown_due = cells[3] if len(cells) > 3 else None
    badge = row.locator(".badge").inner_text().strip() if row.count() else None
    rec.expect(row.count() == 1 and shown_due == due and badge == "Upcoming",
               f"CMP-Date listed with due date {due} and badge Upcoming", {"due": shown_due, "badge": badge})
    shared["cmp_due"] = due
    rec.capture(page, "created")
    rec.assert_all()


@pytest.mark.case("TC-CMP-003")
def test_cmp_003_filter_and_search(page, rec, account_a):
    data = case_data("TC-CMP-003")
    login(page, account_a)
    page.goto("/")
    applied = []
    for selector, value in (("select[name=category]", data["category"]), ("select[name=status]", data["status"])):
        try:
            with page.expect_navigation(timeout=5000):
                page.select_option(selector, value)
            applied.append(True)
        except Exception:
            applied.append(False)
    rec.expect(all(applied), "category and status apply on change without Filter", applied)
    page.fill("input[name=q]", data["q"])
    with page.expect_navigation():
        page.press("input[name=q]", "Enter")
    titles = listed_titles(page)
    rec.expect(titles == data["expected_titles"], "final list equals the C01 result (F1 only)", titles)
    rec.capture(page, "filtered")
    rec.assert_all()


@pytest.mark.case("TC-CMP-004")
def test_cmp_004_complete_and_reopen(page, rec, account_a):
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
    done = state()
    rec.expect(done == {"button": "✓", "strike": True, "badge": "Done"}, "after completing: ✓, struck through, Done", done)
    rec.capture(page, "done")
    with page.expect_navigation():
        row_for(page, title).locator("button.check-btn").click()
    reopened = state()
    rec.expect(reopened == {"button": "○", "strike": False, "badge": "Due Soon"},
               "after reopening: ○, no strikethrough, Due Soon", reopened)
    glyph_width = row_for(page, title).locator("button.check-btn").evaluate(
        "b => { const r = document.createRange(); r.selectNodeContents(b); return r.getBoundingClientRect().width; }")
    rec.expect(glyph_width > 0, "the ○/✓ symbols render as glyphs", f"glyph width {round(glyph_width, 1)}px")
    rec.capture(page, "reopened")
    rec.assert_all()


@pytest.mark.case("TC-CMP-005")
def test_cmp_005_edit_task(page, rec, account_a):
    title = case_data("TC-CMP-002")["title"]
    new_due = iso_in(case_data("TC-CMP-005")["new_due_offset_days"])
    login(page, account_a)
    page.goto("/")
    if not row_for(page, title).count():
        pytest.fail("CMP-Date from TC-CMP-002 is missing, so this case is blocked")
    with page.expect_navigation():
        row_for(page, title).get_by_role("link", name="Edit").click()
    shown = page.input_value("input[name=due_date]")
    rec.expect(shown == shared.get("cmp_due"), "edit form shows the saved date", shown)
    page.fill("input[name=due_date]", new_due)
    with page.expect_navigation():
        page.get_by_role("button", name="Save Changes").click()
    listed_due = row_for(page, title).locator("td").nth(3).inner_text().strip()
    rec.expect(listed_due == new_due, f"list shows the new date {new_due}", listed_due)
    with page.expect_navigation():
        row_for(page, title).get_by_role("link", name="Edit").click()
    reopened = page.input_value("input[name=due_date]")
    rec.expect(reopened == new_due, "edit form shows the new date", reopened)
    rec.capture(page, "edited")
    rec.assert_all()


@pytest.mark.case("TC-CMP-006")
def test_cmp_006_delete_with_confirmation(page, rec, account_a):
    title = case_data("TC-CMP-002")["title"]
    login(page, account_a)
    page.goto("/")
    if not row_for(page, title).count():
        pytest.fail("CMP-Date from TC-CMP-002 is missing, so this case is blocked")
    dialogs = []

    def handler(accept):
        def _handle(dialog):
            dialogs.append({"type": dialog.type, "message": dialog.message})
            dialog.accept() if accept else dialog.dismiss()
        return _handle

    page.once("dialog", handler(False))
    row_for(page, title).get_by_role("button", name="Delete").click()
    page.wait_for_timeout(300)
    rec.expect(dialogs and dialogs[0]["type"] == "confirm", "a confirmation dialog appears", dialogs)
    rec.expect(row_for(page, title).count() == 1, "Cancel keeps the task")
    page.once("dialog", handler(True))
    with page.expect_navigation():
        row_for(page, title).get_by_role("button", name="Delete").click()
    rec.expect(row_for(page, title).count() == 0, "confirming removes the task")
    rec.note(f"Native dialog text recorded by Playwright (not drawn in page screenshots): {dialogs}")
    rec.capture(page, "deleted")
    rec.assert_all()


@pytest.mark.case("TC-CMP-007")
def test_cmp_007_nav_and_table_layout(page, rec, account_a):
    login(page, account_a)
    page.goto("/")
    layout, overlaps = nav_layout(page)
    # With mobile emulation and no viewport meta tag (H1) the layout viewport is wider than the
    # device, so element positions are compared with the page's own layout width.
    viewport_width = page.evaluate("() => window.innerWidth")
    if viewport_width != page.viewport_size["width"]:
        rec.note(f"Device width {page.viewport_size['width']} CSS px, but the page is laid out at "
                 f"{viewport_width} CSS px and scaled down to fit (H1: no viewport meta tag).")
    wrapped = [f"{i['text']} ({i['lines']} lines)" for i in layout if i["lines"] > 1]
    offscreen = [i["text"] for i in layout if i["box"]["x"] + i["box"]["width"] > viewport_width + 1]
    rec.expect(not wrapped, "each nav item fits on one line", wrapped)
    rec.expect(not overlaps, "no nav items overlap", overlaps)
    rec.expect(not offscreen, "no nav item extends past the viewport", offscreen)
    headers = page.locator("table.task-table thead th")
    clipped = []
    for i in range(headers.count()):
        box = headers.nth(i).bounding_box()
        if box["x"] < 0 or box["x"] + box["width"] > viewport_width + 1:
            clipped.append(headers.nth(i).inner_text().strip() or f"column {i + 1}")
    rec.expect(not clipped, "all six table columns are within the viewport", clipped)
    # "Readable" is measured as the smallest nav/table text size as rendered on the device screen,
    # against Lighthouse's 12 px legibility threshold.
    scale = page.viewport_size["width"] / viewport_width
    smallest = page.evaluate("""() => Math.min(...[...document.querySelectorAll(
        'nav.topnav a, nav.topnav span, table.task-table th, table.task-table td, table.task-table .badge')]
        .filter(e => e.innerText.trim()).map(e => parseFloat(getComputedStyle(e).fontSize)))""")
    effective = round(smallest * scale, 1)
    rec.expect(effective >= 12, "smallest nav and table text renders at 12 px or more on the device screen",
               f"{effective} px ({smallest} px CSS x {round(scale, 3)} page scale)")
    scroll = has_horizontal_scroll(page)
    table_wider = page.evaluate(
        "() => document.querySelector('table.task-table').scrollWidth > document.querySelector('.container').clientWidth")
    rec.expect(not scroll or table_wider, "no horizontal page scroll, unless the table alone causes it",
               {"page scrolls": scroll, "table wider than container": table_wider})
    if scroll:
        rec.note(f"Page scrolls horizontally; table wider than its container: {table_wider}.")
    rec.capture(page, "layout")
    rec.assert_all()


@pytest.mark.case("TC-CMP-008")
def test_cmp_008_dashboard_layout(page, rec, account_a, w3_config):
    login(page, account_a)
    page.goto("/dashboard")
    cards = page.locator(".stat-card")
    boxes = [cards.nth(i).bounding_box() for i in range(cards.count())]
    overlaps = [(i + 1, j + 1) for i in range(len(boxes)) for j in range(i + 1, len(boxes))
                if boxes_overlap(boxes[i], boxes[j])]
    rec.expect(not overlaps, "the five cards do not overlap", overlaps)
    values = dict(zip(
        [t.strip() for t in page.locator(".stat-label").all_inner_texts()],
        [t.strip() for t in page.locator(".stat-value").all_inner_texts()],
    ))
    rec.note(f"Counter values on {RUN_DATE.isoformat()}: {values}")
    if w3_config["id"] != "C01":
        baseline = sorted((PHASE_DIR / "2_Compatibility/evidences/mac-chrome/desktop").glob(
            f"results-C01-{RUN_DATE:%Y%m%d}-*.json"))
        if baseline:
            c01 = json.loads(baseline[-1].read_text(encoding="utf-8"))["cases"].get("TC-CMP-008", {})
            c01_note = next((n for n in c01.get("notes", []) if n.startswith("Counter values")), "")
            rec.expect(str(values) in c01_note, "counter values equal C01 for the same day", c01_note)
        else:
            rec.note("No same-day C01 result found; compare with C01 values recalculated for this date.")
    rec.capture(page, "dashboard")
    rec.assert_all()
