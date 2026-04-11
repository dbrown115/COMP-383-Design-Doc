import os
import csv
import argparse
import subprocess

# -------- accessions --------
ACCESSIONS = {
    "mtb": [
        "GCF_000008585.1",
        "GCF_000009445.1",
        "GCF_000010685.1"
    ],
    "streptomyces": [
        "GCF_000009765.2",
        "GCF_000010605.1",
        "GCF_000091305.1"
    ],
    "streptococcus": [
        "GCF_000006785.2",
        "GCF_000006885.1",
        "GCF_000007045.1"
    ]
}


def get_fna_files(genus_name, genus_dir):
    """Return list of .fna file paths for a given genus."""
    fna_files = []

    for accession in ACCESSIONS[genus_name]:
        accession_path = os.path.join(genus_dir, accession)

        if os.path.isdir(accession_path):
            for f in os.listdir(accession_path):
                if f.endswith(".fna"):
                    fna_files.append(os.path.join(accession_path, f))
        else:
            print(f"Warning: {accession} not found")

    return fna_files


# -------- mash ani --------
def run_mash_ani(query, reference):
    """
    Run mash triangle on two genomes and extract the ANI-equivalent distance.
    mash dist output: query  reference  distance  p-value  shared-hashes
    ANI = (1 - mash_distance) * 100
    """
    result = subprocess.run(
        ["mash", "dist", query, reference],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()

    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3:
            try:
                mash_dist = float(parts[2])
                ani = (1 - mash_dist) * 100  # convert distance to ANI %
                return round(ani, 4)
            except ValueError:
                continue

    print("Error: could not parse mash dist output")
    print(result.stdout + result.stderr)
    return None


# -------- args --------
parser = argparse.ArgumentParser(description="Compute pairwise Mash ANI for bacterial genomes.")

parser.add_argument("-d", "--data_dir", required=True, help="Root directory containing genus subdirs")
parser.add_argument("-o", "--output", required=True, help="Output CSV file path")

args = parser.parse_args()


# -------- genus dirs --------
genera = {
    "mtb": os.path.join(args.data_dir, "mtb", "ncbi_dataset", "data"),
    "streptomyces": os.path.join(args.data_dir, "streptomyces", "ncbi_dataset", "data"),
    "streptococcus": os.path.join(args.data_dir, "streptococcus", "ncbi_dataset", "data"),
}


# -------- main loop --------
with open(args.output, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["genus", "query", "reference", "mash_ani"])

    for genus_name, genus_dir in genera.items():
        print(f"\nProcessing {genus_name}...")

        fna_files = get_fna_files(genus_name, genus_dir)
        print(f"  Selected {len(fna_files)} genomes")

        total = len(fna_files) * (len(fna_files) - 1) // 2
        count = 0

        for i in range(len(fna_files)):
            for j in range(i + 1, len(fna_files)):
                ani = run_mash_ani(fna_files[i], fna_files[j])

                count += 1
                print(f"  [{count}/{total}] Mash ANI: {ani}")

                query_name = os.path.basename(os.path.dirname(fna_files[i]))
                ref_name = os.path.basename(os.path.dirname(fna_files[j]))

                writer.writerow([genus_name, query_name, ref_name, ani])


print(f"\nDone Results saved to {args.output}")