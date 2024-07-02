#Script to calculate the GC content of a given FASTA sequence


import os

#Changing the current computer folder 
os.chdir(r"C:\\Users\\jorle\\Downloads\\Python-data-test\\rosalind-exercises")              


dna_dict = {}


#Creating dictionary with the DNA sequences

##The Fasta headers are the keys and the DNA sequences are the values

with open("rosalind_gc.txt","r") as texto:
    for i in texto:

        i =  i.replace("\n","")
        
        if i.startswith(">"):                               #Checking if the line is a FASTA header
            i = i.replace(">","")                           #Removing > characters from the header
            
            dict_key = i                                    #Storing the current i value
                                                            ##This is used to ensure all the DNA sequence lines will be stored in this value
            
            dna_dict[i]=""                                  #Creating new dict key based on the current i value

        else:                                               #while the loop finds lines different from >, they are added to the dict value
            dna_dict[dict_key] = dna_dict[dict_key] + i


print(dna_dict)


#GC sum
gc_greatest_sum = 0
gc_list = []

for i in dna_dict.keys():
    gc_sum = dna_dict[i].count("G")+dna_dict[i].count("C")
    gc_content = round(gc_sum/len(dna_dict[i]),6)*100
    
    print(i,gc_content)

    if gc_content > gc_greatest_sum:
        gc_greatest_sum = gc_content
       
        gc_list = [i,gc_content]


for i in gc_list:
    print(i)
    