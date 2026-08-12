#!/bin/bash

###############################################################################
# Project : Human Germline Variant Calling using GATK Best Practices
#
# Script  : 05_bqsr.sh
#
# Purpose :
# Perform Base Quality Score Recalibration (BQSR) using GATK.
# First, generate a recalibration table using known variant sites.
# Then apply the recalibration to produce the final analysis-ready BAM.
#
# Input :
#   results/alignment/NIST7035_markdup.bam
#
# Reference :
#   data/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna
#
# Known Sites :
#   data/known_sites/Homo_sapiens_assembly38.dbsnp138.vcf
#   data/known_sites/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz
#
# Output :
#   results/alignment/recal_data.table
#   results/alignment/NIST7035_recal.bam
#   results/alignment/NIST7035_recal.bai
#
###############################################################################

set -euo pipefail

echo "==============================================="
echo "Step 5 : Base Quality Score Recalibration (BQSR)"
echo "==============================================="

# Generate recalibration table
gatk BaseRecalibrator \
-R data/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna \
-I results/alignment/NIST7035_markdup.bam \
--known-sites data/known_sites/Homo_sapiens_assembly38.dbsnp138.vcf \
--known-sites data/known_sites/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz \
-O results/alignment/recal_data.table

# Apply recalibration
gatk ApplyBQSR \
-R data/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna \
-I results/alignment/NIST7035_markdup.bam \
--bqsr-recal-file results/alignment/recal_data.table \
-O results/alignment/NIST7035_recal.bam

# Index recalibrated BAM
samtools index results/alignment/NIST7035_recal.bam

echo ""
echo "BQSR completed successfully."
echo "Output:"
echo "  - results/alignment/recal_data.table"
echo "  - results/alignment/NIST7035_recal.bam"
