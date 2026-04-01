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

### FastANI

Visit our JSON Lines data report documentation page:
https://www.ncbi.nlm.nih.gov/datasets/docs/v2/tutorials/working-with-jsonl-data-reports/

### SkANI

NCBI Datasets is a resource that lets you easily gather data from across NCBI databases. Find and download gene, transcript, protein and genome sequences, annotation and metadata.

### MASH

Visit the NCBI Datasets documentation pages:
https://www.ncbi.nlm.nih.gov/datasets/docs/

### SourMASH 

### Dashing 2
---

National Center for Biotechnology Information
National Library of Medicine
info@ncbi.nlm.nih.gov
# COMP-383-Design-Doc
