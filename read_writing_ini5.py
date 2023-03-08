#Ini5

import os           #Importing os library

os.chdir("C:/Users/jorle/Downloads/rosalind_files")             #Setting local working directory

with open("rosalind_ini5.txt","r") as texto:            #Importing dataset 
    dna = texto.read()                                  #Saving content to dna variable

dna = dna.split("\n")                       #Splitting the string on every linebreak

lista=[]
even_count_var=1

for i in dna:                           #Appending the even-numbered lines 
    if even_count_var%2==0:                          #Checking if the current line is even    
        lista.append(i)
    even_count_var=even_count_var+1


for i in lista:                         
    print(i)


#Comitting changes to test github and git