#first activate sourmash_env 
#steps to activate sourmash_env can be found on the GitHub

import subprocess #used to run ANI tools
import os
import glob #finds files that match a pattern --> i'm looking for files that match the ending .fna 

input_dir = "/home/amathew6/ANIProject/SourMASH/streptomyces_3genomes" #where the genomes live
output_dir = "/home/amathew6/ANIProject/SourMASH/streptomyces_SourMASH_results" #where I want my results stored

os.makedirs(output_dir, exist_ok=True) #checks if there's an output directory, and if there isn't one it'll create one

genome_files = glob.glob(os.path.join(input_dir, "*.fna")) #looks for all files that ends in .fna and creates a list

signature_file = os.path.join(output_dir, "signatures.sig") #makes sketches for genomes
csv_output = os.path.join(output_dir, "ani_matrix.csv") #stores the output as a csv table 

print("Sketching genomes...") #used print statements to see where my code was erroring out
cmd = ["sourmash", "sketch", "dna", *genome_files, "-o", signature_file] #this part converts each genome into a Minihash sketch which will allow for faster comparison between genomes 
subprocess.run(cmd, check=True)


print("Exporting CSV...") #used print statements to see where my code was erroring out
subprocess.run(["sourmash", "compare", signature_file, "--csv", csv_output], check=True)#creates a csv file for output

print("Finished!") #end result
