from tkinter import *
import math

#various globals (tiny one window application means using global variables not THAT bad. Makes code arguably more readable.)

#from difficulty table
checkDifficulty = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5] #check difficulty based on rarity

#calculate successes effect on purchase price
def buyPrice(successes, basePrice):
    if successes > 1:
        return baseprice - (baseprice*0.05*(successes-1)) #-5% price each success past first
    return 0    


#when selling goods, 1/4 on 1 success, 2/4 on two, 3/4 on three
#+5% for each additional past first
#calculate successes effect on sale price
def sellPrice(successes, basePrice):
    if successes > 0:
        sp = min(successes*1/4, 3/4)*basePrice
        if successes > 1:
            sp += .05*basePrice*(successes-1)
            return sp
        return sp
    return 0

#returns modified base price based on rarity
def sellPriceRarity(rarityBuy, raritySell, basePrice):
    if raritySell - rarityBuy > 0:
        return basePrice * min(raritySell - rarityBuy, 4)
    return basePrice



#tk window stuff

window = Tk()
 
window.title("Trade Calculator")
window.geometry('400x300')

basePricePrompt = Label(window, text="Good Price:")
basePricePrompt.grid(column=0, row=0)

priceEntry = Entry(window,width=10)
priceEntry.grid(column=1, row=0)

rarityBuyPrompt = Label(window, text="Rarity (buy):")
rarityBuyPrompt.grid(column=2, row=0)

rarityBuyEntry = Entry(window, width=10)
rarityBuyEntry.grid(column=3, row=0)


def checkCalc():
    r = int(rarityBuyEntry.get())
    if r < 11:
        buyDifficultyDisplay.configure(text=str(checkDifficulty[r]))
    elif r > 10:
        buyDifficultyDisplay.configure(text=str(5 + (r - 10)))


calculateCheckBtn = Button(window, text="Calculate Check", command=checkCalc)
calculateCheckBtn.grid(column=0, row=5)

buyDifficultyLabel = Label(window, text="Buy Difficulty:")
buyDifficultyLabel.grid(column=2, row=5)

buyDifficultyDisplay = Label(window, text="---")
buyDifficultyDisplay.grid(column=3, row=5)



dividerOne = Label(window, text="---Check Results (buy)---")
dividerOne.grid(column=0, row=10)




 
window.mainloop()


