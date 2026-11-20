"""REQ-006 Due-date urgency and REQ-007 Dashboard counters.

Automates Week 1 cases TC-BB-036 to TC-BB-043 with the Week 1 controlled
seven-task dataset. Due dates are offsets from the execution day, so the
dataset stays valid on any date (Week 1 had to use fixed October 2026 dates).

The Week 1 dashboard case failed on one counter only (DEF-002). Here the
counters are split so that the known defect is isolated to a single check and
the other four counters keep protecting against new regressions.
"""

import pytest

from api_client import ApiClient
from conftest import PASSWORD, iso_in, unique_username

# title, due offset in days (None = no due date), done
DATASET = [
    ("BB-NO-DATE", None, False),
    ("BB-YESTERDAY", -1, False),
    ("BB-TODAY", 0, False),
    ("BB-TOMORROW", 1, False),
    ("BB-PLUS-TWO", 2, False),
    ("BB-PLUS-THREE", 3, False),
    ("BB-COMPLETED", -1, True),
]


@pytest.fixture(scope="module")
def dashboard_account(base_url):
    """One account holding exactly the seven-task dataset (read-only for these tests)."""
    username = unique_username("dash")
    api = ApiClient(base_url)
    api.register(username, PASSWORD)
    for title, offset, done in DATASET:
        api.create_task(title, category="Study", due_date=iso_in(offset), done=done)
    return {"username": username, "password": PASSWORD, "api": api}


@pytest.fixture
def on_task_list(ui, dashboard_account):
    ui.login(dashboard_account["username"], dashboard_account["password"])
    assert len(ui.rows()) == len(DATASET), "precondition: dataset not complete"
    return ui


@pytest.mark.auto("TC-AUT-022")
@pytest.mark.req("REQ-006")
@pytest.mark.parametrize("title, expected", [
    pytest.param("BB-NO-DATE", "No due date", marks=pytest.mark.manual("TC-BB-036"), id="TC-BB-036-no-date"),
    pytest.param("BB-YESTERDAY", "Overdue", marks=pytest.mark.manual("TC-BB-037"), id="TC-BB-037-yesterday"),
    pytest.param("BB-TODAY", "Due Today", marks=[pytest.mark.manual("TC-BB-038", "TC-GUI-010"),
                                                 pytest.mark.known_defect("DEF-002")], id="TC-BB-038-today"),
    pytest.param("BB-TOMORROW", "Due Soon", marks=pytest.mark.manual("TC-BB-039"), id="TC-BB-039-tomorrow"),
    pytest.param("BB-PLUS-TWO", "Due Soon", marks=pytest.mark.manual("TC-BB-040"), id="TC-BB-040-plus-two"),
    pytest.param("BB-PLUS-THREE", "Upcoming", marks=pytest.mark.manual("TC-BB-041"), id="TC-BB-041-plus-three"),
])
def test_urgency_label(on_task_list, title, expected):
    row = on_task_list.row(title)
    assert row["urgency"] == expected, f"{title} due {row['due_date']} shows {row['urgency']!r}"


@pytest.mark.auto("TC-AUT-023")
@pytest.mark.manual("TC-BB-042")
@pytest.mark.req("REQ-004", "REQ-006")
def test_completion_overrides_overdue(on_task_list):
    row = on_task_list.row("BB-COMPLETED")
    assert (row["toggle"], row["urgency"], row["done"]) == ("✓", "Done", True)


@pytest.mark.auto("TC-AUT-024")
@pytest.mark.manual("TC-BB-043")
@pytest.mark.req("REQ-007")
def test_dashboard_counters_unaffected_by_def002(on_task_list):
    counters = on_task_list.dashboard_counters()
    observed = {k: counters.get(k) for k in ("Total Tasks", "Open", "Due Soon", "Completed (last 7 days)")}
    assert observed == {"Total Tasks": 7, "Open": 6, "Due Soon": 2, "Completed (last 7 days)": 1}


@pytest.mark.auto("TC-AUT-025")
@pytest.mark.manual("TC-BB-043")
@pytest.mark.req("REQ-007")
@pytest.mark.known_defect("DEF-002")
def test_dashboard_overdue_counter(on_task_list):
    counters = on_task_list.dashboard_counters()
    assert counters.get("Overdue") == 1, f"Overdue counter is {counters.get('Overdue')}, expected 1 " \
                                         "(only BB-YESTERDAY is overdue)"
