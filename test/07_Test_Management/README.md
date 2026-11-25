# Week 7 - Test Management and Consolidation

| Item | Recorded value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / Lab Group | September 2026 / Wednesday Lab - Group 2 |
| Phase owner | Defect & Metrics Coordinator (Ameera Alysha binti Azlan, 22002998), with the whole team |
| Team | Eu Kwan Ik (22001674), Darius Lee Shin (22003269), Mohamad Shukri Bin Abd Ajed (22006255), Ameera Alysha binti Azlan (22002998) |
| Phase status | Draft for peer review. Weeks 1-6 consolidated (Week 5 merged from the 25 Nov 2026 run); Week 3 usability review not yet run |

## Deliverable Checklist

- [ ] [Task 1](#task-1) - Formal Software Test Plan. Pending peer review.
- [ ] [Task 2](#task-2) - Test Strategy. Pending peer review; the Week 5 row was written from the Week 5 report.
- [ ] [Task 3](#task-3) - Updated RTM. Pending the W2 and W5 authors' sign-off of the requirement mapping.
- [ ] [Task 4](#task-4) - Master test-case repository. Pending the commit of each source file.
- [ ] [Task 5](#task-5) - Consolidated defect log. Pending peer review of the W5 defect statuses and severities.
- [ ] [Task 6](#task-6) - Test execution/regression status. Pending `TC-USA-001` to `005`.

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

## Current consolidation status (Weeks 1-6)

| Measure | Value |
| --- | --- |
| Designed cases | 208 (W1 44 + W2 19 + W3 53 + W4 61 + W5 31) |
| Execution units | 239 (W2 counted as 50 pytest instances; W5 as 24 security + 7 performance IDs) |
| Pass / Fail / Blocked / Not Run | 173 / 61 / 0 / 5 (the five Not Run are `TC-USA-001` to `005`) |
| Pass rate | 72.38% of execution units; 68.27% of designed cases; 70.25% of manual cases (W1 + W3 + W4); W5 alone 38.71% (12 of 31) |
| Automated regression (W6, separate) | 65 checks: 58 Pass, 7 known-defect Fail, 0 unexpected; 7 of 7 seeded faults detected |
| Unique defects | 37 (`DEF-001` to `DEF-037`): 4 Critical, 6 Major, 16 Moderate, 11 Minor; 23 Confirmed, 14 Open (all from W5) |
| Observations | `USA-OBS-001` to `004` (severity pending the usability review) |
| Risks | See [risk_register.md](risk_register.md) |

## Task 1

[test_plan.md](test_plan.md): objectives, scope, approach by week, environment, roles (names and IDs), criteria and risks. Exit criteria are split into test-completion criteria and a quality gate; the Critical-defect gate is reported as not met (`DEF-014`, `015`, `028`, `029` open) and recorded as accepted risk because the application is frozen. The W5 performance target is reported as met.

## Task 2

[test_strategy.md](test_strategy.md): levels and techniques, data and environment control, automation selection rule (four criteria, threshold 9 of 12 plus an exact oracle), regression policy, defect workflow and severity scale (the W4 scale).

## Task 3

[rtm.md](rtm.md): nine requirements plus cross-cutting UI, cross-cutting security and performance, and supporting rows, in template order with per-week case columns (W5 filled in).

## Task 4

[master_test_cases.md](master_test_cases.md): index of 208 designed cases plus 28 automated cases; Appendix A (W1, 44), D (W4, 61) and E (W5, 31) copied unchanged; Appendix C (W3, 53) pasted as-is; Appendix B (W2) and F (W6) normalised to the 12 fields with the original IDs kept (`TC-WB-*`, `TC-AUT-*`). Results are corrected in the source file and re-copied, never edited here.

## Task 5

[defect_log.md](defect_log.md): one row for each of the 37 defects with all 12 template fields. Status rule: Confirmed means reproduced twice.

## Task 6

[execution_summary.md](execution_summary.md): counts by phase and by counting unit, W2 coverage, W5 detail and performance results, W6 regression status and the regression gap (W6 ran before the W4 failures existed).

## Pending integration items

1. **Week 5 follow-ups:** the W5 report leaves the phase owner blank (`_(your name)_`) and does not record the application commit; it ran on a Linux VM with Flask 3.1.3, not the pinned 3.0.3. Group decisions: raise `DEF-005` to Major (applied as a proposal), keep the 14 W5 defects `Open` until reproduced twice, whether `DEF-034` duplicates `DEF-022` and `DEF-029` duplicates `DEF-017`, whether `Critical` covers confidentiality (`DEF-028`, `DEF-029`), the W5 requirement mapping and the proposed risk re-scores (R-02, R-05, R-08, R-10, R-11).
2. **Week 3 usability review:** `TC-USA-001` to `005` (and the severities of `USA-OBS-001` to `004`). Compatibility C07 is blocked by default.
3. **Source commits:** record the commit of each source file copied into the master repository.
4. **Group decisions:** whether `completed_in_last_n_days` (exclusive `<` against an inclusive docstring) becomes a new defect (it would now be `DEF-038`); W2 requirement mapping sign-off; confirm risk re-scores; confirm role assignments.
5. **Check `helpers.py`** before stating the code-level cause of `DEF-002` (the log currently cites only what W2 recorded).
6. **risk_register.md** was updated for Week 5 (R-10 and R-11 filled in; re-scores of R-02, R-05 and R-08 proposed). Its other references to `DEF-` IDs, counts and requirement meanings still need a check against the corrected files.
