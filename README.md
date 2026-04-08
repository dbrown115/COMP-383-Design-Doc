# How to Run ANI Tools

The following sections show how to run the different ANI tools to compare different .fna files within 3 genomes: streptococcus, streptomyces, and mycobacterium. Scores with a 

---
## Tools
### ANIb and ANIm
To use ANIb and ANIm you would need to install conda. To install conda follow the instructions below: 
1) open up the terminal and run: bash Miniconda3-latest-Linux-x86_64.sh
2) It will prompt you if you want to initialize with conda init, select Yes (Y)
3) Once it is done installing you now have to create the pyANI environment
4) run the command conda create --name pyani_env
5) then run conda activate pyani_env in your terminal and you should see that you base changed to pyani_env
6) Then install the necessary channels that we need to run pyANI
7) run conda config --add channels defaults
8) run conda config --add channles bioconda
9) run conda config --add channels conda-forge
10) run conda install pyani - y

### OrthoANI

We have identified a bug affecting Mac Safari users. When downloading data from the NCBI Datasets web interface, you may see only this README file after the download has completed (while other files appear to be missing).
As a workaround to prevent this issue from recurring, we recommend disabling automatic zip archive extraction in Safari until Apple releases a bug fix.
For more information, visit:
https://www.ncbi.nlm.nih.gov/datasets/docs/reference-docs/mac-zip-bug/

# ANI Tools: FastANI + skani and Dashing 2

This repository contains scripts for computing Average Nucleotide Identity (ANI) across three organisms: *Mycobacterium tuberculosis*, *Streptococcus*, and *Streptomyces* using FastANI, skani, and Dashing 2.

---

## FastANI + skani

### Installation
Run the installation script to set up the `ani` conda environment with FastANI and skani:
```bash
bash Install_ANI.sh
source ~/.bashrc
```

`source ~/.bashrc` reloads your terminal configuration so that micromamba and the newly installed tools are recognized in your current session.

### Usage
Activate the environment and run the desired script:
```bash
micromamba activate ani
python Run_mtb.py
python Run_streptococcus.py
```

### Input
Each script expects a folder of `.fna` genome files. The script will automatically grab the first 3 genomes from the specified directory.

### Output
Results are saved to the specified output directory:
- `fastani_output.txt` — tab-separated file with columns: Genome1, Genome2, ANI, Fragments matched, Total fragments
- `skani_output.txt` — tab-separated file with columns: Ref_file, Query_file, ANI, Align_fraction_ref, Align_fraction_query

---

## Dashing 2

### Installation
Run the installation script inside your existing `ani` environment:
```bash
micromamba activate ani
bash Install_Dashing2.sh
```

### Usage
```bash
micromamba activate ani
python Run_mtb_dashing.py
python Run_streptococcus_dashing.py
python Run_streptomyces_dashing.py
```

### Input
Each script expects a folder of `.fna` genome files. The script will automatically grab the first 3 genomes from the specified directory.

### Output
Results are saved to the specified output directory as `dashing2_output.txt` — a symmetric pairwise similarity matrix where each value represents the Jaccard similarity between two genomes.

### MASH

Visit the NCBI Datasets documentation pages:
https://www.ncbi.nlm.nih.gov/datasets/docs/

### SourMASH 

---

National Center for Biotechnology Information
National Library of Medicine
info@ncbi.nlm.nih.gov
# COMP-383-Design-Doc
