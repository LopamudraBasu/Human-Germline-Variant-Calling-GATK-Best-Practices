#!/bin/bash

###############################################################################
# Project : Human Germline Variant Calling using GATK Best Practices
#
# Script  : 08_snpeff_annotation.sh
#
# Purpose :
# Annotate filtered germline variants using SnpEff to predict
# functional consequences on genes and transcripts.
#
# Input :
#   results/variants/NIST7035_filtered_variants.vcf.gz
#
# Database :
#   GRCh38.115
#
# Output :
#   results/annotation/NIST7035_annotated.vcf
#
# NOTE:
# Activate the SnpEff environment before running this script:
#
#   conda activate snpeff_env
#
###############################################################################

set -euo pipefail

echo "==============================================="
echo "Step 8 : Variant Annotation using SnpEff"
echo "==============================================="

mkdir -p results/annotation

snpEff \
-Xmx6g \
GRCh38.115 \
results/variants/NIST7035_filtered_variants.vcf.gz \
> results/annotation/NIST7035_annotated.vcf

echo ""
echo "Variant annotation completed successfully."
echo "Output:"
echo "  - results/annotation/NIST7035_annotated.vcf"
