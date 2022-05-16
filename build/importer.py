# coding: utf-8


from encodings import utf_8
import json
from multiprocessing.dummy import Array

EnumClasses = ['Bard', 'Ens/Mag', 'Prê', 'Rôd', 'Cham', 'Con', 'Dru', 'Sor', 'Alch', 'Pal', 'Inq', 'Magus', 'San', 'Apal']

class LoaderData:
    json_data = open('Spells.json', encoding='utf-8')
    data_dict = json.load(json_data)
    sorted_dict = data_dict
    json_data.close()

    def __init__(self):
        pass

    def resetList(self):
        self.sorted_dict = self.data_dict
    
    def sortSpellsListFromClasses(self, classList):
        res = {}
        for nameSpell, currentSpell in self.sorted_dict:
            for nameClass, lvlClass in currentSpell["Niveau"]:
                if ((nameClass in classList) and (not nameSpell in res)):
                    res[nameClass] = currentSpell
        self.sorted_dict = res
    
    def sortSpellsListFromLevels(self, levelsList):
        res = {}
        for nameSpell, currentSpell in self.sorted_dict:
            for nameClass, lvlClass in currentSpell["Niveau"]:
                if ((lvlClass in levelsList) and (not nameSpell in res)):
                    res[nameClass] = currentSpell
        self.sorted_dict = res
    
    def sortSpellsListFromClassesAndLevels(self, classList, levelsList):
        res = {}
        for nameSpell, currentSpell in self.sorted_dict:
            for nameClass, lvlClass in currentSpell["Niveau"]:
                if ((nameClass in classList) and (lvlClass in levelsList) and (not nameSpell in res)):
                    res[nameClass] = currentSpell
        self.sorted_dict = res
    
    def printSortedSpellsNames(self):
        for nameSpell in self.sorted_dict:
            print(nameSpell, end=", ")
    
    def numberSpells(self):
        return len(self.data_dict)


loaderData = LoaderData()
for k in loaderData.sorted_dict:
    print(k)

# print(loaderData.sorted_dict)
# loaderData.sortSpellsListFromClassesAndLevels([0], ["Bard"])
# loaderData.sortSpellsListFromClasses(["Bard"])
# loaderData.printSortedSpellsNames()
# print(loaderData.numberSpells())

