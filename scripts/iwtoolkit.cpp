#include <string>
#include "molecule.h"
#include "smiles.h"

int main(int argc, char** argv)
{
  if (argc != 3) {
    printf("Usage: NUM SMILES\n  where NUM is 0 for aromatic SMILES\n  and 1 for a list of H counts\n  and 2 for unique SMILES\n");
    exit(0);
  }

  IWString smi(argv[2]);
  Molecule m;
  m.build_from_smiles(smi);

  switch(argv[1][0]) {
  case '0': {
  set_include_aromaticity_in_smiles(1);
  IWString ans = m.smiles();
  printf("%s\n", ans.c_str());
  break;
  }

  case '1': {
  const int N = m.natoms();
  for(int i=0; i<N; ++i) {
    printf(" %d", m.implicit_hydrogens(i));
  }
  printf("\n");
  break;
  }

  case '2': {
  IWString ans = m.unique_smiles();
  printf("%s\n", ans.c_str());
  break;
  }
  }

  return 0;
}

