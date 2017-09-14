import common_molfile
from openeye import oechem as oe

class MyHydrogenCounterFromMolfile(common_molfile.HydrogenCounterFromMolfile):
    def getoutput(self, molfile):
        istream = oe.oemolistream()
        istream.SetFormat(oe.OEFormat_MDL)
        ok = istream.openstring(molfile)
        assert ok
        mol = oe.OEGraphMol()
        ok = oe.OEReadMDLFile(istream, mol)
        assert ok
        return [x.GetImplicitHCount() for x in mol.GetAtoms()]

if __name__ == "__main__":
    # myname = "BIOVIADraw_2017"
    myname = "ChemDraw_16.0"
    MyHydrogenCounterFromMolfile(myname).main()
