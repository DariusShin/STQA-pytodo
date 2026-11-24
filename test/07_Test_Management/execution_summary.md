# Test Execution & Regression Status Summary

Consolidated execution counts across Weeks 1–6 and Week 6 automated regression suite results for **PyTodo Pro**.

---

## 1. Test Execution Status Across Weeks

| Week / Phase | Planned | Pass | Fail | Blocked | Not Run | Pass Rate | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Week 1:** Black-box | 44 | 40 | 4 | 0 | 0 | **90.91%** | 4 failed cases map to 3 unique defects (`DEF-001`–`DEF-003`) |
| **Week 2:** White-box | 50 | 50 | 0 | 0 | 0 | **100.00%** | 50 pytest instances (38 test functions covering 19 designed cases) |
| **Week 3:** GUI / Special | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | 53 cases listed in W6 README; pending W3 verification |
| **Week 4:** Web & API | 61 | 43 | 18 | 0 | 0 | **70.49%** | 18 failed cases map to 13 defects (10 new + 3 W1 reproductions) |
| **Week 5:** Security / Performance | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | Pending Week 5 completion |
| **Week 6:** Automation *(excluded from total)* | 65 | 58 | 7 | 0 | 0 | **89.23%** | Automated re-runs of W1 cases; 7 failures are expected known defects |
| **Total (W1, W2, W4 Consolidated)** | **155** | **133** | **22** | **0** | **0** | **85.81%** | Excludes W6 to prevent double-counting; update once W3 & W5 merge |

### Counting & Metric Definitions
1. **Counting Units:** Weeks 1 and 4 count manual test cases; Week 2 counts pytest test instances (50 instances across 38 test definitions covering 19 designed path-based cases); Week 6 counts automated pytest checks.
2. **Double-Counting Prevention:** Week 6's 65 automated checks re-execute the Week 1 functional scope and are therefore reported separately rather than added to the 155 planned total.
3. **Failed Cases vs. Unique Defects:** Pass rate is calculated as `Pass / Planned`. A single defect can cause multiple test cases to fail (e.g., Week 1 has 4 failed cases from 3 defects; Week 4 has 18 failed cases across 13 defect records; Week 6's 7 failures correspond to known defects `DEF-001`, `DEF-002`, `DEF-003`, and `DEF-005`, with 0 new defects discovered).

---

## 2. Automated Regression Status (Week 6)

- **Source:** Week 6 README, Task 4.1
- **Execution Date & Environment:** `2026-11-20`, Microsoft Edge 157 (headless), isolated temporary SQLite database
- **Stability Verification:** Runs 1 to 3 of the full regression suite produced identical results across all 65 checks.

| Regression Tier | Pytest Marker / Scope | Total Checks | Pass | Fail (Known Defect) | New Failures | Pass Rate |
| --- | --- | --- | --- | --- | --- | --- |
| **Full Regression Suite** | All automated checks | 65 | 58 | 7 | 0 | **89.23%** |
| **Smoke Suite** | `-m smoke` (critical path) | 11 | 11 | 0 | 0 | **100.00%** |
| **Unit / Business Rules** | `-m unit` (no browser) | 17 | 15 | 2 | 0 | **88.24%** |

### Mutation / Seeded-Fault Verification
- **Seeded-Fault Detection (Week 6, Task 4.4):** **7 / 7 (100%)** injected faults were caught by the automated regression suite, confirming strong fault-detection effectiveness for covered functional paths.
