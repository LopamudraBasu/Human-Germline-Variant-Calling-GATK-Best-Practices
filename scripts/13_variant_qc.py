#!/usr/bin/env python3

import csv
import subprocess
from pathlib import Path

VCF = Path("results/variants/NIST7035_filtered_variants.vcf.gz")
OUT = Path("results/variants/variant_qc_summary.csv")


def run_bcftools_query(format_string, filter_pass=False):
    cmd = ["bcftools", "query"]

    if filter_pass:
        cmd += ["-i", 'FILTER="PASS"']

    cmd += ["-f", format_string, str(VCF)]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True
    )

    return result.stdout.strip().splitlines()


# ---------------------------------------------------------
# Variant counts
# ---------------------------------------------------------

total_records = int(
    subprocess.check_output(
        ["bcftools", "view", "-H", str(VCF)]
    ).decode().count("\n")
)

pass_filters = run_bcftools_query("%FILTER\n")

pass_count = sum(1 for x in pass_filters if x == "PASS")
filtered_count = total_records - pass_count


# ---------------------------------------------------------
# PASS SNP / INDEL counts
# ---------------------------------------------------------

variants = run_bcftools_query("%REF\t%ALT\n", filter_pass=True)

pass_snps = 0
pass_indels = 0

for line in variants:
    ref, alt = line.split("\t")

    if len(ref) == 1 and len(alt) == 1:
        pass_snps += 1
    else:
        pass_indels += 1


# ---------------------------------------------------------
# Ti/Tv
# ---------------------------------------------------------

transitions = 0
transversions = 0

for line in variants:
    ref, alt = line.split("\t")

    if len(ref) == 1 and len(alt) == 1:

        if (
            (ref == "A" and alt == "G")
            or (ref == "G" and alt == "A")
            or (ref == "C" and alt == "T")
            or (ref == "T" and alt == "C")
        ):
            transitions += 1
        else:
            transversions += 1

ti_tv = transitions / transversions if transversions else 0


# ---------------------------------------------------------
# PASS GQ
# ---------------------------------------------------------

gq_values = [
    float(x)
    for x in run_bcftools_query("[%GQ\n]", filter_pass=True)
    if x not in ("", ".")
]

mean_gq = sum(gq_values) / len(gq_values)

gq_lt20 = sum(x < 20 for x in gq_values)
gq_lt30 = sum(x < 30 for x in gq_values)


# ---------------------------------------------------------
# PASS variant DP
# ---------------------------------------------------------

dp_values = [
    float(x)
    for x in run_bcftools_query("%DP\n", filter_pass=True)
    if x not in ("", ".")
]

mean_dp = sum(dp_values) / len(dp_values)

dp_lt10 = sum(x < 10 for x in dp_values)
dp_10_19 = sum(10 <= x < 20 for x in dp_values)
dp_20_29 = sum(20 <= x < 30 for x in dp_values)
dp_ge30 = sum(x >= 30 for x in dp_values)


# ---------------------------------------------------------
# Write summary
# ---------------------------------------------------------

OUT.parent.mkdir(parents=True, exist_ok=True)

rows = [
    ("Total variant records", total_records),
    ("PASS variants", pass_count),
    ("Filtered variants", filtered_count),
    ("PASS rate (%)", round(pass_count / total_records * 100, 2)),
    ("PASS SNPs", pass_snps),
    ("PASS INDELs", pass_indels),
    ("Transitions", transitions),
    ("Transversions", transversions),
    ("Ti/Tv ratio", round(ti_tv, 3)),
    ("PASS genotypes", len(gq_values)),
    ("Mean PASS GQ", round(mean_gq, 2)),
    ("PASS GQ <20", gq_lt20),
    ("PASS GQ <30", gq_lt30),
    ("Mean PASS variant DP", round(mean_dp, 2)),
    ("PASS DP <10", dp_lt10),
    ("PASS DP 10-19", dp_10_19),
    ("PASS DP 20-29", dp_20_29),
    ("PASS DP >=30", dp_ge30),
]

with open(OUT, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Metric", "Value"])
    writer.writerows(rows)


print(f"Variant QC summary written to: {OUT}")
