#!/bin/bash

###############################################################################
# Project : Human Germline Variant Calling using GATK Best Practices
#
# Script  : 02_fastp.sh
#
# Purpose :
# Trim sequencing adapters and low-quality bases using fastp.
#
# Input :
# data/raw/NIST7035_TAAGGCGA_L001_R1_001.fastq.gz
# data/raw/NIST7035_TAAGGCGA_L001_R2_001.fastq.gz
#
# Output :
# results/trimmed/
#
###############################################################################

set -euo pipefail

echo "==============================================="
echo "Running fastp..."
echo "==============================================="

mkdir -p results/trimmed

fastp \
-i data/raw/NIST7035_TAAGGCGA_L001_R1_001.fastq.gz \
-I data/raw/NIST7035_TAAGGCGA_L001_R2_001.fastq.gz \
-o results/trimmed/NIST7035_R1_trimmed.fastq.gz \
-O results/trimmed/NIST7035_R2_trimmed.fastq.gz \
-h results/trimmed/fastp_report.html \
-j results/trimmed/fastp_report.json \
--thread 4

echo ""
echo "fastp completed successfully."
echo "Trimmed FASTQ files saved in results/trimmed/"
