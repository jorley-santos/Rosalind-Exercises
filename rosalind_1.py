import os

os.chdir(r"C:\Users\jorle\Downloads\Python-data-test\rosalind-exercises")


with open("rosalind_dna_1.txt","r") as texto:
    dna = texto.read()

dna_dict = {"A":0,"T":0,"C":0,"G":0}



dna_length = len(dna)


for i in dna.upper():
    if i =="A":
        dna_dict["A"] += 1

    if i =="T":
        dna_dict["T"] += 1

    if i =="C":
        dna_dict["C"] += 1

    if i =="G":
        dna_dict["G"] += 1


gc_content = (dna_dict["G"] + dna_dict["C"])/dna_length

print(f'Adenine: {dna_dict["A"]} | Thymine: {dna_dict["T"]} | Guanine: {dna_dict["G"]} | Cytosine: {dna_dict["C"]}')

print(f"\nThe GC content of the given DNA sequence is",round(gc_content*100,2),"%")


