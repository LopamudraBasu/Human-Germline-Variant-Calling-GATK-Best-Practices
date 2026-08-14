#!/usr/bin/env python3

import csv
from pathlib import Path
import matplotlib.pyplot as plt

INPUT = Path("results/qc/qc_summary.csv")
OUTPUT = Path("figures/qc_summary.png")

data = {}

with open(INPUT, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data[row["Metric"]] = row

q20_before = float(data["Q20_Rate"]["Before_Filtering"]) * 100
q20_after = float(data["Q20_Rate"]["After_Filtering"]) * 100

q30_before = float(data["Q30_Rate"]["Before_Filtering"]) * 100
q30_after = float(data["Q30_Rate"]["After_Filtering"]) * 100

reads_before = int(data["Total_Reads"]["Before_Filtering"])
reads_after = int(data["Total_Reads"]["After_Filtering"])

retention = reads_after / reads_before * 100

fig, ax = plt.subplots(figsize=(7, 5))

metrics = ["Q20", "Q30"]
before = [q20_before, q30_before]
after = [q20_after, q30_after]

x = range(len(metrics))
width = 0.35

ax.bar([i - width/2 for i in x], before, width, label="Before filtering")
ax.bar([i + width/2 for i in x], after, width, label="After filtering")

ax.set_ylabel("Quality rate (%)")
ax.set_title("Read Quality Before and After Filtering")
ax.set_xticks(list(x))
ax.set_xticklabels(metrics)
ax.set_ylim(80, 100)
ax.legend()

for i, value in enumerate(before):
    ax.text(i - width/2, value + 0.2, f"{value:.2f}%",
            ha="center", va="bottom")

for i, value in enumerate(after):
    ax.text(i + width/2, value + 0.2, f"{value:.2f}%",
            ha="center", va="bottom")

fig.text(
    0.5,
    0.01,
    f"Read retention after filtering: {retention:.2f}% "
    f"({reads_after:,} / {reads_before:,} reads)",
    ha="center"
)

plt.tight_layout(rect=[0, 0.05, 1, 1])

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT, dpi=300, bbox_inches="tight")
plt.close()

print(f"QC figure written to: {OUTPUT}")
