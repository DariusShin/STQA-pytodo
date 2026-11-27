# 01_Black_Box - Application Analysis and Black-Box Testing

Week 1 analyses PyTodo Pro's features, users and risks, then tests the web interface manually with Equivalence Partitioning, Boundary Value Analysis, decision tables and state transitions.

| File / folder | Contents |
| --- | --- |
| [W1_Report.md](W1_Report.md) | Week 1 report: feature inventory, risk matrix, RTM, technique justification, results |
| [test_cases.md](test_cases.md) | 44 manual cases, TC-BB-001 to TC-BB-044 |
| [defects.md](defects.md) | DEF-001 to DEF-003 |
| [evidences/](evidences/) | One screenshot per case (`TC-BB-0NN.jpg`), input screenshots (`-input.jpg`) and dataset screenshots |

## How to run

1. Start the app from the repository root: `python app.py`, then open `http://127.0.0.1:5000` in Chrome.
2. Register the test accounts listed in [W1_Report.md](W1_Report.md#test-accounts). Use new suffixes on a re-run so existing data is not reused.
3. Follow the numbered steps of each case in [test_cases.md](test_cases.md). Recalculate date-based inputs (urgency cases TC-BB-036 to 043) from the day of the run.
4. Save one screenshot per case in `evidences/` as `TC-BB-0NN.jpg` and record the actual result and status.
