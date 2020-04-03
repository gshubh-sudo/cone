import os
from shutil import copy2

rev=open("train.txt",'w')
with open('FS_train.txt', 'r') as file:
    content=file.readlines()
    for line in content:

#         type the diretory of your images instead here. 
        rev.write('C:/Users/team/Downloads/data/'+line[29:])

rev.close()
file.close()