from tkinter import *
import math

#various globals (tiny one window application means using global variables not THAT bad. Makes code arguably more readable.)

#information about goods
price = 0
rarity = 0
quantity = 0

 
#tk window stuff
window = Tk()
 
window.title("Trade Calculator")
window.geometry('400x300')



pricePrompt = Label(window, text="Good Price:")
pricePrompt.grid(column=0, row=0)

rarityPrompt = Label(window, text="Rarity:")
rarityPrompt.grid(column=0, row=1)

priceEntry = Entry(window,width=10)
priceEntry.grid(column=1, row=0)

rarityEntry = Entry(window, width=10)
rarityEntry.grid(column=1, row=1)

def TradeCalc():
    print("test")


calculateBtn = Button(window, text="Calculate", command=TradeCalc)
calculateBtn.grid(column=2, row=0)

 
window.mainloop()


