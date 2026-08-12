#!/bin/bash

###############################################################################
# Human Germline Variant Calling using GATK Best Practices
#
# Master Pipeline Script
###############################################################################

set -euo pipefail

echo "=========================================="
echo "Starting Human Germline Variant Calling Pipeline"
echo "=========================================="

bash scripts/01_fastqc.sh
bash scripts/02_fastp.sh
bash scripts/03_bwa_alignment.sh
bash scripts/04_markduplicates.sh
bash scripts/05_bqsr.sh
bash scripts/06_haplotypecaller.sh
bash scripts/07_variantfiltration.sh

echo ""
echo "====================================================="
echo "Activate the SnpEff environment before annotation:"
echo ""
echo "conda activate snpeff_env"
echo ""
echo "Then run:"
echo ""
echo "bash scripts/08_snpeff_annotation.sh"
echo "====================================================="
