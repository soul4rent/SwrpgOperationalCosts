from tkinter import *
import math

#various globals (tiny one window application means using global variables not THAT bad. Makes code arguably more readable.)
shipFuel = 60
shipFuelRemain = 60
hyperUses = 20 #hyperspace uses total (before bad things happen)
spentHyper = 0 #spent hyperspace uses
hyperCalc = 0 #fuel spent in hyperspace jumps

 
#tk window stuff
window = Tk()
 
window.title("Operational Costs")
window.geometry('400x500')


#Hyperspace Fuel Calculations (Higher in window)

baseTimePrompt = Label(window, text="Squares Traveled")
baseTimePrompt.grid(column=0, row=0)

modTimePrompt = Label(window, text="Travel Time %Mod")
modTimePrompt.grid(column=0, row=1)

spentFuelDisplay = Label(window, text="Spent Fuel: -")
spentFuelDisplay.grid(column=0, row=2)
 
baseTimeEntry = Entry(window,width=10)
baseTimeEntry.grid(column=1, row=0)

modTimeEntry = Entry(window, width=10)
modTimeEntry.grid(column=1, row=1)

#Calculate and display hyperspace fuel costs
def HyperCalc():
    global hyperCalc #made global var so others can use it
    hyperCalc = float(baseTimeEntry.get())*4
    #24 hours per square, 1 fuel cell spent per 6 hours of hyperspace travel
    hyperCalc = math.ceil(hyperCalc - (hyperCalc*float(modTimeEntry.get()))) #calculations NOT in player's favor (tiny jumps take minimum of 1 fuel)
    #add fuel cost modifiers.

    res = "Spent Fuel: " + str(hyperCalc) 
    spentFuelDisplay.configure(text=res)

astroBtn = Button(window, text="Calculate", command=HyperCalc)
astroBtn.grid(column=2, row=0)

#=====================================
firstDivider = Label(window, text="-------")
firstDivider.grid(column=0, row=3)
#=====================================
#Fuel Calculations


def IncFuel():
    global shipFuelRemain
    shipFuelRemain += 1
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))

def DecFuel():
    global shipFuelRemain
    shipFuelRemain -= 1
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))

def ResFuel():
    global shipFuelRemain
    shipFuelRemain = shipFuel
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))

def HyperFuelCalc(): #subtract fuel cost from hyperspace jump; inc hyperspace jumps
    global shipFuelRemain
    global spentHyper
    shipFuelRemain -= hyperCalc
    spentHyper += 1
    spentHyperDisplay.configure(text="Hyper: "+str(spentHyper) + "/" + str(hyperUses))
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))


decFuelButton = Button(window, text="-", command=DecFuel)
decFuelButton.grid(column=0, row=10)

remainFuelDisplay = Label(window, text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))
remainFuelDisplay.grid(column=1, row=10)

incFuelButton = Button(window, text="+", command=IncFuel)
incFuelButton.grid(column=2, row=10)

resFuelButton = Button(window, text="Refuel", command=ResFuel)
resFuelButton.grid(column=3, row=10)


#================================
#Hyperspace calculation button

subHyperFuelButton = Button(window, text="Calculate Hyperspace", command=HyperFuelCalc)
subHyperFuelButton.grid(column=1, row=3)


#=================================
#Hyperdrive Use Calculations


def IncHyper():
    global spentHyper
    spentHyper += 1
    spentHyperDisplay.configure(text="Hyper: "+str(spentHyper) + "/" + str(hyperUses))

def DecHyper():
    global spentHyper
    spentHyper -= 1
    spentHyperDisplay.configure(text="Hyper: "+str(spentHyper) + "/" + str(hyperUses))

def ResHyper():
    global spentHyper
    spentHyper = 0
    spentHyperDisplay.configure(text="Hyper: "+str(spentHyper) + "/" + str(hyperUses))


decHyperButton = Button(window, text="-", command=DecHyper)
decHyperButton.grid(column=0, row=11)

spentHyperDisplay = Label(window, text="Hyper: "+str(spentHyper) + "/" + str(hyperUses))
spentHyperDisplay.grid(column=1, row=11)

incHyperButton = Button(window, text="+", command=IncHyper)
incHyperButton.grid(column=2, row=11)

resHyperButton = Button(window, text="Reset", command=ResHyper)
resHyperButton.grid(column=3, row=11)

#==================================
#Refuel / Maintain Parts calculations



 
window.mainloop()
