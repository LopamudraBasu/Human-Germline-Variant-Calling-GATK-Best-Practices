#!/bin/bash

###############################################################################
# Project : Human Germline Variant Calling using GATK Best Practices
#
# Script  : 06_haplotypecaller.sh
#
# Purpose :
# Call germline variants from the recalibrated BAM file using
# GATK HaplotypeCaller.
#
# Input :
#   results/alignment/NIST7035_recal.bam
#
# Reference :
#   data/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna
#
# Output :
#   results/variants/NIST7035_raw_variants.vcf.gz
#
###############################################################################

set -euo pipefail

echo "==============================================="
echo "Step 6 : Germline Variant Calling"
echo "==============================================="

mkdir -p results/variants

gatk HaplotypeCaller \
-R data/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna \
-I results/alignment/NIST7035_recal.bam \
-O results/variants/NIST7035_raw_variants.vcf.gz

echo ""
echo "Variant calling completed successfully."
echo "Output:"
echo "  - results/variants/NIST7035_raw_variants.vcf.gz"

