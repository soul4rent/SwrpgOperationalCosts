from tkinter import *


#unsure how much of this to use
shipFuel = 60
shipFuelRemain = 60
hyperdriveUses = 20
spentHyperdriveUses = 0


 

#tk window stuff
window = Tk()
 
window.title("Op Costs")
window.geometry('350x500')


#Hyperspace Fuel Calculations (Higher in window)

baseTimePrompt = Label(window, text="Squares Traveled")
baseTimePrompt.grid(column=0, row=0)

modTimePrompt = Label(window, text="Travel Time %Mod")
modTimePrompt.grid(column=0, row=1)

spentFuelDisplay = Label(window, text="---")
spentFuelDisplay.grid(column=0, row=2)
 
baseTimeEntry = Entry(window,width=10)
baseTimeEntry.grid(column=1, row=0)

modTimeEntry = Entry(window, width=10)
modTimeEntry.grid(column=1, row=1)

#Calculate and display hyperspace fuel costs
def HyperCalc():
    fuelCost = float(baseTimeEntry.get())*4
    #24 hours per square, 1 fuel cell spent per 6 hours of hyperspace travel
    fuelCost = fuelCost - (fuelCost*float(modTimeEntry.get()))
    #add fuel cost modifiers.

    res = "Spent Fuel: " + str(fuelCost) 
    spentFuelDisplay.configure(text=res)

astroBtn = Button(window, text="Calculate", command=HyperCalc)
astroBtn.grid(column=2, row=0)

#=====================================

#Fuel Calculations (lower in window)1

#increment value given
def IncFuel():
    global shipFuelRemain
    shipFuelRemain += 1
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))

def DecFuel():
    global shipFuelRemain
    shipFuelRemain -= 1
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))


decFuelButton = Button(window, text="-", command=DecFuel)
decFuelButton.grid(column=0, row=10)

remainFuelDisplay = Label(window, text="60")
remainFuelDisplay.grid(column=1, row=10)

incFuelButton = Button(window, text="+", command=IncFuel)
incFuelButton.grid(column=2, row=10)


#=====================================

#Hyperdrive Use Calculations (lower in window)1

#increment value given
def IncHyper():
    global shipFuelRemain
    shipFuelRemain += 1
    remainFuelDisplay.configure(text="Hyper: "+str(shipFuelRemain) + "/" + str(shipFuel))

def DecHyper():
    global shipFuelRemain
    shipFuelRemain -= 1
    remainFuelDisplay.configure(text="Hyper: "+str(shipFuelRemain) + "/" + str(shipFuel))


decHyperButton = Button(window, text="-", command=DecHyper)
decHyperButton.grid(column=0, row=11)

spentHyperDisplay = Label(window, text="60")
spentHyperDisplay.grid(column=1, row=11)

incHyperButton = Button(window, text="+", command=IncHyper)
incHyperButton.grid(column=2, row=11)





 
window.mainloop()
