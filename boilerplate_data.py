#!/usr/bin/env python3

import os

# create folders
root_path = '/Users/vpv/Desktop/myProject/'
folders = [
    'src/module/',
    'data/source',
    'data/draft',
    'data/clean',
    'generate/csv'
    'generate/chart'
    ]


for folder in folders:
    os.makedirs(os.path.join(root_path,folder))


# create files
files = [
    'requirement.txt',
    'config.py',
    'src/notebook.ipynb',
    '.gitignore',
]
    
for file in files: 
    open(root_path+file, 'w')
