import subprocess #used to run pyANI
import os
import pandas as pd #used it to visualize my data in a "table" format


input_dir = "/home/amathew6/ANIProject/ANIm/streptococcus_3genomes" #where my genomes.fna files live
output_dir = "/home/amathew6/ANIProject/ANIm/streptococcus_ANIm_results" #where all the files that I am generating get output


os.makedirs(output_dir, exist_ok=True) #when I first ran this, I didn't have an output directory made, so this command just made the directory for me

print("Starting ANIm run...") #i added print statements because when I first ran this the first few times it didn't work and I wanted to see where my code was failing


subprocess.run([
    "average_nucleotide_identity.py", #this will find the average_nucleotide_identity that is built into the pyANI tool
    "-i", input_dir, #calls the genomes in my input directory
    "-o", output_dir, #outputs all the results to output_dir which leads to my mtb_3genomes_ani folder
    "-m", "ANIm",  #shows what kind of ANI I want to run -- ANIm
    "--workers", "4", #uses 4 cores 
    "-f" #when running this script many time -f is used to force a manual overwrite 
], check=True)

output_file = os.path.join(output_dir, "ANIm_percentage_identity.tab") #reads to the correct output file


df = pd.read_csv(output_file, sep="\t", index_col=0) #creates an easy readable table to interpret ANIm results
df_percent = df * 100 #converts answer to a percent

print(df_percent) #prints out the percents

print("Finished ANIm!") #made a print statement to ensure that the code runs to completion without erroring out