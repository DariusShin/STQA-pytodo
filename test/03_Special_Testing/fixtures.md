# Week 3 - Shared Preconditions and Test Data

Reference data for every Week 3 test-case file:

| Technique | Cases |
| --- | --- |
| [1_GUI/test_cases.md](1_GUI/test_cases.md) | TC-GUI-001 to 022 |
| [2_Compatibility/test_cases.md](2_Compatibility/test_cases.md) | TC-CMP-001 to 008 |
| [3_Usability/test_cases.md](3_Usability/test_cases.md) | TC-USA-001 to 005 |
| [4_Accessibility/test_cases.md](4_Accessibility/test_cases.md) | TC-A11Y-001 to 018 |

## Test-case template

Every case uses the fields from the project guideline:

| Field | Required Information |
| --- | --- |
| Test Case ID | Unique identifier, e.g. `TC-GUI-001` |
| Feature/Requirement | Week 1 requirement (`REQ-001` to `REQ-008`), page, or WCAG success criterion |
| Technique/Test Type | GUI checklist, Compatibility, Usability - heuristic evaluation, or Accessibility (WCAG) |
| Objective | What the test verifies |
| Preconditions | Required initial state; codes are defined in [Shared preconditions](#shared-preconditions) |
| Test Data | Input values in JSON format; fixture IDs refer to [Fixture sets](#fixture-sets) |
| Steps | Numbered procedure |
| Expected Result | Expected behaviour defined before execution, with its basis |
| Actual Result | Observed behaviour |
| Status | Pass / Fail / Blocked / Not Run |
| Evidence | Planned screenshot or report filename |
| Defect ID | Related defect, or an earlier defect to re-check |

## Shared preconditions

| Code | Meaning |
| --- | --- |
| P-APP | `python app.py` is running at `http://127.0.0.1:5000` from the recorded commit. Configuration C01 (Chrome on macOS, 1440x900 window) unless the case says otherwise |
| P-OUT | P-APP, and the browser is logged out (open `/logout` first) |
| P-A | P-APP, logged in as account A with [Fixture Set A](#fixture-set-a---gui-and-accessibility) seeded on the execution day |
| P-C | P-APP, logged in as account C, which has no tasks |
| P-VO | VoiceOver is on (Command-F5) and Chrome is the active window |

## Fixture sets

**Source of truth:** [fixtures.json](fixtures.json) holds the machine-readable data loaded by `conftest.py`: accounts, Fixture Set A, the browser configurations and each case's test data. This page describes the same data for readers. Change the JSON first, then this page.

Relative dates such as `today+2` are calculated on the execution day and entered as `YYYY-MM-DD`. The automated suites seed accounts and tasks through the JSON API (`POST /api/register`, `POST /api/tasks`, `PUT /api/tasks/<id>` for F6). Manual runs may seed through the web UI; record which method was used.

### Accounts

| Account | Username | Password | Tasks |
| --- | --- | --- | --- |
| A | `w3<initial>_gui_<mmddHHMM>`, e.g. `w3d_gui_11181933` | `Test12345` | Fixture Set A |
| C | `w3<initial>_empty_<mmddHHMM>` | `Test12345` | None |
| Per configuration | `w3<initial>_<config>_<mmddHHMM>`, e.g. `w3d_c01_11181931` | `Test12345` | Created during TC-CMP-001 |
| TC-GUI-004 submissions 2 and 3 | `w3<initial>_short_<mmddHHMM>`, `w3<initial>_p8_<mmddHHMM>` | As in the case | Created only if the submission is accepted |

The registration form does not reject duplicate usernames, and login uses the first match, so every run stamps its usernames with the run's start time (`<mmddHHMM>`) to stay unique. Usernames stay within the 20-character rule.

### Fixture Set A - GUI and accessibility

| ID | Title | Description | Category | Due date | State |
| --- | --- | --- | --- | --- | --- |
| F1 | `GUI-Overdue` | `Fixture overdue` | Work | today-3 | Open |
| F2 | `GUI-Today` | `Fixture due today` | Personal | today | Open |
| F3 | `GUI-Soon` | `Week 3 GUI fixture` | Study | today+2 | Open |
| F4 | `GUI-Upcoming` | (empty) | Urgent | today+7 | Open |
| F5 | `GUI-NoDate` | (empty) | None | (empty) | Open |
| F6 | `GUI-Done` | (empty) | Work | today+1 | Done (complete it after creating) |
| F7 | 200-character title, see below | (empty) | Personal | (empty) | Open |
| F8 | 60-character unbroken title, see below | (empty) | None | (empty) | Open |
| F9 | `GUI-Special & <b>bold</b> "double" 'single' Résumé 报告` | (empty) | Study | (empty) | Open |

The F7 and F8 titles are stored literally in `fixtures.json`; they were generated with:

```bash
python3 -c "print(('GUI-Long ' + 'quarterly report review ' * 9)[:200])"   # F7, 200 characters
python3 -c "print('GUI-Unbroken-' + 'A' * 47)"                             # F8, 60 characters
```

F9 contains HTML tags only to check that text is displayed literally. Do not enter `<script>` or event-handler payloads in Week 3; script behaviour belongs to the Week 5 security tests.
