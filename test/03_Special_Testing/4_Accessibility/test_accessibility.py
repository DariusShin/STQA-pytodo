"""Task 4 - Accessibility cases TC-A11Y-001 to 018 (see test_cases.md).

Runs on the C01 baseline. Accessible names, roles and landmarks are read from
Chrome's accessibility tree; screen readers are out of scope. Automated scans
(axe-core, Lighthouse) are saved to evidences/reports/.
"""

import json
import re
import subprocess
from datetime import timedelta
from urllib.parse import urlparse

import pytest
from axe_playwright_python.sync_playwright import Axe

from conftest import (
    BASE_URL, PHASE_DIR, RUN_DATE, case_data, computed, has_horizontal_scroll,
    login, nav_layout, row_for,
)

REPORTS = PHASE_DIR / "4_Accessibility/evidences/reports"
AUTH_PAGES = ["/login", "/register"]


@pytest.fixture(autouse=True)
def baseline_only(w3_config):
    if w3_config["id"] != "C01":
        pytest.skip("Accessibility cases run on the C01 baseline only")


def app_pages(account):
    f3 = account["tasks"]["F3"]["task_id"]
    return ["/", "/tasks/new", f"/tasks/{f3}/edit", "/dashboard"]


def ax_nodes(page):
    """Chrome's accessibility tree for the current page: list of (role, name, node)."""
    cdp = page.context.new_cdp_session(page)
    try:
        nodes = cdp.send("Accessibility.getFullAXTree")["nodes"]
    finally:
        cdp.detach()
    out = []
    for node in nodes:
        if node.get("ignored"):
            continue
        role = node.get("role", {}).get("value", "")
        name = node.get("name", {}).get("value", "")
        out.append((role, name, node))
    return out


CONTRAST_JS = """el => {
  const parse = c => (c.match(/[\\d.]+/g) || []).map(Number);
  const lum = ([r, g, b]) => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
                               return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  let bg = null, node = el;
  while (node && node.nodeType === 1) {
    const c = parse(getComputedStyle(node).backgroundColor);
    if (c.length === 3 || (c.length === 4 && c[3] > 0)) { bg = c.slice(0, 3); break; }
    node = node.parentElement;
  }
  bg = bg || [255, 255, 255];
  const fg = parse(getComputedStyle(el).color).slice(0, 3);
  const [a, b] = [lum(fg), lum(bg)].sort((x, y) => y - x);
  const size = parseFloat(getComputedStyle(el).fontSize), weight = parseInt(getComputedStyle(el).fontWeight);
  return { ratio: Math.round((a + 0.05) / (b + 0.05) * 100) / 100, size, weight,
           large: size >= 24 || (size >= 18.66 && weight >= 700) };
}"""


@pytest.mark.case("TC-A11Y-001")
def test_a11y_001_non_text_content(page, rec, account_a):
    found = {}
    for path in AUTH_PAGES:
        page.goto(path)
        found[path] = [(r, n) for r, n, _ in ax_nodes(page) if r in ("button", "link", "img", "image")
                       and not re.search(r"[A-Za-z]", n or "")]
    login(page, account_a)
    for path in app_pages(account_a):
        page.goto(path)
        found[path] = [(r, n) for r, n, _ in ax_nodes(page) if r in ("button", "link", "img", "image")
                       and not re.search(r"[A-Za-z]", n or "")]
    for path, items in found.items():
        rec.expect(not items, f"{path}: every symbol-only control or image has a name describing its purpose",
                   sorted(set(items)))
    page.goto("/")
    rec.capture(page, "names")
    rec.assert_all()


@pytest.mark.case("TC-A11Y-002")
def test_a11y_002_info_and_relationships(page, rec, account_a):
    def check(path):
        h1 = page.locator("h1")
        nodes = ax_nodes(page)
        roles = {r for r, _, _ in nodes}
        rec.expect(h1.count() == 1, f"{path}: one top-level heading", h1.count())
        rec.expect("navigation" in roles and "main" in roles,
                   f"{path}: navigation and main content are identifiable regions",
                   sorted(r for r in roles if r in ("navigation", "main", "banner", "contentinfo")))
        if path == "/":
            headers = [n for r, n, _ in nodes if r == "columnheader"]
            rec.expect(len(headers) == 6, "/: table column headings are header cells", headers)

    for path in AUTH_PAGES:
        page.goto(path)
        check(path)
    login(page, account_a)
    for path in app_pages(account_a):
        page.goto(path)
        check(path)
    page.goto("/")
    rec.capture(page, "structure")
    rec.assert_all()


@pytest.mark.case("TC-A11Y-003")
def test_a11y_003_use_of_colour(page, rec, account_a):
    login(page, account_a)
    cdp = page.context.new_cdp_session(page)
    cdp.send("Emulation.setEmulatedVisionDeficiency", {"type": "achromatopsia"})
    page.goto("/")
    for fixture_id in ("F1", "F3", "F4", "F5", "F6"):
        badge = row_for(page, account_a["tasks"][fixture_id]["title"]).locator(".badge").inner_text().strip()
        rec.expect(bool(badge), f"{fixture_id}: urgency identifiable from its badge text", badge)
    done_row = row_for(page, account_a["tasks"]["F6"]["title"])
    strike = "line-through" in computed(done_row.locator("td.title-cell"), "textDecorationLine")["textDecorationLine"]
    rec.expect(done_row.locator("button.check-btn").inner_text().strip() == "✓" and strike,
               "completed task identifiable by symbol and strikethrough, not colour alone")
    rec.capture(page, "greyscale-list")
    page.goto("/dashboard")
    labels = [t.strip() for t in page.locator(".stat-label").all_inner_texts()]
    rec.expect(all(labels) and len(labels) == 5, "dashboard cards identifiable by their labels", labels)
    rec.capture(page, "greyscale-dashboard")
    cdp.send("Emulation.setEmulatedVisionDeficiency", {"type": "none"})
    cdp.detach()
    rec.assert_all()


@pytest.mark.case("TC-A11Y-004")
def test_a11y_004_text_contrast(page, rec, account_a):
    measured = {}

    def measure(label, locator):
        if locator.count():
            measured[label] = locator.first.evaluate(CONTRAST_JS)

    page.goto("/register")
    measure("registration hint", page.locator(".hint"))
    measure("muted text (auth card)", page.locator(".auth-card .muted"))
    login(page, account_a)
    page.goto("/")
    measure("navigation link", page.locator(".nav-links a"))
    measure("navigation username", page.locator(".nav-user"))
    measure("completed task title", page.locator("tr.done td.title-cell"))
    measure("Edit link", page.get_by_role("link", name="Edit"))
    measure("Delete button", page.get_by_role("button", name="Delete"))
    for cls in ("overdue", "due-soon", "upcoming", "no-due-date", "done"):
        measure(f"badge {cls}", page.locator(f".badge-{cls}"))
    page.goto("/?q=NO-SUCH-TITLE-W3")
    measure("empty-state message", page.locator("td.empty"))
    rec.capture(page, "contrast-empty-state")
    page.goto("/dashboard")
    measure("dashboard label", page.locator(".stat-label"))
    for label, m in measured.items():
        need = 3.0 if m["large"] else 4.5
        rec.expect(m["ratio"] >= need, f"{label}: contrast at least {need}:1",
                   f"{m['ratio']}:1 at {m['size']}px weight {m['weight']}")
    page.goto("/")
    rec.capture(page, "contrast-list")
    rec.assert_all()


@pytest.mark.case("TC-A11Y-005")
def test_a11y_005_form_labels_associated(page, rec, account_a):
    forms = {"/login": ["Username", "Password"], "/register": ["Username", "Password"],
             "/tasks/new": ["Title", "Description", "Category", "Due Date"]}
    for path, labels in forms.items():
        if path == "/tasks/new":
            login(page, account_a)
        page.goto(path)
        for text in labels:
            label = page.locator("label", has_text=re.compile(rf"^{text}"))
            label.click()
            focused = page.evaluate("() => document.activeElement.tagName.toLowerCase()")
            rec.expect(focused in ("input", "textarea", "select"), f"{path}: clicking '{text}' focuses its field",
                       f"focus on <{focused}>")
        names = [n for r, n, _ in ax_nodes(page) if r in ("textbox", "combobox", "PopUpButton", "ListBox")]
        rec.expect(all(any(n.startswith(t) for n in names) for t in labels),
                   f"{path}: each field's accessible name is its visible label", names)
    rec.capture(page, "labels")
    rec.assert_all()


@pytest.mark.case("TC-A11Y-006")
def test_a11y_006_filter_and_search_labels(page, rec, account_a):
    login(page, account_a)
    page.goto("/")
    visible_labels = page.locator("form.filters label").count()
    rec.expect(visible_labels >= 3, "category, status and search each have a visible label",
               f"{visible_labels} visible labels")
    names = {}
    for selector in ("select[name=category]", "select[name=status]", "input[name=q]"):
        names[selector] = page.locator(selector).evaluate(
            "el => el.labels && el.labels.length ? el.labels[0].innerText : (el.getAttribute('aria-label') || '')")
    ax = [(r, n) for r, n, _ in ax_nodes(page) if r in ("combobox", "textbox", "searchbox")]
    rec.expect(all(names.values()), "each control has a programmatic label (not placeholder only)",
               {"labels": names, "accessibility tree": ax})
    rec.capture(page, "filter-labels", full_page=False)
    rec.assert_all()


@pytest.mark.case("TC-A11Y-007")
def test_a11y_007_toggle_button_name_and_state(page, rec, account_a):
    login(page, account_a)
    page.goto("/")
    for fixture_id in ("F3", "F6"):
        title = account_a["tasks"][fixture_id]["title"]
        button = row_for(page, title).locator("button.check-btn")
        snapshot = button.aria_snapshot()
        match = re.search(r'button "([^"]*)"', snapshot)
        name = match.group(1) if match else ""
        rec.note(f"{fixture_id} accessibility snapshot: {snapshot.strip()}")
        rec.expect(title.lower() in name.lower() and re.search(r"[A-Za-z]{3,}", name.replace(title, "")),
                   f"{fixture_id}: the button's name states the action and the task", name)
        pressed = button.get_attribute("aria-pressed")
        rec.expect(pressed is not None or re.search(r"\b(done|complete|not done|open)\b", name.lower()),
                   f"{fixture_id}: the task's state is conveyed", {"name": name, "aria-pressed": pressed})
    rec.capture(page, "toggle-name", full_page=False)
    rec.assert_all()


def tab_to(page, predicate, limit=80):
    """Press Tab until document.activeElement satisfies the JS predicate; return the count or None."""
    for count in range(1, limit + 1):
        page.keyboard.press("Tab")
        if page.evaluate(f"() => {{ const el = document.activeElement; return !!(el && ({predicate})); }}"):
            return count
    return None


@pytest.mark.case("TC-A11Y-008")
def test_a11y_008_keyboard_operation(page, rec, account_a):
    data = {"title": "A11Y-Keyboard", "category_key": "W"}
    page.goto("/login")
    steps = {}

    def step(name, ok, actual=None):
        steps[name] = bool(ok)
        rec.expect(ok, f"keyboard: {name}", actual)

    step("reach Username", tab_to(page, "el.name === 'username'"))
    page.keyboard.type(account_a["username"])
    page.keyboard.press("Tab")
    page.keyboard.type(account_a["password"])
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("log in", urlpath(page) == "/", page.url)
    step("reach + New Task", tab_to(page, "el.classList.contains('btn')"))
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("reach Title", tab_to(page, "el.name === 'title'"))
    page.keyboard.type(data["title"])
    step("reach Category", tab_to(page, "el.name === 'category_id'"))
    page.keyboard.type(data["category_key"])
    category = page.locator("select[name=category_id] option:checked").inner_text().strip()
    step("choose a category by keyboard", category == "Work", category)
    step("reach Due Date", tab_to(page, "el.name === 'due_date'"))
    due = RUN_DATE + timedelta(days=3)
    typed = page.evaluate("() => { const p = new Intl.DateTimeFormat().formatToParts(new Date(2001, 1, 3)); "
                          "return p.filter(x => x.type !== 'literal').map(x => x.type).join(','); }")
    order = {"day": f"{due.day:02d}", "month": f"{due.month:02d}", "year": f"{due.year}"}
    for part in typed.split(","):
        page.keyboard.type(order[part])
    entered = page.input_value("input[name=due_date]")
    step("enter the due date by keyboard", entered == due.isoformat(), entered)
    # The date control has one Tab stop per segment, so tab on to the submit button.
    step("reach Create Task", tab_to(page, "el.tagName === 'BUTTON' && el.innerText.includes('Create')"))
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("create the task", row_for(page, data["title"]).count() == 1)
    page.goto("/")
    step("reach the category filter", tab_to(page, "el.name === 'category'"))
    with page.expect_navigation():
        page.keyboard.type("W")
    step("reach the search box", tab_to(page, "el.name === 'q'"))
    page.keyboard.type("A11Y")
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("filter and search", [t.strip() for t in page.locator("td.title-cell").all_inner_texts()] == [data["title"]])
    step("reach the complete button", tab_to(page, "el.classList.contains('check-btn')"))
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("complete the task", row_for(page, data["title"]).locator("button.check-btn").inner_text().strip() == "✓")
    tab_to(page, "el.classList.contains('check-btn')")
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("reopen the task", row_for(page, data["title"]).locator("button.check-btn").inner_text().strip() == "○")
    step("reach Edit", tab_to(page, "el.tagName === 'A' && el.innerText.trim() === 'Edit'"))
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("reach Save Changes", tab_to(page, "el.tagName === 'BUTTON' && el.innerText.includes('Save')"))
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("reach Delete", tab_to(page, "el.classList.contains('link-btn')"))
    page.once("dialog", lambda d: d.accept())
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("delete the task", row_for(page, data["title"]).count() == 0)
    step("reach Dashboard", tab_to(page, "el.tagName === 'A' && el.innerText.trim() === 'Dashboard'"))
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("reach Log out", tab_to(page, "el.tagName === 'A' && el.innerText.trim() === 'Log out'"))
    with page.expect_navigation():
        page.keyboard.press("Enter")
    step("log out", urlpath(page) == "/login", page.url)
    rec.note("The native confirm dialog was answered by Playwright; browsers make it keyboard-operable "
             "(Enter/Escape), which page automation cannot exercise.")
    rec.note(f"Keyboard steps: {steps}")
    rec.capture(page, "keyboard-end")
    rec.assert_all()


def urlpath(page):
    return urlparse(page.url).path


@pytest.mark.case("TC-A11Y-009")
def test_a11y_009_bypass_navigation(page, rec, account_a):
    login(page, account_a)
    page.goto("/")
    page.keyboard.press("Tab")
    first = page.evaluate("() => ({text: document.activeElement.innerText.trim(), href: document.activeElement.getAttribute('href')})")
    skip_link = bool(re.search(r"skip|main content", first["text"] or "", re.I)) and (first["href"] or "").startswith("#")
    main = any(r == "main" for r, _, _ in ax_nodes(page))
    rec.expect(skip_link or main, "a skip link on the first Tab, or a main landmark",
               {"first focus": first, "main landmark": main})
    rec.capture(page, "bypass", full_page=False)
    rec.assert_all()


@pytest.mark.case("TC-A11Y-010")
def test_a11y_010_page_titles(page, rec, account_a):
    titles = {}
    for path in AUTH_PAGES:
        page.goto(path)
        titles[path] = page.title()
    login(page, account_a)
    for path in app_pages(account_a):
        page.goto(path)
        titles[path] = page.title()
    rec.expect(len(set(titles.values())) == len(titles), "each page title is unique", titles)
    rec.expect(all(" — PyTodo Pro" in t and t.split(" — ")[0].strip() for t in titles.values()),
               "each title names the page's topic and the application", titles)
    rec.note("Shares evidence with TC-GUI-021.")
    rec.assert_all()


FOCUS_JS = """() => {
  const el = document.activeElement, r = el.getBoundingClientRect(), s = getComputedStyle(el);
  const ring = (s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0) || s.boxShadow !== 'none';
  return { tag: el.tagName, text: (el.innerText || el.value || el.name || '').trim().slice(0, 30),
           x: Math.round(r.left), y: Math.round(r.top), h: Math.round(r.height), ring };
}"""


@pytest.mark.case("TC-A11Y-011")
def test_a11y_011_focus_order_and_visible_focus(page, rec, account_a):
    def walk(path):
        page.goto(path)
        seen, order = set(), []
        for _ in range(80):
            page.keyboard.press("Tab")
            info = page.evaluate(FOCUS_JS)
            key = (info["tag"], info["text"], info["x"], info["y"])
            if info["tag"] == "BODY" or key in seen:
                break
            seen.add(key)
            order.append(info)
        no_ring = [f"{i['tag']} '{i['text']}'" for i in order if not i["ring"]]
        rec.expect(order and not no_ring, f"{path}: every focused control shows a focus indicator", no_ring)
        backwards = []
        for prev, cur in zip(order, order[1:]):
            same_line = abs(cur["y"] - prev["y"]) < max(prev["h"], cur["h"])
            if (same_line and cur["x"] < prev["x"]) or (not same_line and cur["y"] < prev["y"]):
                backwards.append(f"'{prev['text']}' -> '{cur['text']}'")
        rec.expect(not backwards, f"{path}: focus follows the visual reading order", backwards)

    for path in AUTH_PAGES:
        walk(path)
    login(page, account_a)
    for path in app_pages(account_a):
        walk(path)
    page.goto("/")
    page.keyboard.press("Tab")
    rec.capture(page, "focus-first", full_page=False)
    rec.assert_all()


def layout_checks(page, rec, label):
    layout, overlaps = nav_layout(page) if page.locator("nav.topnav").count() else ([], [])
    width = page.evaluate("() => window.innerWidth")
    wrapped = [i["text"] for i in layout if i["lines"] > 1]
    offscreen = [i["text"] for i in layout if i["box"]["x"] + i["box"]["width"] > width + 1]
    rec.expect(not wrapped and not offscreen and not overlaps, f"{label}: navigation readable and on screen",
               {"wrapped": wrapped, "off-screen": offscreen, "overlaps": overlaps})
    scroll = has_horizontal_scroll(page)
    table = page.evaluate("() => { const t = document.querySelector('table.task-table'); "
                          "return t ? t.scrollWidth > document.documentElement.clientWidth : false; }")
    rec.expect(not scroll or table, f"{label}: no horizontal scrolling except caused by the data table",
               {"page scrolls": scroll, "table wider than viewport": table})


@pytest.mark.case("TC-A11Y-012")
def test_a11y_012_reflow_320(page, rec, account_a):
    page.set_viewport_size({"width": 320, "height": 640})
    for path in AUTH_PAGES:
        page.goto(path)
        layout_checks(page, rec, f"320px {path}")
        rec.capture(page, f"reflow-{path.strip('/')}", full_page=False)
    login(page, account_a)
    for path in app_pages(account_a):
        page.goto(path)
        layout_checks(page, rec, f"320px {path}")
    page.goto("/")
    rec.capture(page, "reflow-list", full_page=False)
    page.goto("/dashboard")
    rec.capture(page, "reflow-dashboard", full_page=False)
    rec.assert_all()


@pytest.mark.case("TC-A11Y-013")
def test_a11y_013_text_resize_200(browser, rec, account_a):
    # 200% browser zoom on a 1280x800 window gives a 640x400 CSS-pixel viewport at device scale 2.
    context = browser.new_context(base_url=BASE_URL, viewport={"width": 640, "height": 400}, device_scale_factor=2)
    page = context.new_page()
    try:
        for path in AUTH_PAGES:
            page.goto(path)
            layout_checks(page, rec, f"200% {path}")
            rec.expect(page.locator("form button[type=submit]").is_visible(), f"200% {path}: submit button available")
        rec.capture(page, "zoom-register")
        login(page, account_a)
        for path in app_pages(account_a):
            page.goto(path)
            layout_checks(page, rec, f"200% {path}")
        page.goto("/")
        rec.capture(page, "zoom-list")
        rec.note("200% zoom emulated as a 640x400 CSS-pixel viewport at device scale 2 (equivalent layout to "
                 "zooming a 1280x800 window); browser zoom itself cannot be set by Playwright.")
    finally:
        context.close()
    rec.assert_all()


@pytest.mark.case("TC-A11Y-014")
def test_a11y_014_language_of_page(page, rec, account_a):
    langs = {}
    for path in AUTH_PAGES:
        page.goto(path)
        langs[path] = page.get_attribute("html", "lang")
    login(page, account_a)
    for path in app_pages(account_a):
        page.goto(path)
        langs[path] = page.get_attribute("html", "lang")
    rec.expect(all(v == "en" for v in langs.values()), "every page declares lang=\"en\"", langs)
    rec.assert_all()


@pytest.mark.case("TC-A11Y-015")
def test_a11y_015_error_identification(page, rec, account_a):
    cases = [("/login", account_a["username"], "WrongPass1"), ("/register", "ab", "Test12345")]
    for path, username, password in cases:
        page.goto(path)
        page.fill("input[name=username]", username)
        page.fill("input[name=password]", password)
        with page.expect_navigation():
            page.click("button[type=submit]")
        error = page.locator(".error")
        text = error.inner_text() if error.count() else ""
        rec.expect(bool(text.strip()), f"{path}: the error is described in text", text)
        exposure = error.evaluate(
            "el => ({role: el.getAttribute('role'), live: el.getAttribute('aria-live'), "
            "focused: document.activeElement === el || el.contains(document.activeElement)})") if error.count() else {}
        rec.expect(exposure.get("role") in ("alert", "status") or exposure.get("live") in ("assertive", "polite")
                   or exposure.get("focused"),
                   f"{path}: the error is exposed for announcement (alert role, live region or focus)", exposure)
        rec.capture(page, f"error-{path.strip('/')}")
    rec.assert_all()


@pytest.mark.case("TC-A11Y-016")
def test_a11y_016_target_size(page, rec, account_a):
    login(page, account_a)
    page.goto("/")
    targets = page.evaluate("""() => [...document.querySelectorAll(
        'button.check-btn, td.actions a, td.actions button, .nav-links a, .topnav .brand')].map(el => {
          const r = el.getBoundingClientRect();
          return { text: el.innerText.trim() || el.className, x: r.left, y: r.top, w: r.width, h: r.height };
        })""")
    small = [t for t in targets if t["w"] < 24 or t["h"] < 24]

    def centre(t):
        return (t["x"] + t["w"] / 2, t["y"] + t["h"] / 2)

    def distance_to_rect(point, t):
        dx = max(t["x"] - point[0], 0, point[0] - (t["x"] + t["w"]))
        dy = max(t["y"] - point[1], 0, point[1] - (t["y"] + t["h"]))
        return (dx * dx + dy * dy) ** 0.5

    failing = []
    for t in small:
        c = centre(t)
        for other in targets:
            if other is t:
                continue
            if other in small:
                oc = centre(other)
                clash = ((c[0] - oc[0]) ** 2 + (c[1] - oc[1]) ** 2) ** 0.5 < 24
            else:
                clash = distance_to_rect(c, other) < 12
            if clash:
                failing.append(f"'{t['text']}' {round(t['w'])}x{round(t['h'])} too close to '{other['text']}'")
                break
    rec.expect(not failing, "each target is at least 24x24 px or meets the spacing exception", sorted(set(failing))[:10])
    rec.note("Undersized targets measured: " + ", ".join(sorted({f"{t['text']} {round(t['w'])}x{round(t['h'])}" for t in small})))
    rec.capture(page, "targets", full_page=False)
    rec.assert_all()


@pytest.mark.case("TC-A11Y-017")
def test_a11y_017_descriptive_headings_and_labels(page, rec, account_a):
    found = {}
    for path in AUTH_PAGES:
        page.goto(path)
        found[path] = {"headings": page.locator("h1, h2, h3").all_inner_texts(),
                       "labels": [t.strip() for t in page.locator("label").all_inner_texts()]}
    login(page, account_a)
    for path in app_pages(account_a):
        page.goto(path)
        found[path] = {"headings": page.locator("h1, h2, h3").all_inner_texts(),
                       "labels": [t.strip() for t in page.locator("label").all_inner_texts()]}
    page.goto("/")
    headers = [h.strip() for h in page.locator("table.task-table thead th").all_inner_texts()]
    rec.expect(all(h for h in headers), "every table column, including control columns, has a header", headers)
    rec.expect(all(v["headings"] for v in found.values()), "every page has a heading", found)
    rec.note(f"Headings and labels for review: {found}")
    rec.capture(page, "headings", full_page=False)
    rec.assert_all()


@pytest.mark.case("TC-A11Y-018")
def test_a11y_018_automated_scans(page, rec, account_a):
    REPORTS.mkdir(parents=True, exist_ok=True)
    axe = Axe()
    stamp = RUN_DATE.strftime("%Y%m%d")
    summary = {}
    pages = [(p, p.strip("/") or "list") for p in AUTH_PAGES]
    for path, slug in pages:
        page.goto(path)
        summary[path] = _axe(axe, page, slug, stamp)
    login(page, account_a)
    for path in app_pages(account_a):
        slug = {"/": "list", "/tasks/new": "new", "/dashboard": "dashboard"}.get(path, "edit")
        page.goto(path)
        summary[path] = _axe(axe, page, slug, stamp)
    cookie = "; ".join(f"{c['name']}={c['value']}" for c in page.context.cookies())
    for path, slug in pages + [(p, {"/": "list", "/tasks/new": "new", "/dashboard": "dashboard"}.get(p, "edit"))
                               for p in app_pages(account_a)]:
        summary[path]["lighthouse"] = _lighthouse(path, slug, stamp, None if path in AUTH_PAGES else cookie)
    (REPORTS / f"summary-{stamp}.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    for path, s in summary.items():
        rec.expect(s["axe_report"] and s["lighthouse"] is not None, f"{path}: axe and Lighthouse reports saved", s)
        audited = urlparse((s["lighthouse"] or {}).get("final_url") or "").path
        rec.expect(audited == path, f"{path}: Lighthouse audited the intended page (not a redirect)", audited)
    rec.note(f"Scan summary: {summary}")
    rec.assert_all()


def _axe(axe, page, slug, stamp):
    result = axe.run(page)
    out = REPORTS / f"axe-{slug}-{stamp}.json"
    out.write_text(json.dumps(result.response, indent=2), encoding="utf-8")
    counts = {"critical": [], "serious": [], "moderate": [], "minor": []}
    for violation in result.response["violations"]:
        counts.setdefault(violation["impact"] or "minor", []).append(violation["id"])
    return {"axe_report": out.name, **counts}


def _lighthouse(path, slug, stamp, cookie):
    out = REPORTS / f"lighthouse-{slug}-{stamp}.html"
    cmd = ["npx", "-y", "lighthouse@12.8.2", BASE_URL + path, "--only-categories=accessibility",
           "--preset=desktop", "--output=html", "--output=json", f"--output-path={out.with_suffix('')}",
           "--chrome-flags=--headless=new", "--quiet"]
    if cookie:
        cmd.append(f"--extra-headers={json.dumps({'Cookie': cookie})}")
    done = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    report_json = out.with_suffix("").with_name(out.stem + ".report.json")
    if done.returncode != 0 or not report_json.exists():
        return None
    data = json.loads(report_json.read_text(encoding="utf-8"))
    return {"score": round(data["categories"]["accessibility"]["score"] * 100),
            "final_url": data.get("finalDisplayedUrl") or data.get("finalUrl")}
