"""
Reads results/step_<N>u_stats.csv from each load step and writes:
  results/perf_summary.csv      - one row per (users, endpoint): requests, RPS, median, p95, max, error %
  results/perf_summary.md       - same table in Markdown, paste into the report
  results/perf_steps_chart.png        - median and p95 response time vs users (overall)
"""
import csv
import glob
import re
import os

rows = []
for path in sorted(glob.glob("results/step_*u_stats.csv"),
                   key=lambda p: int(re.search(r"step_(\d+)u", p).group(1))):
    users = int(re.search(r"step_(\d+)u", path).group(1))
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            reqs = int(r["Request Count"])
            fails = int(r["Failure Count"])
            rows.append({
                "users": users,
                "endpoint": r["Name"] if r["Name"] != "Aggregated" else "ALL (aggregated)",
                "requests": reqs,
                "rps": round(float(r["Requests/s"]), 2),
                "median_ms": round(float(r["Median Response Time"])),
                "p95_ms": r.get("95%", ""),
                "max_ms": round(float(r["Max Response Time"])),
                "error_pct": round(100 * fails / reqs, 2) if reqs else 0,
            })

if not rows:
    raise SystemExit("No results/step_*u_stats.csv files found. Run run_load_steps first.")

os.makedirs("results", exist_ok=True)
keys = list(rows[0].keys())
with open("results/perf_summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keys)
    w.writeheader()
    w.writerows(rows)

with open("results/perf_summary.md", "w") as f:
    f.write("| Users | Endpoint | Requests | Req/s | Median (ms) | p95 (ms) | Max (ms) | Errors % |\n")
    f.write("|---|---|---|---|---|---|---|---|\n")
    for r in rows:
        f.write("| " + " | ".join(str(r[k]) for k in keys) + " |\n")
print(open("results/perf_summary.md").read())

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    agg = [r for r in rows if r["endpoint"] == "ALL (aggregated)"]
    u = [r["users"] for r in agg]
    fig, ax1 = plt.subplots(figsize=(7, 4))
    ax1.plot(u, [float(r["median_ms"]) for r in agg], marker="o", label="Median")
    ax1.plot(u, [float(r["p95_ms"] or 0) for r in agg], marker="o", label="p95")
    ax1.set_xlabel("Concurrent virtual users")
    ax1.set_ylabel("Response time (ms)")
    ax1.set_title("PyTodo Pro response time as load increases")
    ax1.grid(alpha=0.3)
    ax1.legend()
    fig.tight_layout()
    fig.savefig("results/perf_steps_chart.png", dpi=150)
    print("Chart saved: results/perf_steps_chart.png")
except ImportError:
    print("Install matplotlib for the chart:  pip install matplotlib")
