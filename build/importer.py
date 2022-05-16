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
        for nameSpell, currentSpell in self.sorted_dict.items():
            for nameClass, lvlClass in currentSpell["Niveau"].items():
                if ((nameClass in classList) and (not nameSpell in res)):
                    res[nameSpell] = currentSpell
        self.sorted_dict = res
    
    def sortSpellsListFromLevels(self, levelsList):
        res = {}
        for nameSpell, currentSpell in self.sorted_dict.items():
            for nameClass, lvlClass in currentSpell["Niveau"].items():
                if ((lvlClass in levelsList) and (not nameSpell in res)):
                    res[nameSpell] = currentSpell
        self.sorted_dict = res
    
    def sortSpellsListFromClassesAndLevels(self, levelsList, classList):
        res = {}
        for nameSpell, currentSpell in self.sorted_dict.items():
            for nameClass, lvlClass in currentSpell["Niveau"].items():
                if ((nameClass in classList) and (lvlClass in levelsList) and (not nameSpell in res)):
                    res[nameSpell] = currentSpell
        self.sorted_dict = res
    
    def printSortedSpellsNames(self):
        for nameSpell in self.sorted_dict:
            print(nameSpell, end=", ")
    
    def numberSpells(self):
        return len(self.data_dict)


loaderData = LoaderData()

loaderData.sortSpellsListFromClassesAndLevels([0], ["Bard"])
loaderData.printSortedSpellsNames()
print(loaderData.numberSpells())

