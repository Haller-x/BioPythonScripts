from Bio import pairwise2

def pairwise_seq(seq1,seq2,match_pesos=5,mismatch_pesos=-4,gap_abertura=-2,gap_extensao=-0.5):
    align= pairwise2.align.globalms(seq1,seq2,match_pesos,mismatch_pesos,gap_abertura,gap_extensao)
    return (pairwise2.format_alignment(*align[0]))

print(pairwise_seq("ATGCCAGTTTCACCAGGA","AAGTCCCATGATGAT"))