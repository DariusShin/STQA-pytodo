# Week 3 - GUI, Compatibility, Usability and Accessibility Testing

| Item | Recorded value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / Lab Group | September 2026 / Wednesday Lab - Group 2 |
| Phase status | In progress - Task 1 (GUI) executed on C01, and Task 2 executed on C01-C03, on 2026-11-18 by the Playwright suites; C04-C06, usability and accessibility not yet run |

## Deliverable Checklist

- [ ] [Task 1](#task-1) - GUI testing checklist/results.
- [ ] [Task 2](#task-2) - Compatibility/configuration matrix.
- [ ] [Task 3](#task-3) - Usability observations.
- [ ] [Task 4](#task-4) - Basic accessibility findings.
- [ ] [Task 5](#task-5) - Defects and improvement recommendations.

Tick a task only after its results, evidence and peer review are complete. Every planned case below is `Not Run` until it is executed; do not record an actual result before execution.

## Deliverable structure

This README is the single phase report: the plan, every summary table and matrix, and the Task 5 defects and recommendations. Each technique folder holds the detailed cases and the evidence that backs up the report.

```
03_Special_Testing/
├── README.md            ← this report
├── fixtures.md          ← test-case template, precondition codes, accounts, Fixture Set A (readable form)
├── fixtures.json        ← the same test data, loaded by the scripts
├── conftest.py, pytest.ini, setup.md, requirements-test-lock.txt  ← Playwright/pytest harness and run guide
├── 1_GUI/               ← Task 1: test_cases.md (TC-GUI-001 to 022), test_gui.py + evidences/
├── 2_Compatibility/     ← Task 2: test_cases.md (TC-CMP-001 to 008), test_compatibility.py + evidences/<os>-<browser>/<viewport>/
├── 3_Usability/         ← Task 3: test_cases.md (TC-USA-001 to 005) + evidences/
└── 4_Accessibility/     ← Task 4: test_cases.md (TC-A11Y-001 to 018) + evidences/ and evidences/reports/
```

| Deliverable (guideline) | Report section | Detailed cases | Evidence |
| --- | --- | --- | --- |
| GUI testing checklist/results | [Task 1](#task-1) | [1_GUI/test_cases.md](1_GUI/test_cases.md) | `1_GUI/evidences/` |
| Compatibility/configuration matrix | [Task 2](#task-2) | [2_Compatibility/test_cases.md](2_Compatibility/test_cases.md) | `2_Compatibility/evidences/` |
| Usability observations | [Task 3](#task-3) | [3_Usability/test_cases.md](3_Usability/test_cases.md) | `3_Usability/evidences/` |
| Basic accessibility findings | [Task 4](#task-4) | [4_Accessibility/test_cases.md](4_Accessibility/test_cases.md) | `4_Accessibility/evidences/` |
| Defects and improvement recommendations | [Task 5](#task-5) | Drawn from Tasks 1-4 | Linked from each defect |

**Execution strategy.** The GUI and compatibility cases are executed by Playwright scripts run with pytest (`1_GUI/test_gui.py`, `2_Compatibility/test_compatibility.py`), decided by the team on 2026-11-18. Each script performs the documented steps, checks the expected result written in `test_cases.md` before execution, saves `.jpg` evidence and writes a per-run results file listing every check with its actual value. Visual judgements are recorded as notes and judged from the screenshots. The usability review and the screen-reader parts of accessibility stay manual. Setup and run commands are in [setup.md](setup.md). Week 6 can reuse these scripts as regression candidates.

## Task 0 - Phase plan

### 0.1 Required activities from the project guideline

| # | Guideline activity | Covered by |
| --- | --- | --- |
| A1 | Evaluate forms, buttons, links, labels, navigation, messages and visual consistency | [Task 1](#task-1) |
| A2 | Test selected browser/configuration combinations available to the group | [Task 2](#task-2) |
| A3 | Evaluate ease of navigation, feedback, consistency, error prevention and understandability | [Task 3](#task-3) |
| A4 | Conduct a basic accessibility review using WCAG concepts introduced in class | [Task 4](#task-4) |
| A5 | Document issues with screenshots and reproducible evidence | All tasks; defects in [Task 5](#task-5) |

### 0.2 Scope

| In scope | Out of scope (phase that owns it) |
| --- | --- |
| The six rendered pages: `/login`, `/register`, `/` (task list), `/tasks/new`, `/tasks/<id>/edit`, `/dashboard` | JSON REST API behaviour and status codes (Week 4) |
| Shared layout: top navigation bar, page titles, buttons, badges, messages | Script injection and other security behaviour, even when found through the UI (Week 5) |
| Selected browsers and viewports available to the group | Load and response-time measurement (Week 5) |
| Keyboard, screen-reader and contrast checks against a WCAG 2.2 Level A/AA subset | Regression-suite selection and CI integration (Week 6) |
| Re-checking DEF-001 to DEF-003 where they surface in the GUI | Full WCAG conformance audit or certification |
| Usability by expert heuristic review | Usability testing with end-user participants |

Functional correctness was established in Week 1. This phase asks a different question: does each page present that behaviour clearly, consistently and accessibly across configurations?

### 0.3 Test basis

Expected results must be written before execution and must cite one of these sources:

1. The interface itself: visible labels, hints and button text (for example, `min 8 characters` on Register).
2. The project `README.md` page and feature list.
3. Week 1 requirements `REQ-001` to `REQ-008` and assumptions in [01_Black_Box/README.md](../01_Black_Box/README.md).
4. WCAG 2.2 success criteria for accessibility cases.
5. Usability heuristics introduced in class (Nielsen's 10 heuristics) for usability cases.

### 0.4 Test case ID conventions

| Prefix | Use | Planned range | Defined in |
| --- | --- | --- | --- |
| `TC-GUI-` | GUI checklist cases | 001-022 | [1_GUI/test_cases.md](1_GUI/test_cases.md) |
| `TC-CMP-` | Compatibility smoke scenarios, run once per configuration | 001-008 | [2_Compatibility/test_cases.md](2_Compatibility/test_cases.md) |
| `TC-USA-` | Usability heuristic review, one case per guideline quality | 001-005 | [3_Usability/test_cases.md](3_Usability/test_cases.md) |
| `USA-OBS-` | Usability observations from the heuristic review | from 001 | [3.3](#33-observation-log) |
| `TC-A11Y-` | Accessibility checks | 001-018 | [4_Accessibility/test_cases.md](4_Accessibility/test_cases.md) |
| `DEF-` | New defects, continuing the shared defect log | from `DEF-004` | [Task 5](#task-5) |

Each detailed case uses the full test-case template (ID, feature, technique, objective, preconditions, test data, steps, expected, actual, status, evidence, defect ID), following the Week 1 format. Each `test_cases.md` has its own review sign-off table. Shared precondition codes and test data are in [fixtures.md](fixtures.md).

### 0.5 Environment to record

Record these values at execution time. Do not copy versions from earlier weeks without checking them again.

| Component | Value |
| --- | --- |
| Application commit | `git rev-parse --short HEAD` at execution |
| Target | `python app.py` development server at `http://127.0.0.1:5000` |
| Operating systems | macOS 26.5.2 (build 25F84, checked 2026-10-27 with `sw_vers`); Windows 11 (record the build with `winver`) |
| Windows hardware | Acer Nitro 5 (2021) owned by Darius Lee Shin: AMD Ryzen 5 CPU, NVIDIA GTX 1650 GPU, 32 GB DDR4 RAM. Record the exact model number, CPU model, screen size and native resolution from `msinfo32` and Settings -> System -> Display |
| Browsers | macOS: Google Chrome 157.0.8103.80 (checked 2026-11-18; Week 1 used 155.0.8059.80), Mozilla Firefox 160.0.1 (installed 2026-11-18). Windows: record in the [configuration matrix](#21-configurations) |
| Automation | Python 3.14.7, pytest 9.1.1, pytest-playwright 0.10.0, Playwright 1.65.2 driving the installed Chrome through the `chrome` channel, headless; full set in `requirements-test-lock.txt` |
| Viewports | Device-mode preset name and CSS pixel size |
| Accessibility tools | Lighthouse (bundled with Chrome); axe DevTools extension (installed 2026-11-18; record its version); VoiceOver (macOS) / NVDA version |
| Test accounts | Synthetic accounts listed in [fixtures.md](fixtures.md#accounts); password `Test12345` |
| Execution date/time and timezone | Per run |

### 0.6 Test data set

The exact accounts, task titles, dates and generation commands are in [fixtures.md](fixtures.md#fixture-set-a---gui-and-accessibility). Fixture Set A is designed so that every page is checked in a populated state:

| Data item | Purpose |
| --- | --- |
| One task per urgency class: Overdue, Due Today, Due Soon, Upcoming, No due date, Done | Badge colour and text checks (TC-GUI-010, TC-A11Y-004) |
| One task in each category (Work, Personal, Study, Urgent) and one with no category | Filter and table rendering |
| A 200-character title and a 60-character unbroken title | Layout and wrapping (TC-GUI-019) |
| A title containing `&`, `<`, `>`, quotes and non-Latin text (e.g. `Résumé 报告`) | Literal display (TC-GUI-020) |
| A second, empty account (account C) | Empty-state checks (TC-GUI-009) |

### 0.7 Work allocation and schedule

Coordinators own the preparation and review of each task. Every member executes cases, so no member works on only one task.

| Task | Coordinator | Execution support |
| --- | --- | --- |
| Task 1 - GUI checklist | Mohamd Shukri Bin Abd Ajed (Test Design) | All members |
| Task 2 - Compatibility matrix | Darius Lee Shin (Automation/Tool) | Darius Lee Shin runs C04 on the MacBook and C05-C06 on the Windows 11 laptop (Acer Nitro 5); another member reviews the captures |
| Task 3 - Usability | Eu Kwan Ik (QA/Test Lead) | Heuristic reviewers: Eu Kwan Ik and Ameera Alysha binti Azlan, working independently, then merging |
| Task 4 - Accessibility | Darius Lee Shin (Automation/Tool) | Ameera Alysha binti Azlan (manual keyboard/screen-reader checks) |
| Task 5 - Defects and recommendations | Ameera Alysha binti Azlan (Defect & Metrics) | Eu Kwan Ik (review and final integration) |

| Step | Activity | Output |
| --- | --- | --- |
| 1 | Confirm the browsers and devices each member can use; fix the configuration matrix | [2.1](#21-configurations) filled in |
| 2 | Seed Fixture Set A; record the environment | [0.5](#05-environment-to-record) and [fixtures.md](fixtures.md) |
| 3 | Write detailed cases with expected results before execution (drafted 2026-10-27; split into technique folders 2026-11-18), then complete each review sign-off | Peer-reviewed cases |
| 4 | Execute GUI cases on the baseline configuration (C01) | [Task 1](#task-1) results - done 2026-11-18 |
| 5 | Run the compatibility smoke set on every configuration | [Task 2](#task-2) matrix - C01-C03 done 2026-11-18 |
| 6 | Run automated accessibility scans, then the manual keyboard, screen-reader and zoom checks | [Task 4](#task-4) findings |
| 7 | Run the two-reviewer heuristic review (TC-USA-001 to 005) and merge the findings | [Task 3](#task-3) observations |
| 8 | Reproduce each failure once more, log defects and draft recommendations | [Task 5](#task-5) |
| 9 | Peer review, check links, update the [phase status](../README.md#3-deliverable-structure-and-progress) and the shared defect log | Phase ready for review |

### 0.8 Entry and exit criteria

| Entry criteria | Exit criteria |
| --- | --- |
| Application starts locally and the seeded data set is in place | Every planned case is Pass, Fail, Blocked or Not Run, with a reason recorded for Blocked and Not Run |
| Configuration matrix agreed and browser versions recorded | Every Fail links to a defect or to an observation with a recorded rationale |
| Expected results written and reviewed before execution | Every defect has been reproduced at least twice and has screenshot evidence |
| Evidence folders created | Recommendations are prioritised and traced to defects or observations |

### 0.9 Evidence conventions

| Evidence | Location | Filename pattern |
| --- | --- | --- |
| GUI screenshots | `1_GUI/evidences/` | `<TC-ID>-<short-desc>-<YYYYMMDD>.jpg`, e.g. `TC-GUI-013-before-delete-20261118.jpg` |
| Compatibility captures | `2_Compatibility/evidences/<os>-<browser>/<viewport>/`, one folder per configuration in [2.1](#21-configurations) | `TC-CMP-0xx-<short-desc>-<YYYYMMDD>.jpg`; on emulated devices the capture shows the device screen |
| Usability reviewer notes and screenshots | `3_Usability/evidences/` | `TC-USA-0xx-<reviewer-initials>-<YYYYMMDD>.md` (one notes file per reviewer); screenshots `TC-USA-0xx-<short-desc>-<YYYYMMDD>.jpg` |
| Accessibility screenshots | `4_Accessibility/evidences/` | `<TC-ID>-<short-desc>-<YYYYMMDD>.jpg` |
| Lighthouse and axe reports | `4_Accessibility/evidences/reports/` | `<tool>-<page>-<YYYYMMDD>.html` or `.json` |
| Automated run results | The suite's evidence folder (configuration folder for compatibility) | `results-<config>-<YYYYMMDD>-<HHMMSS>.json` (runs before 20:25 on 2026-11-18 used `<HHMM>`) |

All screenshots use `.jpg`, matching the Week 1 evidence. Empty evidence folders contain a `.gitkeep` placeholder so the structure is visible before execution; remove it once the folder holds evidence.

#### Week 1 captures reused as supporting evidence

Before this phase, Week 1 black-box cases were re-run in Chrome on macOS at three viewport sizes. Those captures keep their `TC-BB-` filenames and are **supporting** evidence only: they were judged against Week 1 functional expected results, not against the TC-CMP cases. Every configuration therefore still gets a fresh TC-CMP run.

| Location | Content (checked 2026-11-18) | Use |
| --- | --- | --- |
| [01_Black_Box/evidences/](../01_Black_Box/evidences/) (72 files, 1440x900) | Week 1 desktop captures. A byte-identical copy previously kept under this phase was removed on 2026-11-18; link to the Week 1 folder instead | Supporting evidence for C01 |
| `2_Compatibility/evidences/mac-chrome/tablet/` (72 files, 768x1024) | Week 1 cases re-run with tablet accounts (`w1t_…`) | Supporting evidence for C02 |
| `2_Compatibility/evidences/mac-chrome/mobile/` (102 files, 390x844) | Week 1 cases re-run with mobile accounts (`w1m_…`); includes extra `-full-document` captures | Supporting evidence for C03 |

Fresh `TC-CMP-` captures are saved alongside the `TC-BB-` files in the same configuration folders; the filename prefix distinguishes them.

Before citing the tablet and mobile captures, the person who took them must record which DevTools mode they used: a **Responsive** window with device type Desktop, or a **device preset** such as iPhone 14 with mobile emulation. The 390 px captures show the page laid out at 390 px with normal-size text. Because the page has no viewport tag (H1), true mobile emulation or a real phone would normally lay it out at about 980 px and scale it down. The captures therefore probably came from a resized window and may not show H1. Re-check H1 with a Chrome device preset or a real phone (C07).

### 0.10 Pre-execution inspection notes

The templates (`templates/*.html`) and `static/style.css` were read while planning to target the cases below. These are **hypotheses to confirm in the browser, not defects**. Log one only after it has been reproduced and its user-facing effect observed.

| # | Observation from inspecting the source | Planned check | Result (2026-11-18) |
| --- | --- | --- | --- |
| H1 | `base.html` has no `<meta name="viewport">` tag, and the CSS has no `@media` rules | TC-CMP mobile/tablet runs; TC-A11Y-012 reflow | Confirmed by TC-CMP-007 on C02/C03: the page is laid out at 980 CSS px and scaled down, so text renders at 9.8 px (tablet) and 5.0 px (phone) (DEF-006) |
| H2 | Form `<label>` elements have no `for` attribute, and inputs have no `id`, so labels may not be programmatically associated | TC-A11Y-005, TC-A11Y-006 | Not yet checked (TC-A11Y-005) |
| H3 | The complete/reopen button's only content is `○` or `✓` | TC-A11Y-007 | Not yet checked (TC-A11Y-007) |
| H4 | The filter selects and search box have no visible labels; the search box has a placeholder only | TC-A11Y-006, TC-GUI-008 | Visible-label part confirmed by TC-GUI-008; accessible names pending TC-A11Y-006 |
| H5 | Calculated contrast: completed-task title and empty-state text `#999999` on white = 2.85:1 (WCAG 1.4.3 requires 4.5:1). Hint `#8d6e76` on white = 4.54:1 (borderline). Other text pairs checked were above 4.5:1 | TC-A11Y-004 with a contrast tool on the rendered page | Not yet measured (TC-A11Y-004) |
| H6 | No success message after create, edit, delete or complete; only login and register render an error message | TC-GUI-017, TC-USA-002 | Confirmed by TC-GUI-017 (USA-OBS-001) |
| H7 | Error messages have no `role="alert"` or live region | TC-A11Y-015 | Not yet checked (TC-A11Y-015) |
| H8 | No skip link before the navigation bar | TC-A11Y-009 | Not yet checked (TC-A11Y-009) |
| H9 | `index.html` renders the task title with the `safe` filter | TC-GUI-020 checks only literal display; pass any script behaviour to the Week 5 STRIDE table | Confirmed by TC-GUI-020: HTML tags in a title are rendered (DEF-005); hand-off to Week 5 |
| H10 | Seen in existing evidence [`mac-chrome/mobile/TC-BB-034.jpg`](2_Compatibility/evidences/mac-chrome/mobile/TC-BB-034.jpg): at 390 px the navigation bar is cramped. The brand wraps to `PyTodo / Pro`, `Log out` breaks across lines, and the links sit against the brand with no gap. This follows from `.topnav`/`.nav-links` being a non-wrapping flex row with fixed `2rem` side padding and no `@media` rule | TC-GUI-005 on C03, TC-CMP-007 on C02, C03 and C07, TC-A11Y-012 reflow. If confirmed, log it as a defect with a fresh dated capture | Confirmed in Chrome at a 390 px viewport by TC-GUI-005 (DEF-004); `Log out` is also pushed past the viewport edge |

H10 comes from a capture taken for a functional case, so it remains a hypothesis until a `TC-GUI-` or `TC-CMP-` case reproduces it. The same capture has the mouse pointer covering the `Filter` button. Move the pointer out of the way when capturing new Week 3 evidence.

## Task 1

### GUI testing checklist/results

**Method.** Executed on 2026-11-18 on the baseline configuration (C01: Chrome 157.0.8103.80 on macOS at 1440x900, headless) by [1_GUI/test_gui.py](1_GUI/test_gui.py), using Fixture Set A loaded from `fixtures.json`. Each row summarises one case; the full case is in [1_GUI/test_cases.md](1_GUI/test_cases.md) and its evidence in `1_GUI/evidences/`. Technique: GUI checklist.

| ID | Page / element | Check (objective) | Expected result (before execution) | Actual | Status | Evidence | Defect |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-GUI-001 | Login - layout | Heading, Username and Password fields, Log in button and Register link are present and aligned | All elements visible in one card; password input is masked | As expected; spacing consistent | Pass | [TC-GUI-001-login-layout-20261118.jpg](1_GUI/evidences/TC-GUI-001-login-layout-20261118.jpg) | — |
| TC-GUI-002 | Login - error message | Invalid credentials show an error | Visible error in a distinct box; user stays on `/login`; the message does not reveal which field was wrong | Error above the form in a red box; no field revealed; username field emptied | Pass | [TC-GUI-002-login-error-20261118.jpg](1_GUI/evidences/TC-GUI-002-login-error-20261118.jpg) | — |
| TC-GUI-003 | Register - hints | Field rules are visible before input | Hints `(3-20 chars, letters/numbers/underscore)` and `(min 8 characters)` are readable next to their labels | Both hints shown beside their labels | Pass | [TC-GUI-003-register-hints-20261118.jpg](1_GUI/evidences/TC-GUI-003-register-hints-20261118.jpg) | — |
| TC-GUI-004 | Register - error messages | Each invalid input produces a specific message | Each invalid submission stays on `/register` with a message naming the broken rule; an 8-character password is accepted as the hint states | s1 and s2 messages correct; the 8-character password (s3) is rejected; fields emptied after each error | Fail | [TC-GUI-004-register-errors-s1-20261118.jpg](1_GUI/evidences/TC-GUI-004-register-errors-s1-20261118.jpg) | DEF-001 (reproduced) |
| TC-GUI-005 | Navigation bar | Navigation differs by login state; items stay readable at every viewport | Logged in: Tasks, Dashboard, username, Log out. Logged out: brand only. No item text broken across lines (H10) | Correct items at both widths; at 390 px the brand and `Log out` wrap and `Log out` is pushed past the viewport edge | Fail | [TC-GUI-005-nav-logged-out-20261118.jpg](1_GUI/evidences/TC-GUI-005-nav-logged-out-20261118.jpg) | DEF-004 |
| TC-GUI-006 | Brand link | Brand link goes to the right place | Logged in -> `/`; logged out -> `/login` | As expected | Pass | [TC-GUI-006-brand-link-20261118.jpg](1_GUI/evidences/TC-GUI-006-brand-link-20261118.jpg) | — |
| TC-GUI-007 | Task list - header | Page heading and New Task button | `My Tasks` heading; `+ New Task` opens `/tasks/new` | As expected | Pass | [TC-GUI-007-list-header-20261118.jpg](1_GUI/evidences/TC-GUI-007-list-header-20261118.jpg) | — |
| TC-GUI-008 | Task list - filters | Filter controls behave predictably | Category/status selects apply on change; search applies on Filter button or Enter; selected values persist after reload | As expected; the filter controls have no visible labels (input for TC-A11Y-006) | Pass | [TC-GUI-008-filters-applied-20261118.jpg](1_GUI/evidences/TC-GUI-008-filters-applied-20261118.jpg) | — |
| TC-GUI-009 | Task list - table/empty state | Columns and empty-state message | Title, Category, Due Date and Urgency columns have headers; control columns are identifiable; an empty result shows a single "no tasks match" message in the table area | As expected; `No tasks match your filters.` for both empty cases | Pass | [TC-GUI-009-empty-search-20261118.jpg](1_GUI/evidences/TC-GUI-009-empty-search-20261118.jpg) | — |
| TC-GUI-010 | Urgency badges | Each urgency class has a distinct, labelled badge | Six badge texts shown; Overdue/Due Today/Due Soon/Upcoming are visually distinguishable | F2 (due today) shows `Overdue`; `Due Today` is never displayed; other badges correct and distinct | Fail | [TC-GUI-010-badges-20261118.jpg](1_GUI/evidences/TC-GUI-010-badges-20261118.jpg) | DEF-002 (reproduced) |
| TC-GUI-011 | Complete/reopen button | Button state matches the task state | `○` for open and `✓` for done; done row shown with strikethrough | As expected | Pass | [TC-GUI-011-toggle-done-20261118.jpg](1_GUI/evidences/TC-GUI-011-toggle-done-20261118.jpg) | — |
| TC-GUI-012 | Edit link | Edit opens a pre-filled form | Title, description, category and due date pre-filled with saved values | As expected | Pass | [TC-GUI-012-edit-prefill-20261118.jpg](1_GUI/evidences/TC-GUI-012-edit-prefill-20261118.jpg) | — |
| TC-GUI-013 | Delete confirmation | Delete asks for confirmation | A confirmation dialog appears; Cancel keeps the task, OK removes it | Dialog `Delete this task?` (text recorded); Cancel kept, OK removed | Pass | [TC-GUI-013-before-delete-20261118.jpg](1_GUI/evidences/TC-GUI-013-before-delete-20261118.jpg) | — |
| TC-GUI-014 | New Task form | Fields and controls | Title, Description, Category (None + 4) and Due Date date picker; Create Task and Cancel buttons | As expected; date picker present but not opened by automation | Pass | [TC-GUI-014-new-form-20261118.jpg](1_GUI/evidences/TC-GUI-014-new-form-20261118.jpg) | — |
| TC-GUI-015 | Edit Task form | Edit mode labelling | Heading `Edit Task` and button `Save Changes`; Cancel returns to `/` without saving | As expected | Pass | [TC-GUI-015-edit-form-20261118.jpg](1_GUI/evidences/TC-GUI-015-edit-form-20261118.jpg) | — |
| TC-GUI-016 | Required title | Empty and whitespace-only titles are blocked | Both are blocked with a visible message on Title; no task is created | Empty title blocked; a whitespace-only title creates a task | Fail | [TC-GUI-016-empty-title-20261118.jpg](1_GUI/evidences/TC-GUI-016-empty-title-20261118.jpg) | DEF-003 (reproduced) |
| TC-GUI-017 | Action feedback | Create, edit, delete and complete give visible confirmation | A confirmation message, or a visible highlight of the affected task, after each action; a failure is logged as a `USA-OBS-` item | No confirmation message or highlight after any of the four actions | Fail | [TC-GUI-017-feedback-create-20261118.jpg](1_GUI/evidences/TC-GUI-017-feedback-create-20261118.jpg) | USA-OBS-001 |
| TC-GUI-018 | Dashboard cards | Five counters with labels | Total Tasks, Open, Overdue, Due Soon, Completed (last 7 days); colours match the badge colours | Labels and layout correct; `Completed (last 7 days)` is green while the `Done` badge is grey | Fail | [TC-GUI-018-dashboard-20261118.jpg](1_GUI/evidences/TC-GUI-018-dashboard-20261118.jpg) | USA-OBS-002 |
| TC-GUI-019 | Long content | Long and unbroken titles do not break layout | Table stays within the container; no horizontal page scroll at 1440 px | As expected | Pass | [TC-GUI-019-long-content-20261118.jpg](1_GUI/evidences/TC-GUI-019-long-content-20261118.jpg) | — |
| TC-GUI-020 | Special characters | Titles display exactly as entered | `&`, `<`, `>`, quotes and non-Latin text displayed literally | `<b>bold</b>` rendered as bold text in the list; edit form correct | Fail | [TC-GUI-020-special-list-20261118.jpg](1_GUI/evidences/TC-GUI-020-special-list-20261118.jpg) | DEF-005 |
| TC-GUI-021 | Page titles | Each browser tab title identifies the page | Six different titles, each naming its page and including the application name | Six distinct titles, e.g. `Tasks — PyTodo Pro` | Pass | [results-C01-20261118-1933.json](1_GUI/evidences/results-C01-20261118-1933.json) | — |
| TC-GUI-022 | Visual consistency | Buttons, links, headings and cards are consistent across pages | One primary button style, one secondary style, consistent text actions, headings and cards | Primary buttons, text links, heading sizes and card corners differ between pages | Fail | [TC-GUI-022-consistency-login-20261118.jpg](1_GUI/evidences/TC-GUI-022-consistency-login-20261118.jpg) | USA-OBS-003 |

**Results summary** (executed 2026-11-18 on C01):

| Total | Pass | Fail | Blocked | Not Run | Pass rate |
| --- | --- | --- | --- | --- | --- |
| 22 | 14 | 8 | 0 | 0 | 63.6% |

The eight failures map to three re-checked Week 1 defects (DEF-001 to DEF-003), two new defects (DEF-004, DEF-005) and three usability observations (USA-OBS-001 to 003) with no stated requirement behind them. Every failure appeared in both runs (`results-C01-20261118-1928.json` and the recorded `results-C01-20261118-1933.json`). In the first run the TC-GUI-010 colour comparison was keyed on the expected class rather than the displayed one; the check was corrected before the recorded run, and the verdict is unchanged.

## Task 2

### Compatibility/configuration matrix

**Method.** Run the eight smoke scenarios in [2_Compatibility/test_cases.md](2_Compatibility/test_cases.md) on each configuration with [test_compatibility.py](2_Compatibility/test_compatibility.py) (`--w3-config <ID>`), saving captures to that configuration's evidence folder. C01-C03 were executed on 2026-11-18; the run files are listed in [2_Compatibility/test_cases.md](2_Compatibility/test_cases.md). Compare each result with C01 and record only differences in layout or behaviour. Chrome DevTools device mode is an emulation; label it so and do not present it as a real-device result.

#### 2.1 Configurations

Each configuration is a combination of OS, browser, viewport and settings. The settings columns record the configuration variations the run used, so they are part of the matrix rather than separate cases. 200% text zoom is covered separately by TC-A11Y-013.

| Config | Evidence folder (under `2_Compatibility/`) | OS | Browser (version) | Viewport / device | Zoom / display scaling | Locale / date format | Type | Available? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01 (baseline) | `evidences/mac-chrome/desktop/` | macOS 26.5.2 | Chrome 157.0.8103.80 (Playwright `chrome` channel, headless) | 1440x900 desktop | 100% / device pixel ratio 1 | en-GB; timezone Asia/Kuala_Lumpur | Real | Executed 2026-11-18 - 8/8 Pass |
| C02 | `evidences/mac-chrome/tablet/` | macOS 26.5.2 | Chrome 157.0.8103.80 (Playwright `chrome` channel, headless, mobile emulation) | 768x1024 tablet, device pixel ratio 2, touch | 100% | en-GB; timezone Asia/Kuala_Lumpur | Emulated | Executed 2026-11-18 - 7/8 Pass (TC-CMP-007 Fail, DEF-006) |
| C03 | `evidences/mac-chrome/mobile/` | macOS 26.5.2 | Chrome 157.0.8103.80 (Playwright `chrome` channel, headless, mobile emulation) | 390x844 phone, device pixel ratio 3, touch | 100% | en-GB; timezone Asia/Kuala_Lumpur | Emulated | Executed 2026-11-18 - 7/8 Pass (TC-CMP-007 Fail, DEF-006) |
| C04 | `evidences/mac-firefox/desktop/` | macOS 26.5.2 | Firefox 160.0.1 installed | 1440x900 desktop | 100% / [scaling] | [locale] | Real | Planned - execution method to be decided: Playwright drives its own Firefox build, not the installed 160.0.1 (see [setup.md](setup.md#firefox-configurations)); see [2.4.1](#241-macos-firefox-run-c04) |
| C05 | `evidences/win-chrome/desktop/` | Windows 11 [build] on Acer Nitro 5 (2021) | Chrome [version] | [native resolution] desktop | 100% / [scaling]% | [locale] | Real | Planned - install Chrome on the Windows laptop if not present; see [2.4.2](#242-windows-11-run-c05-chrome-c06-firefox) |
| C06 | `evidences/win-firefox/desktop/` | Windows 11 [build] on Acer Nitro 5 (2021) | Firefox [version] | [native resolution] desktop | 100% / [scaling]% | [locale] | Real | Yes - installed on the Windows laptop; see [2.4.2](#242-windows-11-run-c05-chrome-c06-firefox) |
| C07 | `evidences/<os>-<browser>/mobile/` | iOS or Android | Chrome mobile [version] | Physical phone | Default | [locale] | Real | Optional - blocked by default: `app.py` uses `app.run(debug=True)`, which listens only on 127.0.0.1, and the project does not modify the application |

**Selection rationale.** Exhaustive compatibility testing is not feasible, so the desktop configurations form a 2x2 design: two operating systems (macOS, Windows 11) by two browsers (Chrome on the Blink engine, Firefox on the Gecko engine). Comparing the same browser across both operating systems isolates OS effects; comparing both browsers on the same OS isolates browser effects. Chrome device mode on macOS adds tablet and mobile widths.

**Excluded configurations.** The team excluded these on 2026-10-27 to keep the scope manageable:

| Excluded | Reason | Residual risk |
| --- | --- | --- |
| Microsoft Edge on Windows 11 | Edge uses the same Blink engine as Chrome, so it adds the least new coverage for the effort | Edge-specific features and settings are untested |
| Safari on macOS | Not needed for the 2x2 design above | The WebKit engine, which also underlies every browser on iOS, is untested |

Record both exclusions as limitations in [2.5](#25-interpretation-complete-after-execution) and in the Week 8 residual-risk assessment.

#### 2.2 Compatibility smoke scenarios

Result per cell: `Pass`, `Fail (DEF-xxx)`, `Diff (USA-OBS-xxx)` for a cosmetic difference, `Blocked` or `Not Run`. The matrix has two sections that share the C01 baseline: cross-browser/OS at desktop size, and cross-device in Chrome on macOS.

**Cross-browser and cross-OS (desktop)**

| ID | Scenario | Expected on every configuration | C01 baseline | C04 mac-firefox | C05 win-chrome | C06 win-firefox |
| --- | --- | --- | --- | --- | --- | --- |
| TC-CMP-001 | Register, log in, log out | Pages render; forms submit; redirects match C01 | Pass | | | |
| TC-CMP-002 | Create task with date picker | Native date picker opens; selected date saved as `YYYY-MM-DD` whatever the display format | Pass | | | |
| TC-CMP-003 | Filter by category/status and search | Auto-submit on select change works; results match C01 | Pass | | | |
| TC-CMP-004 | Complete and reopen | Button and strikethrough update | Pass | | | |
| TC-CMP-005 | Edit task | Pre-filled values, including the date, shown and saved | Pass | | | |
| TC-CMP-006 | Delete with confirmation | Native confirm dialog shown; Cancel/OK behave as on C01 | Pass | | | |
| TC-CMP-007 | Navigation bar and task table layout | Nav items readable on one line each (H10); all six columns readable; no clipped text or controls | Pass | | | |
| TC-CMP-008 | Dashboard layout | Cards reflow without overlap | Pass | | | |

**Cross-device (Chrome on macOS; baseline is C01 above)**

| ID | Scenario | C02 tablet | C03 mobile | C07 phone (optional) |
| --- | --- | --- | --- | --- |
| TC-CMP-001 | Register, log in, log out | Pass | Pass | |
| TC-CMP-002 | Create task with date picker | Pass | Pass | |
| TC-CMP-003 | Filter by category/status and search | Pass | Pass | |
| TC-CMP-004 | Complete and reopen | Pass | Pass | |
| TC-CMP-005 | Edit task | Pass | Pass | |
| TC-CMP-006 | Delete with confirmation | Pass | Pass | |
| TC-CMP-007 | Navigation bar and task table layout | Fail (DEF-006) | Fail (DEF-006) | |
| TC-CMP-008 | Dashboard layout | Pass | Pass | |

#### 2.3 Execution order

1. C01 baseline: fresh TC-CMP run on the MacBook.
2. C02 and C03: fresh TC-CMP runs with Chrome mobile emulation (done 2026-11-18). The Week 1 captures ([0.9](#week-1-captures-reused-as-supporting-evidence)) remain supporting evidence only.
3. C04 Firefox on the MacBook ([2.4.1](#241-macos-firefox-run-c04)).
4. C05 and C06 on Windows 11 ([2.4.2](#242-windows-11-run-c05-chrome-c06-firefox)).
5. C07 only if a way to reach the app is found without modifying it. Otherwise mark the column `Blocked` and give the reason.

#### 2.4 Platform run plans

##### 2.4.1 macOS Firefox run (C04)

| Step | Action | Notes |
| --- | --- | --- |
| 1. Install | Done 2026-11-18: Firefox 160.0.1 installed on the MacBook. Re-check the version in `about:support` on the run day | Do not update Firefox partway through the run |
| 2. Run the app | Start `python app.py` at the same commit as C01 and log in as account A with Fixture Set A | Same database and day as C01, so TC-CMP-008 values can be compared directly |
| 3. Execute | Run TC-CMP-001 to TC-CMP-008 in a 1440x900 window. Optional: repeat TC-CMP-007 and TC-CMP-008 at 390 px in Firefox Responsive Design Mode (Option-Command-M) to compare with C03 for H10 | Watch the date picker, the `confirm()` dialog and the validation popup; Firefox draws these differently from Chrome |
| 4. Evidence | Save to `2_Compatibility/evidences/mac-firefox/desktop/` (and `mac-firefox/mobile/` for the optional step) as `TC-CMP-00x-<desc>-YYYYMMDD.jpg`. Use Firefox's "Take Screenshot", or Shift-Command-4 for native dialogs and pickers | |
| 5. Record | Fill the C04 column in [2.2](#22-compatibility-smoke-scenarios). Log only differences from C01 | Estimated time: about 45 minutes |

##### 2.4.2 Windows 11 run (C05 Chrome, C06 Firefox)

| Step | Action | Notes |
| --- | --- | --- |
| 1. Owner and machine | Darius Lee Shin, on the Acer Nitro 5 (2021): AMD Ryzen 5, GTX 1650, 32 GB DDR4. Record the Windows build (`winver`), exact model and CPU (`msinfo32`), native resolution and display scaling (Settings -> System -> Display) | Laptops often default to 125-150% scaling, which changes the layout. If the laptop has a high-refresh or external display, run on the built-in screen and record that |
| 2. Browsers | Firefox is already installed; install Chrome if it is not. Before the run, check for updates in both browsers so they are on a current release. Then record the versions actually used: Chrome from `chrome://version`, Firefox from `about:support` | Do not update a browser partway through the run; if it updates, re-record the version |
| 3. Run the app locally | Clone the repository and check out the **same commit** as the Mac runs. Then run `python -m venv venv`, `venv\Scripts\activate`, `pip install -r requirements.txt` and `python app.py` | `app.py` listens only on 127.0.0.1, so the app must run on the Windows machine itself. Serving it from the Mac would mean modifying the application, which is out of scope |
| 4. Seed data | The Windows database starts empty. Recreate Fixture Set A from [fixtures.md](fixtures.md) with accounts named like `w3<initial>_win_<ddmm>` | Use the same timezone as the Mac runs, because urgency depends on today's date |
| 5. Locale | Record the Windows region and short-date format in the 2.1 table | The date picker displays dates in the locale's format; the saved value must still be `YYYY-MM-DD` |
| 6. Execute | Run TC-CMP-001 to TC-CMP-008 on Chrome, then on Firefox. Optional: repeat TC-CMP-007 and TC-CMP-008 at 390 px in Firefox Responsive Design Mode (Ctrl+Shift+M) | Watch the date picker, the `confirm()` dialog and the validation popup; each browser draws these differently |
| 7. Accessibility pass | On the same machine, run NVDA for TC-A11Y-005, TC-A11Y-007 and TC-A11Y-015, and run axe DevTools in Chrome | Gives Task 4 a second screen reader alongside VoiceOver |
| 8. Evidence | Save to `2_Compatibility/evidences/win-chrome/desktop/` and `2_Compatibility/evidences/win-firefox/desktop/` as `TC-CMP-00x-<desc>-YYYYMMDD.jpg`. Use Win+Shift+S or Firefox's "Take Screenshot" | Capture the whole browser window when a browser-drawn dialog or picker is part of the result |
| 9. Record | Fill the C05 and C06 columns in [2.2](#22-compatibility-smoke-scenarios). Log only differences from C01 as `DEF-` or `USA-OBS-` items | Estimated time: 8 scenarios x 2 browsers, about 1.5 hours |

#### 2.5 Interpretation (complete after execution)

- Which differences are browser-specific, which are OS-specific, and which are viewport-specific (see H1)?
- Do any differences block a task, or are they cosmetic only?
- Limitations: emulation vs real device, the browser versions tested, and untested configurations: Microsoft Edge on Windows 11 and Safari/WebKit on macOS and iOS (both excluded by team decision, see [2.1](#21-configurations)), older browsers and Firefox on Android.

## Task 3

### Usability observations

**Method.** Two-reviewer heuristic evaluation, with no end-user participants and no automation. Eu Kwan Ik and Ameera Alysha binti Azlan each review all six pages independently against the five qualities named in the guideline, mapped to Nielsen's heuristics, and then merge their findings and agree a severity for each one. The procedure, guiding questions and evidence names are in [3_Usability/test_cases.md](3_Usability/test_cases.md).

**Verdict rule (fixed before the review).** Severity uses Nielsen's scale: 0 not a problem, 1 cosmetic, 2 minor, 3 major, 4 catastrophic. A case **fails** if any merged observation for its quality is rated 3 or 4; otherwise it passes, even when observations rated 1 or 2 are logged.

#### 3.1 Review cases

| ID | Guideline quality | Nielsen heuristics | Observations logged | Highest severity | Status |
| --- | --- | --- | --- | --- | --- |
| TC-USA-001 | Ease of navigation | 3 User control and freedom; 6 Recognition rather than recall | | | Not Run |
| TC-USA-002 | Feedback | 1 Visibility of system status | | | Not Run |
| TC-USA-003 | Consistency | 4 Consistency and standards | | | Not Run |
| TC-USA-004 | Error prevention | 5 Error prevention; 9 Help users recover from errors | | | Not Run |
| TC-USA-005 | Understandability | 2 Match with the real world; 8 Aesthetic and minimalist design | | | Not Run |

#### 3.2 Merge record (complete after the review)

| Item | Value |
| --- | --- |
| Review dates (reviewer 1 / reviewer 2) | |
| Observations found by reviewer 1 only / reviewer 2 only / both | |
| Severity disagreements and how they were resolved | |
| Reviewer notes | `3_Usability/evidences/TC-USA-0xx-<reviewer-initials>-<YYYYMMDD>.md` |

#### 3.3 Observation log

| ID | Case | Page | Heuristic | Observation | Severity 0-4 (agreed; R1/R2 if different) | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| USA-OBS-001 | TC-USA-002 | All task actions | 1 Visibility of system status | No confirmation message or highlight after creating, editing, completing or deleting a task (TC-GUI-017) | Pending reviewer rating | [TC-GUI-017-feedback-create-20261118.jpg](1_GUI/evidences/TC-GUI-017-feedback-create-20261118.jpg) | Show a short confirmation after each action |
| USA-OBS-002 | TC-USA-003 | `/dashboard` | 4 Consistency and standards | `Completed (last 7 days)` card is green while completed tasks use a grey `Done` badge (TC-GUI-018) | Pending reviewer rating | [TC-GUI-018-dashboard-20261118.jpg](1_GUI/evidences/TC-GUI-018-dashboard-20261118.jpg) | Use one colour for "completed" across the app |
| USA-OBS-003 | TC-USA-003 | All pages | 4 Consistency and standards | Primary buttons differ (`+ New Task` font size, `Filter` colour and size); auth-page links use the browser-default blue; auth headings 22.4 px vs 32 px; card corners 12 px vs 10 px (TC-GUI-022) | Pending reviewer rating | [TC-GUI-022-consistency-list-20261118.jpg](1_GUI/evidences/TC-GUI-022-consistency-list-20261118.jpg) | Define one style per control type and apply it on every page |
| USA-OBS-004 | TC-USA-004 | `/login`, `/register` | 9 Help users recover from errors | After a login or registration error the username field is emptied, so the user must retype it (TC-GUI-002, TC-GUI-004) | Pending reviewer rating | [TC-GUI-004-register-errors-s1-20261118.jpg](1_GUI/evidences/TC-GUI-004-register-errors-s1-20261118.jpg) | Keep the entered username after an error |

USA-OBS-001 to 004 were found by the GUI suite and are inputs to the heuristic review. The two reviewers confirm each one and agree its severity during TC-USA-002 to 004.

Raise a `DEF-` record only when an observation breaks a stated requirement or interface promise. Keep all other observations as `USA-OBS-` items with recommendations.

## Task 4

### Basic accessibility findings

**Method.** Run three passes on each of the six pages, logged in with Fixture Set A. The full cases are in [4_Accessibility/test_cases.md](4_Accessibility/test_cases.md).

1. **Automated scan.** Lighthouse Accessibility audit and axe DevTools (or WAVE). Save the reports to `4_Accessibility/evidences/reports/`. Automated tools catch only part of the issues, so treat a clean scan as incomplete evidence.
2. **Manual keyboard pass.** Complete the TC-A11Y-008 task sequence with Tab, Shift+Tab, Enter, Space, Escape and the arrow keys only.
3. **Screen reader and zoom pass.** Use VoiceOver (macOS) or NVDA (Windows) on the login, task list and task form pages. Then check 200% zoom and a 320 CSS px width.

#### 4.1 WCAG 2.2 checklist (Level A/AA subset)

| ID | WCAG SC (level) | Check | Pages | Expected | Actual | Status | Evidence | Defect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-A11Y-001 | 1.1.1 Non-text content (A) | Non-text controls and icons have a text alternative | All | Every icon-only control has an accessible name | | Not Run | | |
| TC-A11Y-002 | 1.3.1 Info and relationships (A) | Headings, table headers and form structure are in the markup | All | One `h1` per page; `th` cells for the table | | Not Run | | |
| TC-A11Y-003 | 1.4.1 Use of colour (A) | Urgency is not shown by colour alone | Task list, dashboard | Badge text conveys urgency | | Not Run | | |
| TC-A11Y-004 | 1.4.3 Contrast minimum (AA) | Text contrast at least 4.5:1 (3:1 for large text) | All | Pass; see H5 for predicted failures | | Not Run | | |
| TC-A11Y-005 | 1.3.1 / 4.1.2 Labels associated | Clicking a label focuses its field; screen reader reads the label | Login, register, task form | Each field announced with its label (H2) | | Not Run | | |
| TC-A11Y-006 | 3.3.2 Labels or instructions (A) | Every input has a visible label or instruction | Task list filters | Filters and search have labels (H4) | | Not Run | | |
| TC-A11Y-007 | 4.1.2 Name, role, value (A) | Complete/reopen button announces its purpose and state | Task list | e.g. "Mark <title> as done, button" (H3) | | Not Run | | |
| TC-A11Y-008 | 2.1.1 Keyboard (A) | All functions work by keyboard, including the delete dialog and date picker | All | The TC-A11Y-008 task sequence completed by keyboard only, with no keyboard trap | | Not Run | | |
| TC-A11Y-009 | 2.4.1 Bypass blocks (A) | A way to skip the navigation bar | All logged-in pages | Skip link or landmark navigation available (H8) | | Not Run | | |
| TC-A11Y-010 | 2.4.2 Page titled (A) | Page titles are unique and descriptive | All | Same as TC-GUI-021 | | Not Run | | |
| TC-A11Y-011 | 2.4.3 Focus order / 2.4.7 Focus visible (AA) | Tab order follows the visual order and focus is always visible | All | Logical order; visible focus indicator on every control | | Not Run | | |
| TC-A11Y-012 | 1.4.10 Reflow (AA) | Content usable at 320 CSS px without two-dimensional scrolling | All | No horizontal scrolling except for the data table (H1) | | Not Run | | |
| TC-A11Y-013 | 1.4.4 Resize text (AA) | 200% browser zoom | All | No clipped or overlapping content | | Not Run | | |
| TC-A11Y-014 | 3.1.1 Language of page (A) | `lang` attribute present | All | `<html lang="en">` | | Not Run | | |
| TC-A11Y-015 | 3.3.1 Error identification (A) / 4.1.3 Status messages (AA) | Errors are described in text and announced | Login, register | Screen reader announces the error without a focus change (H7) | | Not Run | | |
| TC-A11Y-016 | 2.5.8 Target size minimum (AA, WCAG 2.2) | Pointer targets at least 24x24 CSS px | Task list (`Edit`, `Delete`, toggle) | All targets meet the minimum or its spacing exception | | Not Run | | |
| TC-A11Y-017 | 2.4.6 Headings and labels (AA) | Headings and labels describe their purpose | All | Clear, unambiguous text | | Not Run | | |
| TC-A11Y-018 | Automated scan summary | Lighthouse score and axe issue count per page | All | Recorded; every serious or critical axe issue triaged | | Not Run | | |

#### 4.2 Automated scan results (complete after execution)

| Page | Lighthouse a11y score | axe critical | axe serious | axe moderate/minor | Report |
| --- | --- | --- | --- | --- | --- |
| `/login` | | | | | |
| `/register` | | | | | |
| `/` | | | | | |
| `/tasks/new` | | | | | |
| `/tasks/<id>/edit` | | | | | |
| `/dashboard` | | | | | |

State the limitation: this is a basic review of a subset of WCAG 2.2 A/AA, not a conformance claim.

## Task 5

### Defects and improvement recommendations

#### 5.1 Process

1. Reproduce each Fail at least twice, on C01 and on the configuration where it was seen.
2. Check the existing log (DEF-001 to DEF-003 in [Week 1](../01_Black_Box/README.md#task-5)). If the issue is already logged, add the new evidence to that defect instead of creating a duplicate.
3. Create the record with the next free ID (`DEF-004` onwards) using the template below. Assign severity and priority with the shared scale.
4. Write a recommendation for each defect and for each usability observation rated 3 or 4.
5. Copy new defects to the consolidated defect log that Week 7 will maintain.

#### 5.2 Defect record template

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-0xx |
| Title | Specific summary |
| Affected Feature | Page / element and REQ-xxx or WCAG SC |
| Environment | Configuration ID (C0x), OS, browser and version, viewport |
| Preconditions | State required to reproduce |
| Steps to Reproduce | Numbered steps |
| Expected Result | With its basis (interface text, README, REQ or WCAG SC) |
| Actual Result | Observed behaviour |
| Severity | Critical / Major / Moderate / Minor |
| Priority | High / Medium / Low |
| Evidence | Relative link to screenshot or report in the technique folder's `evidences/` |
| Status | Open / Confirmed / Retest / Closed |

Severity guidance for this phase: **Major** when a task cannot be completed (for example, a keyboard or screen-reader user cannot complete or delete a task). **Moderate** when a task can be completed but is materially harder or misleading. **Minor** for cosmetic or consistency issues.

#### 5.3 Defect summary (as of 2026-11-18; Tasks 3-4 and C04-C06 still to run)

| Defect ID | Title | Source case(s) | Configuration | Severity | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DEF-001 | Registration rejects the stated minimum-length password (Week 1) | TC-GUI-004 | C01 | Moderate | Medium | Open - reproduced in Week 3 |
| DEF-002 | A task due today displays Overdue (Week 1) | TC-GUI-010 | C01 | Moderate | High | Open - reproduced in Week 3 |
| DEF-003 | A whitespace-only title creates a task (Week 1) | TC-GUI-016 | C01 | Moderate | Medium | Open - reproduced in Week 3 |
| DEF-004 | Navigation bar wraps and pushes `Log out` off-screen at a 390 px viewport | TC-GUI-005 | C01 at 390x844 | Moderate | Medium | Open |
| DEF-005 | HTML in a task title is rendered as markup in the task list | TC-GUI-020 | C01 | Moderate | High | Open |
| DEF-006 | Pages render at a 980 px desktop layout on tablet and phone screens, so text is too small to read | TC-CMP-007 | C02, C03 | Moderate | Medium | Open |

#### DEF-004 - Navigation bar breaks at a narrow viewport

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-004 |
| Title | Navigation bar wraps and pushes `Log out` off-screen at a 390 px viewport |
| Affected Feature | Shared navigation bar; REQ-002 |
| Environment | C01 machine: Chrome 157.0.8103.80 on macOS 26.5.2, Playwright headless, viewport set to 390x844 (desktop device type, no mobile emulation) |
| Preconditions | Logged in as account A |
| Steps to Reproduce | 1. Log in.<br>2. Resize the viewport to 390x844.<br>3. Open `/`, `/tasks/new` or `/dashboard`. |
| Expected Result | Each navigation item fits on one line, no items overlap, and every item can be clicked. Basis: interface; TC-GUI-005 |
| Actual Result | `PyTodo Pro` wraps to two lines. `Log out` wraps to two lines and extends past the right edge of the viewport, so it is not visible without scrolling sideways. Same result on all three pages and in both runs |
| Severity | Moderate - logging out needs horizontal scrolling on narrow screens |
| Priority | Medium |
| Evidence | [TC-GUI-005-nav-390-20261118.jpg](1_GUI/evidences/TC-GUI-005-nav-390-20261118.jpg); [Week 1 mobile capture](2_Compatibility/evidences/mac-chrome/mobile/TC-BB-034.jpg) |
| Status | Open |

Behaviour with true mobile emulation or a phone (H1) is still to be checked in C03/C07. No source-level fix is claimed.

#### DEF-005 - Task title HTML is rendered as markup

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-005 |
| Title | HTML in a task title is rendered as markup in the task list |
| Affected Feature | Task list `/`; REQ-003 |
| Environment | C01: Chrome 157.0.8103.80 on macOS 26.5.2, 1440x900, Playwright headless |
| Preconditions | Logged in; a task titled `GUI-Special & <b>bold</b> "double" 'single' Résumé 报告` exists (fixture F9) |
| Steps to Reproduce | 1. Create a task with the title above.<br>2. Open `/`. |
| Expected Result | The title is displayed exactly as entered, including the literal text `<b>bold</b>`. Basis: REQ-003; TC-GUI-020 |
| Actual Result | The list shows `bold` in bold type and hides the tags. The edit form shows the exact title. Same result in both runs |
| Severity | Moderate - displayed task data differs from what was saved |
| Priority | High - the same behaviour may allow script injection; to be assessed with safe test data in the Week 5 STRIDE table (H9) |
| Evidence | [TC-GUI-020-special-list-20261118.jpg](1_GUI/evidences/TC-GUI-020-special-list-20261118.jpg); [TC-GUI-020-special-edit-20261118.jpg](1_GUI/evidences/TC-GUI-020-special-edit-20261118.jpg) |
| Status | Open |

No script payloads were used in Week 3.

#### DEF-006 - Desktop layout scaled down on tablets and phones

| Field | Required Information |
| --- | --- |
| Defect ID | DEF-006 |
| Title | Pages render at a 980 px desktop layout on tablet and phone screens, so text is too small to read |
| Affected Feature | Every page (shared layout); observed on the task list, REQ-003 |
| Environment | C02: Chrome 157.0.8103.80 mobile emulation, 768x1024, device pixel ratio 2. C03: same browser, 390x844, device pixel ratio 3. macOS 26.5.2, Playwright headless |
| Preconditions | Logged in as account A with Fixture Set A |
| Steps to Reproduce | 1. Open the app with Chrome mobile emulation for a 390x844 phone or a 768x1024 tablet.<br>2. Log in and open `/`.<br>3. Compare `window.innerWidth` with the device width and measure the smallest navigation/table text. |
| Expected Result | All six table columns and the navigation are readable without zooming; text renders at 12 px or more on the device screen. Basis: TC-CMP-007 |
| Actual Result | The page is laid out at 980 CSS px and scaled to 0.784 (tablet) or 0.398 (phone) of its size. The smallest navigation/table text renders at 9.8 px on the tablet and 5.0 px on the phone, so users must zoom in to read it. Same result in two runs per configuration. Consistent with H1 (no viewport meta tag) |
| Severity | Moderate - all content is present but needs zooming on tablets and phones |
| Priority | Medium |
| Evidence | [Tablet](2_Compatibility/evidences/mac-chrome/tablet/TC-CMP-007-layout-20261118.jpg); [phone](2_Compatibility/evidences/mac-chrome/mobile/TC-CMP-007-layout-20261118.jpg) |
| Status | Open |

On emulated devices the desktop-width layout hides DEF-004, which appears in narrow desktop windows. Fixing DEF-006 with a viewport tag alone would expose DEF-004 on phones, so both are covered by R2.

#### 5.4 Improvement recommendations (as of 2026-11-18)

| # | Recommendation | Addresses | Benefit | Effort (L/M/H) | Priority |
| --- | --- | --- | --- | --- | --- |
| R1 | Escape task titles when rendering the task list instead of inserting them as HTML | DEF-005, H9 | Titles display as entered; removes a likely injection path | L | High |
| R2 | Add a viewport meta tag and a narrow-screen navigation layout (wrapping or a menu) | DEF-004, DEF-006, H1, H10 | Navigation, including Log out, usable on phones | M | Medium |
| R3 | Show a confirmation message after create, edit, complete and delete | USA-OBS-001, H6 | Users can see that an action worked | L | Medium |
| R4 | Keep the entered username after a login or registration error | USA-OBS-004 | Fewer retyping errors | L | Low |
| R5 | Apply one style per control type (primary button, text link, heading, card) on every page | USA-OBS-002, USA-OBS-003 | Consistent look; easier to learn | M | Low |

DEF-001 to DEF-003 keep the recommendations recorded in Week 1.

Order the recommendations by priority. Recommendations describe changes for the development team. This project does not modify the application.

#### 5.5 Phase summary and hand-offs (complete after execution)

| Item | Value |
| --- | --- |
| Cases planned / executed / passed / failed / blocked | 53 planned (22 GUI, 8 compatibility, 5 usability, 18 accessibility); compatibility cases are counted once each, with per-configuration results in [2.2](#22-compatibility-smoke-scenarios) |
| New defects (by severity) | So far: 3 Moderate (DEF-004, DEF-005, DEF-006); DEF-001 to DEF-003 reproduced |
| Usability observations (by severity) | So far: 4 found by the GUI suite (USA-OBS-001 to 004), severities pending the heuristic review |
| Hand-off to Week 4 | UI vs API differences seen during GUI testing (e.g. validation shown in the UI but not enforced by the server) |
| Hand-off to Week 5 | H9 rendering of titles, and any other security-relevant behaviour seen in the UI |
| Hand-off to Week 6 | Stable GUI cases suitable for Selenium regression (candidates: TC-CMP-001 to TC-CMP-006) |
| Limitations | Configurations not tested, emulation vs real devices, usability evaluated by two-reviewer heuristic review only (no end-user participants), subset of WCAG covered |
