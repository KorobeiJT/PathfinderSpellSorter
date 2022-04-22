# coding: utf-8


from encodings import utf_8
import json
from multiprocessing.dummy import Array

class LoaderData:
    json_data = open('spells2.json', encoding='utf-8')
    data_dict = json.load(json_data)
    sorted_list = data_dict["Spells"]

    def __init__(self):
        pass

    def resetList(self):
        self.sorted_list = self.data_dict["Spells"]
    
    def getSelectedSchool(self, tabSchool):
        res=[]
        for currentSchool in tabSchool:
            for currentSpell in self.sorted_list:
                if(currentSpell["School"] == currentSchool):
                    res.append(currentSpell["Name"])
        return res

    def getListSchool(self):
        res = []
        for currentSpell in self.sorted_list:
            if(not (currentSpell["School"] in res)):
                res.append(currentSpell["School"])
        return res
    
    def getListClasses(self):
        res = []
        for currentSpell in self.sorted_list:
            for currentLevel in currentSpell["Levels"]:
                if(not (currentLevel["List"] in res)):
                    res.append(currentLevel["List"])
        return res
    
    def sortSpellsListFromClasses(self, classesList):
        res = []
        for currentSpell in self.sorted_list:
            for currentClass in currentSpell["Levels"]:
                if ((currentClass["List"] in classesList) and (not currentSpell in res)):
                    res.append(currentSpell)
        self.sorted_list = res
    
    def sortSpellsListFromLevels(self, levelsList):
        res = []
        for currentSpell in self.sorted_list:
            for currentClass in currentSpell["Levels"]:
                if ((currentClass["Level"] in levelsList) and (not currentSpell in res)):
                    res.append(currentSpell)
        self.sorted_list = res
    
    def sortSpellsListFromClassesAndLevels(self, classList, levelsList):
        res = []
        try:
            for currentSpell in self.sorted_list:
                for currentClass in currentSpell["Levels"]:
                    if ((currentClass["Level"] in levelsList) and (currentClass["List"] in classList) and (not currentSpell in res)):
                        res.append(currentSpell)
        except KeyError:
            print(currentSpell["Name"])
        self.sorted_list = res
    
    def printSortedSpellsNames(self):
        for currentSpell in self.sorted_list:
            print(currentSpell["Name"], end=", ")
    
    def numberSpells(self):
        return len(self.data_dict["Spells"])


# loaderData = LoaderData()
# loaderData.sortSpellsListFromClassesAndLevels([0], ["bard"])
# print(loaderData.printSelectedSchool(["Conjuration","Illusion"]))
# print(loaderData.getListSchool())
# print(loaderData.getListClasses())
# loaderData.sortSpellsListFromClasses(["bard"])
# loaderData.printSortedSpellsNames()
# print(loaderData.numberSpells())

