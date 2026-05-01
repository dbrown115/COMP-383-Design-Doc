import subprocess
import os
import pandas as pd

# ====== PATHS ======
genome_dir = "/home/akawamleh/Dashing2/streptomyces_3genomes"
output_dir = "/home/akawamleh/Dashing2/streptomyces_dashing_results"

os.makedirs(output_dir, exist_ok=True)

# ====== STEP 1: GET GENOME FILES ======
genomes = [os.path.join(genome_dir, f) for f in os.listdir(genome_dir) if f.endswith(".fna")]
genomes = genomes[:3]  # take first 3 genomes

print("Genomes selected:")
for g in genomes:
    print(g)

# ====== STEP 2: RUN DASHING 2 ======
dashing_out = os.path.join(output_dir, "dashing2_output.txt")

print("\nRunning Dashing 2...")
subprocess.run([
    "dashing2", "sketch", "--cmpout", dashing_out,
    *genomes
], check=True)

print("Dashing 2 finished.")

# ====== STEP 3: READ OUTPUT ======
print("\nDashing 2 Results:")
try:
    rows = []
    sources = []
    with open(dashing_out) as f:
        for line in f:
            if line.startswith("#Sources"):
                sources = line.strip().split("\t")[1:]
            elif not line.startswith("#"):
                parts = line.strip().split("\t")
                genome = os.path.basename(parts[0])
                scores = [s if s != "-" else "1.0" for s in parts[1:]]
                rows.append([genome] + scores)
    cols = ["Genome"] + [os.path.basename(s) for s in sources]
    df_dashing = pd.DataFrame(rows, columns=cols)
    print(df_dashing)
except Exception as e:
    print("Could not parse Dashing 2 output:", e)

print("\nPipeline complete.")
