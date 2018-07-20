import sys
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
        # Don't require that the input has the same aromaticity model as Indigo
        indigo.setOption("dearomatize-verification", False)
        try:
            mol = indigo.loadMolecule(smi)
        except IndigoException as e:
            if "unrecognized lowercase symbol" in e.value:
                return None, "Parse_error"
            elif "probably pending bond" in e.value:
                return None, "Parse_error"
            else:
                print smi
                print e.value
                fd
        kekulization_failure = mol.dearomatize()
        if kekulization_failure==0:
            return None, "Kekulization_failure"
        try:
            hcounts = [atom.countImplicitHydrogens() for atom in  mol.iterateAtoms()]
        except IndigoException as e:
            if "can not calculate implicit hydrogens" in e.value:
                return None, "Kekulization_failure"
            elif "bad valence on" in e.value:
                return None, "Bad_valence"
            else:
                print smi
                print e.value
                fd

        return hcounts, None

class MyStereoSmilesWriter(common.StereoSmilesWriter):
    def getoutput(self, smi):
        mol = indigo.loadMolecule(smi)
        return mol.canonicalSmiles()

if __name__ == "__main__":
    myname = "indigo_1.3.0b.r16"
    # MyAromaticSmilesWriter(myname).main()
    # MyHydrogenCounter(myname).main()
    MyStereoSmilesWriter(myname).main()

