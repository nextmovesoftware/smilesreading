import os
import sys
import glob
import re

pat = re.compile("  4  0\s*!!")

class HydrogenCounterFromMolfile(object):
    def __init__(self, name):
        self.name = name
    def main(self):
        fname = os.path.join("..", "3-results", "*", "%s_*.txt" % self.name)
        filenames = glob.glob(os.path.join("..", "3-results", "*", "%s_*.txt" % self.name))
        for results in filenames:
            dirname = os.path.dirname(results)
            basename = os.path.basename(results)
            tmpfile = os.path.join(dirname, "%s.tmp" % basename)
            with open(tmpfile, "w") as out:
                for line in open(results):
                    if line[0] != '#':
                        out.write(line)
                        continue
                    _, title, data = line.rstrip().split(" ", 2)
                    if not data.startswith("MOLFILE:"):
                        out.write(line)
                        continue
                    if pat.search(data): # aromatic bond
                        out.write("# %s Kekulization_failure\n" % title)
                        continue
                    molfile = "\n".join(data[8:].split("!!"))
                    hcounts = self.getoutput(molfile)
                    out.write("%s %s\n" % (title, " ".join(str(x) for x in hcounts)))
            os.rename(results, "%s.orig" % results)
            os.rename(tmpfile, results)
