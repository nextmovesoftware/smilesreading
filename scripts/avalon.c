#include "reaccs.h"
#include "smi2mol.h"
#include <stdio.h>

int main(int argc, char** argv)
{
  struct reaccs_molecule_t *mol;
  struct reaccs_atom_t atom;
  char* ans;
  int i;
  int N;
  int* H_counts;
  int kekulization_failure;

  if (argc != 3) {
    printf("Usage: NUM SMILES\n  where NUM is 0 for aromatic SMILES\n  and 1 for a list of H counts\n  and 2 for unique SMILES\n");
    return 1;
  }

  mol = SMIToMOL(argv[2], 0);

  switch(argv[1][0]) {
  case '0':
  ans = MOLToSMI(mol, DY_AROMATICITY);
  printf("%s\n", ans);
  break;

  case '1':
  if (!mol) {
    fprintf(stderr, "Parse_error\n");
    return 0;
  }
  kekulization_failure = 0;
  for (i=0; i<mol->n_bonds; i++) {
    if (mol->bond_array[i].bond_type == AROMATIC)
      kekulization_failure = 1;
  }
  if (kekulization_failure) {
    fprintf(stderr, "Kekulization_failure\n");
    return 0;
  }
  H_counts = TypeAlloc(mol->n_atoms+1, int);
  for (i=0; i<=mol->n_atoms; i++)
     H_counts[i] = 0;
  ComputeImplicitH(mol, H_counts);
  /* Take care of already fixed hydrogen counts */
  /* Note: Index origin of H_counts is 1 */
  for (i=0; i<mol->n_atoms; i++)
    if (mol->atom_array[i].query_H_count != NONE)
       H_counts[i+1] = mol->atom_array[i].query_H_count-ZERO_COUNT;

  for(i=1; i<=mol->n_atoms; i++) {
    printf(" %d", H_counts[i]);
  }
  printf("\n");
  break;

  case '2':
  ans = MOLToSMI(mol, DY_AROMATICITY | CANONICAL_ORDER);
  printf("%s\n", ans);
  break;
  }

  return 0;
}

