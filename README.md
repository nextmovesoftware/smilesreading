# SMILES reading benchmark

I call this a benchmark, but it is primarily a means to identify ambiguities in the spec and highlight cornercases, with the goal of ensuring that SMILES are transferred between different programs without any loss or corruption of information.

This benchmark focuses exclusively on whether different programs can agree on the identity of a molecule as read from a SMILES string, particularly an aromatic SMILES string. For each benchmark SMILES string, the result is the number of implicit hydrogens on each atom of the molecule (in the order in which they appear in the SMILES string).

If you are interested in looking at the results, unzip some of the entries in the results folder and diff them. Note that it only makes sense to compare entries where they are reading the same SMILES string, i.e. ProgramA-reading-ProgramC.txt and ProgramB-reading-ProgramC.txt.

If you are interested in adding results for a new toolkit, unzip everything (keeping the originals*) and create a new script in the scripts directory that does the conversion, first from the benchmark Kekule SMILES to aromatic SMILES, and then counting the number of implicit hydrogens in each of the aromatic SMILES strings.

* Note: "gunzip -k" will do this, but is not available on some platforms. Otherwise, "for d in *.gz; do gunzip -c $d > ${d%.smi.gz}.smi; done".


