# Week 9 - Standards Integration and Final Presentation

| Item | Value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance, September 2026 |
| Lab group | Wednesday Lab - Group 2 |
| Phase owner | All members; final integration coordinated by Eu Kwan Ik (QA/Test Lead) |
| Presentation | Delivered in person with Canva slides |
| Build under test | `app.py` SHA-256 `050b4ee4...f30f`, `helpers.py` `bf914033...6d80`; unchanged throughout the project |
| Sources | Weekly reports W1-W8, [RTM](../rtm.md), [master test cases](../master_test_cases.md), [consolidated defect log](../consolidated_defect_logs.md), [W8 metrics](../08_Final_QA_Report/metrics.md) |

## Deliverable checklist

- [x] [ISO/IEC 25010 quality characteristics evaluated](#1-isoiec-25010-characteristics-evaluated)
- [x] [Quality characteristics not adequately evaluated](#2-characteristics-not-adequately-evaluated)
- [x] [Automated regression tests in CI/CD and continuous testing](#3-regression-tests-in-cicd-and-continuous-testing)
- [x] [QA/process improvements for an Agile/DevOps workflow](#4-qaprocess-improvements-for-agiledevops)
- [x] [Final presentation and live demonstration](#5-final-presentation-and-live-demonstration)

## 1. ISO/IEC 25010 characteristics evaluated

Characteristic names follow ISO/IEC 25010:2023, with the 2011 name in brackets where it changed. **Direct** means test cases were designed for the characteristic; **indirect** means evidence came as a by-product of other testing.

| Characteristic | Sub-characteristics covered | Evaluation | Weeks and evidence | Result |
| --- | --- | --- | --- | --- |
| Functional suitability | Functional correctness, completeness, appropriateness | Direct | W1 44 black-box cases, W2 28 white-box cases, W4 61 web/API cases, W6 89 automated cases | Correct on the normal path; boundary and invalid-input defects, mostly in the API (DEF-001 to 003, 014 to 022) |
| Performance efficiency | Time behaviour, capacity | Direct | W5 JMeter PERF-01 to 07 | p95 ≤ 9 ms with 0 errors up to 50 users; saturation about 790 req/s; p95 above 1 s between 100 and 200 users; home page slows with data volume (DEF-037) |
| Interaction capability (usability) | Recognisability, operability, user error protection, user engagement | Direct | W3 GUI checklist (22 cases), usability session (USA-OBS-001 to 004) | Usable; weak action feedback and inconsistent styling, no blocking issue |
| Interaction capability - inclusivity (accessibility) | Inclusivity, operability by keyboard | Direct | W3 18 WCAG 2.2 checks, axe-core, Lighthouse 76-100 | Poor: 7 defects, 2 Major (DEF-007, 008) |
| Security | Confidentiality, integrity, authenticity, accountability, non-repudiation | Direct | W5 STRIDE table (22 threats), 24 security cases, bandit, pip-audit | Poor: 3 Critical security defects (DEF-014, 028, 029), no CSRF or rate limiting |
| Flexibility (portability) | Adaptability | Direct | W3 compatibility matrix: macOS and Windows 11, Chrome and Firefox, desktop/tablet/phone viewports | Works on all desktop configurations; layout fails on tablet and phone (DEF-004, 006) |
| Flexibility (portability) | Installability | Indirect | App and test suites installed from the README on macOS and Windows in Weeks 1-6 | Installs with `pip install -r requirements.txt`; development server only |
| Compatibility | Interoperability | Indirect | W4 JSON API contract checks; UI vs API comparison | JSON format consistent; web pages and API apply different rules: blank title (DEF-003), deleting another user's task (DEF-014), apostrophe in search (DEF-017) |
| Reliability | Faultlessness, fault tolerance | Indirect | W5 stress steps (no server errors to 200 users); W4 invalid data (DEF-015, 017) | Robust under load; fragile with bad data: one invalid date makes a user's pages fail |
| Maintainability | Analysability, testability, modularity | Indirect | W2 control-flow graphs (V(G) ≤ 3), W6 seeded-fault check (12 of 12 detected), duplicated web/API rules | Simple, testable functions; duplicated validation is the root of several defects |

## 2. Characteristics not adequately evaluated

| Characteristic | Gap | Why it matters | Next test |
| --- | --- | --- | --- |
| Reliability - availability, recoverability | No soak test, no restart or database-failure test | A task manager must keep data after crashes and long uptime | 8-hour soak with JMeter; kill and restart the server mid-write; corrupt or lock the SQLite file |
| Performance efficiency - resource utilisation | CPU and memory were not measured; only a development server on one MacBook | Capacity figures do not transfer to production | Repeat on a WSGI server (gunicorn) with a separate load generator and resource monitoring |
| Security - authenticity, confidentiality in transit | Session expiry, password change, HTTPS and penetration testing out of scope | Account takeover risk is already Critical (DEF-028) | Session lifetime tests, TLS configuration scan, an authorised penetration test |
| Interaction capability - inclusivity | No screen-reader session; no real users with disabilities | Automated scanners find only part of WCAG failures | NVDA/VoiceOver walkthrough of the main tasks |
| Interaction capability - learnability | Usability users were team members who already knew the app | Problems of first-time, non-technical users are unknown | Moderated sessions with 5 new users and task-completion times |
| Flexibility - adaptability, replaceability | No real mobile devices, Safari/WebKit or Edge (manual); no database other than SQLite | iOS users and deployment choices untested | Real iOS/Android devices; Playwright WebKit project |
| Compatibility - co-existence | Not evaluated | Shared hosting with other services untested | Run alongside another service on the same host and port range |
| Maintainability - modifiability, reusability | No static quality metrics beyond complexity of 8 functions; no code review | Duplicated rules already caused defects | Linting and duplication metrics (ruff, radon) on every change |
| Safety (new in 2023) | Not applicable to a task manager; not evaluated | Low | None planned |

## 3. Regression tests in CI/CD and continuous testing

### 3.1 Pipeline stages

The Week 6 tiers, Week 2 coverage suite and Week 3/5 tool checks fit a pipeline ordered by speed, so the fastest feedback comes first (shift-left).

| Stage | Trigger | Job (existing command) | Time | Quality gate |
| --- | --- | --- | --- | --- |
| 1 Pre-commit | Every local commit | `pytest -m unit` (Week 6 rules tier) | < 1 s | All rule checks pass |
| 2 Commit build | Every push / pull request | Week 6 smoke tier `pytest -m smoke`; Week 2 `pytest` with coverage; `bandit -r app.py helpers.py` | ~1 min | 0 new failures; `helpers.py` coverage stays 100%; no new High bandit finding |
| 3 Integration | Every pull request | Week 6 Web/API tier `pytest -m api`; Week 5 `pytest test_security.py` (regression mode); `pip-audit -r requirements.txt` | ~1 min | 0 new failures; no new vulnerable dependency |
| 4 Pre-merge | Before merge to `main` | Week 6 full regression `pytest --browser chrome` (headless) | ~85 s | Exit code 0: no new failure and no unexpected XPASS |
| 5 Nightly | Schedule | Full suite on Chrome, Firefox and Edge; Week 3 accessibility scan (axe, Lighthouse); `run_performance.py --quick` | ~15 min | No new axe critical/serious issue; 0% errors and p95 within budget on the quick load profile |
| 6 Release candidate | Before a release | Week 5 JMeter load, stress and data-volume runs; full suite with `--defects-as-failures` for the metrics | ~25 min | Open Critical defects = 0 for release; metrics published |

### 3.2 How the suite supports continuous testing

- **Known defects do not block the pipeline, but fixes are noticed.** Open defects are strict `xfail` with their defect ID, so the build stays green while nothing new breaks; when a fix lands, the strict XPASS fails the build and forces the defect to be re-tested and closed.
- **Isolated and repeatable.** Every run starts the unchanged app on its own port with a new temporary database and relative dates, so runs can be parallel and do not depend on the day.
- **Evidence per run.** JUnit XML, screenshots and step logs are written to a run folder and can be kept as pipeline artefacts.
- **Proven regression detection.** The suite detected all 12 seeded faults (Week 6), so a green run is meaningful for the checked behaviours.
- **Limits.** Visual layout, usability and keyboard accessibility stay manual and are reviewed at the end of each sprint.

### 3.3 Example workflow

Illustrative GitHub Actions definition for stages 2-4 (not added to the repository, because the project does not change the application or its hosting):

```yaml
name: regression
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r requirements.txt -r test/06_Automation_Regression/requirements-test-lock.txt bandit pip-audit
      - run: python -m pytest -m "unit or smoke or api"
        working-directory: test/06_Automation_Regression
      - run: bandit -r app.py helpers.py
      - run: pip-audit -r requirements.txt
      - run: python -m pytest --browser chrome
        working-directory: test/06_Automation_Regression
      - uses: actions/upload-artifact@v4
        if: always()
        with: { name: regression-evidence, path: test/06_Automation_Regression/evidences/runs }
```

## 4. QA/process improvements for Agile/DevOps

| Improvement | Agile/DevOps practice | Prevents or addresses |
| --- | --- | --- |
| Acceptance criteria with boundary examples and an API error contract in every story | Definition of Ready; three-amigos refinement | DEF-001, 002, 021 to 023: boundaries and status codes agreed before coding |
| One shared validation and data-access layer, checked in code review | Definition of Done; pull-request review checklist | DEF-003, 014, 015, 017 to 020, 029: web and API applying different rules |
| Secure-coding checklist; bandit and secret scanning in the commit build | Shift-left security (DevSecOps) | DEF-028 hard-coded key, DEF-029 string-built SQL, DEF-031 debug mode |
| Configuration from the environment (secret key, debug flag) | Infrastructure/configuration as code | DEF-028, 031 |
| Automated dependency updates and pip-audit gate | Continuous dependency management | DEF-036 outdated Flask |
| Accessibility check (axe) in the nightly build and an accessible-template checklist | Definition of Done includes accessibility | DEF-007 to 013 |
| Requirements-based unit tests written with the story, not from the code | Test-first / TDD | DEF-001, 002: the Week 2 tests repeated the code's boundary mistakes |
| Performance budget (p95 and data-volume check) in the release stage | Continuous performance testing | DEF-037 |
| Defect triage in each sprint; defect metrics by module and phase reviewed in the retrospective | Scrum events; continuous improvement | Recurring defect areas (API validation, accessibility) found early |
| Error tracking and security-event logging in production | Continuous monitoring (DevOps feedback loop) | DEF-015 and 017 (500 errors), DEF-035 (no security log) |
| Time-boxed exploratory testing each sprint | Agile testing quadrants (Q3) | Usability issues such as USA-OBS-001 to 004 |

### 4.1 Process context: ISO 9001 and CMMI

| Concept | How the project's QA work relates |
| --- | --- |
| ISO 9001 - documented information | Test plan, templates, test cases and defect records kept in version control with evidence for every result |
| ISO 9001 - nonconformity and corrective action | Each defect recorded in one template with evidence, severity and status; Week 8 recommendations and process improvements are the corrective actions |
| ISO 9001 - continual improvement (PDCA) | Plan (W7 test plan), Do (W1-W6 execution), Check (W7-W8 metrics and RTM), Act (W8-W9 recommendations) |
| CMMI Level 2 (Managed) | Planned and owned phases, requirements traced in the RTM, configuration management through Git branches and reviewed pull requests |
| CMMI Level 3 (Defined) | One standard per-week structure and shared templates used by every phase |
| Next step towards Level 4 | Quantitative targets (defect density, escape rate, coverage) tracked across releases, which needs the CI pipeline above |

## 5. Final presentation and live demonstration

The final presentation and live demonstration were delivered in person with Canva slides. They followed the evidence chain the brief asks for: what the application should do, how it was tested, what was observed, which defect was confirmed, what risk remains and what to test next.
