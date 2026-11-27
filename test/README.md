# PyTodo Pro - Software Testing and Quality Assurance

## 1. Project overview

Progressive quality assessment of the PyTodo Pro task-management web application for the UTP September 2026 Software Testing and Quality Assurance group project. The application under test (`app.py`, `helpers.py`, `templates/`, `static/`) is in the repository root and is not modified; all test work is under `test/`.

| Item | Details |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester | September 2026 |
| Lecturer | Ts. Dr Abdullateef Balogun |
| Group / tutorial | Wednesday - Group 2 |
| Repository | [github.com/DariusShin/STQA-pytodo](https://github.com/DariusShin/STQA-pytodo) |

## 2. Team members and responsibilities

Roles coordinate the work; every member contributes across phases.

| Student name | Student ID | Role | Phase ownership |
| --- | --- | --- | --- |
| Eu Kwan Ik | 22001674 | QA/Test Lead | Week 6; Week 3 usability session (user) |
| Mohamad Shukri Bin Abdul Ajed | 22006255 | Test Design Coordinator | Weeks 4, 8; Week 3 usability session (recorder) |
| Darius Lee Shin | 22003269 | Automation/Tool Coordinator | Weeks 1, 2, 3, 8; Week 3 usability session (recorder), demonstration video (editor) |
| Ameera Alysha binti Azlan | 22002998 | Defect & Metrics Coordinator | Week 7; Week 3 usability session (user) |
| Wan Haziqah Binti Wan Hanafi | 22006757 | Test Assistant / Tester | Week 5 |

## 3. Submission structure

Every weekly folder uses the same files, so each deliverable is found in the same place:

| File | Responsibility |
| --- | --- |
| `README.md` | Introduction to the folder: what the week covers, a table of its files, and how to run its tests |
| `WN_Report.md` | The report to be evaluated: header (course, phase owner, execution dates, environment), deliverable checklist, one section per deliverable in the project brief |
| `test_cases.md` | All test cases of the week in the project Test Case Template |
| `defects.md` | Defects first found that week, in the Defect Report Template, followed by a "Re-tested defects" table for earlier defects checked again |
| `evidences/` | Screenshots, logs, tool reports and raw results referenced by the test cases and defects |
| Scripts | Automated tests, Postman collection or JMeter plans, next to the files above |

### Project-level tracking files

Three files in `test/` track the whole project. They were consolidated in Week 7 from the weekly `test_cases.md` and `defects.md` files, which stay the source records.

| File | Contents |
| --- | --- |
| [rtm.md](rtm.md) | Requirements traceability matrix: REQ-001 to REQ-014 traced to test cases, results and defects of every week |
| [master_test_cases.md](master_test_cases.md) | Master test-case repository: all 302 cases of Weeks 1-6, each linked to its full record |
| [consolidated_defect_logs.md](consolidated_defect_logs.md) | Consolidated defect log: DEF-001 to DEF-037 with severity, priority, status and re-test history |

### Project map

| Week | Folder | Focus | Report | Test cases | Defects | Evidence | Scripts / how to run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [01_Black_Box](01_Black_Box/) | Application analysis; manual black-box testing (EP, BVA, decision tables, state transitions) | [W1_Report.md](01_Black_Box/W1_Report.md) | [44 cases](01_Black_Box/test_cases.md) TC-BB-001 to 044 | [DEF-001 to 003](01_Black_Box/defects.md) | [screenshots](01_Black_Box/evidences/) | Manual; [README](01_Black_Box/README.md#how-to-run) |
| 2 | [02_White_Box_Coverage](02_White_Box_Coverage/) | Control-flow analysis, basis-path tests, statement coverage | [W2_Report.md](02_White_Box_Coverage/W2_Report.md) | [28 cases](02_White_Box_Coverage/test_cases.md) TC-WB-001 to 028 | None new | [HTML coverage report](02_White_Box_Coverage/htmlcov/index.html), [CFG figures](02_White_Box_Coverage/figures/) | pytest + pytest-cov; [README](02_White_Box_Coverage/README.md#how-to-run) |
| 3 | [03_Special_Testing](03_Special_Testing/) | GUI checklist, compatibility matrix, usability review, WCAG accessibility | [W3_Report.md](03_Special_Testing/W3_Report.md) | [GUI 22](03_Special_Testing/1_GUI/test_cases.md), [compatibility 8](03_Special_Testing/2_Compatibility/test_cases.md), [accessibility 18](03_Special_Testing/4_Accessibility/test_cases.md), [usability observations 4](03_Special_Testing/3_Usability/observations.md) | [DEF-004 to 013](03_Special_Testing/defects.md) | `evidences/` in each technique folder | Playwright + pytest; [README](03_Special_Testing/README.md#how-to-run) |
| 4 | [04_Web_API](04_Web_API/) | Web workflows, REST API, UI vs API comparison | [W4_Report.md](04_Web_API/W4_Report.md) | [61 cases](04_Web_API/test_cases.md) TC-WEB / TC-API; [test data](04_Web_API/test_data.md) | [DEF-014 to 023](04_Web_API/defects.md) | [runner result and screenshots](04_Web_API/evidences/) | Postman / Newman; [README](04_Web_API/README.md#how-to-run) |
| 5 | [05_Security_Performance](05_Security_Performance/) | STRIDE threat model, security tests, JMeter load/stress/data-volume tests | [W5_Report.md](05_Security_Performance/W5_Report.md) | [24 SEC + 8 PERF](05_Security_Performance/test_cases.md) | [DEF-024 to 037](05_Security_Performance/defects.md) | [security](05_Security_Performance/evidences/security/), [performance](05_Security_Performance/evidences/performance/) | pytest, pip-audit, bandit, JMeter; [README](05_Security_Performance/README.md#how-to-run) |
| 6 | [06_Automation_Regression](06_Automation_Regression/) | Automation candidates, Selenium/pytest/HTTP regression suite, seeded-fault check | [W6_Report.md](06_Automation_Regression/W6_Report.md) | [89 automated cases](06_Automation_Regression/test_cases.md) TC-AUT-001 to 089 | None new (14 re-tested) | [runs and mutation results](06_Automation_Regression/evidences/) | pytest + Selenium; [README](06_Automation_Regression/README.md#how-to-run) |
| 7 | [07_Test_Management](07_Test_Management/) | Test plan and strategy, RTM, master repository, consolidated defect log | [W7_Report.md](07_Test_Management/W7_Report.md) | [Master repository, 302 cases](master_test_cases.md); [RTM](rtm.md) | [Consolidated log, DEF-001 to 037](consolidated_defect_logs.md) | Weekly evidence, linked from each case and defect | None |
| 8 | [08_Final_QA_Report](08_Final_QA_Report/) | Metrics, residual risk, final quality evaluation | [W8_Report.md](08_Final_QA_Report/W8_Report.md) | Uses the [master repository](master_test_cases.md) | Uses the [consolidated log](consolidated_defect_logs.md) | [metrics.md](08_Final_QA_Report/metrics.md), [charts](08_Final_QA_Report/evidences/) | None |
| 9 | [09_Presentation](09_Presentation/) | ISO/IEC 25010 coverage and gaps, CI/CD, Agile/DevOps improvements, presentation and live demonstration | [W9_Report.md](09_Presentation/W9_Report.md) | None new | None new | Reuses weekly evidence | None |

## 4. Progress

| Phase | Status |
| --- | --- |
| 01 Black-box testing | Complete - 44 cases (40 Pass, 4 Fail); 3 defects |
| 02 White-box testing and coverage | Complete - 50 automated instances passed; 100% statement coverage of `helpers.py` and the 8 selected functions |
| 03 GUI, compatibility, usability, accessibility | Complete - 48 cases (28 Pass, 20 Fail) on 6 configurations; 4 usability observations; 10 defects |
| 04 Web and API testing | Complete - 61 cases (43 Pass, 18 Fail); 10 defects |
| 05 Security and performance testing | Complete - 24 security cases (6 Pass, 18 Fail); 8 performance cases; 14 defects |
| 06 Test automation and regression | Complete - 89 automated cases, 166 checks; 0 new failures; 12/12 seeded faults detected |
| 07 Test planning, traceability and defect management | Complete - test plan, strategy, RTM (REQ-001 to 014), 302-case repository, 37-defect log |
| 08 SQA, metrics and final quality evaluation | Complete - metrics, residual risks, quality assessment, recommendations |
| 09 Standards integration, presentation and live demonstration | Complete - standards mapping, CI/CD pipeline, Agile/DevOps improvements; presentation delivered in person |

## 5. Environment and tools

| Component | Purpose | Version / configuration |
| --- | --- | --- |
| Operating systems | Test execution | macOS 26.5.2; Windows 11 25H2; Windows 64-bit desktop (Week 5 security) |
| Python | Application and test execution | 3.14.7 (Weeks 1-3, 5 performance); 3.14 (Week 4); 3.12.10 (Week 5 security) |
| Flask | Application framework | 3.0.3, from `requirements.txt` |
| SQLite | Application database | `pytodo_pro.db` in the repository root; automated suites use temporary databases |
| Browsers | Black-box, GUI and compatibility testing | Google Chrome 155.0.8059.80 (Week 1) and 157.0.8103.80 (Week 3, macOS and Windows); Playwright Firefox 159.0 build |
| pytest, pytest-cov | Unit, integration and security tests; coverage | pytest 9.1.1 / 9.2.0; pytest-cov 7.1.0 |
| Playwright | GUI, compatibility and accessibility automation | 1.65.2 with pytest-playwright 0.10.0 |
| Accessibility tools | WCAG review | axe-core 4.12.1 (axe-playwright-python 0.1.8), Lighthouse 12.8.2 |
| Postman | API and web testing | Postman 12.38.2 Collection Runner; Newman for the command line |
| Security tools | Dependency and static scans | pip-audit, bandit |
| Apache JMeter | Load, stress and data-volume testing | 5.6.3 on OpenJDK 21 |
| Git | Version and contribution tracking | 2.55.0 |

Each week's README explains how to install its dependencies and run its tests from the repository root. Week 3 has its own `pytest.ini`, so always pass `test/03_Special_Testing/...` as the test path; the repository-root `pytest.ini` holds the Week 2 coverage settings.

## 6. Conventions

| Artefact | Convention |
| --- | --- |
| Requirements | `REQ-001` to `REQ-014`: REQ-001 to 008 from Week 1, REQ-009 from Week 4, REQ-010 to 014 (quality requirements) from Week 7 |
| Test cases | `TC-BB-`, `TC-WB-`, `TC-GUI-`, `TC-CMP-`, `TC-A11Y-`, `TC-WEB-`, `TC-API-`, `SEC-`, `PERF-`, `TC-AUT-` |
| Usability observations | `USA-OBS-` |
| Test status | Pass / Fail / Blocked / Not Run |
| Defects | One shared series `DEF-001` to `DEF-037` across all weeks |
| Severity / priority | Critical / Major / Moderate / Minor; High / Medium / Low |
| Defect status | Open / Confirmed / Retest / Closed |
| Evidence | Stored in the week's `evidences/`, named with the test ID and run date, linked from the test case or defect |
