"""Creates a new character sheet with stats filled from the New Character Generator"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

# Create tkinter box    
gui = Tk()
gui.title("UNNAMED CHARACTER")
gui.geometry("1200x700")
gui.configure(bg='light blue')


def save_char():
    print("CHAR_NAME", "has been updated")
def save_as():
    path = filedialog.asksaveasfile(initialdir="/", title="Save file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    """a = gui
    file = asksaveasfile(defaultextension=".txt")
    file.write(a)
    refresh()"""
    print("CHAR_NAME", "has been saved")
def print_char():
    print("Printing...")    
def delete_char():
    # Provide additional window informing user that this will delete current 
    # character and confirm they wish to proceed
    print("CHAR_NAME", "has been deleted")    
def refresh():
    gui.withdraw()

# create header labels for categories and stats
ttk.Label(gui, text = "      ", font = "Helvetica 12 bold", background='light blue').grid(column = 0, row = 1, padx = 15, pady = 15)
ttk.Label(gui, text = "      ", font = "Helvetica 12 bold", background='light blue').grid(column = 1, row = 1, padx = 15, pady = 15)
ttk.Label(gui, text = "      ", font = "Helvetica 12 bold", background='light blue').grid(column = 2, row = 1, padx = 15, pady = 15)
ttk.Label(gui, text = "      ", font = "Helvetica 12 bold", background='light blue').grid(column = 3, row = 1, padx = 15, pady = 15)
ttk.Label(gui, text = "      ", font = "Helvetica 12 bold", background='light blue').grid(column = 4, row = 1, padx = 15, pady = 15)
ttk.Label(gui, text = "      ", font = "Helvetica 12 bold", background='light blue').grid(column = 5, row = 1, padx = 15, pady = 15)
ttk.Label(gui, text = "      ", font = "Helvetica 12 bold", background='light blue').grid(column = 6, row = 1, padx = 15, pady = 15)
ttk.Label(gui, text = "      ", font = "Helvetica 12 bold", background='light blue').grid(column = 7, row = 1, padx = 15, pady = 15)
# label text for each component of the character sheet
ttk.Label(gui, text = "Race: ",
              font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 3, padx = 15, pady = 5)                                                                      
ttk.Label(gui, text = "Class: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 4, padx = 15, pady = 5)                                                                                        
ttk.Label(gui, text = "Alignment: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 5, padx = 15, pady = 5)
ttk.Label(gui, text = "--------------------",
          font = ("Helvetica 12 bold"), background='light blue').grid(column = 0,
          row = 6, padx = 15, pady = 5) 
ttk.Label(gui, text = "--------------------",
          font = ("Helvetica 12 bold"), background='light blue').grid(column = 1,
          row = 6, padx = 15, pady = 5)                                                                       
ttk.Label(gui, text = "Strength: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 7, padx = 15, pady = 5)  
ttk.Label(gui, text = "Dexterity: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 8, padx = 15, pady = 5) 
ttk.Label(gui, text = "Constitution: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 9, padx = 15, pady = 5)
ttk.Label(gui, text = "Charisma: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 10, padx = 15, pady = 5)
ttk.Label(gui, text = "Intelligence: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 11, padx = 15, pady = 5)
ttk.Label(gui, text = "Wisdom: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 12, padx = 15, pady = 5) 
ttk.Label(gui, text = "--------------------",
          font = ("Helvetica 12 bold"), background='light blue').grid(column = 0,
          row = 13, padx = 15, pady = 5)
ttk.Label(gui, text = "Armor Class: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 14, padx = 15, pady = 5)  
ttk.Label(gui, text = "Languages: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 15, padx = 15, pady = 5)   
ttk.Label(gui, text = "Attacks/Spells: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 16, padx = 15, pady = 5)
ttk.Label(gui, text = "",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 0,
          row = 17, padx = 15, pady = 5)                                                          
ttk.Label(gui, text = "Level: ",
          font = ("Helvetica 12 bold"), background='light blue').grid(column = 3,
          row = 3, padx = 5, pady = 5)
ttk.Label(gui, text = ">> Ability Mods <<",
          font = ("Helvetica 12 bold"), background='light blue').grid(column = 3,
          row = 6, padx = 15, pady = 5) 
ttk.Label(gui, text = "Strength: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 3,
          row = 7, padx = 15, pady = 5)
ttk.Label(gui, text = "Dexterity: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 3,
          row = 8, padx = 15, pady = 5)  
ttk.Label(gui, text = "Constitution: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 3,
          row = 9, padx = 15, pady = 5) 
ttk.Label(gui, text = "Charisma: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 3,
          row = 10, padx = 15, pady = 5)  
ttk.Label(gui, text = "Intelligence: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 3,
          row = 11, padx = 15, pady = 5)   
ttk.Label(gui, text = "Wisdom: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 3,
          row = 12, padx = 15, pady = 5) 
ttk.Label(gui, text = "--------------------",
          font = ("Helvetica 12 bold"), background='light blue').grid(column = 3,
          row = 13, padx = 15, pady = 5)
ttk.Label(gui, text = "Proficiencies: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 3,
          row = 15, padx = 15, pady = 5) 
ttk.Label(gui, text = "Equipment/Notes: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 3,
          row = 16, padx = 15, pady = 5)                                                                                  
ttk.Label(gui, text = "XP: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 5,
          row = 3, padx = 15, pady = 5)                                                                      
ttk.Label(gui, text = "Current HP: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 5,
          row = 4, padx = 15, pady = 5)                                                                      
ttk.Label(gui, text = "Temp HP: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 5,
          row = 5, padx = 15, pady = 5)                                                                      
ttk.Label(gui, text = "HP Max: ",
          font = ("Helvetica 10 bold"), background='light blue').grid(column = 5,
          row = 6, padx = 15, pady = 5)
ttk.Label(gui, text = "--------------------",
          font = ("Helvetica 12 bold"), background='light blue').grid(column = 5,
          row = 7, padx = 15, pady = 5)
     
                                                                      
# Create blank text boxes for values to be added by user                                                                     
box_race = Text(gui, width=12, height=1, font=("Helvetica", 12))
box_race.grid(column = 1, row = 3) 

box_class = Text(gui, width=12, height=1, font=("Helvetica", 12))
box_class.grid(column = 1, row = 4) 

box_alignment = Text(gui, width=15, height=1, font=("Papyrus", 12))
box_alignment.grid(column = 1, row = 5) 

box_str = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_str.grid(column = 1, row = 7) 

box_dex = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_dex.grid(column = 1, row = 8) 

box_const = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_const.grid(column = 1, row = 9) 

box_charisma = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_charisma.grid(column = 1, row = 10) 

box_intel = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_intel.grid(column = 1, row = 11) 

box_wisdom = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_wisdom.grid(column = 1, row = 12) 

box_armor_class = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_armor_class.grid(column = 1, row = 14)                                                 

box_languages = Text(gui, width=30, height=4, font=("Helvetica", 12))
box_languages.grid(column = 1, row = 15, pady=10) 

box_attacks = Text(gui, width=35, height=8, font=("Helvetica", 12))
box_attacks.grid(column = 1, row = 16)                              

box_level = Text(gui, width=3, height=1, font=("Helvetica", 20))
box_level.grid(column = 4, row = 3)

box_str_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_str_mod.grid(column = 4, row = 7) 

box_dex_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_dex_mod.grid(column = 4, row = 8) 

box_const_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_const_mod.grid(column = 4, row = 9) 

box_charisma_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_charisma_mod.grid(column = 4, row = 10) 

box_intel_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_intel_mod.grid(column = 4, row = 11) 

box_wisdom_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_wisdom_mod.grid(column = 4, row = 12)

box_prof = Text(gui, width=30, height=4, font=("Helvetica", 12))
box_prof.grid(column = 4, row = 15)

box_equip = Text(gui, width=35, height=10, font=("Helvetica", 12))
box_equip.grid(column = 4, row = 16)

box_XP = Text(gui, width=7, height=1, font=("Helvetica", 12))
box_XP.grid(column = 6, row = 3) 

box_HP_current = Text(gui, width=7, height=1, font=("Helvetica", 12))
box_HP_current.grid(column = 6, row = 4) 

box_HP_temp = Text(gui, width=7, height=1, font=("Helvetica", 12))
box_HP_temp.grid(column = 6, row = 5) 

box_HP_maxi = Text(gui, width=7, height=1, font=("Helvetica", 12))
box_HP_maxi.grid(column = 6, row = 6) 


# create dropdown file menu                                                                      
menu = Menu(gui)
gui.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=save_char)
filemenu.add_command(label="Save As", command=save_as)
filemenu.add_command(label="Delete", command=delete_char)
filemenu.add_command(label="Print", command=print_char)
filemenu.add_separator()
filemenu.add_command(label="Close", command=gui.destroy)                                                                      

                                                                        
gui.mainloop()
