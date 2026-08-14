#!/usr/bin/env python3

"""
NIST7035 Germline Variant Calling
Variant Quality Control Visualization

Input:
    results/variants/variant_qc_summary.csv

Output:
    figures/variant_qc_summary.png

The figure contains:
    1. Variant filtering summary
    2. PASS SNP vs INDEL composition
    3. PASS variant depth distribution
    4. PASS genotype quality distribution
"""

import csv
import os

import matplotlib.pyplot as plt


# ============================================================
# Paths
# ============================================================

INPUT_FILE = "results/variants/variant_qc_summary.csv"
OUTPUT_FILE = "figures/variant_qc_summary.png"


# ============================================================
# Read QC summary
# ============================================================

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(
        f"Input file not found: {INPUT_FILE}"
    )


qc = {}

with open(INPUT_FILE, "r") as f:
    reader = csv.reader(f)

    # Skip header
    next(reader)

    for row in reader:
        if len(row) >= 2:
            metric = row[0].strip()
            value = row[1].strip()
            qc[metric] = value


# ============================================================
# Extract values
# ============================================================

total_variants = int(qc["Total variant records"])
pass_variants = int(qc["PASS variants"])
filtered_variants = int(qc["Filtered variants"])

pass_rate = float(qc["PASS rate (%)"])

pass_snps = int(qc["PASS SNPs"])
pass_indels = int(qc["PASS INDELs"])

mean_pass_dp = float(qc["Mean PASS variant DP"])
mean_pass_gq = float(qc["Mean PASS GQ"])


# ============================================================
# Calculate percentages
# ============================================================

filtered_rate = 100 - pass_rate

snp_percentage = (pass_snps / pass_variants) * 100
indel_percentage = (pass_indels / pass_variants) * 100


# ============================================================
# Create output directory
# ============================================================

os.makedirs(
    os.path.dirname(OUTPUT_FILE),
    exist_ok=True
)


# ============================================================
# Figure setup
# ============================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 11)
)

fig.suptitle(
    "NIST7035 Germline Variant QC",
    fontsize=22,
    y=0.98
)


# ============================================================
# 1. Variant Filtering
# ============================================================

ax = axes[0, 0]

filter_labels = [
    "PASS",
    "Filtered"
]

filter_values = [
    pass_variants,
    filtered_variants
]

bars = ax.bar(
    filter_labels,
    filter_values
)

ax.set_title(
    "Variant Filtering",
    fontsize=16
)

ax.set_ylabel(
    "Number of variants",
    fontsize=12
)

ax.set_ylim(
    0,
    max(filter_values) * 1.18
)

for bar, value, percentage in zip(
    bars,
    filter_values,
    [pass_rate, filtered_rate]
):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + max(filter_values) * 0.015,
        f"{value:,}\n({percentage:.2f}%)",
        ha="center",
        va="bottom",
        fontsize=11
    )


# ============================================================
# 2. PASS Variant Composition
# ============================================================

ax = axes[0, 1]

composition_labels = [
    "SNP",
    "INDEL"
]

composition_values = [
    pass_snps,
    pass_indels
]

composition_percentages = [
    snp_percentage,
    indel_percentage
]

bars = ax.bar(
    composition_labels,
    composition_values
)

ax.set_title(
    "PASS Variant Composition",
    fontsize=16
)

ax.set_ylabel(
    "Number of variants",
    fontsize=12
)

ax.set_ylim(
    0,
    max(composition_values) * 1.20
)

for bar, value, percentage in zip(
    bars,
    composition_values,
    composition_percentages
):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + max(composition_values) * 0.015,
        f"{value:,}\n({percentage:.2f}%)",
        ha="center",
        va="bottom",
        fontsize=11
    )


# ============================================================
# 3. PASS Variant Depth
# ============================================================

ax = axes[1, 0]

# The summary CSV contains only binned depth counts.
# We reconstruct the distribution using the available
# depth categories.

dp_labels = [
    "<10",
    "10-19",
    "20-29",
    ">=30"
]

dp_values = [
    int(qc["PASS DP <10"]),
    int(qc["PASS DP 10-19"]),
    int(qc["PASS DP 20-29"]),
    int(qc["PASS DP >=30"])
]

# Use bin centers for visualization
dp_centers = [
    5,
    15,
    25,
    45
]

bars = ax.bar(
    dp_centers,
    dp_values,
    width=9
)

ax.set_title(
    "PASS Variant Depth",
    fontsize=16
)

ax.set_xlabel(
    "Depth (DP)",
    fontsize=12
)

ax.set_ylabel(
    "Number of variants",
    fontsize=12
)

ax.set_xticks(dp_centers)
ax.set_xticklabels(dp_labels)

ax.axvline(
    mean_pass_dp,
    linestyle="--",
    linewidth=1.5,
    label=f"Mean = {mean_pass_dp:.2f}×"
)

ax.legend(
    loc="upper right",
    fontsize=10
)


# ============================================================
# 4. PASS Genotype Quality
# ============================================================

ax = axes[1, 1]

# The summary CSV provides GQ thresholds rather than
# the complete GQ distribution.
#
# We therefore visualize:
#   GQ <20
#   GQ 20-29
#   GQ >=30

gq_low20 = int(qc["PASS GQ <20"])
gq_low30 = int(qc["PASS GQ <30"])

gq_20_29 = gq_low30 - gq_low20
gq_30_plus = pass_variants - gq_low30

gq_labels = [
    "<20",
    "20-29",
    ">=30"
]

gq_values = [
    gq_low20,
    gq_20_29,
    gq_30_plus
]

gq_centers = [
    10,
    25,
    50
]

bars = ax.bar(
    gq_centers,
    gq_values,
    width=10
)

ax.set_title(
    "PASS Genotype Quality",
    fontsize=16
)

ax.set_xlabel(
    "Genotype Quality (GQ)",
    fontsize=12
)

ax.set_ylabel(
    "Number of genotypes",
    fontsize=12
)

ax.set_xticks(gq_centers)
ax.set_xticklabels(gq_labels)

ax.axvline(
    mean_pass_gq,
    linestyle="--",
    linewidth=1.5,
    label=f"Mean = {mean_pass_gq:.2f}"
)

ax.legend(
    loc="upper right",
    fontsize=10
)


# ============================================================
# Layout
# ============================================================

plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)


# ============================================================
# Save figure
# ============================================================

plt.savefig(
    OUTPUT_FILE,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("Variant QC plot generated successfully.")
print(f"Input : {INPUT_FILE}")
print(f"Output: {OUTPUT_FILE}")
