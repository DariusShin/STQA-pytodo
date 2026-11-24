"""Browser-free regression checks of the business rules behind the UI cases.

The same boundaries as TC-BB-001..009 and TC-BB-036..041, checked directly on
helpers.py. These run in well under a second, need no server or browser, and
inject the date, so they cannot be affected by the midnight edge case that the
browser-level urgency checks are exposed to. They complement - not replace -
the UI checks, which prove the rules are actually wired into the pages.
"""

from datetime import date

import pytest

from helpers import compute_urgency, is_valid_password, is_valid_username

pytestmark = pytest.mark.unit

TODAY = date(2026, 11, 20)


@pytest.mark.auto("TC-AUT-026")
@pytest.mark.req("REQ-001")
@pytest.mark.parametrize("username, valid", [
    pytest.param("ab", False, marks=pytest.mark.manual("TC-BB-001"), id="TC-BB-001-len2"),
    pytest.param("abc", True, marks=pytest.mark.manual("TC-BB-002"), id="TC-BB-002-len3"),
    pytest.param("abcd", True, marks=pytest.mark.manual("TC-BB-003"), id="TC-BB-003-len4"),
    pytest.param("a" * 19, True, marks=pytest.mark.manual("TC-BB-004"), id="TC-BB-004-len19"),
    pytest.param("a" * 20, True, marks=pytest.mark.manual("TC-BB-005"), id="TC-BB-005-len20"),
    pytest.param("a" * 21, False, marks=pytest.mark.manual("TC-BB-006"), id="TC-BB-006-len21"),
    pytest.param("w1-d", False, marks=pytest.mark.manual("TC-BB-011"), id="TC-BB-011-hyphen"),
    pytest.param("w1d_a_2315", True, marks=pytest.mark.manual("TC-BB-010"), id="TC-BB-010-valid"),
])
def test_username_rule(username, valid):
    assert is_valid_username(username) is valid


@pytest.mark.auto("TC-AUT-027")
@pytest.mark.req("REQ-001")
@pytest.mark.parametrize("password, valid", [
    pytest.param("Test123", False, marks=pytest.mark.manual("TC-BB-007"), id="TC-BB-007-len7"),
    pytest.param("Test1234", True, marks=[pytest.mark.manual("TC-BB-008"), pytest.mark.known_defect("DEF-001")],
                 id="TC-BB-008-len8"),
    pytest.param("Test12345", True, marks=pytest.mark.manual("TC-BB-009"), id="TC-BB-009-len9"),
])
def test_password_rule(password, valid):
    assert is_valid_password(password) is valid


@pytest.mark.auto("TC-AUT-028")
@pytest.mark.req("REQ-006")
@pytest.mark.parametrize("due, expected", [
    pytest.param(None, "No due date", marks=pytest.mark.manual("TC-BB-036"), id="TC-BB-036-none"),
    pytest.param("2026-11-19", "Overdue", marks=pytest.mark.manual("TC-BB-037"), id="TC-BB-037-minus1"),
    pytest.param("2026-11-20", "Due Today", marks=[pytest.mark.manual("TC-BB-038"),
                                                   pytest.mark.known_defect("DEF-002")], id="TC-BB-038-today"),
    pytest.param("2026-11-21", "Due Soon", marks=pytest.mark.manual("TC-BB-039"), id="TC-BB-039-plus1"),
    pytest.param("2026-11-22", "Due Soon", marks=pytest.mark.manual("TC-BB-040"), id="TC-BB-040-plus2"),
    pytest.param("2026-11-23", "Upcoming", marks=pytest.mark.manual("TC-BB-041"), id="TC-BB-041-plus3"),
])
def test_urgency_rule(due, expected):
    assert compute_urgency(due, today=TODAY) == expected
