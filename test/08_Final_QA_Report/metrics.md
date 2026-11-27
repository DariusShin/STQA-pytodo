# Week 8 - Metrics

Computed from the [master test-case repository](../master_test_cases.md) and the [consolidated defect log](../consolidated_defect_logs.md).

## 1. Test execution

| Week | Area | Planned | Executed | Pass | Fail | Blocked | Not Run | Execution rate | Pass rate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Week 1 | Black-box | 44 | 44 | 40 | 4 | 0 | 0 | 100.0% | 90.9% |
| Week 2 | White-box | 28 | 28 | 28 | 0 | 0 | 0 | 100.0% | 100.0% |
| Week 3 | GUI | 22 | 22 | 14 | 8 | 0 | 0 | 100.0% | 63.6% |
| Week 3 | Compatibility | 8 | 8 | 7 | 1 | 0 | 0 | 100.0% | 87.5% |
| Week 3 | Accessibility | 18 | 18 | 7 | 11 | 0 | 0 | 100.0% | 38.9% |
| Week 4 | Web and API | 61 | 61 | 43 | 18 | 0 | 0 | 100.0% | 70.5% |
| Week 5 | Security and performance | 32 | 32 | 12 | 19 | 1 | 0 | 100.0% | 37.5% |
| Week 6 | Automation and regression | 89 | 89 | 64 | 25 | 0 | 0 | 100.0% | 71.9% |
| **Total** |  | 302 | 302 | 215 | 86 | 1 | 0 | 100.0% | **71.2%** |

Excluding the Week 6 automated re-runs of earlier cases: 213 cases, 151 Pass, 61 Fail, 1 Blocked, pass rate 70.9%.

## 2. Defects

### 2.1 By severity and priority

| Severity | High | Medium | Low | Total | Share |
| --- | ---: | ---: | ---: | ---: | ---: |
| Critical | 4 | 0 | 0 | 4 | 10.8% |
| Major | 6 | 0 | 0 | 6 | 16.2% |
| Moderate | 1 | 13 | 2 | 16 | 43.2% |
| Minor | 0 | 0 | 11 | 11 | 29.7% |
| **Total** | 11 | 13 | 13 | **37** | 100% |

### 2.2 By module

| Module | Critical | Major | Moderate | Minor | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Accessibility | 0 | 2 | 2 | 3 | 7 |
| Task input validation | 1 | 0 | 5 | 0 | 6 |
| Sessions and access control | 1 | 0 | 2 | 2 | 5 |
| Registration and login | 0 | 1 | 2 | 1 | 4 |
| Task list, search and paging | 1 | 1 | 1 | 1 | 4 |
| Configuration, logging and dependencies | 0 | 1 | 0 | 3 | 4 |
| Layout and responsiveness | 0 | 0 | 2 | 0 | 2 |
| Urgency and dashboard | 0 | 0 | 1 | 0 | 1 |
| Output rendering | 0 | 1 | 0 | 0 | 1 |
| Task ownership | 1 | 0 | 0 | 0 | 1 |
| API contract | 0 | 0 | 0 | 1 | 1 |
| Performance | 0 | 0 | 1 | 0 | 1 |

### 2.3 By phase found

| Phase | Critical | Major | Moderate | Minor | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Week 1 | 0 | 0 | 3 | 0 | 3 |
| Week 2 | 0 | 0 | 0 | 0 | 0 |
| Week 3 | 0 | 3 | 4 | 3 | 10 |
| Week 4 | 2 | 2 | 3 | 3 | 10 |
| Week 5 | 2 | 1 | 6 | 5 | 14 |
| Week 6 | 0 | 0 | 0 | 0 | 0 |

### 2.4 Density and status

| Metric | Value |
| --- | --- |
| Defect density | 37 defects / 557 lines (`app.py` + `helpers.py`) = **66.4 defects per KLOC** |
| Critical + Major share | 10 of 37 = 27.0% |
| Open / closed | 37 open, 0 closed (no fixes delivered) |
| Re-tested in a later week | 14 of 37 |

