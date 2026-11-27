# Week 7 - Test Management and Consolidation

| Item | Recorded value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / Lab Group | September 2026 / Wednesday Lab - Group 2 |
| Phase owner | Defect & Metrics Coordinator (Ameera Alysha binti Azlan, 22002998), with the whole team |
| Team | Eu Kwan Ik (22001674), Darius Lee Shin (22003269), Mohamad Shukri Bin Abd Ajed (22006255), Ameera Alysha binti Azlan (22002998) |
| Phase status | Draft for peer review. Weeks 1-4 and 6 consolidated; Week 5 pending; Week 3 usability review not yet run |

## Deliverable Checklist

- [ ] [Task 1](#task-1) - Formal Software Test Plan. Pending peer review and the Week 5 merge.
- [ ] [Task 2](#task-2) - Test Strategy. Pending peer review (Week 5 approach to be confirmed against the Week 5 report).
- [ ] [Task 3](#task-3) - Updated RTM. Pending the Week 5 column and the W2 author's sign-off.
- [ ] [Task 4](#task-4) - Master test-case repository. Pending Week 5 cases and the commit of each source file.
- [ ] [Task 5](#task-5) - Consolidated defect log. Pending Week 5 defects (`DEF-024` onward).
- [ ] [Task 6](#task-6) - Test execution/regression status. Pending Week 5 and `TC-USA-001` to `005`.

Tick a task only after its content, cross-checks and peer review are complete.

## Deliverable structure

```
07_Test_Management/
├── README.md                this report
├── test_plan.md             Task 1
├── risk_register.md         referenced by the plan (not changed here)
├── test_strategy.md         Task 2
├── rtm.md                   Task 3
├── master_test_cases.md     Task 4 (index + verbatim and normalised appendices)
├── defect_log.md            Task 5
└── execution_summary.md     Task 6
```

## Current consolidation status (Weeks 1-4 and 6)

| Measure | Value |
| --- | --- |
| Designed cases | 177 (W1 44 + W2 19 + W3 53 + W4 61) |
| Execution units | 208 (W2 counted as 50 pytest instances) |
| Pass / Fail / Blocked / Not Run | 161 / 42 / 0 / 5 (the five Not Run are `TC-USA-001` to `005`) |
| Pass rate | 77.40% of execution units; 73.45% of designed cases; 70.25% of manual cases (W1 + W3 + W4) |
| Automated regression (W6, separate) | 65 checks: 58 Pass, 7 known-defect Fail, 0 unexpected; 7 of 7 seeded faults detected |
| Unique defects | 23 (`DEF-001` to `DEF-023`): 2 Critical, 4 Major, 11 Moderate, 6 Minor; all Confirmed |
| Observations | `USA-OBS-001` to `004` (severity pending the usability review) |
| Risks | See [risk_register.md](risk_register.md) |

## Task 1

[test_plan.md](test_plan.md): objectives, scope, approach by week, environment, roles (names and IDs), criteria and risks. Exit criteria are split into test-completion criteria and a quality gate; the Critical-defect gate is reported as not met and recorded as accepted risk because the application is frozen.

## Task 2

[test_strategy.md](test_strategy.md): levels and techniques, data and environment control, automation selection rule (four criteria, threshold 9 of 12 plus an exact oracle), regression policy, defect workflow and severity scale (the W4 scale).

## Task 3

[rtm.md](rtm.md): nine requirements plus cross-cutting and supporting rows, in template order with per-week case columns.

## Task 4

[master_test_cases.md](master_test_cases.md): index of 177 designed cases plus 28 automated cases; Appendix A (W1, 44) and D (W4, 61) copied unchanged; Appendix C (W3, 53) pasted as-is; Appendix B (W2) and F (W6) normalised to the 12 fields with the original IDs kept (`TC-WB-*`, `TC-AUT-*`). Results are corrected in the source file and re-copied, never edited here.

## Task 5

[defect_log.md](defect_log.md): one row for each of the 23 defects with all 12 template fields. Status rule: Confirmed means reproduced twice.

## Task 6

[execution_summary.md](execution_summary.md): counts by phase and by counting unit, W2 coverage, W6 regression status and the regression gap (W6 ran before the W4 failures existed).

## Pending integration items

1. **Week 5 (`05_Security_Performance`):** merge cases, counts, defects (`DEF-024` onward), RTM column and risks.
2. **Week 3 usability review:** `TC-USA-001` to `005` (and the severities of `USA-OBS-001` to `004`). Compatibility C07 is blocked by default.
3. **Source commits:** record the commit of each source file copied into the master repository.
4. **Group decisions:** whether `completed_in_last_n_days` (exclusive `<` against an inclusive docstring) becomes a new defect; W2 requirement mapping sign-off; confirm risk re-scores; confirm role assignments.
5. **Check `helpers.py`** before stating the code-level cause of `DEF-002` (the log currently cites only what W2 recorded).
6. **risk_register.md** was not part of this revision; check its references to `DEF-` IDs, counts and requirement meanings against the corrected files.
