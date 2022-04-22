import json
import numpy
import re

# Ajoute les descriptions des sorts au fichier json

file = open('name+Description.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()
json_data = open('spells.json', encoding='utf-8')
data_dict = json.load(json_data)
sorted_list = data_dict["Spells"]
json_data.close()

def getName(dict):
    return dict["Name"]

names = []
description = []
for line in lines:
    names.append(re.split(" \([A-Z]", line)[0])
    description.append(line.split("). ")[1])

for i in range(len(names)):
    for spell in sorted_list:
        if names[i] == spell["Name"]:
            spell["DescriptionSpell"] = description[i]
            break

data_dict["Spells"] = sorted_list

with open('spells2.json', 'w', encoding='utf-8-sig') as f:
    json.dump(data_dict, f)
    f.close()

# print(names)
# print(len(names))
# print(len(description))

# with open('json_data.json', 'w', encoding='utf-8') as outfile:
#     json.dump(data_dict, outfile, ensure_ascii=False)

