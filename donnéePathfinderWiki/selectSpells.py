import json
import re
from os import listdir
from os.path import isfile, join
import shutil

file = open('name+Description.txt', mode = 'r', encoding = 'utf-8')
lines = file.readlines()
file.close()

mypath = "C:\\Users\lapii\Desktop\donnéePathfinderWiki\PFRPGlower"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

names = []
for line in lines:
    name = line.split(" (")[0]
    name = name.lower()
    if "'" in name:
        name = name.replace("'","")
    if "/" in name:
        name = name.replace("/","")
    if "sort " + name + ".txt" in onlyfiles:
        names.append("sort " + name)
    elif name+".txt" in onlyfiles:
        names.append(name)

src = "C:\\Users\lapii\Desktop\donnéePathfinderWiki\PFRPGlower"
dst = "C:\\Users\lapii\Desktop\donnéePathfinderWiki\Spells"

for file in names:
    sf = src +"\\" +file + ".txt"
    df = dst +"\\" +file.lower() + ".txt"
    shutil.copy(sf,df)

