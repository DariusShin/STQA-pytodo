# PyTodo Pro

## Evaluating the submission

All test deliverables are in [`test/`](test/). The application files in the repository root are unchanged.

1. Start with [test/README.md](test/README.md): team and roles, folder structure, and a map of every week with links to its report, test cases, defects and evidence.
2. Evaluate each week in its folder, `test/01_Black_Box/` to `test/09_Presentation/`. The graded deliverable is the week's report, `WN_Report.md` (for example [W1_Report.md](test/01_Black_Box/W1_Report.md)), supported by `test_cases.md`, `defects.md` and `evidences/` in the same folder.
3. Read the reports in Markdown preview, not as raw text, so that tables, images and links display. Open them on GitHub, or in VS Code with **Markdown: Open Preview** (`Cmd+Shift+V` on macOS, `Ctrl+Shift+V` on Windows).

No tests need to be run to evaluate the reports: results, tool reports and screenshots are already committed in each week's `evidences/`, and the Week 2 coverage report is in `test/02_White_Box_Coverage/htmlcov/`. To re-run a week's tests, follow the "How to run" section of that week's `README.md`.

## About the application

A complete, ready-to-test Flask task manager — the target application
for the course testing project. **You do not need to write or modify
any application code.** Your job is to test it.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The app creates `pytodo_pro.db` on first run and serves at
`http://127.0.0.1:5000/`. Register a new account from the web UI (or
via `POST /api/register`) to get started — there is no pre-seeded
login.

## What's here

### Web UI
- `/register`, `/login`, `/logout` — account management
- `/` — task list, with filters for category, status (open/done), and a title search box
- `/tasks/new`, `/tasks/<id>/edit` — create and edit tasks
- `/dashboard` — summary counters (total, open, overdue, due soon, completed in the last 7 days)

### JSON REST API (all under `/api`, session-cookie authenticated except register/login)
- `POST /api/register` — `{"username": ..., "password": ...}`
- `POST /api/login` — `{"username": ..., "password": ...}`
- `GET /api/categories`
- `GET /api/tasks?category=&status=&q=&page=&per_page=`
- `POST /api/tasks` — `{"title": ..., "description": ..., "category_id": ..., "due_date": "YYYY-MM-DD"}`
- `GET /api/tasks/<id>`
- `PUT /api/tasks/<id>` — partial updates accepted
- `DELETE /api/tasks/<id>`
- `GET /api/dashboard`

### Data model
- **users**: id, username, password_hash
- **categories**: id, name (seeded with Work, Personal, Study, Urgent)
- **tasks**: id, user_id, title, description, category_id, due_date, done, completed_at, created_at

### Task urgency
Each task is classified as one of: `No due date`, `Overdue`, `Due Today`,
`Due Soon` (due within 2 days), `Upcoming`, or `Done`. The exact rules
are implemented in `helpers.py` — a good place to start if you're
designing white-box test cases.

## A note on quality

This app was built to be tested, not audited by its author. Treat it
the way you would treat a real, working piece of software handed to a
QA team: it does what it's supposed to do in the common cases — your
job across the testing phases is to find out where that stops being
true.
