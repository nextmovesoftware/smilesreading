import sys
import subprocess

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        command = ["/home/noel/Tools/IanWatsonLib/Lilly-Medchem-Rules/Molecule/noel", "0", smi]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        msmi = stdout.rstrip()
        if stderr:
            print("%s gives %s\n" % (smi, stderr))
        return msmi

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):

        command = ["/mnt/d/Tools/IanWatsonLib/Lilly-Medchem-Rules/Molecule/iwtoolkittest", "1", smi]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        stderr = stderr.decode()
        hcounts = [int(x) for x in stdout.strip().split()]
        if stderr:
            if "find kekule form failed" in stderr or "no kekule form" in stderr:
                return None, "Kekulization_failure"
            else:
                print("%s gives\n%s\n%s\n" % (smi, hcounts, stderr))
        return hcounts, None

if __name__ == "__main__":
    myname = "iwtoolkit_1.0"
    # MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()

