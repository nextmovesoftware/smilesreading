# At the 64-bit Anaconda prompt, "activate my-rdkit-env" first.

from rdkit import Chem
from StringIO import StringIO

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        m = Chem.MolFromSmiles(smi)
        if m is None:
            return ""
        return Chem.MolToSmiles(m, canonical=False)

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        m = Chem.MolFromSmiles(smi)
        if m is None:
            return None, "No_output"
        return [atom.GetTotalNumHs(False) for atom in m.GetAtoms()], None

if __name__ == "__main__":
    myname = "rdkit_2017.03.3"
    MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()
