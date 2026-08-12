#!/bin/bash

###############################################################################
# Project : Human Germline Variant Calling using GATK Best Practices
#
# Script  : 01_fastqc.sh
#
# Purpose :
# Perform quality assessment of raw paired-end sequencing reads using FastQC.
#
# Input :
# data/raw/NIST7035_TAAGGCGA_L001_R1_001.fastq.gz
# data/raw/NIST7035_TAAGGCGA_L001_R2_001.fastq.gz
#
# Output :
# results/fastqc/
#
###############################################################################

set -euo pipefail

echo "==============================================="
echo "Running FastQC on raw sequencing reads..."
echo "==============================================="

mkdir -p results/fastqc

fastqc \
data/raw/NIST7035_TAAGGCGA_L001_R1_001.fastq.gz \
data/raw/NIST7035_TAAGGCGA_L001_R2_001.fastq.gz \
--threads 4 \
--outdir results/fastqc

echo ""
echo "FastQC completed successfully."
echo "Results saved in results/fastqc/"
