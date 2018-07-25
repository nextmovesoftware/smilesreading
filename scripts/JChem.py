#!/usr/bin/env jython

import os
import sys

# Add all JChem jars to path
JCHEM_LIB = '/Applications/ChemAxon/JChemSuite/lib'
for f in os.listdir(JCHEM_LIB):
    sys.path.append(os.path.join(JCHEM_LIB, f))

from chemaxon.formats import MolImporter, MolExporter, MolFormatException
from chemaxon.marvin.io import MolExportException

import common


# SMILES import/export options: https://docs.chemaxon.com/display/docs/SMILES+and+SMARTS+import+and+export+options
# Aromatization and hydrogen export options: https://docs.chemaxon.com/display/docs/Basic+export+options


class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        try:
            mol = MolImporter.importMol(smi, 'smiles')
        except MolFormatException as e:
            return ''
        try:
            # a - General (Daylight) aromatization. (Alternatives: a_bas, a_loose, a_ambig, etc.)
            # u - Write "unique" smiles (include chirality into graph invariants, slower)
            msmi = MolExporter.exportToFormat(mol, 'smiles:a')
        except MolExportException as e:
            # return ' '.join(str(e).split('\n'))  # Write error message to a single line
            return ''
        return msmi


class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        try:
            mol = MolImporter.importMol(smi, 'smiles')
        except MolFormatException as e:
            return (None, 'Parse_error')
        success = mol.dearomatize()
        if not success:
            return (None, 'Kekulization_failure')
        N = mol.getAtomCount()
        hcounts = [atom.getImplicitHcount() for atom in mol.getAtomIterator()]
        return hcounts, None

class MyStereoSmilesWriter(common.StereoSmilesWriter):
    def getoutput(self, smi):
        try:
            mol = MolImporter.importMol(smi, 'smiles')
        except MolFormatException as e:
            return ''
        try:
            # a - General (Daylight) aromatization. (Alternatives: a_bas, a_loose, a_ambig, etc.)
            # u - Write "unique" smiles (include chirality into graph invariants, slower)
            msmi = MolExporter.exportToFormat(mol, 'smiles:u')
        except MolExportException as e:
            # return ' '.join(str(e).split('\n'))  # Write error message to a single line
            return ''
        return msmi

if __name__ == "__main__":
    myname = "jchem_17.23"
    # MyAromaticSmilesWriter(myname).main()
    # MyHydrogenCounter(myname).main()
    MyStereoSmilesWriter(myname).main()

