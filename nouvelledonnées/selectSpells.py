import json
import re
from os import listdir
from os.path import isfile, join
import shutil

file = open('liste de sorts.txt', mode = 'r', encoding = 'utf-8')
lines = file.readlines()
file.close()

mypath = "C:\\Users\lapii\Desktop\\nouvelledonnées\Pathfinder-RPG"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

names = []
for line in lines:
    name = line.split("]] ")[0][2:]
    if ("|" in name):
        name = name.split("|")[0]
    names.append(name)
    print(name, end= ' ')

src = mypath
dst = "C:\\Users\lapii\Desktop\\nouvelledonnées\Spells"

for file in names:
    sf = src +"\\" + file + ".txt"
    df = dst +"\\" + file + ".txt"
    shutil.copy(sf,df)

