import os

os.chdir(r"C:\Users\jorle\Downloads\Python-data-test\rosalind-exercises")


with open("rosalind_rna.txt","r") as texto:
    rna = texto.read()


print(rna.replace("T","U"))


