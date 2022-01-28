'''
Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s
, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
'''

import os

os.chdir("/home/guest/Downloads")

print(os.listdir())

with open("rosalind_ini6.txt","r+") as rosa:
    text = rosa.read()


word_list = text.split(" ")

dict_empty = {}

for i in word_list:
    if i not in dict_empty.keys():
        dict_empty[i] = 1

    else:
        dict_empty[i] = dict_empty[i] +1


for i,q in dict_empty.items():
    print(i,q)
