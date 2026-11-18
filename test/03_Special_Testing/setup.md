# Week 3 — Environment setup and test execution guide

This guide accompanies the [Week 3 report](README.md). Run all shell commands
from the repository root on branch `w3-special-testing`. The GUI and
compatibility cases are executed by Playwright scripts driven by pytest; the
usability review and the screen-reader parts of accessibility remain manual.

## Verified environment

| Component | Verified version |
| --- | --- |
| Python | 3.14.7 |
| pytest | 9.1.1 |
| pytest-playwright | 0.10.0 |
| Playwright (Python) | 1.65.2 |
| Flask | 3.0.3 |
| Google Chrome (macOS, C01) | 157.0.8103.80, driven through Playwright's `chrome` channel |
| Mozilla Firefox (macOS, C04) | 160.0.1 installed; see [Firefox note](#firefox-configurations) |

The full dependency set is in `requirements-test-lock.txt`.

## 1. Create and activate the virtual environment

```bash
python3 -m venv test/03_Special_Testing/.venv
source test/03_Special_Testing/.venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv test/03_Special_Testing/.venv
.\test\03_Special_Testing\.venv\Scripts\Activate.ps1
```

## 2. Install dependencies

```bash
python -m pip install -r test/03_Special_Testing/requirements-test-lock.txt
python -m pip check
```

Chrome configurations use the **installed Google Chrome** through Playwright's
`chrome` channel, so no browser download is needed for them. Check the installed
version before a run and record it in [README 2.1](README.md#21-configurations).

## 3. Run the suites

The suites start `python app.py` automatically if nothing is serving
`http://127.0.0.1:5000`, and stop it afterwards. They use the existing
development database and register new accounts named
`w3<initial>_<purpose>_<mmddHHMMSS>` for each run, so earlier data is not changed.
Test data is loaded from [fixtures.json](fixtures.json).

Always pass the Week 3 folder as the path so pytest uses
`test/03_Special_Testing/pytest.ini`, not the repository-root configuration that
belongs to Week 2.

```bash
# Task 1 - GUI checklist (baseline C01 only)
python -m pytest test/03_Special_Testing/1_GUI --w3-config C01

# Task 2 - compatibility smoke scenarios, once per configuration
python -m pytest test/03_Special_Testing/2_Compatibility --w3-config C01
python -m pytest test/03_Special_Testing/2_Compatibility --w3-config C02
python -m pytest test/03_Special_Testing/2_Compatibility --w3-config C03
```

Add `--headed` to watch the browser. Runs are headless by default.

## 4. Outputs

| Output | Location |
| --- | --- |
| GUI screenshots | `1_GUI/evidences/TC-GUI-0xx-<desc>-<YYYYMMDD>.jpg` |
| Compatibility screenshots | `2_Compatibility/evidences/<os>-<browser>/<viewport>/TC-CMP-0xx-<desc>-<YYYYMMDD>.jpg` |
| Per-run results (status, every check with its actual value, notes, evidence list) | `results-<config>-<YYYYMMDD>-<HHMMSS>.json` in the same evidence folder |

A case fails if any check derived from its expected result fails; the results
file lists every failed check, not only the first. Screenshots are overwritten by
a later run on the same day, and each run keeps its own results file.

## 5. What the scripts cannot cover

- Native browser UI is not drawn in page screenshots: the delete confirmation
  dialog, the date picker and the required-field validation bubble. The scripts
  record the dialog text and the validation message instead.
- Date fields are filled by value, so the usability of each browser's date
  picker is not exercised.
- Visual judgements (spacing, colour consistency) are recorded as notes and judged
  from the screenshots. Readability on emulated devices is measured as the rendered
  text size (TC-CMP-007).
- On emulated mobile devices, screenshots capture the device screen, not the whole
  layout.

## Firefox configurations

Playwright cannot drive a normally installed Firefox; it runs its own patched
Firefox build. Running C04/C06 through Playwright therefore tests that build,
not the installed Firefox 160.0.1. The choice for C04/C06 is recorded in
[README 2.1](README.md#21-configurations).
