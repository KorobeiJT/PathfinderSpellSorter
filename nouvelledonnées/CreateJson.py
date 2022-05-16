import json
import re
from os import listdir
from os.path import isfile, join
import shutil

name = "nouvelledonnées\liste de sorts.txt"

file = open(name, mode = 'r', encoding = 'utf-8')
lines = file.readlines()
file.close()

res = {}
wanted = ['Bard', 'Ens/Mag', 'Prê', 'Rôd', 'Cham', 'Con', 'Dru', 'Sor', 'Alch', 'Pal', 'Inq', 'Magus', 'San', 'Apal']

mypath = "nouvelledonnées\Spells"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def getClassesLevel(line):
    raw = re.search(r"\(([A-zÀ-ú/-]+ [0-9], )*[A-zÀ-ú/-]+ [0-9]\)", line).group(0)
    raw = raw[1:-1]
    classes = {}
    for level in raw.split(", "):
        if level.split(' ')[0] in wanted:
            classes[level.split(' ')[0]] = int(level.split(' ')[1])
    return classes


def getInfoFromFile(mypath,namef,curSpell):
    fileSpell = open(mypath+'\\'+namef+'.txt', mode = 'r', encoding = 'utf-8')
    linesSpell = fileSpell.readlines()
    fileSpell.close()
    for lineSpell in linesSpell:
        lineSpell = lineSpell.rstrip('\n')
        lineSpell = lineSpell.rstrip()
        if("[École]" in lineSpell):
            curSpell["École"] = lineSpell[len("[École] "):]
        if("[Temps d'incantation]" in lineSpell):
            curSpell["Temps d'incantation"] = lineSpell[len("[Temps d'incantation] "):]
        if("[Composantes]" in lineSpell):
            curSpell["Composantes"] = lineSpell[len("[Composantes] "):]
        if("[Portée]" in lineSpell):
            curSpell["Portée"] = lineSpell[len("[Portée] "):]
        if("[Cible]" in lineSpell):
            curSpell["Cible"] = lineSpell[len("[Cible] "):]
        if("[Durée]" in lineSpell):
            curSpell["Durée"] = lineSpell[len("[Durée] "):]
        if("[Jet de sauvegarde]" in lineSpell):
            curSpell["Jet de sauvegarde"] = lineSpell[len("[Jet de sauvegarde] "):]
        if("[Résistance à la magie]" in lineSpell):
            curSpell["Résistance à la magie"] = lineSpell[len("[Résistance à la magie] "):]
    return curSpell

def setWhatIsUnset(curSpell):
    if(not "École" in curSpell.keys()):
        curSpell["École"] = "Not Define"
    if(not "Temps d'incantation" in curSpell.keys()):
        curSpell["Temps d'incantation"] = "Not Define"
    if(not "Composantes" in curSpell.keys()):
        curSpell["Composantes"] = "Not Define"
    if(not "Portée" in curSpell.keys()):
        curSpell["Portée"] = "Not Define"
    if(not "Durée" in curSpell.keys()):
        curSpell["Durée"] = "Not Define"
    if(not "Jet de sauvegarde" in curSpell.keys()):
        curSpell["Jet de sauvegarde"] = "Not Define"
    if(not "Résistance à la magie" in curSpell.keys()):
        curSpell["Résistance à la magie"] = "Not Define"
    return curSpell

for line in lines:
    curSpell = {}

    name = line.split("]] ")[0][2:]
    if ("|" in name):
        namef = name.split("|")[0]
        name = name.split("|")[1]
    else:
        namef = name

    curSpell["Niveau"] = getClassesLevel(line)
    if (namef+'.txt' in onlyfiles):
        curSpell = getInfoFromFile(mypath,namef,curSpell)
    curSpell = setWhatIsUnset(curSpell)
    curSpell["Description"] = line.split("). ")[1].rstrip()
    curSpell["Lien"] = "https://www.pathfinder-fr.org/Wiki/Pathfinder-RPG."+namef+".ashx"
    res[name] = curSpell
with open('Spells.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False)
    f.close()