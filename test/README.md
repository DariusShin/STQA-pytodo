# PyTodo Pro - Software Testing and Quality Assurance

## 1. Project Overview

This folder contains the progressive quality assessment of PyTodo Pro for the UTP Software Testing and Quality Assurance group project. Document findings and add evidence or test scripts under `test/`; do not modify the application's Python code or logic.

| Item | Details |
| --- | --- |
| Course codes | TEB3433 / TFB3433 - confirm the code applicable to this group |
| Semester | September 2026 |
| Lecturer | Dr Abdullateef |
| Group / tutorial | [To be completed] |
| Repository URL | [To be completed] |
| Submission deadline | End of Course Week 12 - confirm the calendar date |
| Application version / commit tested | [To be recorded for each execution] |

**Current status:** documentation scaffold only. Phase READMEs contain deliverable checklists and task headings, not completed answers. An existing screenshot is retained in `01_Black_Box/evidences/`; it still needs to be linked to a documented test execution. No automated test scripts are currently present.

## 2. Team Members and Responsibilities

Replace the placeholders with the four group members. Roles coordinate work; every member should contribute across phases. Record role rotation and individual contributions as the project progresses.

| Student name | Student ID | Coordination role | Contributions / reviews |
| --- | --- | --- | --- |
| [Member 1] | [ID] | QA/Test Lead | [To be completed] |
| [Member 2] | [ID] | Test Design Coordinator | [To be completed] |
| [Member 3] | [ID] | Automation/Tool Coordinator | [To be completed] |
| [Member 4] | [ID] | Defect & Metrics Coordinator | [To be completed] |

## 3. Deliverable Structure and Progress

The first eight folders correspond to Project Weeks 1-8. Folder 09 covers standards integration and the final presentation during Course Week 12, rather than an additional project execution week.

Source: `STQA Group Project.pdf`, Deliverable Contents on pages 2-5. Page 6 has no separate Deliverable Contents list for Phase 09, so that README reproduces its five integration/presentation requirements. Its introductory guidance also asks the group to briefly contextualise the completed work using ISO 9001, ISO/IEC 25010, CMMI, Agile/DevOps, CI/CD and continuous testing.

| Phase | Folder / deliverable instructions | Status |
| --- | --- | --- |
| 01 | [Application analysis and black-box testing](01_Black_Box/README.md) | Not started |
| 02 | [White-box testing and coverage](02_White_Box_Coverage/README.md) | Not started |
| 03 | [GUI, compatibility, usability and accessibility](03_Special_Testing/README.md) | Not started |
| 04 | [Web and API testing](04_Web_API/README.md) | Not started |
| 05 | [Security and performance testing](05_Security_Performance/README.md) | Not started |
| 06 | [Test automation and regression](06_Automation_Regression/README.md) | Not started |
| 07 | [Test planning, traceability and defect management](07_Test_Management/README.md) | Not started |
| 08 | [SQA, metrics and final quality evaluation](08_Final_QA_Report/README.md) | Not started |
| 09 | [Standards integration, presentation and live demonstration](09_Presentation/README.md) | Not started |

Update status to In progress, Ready for review or Completed as supported by the artefacts. Tick a checklist only after its answer, evidence and peer review are complete. Revisit earlier work when later testing changes a finding or assumption.

## 4. Environment and Tools

Record the actual environment used; proposed tools below are not yet installed or validated by this project.

| Component | Purpose | Version / configuration |
| --- | --- | --- |
| Operating system | Execution environment | [OS and version] |
| Python | Application and Python test execution | [Record `python --version`] |
| Flask | Web application framework | 3.0.3, specified in the application requirements |
| SQLite | Application database | `pytodo_pro.db` in the application root |
| Browser(s) | Manual GUI and compatibility testing | [Name, version, viewport and zoom] |
| pytest (proposed) | Unit and regression test runner | [Record version once adopted] |
| pytest-cov (proposed) | Statement and branch coverage | [Record version once adopted] |
| API tool (to be selected) | Requests, authentication cookies and API evidence | [Tool and version] |
| UI automation tool (to be selected) | Selected browser regression workflows | [Tool, browser and driver versions if applicable] |
| Performance tool (to be selected) | Controlled workload and response measurements | [Tool and version] |
| Accessibility tools (to be selected) | Basic WCAG-oriented review and manual checks | [Tools, versions and checks] |
| Git | Version and contribution tracking | [Record `git --version`] |

Also record the execution date/time, timezone, application commit, test data and relevant hardware/network details. Performance results must identify the workload and environment.

## 5. Application Setup

Run commands from the **application repository root**, containing `app.py`, `requirements.txt` and `test/`. Use a Python installation compatible with Flask 3.0.3 and record the version verified by the group.

### 5.1 Create and activate a virtual environment

macOS / Linux:

```bash
python3 -m venv test/.venv
source test/.venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv test/.venv
.\test\.venv\Scripts\Activate.ps1
```

The environment belongs to the local machine; exclude it from commits. If an existing environment is reused, record that choice and its package versions.

### 5.2 Install dependencies and start PyTodo Pro

With the environment activated:

```bash
python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000/>. The API base is <http://127.0.0.1:5000/api>. Starting with `python app.py` initialises the SQLite tables and default categories if needed. There is no pre-seeded login; register a dedicated test account through the UI or API. Stop the server with `Ctrl+C`.

### 5.3 Test data and database handling

Record account identifiers, task data, prerequisites and cleanup steps for each test. Use dedicated test accounts and preserve existing data needed by other team members. The application uses the database beside `app.py`, so restarting the server does not reset the data.

For future Flask integration tests, use test-side fixtures to direct the application's `DATABASE` variable to a temporary SQLite file, initialise it and restore the original setting after execution. Keep fixtures under `test/`; no source-file changes are required. Pure helper-function tests do not need a server or database.

## 6. Running Automated Tests

**Planned instructions:** these commands become usable after the group adds the corresponding scripts. At this scaffold stage, pytest will find no tests; that outcome is not a passing suite. Record actual results only after running implemented tests.

### 6.1 Install the proposed Python testing tools

In the activated environment, from the repository root:

```bash
python -m pip install pytest pytest-cov
python -m pip show pytest pytest-cov
```

Once validated, record exact versions and add a test-only dependency file under `test/` for reproducible installation. Document additional API, UI or performance dependencies before using them.

### 6.2 Script conventions and prerequisites

Place scripts in the appropriate phase folder. Use pytest filenames such as `test_urgency.py` and functions named `test_*`. Keep a regression suite under `06_Automation_Regression/` and map each automated test to its original requirement/manual test ID.

Pure unit tests and tests using Flask's test client do not require a live server. Tests making real HTTP requests or driving a browser require the server in another terminal, plus documented test accounts, data and browser prerequisites. Add exact tool-specific commands here when those suites exist.

### 6.3 Execute Python suites

All implemented pytest tests:

```bash
python -m pytest test/ -v -o cache_dir=test/.pytest_cache
```

Selected white-box tests:

```bash
python -m pytest test/02_White_Box_Coverage/ -v -o cache_dir=test/.pytest_cache
```

Focused regression suite:

```bash
python -m pytest test/06_Automation_Regression/ -v -o cache_dir=test/.pytest_cache
```

### 6.4 Collect coverage for selected code units

Before the coverage command, direct the coverage data file into the test folder.

macOS / Linux:

```bash
export COVERAGE_FILE=test/02_White_Box_Coverage/.coverage
```

Windows PowerShell:

```powershell
$env:COVERAGE_FILE = "test/02_White_Box_Coverage/.coverage"
```

Then, on either platform:

```bash
python -m pytest test/02_White_Box_Coverage/ -v -o cache_dir=test/.pytest_cache --cov=helpers --cov-branch --cov-report=term-missing --cov-report=html:test/02_White_Box_Coverage/evidences/coverage
```

This example measures `helpers.py` only. Adjust coverage targets to match the units justified in Phase 02 and report that scope explicitly. The HTML entry point will be `test/02_White_Box_Coverage/evidences/coverage/index.html`. Explain uncovered statements/branches and coverage limitations rather than treating coverage as proof of correctness.

### 6.5 Preserve execution results

For an implemented regression suite, this command saves a JUnit XML execution report:

```bash
python -m pytest test/06_Automation_Regression/ -v -o cache_dir=test/.pytest_cache --junitxml=test/06_Automation_Regression/execution-results.xml
```

Record the command, environment, application commit, test data, run time, summary and related defects alongside each report. pytest exit code 0 indicates success, 1 indicates test failures and 5 indicates no tests collected. Investigate other non-zero exits as execution/configuration problems. Report skipped tests separately; explain any mapping to the course's test statuses.

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
