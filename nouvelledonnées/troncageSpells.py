import json
from operator import indexOf
import re
from os import listdir
from os.path import isfile, join
import shutil

mypath = "C:\\Users\lapii\Desktop\\nouvelledonnées\Spells"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

cpt = 0
for name in onlyfiles:
    file = open(mypath+'\\'+name, mode = 'r', encoding = 'utf-8')
    lines = file.readlines()
    file.close()
    for line in lines:
        if line[:len("'''École'''")] == "'''École'''":
            lines = lines[lines.index(line):]
            break
    for line in lines:
        if line[:len("'''")] != "'''":
            lines = lines[:lines.index(line)]
            break
    for line in lines:
        print(line, end='')

    file = open(mypath+'\\'+name, mode = 'w', encoding = 'utf-8')
    for line in lines:
        file.write(line)
    file.close()