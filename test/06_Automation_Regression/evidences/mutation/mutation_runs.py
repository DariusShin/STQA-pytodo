"""Seeded-fault check: run the regression suite against mutated COPIES of the app.

The real app.py/helpers.py are never modified. Each mutant is copied into the
OS temp folder, served on port 5106 with its own temp DB, and the suite is run
with --base-url against it. Run folders land in evidences/runs/*-mutant-Mn.
M1-M7 run the browser checks (-m "not unit and not api"); M8-M12 seed faults
in the JSON API and run the Week 4 Web/API checks (-m api), which need no browser.

Usage (from test/06_Automation_Regression, venv active):
    python -B evidences/mutation/mutation_runs.py [M1 M2 ...]
"""
import json, shutil, subprocess, sys, tempfile, time, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PHASE = REPO / "test" / "06_Automation_Regression"
PY = sys.executable  # run with the Week 6 venv interpreter
WORK = Path(tempfile.gettempdir()) / "w6-mutants"  # copies live outside the repo
PORT = 5106

MUTANTS = {
    "M1": ("REQ-005 Done status filter ignored on task list", "app.py",
           'if status_filter == "done":', 'if status_filter == "done-disabled":'),
    "M2": ("REQ-003 web delete not committed", "app.py",
           'db.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, session["user_id"]))\n    db.commit()',
           'db.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, session["user_id"]))'),
    "M3": ("REQ-002 dashboard loses login protection", "app.py",
           '@app.route("/dashboard")\n@login_required_web', '@app.route("/dashboard")'),
    "M4": ("REQ-008 task list not scoped to the logged-in user", "app.py",
           'query = "SELECT * FROM tasks WHERE user_id = ?"\n    params = [session["user_id"]]\n\n    cat_id = get_category_id_by_name(db, category_filter)',
           'query = "SELECT * FROM tasks WHERE (user_id = ? OR 1=1)"\n    params = [session["user_id"]]\n\n    cat_id = get_category_id_by_name(db, category_filter)'),
    "M5": ("REQ-006 Due Soon window widened to 3 days", "helpers.py",
           "if delta_days <= 2:", "if delta_days <= 3:"),
    "M6": ("DEF-001 fixed (password >= 8 accepted)", "helpers.py",
           "return len(password) > 8", "return len(password) >= 8"),
    "M7": ("REQ-004 reopen no longer possible", "app.py",
           'new_done = 0 if task["done"] else 1', "new_done = 1"),
    "M8": ("REQ-008 API read no longer limited to the owner", "app.py",
           'def api_get_task(task_id):\n    db = get_db()\n    row = db.execute(\n        "SELECT * FROM tasks WHERE id = ? AND user_id = ?"',
           'def api_get_task(task_id):\n    db = get_db()\n    row = db.execute(\n        "SELECT * FROM tasks WHERE id = ? AND (user_id = ? OR 1=1)"'),
    "M9": ("REQ-009 /api/dashboard loses login protection", "app.py",
           '@app.route("/api/dashboard", methods=["GET"])\n@login_required_api', '@app.route("/api/dashboard", methods=["GET"])'),
    "M10": ("DEF-014 and DEF-021 fixed (API delete limited to the owner, 404 when nothing deleted)", "app.py",
            'db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))\n    db.commit()\n    return jsonify({"result": "ok"})',
            'cur = db.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, session["user_id"]))\n'
            '    db.commit()\n    if cur.rowcount == 0:\n        return jsonify({"error": "not found"}), 404\n'
            '    return jsonify({"result": "ok"})'),
    "M11": ("REQ-005 API status=done filter ignored", "app.py",
            'if status == "done":', 'if status == "done-disabled":'),
    "M12": ("REQ-002 API login accepts any password", "app.py",
            'if user and check_password_hash(user["password_hash"], password):\n'
            '        session["user_id"] = user["id"]\n        session["username"] = user["username"]\n        return jsonify(',
            'if user:\n        session["user_id"] = user["id"]\n        session["username"] = user["username"]\n        return jsonify('),
}
API_MUTANTS = {"M8", "M9", "M10", "M11", "M12"}

LAUNCHER = '''import sys
sys.path.insert(0, sys.argv[3])
import app as pytodo
pytodo.DATABASE = sys.argv[1]
pytodo.init_db()
pytodo.app.run(host="127.0.0.1", port=int(sys.argv[2]), debug=False, use_reloader=False)
'''


def up():
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{PORT}/login", timeout=1)
        return True
    except OSError:
        return False


def main():
    only = sys.argv[1:] or list(MUTANTS)
    summary = {}
    for mid in only:
        desc, fname, old, new = MUTANTS[mid]
        d = WORK / mid
        shutil.rmtree(d, ignore_errors=True)
        d.mkdir(parents=True)
        for item in ("app.py", "helpers.py"):
            shutil.copy(REPO / item, d / item)
        shutil.copytree(REPO / "templates", d / "templates")
        shutil.copytree(REPO / "static", d / "static")
        src = (d / fname).read_text(encoding="utf-8")
        assert src.count(old) == 1, f"{mid}: pattern found {src.count(old)} times"
        (d / fname).write_text(src.replace(old, new), encoding="utf-8")
        (d / "launch.py").write_text(LAUNCHER, encoding="utf-8")
        db = Path(tempfile.mkdtemp(prefix=f"w6-{mid}-")) / "m.db"
        server = subprocess.Popen([PY, "-B", str(d / "launch.py"), str(db), str(PORT), str(d)],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            for _ in range(100):
                if up():
                    break
                time.sleep(0.2)
            marker = "api" if mid in API_MUTANTS else "not unit and not api"
            res = subprocess.run([PY, "-B", "-m", "pytest", "--browser", "edge", "-m", marker,
                                  "--base-url", f"http://127.0.0.1:{PORT}", "--run-label", f"mutant-{mid}",
                                  "-q", "-p", "no:randomly"], cwd=PHASE, capture_output=True, text=True)
        finally:
            server.terminate()
            server.wait(timeout=10)
        tail = [ln for ln in res.stdout.splitlines() if ln.startswith(("FAILED", "ERROR")) or " passed" in ln or " failed" in ln]
        summary[mid] = {"desc": desc, "exit": res.returncode, "lines": tail}
        print(mid, desc, "exit", res.returncode, flush=True)
        for ln in tail:
            print("   ", ln[:220], flush=True)
    (WORK / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
