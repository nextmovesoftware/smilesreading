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

msgstream = oe.oeosstream()
oe.OEThrow.SetOutputStream(msgstream)

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        mol = oe.OEGraphMol()
        msgstream.clear()
        ok = oe.OEParseSmiles(mol, smi)
        if not ok:
            msg = msgstream.str().decode("utf-8")
            if "Kekul" in msg:
                return None, "Kekulization_failure"
            else:
                return None, "Parse_error"

        return [atom.GetImplicitHCount() for atom in mol.GetAtoms()], None

flags = oe.OESMILESFlag_BondStereo ^ oe.OESMILESFlag_AtomStereo ^ oe.OESMILESFlag_Canonical

class MyStereoSmilesWriter(common.StereoSmilesWriter):
    def getoutput(self, smi):
        mol = oe.OEGraphMol()
        ok = oe.OEParseSmiles(mol, smi)
        assert ok
        return oe.OECreateSmiString(mol, flags)

if __name__ == "__main__":
    myname = "oechem_Feb2018"
    # MyAromaticSmilesWriter(myname).main()
    # MyHydrogenCounter(myname).main()
    MyStereoSmilesWriter(myname).main()
