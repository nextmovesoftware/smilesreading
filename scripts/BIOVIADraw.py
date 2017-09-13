# IronPython
import clr
clr.AddReferenceToFileAndPath(r"C:\Program Files\BIOVIA\BIOVIA Draw 2017\lib\MDL.Draw.Foundation.dll")

from MDL.Draw.StructureConversion import StructureConverter
sc = StructureConverter()

import common
import urllib
import urllib2

import json

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        sc.Smiles = smi
        return sc.Smiles

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        try:
            sc.Smiles = smi
            molfile = sc.MolfileString
        except StandardError as e:
            msg = e.message
            if "Failed to get a molfile string" in msg:
                return None, "Parse_error"
            print "%s gives %s" % (smi, msg)
        return None, "MOLFILE:%s" % molfile.replace("\r\n", "!!")

if __name__ == "__main__":
    myname = "BIOVIADraw_2017"
    # MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()
