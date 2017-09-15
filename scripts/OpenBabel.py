import common

import pybel
ob = pybel.ob

# Changed smilesformat to return false for kekulization errors

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        try:
            mol = pybel.readstring("smi", smi)
        except IOError:
            return None, "Kekulization_failure"
        return [atom.OBAtom.GetImplicitHCount() for atom in mol], None

if __name__ == "__main__":
    myname = "openbabel_dev4Aug17.smi"
    MyHydrogenCounter(myname).main()
