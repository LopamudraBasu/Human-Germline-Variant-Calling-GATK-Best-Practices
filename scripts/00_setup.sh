#!/bin/bash

###############################################################################
# Project : Human Germline Variant Calling using GATK Best Practices
#
# Script  : 00_setup.sh
#
# Purpose :
# Check availability and versions of software required for the
# germline variant-calling workflow.
#
# Main environment:
#   variant_calling
#   Java 17
#
# Annotation environment:
#   snpeff_env
#   Java 21
###############################################################################

set -u

echo "====================================================="
echo "Human Germline Variant Calling Pipeline"
echo "Software Environment Check"
echo "====================================================="

echo ""
echo "Current Conda environment:"
echo "${CONDA_DEFAULT_ENV:-Not activated}"

echo ""
echo "-----------------------------------------------------"
echo "Main GATK Pipeline Tools"
echo "-----------------------------------------------------"

check_command() {
    local program="$1"

    if command -v "$program" >/dev/null 2>&1; then
        echo "✓ $program found: $(command -v "$program")"
    else
        echo "✗ $program NOT FOUND"
    fi
}

check_command fastqc
check_command fastp
check_command bwa
check_command samtools
check_command gatk

echo ""
echo "Java version:"
java -version 2>&1 | head -1

echo ""
echo "GATK version:"
if command -v gatk >/dev/null 2>&1; then
    gatk --version | tail -1
else
    echo "GATK not available"
fi

echo ""
echo "SAMtools version:"
if command -v samtools >/dev/null 2>&1; then
    samtools --version | head -1
else
    echo "SAMtools not available"
fi

echo ""
echo "BWA version:"
if command -v bwa >/dev/null 2>&1; then
    bwa 2>&1 | head -2
else
    echo "BWA not available"
fi

echo ""
echo "FastQC version:"
if command -v fastqc >/dev/null 2>&1; then
    fastqc --version
else
    echo "FastQC not available"
fi

echo ""
echo "fastp version:"
if command -v fastp >/dev/null 2>&1; then
    fastp --version
else
    echo "fastp not available"
fi

echo ""
echo "-----------------------------------------------------"
echo "SnpEff Annotation Environment"
echo "-----------------------------------------------------"

echo "SnpEff is maintained in the separate 'snpeff_env' environment."
echo ""
echo "To check SnpEff:"
echo ""
echo "    conda activate snpeff_env"
echo "    snpEff -version"
echo ""
echo "Expected:"
echo "    Java 21"
echo "    SnpEff 5.4c"

echo ""
echo "====================================================="
echo "Environment check completed."
echo "====================================================="
