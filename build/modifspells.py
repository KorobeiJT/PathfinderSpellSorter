from encodings import *
import json
from multiprocessing.dummy import Array

# Ajoute la mention des sorts de niveau 0

json_data = open('spells.json', encoding='utf-8')
data_dict = json.load(json_data)

for i in data_dict["Spells"]:
    for currentClass in i["Levels"]:
        if not "Level" in currentClass:
            currentClass["Level"] = 0

with open('json_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_dict, outfile, ensure_ascii=False)