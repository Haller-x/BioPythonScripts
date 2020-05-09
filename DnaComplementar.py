from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

#Fita molde
molde = input("Digite a fita molde: ")
dnaM = Seq(molde, generic_dna)

#Fita complementar
dnaC = dnaM.complement()

#Imprime a fita molde
print('Fita Molde :', dnaM)

#Imprime a fita complementar
print('Fita Complementar :', dnaC)