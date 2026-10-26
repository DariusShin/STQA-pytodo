# Week 3 - GUI, Compatibility, Usability and Accessibility Testing

| Item | Recorded value |
| --- | --- |
| Course | TEB3433 / TFB3433 - Software Testing and Quality Assurance |
| Semester / Lab Group | September 2026 / Wednesday Lab - Group 2 |
| Phase status | Planning complete - execution not started |

## Deliverable Checklist

- [ ] [Task 1](#task-1) - GUI testing checklist/results.
- [ ] [Task 2](#task-2) - Compatibility/configuration matrix.
- [ ] [Task 3](#task-3) - Usability observations.
- [ ] [Task 4](#task-4) - Basic accessibility findings.
- [ ] [Task 5](#task-5) - Defects and improvement recommendations.

Tick a task only after its results, evidence and peer review are complete. Every planned case below is `Not Run` until it is executed; do not record an actual result before execution.

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
| Keyboard, screen-reader and contrast checks against a WCAG 2.2 Level A/AA subset | Automated Selenium regression of GUI flows (Week 6) |
| Re-checking DEF-001 to DEF-003 where they surface in the GUI | Full WCAG conformance audit or certification |

Functional correctness was established in Week 1. This phase asks a different question: does each page present that behaviour clearly, consistently and accessibly across configurations?

### 0.3 Test basis

Expected results must be written before execution and must cite one of these sources:

1. The interface itself: visible labels, hints and button text (for example, `min 8 characters` on Register).
2. The project `README.md` page and feature list.
3. Week 1 requirements `REQ-001` to `REQ-008` and assumptions in [01_Black_Box/README.md](../01_Black_Box/README.md).
4. WCAG 2.2 success criteria for accessibility cases.
5. Usability heuristics introduced in class (Nielsen's 10 heuristics) for usability observations.

### 0.4 Test case ID conventions

| Prefix | Use | Planned range |
| --- | --- | --- |
| `TC-GUI-` | GUI checklist cases | 001-022 |
| `TC-CMP-` | Compatibility smoke scenarios, run once per configuration | 001-008 |
| `TC-USA-` | Usability walkthrough tasks | 001-006 |
| `USA-OBS-` | Usability observations and heuristic findings | from 001 |
| `TC-A11Y-` | Accessibility checks | 001-018 |
| `DEF-` | New defects, continuing the shared defect log | from `DEF-004` |

Detailed cases using the full test-case template (ID, feature, technique, objective, preconditions, test data, steps, expected, actual, status, evidence, defect ID) go in `test_cases.md` in this folder, following the Week 1 format. This README keeps the summary registers, matrices and findings.

### 0.5 Environment to record

Record these values at execution time. Do not copy versions from earlier weeks without checking them again.

| Component | Value |
| --- | --- |
| Application commit | `git rev-parse --short HEAD` at execution |
| Target | `python app.py` development server at `http://127.0.0.1:5000` |
| Operating systems | macOS 26.5.2 (build 25F84, checked 2026-10-27 with `sw_vers`); Windows 11 (record the build with `winver`) |
| Windows hardware | Acer Nitro 5 (2021) owned by Darius Lee Shin: AMD Ryzen 5 CPU, NVIDIA GTX 1650 GPU, 32 GB DDR4 RAM. Record the exact model number, CPU model, screen size and native resolution from `msinfo32` and Settings -> System -> Display |
| Browsers | Name, version and build for each browser in the [configuration matrix](#21-configurations) |
| Viewports | Device-mode preset name and CSS pixel size |
| Accessibility tools | Lighthouse (bundled with Chrome); axe DevTools or WAVE extension version; VoiceOver (macOS) / NVDA version |
| Test accounts | Synthetic accounts named `w3<initial>_<purpose>_<ddmm>`; password `Test12345` |
| Execution date/time and timezone | Per run |

### 0.6 Test data set

Prepare one account with a fixed task set so that every page is checked in a populated state:

| Data item | Purpose |
| --- | --- |
| One task per urgency class: Overdue, Due Today, Due Soon, Upcoming, No due date, Done | Badge colour and text checks (TC-GUI-010, TC-A11Y-004) |
| One task in each category (Work, Personal, Study, Urgent) and one with no category | Filter and table rendering |
| A 200-character title and a 60-character unbroken title | Layout and wrapping (TC-GUI-019) |
| A title containing `&`, `<`, `>`, quotes and non-Latin text (e.g. `Résumé 报告`) | Literal display (TC-GUI-020) |
| A second, empty account | Empty-state checks (TC-GUI-009) |

### 0.7 Work allocation and schedule

Coordinators own the preparation and review of each task. Every member executes cases, so no member works on only one task.

| Task | Coordinator | Execution support |
| --- | --- | --- |
| Task 1 - GUI checklist | Mohamd Shukri Bin Abd Ajed (Test Design) | All members |
| Task 2 - Compatibility matrix | Darius Lee Shin (Automation/Tool) | Darius Lee Shin runs C05, C06 and C08 on the Windows 11 laptop (Acer Nitro 5); another member reviews the captures |
| Task 3 - Usability | Eu Kwan Ik (QA/Test Lead) | Two or three participants who did not design the cases |
| Task 4 - Accessibility | Darius Lee Shin (Automation/Tool) | Ameera Alysha binti Azlan (manual keyboard/screen-reader checks) |
| Task 5 - Defects and recommendations | Ameera Alysha binti Azlan (Defect & Metrics) | Eu Kwan Ik (review and final integration) |

| Step | Activity | Output |
| --- | --- | --- |
| 1 | Confirm the browsers and devices each member can use; fix the configuration matrix | [2.1](#21-configurations) filled in |
| 2 | Seed the test data set; record the environment | [0.5](#05-environment-to-record) and [0.6](#06-test-data-set) |
| 3 | Write detailed cases in `test_cases.md` with expected results before execution | Peer-reviewed cases |
| 4 | Execute GUI cases on the baseline configuration (C01) | [Task 1](#task-1) results |
| 5 | Run the compatibility smoke set on every other configuration | [Task 2](#task-2) matrix |
| 6 | Run automated accessibility scans, then the manual keyboard, screen-reader and zoom checks | [Task 4](#task-4) findings |
| 7 | Run the usability walkthrough and heuristic review | [Task 3](#task-3) observations |
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
| GUI, accessibility and usability screenshots | `evidences/` | `<TC-ID>-<short-desc>-<YYYYMMDD>.png`, e.g. `TC-GUI-013-delete-dialog-20261028.png` |
| Compatibility captures | `<browser>/<viewport>/` (the existing `chrome/desktop`, `chrome/tablet` and `chrome/mobile` folders, plus folders such as `safari/desktop` and `edge/desktop`) | `<TC-ID>-<YYYYMMDD>.png` |
| Lighthouse and axe reports | `evidences/a11y-reports/` | `<tool>-<page>-<YYYYMMDD>.html` or `.json` |
| Usability session notes | `evidences/usability/` | `TC-USA-<id>-P<participant>.md` (no personal data) |

The existing captures in `chrome/desktop`, `chrome/tablet` and `chrome/mobile` reuse Week 1 `TC-BB-` IDs. Map them to `TC-CMP-` scenarios in the [compatibility matrix](#22-compatibility-smoke-scenarios) and list in each cell which `TC-BB-` captures support it. Do not rename them.

#### What the existing `chrome/` captures are, and are not

| Folder | Content (checked 2026-10-27) | Counts as |
| --- | --- | --- |
| `chrome/desktop/` (72 files, 1440x900) | Byte-identical copy of `01_Black_Box/evidences/` | Baseline C01. Not a new Week 3 run |
| `chrome/tablet/` (72 files, 768x1024) | Week 1 cases re-run with tablet accounts (`w1t_…`) | Compatibility evidence for C02 |
| `chrome/mobile/` (102 files, 390x844) | Week 1 cases re-run with mobile accounts (`w1m_…`); includes extra `-full-document` captures | Compatibility evidence for C03 |

These captures were judged against **functional** expected results from Week 1, so they are compatibility and responsiveness evidence, not GUI testing. They may be cited as supporting evidence for a `TC-GUI-` case, but each GUI case still needs its own expected result and verdict.

Before citing the tablet and mobile captures, the person who took them must record which DevTools mode they used: a **Responsive** window with device type Desktop, or a **device preset** such as iPhone 14 with mobile emulation. The 390 px captures show the page laid out at 390 px with normal-size text. Because the page has no viewport tag (H1), true mobile emulation or a real phone would normally lay it out at about 980 px and scale it down. The captures therefore probably came from a resized window and may not show H1. Re-check H1 with a device preset, Safari's Responsive Design Mode or a real phone (C07).

### 0.10 Pre-execution inspection notes

The templates (`templates/*.html`) and `static/style.css` were read while planning to target the cases below. These are **hypotheses to confirm in the browser, not defects**. Log one only after it has been reproduced and its user-facing effect observed.

| # | Observation from inspecting the source | Planned check |
| --- | --- | --- |
| H1 | `base.html` has no `<meta name="viewport">` tag, and the CSS has no `@media` rules | TC-CMP mobile/tablet runs; TC-A11Y-012 reflow |
| H2 | Form `<label>` elements have no `for` attribute, and inputs have no `id`, so labels may not be programmatically associated | TC-A11Y-005, TC-A11Y-006 |
| H3 | The complete/reopen button's only content is `○` or `✓` | TC-A11Y-007 |
| H4 | The filter selects and search box have no visible labels; the search box has a placeholder only | TC-A11Y-006, TC-GUI-008 |
| H5 | Calculated contrast: completed-task title and empty-state text `#999999` on white = 2.85:1 (WCAG 1.4.3 requires 4.5:1). Hint `#8d6e76` on white = 4.54:1 (borderline). Other text pairs checked were above 4.5:1 | TC-A11Y-004 with a contrast tool on the rendered page |
| H6 | No success message after create, edit, delete or complete; only login and register render an error message | TC-GUI-017, usability feedback heuristic |
| H7 | Error messages have no `role="alert"` or live region | TC-A11Y-015 |
| H8 | No skip link before the navigation bar | TC-A11Y-009 |
| H9 | `index.html` renders the task title with the `safe` filter | TC-GUI-020 checks only literal display; pass any script behaviour to the Week 5 STRIDE table |
| H10 | Seen in existing evidence [`chrome/mobile/TC-BB-034.jpg`](chrome/mobile/TC-BB-034.jpg): at 390 px the navigation bar is cramped. The brand wraps to `PyTodo / Pro`, `Log out` breaks across lines, and the links sit against the brand with no gap. This follows from `.topnav`/`.nav-links` being a non-wrapping flex row with fixed `2rem` side padding and no `@media` rule | TC-GUI-005 on C03, TC-CMP-007 on C02, C03 and C07, TC-A11Y-012 reflow. If confirmed, log it as a defect with a fresh dated capture |

H10 comes from a capture taken for a functional case, so it remains a hypothesis until a `TC-GUI-` or `TC-CMP-` case reproduces it. The same capture has the mouse pointer covering the `Filter` button. Move the pointer out of the way when capturing new Week 3 evidence.

## Task 1

### GUI testing checklist/results

**Method.** Run the checklist on the baseline configuration (C01: Chrome on macOS at 1440x900) using the [seeded data set](#06-test-data-set). Each row is one test case with a full entry in `test_cases.md`. Technique: GUI checklist / Functional.

| ID | Page / element | Check (objective) | Expected result (before execution) | Actual | Status | Evidence | Defect |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-GUI-001 | Login - layout | Heading, Username and Password fields, Log in button and Register link are present and aligned | All elements visible in one card; password input is masked | | Not Run | | |
| TC-GUI-002 | Login - error message | Invalid credentials show an error | Visible error in the red error box; user stays on `/login` | | Not Run | | |
| TC-GUI-003 | Register - hints | Field rules are visible before input | Hints `(3-20 chars, letters/numbers/underscore)` and `(min 8 characters)` are readable next to their labels | | Not Run | | |
| TC-GUI-004 | Register - error messages | Each invalid input produces a specific message | Message names the violated rule; entered values handled consistently (retained or cleared) | | Not Run | | DEF-001 re-check |
| TC-GUI-005 | Navigation bar | Navigation differs by login state; items stay readable at every viewport | Logged in: Tasks, Dashboard, username, Log out. Logged out: brand only. No item text broken across lines (H10) | | Not Run | | |
| TC-GUI-006 | Brand link | Brand link goes to the right place | Logged in -> `/`; logged out -> `/login` | | Not Run | | |
| TC-GUI-007 | Task list - header | Page heading and New Task button | `My Tasks` heading; `+ New Task` opens `/tasks/new` | | Not Run | | |
| TC-GUI-008 | Task list - filters | Filter controls behave predictably | Category/status selects apply on change; search applies on Filter button or Enter; selected values persist after reload | | Not Run | | |
| TC-GUI-009 | Task list - table/empty state | Columns and empty-state message | Six columns with headers; empty account shows `No tasks match your filters.` | | Not Run | | |
| TC-GUI-010 | Urgency badges | Each urgency class has a distinct, labelled badge | Six badge texts shown; Overdue/Due Today/Due Soon/Upcoming are visually distinguishable | | Not Run | | DEF-002 re-check |
| TC-GUI-011 | Complete/reopen button | Button state matches the task state | `○` for open and `✓` for done; done row shown with strikethrough | | Not Run | | |
| TC-GUI-012 | Edit link | Edit opens a pre-filled form | Title, description, category and due date pre-filled with saved values | | Not Run | | |
| TC-GUI-013 | Delete confirmation | Delete asks for confirmation | Dialog `Delete this task?`; Cancel keeps the task, OK removes it | | Not Run | | |
| TC-GUI-014 | New Task form | Fields and controls | Title, Description, Category (None + 4) and Due Date date picker; Create Task and Cancel buttons | | Not Run | | |
| TC-GUI-015 | Edit Task form | Edit mode labelling | Heading `Edit Task` and button `Save Changes`; Cancel returns to `/` without saving | | Not Run | | |
| TC-GUI-016 | Required title | Empty title is blocked | Browser validation message on Title; no navigation | | Not Run | | DEF-003 re-check |
| TC-GUI-017 | Action feedback | Create, edit, delete and complete give visible confirmation | User can tell the action succeeded (message or obvious list change) | | Not Run | | |
| TC-GUI-018 | Dashboard cards | Five counters with labels | Total, Open, Overdue, Due Soon, Completed (last 7 days); colours match the badge colours | | Not Run | | |
| TC-GUI-019 | Long content | Long and unbroken titles do not break layout | Table stays within the container; no horizontal page scroll at 1440 px | | Not Run | | |
| TC-GUI-020 | Special characters | Titles display exactly as entered | `&`, `<`, `>`, quotes and non-Latin text displayed literally | | Not Run | | |
| TC-GUI-021 | Page titles | Each browser tab title identifies the page | `Log in`, `Register`, `Tasks`, `New Task`, `Edit Task`, `Dashboard`, each followed by `— PyTodo Pro` | | Not Run | | |
| TC-GUI-022 | Visual consistency | Primary/secondary buttons, fonts, spacing and colours are consistent across pages | One primary button style (`#1B3A5C`), one secondary style, consistent card styling | | Not Run | | |

**Results summary** (complete after execution):

| Total | Pass | Fail | Blocked | Not Run |
| --- | --- | --- | --- | --- |
| 22 | | | | 22 |

## Task 2

### Compatibility/configuration matrix

**Method.** Choose configurations the group actually has access to. Run the eight smoke scenarios on each configuration. Compare the result with C01 and record only differences in layout or behaviour. Chrome DevTools device mode is an emulation; label it so and do not present it as a real-device result.

#### 2.1 Configurations

Confirm availability in step 1 and delete rows that cannot be run. Record a reason for each deleted row.

| Config | OS | Browser (version) | Viewport / device | Type | Available? |
| --- | --- | --- | --- | --- | --- |
| C01 (baseline) | macOS 26.5.2 | Chrome [version] | 1440x900 desktop | Real | Yes - existing `chrome/desktop` captures |
| C02 | macOS 26.5.2 | Chrome [version] | Tablet preset, e.g. iPad Air 820x1180 | Emulated | Yes - existing `chrome/tablet` captures |
| C03 | macOS 26.5.2 | Chrome [version] | Mobile preset, e.g. iPhone 14 390x844 | Emulated | Yes - existing `chrome/mobile` captures |
| C04 | macOS 26.5.2 | Safari 26.5.2 | 1440x900 desktop; optional iPhone preset in Responsive Design Mode for H1/H10 | Real (preset is emulated) | Yes - installed on the MacBook (checked 2026-10-27) |
| C05 | Windows 11 [build] on Acer Nitro 5 (2021) | Firefox [version] | [native resolution] desktop at [scaling]% | Real | Yes - installed on the Windows laptop; see [2.4.2](#242-windows-11-run-c05-firefox-c06-edge-c08-chrome) |
| C06 | Windows 11 [build] on Acer Nitro 5 (2021) | Microsoft Edge [version] | [native resolution] desktop at [scaling]% | Real | Yes - installed on the Windows laptop; see [2.4.2](#242-windows-11-run-c05-firefox-c06-edge-c08-chrome) |
| C07 | iOS or Android | Safari or Chrome mobile [version] | Physical phone | Real | Optional - blocked by default: `app.py` uses `app.run(debug=True)`, which listens only on 127.0.0.1, and the project does not modify the application |
| C08 | Windows 11 [build] on Acer Nitro 5 (2021) | Chrome [version] | [native resolution] desktop at [scaling]% | Real | Optional - install Chrome if not present; separates OS differences from browser differences |

Firefox and Edge are not installed on the MacBook (checked 2026-10-27), so they are tested only on Windows 11.

#### 2.2 Compatibility smoke scenarios

Result per cell: `Pass`, `Fail (DEF-xxx)`, `Diff (USA-OBS-xxx)` for a cosmetic difference, `Blocked` or `Not Run`.

| ID | Scenario | Expected on every configuration | C01 | C02 | C03 | C04 | C05 | C06 | C07 | C08 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-CMP-001 | Register, log in, log out | Pages render; forms submit; redirects match C01 | | | | | | | | |
| TC-CMP-002 | Create task with date picker | Native date picker opens; selected date saved as `YYYY-MM-DD` whatever the display format | | | | | | | | |
| TC-CMP-003 | Filter by category/status and search | Auto-submit on select change works; results match C01 | | | | | | | | |
| TC-CMP-004 | Complete and reopen | Button and strikethrough update | | | | | | | | |
| TC-CMP-005 | Edit task | Pre-filled values, including the date, shown and saved | | | | | | | | |
| TC-CMP-006 | Delete with confirmation | Native confirm dialog shown; Cancel/OK behave as on C01 | | | | | | | | |
| TC-CMP-007 | Navigation bar and task table layout | Nav items readable on one line each (H10); all six columns readable; no clipped text or controls | | | | | | | | |
| TC-CMP-008 | Dashboard layout | Cards reflow without overlap | | | | | | | | |

#### 2.3 Execution order

1. C01 baseline, using the existing captures where they cover the scenario.
2. C02 and C03, using the existing captures after their DevTools mode is recorded ([0.9](#what-the-existing-chrome-captures-are-and-are-not)). Re-run only the scenarios they do not cover.
3. C04 Safari on the MacBook ([2.4.1](#241-macbook-safari-run-c04)).
4. C05, C06 and optionally C08 on Windows 11 ([2.4.2](#242-windows-11-run-c05-firefox-c06-edge-c08-chrome)).
5. C07 only if a way to reach the app is found without modifying it. Otherwise mark the column `Blocked` and give the reason.

#### 2.4 Platform run plans

##### 2.4.1 MacBook Safari run (C04)

| Step | Action |
| --- | --- |
| 1 | In Safari -> Settings -> Advanced, turn on "Show features for web developers". This adds the Develop menu, Web Inspector and Responsive Design Mode |
| 2 | Start the app with `python app.py` at the same commit as C01 and log in with the seeded account from [0.6](#06-test-data-set) |
| 3 | Run TC-CMP-001 to TC-CMP-008 in a 1440x900 window. Save captures to `safari/desktop/` |
| 4 | Optional: Develop -> Enter Responsive Design Mode (Option-Command-R), choose an iPhone preset and repeat TC-CMP-007 and TC-CMP-008 to check H1 and H10. Save to `safari/mobile/` and label the result as emulated |
| 5 | Watch for differences from Chrome in the date picker, the `confirm()` dialog, the required-field popup, form-control styling and fonts. The CSS font stack starts with `-apple-system` |

##### 2.4.2 Windows 11 run (C05 Firefox, C06 Edge, C08 Chrome)

| Step | Action | Notes |
| --- | --- | --- |
| 1. Owner and machine | Darius Lee Shin, on the Acer Nitro 5 (2021): AMD Ryzen 5, GTX 1650, 32 GB DDR4. Record the Windows build (`winver`), exact model and CPU (`msinfo32`), native resolution and display scaling (Settings -> System -> Display) | Laptops often default to 125-150% scaling, which changes the layout. If the laptop has a high-refresh or external display, run on the built-in screen and record that |
| 2. Browsers | Firefox and Edge are already installed. Before the run, check for updates in each browser so both are on a current release. Then record the versions actually used: Edge from `edge://version`, Firefox from `about:support`. Optionally record Chrome's version from `chrome://version` for C08 | Do not update a browser partway through the run; if it updates, re-record the version |
| 3. Run the app locally | Clone the repository and check out the **same commit** as the Mac runs. Then run `python -m venv venv`, `venv\Scripts\activate`, `pip install -r requirements.txt` and `python app.py` | `app.py` listens only on 127.0.0.1, so the app must run on the Windows machine itself. Serving it from the Mac would mean modifying the application, which is out of scope |
| 4. Seed data | The Windows database starts empty. Recreate the data set from [0.6](#06-test-data-set) with accounts named like `w3<initial>_win_<ddmm>` | Use the same timezone as the Mac runs, because urgency depends on today's date |
| 5. Locale | Record the Windows region and short-date format | The date picker displays dates in the locale's format; the saved value must still be `YYYY-MM-DD` |
| 6. Execute | Run TC-CMP-001 to TC-CMP-008 on Edge, then Firefox, then optionally Chrome. Optional: repeat TC-CMP-007 and TC-CMP-008 at 390 px in Firefox Responsive Design Mode (Ctrl+Shift+M) | Watch the date picker, the `confirm()` dialog and the validation popup; each browser draws these differently |
| 7. Accessibility pass | On the same machine, run NVDA for TC-A11Y-005, TC-A11Y-007 and TC-A11Y-015, and run axe DevTools in Edge | Gives Task 4 a second screen reader alongside VoiceOver |
| 8. Evidence | Save to `edge/desktop/`, `firefox/desktop/` and `chrome-win/desktop/` as `TC-CMP-00x-YYYYMMDD.png`. Use Win+Shift+S, Firefox's "Take Screenshot" or Edge's Web Capture (Ctrl+Shift+S) | Capture the whole browser window when a browser-drawn dialog or picker is part of the result |
| 9. Record | Fill the C05, C06 and C08 columns in [2.2](#22-compatibility-smoke-scenarios). Log only differences from C01 as `DEF-` or `USA-OBS-` items | Estimated time: 8 scenarios x 2-3 browsers, about 1.5-2.5 hours |

#### 2.5 Interpretation (complete after execution)

- Which differences are browser-specific, and which are viewport-specific (see H1)?
- Do any differences block a task, or are they cosmetic only?
- Limitations: emulation vs real device, the browser versions tested, and untested configurations such as older browsers and Firefox on Android.

## Task 3

### Usability observations

**Method.** Use two techniques so that findings do not depend only on the testers' opinions:

1. **Task-based walkthrough.** Two or three participants who did not design the cases each attempt the tasks below on C01 without help. The facilitator records completion, time, errors or wrong paths, and a 1-7 ease rating (Single Ease Question), and asks participants to think aloud.
2. **Heuristic review.** Two team members independently review every page against the five qualities named in the guideline (mapped to Nielsen heuristics) and then merge their findings.

#### 3.1 Walkthrough tasks

| ID | Task given to participant | Success criterion | P1 (done / time / errors / SEQ) | P2 | P3 |
| --- | --- | --- | --- | --- | --- |
| TC-USA-001 | Create an account and log in | Reaches `My Tasks` | | | |
| TC-USA-002 | Add a Study task due tomorrow | Task listed with category Study and the correct date | | | |
| TC-USA-003 | Show only open Work tasks whose title contains "report" | Correct filtered list shown | | | |
| TC-USA-004 | Mark a task as done, then undo it | Task returns to the open state | | | |
| TC-USA-005 | Delete one specific task | Correct task removed; others intact | | | |
| TC-USA-006 | Find how many tasks are overdue | States the correct number from the dashboard | | | |

Use synthetic data only. Record participants as P1-P3 and do not record names or student IDs.

#### 3.2 Heuristic checklist

| Guideline quality | Heuristic | Questions to answer per page |
| --- | --- | --- |
| Ease of navigation | Recognition rather than recall; user control and freedom | Can every page be reached from the navigation bar? Is there always a way back or a Cancel option? |
| Feedback | Visibility of system status | Does every action show that it succeeded or failed (H6)? |
| Consistency | Consistency and standards | Are terms, button styles and positions the same across pages (for example `Log in` and `Log out`, `Create Task` and `Save Changes`)? |
| Error prevention | Error prevention; help users recover from errors | Are rules shown before input? Are destructive actions confirmed? Do error messages explain how to fix the problem? |
| Understandability | Match with the real world; aesthetic and minimalist design | Are urgency names, the `○`/`✓` control and the dashboard counters self-explanatory? |

#### 3.3 Observation log

Severity scale: 0 not a problem, 1 cosmetic, 2 minor, 3 major, 4 catastrophic (Nielsen).

| ID | Page | Heuristic | Observation | Source (walkthrough / review) | Severity 0-4 | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| USA-OBS-001 | | | | | | | |

Raise a `DEF-` record only when an observation breaks a stated requirement or interface promise. Keep all other observations as `USA-OBS-` items with recommendations.

## Task 4

### Basic accessibility findings

**Method.** Run three passes on each of the six pages, logged in with the seeded data set:

1. **Automated scan.** Lighthouse Accessibility audit and axe DevTools (or WAVE). Save the reports. Automated tools catch only part of the issues, so treat a clean scan as incomplete evidence.
2. **Manual keyboard pass.** Complete TC-USA-001 to TC-USA-005 with Tab, Shift+Tab, Enter, Space and the arrow keys only.
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
| TC-A11Y-008 | 2.1.1 Keyboard (A) | All functions work by keyboard, including the delete dialog and date picker | All | TC-USA-001 to TC-USA-005 completed by keyboard only | | Not Run | | |
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
| Evidence | Relative link to screenshot or report |
| Status | Open / Confirmed / Retest / Closed |

Severity guidance for this phase: **Major** when a task cannot be completed (for example, a keyboard or screen-reader user cannot complete or delete a task). **Moderate** when a task can be completed but is materially harder or misleading. **Minor** for cosmetic or consistency issues.

#### 5.3 Defect summary (complete after execution)

| Defect ID | Title | Source case(s) | Configuration | Severity | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

#### 5.4 Improvement recommendations (complete after execution)

| # | Recommendation | Addresses | Benefit | Effort (L/M/H) | Priority |
| --- | --- | --- | --- | --- | --- |
| R1 | | | | | |

Order the recommendations by priority. Recommendations describe changes for the development team. This project does not modify the application.

#### 5.5 Phase summary and hand-offs (complete after execution)

| Item | Value |
| --- | --- |
| Cases planned / executed / passed / failed / blocked | |
| New defects (by severity) | |
| Usability observations (by severity) | |
| Hand-off to Week 4 | UI vs API differences seen during GUI testing (e.g. validation shown in the UI but not enforced by the server) |
| Hand-off to Week 5 | H9 rendering of titles, and any other security-relevant behaviour seen in the UI |
| Hand-off to Week 6 | Stable GUI cases suitable for Selenium regression (candidates: TC-CMP-001 to TC-CMP-006) |
| Limitations | Configurations not tested, emulation vs real devices, number of usability participants, subset of WCAG covered |
