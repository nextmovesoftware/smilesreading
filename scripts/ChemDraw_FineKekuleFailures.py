"""
1. Copy the original results into 3-results/ChemDraw_orig
2. Ensure that all of the input smiles files are unzipped
3. The files chemdraw/avalon_1.2.0.out, etc. should exist containing a list of SMILES along with any
   error messages

Run this script. The output is written to chemdraw.

"""
import os
import glob

def geterrors(logfile):
    errors = []
    with open(logfile) as inp:
        old = None
        for line in inp:
            line = line.strip()
            if "MF changed" in line:
                if "ChemCentral" in line:
                    errors.append( old )
                continue
            old = line
    return errors

if __name__ == "__main__":
    inputfiles = glob.glob(os.path.join("..", "3-results", "chembl", "ChemDraw_16.0_reading*.txt"))
    for inputfile in inputfiles:
        program = os.path.basename(inputfile)[22:-4]
        print(program)
        errors = geterrors(os.path.join("chemdraw", "%s.out" % program))
        print(len(errors))
        with open(os.path.join("chemdraw", "%s.errors.smi" % program), "w") as out:
            for error in errors:
                out.write("%s %s\n" % (error, error))
        errorno = 0
        finished = False
        with open(os.path.join("..", "2-aromaticsmiles", "chembl", "%s.smi" % program)) as inp:
            with open(os.path.join("..", "3-results", "chembl", "ChemDraw_orig", "ChemDraw_16.0_reading_%s.txt" % program)) as result:
                with open(os.path.join("chemdraw", "ChemDraw_16.0_reading_%s.txt" % program), "w") as out:
                    for smi, hcounts in zip(inp, result):
                        if finished or smi.split()[0] != errors[errorno]:
                            out.write(hcounts)
                        else:
                            out.write("# Kekulization_failure\n")
                            errorno += 1
                            if errorno == len(errors):
                                finished = True

