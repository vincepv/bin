#!/usr/bin/env python3

import os
import time

name_client = input("Quel est le nom du client ?")
name_url = input("Quel est l'URL du client ? ")
parent_directory = "/Users/VPV/Desktop/"
get_time = time.strftime("%Y%m%d")
directory_created = ["/source", "/draft", "/import"]
path_generate =[]

# get name of each folder
for i in directory_created:
    path_generate.append(parent_directory+get_time+name_client+i)

# create folder
for x in path_generate:
    os.makedirs(x)

# create note.txt file
with open(parent_directory+get_time+name_client+'/note.txt', 'w') as f:
    template = '''
BESOIN

REMARQUES 

QUESTIONS

HYPOTHESE
'''
    f.write(get_time + ' Note import du client ' + name_client +" "+name_url + template)
    f.close()