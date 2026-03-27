import subprocess #used to run pyANI
import os
import pandas as pd #used it to visualize my data in a "table" format


input_dir = "/home/amathew6/ANIProject/streptococcus_3genomes" #where my genomes.fna files live
output_dir = "/home/amathew6/ANIProject/streptococcus_3genomes_ani" #where all the files that I am generating get output


os.makedirs(output_dir, exist_ok=True) #when I first ran this, I didn't have an output directory made, so this command just made the directory for me

print("Starting ANIb run...") #i added print statements because when I first ran this the first few times it didn't work and I wanted to see where my code was failing


subprocess.run([
    "average_nucleotide_identity.py", #this will find the average_nucleotide_identity that is built into the pyANI tool 
    "-i", input_dir, #calls the genomes in my input directory 
    "-o", output_dir, #outputs all the results to output_dir which leads to my mtb_3genomes_ani folder
    "-m", "ANIb",  #shows what kind of ANIm I want to run 
    "--workers", "4", #uses 4 cores 
    "-g", #generates the graphs (heatmaps) for this output
    "-f" #when running this script many time -f is used to froce a manual overwrite 
], check=True)



df = pd.read_csv("streptococcus_3genomes_ani/ANIb_percentage_identity.tab", sep="\t", index_col=0) #creates an easy readable table to interpret ANIb results 


df_percent = df * 100 #did this becauase it defaulted to printing as a decimal 

print(df_percent) #prints a nice table 


print("Finished ANIb!") #to show that the entire code did run with no errors