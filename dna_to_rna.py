#Ini5

import os           #Importing os library

os.chdir("C:/Users/jorle/Downloads/rosalind_files")             #Setting local working directory

with open("rosalind_rna.txt","r") as texto:            #Importing dataset 
    dna = texto.read()                                  #Saving content to dna variable




print(dna.replace("T","U"))
