import sys
sys.path.append(r"C:\Tools\Indigo\indigo-python-1.2.3.r0-win")
from indigo import Indigo, IndigoException
indigo = Indigo()

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        mol = indigo.loadMolecule(smi)
        mol.aromatize()
        return mol.smiles()

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        try:
            mol = indigo.loadMolecule(smi)
        except IndigoException as e:
            if "unrecognized lowercase symbol" in e.value:
                return None, "Unrecognized_lowercase_symbol"
            else:
                print smi
                print e.value
                fd
        try:
            hcounts = [atom.countImplicitHydrogens() for atom in  mol.iterateAtoms()]
        except IndigoException as e:
            if "can not calculate implicit hydrogens" in e.value:
                return None, "Unknown_HCount"
            elif "bad valence on" in e.value:
                return None, "Bad_valence"
            else:
                print smi
                print e.value
                fd

        return hcounts, None

if __name__ == "__main__":
    myname = "indigo_1.2.3.r0"
    # MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()

