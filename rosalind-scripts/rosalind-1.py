with open("rosalind_dna.txt","r") as texto:
    dna = texto.read().upper()

A = dna.count("A")
C = dna.count("C")
G = dna.count("G")
T = dna.count("T")

print(A,C,G,T,sep=" ")
