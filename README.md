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
- Variant-level quality control
- Functional annotation using SnpEff

The analysis was performed using a **Genome in a Bottle (GIAB) NIST7035 human sequencing sample**.

The project demonstrates practical experience with:

- Next Generation Sequencing (NGS) analysis
- Human germline variant calling
- GATK workflows
- Linux/Ubuntu WSL
- Bash scripting
- Python-based QC analysis
- Conda environment management
- SAM/BAM processing
- VCF processing
- Variant quality control
- Variant annotation
- Reproducible bioinformatics workflows

---

## 🎯 Objectives

The main objectives of this project were to:

1. Perform quality assessment of raw sequencing reads.
2. Remove adapters and low-quality reads/bases.
3. Align paired-end reads to the GRCh38 reference genome.
4. Process, sort, and index alignment files.
5. Mark PCR/optical duplicate reads.
6. Perform Base Quality Score Recalibration.
7. Call germline variants using GATK HaplotypeCaller.
8. Apply hard-filtering criteria to the variant callset.
9. Evaluate alignment and genome-wide coverage metrics.
10. Perform variant-level quality control.
11. Characterize SNPs, INDELs, Ti/Tv ratio, variant depth, and genotype quality.
12. Functionally annotate variants using SnpEff.
13. Organize the complete analysis into a reproducible workflow.

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
🧬 Reference Genome

The workflow uses the GRCh38 human reference genome.

Reference:

GCA_000001405.15_GRCh38_no_alt_analysis_set

The reference genome and its indexes are excluded from GitHub because of their large size.

Information about the reference resources is provided in:

data/reference/README.md
🔬 Pipeline Workflow

Workflow Steps
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
Variant QC
    │
    ▼
SnpEff
    │
    ▼
Annotated VCF
🛠 Software and Versions
Main Variant Calling Environment

The primary analysis was performed in the variant_calling Conda environment.

Software	Version
Java	17.0.18
GATK	4.6.2.0
Picard	3.4.0
SAMtools	1.24
FastQC	0.12.1
fastp	1.3.6
BWA-MEM	BWA
Python	3.11
Matplotlib	Conda environment
SnpEff Annotation Environment

SnpEff was maintained in a separate Conda environment because SnpEff 5.4c requires a newer Java runtime.

Software	Version
Java	21.0.10
SnpEff	5.4c
SnpEff Database	GRCh38.115

Environment specifications are provided in:

environment.yml
environment_snpeff.yml
📁 Repository Structure
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
│   ├── 09_qc_summary.py
│   ├── 10_qc_plot.py
│   ├── 11_alignment_qc.py
│   ├── 12_alignment_qc_plot.py
│   ├── 13_variant_qc.py
│   ├── 14_variant_qc_plot.py
│   └── run_pipeline.sh
│
├── results/
│   ├── fastqc/
│   ├── trimmed/
│   ├── alignment/
│   ├── variants/
│   ├── annotation/
│   └── qc/
│
├── figures/
│   ├── pipeline_workflow.svg
│   ├── qc_summary.png
│   ├── alignment_qc.png
│   └── variant_qc_summary.png
│
├── docs/
└── logs/

Large sequencing, reference, alignment, and annotation files are excluded through .gitignore.

🔬 Methods
1. Raw Read Quality Control

FastQC was used to assess the quality of the raw paired-end sequencing reads.

The resulting HTML and ZIP reports are retained under:

results/fastqc/

FastQC evaluated:

Per-base sequence quality
Per-tile sequence quality
Per-sequence quality scores
Per-base sequence composition
Per-sequence GC content
Per-base N content
Sequence length distribution
Sequence duplication
Adapter content
Overrepresented sequences
2. Adapter and Quality Trimming

fastp was used for adapter removal and quality filtering.

The workflow retains:

results/trimmed/fastp_report.html
results/trimmed/fastp_report.json

Additional FastQC reports were generated after trimming.

fastp Summary
Metric	Before Filtering	After Filtering
Total reads	40,406,004	38,192,282
Total bases	4,081,006,404	3,768,294,726
Q20 rate	95.95%	98.31%
Q30 rate	90.82%	93.74%
Mean read length	101 bp	98 bp
GC content	49.69%	49.36%

Filtering results:

Filtering category	Reads
Passed filtering	38,192,282
Low-quality reads	2,190,360
Too many N reads	23,362
Adapter-trimmed reads	4,590,044
Adapter-trimmed bases	91,152,918

The Q20 and Q30 rates increased after filtering, while the mean read length decreased from 101 bp to 98 bp.

The post-trimming FastQC reports showed that adapter content changed from WARN before trimming to PASS after trimming for both read pairs.

3. Read Alignment

Trimmed paired-end reads were aligned to the GRCh38 reference genome using BWA-MEM.

The alignment workflow follows:

FASTQ
  ↓
SAM
  ↓
BAM
  ↓
Coordinate-sorted BAM
  ↓
BAM index

Large SAM/BAM files are excluded from GitHub because of their size.

4. Duplicate Marking

Picard MarkDuplicates was used to identify and mark duplicate reads.

Duplicate metrics were retained as a quality-control output:

results/alignment/marked_dup_metrics.txt
5. Base Quality Score Recalibration

GATK BaseRecalibrator and ApplyBQSR were used to perform Base Quality Score Recalibration.

Known-sites resources included:

dbSNP138
Mills and 1000G Gold Standard Indels

The recalibration table is retained as:

results/alignment/recal_data.table
6. Germline Variant Calling

GATK HaplotypeCaller was used to identify germline variants from the recalibrated BAM file.

The resulting raw callset is:

results/variants/NIST7035_raw_variants.vcf.gz

with its tabix index:

results/variants/NIST7035_raw_variants.vcf.gz.tbi
7. Variant Filtering

Hard-filtering was applied using variant-level quality annotations.

The filtering criteria included:

QD < 2.0
FS > 60.0
MQ < 40.0

The filtered callset is:

results/variants/NIST7035_filtered_variants.vcf.gz

with its tabix index:

results/variants/NIST7035_filtered_variants.vcf.gz.tbi
8. Functional Annotation

The filtered variants were functionally annotated using SnpEff 5.4c with the:

GRCh38.115

database.

The annotation step predicts the potential functional effects of detected variants.

The large annotated VCF is excluded from GitHub because of its size.

📊 Quality Control Analysis
9. Sequencing Quality Control

FastQC and fastp outputs were further summarized using Python-based QC scripts.

The QC summary is available in:

results/qc/qc_summary.csv

and visualized in:

The corresponding scripts are:

scripts/09_qc_summary.py
scripts/10_qc_plot.py

The sequencing QC results demonstrate an improvement in Q20 and Q30 rates after filtering:

Q20: 95.95% → 98.31%
Q30: 90.82% → 93.74%
10. Alignment Quality Control

Alignment quality was evaluated using SAMtools and Picard MarkDuplicates.

The recalibrated BAM contained:

Metric	Result
Total reads	38,192,282
Mapped reads	38,191,043
Mapping rate	99.997%
Properly paired reads	37,985,850
Properly paired rate	99.46%
Duplicate reads	2,338,372
Duplicate rate	6.12%

The high mapping rate and properly paired rate indicate successful alignment of the retained reads to the reference genome.

Alignment statistics were generated using:

SAMtools stats
SAMtools coverage
SAMtools depth
SAMtools idxstats
Picard MarkDuplicates

The resulting outputs include:

results/alignment/NIST7035_recal_stats.txt
results/alignment/NIST7035_coverage.txt
results/alignment/alignment_summary.csv
results/alignment/marked_dup_metrics.txt

Alignment QC visualization:

Analysis scripts:

scripts/11_alignment_qc.py
scripts/12_alignment_qc_plot.py
11. Coverage Assessment

Coverage was evaluated across the primary chromosomes:

chr1–chr22
chrX
chrY

The primary chromosome reference length was:

3,088,269,832 bp

The calculated mean depth across these positions was approximately:

1.135×

The distribution of genomic positions by depth was:

Coverage	Genome Positions
0×	85.37%
1–4×	11.41%
5–9×	0.69%
10–19×	0.84%
20–29×	0.55%
≥30×	1.13%

Coverage thresholds:

Threshold	Positions
≥10×	2.52%
≥20×	1.69%
≥30×	1.13%

These results indicate that the analyzed dataset provides limited genome-wide coverage.

Therefore, the resulting variant callset should not be interpreted as a comprehensive high-confidence genome-wide germline callset.

The coverage output is retained in:

results/alignment/NIST7035_coverage.txt
12. Variant-Level Quality Control

Variant-level QC was performed using bcftools and custom Python scripts.

The raw callset contained:

283,102 variant records

After hard filtering:

271,726 PASS variants
11,376 filtered variants

The resulting PASS rate was:

95.98%

Variant QC outputs:

results/variants/NIST7035_variant_stats.txt
results/variants/variant_qc_summary.csv

Analysis scripts:

scripts/13_variant_qc.py
scripts/14_variant_qc_plot.py
PASS Variant Composition

The PASS callset contained:

Variant Type	Number	Percentage
SNPs	238,731	87.86%
INDELs	32,995	12.14%
Transition / Transversion Analysis

The PASS SNP callset showed:

Metric	Value
Transitions	143,432
Transversions	95,299
Ti/Tv ratio	1.505

The Ti/Tv ratio was calculated from PASS SNPs.

PASS Variant Depth

The mean PASS variant depth was:

11.83×

The distribution across depth categories was:

PASS Variant DP	Number
<10×	191,340
10–19×	30,007
20–29×	18,050
≥30×	32,329
PASS Genotype Quality

The mean PASS genotype quality was:

34.22

The genotype-quality summary was:

Metric	Number
PASS genotypes	271,726
GQ <20	163,859
GQ <30	173,482

The large number of low-depth and lower-GQ genotypes is consistent with the limited genome-wide coverage observed during alignment QC.

📈 Variant QC Visualization

The complete variant QC summary is shown below:

The figure summarizes:

PASS versus filtered variants
SNP versus INDEL composition
PASS variant depth categories
PASS genotype quality categories
📊 Results
Sequencing QC

The input dataset contained approximately 40.4 million reads before filtering.

After adapter and quality filtering:

38.19 million reads passed filtering.
Q20 increased from 95.95% to 98.31%.
Q30 increased from 90.82% to 93.74%.
Mean read length changed from 101 bp to 98 bp.
Adapter content changed from WARN to PASS in the post-trimming FastQC reports.
Alignment QC

The alignment results showed:

Metric	Result
Mapping rate	99.997%
Properly paired rate	99.46%
Duplicate rate	6.12%

These results demonstrate successful read alignment and relatively low duplication.

Coverage QC

The coverage analysis identified a major limitation of the dataset.

Across the primary chromosomes:

Coverage Threshold	Positions
≥10×	2.52%
≥20×	1.69%
≥30×	1.13%

Approximately 85.37% of primary-chromosome positions had zero coverage.

The mean depth across the primary chromosomes was approximately 1.14×.

Therefore, the variant callset should be interpreted primarily as a demonstration and evaluation of the germline variant-calling workflow, rather than as a complete high-confidence genome-wide variant set.

Variant Calling Summary

The variant calling workflow produced:

Metric	Number
Raw variant records	283,102
PASS variants	271,726
Filtered variants	11,376
PASS rate	95.98%

Filtering outcome:

283,102 total variant records
        │
        ├── 271,726 PASS (95.98%)
        │
        └── 11,376 filtered (4.02%)
PASS Variant Composition

The PASS variant callset consisted of:

Variant Type	Number	Percentage
SNP	238,731	87.86%
INDEL	32,995	12.14%

Ti/Tv:

1.505
Functional Annotation

Functional annotation was performed using:

SnpEff 5.4c

Database:

GRCh38.115

The annotation workflow produces predicted effects for detected variants, including their potential impact on genomic features and genes.

The large annotated VCF is excluded from GitHub because of its size.

⚠️ Data Quality Considerations and Limitations

This project demonstrates a complete reproducible germline variant-calling workflow, but the coverage characteristics of the analyzed dataset impose important limitations.

Major observations
Mapping rate: 99.997%
Properly paired reads: 99.46%
Duplicate rate: 6.12%
Mean primary-chromosome depth: 1.135×
Primary-chromosome positions at 0×: 85.37%
Positions reaching ≥10×: 2.52%
Positions reaching ≥20×: 1.69%
Positions reaching ≥30×: 1.13%

The high mapping rate demonstrates that the reads align efficiently to the reference genome. However, the low genome-wide coverage substantially limits sensitivity for germline variant detection, particularly for heterozygous variants and poorly covered genomic regions.

Therefore:

The project demonstrates the implementation, QC, and interpretation of a GATK germline variant-calling workflow rather than claiming comprehensive high-confidence genome-wide variant discovery from this dataset.

This distinction is important when evaluating the final VCF.

🔁 Reproducibility

The analysis was organized into modular Bash and Python scripts.

The main workflow can be executed using:

bash scripts/run_pipeline.sh

The QC and reporting scripts can be executed separately after the main pipeline:

python3 scripts/09_qc_summary.py
python3 scripts/10_qc_plot.py
python3 scripts/11_alignment_qc.py
python3 scripts/12_alignment_qc_plot.py
python3 scripts/13_variant_qc.py
python3 scripts/14_variant_qc_plot.py

The Conda environments required for the workflow are provided as:

environment.yml
environment_snpeff.yml
💻 Skills Demonstrated
Bioinformatics
Next Generation Sequencing (NGS)
Human germline variant calling
GRCh38 reference genome analysis
Variant quality control
VCF analysis
SNP and INDEL analysis
Functional variant annotation
GATK / Variant Calling
GATK HaplotypeCaller
BaseRecalibrator
ApplyBQSR
Base Quality Score Recalibration
VariantFiltration
Germline variant analysis
Sequence and Alignment QC
FastQC
fastp
BWA-MEM
SAMtools
Picard
Alignment QC
Coverage analysis
Duplicate analysis
Mapping statistics
Read-depth analysis
Variant QC
bcftools
SNP / INDEL classification
Transition / transversion analysis
Ti/Tv calculation
Variant depth analysis
Genotype quality analysis
PASS / filtered variant assessment
Programming and Workflow
Linux / Ubuntu WSL
Bash scripting
Python
Matplotlib
Conda environment management
Git
GitHub
Reproducible bioinformatics workflows
Functional Annotation
SnpEff
GRCh38.115 annotation database
📚 References

This workflow follows concepts and recommendations from the GATK Best Practices framework.

Please consult the official documentation and associated publications for each software package when using or extending this workflow.

Key tools include:

GATK
BWA
SAMtools
FastQC
fastp
Picard
SnpEff
👩‍🔬 Author

Lopamudra Basu

M.Sc. Biotechnology

Bioinformatics | Genomics | Transcriptomics | NGS Analysis
