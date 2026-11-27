"""
Confirmed Week 5 findings (run of 25 Nov 2026 against pytodo_pro_student).
By default these tests are reported as XFAIL with their defect ID, so the file also works
as a regression suite: XPASS(strict) means the defect has been fixed -> retest and close it.
Use  pytest --raw  to see every finding as a plain FAILED (for the Week 5 evidence run).
"""
import pytest

KNOWN_DEFECTS = {
    "test_SEC_02_repeated_failed_logins_are_throttled": "DEF-024 no login throttling",
    "test_SEC_03_api_requires_login": "Week 4 defect: /api/categories needs no login",
    "test_SEC_04_session_cookie_flags": "DEF-025 session cookie has no SameSite",
    "test_SEC_05_old_session_cookie_rejected_after_logout": "DEF-026 cookie valid after logout",
    "test_SEC_06_common_password_rejected": "DEF-027 common passwords accepted",
    "test_SEC_20_session_cannot_be_forged_with_source_secret_key": "DEF-028 hard-coded SECRET_KEY allows session forgery",
    "test_SEC_07a_search_with_quote_does_not_crash": "DEF-017 search crash on apostrophe",
    "test_SEC_07b_sql_injection_in_search_cannot_read_other_users": "DEF-029 SQL injection in API search",
    "test_SEC_09a_forms_have_csrf_token": "DEF-030 no CSRF protection",
    "test_SEC_09b_cross_site_post_is_refused": "DEF-030 no CSRF protection",
    "test_SEC_12_stored_xss_title_is_escaped": "DEF-005 stored XSS (|safe in index.html)",
    "test_SEC_13_errors_do_not_show_tracebacks": "DEF-031 debug=True exposes tracebacks",
    "test_SEC_14_security_headers_present": "DEF-032 security headers missing",
    "test_SEC_16_huge_title_rejected": "DEF-033 no title length limit",
    "test_SEC_17_page_size_is_capped": "DEF-034 per_page not capped",
    "test_SEC_24_one_bad_due_date_does_not_lock_user_out": "DEF-015 bad due date locks user out",
    "test_SEC_18_another_users_task_cannot_be_deleted": "DEF-014 API delete skips ownership check",
}


def pytest_addoption(parser):
    parser.addoption("--raw", action="store_true", help="show known defects as plain failures")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--raw"):
        return
    for item in items:
        reason = KNOWN_DEFECTS.get(item.originalname or item.name)
        if reason:
            item.add_marker(pytest.mark.xfail(strict=True, reason=reason))
