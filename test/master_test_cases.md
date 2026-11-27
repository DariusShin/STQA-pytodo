# Master Test-Case Repository

All test cases of Weeks 1-6 in one place, consolidated in Week 7 from the weekly `test_cases.md` files. Each ID links to its full record (preconditions, data, steps, expected and actual results, evidence). Week 6 cases are automated versions of earlier manual cases; the 4 usability observations of Week 3 are in [03_Special_Testing/3_Usability/observations.md](03_Special_Testing/3_Usability/observations.md).

## Summary

| Week | Area | Cases | Pass | Fail | Blocked | Not Run |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Week 1 | Black-box | 44 | 40 | 4 | 0 | 0 |
| Week 2 | White-box | 28 | 28 | 0 | 0 | 0 |
| Week 3 | GUI | 22 | 14 | 8 | 0 | 0 |
| Week 3 | Compatibility | 8 | 7 | 1 | 0 | 0 |
| Week 3 | Accessibility | 18 | 7 | 11 | 0 | 0 |
| Week 4 | Web and API | 61 | 43 | 18 | 0 | 0 |
| Week 5 | Security and performance | 32 | 12 | 19 | 1 | 0 |
| Week 6 | Automation and regression | 89 | 64 | 25 | 0 | 0 |
| **Total** | | **302** | **215** | **86** | **1** | **0** |

## Week 1 - Black-box

Source: [01_Black_Box/test_cases.md](01_Black_Box/test_cases.md)

| ID | Title | Requirement(s) | Technique | Status | Defect(s) |
| --- | --- | --- | --- | --- | --- |
| [TC-BB-001](01_Black_Box/test_cases.md#tc-bb-001---username-length-2) | Username length 2 | REQ-001 | BVA / Functional | Pass | — |
| [TC-BB-002](01_Black_Box/test_cases.md#tc-bb-002---username-length-3) | Username length 3 | REQ-001 | BVA / Functional | Pass | — |
| [TC-BB-003](01_Black_Box/test_cases.md#tc-bb-003---username-length-4) | Username length 4 | REQ-001 | BVA / Functional | Pass | — |
| [TC-BB-004](01_Black_Box/test_cases.md#tc-bb-004---username-length-19) | Username length 19 | REQ-001 | BVA / Functional | Pass | — |
| [TC-BB-005](01_Black_Box/test_cases.md#tc-bb-005---username-length-20) | Username length 20 | REQ-001 | BVA / Functional | Pass | — |
| [TC-BB-006](01_Black_Box/test_cases.md#tc-bb-006---username-length-21) | Username length 21 | REQ-001 | BVA / Functional | Pass | — |
| [TC-BB-007](01_Black_Box/test_cases.md#tc-bb-007---password-length-7) | Password length 7 | REQ-001 | BVA / Functional | Pass | — |
| [TC-BB-008](01_Black_Box/test_cases.md#tc-bb-008---password-length-8) | Password length 8 | REQ-001 | BVA / Functional | Fail | DEF-001 |
| [TC-BB-009](01_Black_Box/test_cases.md#tc-bb-009---password-length-9) | Password length 9 | REQ-001 | BVA / Functional | Pass | — |
| [TC-BB-010](01_Black_Box/test_cases.md#tc-bb-010---valid-registration) | Valid registration | REQ-001 | EP / Functional | Pass | — |
| [TC-BB-011](01_Black_Box/test_cases.md#tc-bb-011---disallowed-username-character) | Disallowed username character | REQ-001 | EP / Functional | Pass | — |
| [TC-BB-012](01_Black_Box/test_cases.md#tc-bb-012---empty-registration-username) | Empty registration username | REQ-001 | EP / Functional / Browser validation | Pass | — |
| [TC-BB-013](01_Black_Box/test_cases.md#tc-bb-013---empty-registration-password) | Empty registration password | REQ-001 | EP / Functional / Browser validation | Pass | — |
| [TC-BB-014](01_Black_Box/test_cases.md#tc-bb-014---login-credential-decision-rule-1) | Login credential decision rule 1 | REQ-002 | Decision table / Functional | Pass | — |
| [TC-BB-015](01_Black_Box/test_cases.md#tc-bb-015---login-credential-decision-rule-2) | Login credential decision rule 2 | REQ-002 | Decision table / Functional | Pass | — |
| [TC-BB-016](01_Black_Box/test_cases.md#tc-bb-016---login-credential-decision-rule-3) | Login credential decision rule 3 | REQ-002 | Decision table / Functional | Pass | — |
| [TC-BB-017](01_Black_Box/test_cases.md#tc-bb-017---login-credential-decision-rule-4) | Login credential decision rule 4 | REQ-002 | Decision table / Functional | Pass | — |
| [TC-BB-018](01_Black_Box/test_cases.md#tc-bb-018---protected-page-while-logged-out) | Protected page while logged out | REQ-002 | State transition / Functional | Pass | — |
| [TC-BB-019](01_Black_Box/test_cases.md#tc-bb-019---logout-revokes-protected-page-access) | Logout revokes protected-page access | REQ-002 | State transition / Functional | Pass | — |
| [TC-BB-020](01_Black_Box/test_cases.md#tc-bb-020---create-and-persist-a-full-field-task) | Create and persist a full-field task | REQ-003 | EP / Functional | Pass | — |
| [TC-BB-021](01_Black_Box/test_cases.md#tc-bb-021---create-a-title-only-task) | Create a title-only task | REQ-003 | EP / Functional | Pass | — |
| [TC-BB-022](01_Black_Box/test_cases.md#tc-bb-022---empty-title-browser-validation) | Empty title browser validation | REQ-003 | EP / Browser validation | Pass | — |
| [TC-BB-023](01_Black_Box/test_cases.md#tc-bb-023---reject-a-whitespace-only-title) | Reject a whitespace-only title | REQ-003 | EP / Functional / Input validation | Fail | DEF-003 |
| [TC-BB-024](01_Black_Box/test_cases.md#tc-bb-024---edit-and-persist-all-task-fields) | Edit and persist all task fields | REQ-003 | Functional | Pass | — |
| [TC-BB-025](01_Black_Box/test_cases.md#tc-bb-025---cancel-edit-preserves-saved-data) | Cancel edit preserves saved data | REQ-003 | State transition / Functional | Pass | — |
| [TC-BB-026](01_Black_Box/test_cases.md#tc-bb-026---cancel-deletion-retains-task) | Cancel deletion retains task | REQ-003 | State transition / Functional | Pass | — |
| [TC-BB-027](01_Black_Box/test_cases.md#tc-bb-027---confirm-deletion-and-verify-persistence) | Confirm deletion and verify persistence | REQ-003 | State transition / Functional | Pass | — |
| [TC-BB-028](01_Black_Box/test_cases.md#tc-bb-028---complete-an-open-task) | Complete an Open task | REQ-004 | State transition / Functional | Pass | — |
| [TC-BB-029](01_Black_Box/test_cases.md#tc-bb-029---reopen-a-done-task) | Reopen a Done task | REQ-004 | State transition / Functional | Pass | — |
| [TC-BB-030](01_Black_Box/test_cases.md#tc-bb-030---filter-by-category) | Filter by category | REQ-005 | EP / Functional | Pass | — |
| [TC-BB-031](01_Black_Box/test_cases.md#tc-bb-031---filter-open-tasks) | Filter Open tasks | REQ-005 | EP / Functional | Pass | — |
| [TC-BB-032](01_Black_Box/test_cases.md#tc-bb-032---filter-done-tasks) | Filter Done tasks | REQ-005 | EP / Functional | Pass | — |
| [TC-BB-033](01_Black_Box/test_cases.md#tc-bb-033---matching-title-search) | Matching title search | REQ-005 | EP / Functional | Pass | — |
| [TC-BB-034](01_Black_Box/test_cases.md#tc-bb-034---nonmatching-title-search) | Nonmatching title search | REQ-005 | EP / Functional | Pass | — |
| [TC-BB-035](01_Black_Box/test_cases.md#tc-bb-035---combined-filters-all-conditions-required) | Combined filters: all conditions required | REQ-005 | Decision table / Functional | Pass | — |
| [TC-BB-036](01_Black_Box/test_cases.md#tc-bb-036---urgency-bb-no-date) | Urgency: BB-NO-DATE | REQ-006 | EP / Functional | Pass | — |
| [TC-BB-037](01_Black_Box/test_cases.md#tc-bb-037---urgency-bb-yesterday) | Urgency: BB-YESTERDAY | REQ-006 | BVA / Functional | Pass | — |
| [TC-BB-038](01_Black_Box/test_cases.md#tc-bb-038---urgency-bb-today) | Urgency: BB-TODAY | REQ-006 | BVA / Functional | Fail | DEF-002 |
| [TC-BB-039](01_Black_Box/test_cases.md#tc-bb-039---urgency-bb-tomorrow) | Urgency: BB-TOMORROW | REQ-006 | BVA / Functional | Pass | — |
| [TC-BB-040](01_Black_Box/test_cases.md#tc-bb-040---urgency-bb-plus-two) | Urgency: BB-PLUS-TWO | REQ-006 | BVA / Functional | Pass | — |
| [TC-BB-041](01_Black_Box/test_cases.md#tc-bb-041---urgency-bb-plus-three) | Urgency: BB-PLUS-THREE | REQ-006 | BVA / Functional | Pass | — |
| [TC-BB-042](01_Black_Box/test_cases.md#tc-bb-042---completion-overrides-overdue-urgency) | Completion overrides overdue urgency | REQ-004, REQ-006 | State transition / Functional | Pass | — |
| [TC-BB-043](01_Black_Box/test_cases.md#tc-bb-043---reconcile-dashboard-with-controlled-data) | Reconcile dashboard with controlled data | REQ-007 | Functional / Independent calculation | Fail | DEF-002 |
| [TC-BB-044](01_Black_Box/test_cases.md#tc-bb-044---visible-task-list-isolation-between-accounts) | Visible task-list isolation between accounts | REQ-008 | EP / Functional | Pass | — |

## Week 2 - White-box

Source: [02_White_Box_Coverage/test_cases.md](02_White_Box_Coverage/test_cases.md)

| ID | Title | Requirement(s) | Technique | Status | Defect(s) |
| --- | --- | --- | --- | --- | --- |
| [TC-WB-001](02_White_Box_Coverage/test_cases.md) | New connection is created | REQ-003 | Basis path DB01 | Pass | — |
| [TC-WB-002](02_White_Box_Coverage/test_cases.md) | Existing connection is reused | REQ-003 | Basis path DB02 | Pass | — |
| [TC-WB-003](02_White_Box_Coverage/test_cases.md) | Existing connection is closed | REQ-003 | Basis path CL01 | Pass | — |
| [TC-WB-004](02_White_Box_Coverage/test_cases.md) | Missing connection is safe | REQ-003 | Basis path CL02 | Pass | — |
| [TC-WB-005](02_White_Box_Coverage/test_cases.md) | Schema created with no categories | REQ-003 | Basis path IN01 (zero iterations) | Pass | — |
| [TC-WB-006](02_White_Box_Coverage/test_cases.md) | Defaults seeded and committed | REQ-003 | Basis path IN02 (four iterations) | Pass | — |
| [TC-WB-007](02_White_Box_Coverage/test_cases.md) | Open task gets computed urgency | REQ-003 | Basis path RT01 | Pass | — |
| [TC-WB-008](02_White_Box_Coverage/test_cases.md) | Done task gets `Done` | REQ-003 | Basis path RT02 | Pass | — |
| [TC-WB-009](02_White_Box_Coverage/test_cases.md) | Falsy id skips the database | REQ-003 | Basis path CN01 | Pass | — |
| [TC-WB-010](02_White_Box_Coverage/test_cases.md) | Existing id resolves | REQ-003 | Basis path CN02 | Pass | — |
| [TC-WB-011](02_White_Box_Coverage/test_cases.md) | Unknown id returns nothing | REQ-003 | Basis path CN03 | Pass | — |
| [TC-WB-012](02_White_Box_Coverage/test_cases.md) | Existing name resolves | REQ-003 | Basis path CI01 | Pass | — |
| [TC-WB-013](02_White_Box_Coverage/test_cases.md) | Unknown or injected name returns nothing | REQ-003 | Basis path CI02 | Pass | — |
| [TC-WB-014](02_White_Box_Coverage/test_cases.md) | Decorator keeps metadata | REQ-002 | Basis path WF01 | Pass | — |
| [TC-WB-015](02_White_Box_Coverage/test_cases.md) | Anonymous request redirected | REQ-002 | Basis path WA01 | Pass | — |
| [TC-WB-016](02_White_Box_Coverage/test_cases.md) | Signed-in request forwarded | REQ-002 | Basis path WA02 | Pass | — |
| [TC-WB-017](02_White_Box_Coverage/test_cases.md) | Decorator keeps metadata | REQ-002 | Basis path AF01 | Pass | — |
| [TC-WB-018](02_White_Box_Coverage/test_cases.md) | Anonymous API call rejected | REQ-002 | Basis path AA01 | Pass | — |
| [TC-WB-019](02_White_Box_Coverage/test_cases.md) | Signed-in API call forwarded | REQ-002 | Basis path AA02 | Pass | — |
| [TC-WB-020](02_White_Box_Coverage/test_cases.md) | Real teardown closes the connection | REQ-003 | Integration | Pass | — |
| [TC-WB-021](02_White_Box_Coverage/test_cases.md) | New context gets a new connection | REQ-003 | Integration | Pass | — |
| [TC-WB-022](02_White_Box_Coverage/test_cases.md) | Re-running init keeps data | REQ-003 | Integration | Pass | — |
| [TC-WB-023](02_White_Box_Coverage/test_cases.md) | Real endpoints reject anonymous calls | REQ-002 | Integration | Pass | — |
| [TC-WB-024](02_White_Box_Coverage/test_cases.md) | Real endpoints accept a session | REQ-002 | Integration | Pass | — |
| [TC-WB-025](02_White_Box_Coverage/test_cases.md) | 6 urgency outcomes | REQ-006 | Statement coverage | Pass | — |
| [TC-WB-026](02_White_Box_Coverage/test_cases.md) | Password rule | REQ-001 | Statement coverage | Pass | — |
| [TC-WB-027](02_White_Box_Coverage/test_cases.md) | Username rule | REQ-001 | Statement coverage | Pass | — |
| [TC-WB-028](02_White_Box_Coverage/test_cases.md) | Recent-completion window | REQ-007 | Statement coverage | Pass | — |

## Week 3 - GUI

Source: [03_Special_Testing/1_GUI/test_cases.md](03_Special_Testing/1_GUI/test_cases.md)

| ID | Title | Requirement(s) | Technique | Status | Defect(s) |
| --- | --- | --- | --- | --- | --- |
| [TC-GUI-001](03_Special_Testing/1_GUI/test_cases.md#tc-gui-001---login-page-layout) | Login page layout | REQ-002, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-002](03_Special_Testing/1_GUI/test_cases.md#tc-gui-002---login-error-message) | Login error message | REQ-002, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-003](03_Special_Testing/1_GUI/test_cases.md#tc-gui-003---registration-hints) | Registration hints | REQ-001, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-004](03_Special_Testing/1_GUI/test_cases.md#tc-gui-004---registration-error-messages) | Registration error messages | REQ-001, REQ-010 | GUI checklist | Fail | DEF-001 |
| [TC-GUI-005](03_Special_Testing/1_GUI/test_cases.md#tc-gui-005---navigation-bar) | Navigation bar | REQ-002, REQ-010 | GUI checklist | Fail | DEF-004 |
| [TC-GUI-006](03_Special_Testing/1_GUI/test_cases.md#tc-gui-006---brand-link) | Brand link | REQ-002, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-007](03_Special_Testing/1_GUI/test_cases.md#tc-gui-007---task-list-header) | Task list header | REQ-003, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-008](03_Special_Testing/1_GUI/test_cases.md#tc-gui-008---filter-controls) | Filter controls | REQ-005, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-009](03_Special_Testing/1_GUI/test_cases.md#tc-gui-009---task-table-and-empty-state) | Task table and empty state | REQ-003, REQ-005, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-010](03_Special_Testing/1_GUI/test_cases.md#tc-gui-010---urgency-badges) | Urgency badges | REQ-006, REQ-010 | GUI checklist | Fail | DEF-002 |
| [TC-GUI-011](03_Special_Testing/1_GUI/test_cases.md#tc-gui-011---complete-and-reopen-button) | Complete and reopen button | REQ-004, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-012](03_Special_Testing/1_GUI/test_cases.md#tc-gui-012---edit-link-opens-a-pre-filled-form) | Edit link opens a pre-filled form | REQ-003, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-013](03_Special_Testing/1_GUI/test_cases.md#tc-gui-013---delete-confirmation) | Delete confirmation | REQ-003, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-014](03_Special_Testing/1_GUI/test_cases.md#tc-gui-014---new-task-form) | New Task form | REQ-003, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-015](03_Special_Testing/1_GUI/test_cases.md#tc-gui-015---edit-task-form) | Edit Task form | REQ-003, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-016](03_Special_Testing/1_GUI/test_cases.md#tc-gui-016---required-title) | Required title | REQ-003, REQ-010 | GUI checklist | Fail | DEF-003 |
| [TC-GUI-017](03_Special_Testing/1_GUI/test_cases.md#tc-gui-017---feedback-after-actions) | Feedback after actions | REQ-003, REQ-004, REQ-010 | GUI checklist / Usability heuristic | Fail | — |
| [TC-GUI-018](03_Special_Testing/1_GUI/test_cases.md#tc-gui-018---dashboard-cards) | Dashboard cards | REQ-007, REQ-010 | GUI checklist | Fail | — |
| [TC-GUI-019](03_Special_Testing/1_GUI/test_cases.md#tc-gui-019---long-content) | Long content | REQ-003, REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-020](03_Special_Testing/1_GUI/test_cases.md#tc-gui-020---special-characters) | Special characters | REQ-003, REQ-010 | GUI checklist | Fail | DEF-005 |
| [TC-GUI-021](03_Special_Testing/1_GUI/test_cases.md#tc-gui-021---page-titles) | Page titles | REQ-010 | GUI checklist | Pass | — |
| [TC-GUI-022](03_Special_Testing/1_GUI/test_cases.md#tc-gui-022---visual-consistency) | Visual consistency | REQ-010 | GUI checklist | Fail | — |

## Week 3 - Compatibility

Source: [03_Special_Testing/2_Compatibility/test_cases.md](03_Special_Testing/2_Compatibility/test_cases.md)

| ID | Title | Requirement(s) | Technique | Status | Defect(s) |
| --- | --- | --- | --- | --- | --- |
| [TC-CMP-001](03_Special_Testing/2_Compatibility/test_cases.md#tc-cmp-001---register-log-in-and-log-out) | Register, log in and log out | REQ-001, REQ-002, REQ-010 | Compatibility | Pass | — |
| [TC-CMP-002](03_Special_Testing/2_Compatibility/test_cases.md#tc-cmp-002---create-a-task-with-the-date-picker) | Create a task with the date picker | REQ-003, REQ-006, REQ-010 | Compatibility | Pass | — |
| [TC-CMP-003](03_Special_Testing/2_Compatibility/test_cases.md#tc-cmp-003---filter-and-search) | Filter and search | REQ-005, REQ-010 | Compatibility | Pass | — |
| [TC-CMP-004](03_Special_Testing/2_Compatibility/test_cases.md#tc-cmp-004---complete-and-reopen) | Complete and reopen | REQ-004, REQ-010 | Compatibility | Pass | — |
| [TC-CMP-005](03_Special_Testing/2_Compatibility/test_cases.md#tc-cmp-005---edit-a-task) | Edit a task | REQ-003, REQ-010 | Compatibility | Pass | — |
| [TC-CMP-006](03_Special_Testing/2_Compatibility/test_cases.md#tc-cmp-006---delete-with-confirmation) | Delete with confirmation | REQ-003, REQ-010 | Compatibility | Pass | — |
| [TC-CMP-007](03_Special_Testing/2_Compatibility/test_cases.md#tc-cmp-007---navigation-bar-and-task-table-layout) | Navigation bar and task table layout | REQ-002, REQ-003, REQ-010 | Compatibility | Fail | DEF-006 |
| [TC-CMP-008](03_Special_Testing/2_Compatibility/test_cases.md#tc-cmp-008---dashboard-layout) | Dashboard layout | REQ-007, REQ-010 | Compatibility | Pass | — |

## Week 3 - Accessibility

Source: [03_Special_Testing/4_Accessibility/test_cases.md](03_Special_Testing/4_Accessibility/test_cases.md)

| ID | Title | Requirement(s) | Technique | Status | Defect(s) |
| --- | --- | --- | --- | --- | --- |
| [TC-A11Y-001](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-001---non-text-content) | Non-text content | REQ-012 | Accessibility (WCAG) - inspection | Fail | DEF-008 |
| [TC-A11Y-002](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-002---info-and-relationships) | Info and relationships | REQ-012 | Accessibility (WCAG) - inspection | Fail | DEF-010 |
| [TC-A11Y-003](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-003---use-of-colour) | Use of colour | REQ-012 | Accessibility (WCAG) - simulation | Pass | — |
| [TC-A11Y-004](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-004---text-contrast) | Text contrast | REQ-012 | Accessibility (WCAG) - measurement | Fail | DEF-009 |
| [TC-A11Y-005](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-005---form-labels-associated-with-fields) | Form labels associated with fields | REQ-012 | Accessibility (WCAG) - inspection | Fail | DEF-007 |
| [TC-A11Y-006](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-006---filter-and-search-labels) | Filter and search labels | REQ-012 | Accessibility (WCAG) - inspection | Fail | DEF-007 |
| [TC-A11Y-007](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-007---complete-and-reopen-button-name-and-state) | Complete and reopen button name and state | REQ-012 | Accessibility (WCAG) - inspection | Fail | DEF-008 |
| [TC-A11Y-008](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-008---keyboard-operation) | Keyboard operation | REQ-012 | Accessibility (WCAG) - keyboard | Pass | — |
| [TC-A11Y-009](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-009---bypass-the-navigation-bar) | Bypass the navigation bar | REQ-012 | Accessibility (WCAG) - keyboard and inspection | Fail | DEF-010 |
| [TC-A11Y-010](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-010---page-titles) | Page titles | REQ-012 | Accessibility (WCAG) - inspection | Pass | — |
| [TC-A11Y-011](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-011---focus-order-and-visible-focus) | Focus order and visible focus | REQ-012 | Accessibility (WCAG) - keyboard | Pass | — |
| [TC-A11Y-012](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-012---reflow-at-320-css-pixels) | Reflow at 320 CSS pixels | REQ-012 | Accessibility (WCAG) - viewport | Fail | DEF-004 |
| [TC-A11Y-013](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-013---text-resize-to-200) | Text resize to 200% | REQ-012 | Accessibility (WCAG) - zoom | Pass | — |
| [TC-A11Y-014](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-014---language-of-page) | Language of page | REQ-012 | Accessibility (WCAG) - inspection | Pass | — |
| [TC-A11Y-015](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-015---error-identification-and-announcement) | Error identification and announcement | REQ-012 | Accessibility (WCAG) - inspection | Fail | DEF-011 |
| [TC-A11Y-016](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-016---target-size) | Target size | REQ-012 | Accessibility (WCAG) - measurement | Fail | DEF-012 |
| [TC-A11Y-017](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-017---descriptive-headings-and-labels) | Descriptive headings and labels | REQ-012 | Accessibility (WCAG) - review | Fail | DEF-013 |
| [TC-A11Y-018](03_Special_Testing/4_Accessibility/test_cases.md#tc-a11y-018---automated-scan-summary) | Automated scan summary | REQ-012 | Accessibility (WCAG) - automated scan | Pass | — |

## Week 4 - Web and API

Source: [04_Web_API/test_cases.md](04_Web_API/test_cases.md)

| ID | Title | Requirement(s) | Technique | Status | Defect(s) |
| --- | --- | --- | --- | --- | --- |
| [TC-WEB-001](04_Web_API/test_cases.md#tc-web-001---register-through-the-web-form) | Register through the web form | REQ-001 | Workflow / web | Pass | — |
| [TC-WEB-002](04_Web_API/test_cases.md#tc-web-002---registration-validated-on-the-server) | Registration validated on the server | REQ-001 | Client-server validation / EP | Pass | — |
| [TC-WEB-003](04_Web_API/test_cases.md#tc-web-003---login-through-the-web-form) | Login through the web form | REQ-002 | Decision table / web | Pass | — |
| [TC-WEB-004](04_Web_API/test_cases.md#tc-web-004---protected-pages-redirect-when-logged-out) | Protected pages redirect when logged out | REQ-002 | EP (unauthenticated) / web | Pass | — |
| [TC-WEB-005](04_Web_API/test_cases.md#tc-web-005---web-created-task-matches-the-api) | Web-created task matches the API | REQ-003 | Workflow / UI vs API comparison | Pass | — |
| [TC-WEB-006](04_Web_API/test_cases.md#tc-web-006---api-created-task-matches-the-web-list) | API-created task matches the web list | REQ-003, REQ-006 | Workflow / API vs UI comparison | Pass | — |
| [TC-WEB-007](04_Web_API/test_cases.md#tc-web-007---web-edit-matches-the-api) | Web edit matches the API | REQ-003 | Workflow / UI vs API comparison | Pass | — |
| [TC-WEB-008](04_Web_API/test_cases.md#tc-web-008---web-toggle-matches-the-api) | Web toggle matches the API | REQ-004 | State transition / UI vs API comparison | Pass | — |
| [TC-WEB-009](04_Web_API/test_cases.md#tc-web-009---web-delete-matches-the-api) | Web delete matches the API | REQ-003 | Workflow / UI vs API comparison | Pass | — |
| [TC-WEB-010](04_Web_API/test_cases.md#tc-web-010---blank-title-validated-on-the-server) | Blank title validated on the server | REQ-003 | Client-server validation / EP | Fail | DEF-003 |
| [TC-WEB-011](04_Web_API/test_cases.md#tc-web-011---due-date-validated-on-the-server) | Due date validated on the server | REQ-003, REQ-006 | Client-server validation / EP | Fail | DEF-015 |
| [TC-WEB-012](04_Web_API/test_cases.md#tc-web-012---category-validated-on-the-server) | Category validated on the server | REQ-003 | Client-server validation / EP | Fail | DEF-019 |
| [TC-WEB-013](04_Web_API/test_cases.md#tc-web-013---web-actions-on-another-users-task) | Web actions on another user's task | REQ-008 | EP (foreign id) / UI vs API comparison | Pass | — |
| [TC-WEB-014](04_Web_API/test_cases.md#tc-web-014---web-dashboard-matches-the-api-dashboard) | Web dashboard matches the API dashboard | REQ-007 | UI vs API comparison | Pass | — |
| [TC-WEB-015](04_Web_API/test_cases.md#tc-web-015---web-search-with-an-apostrophe) | Web search with an apostrophe | REQ-005 | EP (special character) / UI vs API comparison | Pass | — |
| [TC-WEB-016](04_Web_API/test_cases.md#tc-web-016---duplicate-username-on-the-web-form) | Duplicate username on the web form | REQ-001 | EP / web negative | Fail | DEF-016 |
| [TC-API-001](04_Web_API/test_cases.md#tc-api-001---register-a-valid-account) | Register a valid account | REQ-001 | EP / API functional | Pass | — |
| [TC-API-002](04_Web_API/test_cases.md#tc-api-002---username-valid-length-boundaries-3-20) | Username valid length boundaries (3, 20) | REQ-001 | BVA / API | Pass | — |
| [TC-API-003](04_Web_API/test_cases.md#tc-api-003---invalid-username-partitions) | Invalid username partitions | REQ-001 | EP + BVA / API negative | Pass | — |
| [TC-API-004](04_Web_API/test_cases.md#tc-api-004---password-length-7-rejected) | Password length 7 rejected | REQ-001 | BVA / API negative | Pass | — |
| [TC-API-005](04_Web_API/test_cases.md#tc-api-005---password-length-8-accepted) | Password length 8 accepted | REQ-001 | BVA / API | Fail | DEF-001 |
| [TC-API-006](04_Web_API/test_cases.md#tc-api-006---missing-password-rejected) | Missing password rejected | REQ-001 | EP / API negative | Pass | — |
| [TC-API-007](04_Web_API/test_cases.md#tc-api-007---username-of-the-wrong-json-type) | Username of the wrong JSON type | REQ-001, REQ-009 | EP (data type) / API negative | Fail | DEF-018 |
| [TC-API-008](04_Web_API/test_cases.md#tc-api-008---duplicate-username-rejected) | Duplicate username rejected | REQ-001 | EP / API negative | Fail | DEF-016 |
| [TC-API-009](04_Web_API/test_cases.md#tc-api-009---login-with-valid-credentials) | Login with valid credentials | REQ-002 | Decision table (valid/valid) / API | Pass | — |
| [TC-API-010](04_Web_API/test_cases.md#tc-api-010---login-with-invalid-credentials) | Login with invalid credentials | REQ-002 | Decision table / API negative | Pass | — |
| [TC-API-011](04_Web_API/test_cases.md#tc-api-011---protected-endpoints-require-a-session) | Protected endpoints require a session | REQ-002, REQ-009 | EP (unauthenticated) / API negative | Pass | — |
| [TC-API-012](04_Web_API/test_cases.md#tc-api-012---categories-endpoint-requires-a-session) | Categories endpoint requires a session | REQ-009 | EP (unauthenticated) / API negative | Fail | DEF-023 |
| [TC-API-013](04_Web_API/test_cases.md#tc-api-013---list-categories) | List categories | REQ-009 | API functional | Pass | — |
| [TC-API-014](04_Web_API/test_cases.md#tc-api-014---create-a-task-with-all-fields) | Create a task with all fields | REQ-003 | EP (valid) / API functional | Pass | — |
| [TC-API-015](04_Web_API/test_cases.md#tc-api-015---create-a-title-only-task) | Create a title-only task | REQ-003 | EP (valid, optional fields omitted) / API | Pass | — |
| [TC-API-016](04_Web_API/test_cases.md#tc-api-016---title-required) | Title required | REQ-003 | EP (invalid) / API negative | Pass | — |
| [TC-API-017](04_Web_API/test_cases.md#tc-api-017---non-json-request-body) | Non-JSON request body | REQ-009 | EP (invalid format) / API negative | Pass | — |
| [TC-API-018](04_Web_API/test_cases.md#tc-api-018---wrong-json-types-on-create) | Wrong JSON types on create | REQ-003, REQ-009 | EP (data type) / API negative | Fail | DEF-018 |
| [TC-API-019](04_Web_API/test_cases.md#tc-api-019---invalid-due-date-on-create) | Invalid due date on create | REQ-003, REQ-006 | EP (invalid) / API negative | Fail | DEF-015 |
| [TC-API-020](04_Web_API/test_cases.md#tc-api-020---invalid-category-on-create) | Invalid category on create | REQ-003 | EP (invalid) / API negative | Fail | DEF-019 |
| [TC-API-021](04_Web_API/test_cases.md#tc-api-021---urgency-boundaries-returned-by-the-api) | Urgency boundaries returned by the API | REQ-006 | BVA / API | Fail | DEF-002 |
| [TC-API-022](04_Web_API/test_cases.md#tc-api-022---read-own-task) | Read own task | REQ-003 | API functional | Pass | — |
| [TC-API-023](04_Web_API/test_cases.md#tc-api-023---read-a-non-existent-task) | Read a non-existent task | REQ-003, REQ-009 | EP (invalid id) / API negative | Pass | — |
| [TC-API-024](04_Web_API/test_cases.md#tc-api-024---read-another-users-task) | Read another user's task | REQ-008 | EP (foreign id) / API negative | Pass | — |
| [TC-API-025](04_Web_API/test_cases.md#tc-api-025---non-integer-task-id) | Non-integer task id | REQ-009 | EP (invalid type) / API negative | Pass | — |
| [TC-API-026](04_Web_API/test_cases.md#tc-api-026---filter-by-category) | Filter by category | REQ-005 | EP / API functional | Pass | — |
| [TC-API-027](04_Web_API/test_cases.md#tc-api-027---filter-by-status) | Filter by status | REQ-005 | EP / API functional | Pass | — |
| [TC-API-028](04_Web_API/test_cases.md#tc-api-028---title-search) | Title search | REQ-005 | EP / API functional | Pass | — |
| [TC-API-029](04_Web_API/test_cases.md#tc-api-029---combined-filters) | Combined filters | REQ-005 | Decision table / API functional | Pass | — |
| [TC-API-030](04_Web_API/test_cases.md#tc-api-030---search-text-containing-an-apostrophe) | Search text containing an apostrophe | REQ-005 | EP (special character) / API negative | Fail | DEF-017 |
| [TC-API-031](04_Web_API/test_cases.md#tc-api-031---pagination) | Pagination | REQ-005, REQ-009 | BVA / API functional | Pass | — |
| [TC-API-032](04_Web_API/test_cases.md#tc-api-032---invalid-pagination-parameters) | Invalid pagination parameters | REQ-009 | EP + BVA (invalid) / API negative | Fail | DEF-022 |
| [TC-API-033](04_Web_API/test_cases.md#tc-api-033---task-list-scoped-to-the-user) | Task list scoped to the user | REQ-008 | EP / API | Pass | — |
| [TC-API-034](04_Web_API/test_cases.md#tc-api-034---partial-update) | Partial update | REQ-003 | API functional | Pass | — |
| [TC-API-035](04_Web_API/test_cases.md#tc-api-035---complete-and-reopen-through-the-api) | Complete and reopen through the API | REQ-004 | State transition (Open -> Done -> Open) / API | Pass | — |
| [TC-API-036](04_Web_API/test_cases.md#tc-api-036---invalid-values-on-update) | Invalid values on update | REQ-003, REQ-009 | EP (invalid) / API negative | Fail | DEF-015, DEF-018, DEF-019, DEF-020 |
| [TC-API-037](04_Web_API/test_cases.md#tc-api-037---update-another-users-task) | Update another user's task | REQ-008 | EP (foreign id) / API negative | Pass | — |
| [TC-API-038](04_Web_API/test_cases.md#tc-api-038---update-a-non-existent-task) | Update a non-existent task | REQ-009 | EP (invalid id) / API negative | Pass | — |
| [TC-API-039](04_Web_API/test_cases.md#tc-api-039---delete-own-task) | Delete own task | REQ-003 | State transition (exists -> deleted) / API | Pass | — |
| [TC-API-040](04_Web_API/test_cases.md#tc-api-040---delete-another-users-task) | Delete another user's task | REQ-008 | EP (foreign id) / API negative | Fail | DEF-014 |
| [TC-API-041](04_Web_API/test_cases.md#tc-api-041---delete-a-non-existent-task) | Delete a non-existent task | REQ-009 | EP (invalid id) / API negative | Fail | DEF-021 |
| [TC-API-042](04_Web_API/test_cases.md#tc-api-042---dashboard-counts-with-a-controlled-dataset) | Dashboard counts with a controlled dataset | REQ-007 | API functional (oracle: independent count) | Pass | — |
| [TC-API-043](04_Web_API/test_cases.md#tc-api-043---task-due-today-is-not-overdue-on-the-dashboard) | Task due today is not overdue on the dashboard | REQ-006, REQ-007 | BVA / API | Fail | DEF-002 |
| [TC-API-044](04_Web_API/test_cases.md#tc-api-044---dashboard-scoped-to-the-user) | Dashboard scoped to the user | REQ-008 | EP / API | Pass | — |
| [TC-API-045](04_Web_API/test_cases.md#tc-api-045---unsupported-http-method) | Unsupported HTTP method | REQ-009 | EP (invalid method) / API negative | Pass | — |

## Week 5 - Security and performance

Source: [05_Security_Performance/test_cases.md](05_Security_Performance/test_cases.md)

| ID | Title | Requirement(s) | Technique | Status | Defect(s) |
| --- | --- | --- | --- | --- | --- |
| [SEC-01](05_Security_Performance/test_cases.md) | Login errors do not reveal which field is wrong | REQ-013 | Automated | Pass | — |
| [SEC-02](05_Security_Performance/test_cases.md) | Repeated failures are throttled | REQ-013 | Automated | Fail | DEF-024 |
| [SEC-03](05_Security_Performance/test_cases.md) | Every API endpoint needs login | REQ-013 | Automated | Fail | DEF-023 |
| [SEC-04](05_Security_Performance/test_cases.md) | Cookie has protective flags | REQ-013 | Automated | Fail | DEF-025 |
| [SEC-05](05_Security_Performance/test_cases.md) | Logout ends the session | REQ-013 | Automated | Fail | DEF-026 |
| [SEC-06](05_Security_Performance/test_cases.md) | Common passwords refused | REQ-013 | Automated | Fail | DEF-027 |
| [SEC-07](05_Security_Performance/test_cases.md) | Quote in search does not crash / Injection cannot read other users' tasks | REQ-013 | Automated | Fail | DEF-017, DEF-029 |
| [SEC-08](05_Security_Performance/test_cases.md) | Injection in login does not bypass auth | REQ-013 | Automated | Pass | — |
| [SEC-09](05_Security_Performance/test_cases.md) | Forms carry a CSRF token / Cross-site POST refused | REQ-013 | Automated | Fail | DEF-030 |
| [SEC-10](05_Security_Performance/test_cases.md) | Owner cannot be set by the client | REQ-013 | Automated | Pass | — |
| [SEC-11](05_Security_Performance/test_cases.md) | Security events are logged | REQ-013 | Manual | Fail | DEF-035 |
| [SEC-12](05_Security_Performance/test_cases.md) | Titles are escaped | REQ-013 | Automated | Fail | DEF-005 |
| [SEC-13](05_Security_Performance/test_cases.md) | Errors show no internals | REQ-013 | Automated | Fail | DEF-031 |
| [SEC-14](05_Security_Performance/test_cases.md) | Security headers present | REQ-013 | Automated | Fail | DEF-032 |
| [SEC-15](05_Security_Performance/test_cases.md) | Another user's task cannot be read | REQ-013 | Automated | Pass | — |
| [SEC-16](05_Security_Performance/test_cases.md) | Oversized titles refused | REQ-013 | Automated | Fail | DEF-033 |
| [SEC-17](05_Security_Performance/test_cases.md) | Page size is capped | REQ-013 | Automated | Fail | DEF-034 |
| [SEC-18](05_Security_Performance/test_cases.md) | Another user's task cannot be deleted | REQ-013 | Automated | Fail | DEF-014 |
| [SEC-19](05_Security_Performance/test_cases.md) | Another user's task cannot be edited | REQ-013 | Automated | Pass | — |
| [SEC-20](05_Security_Performance/test_cases.md) | Session cannot be forged | REQ-013 | Automated | Fail | DEF-028 |
| [SEC-21](05_Security_Performance/test_cases.md) | Passwords are hashed | REQ-013 | Automated | Pass | — |
| [SEC-22](05_Security_Performance/test_cases.md) | No known vulnerable packages | REQ-013 | Tool (pip-audit) | Fail | DEF-036 |
| [SEC-23](05_Security_Performance/test_cases.md) | No High static-analysis issues | REQ-013 | Tool (bandit) | Fail | DEF-028, DEF-031 |
| [SEC-24](05_Security_Performance/test_cases.md) | One bad date does not lock the user out | REQ-013 | Automated (re-test) | Fail | DEF-015 |
| [PERF-01](05_Security_Performance/test_cases.md) | Baseline, 1 user | REQ-014 | Performance (JMeter) | Pass | — |
| [PERF-02](05_Security_Performance/test_cases.md) | 5 users | REQ-014 | Performance (JMeter) | Pass | — |
| [PERF-03](05_Security_Performance/test_cases.md) | 10 users | REQ-014 | Performance (JMeter) | Pass | — |
| [PERF-04](05_Security_Performance/test_cases.md) | 25 users (expected small-team load) | REQ-014 | Performance (JMeter) | Pass | — |
| [PERF-05](05_Security_Performance/test_cases.md) | 50 users | REQ-014 | Performance (JMeter) | Pass | — |
| [PERF-06](05_Security_Performance/test_cases.md) | Find saturation and breakpoint | REQ-014 | Performance (JMeter) | Pass | — |
| [PERF-06b](05_Security_Performance/test_cases.md) | Sustained stress | REQ-014 | Performance (JMeter) | Blocked | — |
| [PERF-07](05_Security_Performance/test_cases.md) | Data volume 50 -> 2,000 tasks | REQ-014 | Performance (JMeter) | Fail | DEF-037 |

## Week 6 - Automation and regression

Source: [06_Automation_Regression/test_cases.md](06_Automation_Regression/test_cases.md)

| ID | Title | Requirement(s) | Technique | Status | Defect(s) |
| --- | --- | --- | --- | --- | --- |
| [TC-AUT-001](06_Automation_Regression/test_cases.md) | test_01_auth::test_username_length_boundaries | REQ-001 | BVA | Pass | — |
| [TC-AUT-002](06_Automation_Regression/test_cases.md) | test_01_auth::test_password_length_boundaries | REQ-001 | BVA | Fail | DEF-001 |
| [TC-AUT-003](06_Automation_Regression/test_cases.md) | test_01_auth::test_valid_registration_opens_task_list | REQ-001 | EP | Pass | — |
| [TC-AUT-004](06_Automation_Regression/test_cases.md) | test_01_auth::test_username_with_hyphen_is_rejected | REQ-001 | EP | Pass | — |
| [TC-AUT-005](06_Automation_Regression/test_cases.md) | test_01_auth::test_empty_registration_field_blocked_by_browser | REQ-001 | EP / browser validation | Pass | — |
| [TC-AUT-006](06_Automation_Regression/test_cases.md) | test_01_auth::test_login_decision_table | REQ-002 | Decision table | Pass | — |
| [TC-AUT-007](06_Automation_Regression/test_cases.md) | test_01_auth::test_protected_page_redirects_when_logged_out | REQ-002 | State transition | Pass | — |
| [TC-AUT-008](06_Automation_Regression/test_cases.md) | test_01_auth::test_logout_revokes_protected_page_access | REQ-002 | State transition | Pass | — |
| [TC-AUT-009](06_Automation_Regression/test_cases.md) | test_02_tasks::test_create_full_field_task_persists | REQ-003 | EP | Pass | — |
| [TC-AUT-010](06_Automation_Regression/test_cases.md) | test_02_tasks::test_create_title_only_task | REQ-003 | EP | Pass | — |
| [TC-AUT-011](06_Automation_Regression/test_cases.md) | test_02_tasks::test_empty_title_blocked_by_browser | REQ-003 | EP / browser validation | Pass | — |
| [TC-AUT-012](06_Automation_Regression/test_cases.md) | test_02_tasks::test_whitespace_only_title_rejected | REQ-003 | EP / input validation | Fail | DEF-003 |
| [TC-AUT-013](06_Automation_Regression/test_cases.md) | test_02_tasks::test_edit_persists_all_fields | REQ-003 | Functional | Pass | — |
| [TC-AUT-014](06_Automation_Regression/test_cases.md) | test_02_tasks::test_cancel_edit_preserves_saved_data | REQ-003 | State transition | Pass | — |
| [TC-AUT-015](06_Automation_Regression/test_cases.md) | test_02_tasks::test_cancel_deletion_retains_task | REQ-003 | State transition | Pass | — |
| [TC-AUT-016](06_Automation_Regression/test_cases.md) | test_02_tasks::test_confirm_deletion_removes_only_that_task | REQ-003 | State transition | Pass | — |
| [TC-AUT-017](06_Automation_Regression/test_cases.md) | test_02_tasks::test_complete_then_reopen_task | REQ-004 | State transition | Pass | — |
| [TC-AUT-018](06_Automation_Regression/test_cases.md) | test_02_tasks::test_special_characters_preserved_in_edit_form | REQ-003 | Functional | Pass | — |
| [TC-AUT-019](06_Automation_Regression/test_cases.md) | test_02_tasks::test_special_characters_displayed_literally_in_list | REQ-003 | Functional | Fail | DEF-005 |
| [TC-AUT-020](06_Automation_Regression/test_cases.md) | test_02_tasks::test_each_account_sees_only_its_own_tasks | REQ-008 | EP | Pass | — |
| [TC-AUT-021](06_Automation_Regression/test_cases.md) | test_03_filters::test_filters_return_only_matching_tasks | REQ-005 | EP / decision table | Pass | — |
| [TC-AUT-022](06_Automation_Regression/test_cases.md) | test_04_urgency_dashboard::test_urgency_label | REQ-006 | BVA | Fail | DEF-002 |
| [TC-AUT-023](06_Automation_Regression/test_cases.md) | test_04_urgency_dashboard::test_completion_overrides_overdue | REQ-004, REQ-006 | State transition | Pass | — |
| [TC-AUT-024](06_Automation_Regression/test_cases.md) | test_04_urgency_dashboard::test_dashboard_counters_unaffected_by_def002 | REQ-007 | Independent calculation | Pass | — |
| [TC-AUT-025](06_Automation_Regression/test_cases.md) | test_04_urgency_dashboard::test_dashboard_overdue_counter | REQ-007 | Independent calculation | Fail | DEF-002 |
| [TC-AUT-026](06_Automation_Regression/test_cases.md) | test_05_rules_unit::test_username_rule | REQ-001 | BVA / EP (unit) | Pass | — |
| [TC-AUT-027](06_Automation_Regression/test_cases.md) | test_05_rules_unit::test_password_rule | REQ-001 | BVA (unit) | Fail | DEF-001 |
| [TC-AUT-028](06_Automation_Regression/test_cases.md) | test_05_rules_unit::test_urgency_rule | REQ-006 | BVA (unit) | Fail | DEF-002 |
| [TC-AUT-029](06_Automation_Regression/test_cases.md) | test_06_api::test_api_register_valid_account | REQ-001 | EP / API functional | Pass | — |
| [TC-AUT-030](06_Automation_Regression/test_cases.md) | test_06_api::test_api_username_valid_length_boundaries | REQ-001 | BVA / API | Pass | — |
| [TC-AUT-031](06_Automation_Regression/test_cases.md) | test_06_api::test_api_invalid_username_partitions | REQ-001 | EP + BVA / API negative | Pass | — |
| [TC-AUT-032](06_Automation_Regression/test_cases.md) | test_06_api::test_api_password_length_7_rejected | REQ-001 | BVA / API negative | Pass | — |
| [TC-AUT-033](06_Automation_Regression/test_cases.md) | test_06_api::test_api_password_length_8_accepted | REQ-001 | BVA / API | Fail | DEF-001 |
| [TC-AUT-034](06_Automation_Regression/test_cases.md) | test_06_api::test_api_missing_password_rejected | REQ-001 | EP / API negative | Pass | — |
| [TC-AUT-035](06_Automation_Regression/test_cases.md) | test_06_api::test_api_username_wrong_json_type | REQ-001, REQ-009 | EP (data type) / API negative | Fail | DEF-018 |
| [TC-AUT-036](06_Automation_Regression/test_cases.md) | test_06_api::test_api_duplicate_username_rejected | REQ-001 | EP / API negative | Fail | DEF-016 |
| [TC-AUT-037](06_Automation_Regression/test_cases.md) | test_06_api::test_api_login_valid_credentials | REQ-002 | Decision table (valid/valid) / API | Pass | — |
| [TC-AUT-038](06_Automation_Regression/test_cases.md) | test_06_api::test_api_login_invalid_credentials | REQ-002 | Decision table / API negative | Pass | — |
| [TC-AUT-039](06_Automation_Regression/test_cases.md) | test_06_api::test_api_protected_endpoints_require_session | REQ-002, REQ-009 | EP (unauthenticated) / API negative | Pass | — |
| [TC-AUT-040](06_Automation_Regression/test_cases.md) | test_06_api::test_api_categories_require_session | REQ-009 | EP (unauthenticated) / API negative | Fail | DEF-023 |
| [TC-AUT-041](06_Automation_Regression/test_cases.md) | test_06_api::test_api_list_categories | REQ-009 | API functional | Pass | — |
| [TC-AUT-042](06_Automation_Regression/test_cases.md) | test_06_api::test_api_create_task_with_all_fields | REQ-003 | EP (valid) / API functional | Pass | — |
| [TC-AUT-043](06_Automation_Regression/test_cases.md) | test_06_api::test_api_create_title_only_task | REQ-003 | EP (valid, optional fields omitted) / API | Pass | — |
| [TC-AUT-044](06_Automation_Regression/test_cases.md) | test_06_api::test_api_title_required | REQ-003 | EP (invalid) / API negative | Pass | — |
| [TC-AUT-045](06_Automation_Regression/test_cases.md) | test_06_api::test_api_non_json_body_rejected | REQ-009 | EP (invalid format) / API negative | Pass | — |
| [TC-AUT-046](06_Automation_Regression/test_cases.md) | test_06_api::test_api_wrong_json_types_on_create | REQ-003, REQ-009 | EP (data type) / API negative | Fail | DEF-018 |
| [TC-AUT-047](06_Automation_Regression/test_cases.md) | test_06_api::test_api_invalid_due_date_on_create | REQ-003, REQ-006 | EP (invalid) / API negative | Fail | DEF-015 |
| [TC-AUT-048](06_Automation_Regression/test_cases.md) | test_06_api::test_api_invalid_category_on_create | REQ-003 | EP (invalid) / API negative | Fail | DEF-019 |
| [TC-AUT-049](06_Automation_Regression/test_cases.md) | test_06_api::test_api_urgency_boundaries | REQ-006 | BVA / API | Fail | DEF-002 |
| [TC-AUT-050](06_Automation_Regression/test_cases.md) | test_06_api::test_api_read_own_task | REQ-003 | API functional | Pass | — |
| [TC-AUT-051](06_Automation_Regression/test_cases.md) | test_06_api::test_api_read_missing_task | REQ-003, REQ-009 | EP (invalid id) / API negative | Pass | — |
| [TC-AUT-052](06_Automation_Regression/test_cases.md) | test_06_api::test_api_read_another_users_task | REQ-008 | EP (foreign id) / API negative | Pass | — |
| [TC-AUT-053](06_Automation_Regression/test_cases.md) | test_06_api::test_api_non_integer_task_id | REQ-009 | EP (invalid type) / API negative | Pass | — |
| [TC-AUT-054](06_Automation_Regression/test_cases.md) | test_06_api::test_api_filter_by_category | REQ-005 | EP / API functional | Pass | — |
| [TC-AUT-055](06_Automation_Regression/test_cases.md) | test_06_api::test_api_filter_by_status | REQ-005 | EP / API functional | Pass | — |
| [TC-AUT-056](06_Automation_Regression/test_cases.md) | test_06_api::test_api_title_search | REQ-005 | EP / API functional | Pass | — |
| [TC-AUT-057](06_Automation_Regression/test_cases.md) | test_06_api::test_api_combined_filters | REQ-005 | Decision table / API functional | Pass | — |
| [TC-AUT-058](06_Automation_Regression/test_cases.md) | test_06_api::test_api_search_with_apostrophe | REQ-005 | EP (special character) / API negative | Fail | DEF-017 |
| [TC-AUT-059](06_Automation_Regression/test_cases.md) | test_06_api::test_api_pagination | REQ-005, REQ-009 | BVA / API functional | Pass | — |
| [TC-AUT-060](06_Automation_Regression/test_cases.md) | test_06_api::test_api_invalid_pagination | REQ-009 | EP + BVA (invalid) / API negative | Fail | DEF-022 |
| [TC-AUT-061](06_Automation_Regression/test_cases.md) | test_06_api::test_api_task_list_scoped_to_user | REQ-008 | EP / API | Pass | — |
| [TC-AUT-062](06_Automation_Regression/test_cases.md) | test_06_api::test_api_partial_update | REQ-003 | API functional | Pass | — |
| [TC-AUT-063](06_Automation_Regression/test_cases.md) | test_06_api::test_api_complete_and_reopen | REQ-004 | State transition (Open -> Done -> Open) / API | Pass | — |
| [TC-AUT-064](06_Automation_Regression/test_cases.md) | test_06_api::test_api_invalid_values_on_update | REQ-003, REQ-009 | EP (invalid) / API negative | Fail | DEF-015, DEF-018, DEF-019, DEF-020 |
| [TC-AUT-065](06_Automation_Regression/test_cases.md) | test_06_api::test_api_update_another_users_task | REQ-008 | EP (foreign id) / API negative | Pass | — |
| [TC-AUT-066](06_Automation_Regression/test_cases.md) | test_06_api::test_api_update_missing_task | REQ-009 | EP (invalid id) / API negative | Pass | — |
| [TC-AUT-067](06_Automation_Regression/test_cases.md) | test_06_api::test_api_delete_own_task | REQ-003 | State transition (exists -> deleted) / API | Pass | — |
| [TC-AUT-068](06_Automation_Regression/test_cases.md) | test_06_api::test_api_delete_another_users_task | REQ-008 | EP (foreign id) / API negative | Fail | DEF-014 |
| [TC-AUT-069](06_Automation_Regression/test_cases.md) | test_06_api::test_api_delete_missing_task | REQ-009 | EP (invalid id) / API negative | Fail | DEF-021 |
| [TC-AUT-070](06_Automation_Regression/test_cases.md) | test_06_api::test_api_dashboard_counts | REQ-007 | API functional (oracle: independent count) | Pass | — |
| [TC-AUT-071](06_Automation_Regression/test_cases.md) | test_06_api::test_api_dashboard_due_today_not_overdue | REQ-006, REQ-007 | BVA / API | Fail | DEF-002 |
| [TC-AUT-072](06_Automation_Regression/test_cases.md) | test_06_api::test_api_dashboard_scoped_to_user | REQ-008 | EP / API | Pass | — |
| [TC-AUT-073](06_Automation_Regression/test_cases.md) | test_06_api::test_api_unsupported_method | REQ-009 | EP (invalid method) / API negative | Pass | — |
| [TC-AUT-074](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_register_through_form | REQ-001 | Workflow / web | Pass | — |
| [TC-AUT-075](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_registration_validated_on_server | REQ-001 | Client-server validation / EP | Pass | — |
| [TC-AUT-076](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_login_through_form | REQ-002 | Decision table / web | Pass | — |
| [TC-AUT-077](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_protected_pages_redirect_when_logged_out | REQ-002 | EP (unauthenticated) / web | Pass | — |
| [TC-AUT-078](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_created_task_matches_api | REQ-003 | Workflow / UI vs API comparison | Pass | — |
| [TC-AUT-079](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_api_created_task_matches_web_list | REQ-003, REQ-006 | Workflow / API vs UI comparison | Pass | — |
| [TC-AUT-080](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_edit_matches_api | REQ-003 | Workflow / UI vs API comparison | Pass | — |
| [TC-AUT-081](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_toggle_matches_api | REQ-004 | State transition / UI vs API comparison | Pass | — |
| [TC-AUT-082](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_delete_matches_api | REQ-003 | Workflow / UI vs API comparison | Pass | — |
| [TC-AUT-083](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_blank_title_validated_on_server | REQ-003 | Client-server validation / EP | Fail | DEF-003 |
| [TC-AUT-084](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_due_date_validated_on_server | REQ-003, REQ-006 | Client-server validation / EP | Fail | DEF-015 |
| [TC-AUT-085](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_category_validated_on_server | REQ-003 | Client-server validation / EP | Fail | DEF-019 |
| [TC-AUT-086](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_actions_on_another_users_task | REQ-008 | EP (foreign id) / UI vs API comparison | Pass | — |
| [TC-AUT-087](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_dashboard_matches_api | REQ-007 | UI vs API comparison | Pass | — |
| [TC-AUT-088](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_search_with_apostrophe | REQ-005 | EP (special character) / UI vs API comparison | Pass | — |
| [TC-AUT-089](06_Automation_Regression/test_cases.md) | test_07_web_forms::test_web_duplicate_username_rejected | REQ-001 | EP / web negative | Fail | DEF-016 |
