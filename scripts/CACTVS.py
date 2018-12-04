# Run this as follows:
# start D:\Program Files (x86)\cactvs3_426\lib\pycactvs
# > import os, sys
# > os.chdir("D:\Work\smilesreading\scripts")
# > sys.path.append("C:\Tools\smilesreading\scripts")
# > import CACTVS
# > CACTVS.MyAromaticSmilesWriter("cactvs_3_426").main()
# > CACTVS.MyHydrogenCounter("cactvs_3_426").main()

import common
import pycactvs as cs

cs.Prop.Setparam('E_SMILES', {'usearo':True}) # Create aromatic SMILES

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        mol = cs.Ens(smi)
        aromsmi = mol.new("E_SMILES")
        mol.delete()
        return aromsmi

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        mol = cs.Ens(smi)
        hcounts = [atom.A_HCOUNT for atom in mol.atoms() if atom.A_ELEMENT != 1]
        mol.delete()
        return hcounts, None

if __name__ == "__main__":
    myname = "cactvs_3_426"
    # MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()
