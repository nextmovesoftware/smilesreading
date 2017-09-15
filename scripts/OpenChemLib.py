# Jython
import java
import com.actelion.research.chem as chem

import common

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        parser = chem.SmilesParser()
        mol = chem.StereoMolecule()
        try:
            parser.parse(mol, smi, False, False)
        except java.lang.Exception, e:
            if "Assignment of aromatic double bonds" in e.message:
                return None, "Kekulization_failure"
            else:
                raise e
        N = mol.getAllAtoms()
        hcounts = [mol.getImplicitHydrogens(i) for i in range(N)]
        return hcounts, None

if __name__ == "__main__":
    myname = "openchemlib_2017.9.0"
    MyHydrogenCounter(myname).main()

