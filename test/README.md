# PyTodo Pro - Software Testing and Quality Assurance

## 1. Project Overview

This folder contains the progressive quality assessment of PyTodo Pro application for the UTP September 2026 Semester - Software Testing and Quality Assurance group project. Document findings and add evidence or test scripts under `test/`.

| Item | Details |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance|
| Semester | September 2026 |
| Lecturer | Ts. Dr Abdullateef Balogun  |
| Group / tutorial | Wednesday - Group 2 |
| Repository URL | [GitHub Repository](https://github.com/DariusShin/STQA-pytodo) |

## 2. Team Members and Responsibilities

Replace the placeholders with the four group members. Roles coordinate work; every member should contribute across phases. Record role rotation and individual contributions as the project progresses.

| Student name | Student ID | Coordination role |
| --- | --- | --- |
| Eu Kwan Ik  | 22001674 | QA/Test Lead |
| Mohamd Shukri Bin Abd Ajed | 22006225 | Test Design Coordinator |
| Darius Lee Shin | 220032369 | Automation/Tool Coordinator |
| Ameera Alysha binti Azlan | 22002998 | Defect & Metrics Coordinator |

## 3. Deliverable Structure and Progress

The first eight folders correspond to Project Weeks 1-8. Folder 09 covers standards integration and the final presentation during Course Week 12.

| Phase | Folder / deliverable instructions | Status |
| --- | --- | --- |
| 01 | [Application analysis and black-box testing](01_Black_Box/README.md) | Not started |
| 02 | [White-box testing and coverage](02_White_Box_Coverage/README.md) | In Progress |
| 03 | [GUI, compatibility, usability and accessibility](03_Special_Testing/README.md) | Not started |
| 04 | [Web and API testing](04_Web_API/README.md) | Not started |
| 05 | [Security and performance testing](05_Security_Performance/README.md) | Not started |
| 06 | [Test automation and regression](06_Automation_Regression/README.md) | Not started |
| 07 | [Test planning, traceability and defect management](07_Test_Management/README.md) | Not started |
| 08 | [SQA, metrics and final quality evaluation](08_Final_QA_Report/README.md) | Not started |
| 09 | [Standards integration, presentation and live demonstration](09_Presentation/README.md) | Not started |

Update status to `In progress`, `Ready for review` or `Completed` as supported by the artefacts. Tick a checklist only after its answer, evidence and peer review are complete. Revisit earlier work when later testing changes a finding or assumption.

## 4. Environment and Tools

Record the actual environment used; proposed tools below are not yet installed or validated by this project.

| Component | Purpose | Version / configuration |
| --- | --- | --- |
| Operating system | Execution environment | Windows 11, MacOS 26.5.2 |
| Python | Application and Python test execution | Python 3.14.7 |
| Flask | Web application framework | 3.0.3, specified in the application requirements |
| SQLite | Application database | `pytodo_pro.db` in the application root |
| Browser(s) | Manual GUI and compatibility testing | [Name, version, viewport and zoom] |
| pytest (proposed) | Unit and regression test runner | [Record version once adopted] |
| pytest-cov (proposed) | Statement and branch coverage | [Record version once adopted] |
| API tool (to be selected) | Requests, authentication cookies and API evidence | [Tool and version] |
| UI automation tool (to be selected) | Selected browser regression workflows | [Tool, browser and driver versions if applicable] |
| Performance tool (to be selected) | Controlled workload and response measurements | [Tool and version] |
| Accessibility tools (to be selected) | Basic WCAG-oriented review and manual checks | [Tools, versions and checks] |
| Git | Version and contribution tracking | git version 2.55.0 |

Also record the execution date/time, timezone, application commit, test data and relevant hardware/network details. Performance results must identify the workload and environment.

## 5. Application Setup Using the Phase 02 Environment

The virtual environment and installed application/testing packages can live entirely inside `test/02_White_Box_Coverage/.venv/`. A virtual environment controls which Python interpreter and packages are used; its location does not restrict which application files the tests can import. Keep the original `app.py` and `helpers.py` in the application root.

No installation is performed by this README update. The commands below are setup instructions for the group. Existing environments can remain in place; do not move an existing virtual environment into this folder. Create a new one here instead.

### 5.1 Create and activate the local virtual environment

Start in the **application repository root**, containing `app.py`, `requirements.txt` and `test/`, in a terminal without another environment activated. Choose the commands for your platform.

macOS / Linux:

```bash
cd test/02_White_Box_Coverage
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
cd test/02_White_Box_Coverage
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

All subsequent commands in Sections 5 and 6 run from **`test/02_White_Box_Coverage/`**, with this environment activated. Use a Python version verified by the group to work with the dependencies.

Confirm the interpreter before installing packages:

```bash
python -c "import sys; print(sys.executable)"
python --version
python -m pip --version
```

The interpreter and pip paths should point inside this folder's `.venv`. Activation is optional if the interpreter is invoked explicitly: `.venv/bin/python` on macOS/Linux or `.\.venv\Scripts\python.exe` on Windows.

### 5.2 Install dependencies locally

```bash
python -m pip install --no-cache-dir -r ../../requirements.txt pytest pytest-cov
python -m pip check
python -m pip show Flask pytest pytest-cov
```

The requirements file is read from the application root, while the packages are installed into the active Phase 02 `.venv`. `--no-cache-dir` avoids creating a pip download cache for this installation. Do not use `--user` or `--system-site-packages` for this setup. Testing `helpers.py` alone needs pytest/pytest-cov and Python's standard library; importing/testing `app.py` also requires Flask and its dependencies.

Record exact installed versions after validating the setup. A future `requirements-test-lock.txt` can be kept beside the Phase 02 README. To generate it from this dedicated environment once validated:

```bash
python -m pip freeze > requirements-test-lock.txt
```

Once that file exists, teammates can install the recorded dependencies with:

```bash
python -m pip install --no-cache-dir -r requirements-test-lock.txt
```

The lock file is not created by this documentation update. Each teammate creates their own `.venv`; do not commit or copy the environment. Exclude `.venv/`, `.pytest_cache/` and other local caches using a test-side ignore file when implementing the workspace. Keep the dependency record and submission evidence in version control.

### 5.3 Start the application for manual or live-server testing

From the Phase 02 folder, with its environment activated:

```bash
python -B ../../app.py
```

Open <http://127.0.0.1:5000/>. The API base is <http://127.0.0.1:5000/api>. This startup initialises SQLite tables and default categories if needed. There is no pre-seeded login; register a dedicated test account. Stop the server with `Ctrl+C`.

The environment's location does **not** relocate the application's database: the unchanged application still uses `pytodo_pro.db` beside `app.py`. Restarting the server does not reset it. Record test data and cleanup steps, and preserve data needed by teammates.

### 5.4 Isolate future Flask integration tests

Keep fixtures in `02_White_Box_Coverage/conftest.py`. Before database initialisation or requests, use pytest's `monkeypatch` fixture to redirect the application's module-level `DATABASE` variable to a temporary SQLite file, and initialise that test database. Enable Flask testing mode through the fixture and use Flask's test client. Restore settings and close connections during teardown. These are test-side runtime changes; do not edit the application source or replace its real database.

Pure helper tests need no server or database. Use explicit `today`/`now` arguments for deterministic date/time tests. `tmp_path` test databases may live in the operating system's temporary directory; a virtual environment is dependency isolation, not a filesystem sandbox.

## 6. Running Automated Tests from Phase 02

**Planned instructions:** no automated scripts are currently present. These commands become usable after the corresponding tests are added. No tests collected is not a passing suite.

### 6.1 Local workspace and imports

Suggested layout; only the README exists at this stage:

```text
02_White_Box_Coverage/
  README.md
  .venv/                         # local interpreter and packages; do not commit
  requirements-test-lock.txt     # create after dependency validation
  conftest.py                    # future database/client fixtures, if needed
  test_helpers.py                # future helper-function tests
  test_app_routes.py             # future selected Flask tests
  .pytest_cache/                 # generated local cache
  .coverage                      # generated coverage data
  evidences/                     # generated reports and captured evidence
```

The commands use `--rootdir=.` to anchor pytest in Phase 02 and `-o pythonpath=../..` to make the original application modules importable. Setting pytest's root directory alone does not add application modules to Python's import path. No source copying, application installation or changes to application files are required.

`python -B` prevents Python bytecode files being generated beside imported application modules. Keep test filenames unique across phases when running multiple folders together.

### 6.2 Execute selected white-box tests

From `test/02_White_Box_Coverage/`, with its `.venv` activated:

```bash
python -B -m pytest . --rootdir=. -o pythonpath=../.. -o cache_dir=.pytest_cache -v
```

Tests of `helpers.py` and tests using Flask's test client need no running server. Tests using real HTTP requests or browser automation need a server in a separate terminal, documented test data and any additional tool dependencies.

### 6.3 Collect statement and branch coverage

Keep the coverage data file in the Phase 02 working directory. Set this before the coverage run to override any inherited coverage-file setting.

macOS / Linux:

```bash
export COVERAGE_FILE=.coverage
```

Windows PowerShell:

```powershell
$env:COVERAGE_FILE = ".coverage"
```

Then run, on either platform:

```bash
python -B -m pytest . --rootdir=. -o pythonpath=../.. -o cache_dir=.pytest_cache -v --cov=helpers --cov-branch --cov-report=term-missing --cov-report=html:evidences/coverage --cov-report=xml:evidences/coverage.xml --junitxml=evidences/execution-results.xml
```

The terminal shows test results and coverage. Open `evidences/coverage/index.html` for annotated source and uncovered branches. The XML files preserve machine-readable coverage and test execution results. Save a terminal screenshot/log with the command, environment, run date/time and application commit.

This command measures `helpers.py` only. Once selected `app.py` tests exist, add `--cov=app` alongside `--cov=helpers`. That reports coverage across the whole measured `app.py` module, even if only selected routes are tested; describe untested routes and the resulting denominator. Explain uncovered statements/branches, failing assertions and scope limitations. Do not change an assertion to match defective behaviour simply to obtain a green suite.

### 6.4 Run later suites using the same environment

The Phase 02 environment can also execute other phase tests without installing dependencies in the application root. From Phase 02, a future focused regression run is:

```bash
python -B -m pytest ../06_Automation_Regression/ --rootdir=. -o pythonpath=../.. -o cache_dir=.pytest_cache -v --junitxml=../06_Automation_Regression/execution-results.xml
```

To collect all implemented pytest suites under `test/`:

```bash
python -B -m pytest .. --rootdir=. -o pythonpath=../.. -o cache_dir=.pytest_cache -v
```

Install and document additional dependencies in the chosen environment before using later suites. Alternatively, a later phase can have its own dedicated environment with its own dependency record.

### 6.5 Interpret and preserve results

Record command, environment, application commit, test data, execution time, test totals and related defect IDs. pytest exit code 0 indicates a successful run, 1 indicates test failures and 5 indicates no tests collected. Investigate other non-zero exits as execution/configuration problems. Report skips separately and explain their mapping to the course's test statuses.

A failing specification-based test can be valid evidence of an application defect. A high coverage percentage does not imply the covered behaviour is correct. Preserve failing-test output and reproduction evidence without modifying production logic.

Setup references: [Python virtual environments](https://docs.python.org/3/library/venv.html), [pytest import-path configuration](https://docs.pytest.org/en/stable/reference/reference.html#confval-pythonpath), [pytest-cov report output](https://pytest-cov.readthedocs.io/en/latest/reporting.html).

## 7. Documentation and Evidence Conventions

Use the guideline's required test-case, defect-report and RTM fields. Define expected results before execution. Do not mark an unexecuted test Pass or invent actual results.

| Artefact | Convention |
| --- | --- |
| Requirements | Stable IDs such as `REQ-001`, maintained in the RTM |
| Test cases | Unique IDs such as `TC-BB-001`, `TC-WB-001`, `TC-API-001` |
| Test statuses | Pass / Fail / Blocked / Not Run |
| Defects | Unique IDs such as `DEF-001`, consistent across phases |
| Severity | Critical / Major / Moderate / Minor |
| Priority | High / Medium / Low |
| Defect status | Open / Confirmed / Retest / Closed, as applicable |
| Evidence | Store under the phase's `evidences/`; include test ID and run/date in new filenames |

Link screenshots, logs and outputs from the relevant answer using relative Markdown links. Keep `01_Black_Box/evidences/LoginPageEvidence.png` and associate it with a test when its context is documented. Retain earlier evidence when later executions change an outcome.

Each test case must contain its ID, feature/requirement, technique/type, objective, preconditions, test data, numbered steps, expected result, actual result, status, evidence and related defect ID. Each defect must contain its ID, title, feature, environment, preconditions, reproduction steps, expected/actual results, severity, priority, evidence and status. The RTM must connect requirements/features, scenarios, test IDs, techniques, results and defect IDs.

## 8. Final Submission Readiness

- [ ] Replace group, member and environment placeholders with verified information.
- [ ] Complete and review all nine phase READMEs and supporting artefacts.
- [ ] Verify setup and implemented automated-test commands in the documented environment.
- [ ] Check that every test has a unique ID and recorded expected/actual results or an explicit Not Run/Blocked status.
- [ ] Reconcile the RTM, master test-case repository and consolidated defect log.
- [ ] Verify evidence links, performance workload/environment details and metric calculations.
- [ ] State quality limitations, untested areas, residual risks and prioritised recommendations.
- [ ] Complete standards integration and prepare the presentation/live demonstration.
- [ ] Exclude local environments, caches and unnecessary generated files from commits; retain reports used as submission evidence.
##
