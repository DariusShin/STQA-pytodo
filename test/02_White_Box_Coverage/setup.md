# Week 2 — Environment setup and reproduction guide

This guide accompanies the [white-box testing submission report](README.md).
Run all shell commands from the repository root on branch `w2-whitebox`.
The main examples use macOS/Linux shells; the Windows activation alternative
is included below.
The test directory is `test/02_White_Box_Coverage`; no separate Flask server
is required.

## Verified environment

| Component | Verified version |
| --- | --- |
| Python | 3.14.7 |
| pytest | 9.1.1 |
| pytest-cov | 7.1.0 |
| coverage.py | 7.16.2 |
| Flask | 3.0.3 |

Based on the table above, the recorded results were obtained with these package
versions. The full dependency set is retained in `requirements-test-lock.txt`.
A virtual environment stores the testing and application dependencies together;
Flask must be installed in the same environment that runs pytest.

## 1. Create and activate the virtual environment

Create the environment only when setting up a fresh checkout; the existing
`.venv` can be reused. Python 3.14 matches the verified environment.

```bash
python3 -m venv test/02_White_Box_Coverage/.venv
source test/02_White_Box_Coverage/.venv/bin/activate
python -c 'import sys; print(sys.executable)'
```

On Windows PowerShell, create and activate the environment from the repository
root using:

```powershell
python -m venv test/02_White_Box_Coverage/.venv
.\test\02_White_Box_Coverage\.venv\Scripts\Activate.ps1
python -c 'import sys; print(sys.executable)'
```

The commands after activation use `python -m ...` on either platform.

On macOS/Linux, the printed interpreter should end with `test/02_White_Box_Coverage/.venv/bin/python`. Activate this environment again in each new terminal session. On Windows, the interpreter should end with
`test\02_White_Box_Coverage\.venv\Scripts\python.exe`.
To leave the environment, run `deactivate`.

## 2. Install and verify dependencies

Install the committed package versions, including Flask, pytest, pytest-cov,
and their dependencies:

```bash
python -m pip install -r test/02_White_Box_Coverage/requirements-test-lock.txt
python -m pip check
python -m pytest --version
python -m pip show pytest pytest-cov coverage Flask
```

Use `python -m pip` and `python -m pytest` so both commands use the active interpreter. There is no need to start the Flask server for unit tests. When implementing database tests, use a temporary SQLite database and patch `app.DATABASE` so tests do not change the application's local database.

## 3. Run the unit tests

Run both files explicitly:

```bash
python -m pytest test/02_White_Box_Coverage/test_helpers.py test/02_White_Box_Coverage/test_app.py
```

Or use the configured discovery path to run both:

```bash
python -m pytest
```

Run either file individually:

```bash
python -m pytest test/02_White_Box_Coverage/test_helpers.py
python -m pytest test/02_White_Box_Coverage/test_app.py
```

Add `-v` for individual test names. To check discovery without running tests:

```bash
python -m pytest --collect-only --no-cov
```

Pytest returns exit code 0 when all selected tests pass. Exit code 5 means
no tests were collected; check the selected path and test function names.

To run only the unit or integration tests in `test_app.py`:

```bash
python -m pytest test/02_White_Box_Coverage/test_app.py -m unit
python -m pytest test/02_White_Box_Coverage/test_app.py -m integration
```

Database integration tests patch `app.DATABASE` to a fresh temporary file for each test. Auth unit tests use request contexts and dummy protected functions.
HTTP integration tests exercise the actual `/` and `/api/tasks` endpoints with missing and authenticated sessions. These tests do not verify login credentials.

## 4. Generate and open the HTML coverage report

The root `pytest.ini` already enables pytest-cov for `helpers` and `app`.
Its `pythonpath = .` imports the root application modules, and its `testpaths`
selects `test/02_White_Box_Coverage`. Do not use the older phase-directory
`--rootdir=.` overrides; the documented commands rely on the root configuration.
Every normal command in step 3 generates statement coverage in the terminal
and an HTML report in this week's directory:

```text
test/02_White_Box_Coverage/htmlcov/index.html
```

To specify the HTML output explicitly:

```bash
python -m pytest test/02_White_Box_Coverage/test_helpers.py test/02_White_Box_Coverage/test_app.py --cov-report=html:test/02_White_Box_Coverage/htmlcov
open test/02_White_Box_Coverage/htmlcov/index.html
```

`open` launches the report in the default browser on macOS. On Windows,
open `test/02_White_Box_Coverage/htmlcov/index.html` in a browser; on Linux,
use the desktop file manager or `xdg-open` with that path. Select `helpers.py`
or `app.py` in the report to inspect executed and missing statements.
Reports are regenerated for each run, so run **both test files together** for
the combined report. The raw `.coverage` data file is stored in the repository
root. Generated coverage files, caches, and virtual environments are ignored
by Git.

The default metric is **statement coverage**: executed statements divided by
measured statements. In the terminal, `Stmts` is the measured count, `Miss` is
the unexecuted count, and `Missing` identifies uncovered lines. The target for
`helpers.py` is zero missed statements. After running both files, check that
target independently of the rest of the application:

```bash
python -m coverage report --include=helpers.py --fail-under=100
```

This check returns a nonzero exit code if helpers coverage is below 100%.
No global 100% threshold is configured: `app.py` is measured in full, so routes
outside this week's scope remain visible as uncovered. Inspect the selected
Database helpers and Auth functions individually in the HTML source view;
the overall `app.py` percentage does not represent only those functions.
No production code is excluded to inflate the score.

For optional branch coverage, run:

```bash
python -m pytest --cov-branch
```

This adds decision outcomes to the metric, so its percentage is different from
the statement-only target. Rerun `python -m pytest` to restore a statement-only
report. To run tests without collecting coverage, use `python -m pytest --no-cov`.

## 5. VS Code test runner

`.vscode/settings.json` points to the Week 2 virtual environment and enables
pytest discovery in this directory. If VS Code has a previously selected
interpreter, run **Python: Select Interpreter** and choose
`test/02_White_Box_Coverage/.venv/bin/python`. Then run **Test: Refresh Tests**.
The editor's test runner uses `--no-cov`; use the terminal commands above to
produce the assignment's coverage report.

## pytest-cov documentation

- [Configuration and command options](https://pytest-cov.readthedocs.io/en/latest/config.html):
  `--cov` selects source modules; `--no-cov` disables collection;
  `--cov-branch` enables branch coverage.
- [Reporting and output paths](https://pytest-cov.readthedocs.io/en/latest/reporting.html):
  `--cov-report=term-missing` lists uncovered lines and
  `--cov-report=html:DEST` writes HTML to the chosen directory.
- `--cov-fail-under=100` checks the combined coverage total. Use the separate
  `coverage report --include=helpers.py --fail-under=100` check above for this
  project's helpers-only target.


## 6. Troubleshooting and submission evaluation

If collection fails with `ModuleNotFoundError: No module named 'flask'`, the
selected interpreter does not have Flask installed. Activate the Week 2
environment, install the lock file, and rerun. To bypass shell activation and
select the interpreter explicitly:

```bash
test/02_White_Box_Coverage/.venv/bin/python -m pip install -r test/02_White_Box_Coverage/requirements-test-lock.txt
test/02_White_Box_Coverage/.venv/bin/python -m pytest
```

For marks evaluation, a combined run is essential: a run of only `test_app.py`
does not execute all pure helper tests. The expected baseline after this
report's basis-path addition is **50 passed**: 30 backend tests and 20 helper
tests. `helpers.py` should have 31 measured statements and no missed statements;
`app.py` should have 299 measured statements and 163 missed statements.

The HTML report shows source modules, rather than percentages for the test
scripts. To inspect per-function counts, open the report's function view or
optionally export machine-readable results:

```bash
python -m coverage json -o test/02_White_Box_Coverage/coverage.json
```

If branch coverage is investigated, write it to a different report directory:

```bash
COVERAGE_FILE=/tmp/pytodo-week2-branch.coverage python -m pytest --cov-branch --cov-report=term-missing --cov-report=html:test/02_White_Box_Coverage/htmlcov_branch
```

This leaves the default statement-only HTML report intact. Branch measurements
do not establish basis-path or exhaustive path coverage. For the selected
functions, compare the inputs and assertions with the numbered paths in Task 3.
The temporary database fixture prevents tests from modifying `pytodo_pro.db`.

The CFG figures in `figures/` are retained report assets. Their Mermaid source
is included directly beneath each figure in `README.md`, so they remain
reviewable when a Markdown viewer does not render Mermaid.

## 7. Manual application startup

For manual GUI or live-server testing, activate the environment as above and
start the application from the repository root:

```bash
python app.py
```

Open <http://127.0.0.1:5000/>; the API base is
<http://127.0.0.1:5000/api>. Startup initialises the application database and
default categories. Register a dedicated test account if required and stop
the server with `Ctrl+C`.

Manual startup uses `pytodo_pro.db` beside `app.py`, and restarting the server
does not reset that database. Preserve shared test data and document cleanup.
The automated tests instead patch `app.DATABASE` to a temporary per-test file.
A live server is not required for either existing pytest script.
