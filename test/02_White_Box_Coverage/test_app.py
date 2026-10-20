import sqlite3
from contextlib import closing
from unittest.mock import Mock

import pytest
from flask import g, session

import app as app_module


@pytest.fixture
def flask_app(monkeypatch, tmp_path):
    # Use the Flask instance
    monkeypatch.setattr(app_module, "DATABASE", str(tmp_path / "test.db"))
    monkeypatch.setitem(app_module.app.config, "TESTING", True)
    monkeypatch.setitem(app_module.app.config, "SECRET_KEY", "week-2-test-secret")
    return app_module.app


@pytest.fixture
def initialized_app(flask_app):
    app_module.init_db()
    return flask_app

# Database helpers
@pytest.mark.integration
class TestDatabaseHelpers:
    def test_get_db_creates_and_reuses_connection(self, flask_app):
        with flask_app.app_context():
            first = app_module.get_db()
            assert g._database is first
            assert first.row_factory is sqlite3.Row
            assert app_module.get_db() is first
            assert first.execute("SELECT 1 AS value").fetchone()["value"] == 1

    def test_context_teardown_closes_connection(self, flask_app):
        with flask_app.app_context():
            connection = app_module.get_db()
        with pytest.raises(sqlite3.ProgrammingError, match="closed"):
            connection.execute("SELECT 1")

    def test_new_context_gets_new_connection(self, flask_app):
        with flask_app.app_context():
            first = app_module.get_db()
        with flask_app.app_context():
            second = app_module.get_db()
            assert second is not first
            assert second.execute("SELECT 1").fetchone()[0] == 1

    def test_init_db_creates_tables_and_commits_categories(self, flask_app):
        app_module.init_db()
        # An independent connection verifies that seeding was committed to disk.
        with closing(sqlite3.connect(app_module.DATABASE)) as db:
            tables = {
                row[0]
                for row in db.execute(
                    "SELECT name FROM sqlite_master WHERE type = 'table'"
                )
            }
            assert {"users", "categories", "tasks"} <= tables
            names = [row[0] for row in db.execute("SELECT name FROM categories")]
            assert sorted(names) == ["Personal", "Study", "Urgent", "Work"]
            db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("student", "test-hash"),
            )
            user_id = db.execute("SELECT id FROM users").fetchone()[0]
            db.execute(
                "INSERT INTO tasks (user_id, title, created_at) VALUES (?, ?, ?)",
                (user_id, "Study", "2026-10-20 12:00:00"),
            )
            assert db.execute(
                "SELECT description, done, completed_at FROM tasks"
            ).fetchone() == ("", 0, None)

    def test_init_db_is_repeatable_and_preserves_existing_data(self, initialized_app):
        with initialized_app.app_context():
            db = app_module.get_db()
            db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("student", "test-hash"),
            )
            db.execute("INSERT INTO categories (name) VALUES (?)", ("Custom",))
            original = list(db.execute("SELECT id, name FROM categories ORDER BY id"))
            original = [tuple(row) for row in original]
            db.commit()
        app_module.init_db()
        with initialized_app.app_context():
            db = app_module.get_db()
            assert [
                tuple(row)
                for row in db.execute("SELECT id, name FROM categories ORDER BY id")
            ] == original
            assert db.execute("SELECT username FROM users").fetchone()[0] == "student"

    def test_category_lookups_find_seeded_category(self, initialized_app):
        with initialized_app.app_context():
            db = app_module.get_db()
            expected_id = db.execute(
                "SELECT id FROM categories WHERE name = ?", ("Study",)
            ).fetchone()["id"]
            assert app_module.get_category_id_by_name(db, "Study") == expected_id
            assert app_module.get_category_name(db, expected_id) == "Study"

    def test_category_lookups_return_none_for_missing_values(self, initialized_app):
        with initialized_app.app_context():
            db = app_module.get_db()
            assert app_module.get_category_name(db, 999999) is None
            assert app_module.get_category_id_by_name(db, "Unknown") is None
            assert app_module.get_category_id_by_name(db, "Study' OR 1=1 --") is None


@pytest.mark.unit
class TestCloseConnection:
    def test_closes_existing_connection(self, flask_app):
        with flask_app.app_context():
            connection = Mock()
            g._database = connection
            app_module.close_connection(None)
            connection.close.assert_called_once_with()
            g.pop("_database")  # Avoid closing the mock again during teardown.

    def test_closes_connection_when_teardown_receives_exception(self, flask_app):
        with flask_app.app_context():
            connection = Mock()
            g._database = connection
            app_module.close_connection(RuntimeError("request failed"))
            connection.close.assert_called_once_with()
            g.pop("_database")

    def test_no_connection_is_safe(self, flask_app):
        with flask_app.app_context():
            assert app_module.close_connection(None) is None
            assert not hasattr(g, "_database")


@pytest.mark.unit
@pytest.mark.parametrize("category_id", [None, 0, ""])
def test_missing_category_id_skips_database(category_id):
    db = Mock()
    assert app_module.get_category_name(db, category_id) is None
    db.execute.assert_not_called()


@pytest.mark.unit
@pytest.mark.parametrize("done", [0, 1])
@pytest.mark.parametrize("category_name", [None, "Study"])
def test_row_to_task_converts_fields_and_selects_urgency(
    monkeypatch, done, category_name
):
    urgency = Mock(return_value="Due Soon")
    monkeypatch.setattr(app_module, "compute_urgency", urgency)
    row = {
        "id": 7,
        "title": "Revise",
        "description": "White-box testing",
        "category_id": 3,
        "due_date": "2026-10-22",
        "done": done,
        "completed_at": "2026-10-20 12:00:00" if done else None,
        "created_at": "2026-10-19 12:00:00",
    }
    original = row.copy()
    result = (
        app_module.row_to_task(row)
        if category_name is None
        else app_module.row_to_task(row, category_name)
    )
    assert result == {
        **row,
        "category": category_name,
        "done": bool(done),
        "urgency": "Done" if done else "Due Soon",
    }
    assert result["done"] is bool(done)
    assert row == original
    if done:
        urgency.assert_not_called()
    else:
        urgency.assert_called_once_with("2026-10-22")

# Auth decorators
@pytest.mark.unit
@pytest.mark.parametrize(
    "decorator", [app_module.login_required_web, app_module.login_required_api]
)
class TestAuthDecorators:
    @pytest.mark.parametrize("user_id", [None, 0, ""])
    def test_unauthenticated_request_does_not_call_function(
        self, flask_app, decorator, user_id
    ):
        protected = Mock(return_value="allowed")
        wrapped = decorator(protected)
        with flask_app.test_request_context("/"):
            if user_id is not None:
                session["user_id"] = user_id
            result = wrapped()
            if decorator is app_module.login_required_web:
                assert result.status_code == 302
                assert result.headers["Location"] == "/login"
            else:
                response, status = result
                assert status == 401
                assert response.get_json() == {"error": "authentication required"}
            protected.assert_not_called()

    def test_authenticated_request_forwards_arguments_and_result(
        self, flask_app, decorator
    ):
        expected = object()
        protected = Mock(return_value=expected)
        wrapped = decorator(protected)
        with flask_app.test_request_context("/"):
            session["user_id"] = 1
            assert wrapped(7, category="Study") is expected
            protected.assert_called_once_with(7, category="Study")

    def test_preserves_wrapped_function_metadata(self, decorator):
        def protected():
            """Protected view documentation."""
            return "allowed"

        wrapped = decorator(protected)
        assert wrapped.__name__ == protected.__name__
        assert wrapped.__doc__ == protected.__doc__
        assert wrapped.__wrapped__ is protected


@pytest.mark.integration
class TestAuthBackendIntegration:
    def test_backend_rejects_unauthenticated_requests(self, flask_app):
        with flask_app.test_client() as client:
            web = client.get("/", follow_redirects=False)
            assert web.status_code == 302
            assert web.headers["Location"] == "/login"
            api = client.get("/api/tasks")
            assert api.status_code == 401
            assert api.get_json() == {"error": "authentication required"}

    def test_backend_accepts_authenticated_session(self, initialized_app):
        with initialized_app.app_context():
            db = app_module.get_db()
            user_id = db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("student", "test-hash"),
            ).lastrowid
            db.commit()
        with initialized_app.test_client() as client:
            with client.session_transaction() as user_session:
                user_session["user_id"] = user_id
                user_session["username"] = "student"
            assert client.get("/").status_code == 200
            api = client.get("/api/tasks")
            assert api.status_code == 200
            assert api.get_json() == []
