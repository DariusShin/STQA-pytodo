# 04_Web_API - Web and API Testing

Week 4 tests the nine JSON endpoints and the data-changing web routes with a Postman collection: valid and invalid requests, status codes and response bodies, server-side validation of the web forms, and a comparison of web and API behaviour.

| File / folder | Contents |
| --- | --- |
| [W4_Report.md](W4_Report.md) | Week 4 report: scope, web scenarios, API suite, endpoint inventory, RTM, expected vs actual, UI vs API comparison |
| [test_cases.md](test_cases.md) | 61 cases: TC-WEB-001 to 016, TC-API-001 to 045 |
| [test_data.md](test_data.md) | Accounts, input partitions and boundaries, datasets |
| [defects.md](defects.md) | DEF-014 to DEF-023, and re-tests of DEF-001 to DEF-003 |
| [postman/](postman/) | `PyTodo_Pro_Week4.postman_collection.json` (190 requests) and `PyTodo_Local.postman_environment.json` |
| [evidences/](evidences/) | Full runner result `postman-run-full-20261124.json`, run summary screenshot, one screenshot per defect |
| `STQA_Week4_Web_API_Report.docx` | Word summary of the Week 4 results |

## How to run

1. Delete `pytodo_pro.db` in the repository root, then start the app from the repository root: `python app.py`.
2. In Postman, **Import** both files from `postman/` and select the **PyTodo Local** environment.
3. Collection **...** -> **Run collection**: all requests, 1 iteration, in order. Folder 99 runs last on purpose (it leaves a test user unable to load their list, DEF-015).

Expected on the current code: 339 checks, 276 passed, 63 failed. Each folder registers its own users, so a single folder can also be run on its own.

Command line alternative: `npm install -g newman`, then `newman run postman/PyTodo_Pro_Week4.postman_collection.json -e postman/PyTodo_Local.postman_environment.json`.
