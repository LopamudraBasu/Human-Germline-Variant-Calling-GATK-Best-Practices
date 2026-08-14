#!/usr/bin/env python3

import json
import csv
from pathlib import Path

INPUT = Path("results/trimmed/fastp_report.json")
OUTPUT_DIR = Path("results/qc")
OUTPUT = OUTPUT_DIR / "qc_summary.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

with open(INPUT) as f:
    data = json.load(f)

before = data["summary"]["before_filtering"]
after = data["summary"]["after_filtering"]
filtering = data["filtering_result"]
adapter = data["adapter_cutting"]

rows = [
    ["Metric", "Before_Filtering", "After_Filtering"],
    ["Total_Reads", before["total_reads"], after["total_reads"]],
    ["Total_Bases", before["total_bases"], after["total_bases"]],
    ["Q20_Rate", before["q20_rate"], after["q20_rate"]],
    ["Q30_Rate", before["q30_rate"], after["q30_rate"]],
    ["Mean_Read_Length", before["read1_mean_length"], after["read1_mean_length"]],
    ["GC_Content", before["gc_content"], after["gc_content"]],
    ["Passed_Filter_Reads", "", filtering["passed_filter_reads"]],
    ["Low_Quality_Reads", "", filtering["low_quality_reads"]],
    ["Too_Many_N_Reads", "", filtering["too_many_N_reads"]],
    ["Adapter_Trimmed_Reads", "", adapter["adapter_trimmed_reads"]],
    ["Adapter_Trimmed_Bases", "", adapter["adapter_trimmed_bases"]],
]

with open(OUTPUT, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"QC summary written to: {OUTPUT}")
