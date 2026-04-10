import subprocess #used to run pyANI
import os
import pandas as pd #used it to visualize my data in a "table" format


input_dir = "/home/amathew6/ANIProject/mtb_3genomes" #where my genomes.fna files live
output_dir = "/home/amathew6/ANIProject/mtb_3genomes_anim" #where all the files that I am generating get output


os.makedirs(output_dir, exist_ok=True) #when I first ran this, I didn't have an output directory made, so this command just made the directory for me

print("Starting ANIm run...") #i added print statements because when I first ran this the first few times it didn't work and I wanted to see where my code was failing


subprocess.run([
    "average_nucleotide_identity.py",
    "-i", input_dir,
    "-o", output_dir,
    "-m", "ANIm",
    "--workers", "4",
    "-g",
    "-f"
], check=True)

output_file = os.path.join(output_dir, "ANIm_percentage_identity.tab")

#if not os.path.exists(output_file):
   # raise FileNotFoundError(f"{output_file} not found. ANIm may have failed.")

df = pd.read_csv(output_file, sep="\t", index_col=0)
df_percent = df * 100

print(df_percent)

print("Finished ANIm!")