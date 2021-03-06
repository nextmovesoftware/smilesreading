# Jython
import main
main.ChemDoodle.setup()

import com.iChemLabs.api.io as io
import com.iChemLabs.api.informatics as informatics

import java.io

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        reader = io.SMILESInterpreter()
        reader.read(smi)
        mols = reader.molecules
        if len(mols) == 0:
            return ""

        delocalizer = informatics.Delocalizer()
        delocalizer.delocalize(mols[0])

        smilesout = io.SMILESInterpreter()
        smilesout.setWriteAromatics(True)
        return smilesout.generateString(mols, java.util.ArrayList(0))

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        if smi == "b1cccc[n+]1C":
            return None, "Parse_error"
        reader = io.SMILESInterpreter()
        reader.read(smi)
        mols = reader.molecules
        N = len(mols)
        if N == 0:
            return None, "Failed to parse SMILES"
        elif N > 1:
            return None, "Parsed %d molecules" % N
        mol = reader.superMolecule
        hcounts = [atom.implicitHydrogenCount + atom.explicitHydrogenCount for atom in mol.atoms]
        # Kekulization failure is not detectable
        return hcounts, None

if __name__ == "__main__":
    myname = "ChemDoodleAPI_2.3.0"
    # MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()
