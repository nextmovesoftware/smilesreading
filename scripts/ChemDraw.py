# Python 3
import common
import sys
sys.path.append(r"C:\Program Files (x86)\PerkinElmerInformatics\ChemOffice2016\ChemScript\Lib")
import ChemScript16 as cs

mol = cs.StructureData.LoadData("c1ccccc1")
op = cs.NormOptions()

op.AnonList = False
op.Azide = False
op.CleaveIntoSalts = False
op.CreatedDelRep_1 = False
op.CreatedDelRep_2 = False
op.CollapseZwitterion = False
op.Dative = False
op.DativeToDouble = False
op.Dekekulize = True
op.Delrep = False
op.Diazo_a = False
op.Diazo_b = False
op.FeaturelessHydrogens = False
op.Isonitrile_fg = False
op.MergeCharges = False
op.MergeMetalSalts = False
op.MoveChargeFromCarbon = False
op.NeutralDiazo_fg = False
op.RemoveIsotopy = False
op.RemoveLabel = False
op.RemoveNonGraphStereo = False
op.RemoveRTable = False
op.RemoveRxnCenters = False
op.RemoveTextAtoms = False
op.RemoveValence = False
op.RemoveWedge = False
op.StripEitherDoubleBond = False
op.StripEitherSingleBond = False
op.R3NO_b = False
op.ProvideMissingCoords = False
op.Thiazole = False
op.XMinusToX_fg = False
op.ExpandStoichiometry = False
op.ConsolidateStoichiometry = False

print(op) # Prints out the values of the options

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        mol = cs.StructureData.LoadData(smi)
        if mol is None:
            return None, "Parse_error"
        mol.NormalizeStructure(op)
        writer = cs.SDFileWriter.OpenFile("tmp.sdf", cs.OverWrite)
        writer = cs.SDFileWriter.OpenFile("tmp.sdf", cs.OverWrite)
        writer.WriteStructure(mol)
        writer.Close()
        with open("tmp.sdf", "r") as f:
            molfile = f.read()
        return None, "MOLFILE:%s" % molfile.replace("\n", "!!")

if __name__ == "__main__":
    myname = "ChemDraw_16.0"
    # MyHydrogenCounter(myname).main()
