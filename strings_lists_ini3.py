#Variables and Some Arithmetic

import os           #Importing os library

os.chdir("C:/Users/jorle/Downloads/rosalind_files")             #Setting local working directory

with open("rosalind_ini3.txt","r") as texto:            #Importing dataset 
    dna = texto.read()                                  #Saving content to dna variable


index=dna.split("\n")[1]

index = index.split(" ")

i0 = int(index[0])
i1 = int(index[1])+1
i2 = int(index[2])
i3 = int(index[3])+1

print(dna)
print(index)
print(dna[i0:i1]+" "+dna[i2:i3])
