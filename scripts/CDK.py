# Jython
import org.openscience.cdk as cdk
import java

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        sp = cdk.smiles.SmilesParser(cdk.silent.SilentChemObjectBuilder.getInstance())
        mol = sp.parseSmiles(smi)

        aromaticity = cdk.aromaticity.Aromaticity(cdk.aromaticity.ElectronDonation.daylight(),  cdk.graph.Cycles.or(cdk.graph.Cycles.all(),cdk.graph.Cycles.all(6)))
        aromaticity.apply(mol)
        sg = cdk.smiles.SmilesGenerator(cdk.smiles.SmiFlavor.UseAromaticSymbols)
        msmi = sg.create(mol)
        return msmi

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        sp = cdk.smiles.SmilesParser(cdk.silent.SilentChemObjectBuilder.getInstance())
        try:
            mol = sp.parseSmiles(smi)
        except cdk.exception.InvalidSmilesException as e:
            msg = e.message
            if "kekul" in msg.lower():
                return None, "Kekulization_failure"
            if "could not parse" in msg:
                return None, "Parse_error"
            print "%s gives %s" % (smi, msg)
            return

        N = mol.getAtomCount()
        hcounts = [mol.getAtom(i).getImplicitHydrogenCount() for i in range(N)]
        return hcounts, None

class MyStereoSmilesWriter(common.StereoSmilesWriter):
    def getoutput(self, smi):
        sp = cdk.smiles.SmilesParser(cdk.silent.SilentChemObjectBuilder.getInstance())
        mol = sp.parseSmiles(smi)

        sg = cdk.smiles.SmilesGenerator(cdk.smiles.SmiFlavor.Absolute)
        msmi = sg.create(mol)
        return msmi

if __name__ == "__main__":
    myname = "cdk_2.1"
    # MyAromaticSmilesWriter(myname).main()
    # MyHydrogenCounter(myname).main()
    MyStereoSmilesWriter(myname).main()
