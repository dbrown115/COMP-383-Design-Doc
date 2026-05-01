# How to Run ANI Tools

The following sections show how to run the different ANI tools to compare different .fna files within 3 genomes: streptococcus, streptomyces, and mycobacterium. Scores with a 
---

## Clone the Repo
To use the ANI tools in this repository, you will first need to download the genome files. Clone the full repository using the following command:

```bash
bash git clone https://github.com/dbrown115/COMP-383-Design-Doc.git
```

This will create a local copy of the repository. Navigate into it:
```bash
bash cd COMP-383-Design-Doc
```

The genome files are organized into three folders:
```bash
mtb_3genomes/
streptococcus_3genomes/
streptomyces_3genomes/
```
---
## Installation of micromamba for FastANI, skani, and Dashing2
```bash
cd ~

mkdir -p ~/bin

curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj -C ~ bin/micromamba

~/bin/micromamba shell init -s bash
```

## Installation of conda for ANIb, ANIm, SourMASH, MASH, and OrthoANI
To use these different tools, you will have to intsall miniconda onto your terminal. To install miniconda follow the instructions at this link: https://www.anaconda.com/docs/getting-started/miniconda/install/overview

After you have installed miniconda onto your mac, you should be ready to create your different environments.

### Activating the pyANI_env to run ANIb and ANIm
The environment you will need to run ANIb and ANIm is the pyani_env. Follow the insturctions below to activate this environment in your terminal. (Activation of these environments assumes that you have downloaded miniconda onto your terminal following the instructions from the link above)

```bash
conda create --name pyani_env
```

```bash
conda activate pyani_env
```

After activating your terminal you should see that your (base) has changed to (pyani_env) as seen below:

<img width="402" height="43" alt="Screen Shot 2026-05-01 at 9 09 01 AM" src="https://github.com/user-attachments/assets/9a296dab-c16a-4d26-8be5-d9322adfeada" />


It is necessary to activate three channels in the pyani_env to run the ANI tools. Follow the steps below: 

```bash
conda config --add channels conda-forge
conda config --add channels bioconda
conda config --add channels defaults
conda install pyani -y
```

Once you have added all your channels and installed pyani, you should be ready to test your ANIb and ANIm tools (refer to the section below labelled ANIb and ANIm)

To deactivate the environment run this command: 
```bash
conda deactivate
```

### Activating the sourmash_env to run sourMASH
The environment you will need to run sourMASH is sourmash_env. Follow the instructions below to activate this environment. (Activation of these environments assumes that you have downloaded miniconda onto your terminal following the instructions from the link above)

```bash
conda create -n sourmash_env -c conda-forge -c bioconda sourmash
```

```bash
conda activate sourmash_env
```

After activating the sourmash_env you should see that your (base) has changed to (sourmash_env) as seen below: 

<img width="380" height="33" alt="Screen Shot 2026-05-01 at 2 28 49 PM" src="https://github.com/user-attachments/assets/6d5b35ed-b855-4dfe-8100-08e751c0c211" />


If you have not already configured and installed the following, as done for the ANIb and ANIm tools, it is necessary to add the following channles to your conda environment to run sourMASH:

```bash
conda config --add channels conda-forge
conda config --add channels bioconda
conda config --add channels defaults
conda install pyani -y
conda install -c bioconda pyani dashing
```
Once you have added all your channels and installed bioconda pyani dashing, you should be ready to test your sourMASH tools (refer to the section below labelled sourMASH)

## Tools to Find Different ANI scores

## ANIb and ANIm
ANIb is a BLASTn based ANI tool to find average nucleotide identity between different genomes. ANIm is a MUMmer based ANI tool to find average nucleotide identity between different genomes.

The steps below show how to run ANIb with three test genomes in the genera *Mycobacterium*, *Streptoccous*, and *Streptomyces*. These steps will run assuming you have already cloned the repo (refer to Clone the Repo if you have not already done this)

Below is an in depth step by step run of how to test ANIb with the *Mycobacterium* genomes. The steps for the other two genera follow a very similar style with slight changes, so they display a very broad overview of how to test ANIb.

### running ANIb with *Mycobacterium*, *Streptococcus*, and *Streptomyces* genomes
After you have activated your pyANI_env (refer to Activating the pyANI_env to run ANIb and ANIm for instructions on how to do this), run the following code:

```bash
cd COMP-383-Design-Doc
```

```bash
cd ANIb/runanib_mtb.py
```

Once you're in the runanib_mtb.py script, you will have to change the input directory to where the three genomes we are using are stored, and also change the output directory. These changes will have to be made on lines 6,7, and 26 of the script. See photo below for specific lines of code you will need to hardcode: 

<img width="976" height="432" alt="Screen Shot 2026-05-01 at 2 49 05 PM" src="https://github.com/user-attachments/assets/9cc05070-1c88-440c-a652-b396ef19f7fd" />

The input directory, line 6's, path should change to "/home/username/COMP-383-Design-Doc/genomes/mtb_3genomes" with your respective username

The output directory, line 7's, path should change to "/home/username/COMP-383-Design-Doc/ANIb/mtb_ANIb_results" with your respective username 

Line 26's path should change to "/home/username/COMP-383-Design-Doc/ANIb/mtb_ANIb_results/ANIb_percentage_identity.tab" with your respective username

Once you have edited these lines of code, you are ready to run the code by running the following command: 
```bash
python runanib_mtb.py
```

Note: The code might take some time to run, but it will eventually generate results directly in the terminal, as well as in your file called mtb_ANIb_results

These results generate true ANI scores. 

To test the ANIb tool for Streptoccocus and Streptomyces follow the same instructions as above except change where input and output to the correct paths for each respective species. 

### running ANIb for *Streptomyces* genomes
For *Streptomyces*, follow the instructions as seen in the *Mycobacterium* run, and implement the following changes to the code: 

```bash
cd COMP-383-Design-Doc
```

```bash
cd ANIb/runanib_streptomyces.py
```

The input directory's path should be changed to "/home/username/COMP-383-Design-Doc/genomes/streptomyces_3genomes"

The output directory's path should change to "/home/username/COMP-383-Design-Doc/ANIb/streptomyces_ANIb_results" with your respective username 

The final change should occur with the line that starts with "df" in the script and the path should change to "/home/username/COMP-383-Design-Doc/ANIb/streptomyces_ANIb_results/ANIb_percentage_identity.tab" with you respective username 

Once those changes are made run the script by running the following command: 

```bash
python runanib_streptomyces.py
```

### running ANIb for *Streptococcus* genomes
For *Streptococcus*, follow the instructions as seen in the *Mycobacterium* run, and implement the following changes to the code:

```bash
cd COMP-383-Design-Doc
```

```bash
cd ANIb/runanib_streptococcus.py
```

The input directory's path should be changed to "/home/username/COMP-383-Design-Doc/genomes/streptococcus_3genomes"

The output directory's path should change to "/home/username/COMP-383-Design-Doc/ANIb/streptococcus_ANIb_results" with your respective username 

The final change should occur with the line that starts with "df" in the script and the path should change to "/home/username/COMP-383-Design-Doc/ANIb/streptococcus_ANIb_results/ANIb_percentage_identity.tab" with you respective username 

Once those changes are made run the script by running the following command: 

```bash
python runanib_streptococcus.py
```

### OrthoANI

We have identified a bug affecting Mac Safari users. When downloading data from the NCBI Datasets web interface, you may see only this README file after the download has completed (while other files appear to be missing).
As a workaround to prevent this issue from recurring, we recommend disabling automatic zip archive extraction in Safari until Apple releases a bug fix.
For more information, visit:
https://www.ncbi.nlm.nih.gov/datasets/docs/reference-docs/mac-zip-bug/

Steps to install: 
1. install blast
2. conda create -n orthoani_env
3. conda activate orthoani_env
4. conda install -c bioconda blast -y



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
Mash produces distance values that approximate ANI

conda create -n mash_env -y
conda activate mash_env
conda install -c bioconda mash -y

Visit the NCBI Datasets documentation pages:
https://www.ncbi.nlm.nih.gov/datasets/docs/

### SourMASH 

---

National Center for Biotechnology Information
National Library of Medicine
info@ncbi.nlm.nih.gov
# COMP-383-Design-Doc
