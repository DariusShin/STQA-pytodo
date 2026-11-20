"""Start the unchanged PyTodo Pro app against an isolated SQLite database.

Used by conftest.py so every regression run starts from a clean, known state
instead of the shared development database (pytodo_pro.db). Only the module's
DATABASE setting is redirected at runtime; no application source is modified.

Usage:  python -B run_app.py <database-path> <port>
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

import app as pytodo  # noqa: E402  (import after sys.path is set)


def main():
    db_path, port = sys.argv[1], int(sys.argv[2])
    pytodo.DATABASE = db_path
    pytodo.init_db()
    # No debug reloader: a single process that the test session can stop cleanly.
    pytodo.app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()
