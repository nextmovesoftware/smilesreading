import subprocess

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        command = ["/home/noel/Tools/Avalon/SourceDistribution/common/build/noel", "0", smi]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        msmi = stdout.rstrip()
        if stderr:
            print "%s gives %s\n" % (smi, stderr)
        return msmi

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        command = ["/home/noel/Tools/Avalon/SourceDistribution/common/build/noel", "1", smi]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        hcounts = map(int, stdout.strip().split())
        if stderr:
            if "Kekulization" in stderr:
                return None, "Kekulization_failure"
            elif "Parse_error" in stderr:
                return None, "Parse_error"
            #if "illegal character" in stderr and "before ring in SMILES" in stderr:
            #    return None, "Illegal_character_before_ring"
            else:
                print "%s gives\n%s\n%s\n" % (smi, hcounts, stderr)
                fd
        return hcounts, None

if __name__ == "__main__":
    myname = "avalon_1.2.0"
    # MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()

