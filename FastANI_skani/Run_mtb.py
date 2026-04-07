import subprocess
import os
import pandas as pd

# ====== PATHS ======
genome_dir = "mtb_3genomes"
output_dir = "mtb_3genomes_FASTani_SKani"

os.makedirs(output_dir, exist_ok=True)

# ====== STEP 1: GET GENOME FILES ======
genomes = [os.path.join(genome_dir, f) for f in os.listdir(genome_dir) if f.endswith(".fna")]
genomes = genomes[:3]  # take first 3 genomes

# write genome list file
genome_list = os.path.join(output_dir, "genome_list.txt")
with open(genome_list, "w") as f:
    for g in genomes:
        f.write(g + "\n")

print("Genomes selected:")
for g in genomes:
    print(g)

# ====== STEP 2: RUN FASTANI ======
fastani_out = os.path.join(output_dir, "fastani_output.txt")

print("\nRunning FastANI...")
subprocess.run([
    "fastANI",
    "--ql", genome_list,
    "--rl", genome_list,
    "-o", fastani_out
], check=True)

print("FastANI finished.")

# ====== STEP 3: RUN SKANI ======
print("\nRunning skani...")

skani_out = os.path.join(output_dir, "skani_output.txt")

subprocess.run([
    "skani",
    "dist",
    "-q", *genomes,
    "-r", *genomes
], stdout=open(skani_out, "w"), check=True)

print("skani finished.")

# ====== STEP 4: READ OUTPUT ======
print("\nFastANI Results:")
try:
    df_fastani = pd.read_csv(fastani_out, sep="\t", header=None)
    df_fastani.columns = ["Genome1", "Genome2", "ANI", "Fragments", "Total"]
    print(df_fastani)
except:
    print("Could not parse FastANI output.")

print("\nskani Results:")
try:
    df_skani = pd.read_csv(skani_out, sep="\t")
    print(df_skani[["Ref_file", "Query_file", "ANI"]])
except:
    print("Could not parse skani output.")

print("\nPipeline complete.")