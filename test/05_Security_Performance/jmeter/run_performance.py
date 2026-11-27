"""Week 5 performance runner: JMeter load, stress and data-volume tests (PERF-01 to PERF-07).

For every test it starts the unchanged app on a fresh database, runs JMeter in
non-GUI mode, saves the raw results (.jtl) and JMeter's HTML dashboard, stops the
server, and finally writes the summary tables and charts.

Usage (from this folder):
    python run_performance.py --out DIR                 # PERF-01 to 05, 06b and 07, about 15 minutes
    python run_performance.py --stress-steps --out DIR  # PERF-06 stepped stress, about 7 minutes
    python run_performance.py --quick                   # 1 and 5 users, 30 s each (script check)
    python run_performance.py --analyse DIR             # rebuild tables/charts for an existing run

Options: --jmeter PATH (default: `jmeter` on PATH), --port 5015, --out DIR.
"""

import argparse
import csv
import gzip
import json
import os
import platform
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
LOAD_PLAN = HERE / "pytodo_load.jmx"
VOLUME_PLAN = HERE / "pytodo_data_volume.jmx"
RESULTS = HERE.parent / "evidences" / "performance"

LOAD_STEPS = [("PERF-01", 1), ("PERF-02", 5), ("PERF-03", 10), ("PERF-04", 25), ("PERF-05", 50)]
STEADY_S = 120          # measured window per load step
STRESS = ("PERF-06b", 50, 90)  # sustained stress: id, users, measured seconds, no think time
# Stepped stress (no think time): short steps so the client's free local ports
# (about 16k, each held 30 s after closing on macOS) are not used up within a step.
STRESS_STEPS = [1, 5, 10, 25, 50, 100, 200]
STEP_RAMP_S, STEP_MEASURED_S, STEP_PAUSE_S = 5, 10, 35
VOLUME_SIZES = [50, 500, 2000]
TARGET = {"median_ms": 200, "p95_ms": 1000, "error_pct": 1.0}   # set before execution


# ---------------------------------------------------------------- execution
def wait_for_port(port, timeout=20):
    end = time.time() + timeout
    while time.time() < end:
        with socket.socket() as s:
            if s.connect_ex(("127.0.0.1", port)) == 0:
                return
        time.sleep(0.2)
    raise RuntimeError(f"server did not start on port {port}")


def run_one(test_id, plan, props, out, port, jmeter):
    db_dir = tempfile.mkdtemp(prefix="pytodo_perf_")
    log = open(out / f"{test_id}_server.log", "w")
    server = subprocess.Popen([sys.executable, "-B", str(HERE / "run_perf_server.py"),
                               os.path.join(db_dir, "perf.db"), str(port)],
                              stdout=log, stderr=subprocess.STDOUT)
    try:
        wait_for_port(port)
        jtl = out / f"{test_id}.jtl"
        report = out / f"{test_id}_dashboard"
        for p in (jtl, report):
            if p.is_dir():
                shutil.rmtree(p)
            elif p.exists():
                p.unlink()
        cmd = [jmeter, "-n", "-t", str(plan), "-l", str(jtl), "-j", str(out / f"{test_id}_jmeter.log"),
               "-e", "-o", str(report), "-Jjmeter.reportgenerator.sample_filter=^(?!SETUP).*",
               f"-Jport={port}"] + [f"-J{k}={v}" for k, v in props.items()]
        print(f"[{datetime.now():%H:%M:%S}] {test_id}: {props}")
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    finally:
        server.terminate()
        server.wait(10)
        log.close()
        shutil.rmtree(db_dir, ignore_errors=True)


def environment(jmeter):
    def cmd(*a):
        try:
            return subprocess.run(a, capture_output=True, text=True, timeout=30).stdout.strip()
        except Exception:
            return ""
    from importlib.metadata import version
    cpu = cmd("sysctl", "-n", "machdep.cpu.brand_string") or platform.processor()
    mem = cmd("sysctl", "-n", "hw.memsize")
    jm = [l for l in cmd(jmeter, "--version").splitlines() if "5." in l]
    java = subprocess.run(["java", "-version"], capture_output=True, text=True).stderr.splitlines()
    return {
        "date": datetime.now().astimezone().isoformat(timespec="seconds"),
        "os": f"{platform.system()} {platform.mac_ver()[0] or platform.release()} ({platform.machine()})",
        "cpu": cpu, "logical_cpus": os.cpu_count(),
        "memory_gb": round(int(mem) / 2**30, 1) if mem.isdigit() else None,
        "python": platform.python_version(), "flask": version("flask"), "werkzeug": version("werkzeug"),
        "jmeter": jm[-1].strip().split()[-1] if jm else "", "java": java[0] if java else "",
        "server": "Flask built-in server, threaded, debug=True, reloader off, 127.0.0.1",
        "load_generator": "JMeter on the same machine",
    }


# ---------------------------------------------------------------- analysis
def pct(values, p):
    v = sorted(values)
    return v[max(0, int(round(p / 100 * len(v) + 0.5)) - 1)] if v else 0


def read_jtl(path):
    path = Path(path)
    if not path.exists() and path.with_suffix(".jtl.gz").exists():
        path = path.with_suffix(".jtl.gz")      # raw results are stored gzipped
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", newline="") as f:
        return [r for r in csv.DictReader(f) if not r["label"].startswith("SETUP")]


def window(rows, start_after_s, length_s=None):
    """Keep samples that started after ramp-up and inside the measured window."""
    if not rows:
        return rows
    t0 = min(int(r["timeStamp"]) for r in rows)
    lo = t0 + start_after_s * 1000
    hi = lo + length_s * 1000 if length_s else float("inf")
    return [r for r in rows if lo <= int(r["timeStamp"]) < hi]


def stats(rows, seconds):
    el = [int(r["elapsed"]) for r in rows]
    fails = [r for r in rows if r["success"] != "true"]
    return {
        "requests": len(rows), "rps": round(len(rows) / seconds, 1) if seconds else 0,
        "ok_rps": round((len(rows) - len(fails)) / seconds, 1) if seconds else 0,
        "median_ms": round(median(el)) if el else 0, "p95_ms": pct(el, 95), "p99_ms": pct(el, 99),
        "max_ms": max(el) if el else 0, "errors": len(fails),
        "error_pct": round(100 * len(fails) / len(rows), 2) if rows else 0,
        "connect_ms_median": round(median(int(r["Connect"]) for r in rows)) if rows else 0,
    }


def analyse(out):
    meta = json.loads((out / "run.json").read_text())
    lines, rows_csv, agg = [], [], []
    for t in meta["tests"]:
        if t["kind"] == "volume":
            continue
        rows = window(read_jtl(out / f"{t['id']}.jtl"), t["rampup"], t["measured_s"])
        overall = stats(rows, t["measured_s"])
        overall.update(id=t["id"], users=t["users"], kind=t["kind"])
        agg.append(overall)
        by_label = {}
        for r in rows:
            by_label.setdefault(r["label"], []).append(r)
        for label in sorted(by_label):
            s = stats(by_label[label], t["measured_s"])
            rows_csv.append({"test": t["id"], "users": t["users"], "endpoint": label, **s})
        rows_csv.append({"test": t["id"], "users": t["users"], "endpoint": "ALL", **overall})
        errs = {}
        for r in rows:
            if r["success"] != "true":
                msg = (r["responseMessage"] or r["failureMessage"] or "").splitlines()
                key = f"{r['label']}: {r['responseCode'][:60]} {msg[0] if msg else ''}"[:160].replace("|", "/")
                errs[key] = errs.get(key, 0) + 1
        t["errors"] = errs

    keys = ["test", "users", "endpoint", "requests", "rps", "median_ms", "p95_ms", "p99_ms", "max_ms",
            "errors", "error_pct", "connect_ms_median"]
    with open(out / "perf_summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows_csv)

    lines += ["# Week 5 performance results (JMeter)", "",
              f"Run: {meta['environment']['date']} on {meta['environment']['cpu']}, "
              f"{meta['environment']['os']}. Measured window excludes ramp-up.", "",
              "## Overall, per test", "",
              "| Test | Users | Think time | Requests | Req/s | Successful req/s | Median (ms) | p95 (ms) | p99 (ms) | Max (ms) | Errors |",
              "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for a in agg:
        lines.append(f"| {a['id']} | {a['users']} | {'1-3 s' if a['kind'] == 'load' else 'none'} | {a['requests']} | "
                     f"{a['rps']} | {a['ok_rps']} | {a['median_ms']} | {a['p95_ms']} | {a['p99_ms']} | {a['max_ms']} | "
                     f"{a['errors']} ({a['error_pct']}%) |")
    lines += ["", "## Per endpoint", "",
              "| Test | Endpoint | Requests | Req/s | Median (ms) | p95 (ms) | p99 (ms) | Max (ms) | Errors |",
              "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for r in rows_csv:
        lines.append(f"| {r['test']} | {r['endpoint']} | {r['requests']} | {r['rps']} | {r['median_ms']} | "
                     f"{r['p95_ms']} | {r['p99_ms']} | {r['max_ms']} | {r['errors']} ({r['error_pct']}%) |")

    vol = [t for t in meta["tests"] if t["kind"] == "volume"]
    if vol:
        lines += ["", "## PERF-07 data volume (1 user, 30 sequential requests each)", "",
                  "| Tasks per user | Endpoint | Median (ms) | p95 (ms) | Errors |", "|---:|---|---:|---:|---:|"]
        for t in vol:
            rows = [r for r in read_jtl(out / f"{t['id']}.jtl") if r["label"] != "POST /api/login"]
            by_label = {}
            for r in rows:
                by_label.setdefault(r["label"], []).append(r)
            for label, rs in by_label.items():
                s = stats(rs, 1)
                t.setdefault("by_label", {})[label] = s
                lines.append(f"| {t['tasks']} | {label} | {s['median_ms']} | {s['p95_ms']} | {s['errors']} |")

    for t in meta["tests"]:
        if t.get("errors"):
            lines += ["", f"### {t['id']} errors", "", "| Count | Sample: code and message |", "|---:|---|"]
            for k, v in sorted(t["errors"].items(), key=lambda kv: -kv[1]):
                lines.append(f"| {v} | {k} |")
    (out / "perf_summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    charts(out, agg, vol)


def charts(out, agg, vol):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed; charts skipped")
        return
    load = [a for a in agg if a["kind"] == "load"]
    u = [a["users"] for a in load]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    ax1.plot(u, [a["median_ms"] for a in load], marker="o", label="Median")
    ax1.plot(u, [a["p95_ms"] for a in load], marker="o", label="p95")
    ax1.set(xlabel="Concurrent virtual users", ylabel="Response time (ms)", title="Response time vs load (PERF-01 to 05)")
    ax1.grid(alpha=.3)
    ax1.legend()
    ax2.plot(u, [a["rps"] for a in load], marker="o", color="tab:green")
    ax2.set(xlabel="Concurrent virtual users", ylabel="Requests per second", title="Throughput vs load")
    ax2.grid(alpha=.3)
    fig.tight_layout()
    fig.savefig(out / "perf_load_chart.png", dpi=150)
    steps = [a for a in agg if a["kind"] == "stress-step"]
    if steps:
        u = [a["users"] for a in steps]
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
        ax1.plot(u, [a["ok_rps"] for a in steps], marker="o", color="tab:green")
        ax1.set(xscale="log", xlabel="Concurrent users, no think time (log scale)",
                ylabel="Successful requests per second", title="Stress: successful throughput (PERF-06 steps)")
        ax1.grid(alpha=.3)
        ax2.plot(u, [a["median_ms"] for a in steps], marker="o", label="Median")
        ax2.plot(u, [a["p95_ms"] for a in steps], marker="o", label="p95")
        ax2.set(xscale="log", xlabel="Concurrent users, no think time (log scale)", ylabel="Response time (ms)",
                title="Stress: response time (PERF-06 steps)")
        ax2.grid(alpha=.3)
        ax2.legend()
        fig.tight_layout()
        fig.savefig(out / "perf_stress_chart.png", dpi=150)
    if vol:
        fig, ax = plt.subplots(figsize=(6.5, 4))
        sizes = [t["tasks"] for t in vol]
        for label in vol[0]["by_label"]:
            ax.plot(sizes, [t["by_label"][label]["median_ms"] for t in vol], marker="o", label=label)
        ax.set(xlabel="Tasks owned by the user", ylabel="Median response time (ms)", title="PERF-07 data volume")
        ax.grid(alpha=.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(out / "perf_volume_chart.png", dpi=150)
    print("charts written")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--analyse", type=Path)
    ap.add_argument("--jmeter", default=shutil.which("jmeter") or "jmeter")
    ap.add_argument("--port", type=int, default=5015)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--stress-steps", action="store_true",
                    help="only run the stepped stress test and add it to --out's run.json")
    a = ap.parse_args()
    if a.analyse:
        analyse(a.analyse.resolve())
        return
    if a.stress_steps:
        out = (a.out or RESULTS / datetime.now().strftime("%Y%m%d-%H%M")).resolve()
        out.mkdir(parents=True, exist_ok=True)
        run_json = out / "run.json"
        meta = json.loads(run_json.read_text()) if run_json.exists() else \
            {"environment": environment(a.jmeter), "target": TARGET, "tests": []}
        meta["tests"] = [t for t in meta["tests"] if t["kind"] != "stress-step"]
        for users in STRESS_STEPS:
            sid = f"PERF-06_step_{users:03d}u"
            run_one(sid, LOAD_PLAN, {"users": users, "rampup": STEP_RAMP_S,
                                     "duration": STEP_RAMP_S + STEP_MEASURED_S,
                                     "think_min": 0, "think_range": 0}, out, a.port, a.jmeter)
            meta["tests"].append({"id": sid, "kind": "stress-step", "users": users,
                                  "rampup": STEP_RAMP_S, "measured_s": STEP_MEASURED_S})
            time.sleep(STEP_PAUSE_S)
        meta["environment"]["stress_steps_finished"] = datetime.now().astimezone().isoformat(timespec="seconds")
        run_json.write_text(json.dumps(meta, indent=2))
        analyse(out)
        return

    out = (a.out or RESULTS / datetime.now().strftime("%Y%m%d-%H%M")).resolve()
    out.mkdir(parents=True, exist_ok=True)
    steps = LOAD_STEPS[:2] if a.quick else LOAD_STEPS
    steady = 30 if a.quick else STEADY_S
    meta = {"environment": environment(a.jmeter), "target": TARGET, "tests": []}

    for test_id, users in steps:
        ramp = max(1, users // 5)
        run_one(test_id, LOAD_PLAN, {"users": users, "rampup": ramp, "duration": ramp + steady},
                out, a.port, a.jmeter)
        meta["tests"].append({"id": test_id, "kind": "load", "users": users, "rampup": ramp, "measured_s": steady})
        time.sleep(5)
    if not a.quick:
        test_id, users, secs = STRESS
        ramp = max(1, users // 5)
        run_one(test_id, LOAD_PLAN, {"users": users, "rampup": ramp, "duration": ramp + secs,
                                     "think_min": 0, "think_range": 0}, out, a.port, a.jmeter)
        meta["tests"].append({"id": test_id, "kind": "stress", "users": users, "rampup": ramp, "measured_s": secs})
        for n in VOLUME_SIZES:
            vid = f"PERF-07_{n}tasks"
            run_one(vid, VOLUME_PLAN, {"seed_tasks": n}, out, a.port, a.jmeter)
            meta["tests"].append({"id": vid, "kind": "volume", "tasks": n})
    meta["environment"]["finished"] = datetime.now().astimezone().isoformat(timespec="seconds")
    (out / "run.json").write_text(json.dumps(meta, indent=2))
    analyse(out)


if __name__ == "__main__":
    main()
