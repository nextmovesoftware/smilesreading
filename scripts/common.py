import os
import sys
import glob

class AromaticSmilesWriter:
    def __init__(self, name):
        self.name = name
    def main(self):
        for benchmark in glob.glob(os.path.join("..", "1-benchmarks", "*.smi")):
            dirname = os.path.basename(benchmark).split(".")[0]
            outdirname = os.path.join("..", "2-aromaticsmiles", dirname)
            if not os.path.isdir(outdirname):
                os.mkdir(outdirname)
            outfname = os.path.join(outdirname, "%s.smi" % self.name)
            with open(outfname) as out:
                for line in open(fname):
                    smi, title = line.rstrip().split()
                    output = getoutput(smi)
                    out.write("%s %s\n" % (output, title))

class HydrogenCounter:
    def __init__(self, name):
        self.name = name
    def main(self):
        for benchmark in glob.glob(os.path.join("..", "1-benchmarks", "*.smi")):
            dirname = os.path.basename(benchmark).split(".")[0]
            outdirname = os.path.join("..", "3-results", dirname)
            if not os.path.isdir(outdirname):
                os.mkdir(outdirname)
            for inputfile in glob.glob(os.path.join("..", "2-aromaticsmiles", dirname, "*.smi")):
                inputprogram = os.path.basename(inputfile).split(".")[0]
                outfname = os.path.join(outdirname, "%s_reading_%s.txt" % (self.name, inputprogram))
                with open(outfname, "w") as out:
                    for line in open(fname):
                        tmp = line.rstrip().split()
                        if len(tmp) == 1:
                            out.write("# %s No_input\n" % tmp[0])
                            continue
                        elif len(tmp) == 2:
                            smi, title = tmp
                        elif len(tmp) == 3:
                            smi, cxn, title = tmp
                        hcounts, error = getoutput(smi)
                        if error:
                            out.write("# %s %s\n" % (title, error))
                        else:
                            out.write("%s %s\n" % (title, " ".join(str(x) for x in hcounts)))
