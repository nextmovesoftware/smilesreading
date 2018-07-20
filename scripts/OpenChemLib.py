# Jython
import java
import com.actelion.research.chem as chem

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        parser = chem.SmilesParser()
        mol = chem.StereoMolecule()
        parser.parse(mol, smi, java.lang.Boolean(False), java.lang.Boolean(False))

        isc = chem.IsomericSmilesCreator(mol)
        return isc.getSmiles()

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        parser = chem.SmilesParser()
        mol = chem.StereoMolecule()
        try:
            parser.parse(mol, smi, java.lang.Boolean(False), java.lang.Boolean(False))
        except java.lang.Exception, e:
            if "Assignment of aromatic double bonds" in e.message:
                return None, "Kekulization_failure"
            else:
                raise e
        N = mol.getAllAtoms()
        hcounts = [mol.getImplicitHydrogens(i) for i in range(N)]
        return hcounts, None

class MyStereoSmilesWriter(common.StereoSmilesWriter):
    def getoutput(self, smi):
        parser = chem.SmilesParser()
        mol = chem.StereoMolecule()
        parser.parse(mol, smi)

        isc = chem.IsomericSmilesCreator(mol)
        return isc.getSmiles()

if __name__ == "__main__":
    myname = "openchemlib_2018.7.0"
    # MyAromaticSmilesWriter(myname).main()
    # MyHydrogenCounter(myname).main()
    MyStereoSmilesWriter(myname).main()

