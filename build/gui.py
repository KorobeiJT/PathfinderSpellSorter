
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from numpy import integer

# from tkinter import *
# Explicit imports to satisfy Flake8
from spellsGUI import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def pressClass(button, className):
    if(sGUI.addClass(className)):
        button.configure(relief="sunken")
    else:
        button.configure(relief="flat")

def pressLevel(level1, level2):
    sGUI.lvlList = []
    for i in range(level1, level2+1):
        sGUI.addLevel(i)
    viewLvl.configure(text = sGUI.lvlList)
    
        
    


sGUI = SpellGUI()

window = Tk()

window.geometry("1200x370")
window.configure(bg = "#f3efe2")


canvas = Canvas(
    window,
    bg = "#f3efe2",
    height = 630,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sGUI.OpenGUI(),
    relief="flat"
)
button_1.place(
    x=880.0,
    y=278.0,
    width=240.0,
    height=50.0
)

viewLvl = Label(
    text = ""
)
viewLvl.place(
    x=525.0,
    y=278.0,
    width=150.0,
    height=50.0
)

button_4 = Button(
    text = "Valider les niveaux",
    command=lambda: pressLevel(clicked_1.get(), clicked_2.get()),
)
button_4.place(
    x=350.0,
    y=278.0,
    width=150.0,
    height=50.0
)
option = [0,1,2,3,4,5,6,7,8,9]
clicked_1 = IntVar()
entry_1 = OptionMenu( window , clicked_1 , *option )
entry_1.place(
    x=80.0,
    y=278.0,
    width=115.0,
    height=48.0
)

clicked_2 = IntVar()
entry_2 = OptionMenu( window , clicked_2 , *option )
entry_2.place(
    x=205.0,
    y=278.0,
    width=115.0,
    height=48.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_5,"witch"),
    relief="flat"
)
button_5.place(
    x=1040.0,
    y=158.0,
    width=80.0,
    height=80.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_6,"ranger"),
    relief="flat"
)
button_6.place(
    x=880.0,
    y=158.0,
    width=80.0,
    height=80.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_7,"oracle"),
    relief="flat"
)
button_7.place(
    x=720.0,
    y=158.0,
    width=80.0,
    height=80.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_8,"cleric"),
    relief="flat"
)
button_8.place(
    x=560.0,
    y=158.0,
    width=80.0,
    height=80.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_9,"paladin"),
    relief="flat"
)
button_9.place(
    x=400.0,
    y=158.0,
    width=80.0,
    height=80.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_10,"magus"),
    relief="flat"
)
button_10.place(
    x=240.0,
    y=158.0,
    width=80.0,
    height=80.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_11,"inquisitor"),
    relief="flat"
)
button_11.place(
    x=80.0,
    y=158.0,
    width=80.0,
    height=80.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_12,"druid"),
    relief="flat"
)
button_12.place(
    x=1040.0,
    y=38.0,
    width=80.0,
    height=80.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_13,"summoner"),
    relief="flat"
)
button_13.place(
    x=880.0,
    y=38.0,
    width=80.0,
    height=80.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_14,"shaman"),
    relief="flat"
)
button_14.place(
    x=720.0,
    y=38.0,
    width=80.0,
    height=80.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_15,"bard"),
    relief="flat"
)
button_15.place(
    x=560.0,
    y=38.0,
    width=80.0,
    height=80.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_16,"sorcerer-wizard"),
    relief="flat"
)
button_16.place(
    x=400.0,
    y=38.0,
    width=80.0,
    height=80.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_17,"antipaladin"),
    relief="flat"
)
button_17.place(
    x=240.0,
    y=38.0,
    width=80.0,
    height=80.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth = 5,
    highlightthickness=0,
    command=lambda: pressClass(button_18,"alchemist"),
    relief="flat"
)
button_18.place(
    x=80.0,
    y=38.0,
    width=80.0,
    height=80.0
)

window.resizable(False, False)
window.mainloop()