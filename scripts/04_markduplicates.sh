#!/bin/bash

###############################################################################
# Project : Human Germline Variant Calling using GATK Best Practices
#
# Script  : 04_markduplicates.sh
#
# Purpose :
# Identify and mark PCR duplicates in the sorted BAM file using
# GATK MarkDuplicates.
#
# Input :
#   results/alignment/NIST7035_sorted.bam
#
# Output :
#   results/alignment/NIST7035_markdup.bam
#   results/alignment/marked_dup_metrics.txt
#
###############################################################################

set -euo pipefail

echo "==============================================="
echo "Step 4 : Marking PCR Duplicates"
echo "==============================================="

gatk MarkDuplicates \
-I results/alignment/NIST7035_sorted.bam \
-O results/alignment/NIST7035_markdup.bam \
-M results/alignment/marked_dup_metrics.txt

# Index the duplicate-marked BAM
samtools index results/alignment/NIST7035_markdup.bam

echo ""
echo "Duplicate marking completed successfully."
echo "Output:"
echo "  - results/alignment/NIST7035_markdup.bam"
echo "  - results/alignment/marked_dup_metrics.txt"
