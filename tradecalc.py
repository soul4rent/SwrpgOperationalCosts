from tkinter import *
import math

#various globals (tiny one window application means using global variables not THAT bad. Makes code arguably more readable.)

#from difficulty table
checkDifficulty = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5] #check difficulty based on rarity
wheelAndDealRanks = 0 #wheel and deal ranks

#calculate successes effect on purchase price
def BuyPrice(successes, disadvantages, basePrice):
    if successes >= 1:
        return basePrice - (basePrice*0.05*(successes-1)) + (basePrice*0.01*disadvantages)
        #-5% price each success past first, +1% price each disadvantage
    return 0    


#when selling goods, 1/4 on 1 success, 2/4 on two, 3/4 on three
#+5% for each additional past first
#calculate successes effect on sale price
def SellPrice(successes, disadvantages, basePrice):
    if successes > 0:
        sp = min(successes*1/4, 3/4)*basePrice
        sp -= .01*basePrice*disadvantages
        if successes > 1:
            sp += .05*basePrice*(successes-1)
            return sp
        return sp
    return 0

#returns modified price based on rarity
def SellPriceRarity(rarityBuy, raritySell, basePrice):
    if raritySell - rarityBuy > 0:
        return basePrice * min(raritySell - rarityBuy, 4)
    return basePrice



#tk window stuff

window = Tk()
 
window.title("Trade Calculator")
window.geometry('550x300')

#================================

basePricePrompt = Label(window, text="Good Price:")
basePricePrompt.grid(column=0, row=0)

priceEntry = Entry(window,width=10)
priceEntry.grid(column=1, row=0)

rarityBuyPrompt = Label(window, text="Rarity (buy):")
rarityBuyPrompt.grid(column=2, row=0)

rarityBuyEntry = Entry(window, width=10)
rarityBuyEntry.grid(column=3, row=0)


def BuyCheckCalc():
    r = int(rarityBuyEntry.get())
    if r < 11:
        return checkDifficulty[r]
    elif r > 10:
        return 5 + (r - 10)

def BuyCheckDisplay():
    buyDifficultyDisplay.configure(text=str(BuyCheckCalc()))


calculateBuyCheckBtn = Button(window, text="Calculate Check", command=BuyCheckDisplay)
calculateBuyCheckBtn.grid(column=0, row=5)

buyDifficultyLabel = Label(window, text="Buy Difficulty:")
buyDifficultyLabel.grid(column=2, row=5)

buyDifficultyDisplay = Label(window, text="---")
buyDifficultyDisplay.grid(column=3, row=5)

#==============================

dividerOne = Label(window, text="---Check Results (buy)---")
dividerOne.grid(column=0, row=10)

#==============================

buyCheckSuccessPrompt = Label(window, text="Check Successes:")
buyCheckSuccessPrompt.grid(column=0, row=11)

buyCheckSuccessesEntry = Entry(window,width=11)
buyCheckSuccessesEntry.grid(column=1, row=11)

buyCheckDisadvantagesPrompt = Label(window, text="Disadvantages:")
buyCheckDisadvantagesPrompt.grid(column=2, row=11)

buyCheckDisadvantagesEntry = Entry(window,width=11)
buyCheckDisadvantagesEntry.grid(column=3, row=11)


def calculateBuyPrice():
    s = int(buyCheckSuccessesEntry.get())
    d = int(buyCheckDisadvantagesEntry.get())
    p = float(priceEntry.get())
    buyPriceDisplay.configure(text = str(BuyPrice(s,d,p)))


calculateBuyPriceBtn = Button(window, text="Calculate Price", command=calculateBuyPrice)
calculateBuyPriceBtn.grid(column=0, row=15)

buyPriceLabel = Label(window, text="Buy Price:")
buyPriceLabel.grid(column=2, row=15)

buyPriceDisplay = Label(window, text="---")
buyPriceDisplay.grid(column=3, row=15)

#==========================

dividerTwo = Label(window, text="---Check Results (sell)---")
dividerTwo.grid(column=0, row=20)

#==========================

sellCheckSuccessPrompt = Label(window, text="Check Successes:")
sellCheckSuccessPrompt.grid(column=0, row=21)

sellCheckSuccessEntry = Entry(window,width=11)
sellCheckSuccessEntry.grid(column=1, row=21)

sellCheckDisadvantagesPrompt = Label(window, text="Disadvantages:")
sellCheckDisadvantagesPrompt.grid(column=2, row=21)

sellCheckDisadvantagesEntry = Entry(window,width=11)
sellCheckDisadvantagesEntry.grid(column=3, row=21)

sellRarityPrompt = Label(window, text="Rarity (sell):")
sellRarityPrompt.grid(column=4, row=21)

sellRarityEntry = Entry(window,width=11)
sellRarityEntry.grid(column=5, row=21)


def CalculateSellPrice():
    s = int(sellCheckSuccessEntry.get()) #successes
    d = int(sellCheckDisadvantagesEntry.get()) #disadvantages
    p = float(priceEntry.get()) #price
    br = int(rarityBuyEntry.get()) #buy rarity
    sr = int(sellRarityEntry.get()) #sell rarity
    disp = str(SellPrice(s, d, SellPriceRarity(br, sr, p)))
    sellPriceDisplay.configure(text = disp)

calculateSellPriceBtn = Button(window, text="Calculate Sale", command=CalculateSellPrice)
calculateSellPriceBtn.grid(column=0, row=25)

sellPriceLabel = Label(window, text="Sell Price:")
sellPriceLabel.grid(column=2, row=25)

sellPriceDisplay = Label(window, text="---")
sellPriceDisplay.grid(column=3, row=25)

window.mainloop()


