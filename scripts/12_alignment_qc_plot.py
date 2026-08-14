import csv
import matplotlib.pyplot as plt

INPUT = "results/alignment/alignment_summary.csv"
OUTPUT = "figures/alignment_qc.png"

data = {}

with open(INPUT, newline="") as f:
    reader = csv.reader(f)
    next(reader)  # header

    for metric, value in reader:
        data[metric] = float(value)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# -------------------------
# Alignment metrics
# -------------------------

labels = [
    "Mapping\nrate",
    "Properly\npaired",
    "Duplicate\nrate"
]

values = [
    data["Mapping rate (%)"],
    data["Properly paired rate (%)"],
    data["Duplicate rate (%)"]
]

axes[0].bar(labels, values)
axes[0].set_ylabel("Percentage (%)")
axes[0].set_title("Alignment QC")
axes[0].set_ylim(0, 105)

for i, value in enumerate(values):
    axes[0].text(i, value + 2, f"{value:.2f}%", ha="center")

# -------------------------
# Coverage distribution
# -------------------------

coverage_labels = [
    "0X",
    "1–4X",
    "5–9X",
    "10–19X",
    "20–29X",
    "≥30X"
]

coverage_keys = [
    "Positions 0X (%)",
    "Positions 1-4X (%)",
    "Positions 5-9X (%)",
    "Positions 10-19X (%)",
    "Positions 20-29X (%)",
    "Positions >=30X (%)"
]

coverage_values = [data[x] for x in coverage_keys]

axes[1].bar(coverage_labels, coverage_values)
axes[1].set_ylabel("Genome positions (%)")
axes[1].set_title("Primary Chromosome Coverage")
axes[1].tick_params(axis="x", rotation=45)

for i, value in enumerate(coverage_values):
    axes[1].text(i, value + 1, f"{value:.2f}%", ha="center", fontsize=8)

plt.suptitle(
    "NIST7035 Germline Variant Calling — Alignment & Coverage QC",
    fontsize=14
)

plt.tight_layout()

plt.savefig(
    OUTPUT,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(f"Created: {OUTPUT}")
