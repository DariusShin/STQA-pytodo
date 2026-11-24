# Project Week 7 - Test Management & Consolidation

**Folder:** `/07_Test_Management`  
**Primary Coordinator:** Defect & Metrics Coordinator (with team integration across Weeks 1–6)

## Deliverables Checklist

* [x] **Formal Software Test Plan** — [`test_plan.md`](test_plan.md) *(incorporating [`risk_register.md`](risk_register.md))*
* [x] **Test Strategy** — [`test_strategy.md`](test_strategy.md)
* [x] **Updated Requirements Traceability Matrix (RTM)** — [`rtm.md`](rtm.md) *(W1, W2, W4, W6 mapped; W3 & W5 pending merge)*
* [x] **Master Test-Case Repository** — [`master_test_cases.md`](master_test_cases.md) *(W1, W2, W4, W6 consolidated; W3 & W5 pending merge)*
* [x] **Consolidated Defect Log** — [`defect_log.md`](defect_log.md) *(W1, W2, W4, W6 consolidated; W3 `DEF-004`–`DEF-013` & W5 pending merge)*
* [x] **Test Execution & Regression Status** — [`execution_summary.md`](execution_summary.md) *(W1, W2, W4, W6 summarised; W3 & W5 pending merge)*

## Current Consolidation Status (Pre-W3 & W5 Merge)

* **Total Test Cases Consolidated (W1, W2, W4, W6):** 155 unique planned test cases (+ 65 automated regression re-runs in W6)
* **Current Pass / Fail / Blocked (W1, W2, W4, W6):** 126 Passed | 22 Failed | 6 Blocked | 1 Not Run
* **Unique Defects Logged (W1, W2, W4, W6):** 13 unique defects (`DEF-001`–`DEF-003`, `DEF-014`–`DEF-023`), plus 10 reserved IDs (`DEF-004`–`DEF-013`) for Week 3
* **Active Risks Tracked:** 12 risks in [`risk_register.md`](risk_register.md) (`R-01`–`R-09` assessed; `R-10`–`R-12` pending W3/W5 evidence)

## Pending Integration Items
1. **Week 3 (`03_Special_Testing`):** Merge 53 test cases, execution counts, `DEF-004` to `DEF-013` details, and `R-12` risk scoring.
2. **Week 5 (`05_Security_Performance`):** Merge security/performance test cases, execution counts, new defect IDs (`DEF-024+`), and `R-10`–`R-11` risk scoring.
3. **Group Sign-Off:** Confirm proposed re-scores on `R-05` and `R-09`, retest status (`Open` vs `Confirmed`) for `DEF-001`–`DEF-003` & `DEF-005`, and intended behaviour for `completed_in_last_n_days`.
