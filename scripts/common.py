import os
import sys
import glob

class AromaticSmilesWriter(object):
    def __init__(self, name):
        self.name = name
    def main(self):
        for benchmark in glob.glob(os.path.join("..", "1-benchmarks", "*.smi")):
            dirname = os.path.basename(benchmark).split(".")[0]
            outdirname = os.path.join("..", "2-aromaticsmiles", dirname)
            if not os.path.isdir(outdirname):
                os.mkdir(outdirname)
            outfname = os.path.join(outdirname, "%s.smi" % self.name)
            with open(outfname, "w") as out:
                for line in open(benchmark):
                    smi, title = line.rstrip().split()
                    output = self.getoutput(smi)
                    out.write("%s %s\n" % (output, title))

class HydrogenCounter(object):
    def __init__(self, name):
        self.name = name
    def main(self):
        for benchmark in glob.glob(os.path.join("..", "1-benchmarks", "*.smi")):
            dirname = os.path.basename(benchmark).split(".")[0]
            outdirname = os.path.join("..", "3-results", dirname)
            if not os.path.isdir(outdirname):
                os.mkdir(outdirname)
            for inputfile in glob.glob(os.path.join("..", "2-aromaticsmiles", dirname, "*.smi")):
                inputprogram = os.path.splitext(os.path.basename(inputfile))[0]
                outfname = os.path.join(outdirname, "%s_reading_%s.txt" % (self.name, inputprogram))
                with open(outfname, "w") as out:
                    for line in open(inputfile):
                        tmp = line.rstrip().split()
                        if len(tmp) == 1:
                            out.write("# %s No_input\n" % tmp[0])
                            continue
                        elif len(tmp) == 2:
                            smi, title = tmp
                        elif len(tmp) == 3:
                            smi, cxn, title = tmp
                        hcounts, error = self.getoutput(smi)
                        if error:
                            out.write("# %s %s\n" % (title, error))
                        else:
                            out.write("%s %s\n" % (title, " ".join(str(x) for x in hcounts)))
