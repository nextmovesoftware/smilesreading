"""
Run this as follows:
start D:\Program Files (x86)\cactvs3_426\lib\pycactvs
> import os, sys
> os.chdir("D:\Work\smilesreading\scripts")
> sys.path.append("D:\Work\smilesreading\scripts")
> import Cactvs
> Cactvs.MyAromaticSmilesWriter("cactvs_3_426").main()
> Cactvs.MyHydrogenCounter("cactvs_3_426").main()
> Cactvs.MyStereoSmilesWriter("cactvs_3_426").main()
> import importlib
> importlib.reload(Cactvs)
or on Linux
$ export PYTHONPATH=/home/noel/Tools/Cactvs/python3.6
$ export LD_LIBRARY_PATH=/home/noel/Tools/Cactvs/lib
$ /home/noel/Tools/Cactvs/python3
...as above
"""

import common
import pycactvs as cs

# cs.Prop.Setparam('E_SMILES', {'usearo':True}) # Create aromatic SMILES
cs.Prop.Setparam('E_SMILES', {'unique':True}) # Create canonical SMILES

cs.cactvs['aromaticity_model'] = 'daylight'
# Turn off the following to get the default behaviour
cs.cactvs['smiles_hypervalent_hydrogen_addition'] = 1

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

class MyStereoSmilesWriter(common.StereoSmilesWriter):
    def getoutput(self, smi):
        try:
            mol = cs.Ens(smi)
        except RuntimeError:
            return "# Parse_error"
        aromsmi = mol.new("E_SMILES")
        mol.delete()
        return aromsmi

if __name__ == "__main__":
    myname = "Cactvs_3.4.6.19"
    # MyAromaticSmilesWriter(myname).main()
    # MyHydrogenCounter(myname).main()
    MyStereoSmilesWriter(myname).main()

