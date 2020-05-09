from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

sequencia_dna = input(" Digite a Sequência de DNA: ")
#Fita de Dna:
dna = Seq(sequencia_dna, generic_dna)

#Fita de RNA mensageiro
rna = dna.complement().transcribe()

prot = rna.translate(to_stop=False, table=1)# adicionar tabela 

print('Fita de DNA: ', dna)
print('Fira de RNA: ', rna)
print("Fita de AA: ", prot)