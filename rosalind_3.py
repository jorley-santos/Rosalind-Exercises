import os

os.chdir(r"C:\\Users\\jorle\\Downloads\\Python-data-test\\rosalind-exercises")


with open("rosalind_revc.txt","r") as texto:
    dna = texto.read()


print(dna)

dna_rev = ""

for i in dna:
    if i =="A":
        dna_rev +="T"
    if i =="T":
        dna_rev +="A"
    if i =="G":
        dna_rev +="C"
    if i =="C":
        dna_rev +="G"

print(dna_rev[::-1])