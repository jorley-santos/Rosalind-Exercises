#Ini4

import os           #Importing os library

os.chdir("C:/Users/jorle/Downloads/rosalind_files")             #Setting local working directory

with open("rosalind_ini4.txt","r") as texto:            #Importing dataset 
    dna = texto.read()                                  #Saving content to dna variable


a,b = dna.split()
a,b = int(a),int(b)


var= 0
for i in range(a,b+1):
    if i%2!=0:
        var=var+i


print(var)
