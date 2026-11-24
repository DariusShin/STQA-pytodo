# Week 3 - Usability Review Kit

Everything the two reviewers need to run [TC-USA-001 to 005](test_cases.md). The method, severity scale and verdict rule are defined in [test_cases.md](test_cases.md#how-to-run); this kit adds the setup, the inputs and the note-taking workflow.

| Role | Member | Initials for filenames |
| --- | --- | --- |
| Reviewer 1 | Eu Kwan Ik | `EKI` |
| Reviewer 2 | Ameera Alysha binti Azlan | `AAA` |

## 1. Rules for an independent review

- Review **separately**. Do not compare notes until both reviewers have finished all five cases.
- Judge what you see, not what you know about the code or earlier defects.
- Use the same configuration as the baseline: C01, Google Chrome on macOS in a 1440x900 window (or the closest window size available). Record the browser version in each notes file.
- Rate each problem on its own before reading the four GUI-suite observations in [section 4](#4-inputs-from-the-gui-suite), so they do not anchor your ratings.

## 2. Set up a review account

Each reviewer uses their own freshly seeded account, so the pages show the same Fixture Set A data that the automated suites used.

```bash
# Terminal 1, from the repository root: start the application
python app.py

# Terminal 2, from the repository root: create and seed your account
python test/03_Special_Testing/seed_fixtures.py --initial e     # Eu Kwan Ik
python test/03_Special_Testing/seed_fixtures.py --initial a     # Ameera
```

The script prints the username and password to log in with (`Test12345`). It needs only Python's standard library. Due dates are calculated from the day the script runs, so seed on the review day.

## 3. Workflow for each case

1. Copy [notes_template.md](notes_template.md) to `evidences/TC-USA-0xx-<initials>-<YYYYMMDD>.md`, e.g. `evidences/TC-USA-002-EKI-20261120.md`.
2. Visit the six pages in order: `/login`, `/register`, `/` (task list), `/tasks/new`, `/tasks/<id>/edit`, `/dashboard`, plus the shared navigation bar. Perform each page's main actions as a first-time user would.
3. Answer the case's guiding questions from [test_cases.md](test_cases.md) for every page, and record each problem in a row of the findings table.
4. Save a screenshot for each problem as `evidences/TC-USA-0xx-<short-desc>-<YYYYMMDD>.jpg` (Shift-Command-4 on macOS, Win+Shift+S on Windows) and link it from the row.
5. When both reviewers have finished all five cases, meet and merge (section 5).

| Case | Quality | Guiding questions |
| --- | --- | --- |
| [TC-USA-001](test_cases.md#tc-usa-001---ease-of-navigation) | Ease of navigation | Can every page be reached? Is the current page clear? Is there always a way back or a Cancel? |
| [TC-USA-002](test_cases.md#tc-usa-002---feedback) | Feedback | Does every action show it succeeded or failed? Are active filters visible? |
| [TC-USA-003](test_cases.md#tc-usa-003---consistency) | Consistency | Same names, styles and positions for the same actions? Controls behave as on other sites? |
| [TC-USA-004](test_cases.md#tc-usa-004---error-prevention) | Error prevention | Rules shown before input? Destructive actions confirmed? Errors explain the fix? Entered values kept? |
| [TC-USA-005](test_cases.md#tc-usa-005---understandability) | Understandability | Urgency names, the `○`/`✓` control and dashboard counters clear without explanation? |

**Severity scale (Nielsen):** 0 not a usability problem; 1 cosmetic; 2 minor; 3 major; 4 catastrophic. A case fails if any merged observation for its quality is rated 3 or 4.

## 4. Inputs from the GUI suite

Read these **after** your own review of the matching case, then confirm or reject each one and give it your own severity in the merge.

| Observation | Case | Finding | Evidence |
| --- | --- | --- | --- |
| USA-OBS-001 | TC-USA-002 | No confirmation message or highlight after creating, editing, completing or deleting a task | [create](../1_GUI/evidences/TC-GUI-017-feedback-create-20261118.jpg), [edit](../1_GUI/evidences/TC-GUI-017-feedback-edit-20261118.jpg), [complete](../1_GUI/evidences/TC-GUI-017-feedback-complete-20261118.jpg), [delete](../1_GUI/evidences/TC-GUI-017-feedback-delete-20261118.jpg) |
| USA-OBS-002 | TC-USA-003 | `Completed (last 7 days)` card is green while completed tasks use a grey `Done` badge | [dashboard](../1_GUI/evidences/TC-GUI-018-dashboard-20261118.jpg), [badges](../1_GUI/evidences/TC-GUI-010-badges-20261118.jpg) |
| USA-OBS-003 | TC-USA-003 | Button, link, heading and card styles differ between pages | [login](../1_GUI/evidences/TC-GUI-022-consistency-login-20261118.jpg), [task list](../1_GUI/evidences/TC-GUI-022-consistency-list-20261118.jpg), [dashboard](../1_GUI/evidences/TC-GUI-022-consistency-dashboard-20261118.jpg) |
| USA-OBS-004 | TC-USA-004 | The username field is emptied after a login or registration error | [login error](../1_GUI/evidences/TC-GUI-002-login-error-20261118.jpg), [registration error](../1_GUI/evidences/TC-GUI-004-register-errors-s1-20261118.jpg) |

Related defects already logged, for context only: DEF-001 (8-character password rejected), DEF-002 (due-today task shown as Overdue), DEF-003 (whitespace-only title accepted), DEF-004 and DEF-006 (narrow screens), DEF-008 (unnamed `○`/`✓` button). If a usability problem is the same as a defect, note the defect ID instead of logging a duplicate.

## 5. Merge and report

1. List every problem from both reviewers' notes. Merge duplicates.
2. Agree one severity per problem. If you cannot agree, use the higher rating and record both.
3. Add each merged problem to the [README 3.3 observation log](../README.md#33-observation-log) as `USA-OBS-005` onwards, or update USA-OBS-001 to 004 with the agreed severity.
4. Fill the [README 3.1 review cases](../README.md#31-review-cases) table (observations, highest severity, status) and the [3.2 merge record](../README.md#32-merge-record-complete-after-the-review).
5. Fill Actual Result, Status, Evidence and Defect ID for each case in [test_cases.md](test_cases.md).
6. Raise a `DEF-` record (README Task 5) only when a problem also breaks a stated requirement or interface promise.
