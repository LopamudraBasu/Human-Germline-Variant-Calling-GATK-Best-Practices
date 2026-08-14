# 🧬 Human Germline Variant Calling using GATK

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?logo=ubuntu)
![GATK](https://img.shields.io/badge/GATK-4.6.2.0-blue)
![SAMtools](https://img.shields.io/badge/SAMtools-1.24-orange)
![FastQC](https://img.shields.io/badge/FastQC-0.12.1-green)
![fastp](https://img.shields.io/badge/fastp-1.3.6-brightgreen)
![SnpEff](https://img.shields.io/badge/SnpEff-5.4c-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Project Overview

This project implements a reproducible **single-sample human germline variant-calling workflow** using key steps from the **GATK Best Practices** framework.

Starting from paired-end Illumina FASTQ files, the workflow performs:

- Raw read quality control
- Adapter and quality trimming
- Read alignment to the GRCh38 reference genome
- SAM/BAM processing
- Duplicate marking
- Base Quality Score Recalibration (BQSR)
- Germline variant calling using GATK HaplotypeCaller
- Variant hard filtering
- Functional annotation using SnpEff

The analysis was performed using a **Genome in a Bottle (GIAB) NIST7035 human sequencing sample**.

The project demonstrates practical experience with:

- Next Generation Sequencing (NGS) analysis
- Germline variant calling
- GATK workflows
- Linux/Ubuntu WSL
- Bash scripting
- Conda environment management
- VCF processing
- Variant annotation
- Reproducible bioinformatics workflows

---

## 🎯 Objectives

The main objectives of this project were to:

1. Perform quality assessment of raw sequencing reads.
2. Remove adapters and low-quality bases.
3. Align paired-end reads to the GRCh38 reference genome.
4. Process and index alignment files.
5. Mark PCR/optical duplicate reads.
6. Perform Base Quality Score Recalibration.
7. Call germline variants using GATK HaplotypeCaller.
8. Apply hard-filtering criteria to the variant callset.
9. Functionally annotate variants using SnpEff.
10. Organize the complete analysis into a reproducible Bash-based workflow.

---

## 🧬 Dataset

### Sample

**NIST7035**

### Source

**Genome in a Bottle (GIAB)**

### Sequencing

**Paired-end Illumina sequencing**

The original FASTQ files are not included in the GitHub repository because of their large size.

Information about the expected input files is provided in:

```text
data/raw/README.md
````

---

## 🧬 Reference Genome

The workflow uses the **GRCh38** human reference genome.

Reference:

```text
GCA_000001405.15_GRCh38_no_alt_analysis_set
```

The reference genome and its indexes are excluded from GitHub because of their large size.

Information about the reference resources is provided in:

```text
data/reference/README.md
```

---

## 🔬 Pipeline Workflow

![Human germline variant calling workflow](figures/pipeline_workflow.svg)

### Workflow Steps

```text
Raw FASTQ
    │
    ▼
FastQC
    │
    ▼
fastp
    │
    ▼
BWA-MEM Alignment
    │
    ▼
SAM → BAM → Sorted BAM
    │
    ▼
MarkDuplicates
    │
    ▼
Base Quality Score Recalibration
    │
    ▼
GATK HaplotypeCaller
    │
    ▼
Raw VCF
    │
    ▼
VariantFiltration
    │
    ▼
Filtered VCF
    │
    ▼
SnpEff
    │
    ▼
Annotated VCF
```

---

## 🛠 Software and Versions

### Main Variant Calling Environment

The primary analysis was performed in the `variant_calling` Conda environment.

| Software | Version |
| -------- | ------: |
| Java     | 17.0.18 |
| GATK     | 4.6.2.0 |
| Picard   |   3.4.0 |
| SAMtools |    1.24 |
| FastQC   |  0.12.1 |
| fastp    |   1.3.6 |
| BWA-MEM  |     BWA |
| Python   |    3.11 |

### SnpEff Annotation Environment

SnpEff was maintained in a separate Conda environment because SnpEff 5.4c requires a newer Java runtime.

| Software        |    Version |
| --------------- | ---------: |
| Java            |    21.0.10 |
| SnpEff          |       5.4c |
| SnpEff Database | GRCh38.115 |

Environment specifications are provided in:

```text
environment.yml
environment_snpeff.yml
```

---

## 📁 Repository Structure

```text
Human-Germline-Variant-Calling-GATK-Best-Practices/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── environment.yml
├── environment_snpeff.yml
│
├── data/
│   ├── raw/
│   │   └── README.md
│   │
│   ├── reference/
│   │   └── README.md
│   │
│   └── known_sites/
│       └── README.md
│
├── scripts/
│   ├── 00_setup.sh
│   ├── 01_fastqc.sh
│   ├── 02_fastp.sh
│   ├── 03_bwa_alignment.sh
│   ├── 04_markduplicates.sh
│   ├── 05_bqsr.sh
│   ├── 06_haplotypecaller.sh
│   ├── 07_variantfiltration.sh
│   ├── 08_snpeff_annotation.sh
│   └── run_pipeline.sh
│
├── results/
│   ├── fastqc/
│   ├── trimmed/
│   ├── alignment/
│   ├── variants/
│   └── annotation/
│
├── figures/
│   └── pipeline_workflow.svg
│
├── docs/
└── logs/
```

Large sequencing, reference, alignment, and annotation files are excluded through `.gitignore`.

---

## 🔬 Methods

### 1. Raw Read Quality Control

**FastQC** was used to assess the quality of the raw paired-end sequencing reads.

The resulting HTML and ZIP reports are retained under:

```text
results/fastqc/
```

### 2. Adapter and Quality Trimming

**fastp** was used for adapter removal and quality trimming.

The workflow retains:

```text
results/trimmed/fastp_report.html
results/trimmed/fastp_report.json
```

Additional FastQC reports were generated after trimming.

### 3. Read Alignment

Trimmed paired-end reads were aligned to the GRCh38 reference genome using **BWA-MEM**.

The alignment workflow follows:

```text
FASTQ
  ↓
SAM
  ↓
BAM
  ↓
Coordinate-sorted BAM
  ↓
BAM index
```

Large SAM/BAM files are excluded from GitHub because of their size.

### 4. Duplicate Marking

**Picard MarkDuplicates** was used to identify and mark duplicate reads.

Duplicate metrics were retained as a quality-control output:

```text
results/alignment/marked_dup_metrics.txt
```

### 5. Base Quality Score Recalibration

GATK **BaseRecalibrator** and **ApplyBQSR** were used to perform Base Quality Score Recalibration.

Known-sites resources included:

* dbSNP138
* Mills and 1000G Gold Standard Indels

The recalibration table is retained as:

```text
results/alignment/recal_data.table
```

### 6. Germline Variant Calling

**GATK HaplotypeCaller** was used to identify germline variants from the recalibrated BAM file.

The resulting raw callset is:

```text
results/variants/NIST7035_raw_variants.vcf.gz
```

with its tabix index:

```text
results/variants/NIST7035_raw_variants.vcf.gz.tbi
```

### 7. Variant Filtering

Hard-filtering was applied using variant-level quality annotations.

The filtering criteria included:

```text
QD < 2.0
FS > 60.0
MQ < 40.0
```

The filtered callset is:

```text
results/variants/NIST7035_filtered_variants.vcf.gz
```

with its tabix index:

```text
results/variants/NIST7035_filtered_variants.vcf.gz.tbi
```

### 8. Functional Annotation

The filtered variants were functionally annotated using **SnpEff 5.4c** with the:

```text
GRCh38.115
```

database.

The annotation step predicts the potential functional effects of detected variants.

The large annotated VCF is excluded from GitHub because of its size.

---

## 📊 Results

### Variant Calling Summary

| Metric            |  Number |
| ----------------- | ------: |
| Raw variants      | 283,102 |
| PASS variants     | 271,726 |
| Filtered variants |  11,376 |

### Filtering Outcome

```text
Raw variants
     │
     ├── PASS variants       271,726
     │
     └── Filtered variants    11,376
```

The compressed raw and filtered VCF files and their tabix indexes are retained in:

```text
results/variants/
```

---

## 📈 Functional Annotation

Functional annotation was performed using:

**SnpEff 5.4c**

Database:

```text
GRCh38.115
```

The annotation workflow produces predicted effects for the detected variants, including their potential impact on genomic features and genes.

---

## 💻 Skills Demonstrated

* Next Generation Sequencing (NGS)
* Human germline variant calling
* Linux / Ubuntu WSL
* Bash scripting
* Conda environment management
* FastQC
* fastp
* BWA-MEM
* SAMtools
* Picard
* GATK
* HaplotypeCaller
* Base Quality Score Recalibration
* VariantFiltration
* VCF processing
* SnpEff
* GRCh38 genome analysis
* Reproducible bioinformatics workflows
* Git and GitHub

---

## 🚀 Reproducibility

### 1. Create the Main Conda Environment

```bash
conda env create -f environment.yml
```

Activate it:

```bash
conda activate variant_calling
```

Check the installed tools:

```bash
./scripts/00_setup.sh
```

### 2. Run the Pipeline

The individual pipeline steps are available under:

```text
scripts/
```

The complete workflow can be executed using:

```bash
./scripts/run_pipeline.sh
```

The scripts are numbered according to the analysis workflow:

```text
00_setup.sh
01_fastqc.sh
02_fastp.sh
03_bwa_alignment.sh
04_markduplicates.sh
05_bqsr.sh
06_haplotypecaller.sh
07_variantfiltration.sh
08_snpeff_annotation.sh
```

### 3. Create the SnpEff Environment

```bash
conda env create -f environment_snpeff.yml
```

Activate it:

```bash
conda activate snpeff_env
```

Verify SnpEff:

```bash
snpEff -version
```

Expected:

```text
SnpEff 5.4c
Java 21
```

---

## 📦 Data Availability

Large input and intermediate files are intentionally excluded from the GitHub repository, including:

* Raw FASTQ files
* GRCh38 reference genome
* Reference genome indexes
* Known-sites VCF resources
* Large SAM/BAM files
* Trimmed FASTQ files
* Large annotated VCF files

The corresponding `data/` README files describe the required resources.

---

## 🔮 Future Improvements

Potential extensions of this project include:

* Variant Quality Score Recalibration (VQSR)
* Multi-sample joint genotyping
* Variant Effect Predictor (VEP)
* ANNOVAR annotation
* Structural variant calling
* Additional variant quality-control visualizations
* Automated workflow management using Nextflow or Snakemake
* Containerization using Docker or Apptainer

---

## 📚 Software

This project uses the following open-source bioinformatics software:

* GATK
* BWA
* SAMtools
* FastQC
* fastp
* Picard
* SnpEff

Please consult the official documentation and associated publications for each software package when using or extending this workflow.

---

## 👩‍💻 Author

**Lopamudra Basu**

M.Sc. Biotechnology

**Bioinformatics | Genomics | Transcriptomics | NGS Analysis**

---
