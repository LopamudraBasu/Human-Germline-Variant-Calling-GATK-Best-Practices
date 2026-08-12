#!/bin/bash

###############################################################################
# Project : Human Germline Variant Calling using GATK Best Practices
#
# Script  : 03_bwa_alignment.sh
#
# Purpose :
# Align trimmed paired-end sequencing reads to the human reference genome
# (GRCh38) using BWA-MEM, then convert SAM to BAM, sort and index.
#
# Input :
#   results/trimmed/NIST7035_R1_trimmed.fastq.gz
#   results/trimmed/NIST7035_R2_trimmed.fastq.gz
#
# Reference :
#   data/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna
#
# Output :
#   results/alignment/NIST7035.sam
#   results/alignment/NIST7035.bam
#   results/alignment/NIST7035_sorted.bam
#   results/alignment/NIST7035_sorted.bam.bai
#
###############################################################################

set -euo pipefail

echo "==============================================="
echo "Step 3 : Read Alignment using BWA-MEM"
echo "==============================================="

mkdir -p results/alignment

# Align paired-end reads
bwa mem \
-t 4 \
data/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna \
results/trimmed/NIST7035_R1_trimmed.fastq.gz \
results/trimmed/NIST7035_R2_trimmed.fastq.gz \
> results/alignment/NIST7035.sam

# Convert SAM to BAM
samtools view \
-bS \
results/alignment/NIST7035.sam \
> results/alignment/NIST7035.bam

# Sort BAM
samtools sort \
-@ 4 \
-o results/alignment/NIST7035_sorted.bam \
results/alignment/NIST7035.bam

# Index BAM
samtools index \
results/alignment/NIST7035_sorted.bam

echo ""
echo "Alignment completed successfully."
echo "Sorted BAM saved in results/alignment/"
