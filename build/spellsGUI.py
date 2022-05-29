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

        buttonPutInDeck = tk.Button(wrapperData, text="Insérer sélection", command=self.putInDeck)


        #DeckTreeView
        self.columnsDeck = ("Name","School","Incantation","Range","Target","Duration","Save","SpellResistance","Components","Description","Link")
        self.deck = ttk.Treeview(wrapperDeck, columns=self.columnsDeck)
        self.deck.column('#0', width=50, minwidth=25)
        self.deck.heading('#0',text = '', anchor=W)
        for i in self.columnsDeck:
            self.deck.column(i, width=80)
            self.deck.heading(i, text=i, command= lambda c=i: self.change_width(c))

        #Contenu
        self.importer.sortSpellsListFromClassesAndLevels(self.classList, self.lvlList)
        self.createParentClass()
        self.addSpell()
        # self.transformLevelsIntoSpec()
        
        ### Packing ###
        #Wrappers
        wrapperSearch.pack(fill="both", expand= "yes", padx= 20, pady=10)
        wrapperData.pack(fill="both", expand= "yes", padx= 20, pady=10)
        wrapperDeck.pack(fill="both", expand= "yes", padx= 20, pady=10)
        #treeview
        self.tree.pack()
        buttonPutInDeck.pack()
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
        
    def putInDeck(self):
        # print(self.tree.get_checked())
        name_list = [self.tree.item(spell)["values"][0] for spell in self.tree.get_checked()]
        for name in name_list:
            for spell in self.importer.sorted_dict:
                if spell["Name"] == name:
                    self.deck.insert(spell["Name"])
                    # insertSpell(spell)
    
    # def insertSpellInDeck(self, spell):
    #     self.deck.insert(values=(spell["Name"],spell["School"],self.getCastingTime(spell),
    #     self.getRange(spell),spell["Target"]["Value"],spell[""],spell[""],spell[""],spell[""],spell[""],spell[""]))
    
    # def getCastingTime(self, spell):
    #     if("Unit" not in spell["CastingTime"]):
    #         return "1 action simple"
    #     else:
    #         return str(spell["CastingTime"]["Value"]) + ' ' + str(spell["CastingTime"]["Unit"])

    # def getRange(self, spell):
    #     if "SpecificValue" not in spell["Range"]:
    #         return spell["Range"]["Unit"]
    #     else:
    #         return str(1.5 * spell["Range"]["SpecificValue"]) + ' m'
        

    def addSpell(self):
        for spellName, spell in self.importer.sorted_dict.items():
            for className, levelClass in spell["Niveau"].items():
                if (className in self.classList and levelClass in self.lvlList):
                    self.tree.insert(parent=className+';'+str(levelClass),
                    iid=className+';'+str(levelClass)+';'+str(len(self.tree.get_children(className+';'+str(levelClass)))), #idd = class;level;"taille de la section 'class;level'"
                    index='end', values = (spellName,spell["École"],spell["Description"],''))


    # def transformLevelsIntoSpec(self):
    #     for spellName, spell in self.importer.sorted_dict.items():
    #         res = ""
    #         for className, classLevel in spell["Niveau"]:
    #             if (className in self.classList):
    #                 res += className + ' ' + str(classLevel) + ' ; '
    #         spell["Spec"] = res



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

# sgui = SpellGUI()
# sgui.addClass("Bard")
# sgui.addLevel(0)
# sgui.OpenGUI()