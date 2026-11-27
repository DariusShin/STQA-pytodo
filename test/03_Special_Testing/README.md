# 03_Special_Testing - GUI, Compatibility, Usability and Accessibility Testing

Week 3 checks how PyTodo Pro's pages look and behave: a GUI checklist, a browser/OS/viewport compatibility matrix, a short usability session and a basic WCAG 2.2 accessibility review. GUI, compatibility and accessibility cases are automated with Playwright and pytest.

| File / folder | Contents |
| --- | --- |
| [W3_Report.md](W3_Report.md) | Week 3 report: scope, GUI results, compatibility matrix, usability observations, accessibility findings, recommendations |
| [defects.md](defects.md) | DEF-004 to DEF-013, and re-tests of DEF-001 to DEF-003 |
| [1_GUI/](1_GUI/) | `test_cases.md` (TC-GUI-001 to 022), `test_gui.py`, `evidences/` |
| [2_Compatibility/](2_Compatibility/) | `test_cases.md` (TC-CMP-001 to 008), `test_compatibility.py`, `evidences/<os>-<browser>/<viewport>/` |
| [3_Usability/](3_Usability/) | `observations.md` (USA-OBS-001 to 004, rated) |
| [4_Accessibility/](4_Accessibility/) | `test_cases.md` (TC-A11Y-001 to 018), `test_accessibility.py`, `evidences/` and scan reports in `evidences/reports/` |
| [fixtures.md](fixtures.md), `fixtures.json` | Precondition codes, accounts and Fixture Set A (readable and script form) |
| `conftest.py`, `pytest.ini`, `requirements-test-lock.txt` | Playwright/pytest harness and exact package versions |
| `seed_fixtures.py` | Creates a seeded account for manual checks |

Each run writes `results-<config>-<YYYYMMDD>-<HHMMSS>.json` next to its screenshots, listing every check with its actual value.

## How to run

From the repository root (Python 3.14; the suites start `python app.py` themselves and register fresh accounts for each run):

```bash
python3 -m venv test/03_Special_Testing/.venv
source test/03_Special_Testing/.venv/bin/activate        # Windows: .\test\03_Special_Testing\.venv\Scripts\Activate.ps1
python -m pip install -r test/03_Special_Testing/requirements-test-lock.txt
python -m playwright install firefox                     # only for C04 and C06

python -m pytest test/03_Special_Testing/1_GUI --w3-config C01
python -m pytest test/03_Special_Testing/4_Accessibility --w3-config C01      # includes axe and Lighthouse (Lighthouse needs Node.js/npx)
python -m pytest test/03_Special_Testing/2_Compatibility --w3-config C01      # repeat with C02 ... C06
```

- Always pass the Week 3 folder as the path, so pytest uses this folder's `pytest.ini`.
- `--w3-config` picks the browser and viewport: C01-C03 use the installed Google Chrome; C04 and C06 use Playwright's Firefox build. C05 and C06 are run on Windows 11; set their `viewport` in `fixtures.json` to the machine's CSS resolution (1536x864 for a 1920x1080 screen at 125%).
- Add `--headed` to watch the browser.
- For a manual check, start `python app.py` and run `python test/03_Special_Testing/seed_fixtures.py --initial <letter>` to create a seeded account.
