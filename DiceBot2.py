import random
import tkinter as tk
from tkinter import ttk

  
# Creating tkinter window
gui = tk.Tk()
gui.title('DiceBot')
gui.geometry('450x300')
gui.wm_protocol("WM_DELETE_WINDOW", gui.destroy)
  
# label text for title
ttk.Label(gui, text = "DiceBot Interface", 
          background = 'black', foreground ="yellow", 
          font = ("Times New Roman", 20)).grid(row = 1, column = 1)
  
# label text next to dropdown
ttk.Label(gui, text = "Select: ",
          font = ("Times New Roman", 15)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
# Combobox creation
dice = ttk.Combobox(gui, width = 27, values = ("Coin Flip", "D4", "D6", "D8", "D10", "D12", "D20"))
  

dice.grid(column = 1, row = 5)
dice.current()

def click_me():
    #roll = ""
    
    if dice.get() == "Coin Flip":
        roll = random.randint(1,2)
    elif dice.get() == "D4":
        roll = random.randint(1,4)
    elif dice.get() == "D6":
        roll = random.randint(1,6)
    elif dice.get() == "D8":
        roll = random.randint(1,8)
    elif dice.get() == "D10":
        roll = random.randint(1,10)
    elif dice.get() == "D12":
        roll = random.randint(1,12)
    elif dice.get() == "D20":
        roll = random.randint(1,20)
    else:
        roll = ""
        
    # Start the result area fresh with no overlap from previous double-digit rolls    
    action.configure(ttk.Label(gui, text = "      ", font = ("Times New Roman", 30)).grid(column = 1, row = 10, padx = 10, pady = 25))                                         
    
    # Display results of each roll in large font
    action.configure(ttk.Label(gui, text = (roll), foreground ='black', font = ("Times New Roman", 30)).grid(column = 1, row = 10, padx = 10, pady = 25))                                         
    
    # Add extra mesasge for rolling a 20
    action.configure(ttk.Label(gui, text = "                ", font = ("Times New Roman", 20)).grid(column = 2, row = 10, padx = 10, pady = 25))
    
    if roll == 20:
        action.configure(ttk.Label(gui, text = "It's the big one!", font = ("Times New Roman", 10)).grid(column = 2, row = 10, padx = 10, pady = 25))
   


# Add a button
action = ttk.Button(gui, text="Let's Roll!", command = click_me)
action.grid(column=2, row=5)

# Add a display box for dice outcomes
ttk.Label(gui, text = "Outcome: ",
          font = ("Times New Roman", 15)).grid(column = 0,
          row = 10, padx = 10, pady = 25)

# initialize everything within the main window
gui.mainloop()

