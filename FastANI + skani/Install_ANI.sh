cd ~

mkdir -p ~/bin

curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj -C ~ bin/micromamba

~/bin/micromamba shell init -s bash

source ~/.bashrc

micromamba create -n ani -c bioconda -c conda-forge fastani skani -y