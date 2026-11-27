"""Start the unchanged PyTodo Pro app on a chosen port with an empty database.

The supplied app.py is imported, not edited. Only two runtime settings differ
from `python app.py`:
  * the SQLite file is a fresh one passed on the command line;
  * the port is configurable (macOS reserves port 5000 for AirPlay), and the
    debug reloader is off so the runner can stop a single process cleanly.
Debug mode stays on, as supplied.

Usage:  python run_perf_server.py <database-path> <port>
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

import app as pytodo  # noqa: E402


def main():
    db_path, port = sys.argv[1], int(sys.argv[2])
    pytodo.DATABASE = db_path
    pytodo.init_db()
    pytodo.app.run(host="127.0.0.1", port=port, debug=True, use_reloader=False, threaded=True)


if __name__ == "__main__":
    main()
