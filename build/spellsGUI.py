from pathlib import Path

from numpy import column_stack

from importer import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkwidgets import CheckboxTreeview

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



class SpellGUI:
    importer = LoaderData()
    classList = []
    lvlList = []

    def __init__(self):
        self.importer = LoaderData()
        
    def OpenGUI(self):
        self.root = Tk()
        self.root.geometry("1000x400")

        #Wrappers
        wrapperSearch = LabelFrame(self.root, text = "Recherche")
        wrapperData = LabelFrame(self.root, text = "Résultats")
        wrapperDeck = LabelFrame(self.root, text = "Deck")

        #DataTreeview
        self.columnsData = ("Name","School","Description")
        self.tree = CheckboxTreeview(wrapperData, columns=self.columnsData)
        #Column
        self.tree.column('#0', width=75, minwidth=25)
        self.tree.column("Name", width=120)
        self.tree.column("School", width=120)
        self.tree.column("Description", width=670)

        self.tree.heading('#0',text = '', anchor=W)
        self.tree.heading("Name",text = "Nom")
        self.tree.heading("School",text = "Ecole")
        self.tree.heading("Description",text = "Description")

        #DeckTreeView
        self.columnsDeck = ("Name","School","Incantation","Range","Target","Duration","Save","SpellResistance","Components","Description","Link")
        self.deck = CheckboxTreeview(wrapperDeck, columns=self.columnsDeck)
        self.deck.column('#0', width=50, minwidth=25)
        self.deck.heading('#0',text = '', anchor=W)
        for i in self.columnsDeck:
            self.deck.column(i, width=80)
            self.deck.heading(i, text=i, command= lambda c=i: self.change_width(c))

        #Contenu
        self.importer.sortSpellsListFromClassesAndLevels(self.classList, self.lvlList)
        self.createParentClass()
        self.addSpell()
        self.transformLevelsIntoSpec()
        
        ### Packing ###
        #Wrappers
        wrapperSearch.pack(fill="both", expand= "yes", padx= 20, pady=10)
        wrapperData.pack(fill="both", expand= "yes", padx= 20, pady=10)
        wrapperDeck.pack(fill="both", expand= "yes", padx= 20, pady=10)
        #treeview
        self.tree.pack()
        self.deck.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.importer.resetList())
        self.root.mainloop()
    
    def createParentClass(self):
        ## Crée les parents "classes"
        for className in self.classList:
            self.tree.insert(parent='', iid=className, index='end', text = className, values = ('','','',''))
            ## Crée les parents "niveaux"
            for level in self.lvlList:
                self.tree.insert(parent=className, iid=className+';'+str(level), index='end', text = level, values = ('','','',''))
    
    def change_width(self, col):
        if(col == "Description" or col == "Link"):
            for i in self.columnsDeck:
                self.deck.column(i, width=58)
            self.deck.column(col, width=300)
        else:
            for i in self.columnsDeck:
                self.deck.column(i, width=74)
            self.deck.column(col, width=140)

    def addSpell(self):
        for spell in self.importer.sorted_list:
            for curClass in spell["Levels"]:
                if (curClass["List"] in self.classList and curClass["Level"] in self.lvlList):
                    self.tree.insert(parent=curClass["List"]+';'+str(curClass["Level"]),
                    iid=curClass["List"]+';'+str(curClass["Level"])+';'+str(len(self.tree.get_children(curClass["List"]+';'+str(curClass["Level"])))),
                    index='end', values = (spell["Name"],spell["School"],spell["DescriptionSpell"],''))


    def transformLevelsIntoSpec(self):
        for spell in self.importer.sorted_list:
            res = ""
            for curClass in spell["Levels"]:
                if (curClass["List"] in self.classList):
                    res += curClass["List"] + ' ' + str(curClass["Level"]) + ' ; '
            spell["Spec"] = res



    def addClass(self, className):
        if(not className in self.classList):
            self.classList.append(className)
            print(self.classList)
            return True
        else:
            self.classList.remove(className)
            print(self.classList)
            return False
    
    def addLevel(self, level):
        if(not level in self.classList):
            self.lvlList.append(level)
            return True
        else:
            self.lvlList.remove(level)
            return False

sgui = SpellGUI()
sgui.addClass("bard")
sgui.addLevel(0)
sgui.OpenGUI()