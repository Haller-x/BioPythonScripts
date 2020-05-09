from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
matrizes = {}
matriz_de_escolhas = [matlist.benner6, matlist.benner22, matlist.benner74, matlist.blosum100, matlist.blosum30, matlist.blosum35, matlist.blosum40, matlist.blosum45, matlist.blosum50,matlist.blosum55, matlist.blosum60, matlist.blosum62, matlist.blosum65, matlist.blosum70, matlist.blosum75, matlist.blosum80, matlist.blosum85, matlist.blosum90, matlist.blosum95,matlist.feng, matlist.fitch, matlist.genetic, matlist.gonnet, matlist.grant, matlist.ident, matlist.johnson, matlist.levin, matlist.mclach,matlist.miyata, matlist.nwsgappep, matlist.pam120, matlist.pam180, matlist.pam250, matlist.pam30, matlist.pam300, matlist.pam60, matlist.pam90, matlist.rao, matlist.risler, matlist.structure]
#matrizes possiveis
for i in range(len(matlist.available_matrices)):
    matrizes[i+1] = matriz_de_escolhas[i]
matriz_escolhida  = int(input('''Escolha uma matriz: \n1: benner6\n2: benner22\n3: benner74\n4: blosum100\n5: blosum30\n6: blosum35\n7: blosum40\n8: blosum45\n9: blosum50\n10: blosum55\n11: blosum60\n12: blosum62\n13: blosum65\n14: blosum70\n15: blosum75\n16: blosum80\n17: blosum85\n18: blosum90\n19: blosum95\n20: feng\n21: fitch\n22: genetic\n23: gonnet\n24: grant\n25: ident\n26: johnson\n27: levin\n28: mclach\n29: miyata\n30: nwsgappep\n31: pam120\n32: pam180\n33: pam250\n34: pam30\n35: pam300\n36: pam60\n37: pam90\n38: rao\n39: risler\n40: structure\nMatriz escolhida: '''))
seq1= input("Digite a sequência 1: ")
seq2= input("Digite a sequência 2: ")
matriz = matrizes[matriz_escolhida]
alinhamento =  pairwise2.align.globaldx(seq1,seq2,matriz)
print(pairwise2.format_alignment(*alinhamento[0]))