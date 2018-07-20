# At the 64-bit Anaconda prompt, "activate my-rdkit-env" first.

import sys
from rdkit import Chem
from io import StringIO

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        m = Chem.MolFromSmiles(smi)
        if m is None:
            return ""
        return Chem.MolToSmiles(m, canonical=False)

class MyHydrogenCounter(common.HydrogenCounter):
    def __init__(self, name):
        super(MyHydrogenCounter, self).__init__(name)
        Chem.WrapLogs()
        old_stderr = sys.stderr
        self.sio = sys.stderr = StringIO()
    
    def getoutput(self, smi):
        m = Chem.MolFromSmiles(smi)
        err = self.sio.getvalue()
        if err:
            self.sio = sys.stderr = StringIO()
            if "Can't kekulize" in err:
                return None, "Kekulization_failure"
            elif "Explicit valence" in err:
                return None, "Bad_valence"
            elif "SMILES Parse Error" in err:
                return None, "SMILES_parse_error"
            elif "Aromatic bonds on non aromatic atom" in err:
                return None, "Aromatic_bonds_on_non_aromatic_atom"
            elif "non-ring" in err and "marked aromatic" in err:
                return None, "Non_ring_atom_marked_aromatic"
            print("**ERROR NOT CAPTURED from %s\n%s " % (smi, err))
        if m is None:
            return None, "No_output"
        return [atom.GetTotalNumHs(False) for atom in m.GetAtoms()], None

class MyStereoSmilesWriter(common.StereoSmilesWriter):
    def getoutput(self, smi):
        m = Chem.MolFromSmiles(smi)
        if m is None:
            return ""
        return Chem.MolToSmiles(m, canonical=True)

if __name__ == "__main__":
    myname = "rdkit_2018.03.1"
    # MyAromaticSmilesWriter(myname).main()
    # MyHydrogenCounter(myname).main()
    MyStereoSmilesWriter(myname).main()

