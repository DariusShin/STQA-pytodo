# Week 2 — White-box testing and coverage

## Scope and current status

Work on branch `w2-whitebox`. Run every command below from the **repository root**.
The actual test directory is `test/02_White_Box_Coverage`.

| Source file | Test file | Week 2 target |
| --- | --- | --- |
| `helpers.py` | `test/02_White_Box_Coverage/test_helpers.py` | 100% statement coverage across all four helper functions |
| `app.py` | `test/02_White_Box_Coverage/test_app.py` | Database helpers and Auth decorators |

## Selection of function to be tested
1. The Database helpers are `get_db`, `close_connection`, `init_db`, `row_to_task`,
`get_category_name`, and `get_category_id_by_name`. 
2. The Auth section contains `login_required_web` and `login_required_api`, including their nested wrappers.
3. The subsequent **Web UI — auth pages** section and other routes are ***NOT*** included this week's selected units.

Verified environment: 
| Environment | Version |
| -- | -- |
| Python | 3.14.7 |
| pytest | 9.1.1 |
| pytest-cov | 7.1.0 |
| Flask | 3.0.3 |

## 1. Create and activate the virtual environment

Create the environment only when setting up a fresh checkout; the existing
`.venv` can be reused. Python 3.14 matches the verified environment.

```bash
python -m venv test/02_White_Box_Coverage/.venv
source test/02_White_Box_Coverage/.venv/bin/activate
python -c 'import sys; print(sys.executable)'
```

The print interpreter should end with `test/02_White_Box_Coverage/.venv/bin/python`. Activate this environment again in each new terminal session. To leave it, run `deactivate`.

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

`open` launches the report in the default browser on macOS. Select `helpers.py`
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

## Deliverable Checklist

- [ ] [Task 1](#task-1) - Selected code units and justification.
- [ ] [Task 2](#task-2) - Control-flow analysis.
- [ ] [Task 3](#task-3) - White-box test cases.
- [ ] [Task 4](#task-4) - Automated/unit test file where applicable.
- [ ] [Task 5](#task-5) - Coverage report and interpretation.

## Task 1

Selected code units and justification.

## Task 2

Control-flow analysis.

## Task 3

White-box test cases.

## Task 4

Automated/unit test file where applicable.

## Task 5

Coverage report and interpretation.

