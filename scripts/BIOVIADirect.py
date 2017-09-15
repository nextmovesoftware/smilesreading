# set PATH=C:\Tools\Oracle\product\11.2.0\client_1\BIN;%PATH%
# ...for OCI.dll

import cx_Oracle as cx

import my_oracle
con = cx.connect(my_oracle.details)
c = con.cursor()

import common

class MyAromaticSmilesWriter(common.AromaticSmilesWriter):
    def getoutput(self, smi):
        c.execute("select smiles(mol('%s')) from dual" % smi)
        smi = next(c)[0]
        return smi

class MyHydrogenCounter(common.HydrogenCounter):
    def getoutput(self, smi):
        c.execute("select molfile(mol('%s')) from dual" % smi)
        try:
            results = next(c)
        except cx.DatabaseError:
            return None, "Parse_error"
        molfile = results[0].read()
        return None, "MOLFILE:%s" % molfile.replace("\n", "!!")

if __name__ == "__main__":
    myname = "BIOVIADirect_2017"
    # MyAromaticSmilesWriter(myname).main()
    MyHydrogenCounter(myname).main()
