# 02_White_Box_Coverage - White-Box Testing and Coverage

Week 2 selects eight backend functions in `app.py`, draws their control-flow graphs, derives basis paths, tests each path with pytest, and measures statement coverage of `app.py` and `helpers.py`.

| File / folder | Contents |
| --- | --- |
| [W2_Report.md](W2_Report.md) | Week 2 report: unit selection, CFGs, cyclomatic complexity, basis paths, coverage interpretation |
| [test_cases.md](test_cases.md) | 28 cases, TC-WB-001 to TC-WB-028 |
| [test_app.py](test_app.py) | Backend unit and integration tests (30 instances) |
| [test_helpers.py](test_helpers.py) | `helpers.py` tests (20 instances) |
| [figures/](figures/) | CFG diagrams (SVG) |
| [htmlcov/](htmlcov/index.html) | HTML statement-coverage report of the 2026-10-26 run, kept in the repository so it can be read without running the tests |
| `requirements-test-lock.txt` | Exact package versions used |

No defects were first found in Week 2, so there is no `defects.md`.

## How to run

From the repository root (no Flask server needed; tests use a temporary database):

```bash
python3 -m venv test/02_White_Box_Coverage/.venv
source test/02_White_Box_Coverage/.venv/bin/activate      # Windows: .\test\02_White_Box_Coverage\.venv\Scripts\Activate.ps1
python -m pip install -r test/02_White_Box_Coverage/requirements-test-lock.txt
python -m pytest                                            # both files; expected: 50 passed
```

- The root `pytest.ini` enables coverage of `app` and `helpers` and writes the HTML report to `test/02_White_Box_Coverage/htmlcov/`, overwriting the tracked report. Run both files together to get the combined report.
- Only unit or integration tests: `python -m pytest test/02_White_Box_Coverage/test_app.py -m unit` (or `-m integration`).
- Check the helper target: `python -m coverage report --include=helpers.py --fail-under=100`.
- Optional branch coverage: `python -m pytest --cov-branch`.
- Expected figures: `helpers.py` 31 statements, 0 missed; `app.py` 299 statements, 163 missed.
