from datetime import date, datetime
from helpers import (
    compute_urgency,
    is_valid_password,
    is_valid_username,
    completed_in_last_n_days,
)
import pytest

class TestComputeUrgency:
    def test_no_due_date(self):
        assert compute_urgency("") == "No due date"

    def test_overdue(self):
        assert compute_urgency("2023-01-01", today=date(2023, 1, 2)) == "Overdue"

    def test_due_today(self):
        assert compute_urgency("2023-01-02", today=date(2023, 1, 2)) == "Overdue"

    def test_due_soon(self):
        assert compute_urgency("2023-01-03", today=date(2023, 1, 2)) == "Due Soon"
        assert compute_urgency("2023-01-04", today=date(2023, 1, 2)) == "Due Soon"

    def test_upcoming(self):
        assert compute_urgency("2023-01-05", today=date(2023, 1, 2)) == "Upcoming"

    def test_invalid_date_format(self):
        with pytest.raises(ValueError):
            compute_urgency("2023/01/05", today=date(2023, 1, 2))


class TestIsValidPassword:
    def test_non_string_password(self):
        assert is_valid_password(12345678) is False

    def test_short_password(self):
        assert is_valid_password("short") is False

    def test_valid_password(self):
        assert is_valid_password("longenoughpassword") is True


class TestIsValidUsername:
    def test_non_string_username(self):
        assert is_valid_username(12345) is False

    def test_invalid_characters(self):
        assert is_valid_username("invalid-user!") is False

    def test_short_username(self):
        assert is_valid_username("ab") is False

    def test_long_username(self):
        assert is_valid_username("Not a Twenty Character") is False

    def test_valid_username(self):
        assert is_valid_username("valid_user123") is True


class TestCompletedInLastNDays:
    def test_non_string_completed_at(self):
        assert completed_in_last_n_days("", n=7, now=date(2023, 1, 5)) is False

    def test_invalid_date_format(self):
        with pytest.raises(ValueError):
            assert (
                completed_in_last_n_days("2023/01/01", n=7, now=date(2023, 1, 5))
                is False
            )

    def test_non_now_date(self):
        assert completed_in_last_n_days("2023-01-01 00:00:00", n=7) is False  # Uses current date

    def test_completed_within_n_days(self):
        assert (
            completed_in_last_n_days(
                "2023-01-01 00:00:00", n=7, now=datetime(2023, 1, 5, 0, 0, 0)
            )
            is True
        )

    def test_completed_exactly_n_days_ago(self):
        assert (
            completed_in_last_n_days("2023-01-01 00:00:00", n=5, now=datetime(2023, 1, 5, 0, 0, 0))
            is True
        )

    def test_completed_more_than_n_days_ago(self):
        assert (
            completed_in_last_n_days("2022-12-31 00:00:00", n=4, now=datetime(2023, 1, 5, 0, 0, 0))
            is False
        )
