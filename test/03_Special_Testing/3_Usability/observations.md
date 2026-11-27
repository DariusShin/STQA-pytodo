# Week 3 - Usability Observations

Short usability session on **2026-11-26** with PyTodo Pro running locally (`python app.py`, `http://127.0.0.1:5000`).

| Role | Member |
| --- | --- |
| Users | Eu Kwan Ik, Ameera Alysha binti Azlan |
| Recorders | Darius Lee Shin, Mohamad Shukri Bin Abdul Ajed |

The users carried out the everyday tasks: register, log in, create, edit, complete and delete tasks, filter and search, and view the dashboard. The recorders noted what they experienced. The problems the users met matched the four usability issues already found by the GUI suite (2026-11-18, C01), so each was mapped to a Nielsen heuristic and given an agreed severity. Summary: [W3_Report.md section 4](../W3_Report.md#4-usability-observations).

## Severity scale (Nielsen, 0-4)

Severity combines **frequency** (how often users meet the problem), **impact** (how hard it is to overcome) and **persistence** (whether it keeps recurring once users know about it).

| Rating | Meaning | Fix guidance |
| --- | --- | --- |
| 0 | Not a usability problem | None |
| 1 | Cosmetic | Fix only if time allows |
| 2 | Minor | Low priority |
| 3 | Major | High priority |
| 4 | Catastrophe | Must fix before release |

An observation rated 3 or 4 is logged as a defect; ratings 0-2 stay as observations with a recommendation.

## Observations

| ID | Guideline quality | Nielsen heuristic | Page | Observation | Source case | Severity | Rationale | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| USA-OBS-001 | Feedback | 1 Visibility of system status | All task actions | No confirmation message or highlight after creating, editing, completing or deleting a task | TC-GUI-017 | **2 Minor** | Frequent (every action) and persistent, but low impact: the list visibly changes | [TC-GUI-017](../1_GUI/evidences/TC-GUI-017-feedback-create-20261118.jpg) | Show a short confirmation after each action (R3) |
| USA-OBS-002 | Consistency | 4 Consistency and standards | `/dashboard` | `Completed (last 7 days)` card is green while completed tasks use a grey `Done` badge | TC-GUI-018 | **1 Cosmetic** | Visual only; no task is blocked or misread | [TC-GUI-018](../1_GUI/evidences/TC-GUI-018-dashboard-20261118.jpg) | Use one colour for "completed" (R5) |
| USA-OBS-003 | Consistency | 4 Consistency and standards | All pages | Primary buttons differ (`+ New Task` font size, `Filter` colour and size); auth-page links use browser-default blue; auth headings 22.4 px vs 32 px; card corners 12 px vs 10 px | TC-GUI-022 | **1 Cosmetic** | Visual only; no task is blocked | [TC-GUI-022](../1_GUI/evidences/TC-GUI-022-consistency-list-20261118.jpg) | One style per control type on every page (R5) |
| USA-OBS-004 | Error prevention / recovery | 9 Help users recover from errors | `/login`, `/register` | After a login or registration error the username field is emptied, so the user must retype it | TC-GUI-002, TC-GUI-004 | **2 Minor** | Occasional (only after an error), low impact (retype), but happens on every failed attempt | [TC-GUI-004](../1_GUI/evidences/TC-GUI-004-register-errors-s1-20261118.jpg) | Keep the entered username after an error (R4) |

No observation reached severity 3, so no usability defect was logged.
