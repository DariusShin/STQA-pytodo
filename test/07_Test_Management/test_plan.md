# Formal Software Test Plan — PyTodo Pro

**Course:** TEB3433 / TFB3433 Software Quality Assurance & Testing  
**Deliverable:** Project Week 7 — Test Management & Consolidation (`/07_Test_Management`)  
**Application Under Test (AUT):** PyTodo Pro (Web-based Task & Productivity Manager)  
**Test Plan Version:** 1.0 (Consolidated from Weeks 1–6 Evidence)  

---

## 1. Test Objectives

The objectives of this Software Test Plan are to:
1. **Verify functional completeness** across all core PyTodo Pro requirements (`REQ-001` through `REQ-009`), including authentication, task CRUD, priority/deadline filtering, subtasks, notes, categories, and bulk operations.
2. **Ensure structural code quality** by exercising decision branches, boundary conditions, and error-handling paths in core backend modules (`app.py`, `models.py`, `database.py`).
3. **Validate non-functional and interface quality**, covering UI usability, cross-browser compatibility, accessibility, REST API schema contracts, input security, and response-time performance.
4. **Prevent regressions** via an isolated, repeatable automated test suite (`PyTest` + `Selenium`) that verifies critical workflows before release.
5. **Provide transparent quality metrics** through a traceable Requirements Traceability Matrix ([`rtm.md`](rtm.md)), Consolidated Defect Log ([`defect_log.md`](defect_log.md)), Execution Summary ([`execution_summary.md`](execution_summary.md)), and Risk Register ([`risk_register.md`](risk_register.md)).

---

## 2. Scope

### 2.1 In-Scope Features & Modules
* **Authentication & Access Control (`REQ-001`):** User registration, login, session persistence, logout, and route protection (`@login_required`).
* **Task Management (`REQ-002` to `REQ-006`):** Task creation, title/description validation, due-date boundary handling, priority assignment (`Low`, `Medium`, `High`), status toggling (`Complete`/`Incomplete`), editing, deletion, search, and filtering (`completed_in_last_n_days`, category, priority).
* **Subtasks, Notes & Categories (`REQ-007` to `REQ-009`):** Subtask creation/toggling, task-linked notes, custom category creation/assignment, and bulk task actions (bulk delete/complete).
* **REST API Endpoints (`/api/*`):** JSON request/response schema validation, HTTP status codes (`200`, `201`, `400`, `401`, `404`, `405`), and ownership enforcement.
* **Non-Functional Areas:** Cross-browser layout and responsiveness, WCAG/accessibility checks, authentication/injection hardening, and load response stability.

### 2.2 Out-of-Scope Items
* Third-party hosting infrastructure, DNS/SSL certificate provisioning, and production cloud deployment pipelines.
* Native mobile iOS/Android applications (only responsive mobile viewport testing in web browsers is in scope).
* Email/SMS notification delivery services not implemented in the local PyTodo Pro codebase.

---

## 3. Test Approach & Strategy

Testing is structured progressively across six execution phases, detailed fully in [`test_strategy.md`](test_strategy.md):
* **Week 1 — Black-Box Functional Testing:** Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Decision Tables, and State Transition testing across `REQ-001`–`REQ-009`.
* **Week 2 — White-Box Structural Testing:** Statement, branch, and path coverage analysis on `models.py`, `database.py`, and route controllers using `pytest-cov`.
* **Week 3 — Special Testing:** GUI heuristic evaluation, usability walkthroughs, WCAG accessibility checks, and cross-browser/viewport compatibility testing (`03_Special_Testing` — *pending final merge*).
* **Week 4 — Web & REST API Testing:** HTTP method enforcement, JSON payload validation, session cookie security flags, and unauthorized access checks across `/api/*` endpoints.
* **Week 5 — Security & Performance Testing:** Input sanitization (XSS/SQLi), privilege escalation checks, and concurrent request latency benchmarking (`05_Security_Performance` — *pending final merge*).
* **Week 6 — Test Automation & Regression:** Automated `PyTest` unit/API checks and headless `Selenium` end-to-end UI workflows, validated against 7 seeded defects.

---

## 4. Test Environment & Test Data

### 4.1 Hardware & Software Environment
* **Operating System:** Windows 10 / 11 (x64)
* **Runtime & Framework:** Python 3.x, Flask web framework, SQLite3 relational database
* **Browsers Tested:** Microsoft Edge (Chromium, headless & headed), Google Chrome, Mozilla Firefox
* **Network Setup:** Localhost development server (`http://127.0.0.1:5000`)

### 4.2 Test Data Management
* **Database Isolation:** Automated and API test runs execute against disposable SQLite databases provisioned per test function via PyTest's `tmp_path` fixture, preventing state leakage between test cases.
* **Seeded Datasets:** Standard test accounts (`valid_user`, `secondary_user` for IDOR/ownership checks) and boundary datasets (empty strings, 255+ character titles, past/present/future ISO dates, special characters, and negative filter values).
* **Fault-Injection Suite (Week 6):** Dedicated copy of the application seeded with 7 intentional defects (`SEED-01` to `SEED-07`) used exclusively to verify regression suite detection capability.

---

## 5. Testing Tools

| Category | Tool / Library | Purpose |
| :--- | :--- | :--- |
| **Test Runner & Assertions** | `PyTest` | Executing unit, white-box, API, and regression test suites with markers (`-m smoke`, `-m unit`). |
| **Code Coverage** | `pytest-cov` / `coverage.py` | Measuring line and branch coverage in Week 2 white-box testing. |
| **UI Browser Automation** | `Selenium WebDriver` (Edge) | Automating end-to-end browser flows (login, task creation, filtering, logout) in Week 6. |
| **API & HTTP Inspection** | Flask `test_client` / `requests` | Sending structured HTTP requests and inspecting status codes, headers, and JSON bodies. |
| **Version Control & Docs** | Git / GitHub & Markdown | Tracking test scripts, evidence screenshots, RTM, defect logs, and risk updates. |

---

## 6. Team Roles & Responsibilities

*(In accordance with course guidelines, every member contributes across multiple testing phases and deliverables while holding a primary coordination focus.)*

| Role | Primary Responsibilities | Deliverables Owned / Co-Owned |
| :--- | :--- | :--- |
| **QA / Test Lead** | Coordinates test planning, schedule adherence, scope alignment, and final release readiness sign-off. | `test_plan.md`, `test_strategy.md`, Week 8 Final SQA Report |
| **Test Design Coordinator** | Oversees test case design standards, requirement coverage, and master repository structure. | `rtm.md`, `master_test_cases.md`, Weeks 1–3 test suites |
| **Automation & Technical Lead** | Maintains test environments, API test harnesses, `PyTest`/`Selenium` frameworks, and CI/regression runs. | Week 4/5/6 automation scripts, `execution_summary.md` (Regression) |
| **Defect & Metrics Coordinator** | Maintains defect logging standards, severity/priority triage, execution metrics, and the evolving risk register. | `defect_log.md`, `risk_register.md`, `execution_summary.md`, `README.md` |

---

## 7. Entry and Exit Criteria

### 7.1 Entry Criteria (Starting Test Execution)
* Target feature code is committed to the repository and launches cleanly on `http://127.0.0.1:5000`.
* Requirements (`REQ-001`–`REQ-009`) and acceptance criteria are baselined in [`rtm.md`](rtm.md).
* Test cases are documented in [`master_test_cases.md`](master_test_cases.md) with clear preconditions, inputs, and expected results.
* Clean SQLite test database and required browser drivers (`msedgedriver`) are configured.

### 7.2 Suspension & Resumption Criteria
* **Suspension:** Execution on a module is paused if a blocking defect (`Critical` severity, e.g., application crash on startup, database corruption, or broken login) prevents access to dependent features.
* **Resumption:** Testing resumes once a fix is committed, deployed to the test environment, and passes smoke verification.

### 7.3 Exit Criteria (Phase & Release Sign-Off)
* **100%** of planned test cases across Weeks 1–6 executed (no `Not Run` items remaining after Week 3 & Week 5 merge).
* **0 unresolved `Critical` defects** open in [`defect_log.md`](defect_log.md) *(currently blocked by open `Critical` authentication/API defects such as `DEF-014` and `DEF-015` — release is **NOT** recommended until resolved)*.
* **100% pass rate** on the automated smoke suite (`-m smoke`) and verified detection of all 7 seeded faults in the regression suite.
* All deliverables in `/07_Test_Management` updated, cross-checked for ID consistency, and signed off in Week 8.

---

## 8. Risks and Limitations

### 8.1 Project & Product Risks
Product and process risks are actively tracked and re-scored across testing phases in [`risk_register.md`](risk_register.md). Key active risks identified from Weeks 1–6 evidence include:
* **Broken Authentication & Ownership Controls (`R-08`, Confirmed Critical):** API endpoints accept unauthenticated or cross-user requests (`DEF-014`, `DEF-015`), exposing user task data.
* **Input Validation & Date Boundary Failures (`R-03`, `R-05`):** Inconsistent validation between UI forms and backend models allows invalid date filters (`DEF-002`) and malformed payloads (`DEF-016`–`DEF-018`).
* **Schedule & Integration Bottlenecks (`R-01`):** Delayed consolidation of Week 3 (`03_Special_Testing`) and Week 5 (`05_Security_Performance`) artefacts compresses final cross-artefact verification time in Week 7.
* **Test Environment Parity (`R-06`):** Local SQLite file locking under rapid concurrent requests can cause false-positive failures during performance runs unless isolated properly.

### 8.2 Testing Limitations
* **Local Single-Node Execution:** All performance and API tests run against a local Flask development server with SQLite rather than a multi-worker production WSGI server (e.g., Gunicorn/PostgreSQL), limiting high-concurrency throughput extrapolation.
* **Headless Browser Constraints:** Automated `Selenium` regression runs in headless Edge verify DOM state and functional flows but cannot automatically detect subtle visual layout overlaps, which rely on manual Week 3 visual inspection.
* **Pending Week 3 & Week 5 Consolidation:** At Week 7 v1.0 baseline, execution totals (`155` planned cases) and defect records (`DEF-001`–`DEF-003`, `DEF-014`–`DEF-023`) exclude Week 3 (`53` cases, `DEF-004`–`DEF-013`) and Week 5 results until those folders are merged.

---

## 9. Deliverable Schedule & Sign-Off

| Milestone | Target Folder | Key Outputs | Status |
| :--- | :--- | :--- | :--- |
| **Weeks 1–6 Execution** | `/01_BlackBox` – `/06_Automation` | Phase test cases, scripts, screenshots, and initial defect logs | W1, W2, W4, W6 Complete; W3 & W5 Pending |
| **Week 7 Consolidation** | `/07_Test_Management` | `README.md`, `test_plan.md`, `test_strategy.md`, `rtm.md`, `master_test_cases.md`, `defect_log.md`, `execution_summary.md`, `risk_register.md` | In Progress (Pending W3 & W5 Merge) |
| **Week 8 Final SQA** | `/08_SQA_Evaluation` | Defect density, DRE, test coverage metrics, and final release recommendation | Upcoming |
