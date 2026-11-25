"""Builds results/perf_chart.png (3 panels) from the CSV/MD results of the Week 5 run."""
import csv
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.size": 10, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.facecolor": SURF,
                     "figure.facecolor": SURF, "axes.spines.top": False, "axes.spines.right": False})

# 1) normal load steps
agg = [r for r in csv.DictReader(open("results/perf_summary.csv")) if r["endpoint"].startswith("ALL")]
users = [int(r["users"]) for r in agg]
med = [float(r["median_ms"]) for r in agg]
p95 = [float(r["p95_ms"]) for r in agg]

# 2) stress by endpoint
all_st = list(csv.DictReader(open("results/stress_50u_stats.csv")))
st_agg = next(r for r in all_st if r["Name"] == "Aggregated")
st_rps = float(st_agg["Requests/s"])
st_err = 100 * int(st_agg["Failure Count"]) / int(st_agg["Request Count"])
st = [r for r in all_st if r["Name"] not in ("Aggregated", "POST /api/login")]
st.sort(key=lambda r: float(r["95%"]))

# 3) data volume
scale = {}
for line in open("results/perf_scaling.md"):
    m = re.match(r"\| (\d+) \| (.+?) \| (\d+) \| (\d+) \|", line)
    if m:
        scale.setdefault(m.group(2), []).append((int(m.group(1)), float(m.group(3))))

fig, ax = plt.subplots(1, 3, figsize=(15, 4.6))

a = ax[0]
a.plot(users, p95, color=ORANGE, lw=2, marker="o", ms=8, label="p95")
a.plot(users, med, color=BLUE, lw=2, marker="o", ms=8, label="Median")
a.set_title("Normal load (1–3 s think time)", loc="left", color=INK, fontsize=11)
a.set_xlabel("Concurrent users"); a.set_ylabel("Response time (ms)")
a.set_ylim(0, 50); a.set_xlim(-1, 57); a.set_xticks(users); a.grid(axis="y", color=GRID)
a.text(users[-1] + 1.5, p95[-1], f"{p95[-1]:.0f} ms", color=INK2, va="center")
a.text(users[-1] + 1.5, med[-1], f"{med[-1]:.0f} ms", color=INK2, va="center")
a.legend(frameon=False, loc="upper left")
a.text(0.0, -0.22, "0% errors at every step", transform=a.transAxes, color=INK2)

b = ax[1]
names = [r["Name"].replace("/api/tasks/[id]", "/api/tasks/id") for r in st]
b.barh(names, [float(r["95%"]) for r in st], color=ORANGE, height=0.55, label="p95")
b.barh(names, [float(r["50%"]) for r in st], color=BLUE, height=0.55, label="Median")
for i, r in enumerate(st):
    b.text(float(r["95%"]) + 15, i, f'{float(r["95%"]):.0f}', va="center", color=INK2, fontsize=9)
b.set_title(f"Stress: 50 users, no think time (~{st_rps:.0f} req/s)", loc="left", color=INK, fontsize=11)
b.set_xlabel("Response time (ms)"); b.grid(axis="x", color=GRID)
b.legend(frameon=False, loc="lower right")
try:
    errs = " ".join(r["Error"] for r in csv.DictReader(open("results/stress_50u_failures.csv")))
except FileNotFoundError:
    errs = ""
cause = " (WinError 10048: load generator ran out of ports)" if "10048" in errs else ""
b.text(0.0, -0.22, f"{st_err:.1f}% failed{cause}" if st_err else "0% errors",
       transform=b.transAxes, color=INK2)

c = ax[2]
for (label, pts), col in zip(scale.items(), (BLUE, ORANGE, AQUA)):
    xs, ys = zip(*pts)
    c.plot(xs, ys, color=col, lw=2, marker="o", ms=8, label=label)
    c.text(xs[-1] + 40, ys[-1], f"{ys[-1]:.0f} ms", va="center", color=INK2)
c.set_title("Data volume: 1 user, median per request", loc="left", color=INK, fontsize=11)
c.set_xlabel("Tasks owned by the user"); c.set_ylabel("Median response time (ms)")
c.set_xticks([50, 500, 2000]); c.set_xlim(0, 2400); c.grid(axis="y", color=GRID)
c.legend(frameon=False, loc="upper left")

fig.tight_layout()
fig.savefig("results/perf_chart.png", dpi=150)
print("saved results/perf_chart.png")
