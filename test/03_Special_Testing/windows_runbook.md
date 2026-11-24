# Week 3 — Windows 11 runbook (C05 Chrome, C06 Firefox)

This runbook explains how to run the compatibility smoke set (TC-CMP-001 to 008) on the Windows 11 laptop, from a clean machine to committed evidence. It follows the run plan in [README 2.4.2](README.md#242-windows-11-run-c05-chrome-c06-firefox) and the general [setup.md](setup.md). Those two files are the source of truth for the plan; this file adds only the Windows-specific commands.

| Item | Value |
| --- | --- |
| Machine | Acer Nitro 5 (2021) owned by Darius Lee Shin (see [README 0.5](README.md#05-environment-to-record)) |
| Configurations | C05 = Google Chrome through Playwright's `chrome` channel; C06 = Playwright's Firefox build |
| Evidence folders | `2_Compatibility/evidences/win-chrome/desktop/` and `2_Compatibility/evidences/win-firefox/desktop/` |
| Time needed | About 30 minutes for setup; each scripted run takes under a minute |

Run every command in **PowerShell** from the repository root unless a step says otherwise. Do not run any other suite (GUI, accessibility) on Windows: they belong to the C01 baseline only.

## 1. Record the machine

Fill in the [record sheet](#7-record-sheet) as you go. Each value goes back into the README.

```powershell
# Windows edition, version and build (or run winver)
Get-ComputerInfo -Property OsName, OsDisplayVersion, OsBuildNumber

# Exact laptop model and CPU (or run msinfo32)
Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer, Model
Get-CimInstance Win32_Processor | Select-Object Name

# Regional format and short-date pattern used by the date picker
Get-Culture | Select-Object Name, DisplayName
(Get-Culture).DateTimeFormat.ShortDatePattern

# System timezone; the Mac runs used Asia/Kuala_Lumpur
Get-TimeZone | Select-Object Id, DisplayName
```

Read the display values from **Settings -> System -> Display** on the built-in screen:

- **Display resolution** (native, marked "Recommended")
- **Scale** (laptops often default to 125% or 150%)

If an external monitor is connected, unplug it or make the built-in screen the main display, and record that you did.

**Timezone.** The scripts calculate due dates from the system date (`date.today()`), and the browser uses the system timezone. Set Windows to **(UTC+08:00) Kuala Lumpur, Singapore** (`Singapore Standard Time`) under Settings -> Time & language -> Date & time so that the urgency badges match the Mac runs.

## 2. Install the tools

| Tool | How | Check |
| --- | --- | --- |
| Git for Windows | <https://git-scm.com/download/win>, default options | `git --version` |
| Python 3.14.7 | python.org Windows installer (64-bit). Tick **Add python.exe to PATH**. Matches the Mac runs ([setup.md](setup.md#verified-environment)) | `py -3.14 --version` |
| Google Chrome | <https://www.google.com/chrome/> if not installed | Version recorded in [step 5](#5-record-the-browser-versions) |

Node.js is **not** needed: the compatibility suite does not run Lighthouse.

**Chrome updates.** Chrome updates itself. Record its version just before the first run and finish both C05 runs before restarting Chrome. If it updates between runs, record both versions.

## 3. Get the branch and create the environment

```powershell
# First time only (choose any parent folder)
git clone https://github.com/DariusShin/STQA-pytodo.git
cd STQA-pytodo

# Every time
git switch w3-special-testing
git pull
```

Create and activate the Week 3 virtual environment ([setup.md 1-2](setup.md#1-create-and-activate-the-virtual-environment)):

```powershell
py -3.14 -m venv test/03_Special_Testing/.venv

# Windows blocks activation scripts by default; allow them for this window only
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\test\03_Special_Testing\.venv\Scripts\Activate.ps1

python --version          # must print 3.14.7
python -m pip install -r test/03_Special_Testing/requirements-test-lock.txt
python -m pip check
python -m playwright install firefox    # Playwright's Firefox build, for C06
```

The `(.venv)` prefix shows that the environment is active. Re-run `Set-ExecutionPolicy` and `Activate.ps1` in every new PowerShell window.

The application database (`pytodo_pro.db`) is not in Git. `app.py` creates a fresh one on first start, and the scripts register and seed their own accounts, so no data needs to be copied from the Mac.

## 4. Configure `fixtures.json`

Open `test/03_Special_Testing/fixtures.json` and check these values:

1. **`configurations.C05.viewport` and `configurations.C06.viewport`.** Set both to the screen's CSS resolution: the native resolution divided by the scale.

   | Native resolution | Scale | CSS viewport (width x height) |
   | --- | --- | --- |
   | 1920x1080 | 100% | 1920x1080 |
   | 1920x1080 | 125% | 1536x864 (current value in the file) |
   | 1920x1080 | 150% | 1280x720 |
   | 2560x1440 | 150% | 1707x960 |

   Round to whole pixels. Use the same viewport for C05 and C06 so that the two browsers are compared at the same size.

2. **`tester_initial`.** Currently `"d"`. Change it only if another member runs the suite. It must be a single letter, because it is part of the 20-character usernames.

Commit the edited `fixtures.json` with the evidence ([step 8](#8-commit-the-evidence)) so that the run can be repeated with the same settings.

## 5. Record the browser versions

The results files do not record browser versions, so print them before the first run:

```powershell
@'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    for label, launch in (("C05 Chrome", lambda: p.chromium.launch(channel="chrome")),
                          ("C06 Playwright Firefox", p.firefox.launch)):
        browser = launch()
        print(label, browser.version)
        browser.close()
'@ | python -
```

Cross-check the Chrome version at `chrome://version`. The installed Mozilla Firefox, if any, is not used by the scripts ([setup.md](setup.md#firefox-configurations)).

## 6. Run the suites

Run each configuration **twice**, so that any failure is reproduced (README [0.8](README.md#08-entry-and-exit-criteria) exit criteria):

```powershell
python -m pytest test/03_Special_Testing/2_Compatibility --w3-config C05
python -m pytest test/03_Special_Testing/2_Compatibility --w3-config C05

python -m pytest test/03_Special_Testing/2_Compatibility --w3-config C06
python -m pytest test/03_Special_Testing/2_Compatibility --w3-config C06
```

- Always pass the `test/03_Special_Testing/...` path, so that pytest uses the Week 3 `pytest.ini`.
- The scripts start `python app.py` themselves and stop it afterwards. If something else is already serving `http://127.0.0.1:5000`, the scripts reuse it, so make sure it is this checkout's app at the same commit.
- Add `--headed` to watch the browser. The recorded runs should stay headless, as on the Mac.
- If Windows Firewall asks about Python, **Cancel** is fine: the app only listens on 127.0.0.1.

**Outputs.** Each run writes screenshots to the evidence folder and its own `results-<config>-<YYYYMMDD>-<HHMMSS>.json`. Screenshots from the second run overwrite those from the first on the same day; both results files are kept.

**Interpreting the results.**

| Result | Action |
| --- | --- |
| 8/8 Pass in both runs | Record `Pass` for each case |
| A case fails in both runs | Open the results file to find the failed check. Compare it with the C01 result. A new failure that breaks a stated expectation becomes a `DEF-` record (Task 5); a cosmetic difference becomes `Diff (USA-OBS-xxx)` |
| A case fails in only one run | Run the configuration a third time and record what happened in the notes. Do not log a defect from a single failure |
| TC-CMP-007 fails as on C02/C03 | Check whether the cause is DEF-004/DEF-006 (narrow layout). At a desktop viewport this is not expected, so record the viewport in use |
| TC-CMP-008 values differ from C01 | Expected when the run date differs from 2026-11-18: the counts depend on the day. Compare with C01's values recalculated for the run date |

## 7. Record sheet

Fill this in during steps 1-6, then copy each value into the listed place.

| Value | Recorded | Goes into |
| --- | --- | --- |
| Run date and time | | README [2.1](README.md#21-configurations) Available? column |
| Application commit (`git rev-parse --short HEAD`) | | README [0.5](README.md#05-environment-to-record) |
| Windows edition, version, build | | README 0.5 and 2.1 OS column |
| Laptop model, CPU | | README 0.5 Windows hardware row |
| Native resolution / scale / CSS viewport used | | README 2.1 Viewport and Zoom columns |
| Regional format / short-date pattern | | README 2.1 Locale column |
| Timezone | | README 2.1 Locale column |
| Chrome version (C05) | | README 0.5 and 2.1; [`test/README.md`](../README.md) browser row; [setup.md](setup.md#verified-environment) |
| Playwright Firefox build (C06) | | Same as Chrome |
| Results files (two per configuration) | | [2_Compatibility/test_cases.md](2_Compatibility/test_cases.md) run file list |
| C05 / C06 result for each case | | README [2.2](README.md#22-compatibility-smoke-scenarios) C05/C06 columns; each case's Status line in `2_Compatibility/test_cases.md` |

## 8. Commit the evidence

```powershell
git status
git add test/03_Special_Testing/2_Compatibility/evidences/win-chrome test/03_Special_Testing/2_Compatibility/evidences/win-firefox test/03_Special_Testing/fixtures.json
git commit -m "test: execute week 3 compatibility cases on C05 and C06 Windows"
git push
```

Check `git status` before adding: only the two evidence folders and `fixtures.json` should have changed. The `.venv` folder and `pytodo_pro.db` are ignored by `.gitignore`.

## 9. Update the report

These edits can be made on either machine after pulling the evidence commit:

1. README [2.1](README.md#21-configurations): fill in the C05 and C06 rows from the record sheet.
2. README [2.2](README.md#22-compatibility-smoke-scenarios): fill in the C05 and C06 columns.
3. README [2.5](README.md#25-interpretation): answer "OS-specific differences?" by comparing C05 with C01 (Chrome) and C06 with C04 (Firefox), and change "Based on C01-C04" to C01-C06.
4. README [Task 5](README.md#task-5): add any new defects to the 5.3 defect summary, update the 5.5 compatibility row and run counts (8 cases x 6 configurations = 48 case runs), and remove "C05/C06" from the pending notes and the Limitations row.
5. The phase status line at the top of the README and the Week 3 row in [`test/README.md`](../README.md).
6. Get another member to review the Windows captures, as planned in [README 0.7](README.md#07-work-allocation-and-schedule).
