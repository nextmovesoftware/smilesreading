import subprocess

import common

cex = """$D<MOL>
/_P<molecule>
/_V<Molecule>
/_S<1M>
/_L<XSMILES>
/_X<Molecule represented in XSMILES (Exchange SMILES)>
|
$MOL<%s>
|
"""

def isAromaticSmiles(smi):
    N = len(smi)
    for i in range(N):
        x = smi[i]
        if x == ":": return True
        if x>='a' and x<='z':
            if i==0 or smi[i-1]=='[' or x in "bcnsopfi" or smi[i-1:i+1] in ["cl", "br"]:
                return True
    return False

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        if isAromaticSmiles(smi):
            return None, "Aromatic_smiles_not_supported"
        # Neither are up/down bond symbols
        command = ["/home/noel/Tools/tmp/cex132/src/applics/mol/printmol"]
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate(cex % smi)
        out = stdout.split("\n")
        if stderr:
            return None, stderr.replace(" ", "_")
        for line in out:
            if "Implicit hcount" in line:
                idx = line.find('"')
                hcounts = map(int, line[idx+1:line.find('"', idx+1)].split(";"))
                return hcounts, None
                
        return None, "No_hcounts"

if __name__ == "__main__":
    myname = "WeiningerCEX_132"
    MyHydrogenCounter(myname).main()

