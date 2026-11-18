# Week 3 - Usability Test Cases

Detailed cases for [Task 3 - Usability observations](../README.md#task-3) of the [Week 3 plan](../README.md). Each case uses the guideline's test-case template fields. Precondition codes (P-APP, P-OUT, P-A, P-C), test accounts and fixture IDs (F1-F9) are defined in [fixtures.md](../fixtures.md). Every case is `Not Run` until executed; fill in Actual Result, Status, Evidence and Defect ID only after execution, and replace `<YYYYMMDD>` in evidence filenames with the execution date.

## Review sign-off

Expected results must be reviewed before execution (plan step 3). The reviewer checks that each expected result cites a basis from [README 0.3](../README.md#03-test-basis) and was not derived from observed behaviour.

| Reviewer | Date | Cases reviewed | Changes requested | Approved |
| --- | --- | --- | --- | --- |
| | | TC-USA-001 to 005 | | |

## Case index

| ID | Title |
| --- | --- |
| [TC-USA-001](#tc-usa-001---ease-of-navigation) | Ease of navigation |
| [TC-USA-002](#tc-usa-002---feedback) | Feedback |
| [TC-USA-003](#tc-usa-003---consistency) | Consistency |
| [TC-USA-004](#tc-usa-004---error-prevention) | Error prevention |
| [TC-USA-005](#tc-usa-005---understandability) | Understandability |

## How to run

**Method: two-reviewer heuristic evaluation.** There are no end-user participants and no automation. Each case covers one of the five usability qualities named in the project guideline, mapped to Nielsen's heuristics. Each case is applied to all six pages: `/login`, `/register`, `/` (task list), `/tasks/new`, `/tasks/<id>/edit` and `/dashboard`, together with the shared navigation bar.

| Role | Member |
| --- | --- |
| Reviewer 1 | Eu Kwan Ik |
| Reviewer 2 | Ameera Alysha binti Azlan |

**Procedure for every case:**

1. Each reviewer works **independently**, on C01 with account A and Fixture Set A, and performs each page's main actions as a first-time user would.
2. The reviewer answers the case's guiding questions for every page and records each problem in their own notes: page, element, description, the heuristic it breaks, a severity from 0 to 4, and a screenshot.
3. The two reviewers then meet and merge their notes. They remove duplicates and agree a severity for each problem; if they cannot agree, the higher rating is used and both ratings are recorded.
4. Each merged problem is logged as a `USA-OBS-` item in the [README 3.3 observation log](../README.md#33-observation-log).
5. The case verdict follows the fixed threshold below.

**Severity scale (Nielsen):** 0 not a usability problem; 1 cosmetic; 2 minor; 3 major; 4 catastrophic.

**Verdict threshold (fixed before the review):** a case **fails** if any merged observation for its quality is rated **3 or 4**. Otherwise it **passes**, even if observations rated 1 or 2 are logged. A failed case links each severity 3-4 observation, and a `DEF-` record is raised only when the observation also breaks a stated requirement or interface promise.

**Inputs from other techniques:** findings from [TC-GUI-017](../1_GUI/test_cases.md#tc-gui-017---feedback-after-actions) (feedback after actions) and the username-retention observation in [TC-GUI-002](../1_GUI/test_cases.md#tc-gui-002---login-error-message) are fed into TC-USA-002 and TC-USA-004 respectively, so that the same problem is not counted twice.

## TC-USA-001 - Ease of navigation

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-001 |
| Feature/Requirement | All pages and the navigation bar; REQ-002, REQ-003, REQ-007 |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess how easily a user can move between pages and get back from any page. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H6 Recognition rather than recall", "H3 User control and freedom"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Guiding questions for each page: Can every main page be reached from the navigation bar? Is it clear which page you are on? Is there always a way back or a Cancel option? Can a user who opens a form by mistake leave it without losing other work? |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (ease of navigation); Nielsen heuristics 3 and 6. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-001-<reviewer-initials>-<YYYYMMDD>.md` (one notes file per reviewer) plus screenshots `evidences/TC-USA-001-<short-desc>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-USA-002 - Feedback

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-002 |
| Feature/Requirement | All pages; REQ-001 to REQ-004 |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess whether the application tells the user what happened after every action. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H1 Visibility of system status"], "actions": ["register", "log in", "log out", "create", "edit", "complete", "reopen", "delete", "filter", "search"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Perform each action in Test Data.<br>3. Guiding questions for each action: Does the page show that the action succeeded or failed? Is the result visible without searching for it? Are active filters and search terms clearly shown? Include the TC-GUI-017 findings (H6). |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (feedback); Nielsen heuristic 1. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-002-<reviewer-initials>-<YYYYMMDD>.md` plus screenshots `evidences/TC-USA-002-<short-desc>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-USA-003 - Consistency

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-003 |
| Feature/Requirement | All pages |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess whether wording, controls and layout are consistent across pages and with common web conventions. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H4 Consistency and standards"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Guiding questions: Are the same actions named the same way everywhere (for example `Log in` and `Log out`, `Create Task` and `Save Changes`)? Do buttons with the same role look and sit in the same place? Do controls behave as users expect from other websites (for example, do filters apply on change or on a button)? Use [TC-GUI-022](../1_GUI/test_cases.md#tc-gui-022---visual-consistency) results as input for visual styling. |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (consistency); Nielsen heuristic 4. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-003-<reviewer-initials>-<YYYYMMDD>.md` plus screenshots `evidences/TC-USA-003-<short-desc>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-USA-004 - Error prevention

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-004 |
| Feature/Requirement | `/register`, `/login`, task forms, delete; REQ-001 to REQ-003 |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess whether the interface prevents mistakes and helps users recover from them. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H5 Error prevention", "H9 Help users recognise, diagnose and recover from errors"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Guiding questions: Are input rules shown before the user types? Are destructive actions (delete) confirmed? Can completing a task by mistake be undone easily? Do error messages say what went wrong and how to fix it? Are entered values kept after an error, so the user does not retype them? Include the TC-GUI-002 username-retention observation. |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (error prevention); Nielsen heuristics 5 and 9. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-004-<reviewer-initials>-<YYYYMMDD>.md` plus screenshots `evidences/TC-USA-004-<short-desc>-<YYYYMMDD>.png` |
| Defect ID | — |

## TC-USA-005 - Understandability

| Field | Required Information |
| --- | --- |
| Test Case ID | TC-USA-005 |
| Feature/Requirement | All pages; REQ-004, REQ-006, REQ-007 |
| Technique/Test Type | Usability - heuristic evaluation |
| Objective | Assess whether labels, symbols and terms are understandable without explanation. |
| Preconditions | P-OUT for `/login` and `/register`; P-A for the other pages |
| Test Data | {"heuristics": ["H2 Match between system and the real world", "H8 Aesthetic and minimalist design"], "reviewers": ["Eu Kwan Ik", "Ameera Alysha binti Azlan"]} |
| Steps | 1. Follow the shared procedure.<br>2. Guiding questions: Are the urgency names (Overdue, Due Today, Due Soon, Upcoming, No due date, Done) clear without a definition? Is the `○`/`✓` control recognisable as "mark complete"? Are the dashboard counters clear, including what "Completed (last 7 days)" counts? Does any page show information that is irrelevant or distracting? |
| Expected Result | No merged observation for this quality is rated 3 or 4. Basis: guideline activity A3 (understandability); Nielsen heuristics 2 and 8. |
| Actual Result | Not executed. |
| Status | Not Run |
| Evidence | `evidences/TC-USA-005-<reviewer-initials>-<YYYYMMDD>.md` plus screenshots `evidences/TC-USA-005-<short-desc>-<YYYYMMDD>.png` |
| Defect ID | — |
