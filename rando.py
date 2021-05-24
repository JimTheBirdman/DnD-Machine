import races
import Classes
import functions
import armor
import weapons
from random import choice, randint
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font

ALIGNMENT = [
    "Chaotic Good",
    "Chaotic Neutral",
    "Chaotic Evil",
    "Neutral Good",
    "True Neutral",
    "Neutral Evil",
    "Lawful Good",
    "Lawful Neutral",
    "Lawful Evil"
]
LANGUAGES = [
    "Common",
    "Dwarvish",
    "Elvish",
    "Giant",
    "Gnomish",
    "Goblin",
    "Halfling",
    "Orc"
]
SKILL_TAG = {
        "Acrobatics" :      "Dexterity",
        "Animal Handling" : "Wisdom",
        "Arcana" :          "Intelligence",
        "Athletics" :       "Strength",
        "Deception" :       "Charisma",
        "History" :         "Intelligence",
        "Insight" :         "Wisdom",
        "Intimidation" :    "Charisma",
        "Investigation" :   "Intelligence",
        "Medicine" :        "Wisdom",
        "Nature" :          "Intelligence",
        "Perception" :      "Wisdom",
        "Performance" :     "Charisma",
        "Persuasion" :      "Charisma",
        "Religion" :        "Intelligence",
        "Sleight of Hand" : "Dexterity",
        "Stealth" :         "Dexterity",
        "Survival" :        "Wisdom"
    }

class Character():
    def __init__(self,
                race = choice(races.RACES),
                _class = choice(Classes.CLASSES),
                alignment = choice(ALIGNMENT)
                ):
        self.race = race
        self._class = _class
        self.alignment = alignment
        self.size = self.race.size
        self.speed = self.race.speed
        self.languages = self.race.languages
        self.equipment = []
        self.armor = None
        self.has_shield = False
        self.AC = 0
        self.saving_throws = self._class.saving_throws

    def determine_ability_scores(self, method):
        ## Does NOT YET account for class bias
        self.abilities = {
        "Strength" :     0,
        "Dexterity" :    0,
        "Constitution" : 0,
        "Charisma" :     0,
        "Intelligence" : 0,
        "Wisdom" :       0
        }
        if method == "roll":
            for i in self.abilities:
                scores = functions.die(4, 6)
                scores.sort()
                scores = scores[1::]
                self.abilities[i] = sum(scores)
        elif method == "array":
            scores = [8, 10, 12, 13, 14, 15]
            for i in self.abilities:
                rand_index = randint(0, len(scores) - 1)
                self.abilities[i] = scores[rand_index]
                scores.pop(rand_index)
        #Add racial modifier
        for i in self.abilities:
            self.abilities[i] += self.race.abilities[i]

    def ability_scores_modifiers(self):
        #Functional but ugly
        self.str_mod = (self.abilities["Strength"] - 10) // 2
        self.dex_mod = (self.abilities["Dexterity"] - 10) // 2
        self.con_mod = (self.abilities["Constitution"] - 10) // 2
        self.cha_mod = (self.abilities["Charisma"] - 10) // 2
        self.int_mod = (self.abilities["Intelligence"] - 10) // 2
        self.wis_mod = (self.abilities["Wisdom"] - 10) // 2
        self.ability_mods = {
            "Strength" : self.str_mod,
            "Dexterity" : self.dex_mod,
            "Charisma" : self.cha_mod,
            "Constitution" : self.con_mod,
            "Intelligence" : self.int_mod,
            "Wisdom" : self.wis_mod
        }

    def set_skill_proficiencies(self):
        #Functional
        self.skill_proficiencies = []
        for _ in range(self._class.skills[0]):
            temp = choice(self._class.skills[1])
            while (temp in self.skill_proficiencies):
                temp = choice(self._class.skills[1])
            self.skill_proficiencies.append(temp)

    def skill_modifiers(self):
        #Functional
        self.skills = {
        "Acrobatics" :      0,
        "Animal Handling" : 0,
        "Arcana" :          0,
        "Athletics" :       0,
        "Deception" :       0,
        "History" :         0,
        "Insight" :         0,
        "Intimidation" :    0,
        "Investigation" :   0,
        "Medicine" :        0,
        "Nature" :          0,
        "Perception" :      0,
        "Performance" :     0,
        "Persuasion" :      0,
        "Religion" :        0,
        "Sleight of Hand" : 0,
        "Stealth" :         0,
        "Survival" :        0
        }
        for i in self.skills:
            self.skills[i] = self.ability_mods[SKILL_TAG[i]]
            if i in self.skill_proficiencies:
                self.skills[i] += self._class.prof_bonus

    def set_alignment(self):
        #Functional, accounts for race bias
        if self.race.alignment:
            if functions.die(1,6) == 1:
                self.alignment = choice(ALIGNMENT)
            self.alignment = choice(self.race.alignment)
        else:
            self.alignment = choice(ALIGNMENT)
    
    def set_extras(self):
        ##WIP
        self.hp_start = self._class.hit_dice + self.abilities["Constitution"]
        self.initiative = self.abilities["Dexterity"]
    
    def set_languages(self):
        #Functional, accounts for race bias
        langs = LANGUAGES
        if self.race.name == "Human":
            langs.remove("Common")
            self.languages.remove("Any")
            self.languages.append(choice(langs))
        elif self.race.name == "Half-Elf":
            langs.remove("Common")
            langs.remove("Elvish")
            self.languages.remove("Any")
            self.languages.append(choice(langs))

    def check_equip(self, style):
        #Functional but ugly
        if style == "Ranged":
            ranged_count = 0
            for item in self.equipment:
                if item in weapons.RANGED:
                    ranged_count += 1
            return ranged_count
        elif style == "Armor":
            armor_count = 0
            for item in self.equipment:
                if item in armor.ARMOR:
                    armor_count += 1
            return armor_count

    def get_equipment(self):
        ##Does NOT YET account for wildcards, ugly
        for i in self._class.equipment:
            decision = choice(i)
            if type(decision) is list:
                for i in decision:
                    self.equipment.append(i)
            else:
                self.equipment.append(decision)
        for i in self.equipment:
            if i == "Shield":
                self.has_shield = True
            for j in armor.ARMOR:
                if i == j.name:
                    self.armor = j
        #"Smart" Select
        if self.check_equip("Ranged") > 1 or self.check_equip("Armor") > 1:
            self.get_equipment()
        #Check for duplicates
        for item in self.equipment:
            if self.equipment.count(item) > 1:
                self.get_equipment()

    def calc_armor_class(self):
        #Functional but can probably be simplified
        if self.armor:
            if self.armor in armor.LIGHT_ARMOR:
                self.AC = self.armor.AC + self.dex_mod
            elif self.armor in armor.MEDIUM_ARMOR:
                if self.dex_mod > 2:
                    self.AC = self.armor.AC + 2
                else:
                    self.AC = self.armor.AC + self.dex_mod
            elif self.armor in armor.HEAVY_ARMOR:
                self.AC = self.armor.AC
        else:
            self.AC = 10 + self.dex_mod
        if self.has_shield:
            self.AC += 2



char = Character()
char.determine_ability_scores("array")
char.set_alignment()
char.set_extras()
char.set_languages()
char.ability_scores_modifiers()
char.get_equipment()
char.calc_armor_class()
char.set_skill_proficiencies()
gui = Tk()
gui.title("UNNAMED CHARACTER")
gui.geometry("1200x700")
gui.configure(bg='light blue')

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
# Label for race and class as they cannot change during the game                                                                  
ttk.Label(gui, text =(char.race.name),
              font = ("Helvetica 10 bold"), background='light blue').grid(column = 1,
          row = 3, padx = 15, pady = 5)
                                                                          
ttk.Label(gui, text =(char._class.name),
              font = ("Helvetica 10 bold"), background='light blue').grid(column = 1,
          row = 4, padx = 15, pady = 5)
                                                                          
# Text boxes for the rest so the user can update/save them later as they progress
box_alignment = Text(gui, width=15, height=1, font=("Papyrus", 12))
box_alignment.grid(column = 1, row = 5)
box_alignment.insert(END, (char.alignment)) 

box_str = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_str.grid(column = 1, row = 7) 
box_str.insert(END, (char.abilities["Strength"]))

box_dex = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_dex.grid(column = 1, row = 8) 
box_dex.insert(END, (char.abilities["Dexterity"]))

box_const = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_const.grid(column = 1, row = 9) 
box_const.insert(END, (char.abilities["Constitution"]))

box_charisma = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_charisma.grid(column = 1, row = 10) 
box_charisma.insert(END, (char.abilities["Charisma"]))

box_intel = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_intel.grid(column = 1, row = 11) 
box_intel.insert(END, (char.abilities["Intelligence"]))

box_wisdom = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_wisdom.grid(column = 1, row = 12) 
box_wisdom.insert(END, (char.abilities["Wisdom"]))

box_armor_class = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_armor_class.grid(column = 1, row = 14) 
box_armor_class.insert(END, (char.AC))                                                

box_languages = Text(gui, width=30, height=4, font=("Helvetica", 12))
box_languages.grid(column = 1, row = 15, pady=10)
box_languages.insert(END, (char.languages)) 

box_attacks = Text(gui, width=35, height=8, font=("Helvetica", 12))
box_attacks.grid(column = 1, row = 16) 
                             
box_level = Text(gui, width=3, height=1, font=("Helvetica", 20))
box_level.grid(column = 4, row = 3)
box_level.insert(END, "1")

box_str_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_str_mod.grid(column = 4, row = 7) 
box_str_mod.insert(END, (char.str_mod))

box_dex_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_dex_mod.grid(column = 4, row = 8) 
box_dex_mod.insert(END, (char.dex_mod))

box_const_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_const_mod.grid(column = 4, row = 9) 
box_const_mod.insert(END, (char.con_mod))

box_charisma_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_charisma_mod.grid(column = 4, row = 10) 
box_charisma_mod.insert(END, (char.cha_mod))

box_intel_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_intel_mod.grid(column = 4, row = 11) 
box_intel_mod.insert(END, (char.int_mod))

box_wisdom_mod = Text(gui, width=4, height=1, font=("Helvetica", 12))
box_wisdom_mod.grid(column = 4, row = 12)
box_wisdom_mod.insert(END, (char.wis_mod))

box_prof = Text(gui, width=30, height=4, font=("Helvetica", 12))
box_prof.grid(column = 4, row = 15)
box_prof.insert(END, (char.skill_proficiencies))

box_equip = Text(gui, width=35, height=10, font=("Helvetica", 12))
box_equip.grid(column = 4, row = 16)
box_equip.insert(END, (char.equipment))

box_XP = Text(gui, width=7, height=1, font=("Helvetica", 12))
box_XP.grid(column = 6, row = 3) 
box_XP.insert(END, "0")

box_HP_current = Text(gui, width=7, height=1, font=("Helvetica", 12))
box_HP_current.grid(column = 6, row = 4)
box_HP_current.insert(END, "TBD") 

box_HP_temp = Text(gui, width=7, height=1, font=("Helvetica", 12))
box_HP_temp.grid(column = 6, row = 5) 
box_HP_temp.insert(END, "N/A")

box_HP_maxi = Text(gui, width=7, height=1, font=("Helvetica", 12))
box_HP_maxi.grid(column = 6, row = 6)
box_HP_maxi.insert(END, "TBD") 
             
# create dropdown file menu                                                                      
menu = Menu(gui)
gui.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
#filemenu.add_command(label="Save", command=save_char)
#filemenu.add_command(label="Save As", command=save_as)
#filemenu.add_command(label="Delete", command=delete_char)
#filemenu.add_command(label="Print", command=print_char)
filemenu.add_separator()
filemenu.add_command(label="Close", command=gui.destroy)                                                                      
   

# Make it so                                                                     
gui.mainloop()
