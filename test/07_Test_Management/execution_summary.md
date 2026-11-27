# Test Execution and Regression Status

Consolidated execution counts for Weeks 1-4 and the Week 6 automated regression suite of **PyTodo Pro**. Week 5 is pending.

## 1. Execution status by phase

| Phase | Planned | Pass | Fail | Blocked | Not Run | Pass rate | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **W1** Black-box | 44 | 40 | 4 | 0 | 0 | **90.91%** | 4 failed cases map to 3 defects (`DEF-001` to `003`) |
| **W2** White-box | 50 | 50 | 0 | 0 | 0 | **100.00%** | 50 pytest instances: 30 backend (cover the 19 designed basis paths) + 20 helper |
| **W3** Special testing | 53 | 28 | 20 | 0 | 5 | **52.83%** (58.33% of the 48 executed) | GUI 14/22 Pass; compatibility 7/8; usability 0/5 (Not Run, review pending); accessibility 7/18 |
| **W4** Web and API | 61 | 43 | 18 | 0 | 0 | **70.49%** | 18 failed cases map to 13 defects (10 new + 3 W1 reproductions) |
| **W5** Security and performance | TBD | TBD | TBD | TBD | TBD | TBD | Pending |
| **Total W1-W4** | **208** | **161** | **42** | **0** | **5** | **77.40%** | 79.31% of the 203 executed; verdict completion 97.6% |
| *W6 Automation (excluded)* | *65* | *58* | *7* | *0* | *0* | *89.23%* | *Re-runs W1 scope and 10 W3 GUI functional checks; 7 failures are known defects* |

**W3 detail** (53 cases; compatibility cases count once, Fail if any configuration failed):

| W3 technique | Planned | Pass | Fail | Not Run | Pass rate of executed |
| --- | --- | --- | --- | --- | --- |
| GUI (`TC-GUI`) | 22 | 14 | 8 | 0 | 63.6% |
| Compatibility (`TC-CMP`) | 8 | 7 | 1 (`TC-CMP-007`, `DEF-006`) | 0 | 87.5% |
| Usability (`TC-USA`) | 5 | 0 | 0 | 5 | - |
| Accessibility (`TC-A11Y`) | 18 | 7 | 11 | 0 | 38.9% |

Compatibility ran on six configurations (C01-C06): 48 case runs, 46 Pass, 2 Fail (`TC-CMP-007` on C02 and C03, emulated tablet and phone). C07 (physical phone) is blocked by default. Microsoft Edge on Windows and Safari were excluded by team decision.

## 2. Pass rate by counting unit

| Unit | Denominator | Pass | Pass rate |
| --- | --- | --- | --- |
| Execution units, W1-W4 (W2 as 50 instances) | 208 | 161 | **77.40%** |
| Manual cases only (W1 + W3 + W4) | 158 | 111 | **70.25%** |
| Designed cases (44 + 19 + 53 + 61) | 177 | 130 | **73.45%** |
| Executed execution units (excluding 5 Not Run) | 203 | 161 | **79.31%** |

Use the unit that matches the claim: 208 for effort, 177 for design coverage, 158 for what humans or manual tooling executed.

## 3. Counting rules

1. **Units.** W1, W3 and W4 count cases. W2 counts pytest instances (50 from 38 test functions): 18 backend functions give 30 instances covering the 19 designed basis paths, and 20 helper instances come from `test_helpers.py`. W6 counts pytest checks.
2. **No double counting.** W6's 65 checks re-run W1 scope and part of W3's GUI scope, so they are reported separately.
3. **Failures versus defects.** One defect can fail many cases: W1 has 4 failed cases and 3 defects; W3 has 20 failed cases and 10 defects (plus 3 W1 reproductions and 3 observations); W4 has 18 failed cases and 13 defects. Unique defects: 23 (`DEF-001` to `DEF-023`).

## 4. Coverage (W2)

| Measure | Result |
| --- | --- |
| `helpers.py` statements | 31 of 31 (100.00%) |
| `app.py` statements | 136 of 299 (45.48%) |
| Overall | 167 of 330 (50.61%) |
| Selected backend callables | 31 of 31 (100%) |

Only statement coverage was measured, not branch coverage. The `app.py` figure is low because the whole file is measured, including registration, login, task routes and dashboard that W2 did not select.

## 5. Automated regression status (W6)

Run 2026-11-20, Edge 157 headless, isolated temporary SQLite database, commit `9cc1f34`. Runs 1 to 3 gave identical results for all 65 checks.

| Tier | Scope | Checks | Pass | Known-defect fail | New failures | Pass rate |
| --- | --- | --- | --- | --- | --- | --- |
| Full | all | 65 | 58 | 7 | 0 | 89.23% |
| Smoke | `-m smoke` | 11 | 11 | 0 | 0 | 100.00% |
| Unit | `-m unit`, no browser | 17 | 15 | 2 | 0 | 88.24% |

The 7 known failures are `DEF-001`, `002`, `003` and `005`, kept as strict xfail with the specified result; run 6 (`--defects-as-failures`) reports them as plain failures (exit 1). The gate is therefore **0 unexpected failures**, not a percentage.

**Seeded faults.** 7 of 7 injected faults (M1 to M7) were detected. M1-M5 and M7 are regressions of working behaviour. M6 is a *fix* of `DEF-001`, and the suite correctly reported it as Retest (XPASS).

### Regression gap

W6 ran on 2026-11-20, before W4's 18 failing cases existed (W4 ran 2026-11-24) and before W3's accessibility defects were confirmed. The regression suite therefore does **not** guard `DEF-014` to `DEF-023`, the W3 accessibility defects (`DEF-007` to `013`), `DEF-004` or `DEF-006`. W6 itself names the missing ownership check on `DELETE /api/tasks/<id>` (`DEF-014`) as the first candidate. `REQ-009` has no automated test. The Postman collection with Newman can serve as an interim API regression run.

## 6. Pending

- W5 counts and defects (`DEF-024` onward).
- Usability review `TC-USA-001` to `005` (5 cases Not Run).
- Compatibility configuration C07 (blocked by default).
