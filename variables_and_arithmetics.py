#Variables and Some Arithmetic

import os           #Importing os library

os.chdir("C:/Users/jorle/Downloads/rosalind_files")             #Setting local working directory

with open("rosalind_ini2.txt","r") as texto:            #Importing dataset 
    dna = texto.read()                                  #Saving content to dna variable



a,b= dna.split(" ")                                     #Creating a list based on the input 

print(a,b)
print(int(a)**2+int(b)**2)                              #Adding the square of both values
