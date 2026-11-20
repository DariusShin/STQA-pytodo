"""REQ-005 Category/status filters and title search.

Automates Week 1 cases TC-BB-030 to TC-BB-035 (and the control-retention part
of TC-GUI-008) with the Week 1 combined-filter fixtures F1-F4, seeded into a
fresh account so the expected result sets are exact.

| Fixture | Title               | Category | Status |
| F1      | BB-MATCH-WORK-OPEN  | Work     | Open   |
| F2      | BB-MATCH-WORK-DONE  | Work     | Done   |
| F3      | BB-MATCH-STUDY-OPEN | Study    | Open   |
| F4      | BB-OTHER-WORK-OPEN  | Work     | Open   |
"""

import pytest
from selenium.webdriver.support.ui import Select

FIXTURES = [
    ("BB-MATCH-WORK-OPEN", "Work", False),
    ("BB-MATCH-WORK-DONE", "Work", True),
    ("BB-MATCH-STUDY-OPEN", "Study", False),
    ("BB-OTHER-WORK-OPEN", "Work", False),
]
F1, F2, F3, F4 = (f[0] for f in FIXTURES)


@pytest.fixture
def filter_account(ui, logged_in):
    for title, category, done in FIXTURES:
        logged_in["api"].create_task(title, category=category, done=done)
    ui.open("/")
    assert sorted(ui.titles()) == sorted([F1, F2, F3, F4]), "precondition: fixtures not listed"
    return logged_in


@pytest.mark.auto("TC-AUT-021")
@pytest.mark.req("REQ-005")
@pytest.mark.parametrize("category, status, query, expected", [
    pytest.param("Work", None, None, {F1, F2, F4}, marks=pytest.mark.manual("TC-BB-030"),
                 id="TC-BB-030-category-work"),
    pytest.param(None, "Open", None, {F1, F3, F4}, marks=pytest.mark.manual("TC-BB-031"),
                 id="TC-BB-031-status-open"),
    pytest.param(None, "Done", None, {F2}, marks=pytest.mark.manual("TC-BB-032"),
                 id="TC-BB-032-status-done"),
    pytest.param(None, None, "MATCH", {F1, F2, F3}, marks=pytest.mark.manual("TC-BB-033"),
                 id="TC-BB-033-search-match"),
    pytest.param(None, None, "NO-SUCH-TITLE-881", set(), marks=pytest.mark.manual("TC-BB-034"),
                 id="TC-BB-034-search-nomatch"),
    pytest.param("Work", "Open", "MATCH", {F1},
                 marks=[pytest.mark.manual("TC-BB-035", "TC-GUI-008"), pytest.mark.smoke],
                 id="TC-BB-035-combined"),
])
def test_filters_return_only_matching_tasks(ui, filter_account, category, status, query, expected):
    if category:
        ui.filter_category(category)
    if status:
        ui.filter_status(status)
    if query:
        ui.search(query)

    shown = ui.titles()
    assert set(shown) == expected and len(shown) == len(expected), \
        f"filters category={category} status={status} q={query} listed {shown}"
    if not expected:
        assert ui.empty_message() == "No tasks match your filters."

    # The active filters stay visible in their controls after the reload (TC-GUI-008).
    driver = ui.driver
    assert Select(driver.find_element("name", "category")).first_selected_option.text == \
        (category or "All categories")
    assert Select(driver.find_element("name", "status")).first_selected_option.text == \
        (status or "All statuses")
    assert driver.find_element("name", "q").get_attribute("value") == (query or "")
