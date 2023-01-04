import os                       #Importing library to deal with the operational system

os.chdir("/home/jorley/Downloads")          #Setting the working directory to the folder with the file we will be using

with open("rosalind_dna(5).txt","r") as texto:      #Opening text file content
    dna = texto.read()                              #Saving its content to a variable 


a = dna.count("A")                          #Counting the number of occurrences of A in the string
c = dna.count("C")
g = dna.count("G")
t = dna.count("T")

print(a,c,g,t,sep=" ")                  #Printing the count for each nucleotide in the string
    
