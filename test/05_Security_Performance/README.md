# 05_Security_Performance - Security and Performance Testing

Week 5 builds a STRIDE threat table, derives safe security tests from it (pytest, pip-audit, bandit), and runs a controlled load, stress and data-volume experiment with Apache JMeter.

| File / folder | Contents |
| --- | --- |
| [W5_Report.md](W5_Report.md) | Week 5 report: STRIDE table, security results, performance design, results and interpretation, limitations, recommendations |
| [test_cases.md](test_cases.md) | SEC-01 to SEC-24 and PERF-01 to PERF-07 |
| [defects.md](defects.md) | DEF-024 to DEF-037, and re-tests of DEF-005, 014, 015, 017, 023 |
| `test_security.py`, `conftest.py`, `client.py`, `config.py`, `pytest.ini` | Security test suite and settings |
| [jmeter/](jmeter/) | `pytodo_load.jmx` (PERF-01 to 06), `pytodo_data_volume.jmx` (PERF-07), `run_performance.py` (runs JMeter, builds tables and charts), `run_perf_server.py` (starts the unchanged app on a fresh database) |
| [evidences/security/](evidences/security/) | SEC screenshots, raw pytest output, `bandit.txt`, `pip_audit.txt`, machine specs of the security run |
| [evidences/performance/20261127-mac/](evidences/performance/20261127-mac/) | `perf_summary.md` / `.csv`, charts, `run.json` (environment), raw JMeter results `*.jtl.gz`, server logs, JMeter HTML dashboards for PERF-05, PERF-06b and the 200-user stress step |

## How to run

**Security tests** (about 5 s). Start a fresh copy of the app (`python app.py` from the repository root, with `pytodo_pro.db` deleted), then:

```bash
cd test/05_Security_Performance
pip install pytest requests bandit pip-audit
export PYTODO_DB=../../pytodo_pro.db          # Windows PowerShell: $env:PYTODO_DB="..\..\pytodo_pro.db"
pytest test_security.py -v -rA --raw          # evidence run: every finding shows as FAILED (17 failed, 6 passed)
pytest test_security.py -v -rA                # regression run: findings show as XFAIL with their defect ID
pip-audit -r ../../requirements.txt
bandit -r ../../app.py ../../helpers.py
```

An `XPASS(strict)` in the regression run means a defect was fixed: re-test and close it.

**Performance tests** (Apache JMeter 5.6.3 and Java required; the runner starts and stops the app itself):

```bash
pip install -r ../../requirements.txt matplotlib
cd test/05_Security_Performance/jmeter
python run_performance.py --quick                          # 2-minute script check
python run_performance.py --out ../evidences/performance/<run-name>                 # PERF-01 to 05, 06b, 07 (~15 min)
python run_performance.py --stress-steps --out ../evidences/performance/<run-name>  # PERF-06 stepped stress (~7 min)
python run_performance.py --analyse ../evidences/performance/<run-name>             # rebuild tables and charts
```

Options: `--jmeter <path to jmeter>` if it is not on `PATH`, `--port 5016` if 5015 is in use. The plans can also be opened in the JMeter GUI to inspect the thread groups, samplers and assertions.
