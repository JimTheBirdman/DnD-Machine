"""The D&D Machine is a companion to the beginner D&D player for creating new
    character sheets, updating current character sheets, dice "rolling",
    and random name generator for new DMs creating NPC's"""
    

"""
Currently using CHAR_NAME as a placeholder to represent the name on the character sheet
"""


from tkinter import *
from tkinter.filedialog import askopenfilename



# Assign functions to menu items
def OpenChar():
    #name = askopenfilename()
    path = filedialog.askopenfilename(initialdir="/", title="Select File",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
def About():
    print("This is a simple example of a menu")
def DiceBot():
    import DiceBot2
    print("Clickety Clack!")
def NameRandom():
    print("First Name", "Last Name")
def blanksheet():
    import blank_sheet
def rando_char():
    import rando   
    

# Create tkinter box    
root = Tk()
root.title("D&D Machine")
root.geometry("600x500")
root.configure(bg='grey')


# Create menu with options
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
submenu = Menu(filemenu)
submenu.add_command(label="Random Character", command=rando_char)
submenu.add_command(label="Blank Character Sheet", command=blanksheet)
filemenu.add_cascade(label="New Character", menu=submenu, underline=0)
filemenu.add_command(label="Open Existing Character", command=OpenChar)
#filemenu.add_command(label="Save", command=SaveChar)
#filemenu.add_command(label="Delete", command=DeleteChar)
#filemenu.add_command(label="Print", command=PrintChar)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

toolmenu = Menu(menu)
menu.add_cascade(label="Tools", menu=toolmenu)
toolmenu.add_command(label="DiceBot", command=DiceBot)
toolmenu.add_command(label="NPC Name Generator", command=NameRandom)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()