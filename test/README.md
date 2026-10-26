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
| Darius Lee Shin | 22003269 | Automation/Tool Coordinator |
| Ameera Alysha binti Azlan | 22002998 | Defect & Metrics Coordinator |

## 3. Deliverable Structure and Progress

The first eight folders correspond to Project Weeks 1-8. Folder 09 covers standards integration and the final presentation during Course Week 12.

| Phase | Folder / deliverable instructions | Status |
| --- | --- | --- |
| 01 | [Application analysis and black-box testing](01_Black_Box/README.md) | In progress - 44 functional black-box cases recorded|
| 02 | [White-box testing and coverage](02_White_Box_Coverage/README.md) | In Progress |
| 03 | [GUI, compatibility, usability and accessibility](03_Special_Testing/README.md) | In progress - planning complete |
| 04 | [Web and API testing](04_Web_API/README.md) | Not started |
| 05 | [Security and performance testing](05_Security_Performance/README.md) | Not started |
| 06 | [Test automation and regression](06_Automation_Regression/README.md) | Not started |
| 07 | [Test planning, traceability and defect management](07_Test_Management/README.md) | Not started |
| 08 | [SQA, metrics and final quality evaluation](08_Final_QA_Report/README.md) | Not started |
| 09 | [Standards integration, presentation and live demonstration](09_Presentation/README.md) | Not started |

Update status to `In progress`, `Ready for review` or `Completed` as supported by the artefacts. Tick a checklist only after its answer, evidence and peer review are complete. Revisit earlier work when later testing changes a finding or assumption.

## 4. Environment and Tools

The table below records the project environment. Phase 02 dependency versions
and reproduction commands are maintained in its [setup guide](02_White_Box_Coverage/setup.md).
Tools marked as to be selected remain unverified.

| Component | Purpose | Version / configuration |
| --- | --- | --- |
| Operating system | Execution environment | Windows 11, MacOS 26.5.2 |
| Python | Application and Python test execution | Python 3.14.7 |
| Flask | Web application framework | 3.0.3, specified in the application requirements |
| SQLite | Application database | `pytodo_pro.db` in the application root |
| Browser(s) | Manual GUI and compatibility testing | Google Chrome Version 155.0.8059.85 (Official Build) (arm64) |
| pytest (proposed) | Unit and regression test runner | 9.1.1 |
| pytest-cov (proposed) | Statement and branch coverage | 7.1.0 |
| API tool (to be selected) | Requests, authentication cookies and API evidence | [Tool and version] |
| UI automation tool (to be selected) | Selected browser regression workflows | [Tool, browser and driver versions if applicable] |
| Performance tool (to be selected) | Controlled workload and response measurements | [Tool and version] |
| Accessibility tools (to be selected) | Basic WCAG-oriented review and manual checks | [Tools, versions and checks] |
| Git | Version and contribution tracking | git version 2.55.0 |

Also record the execution date/time, timezone, application commit, test data and relevant hardware/network details. Performance results must identify the workload and environment.

## 5. Setup and Automated Test Execution

Use the [Phase 02 setup and reproduction guide](02_White_Box_Coverage/setup.md)
for virtual-environment creation, dependency installation, interpreter checks,
unit/integration test commands, HTML coverage generation, and optional manual
application startup. Run its commands from the **repository root**. Setup
instructions are maintained in that guide to avoid conflicting working
folders, package records, and report destinations.

The [Week 2 submission report](02_White_Box_Coverage/README.md) records selected
functions, CFGs, test-case traceability, collected test counts, and measured
coverage. Its implemented scripts are `test_helpers.py` and `test_app.py`.
Later phases should document any additional dependencies and their own
execution commands in the corresponding phase guide.

## 6. Documentation and Evidence Conventions

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

Link screenshots, logs and outputs from the relevant answer using relative Markdown links. The current Week 1 captures are indexed in [01_Black_Box/evidences/README.md](01_Black_Box/evidences/README.md). Update evidence links whenever replacing a run.

Each test case must contain its ID, feature/requirement, technique/type, objective, preconditions, test data, numbered steps, expected result, actual result, status, evidence and related defect ID. Each defect must contain its ID, title, feature, environment, preconditions, reproduction steps, expected/actual results, severity, priority, evidence and status. The RTM must connect requirements/features, scenarios, test IDs, techniques, results and defect IDs.

## 7. Final Submission Readiness

- [ ] Replace group, member and environment placeholders with verified information.
- [ ] Complete and review all nine phase READMEs and supporting artefacts.
- [ ] Verify setup and implemented automated-test commands in the documented environment.
- [ ] Check that every test has a unique ID and recorded expected/actual results or an explicit Not Run/Blocked status.
- [ ] Reconcile the RTM, master test-case repository and consolidated defect log.
- [ ] Verify evidence links, performance workload/environment details and metric calculations.
- [ ] State quality limitations, untested areas, residual risks and prioritised recommendations.
- [ ] Complete standards integration and prepare the presentation/live demonstration.
- [ ] Exclude local environments, caches and unnecessary generated files from commits; retain reports used as submission evidence.
