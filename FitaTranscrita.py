from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

#Fita de DNA:
dna_seq = input("Digite a sequência de DNA: ")
dna = Seq(dna_seq, generic_dna)

#Fita de RNA:
rna = dna.complement().transcribe()

#Imprime DNA
print('Fita de DNA: ', dna)

#imprime RNA:
print("Fita de RNA:", rna)