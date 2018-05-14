import sys
from openeye import oechem as oe

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        mol = oe.OEGraphMol()
        ok = oe.OEParseSmiles(mol, smi)
        assert ok
        oe.OEAssignAromaticFlags(mol)
        return oe.OECreateSmiString(mol, 0)

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        mol = oe.OEGraphMol()
        ok = oe.OEParseSmiles(mol, smi)
        if not ok:
            return None, "Kekulization_failure"

        return [atom.GetImplicitHCount() for atom in mol.GetAtoms()], None

if __name__ == "__main__":
    myname = "oechem_Feb2018"
    # MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()
