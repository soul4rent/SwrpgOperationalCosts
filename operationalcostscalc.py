from tkinter import *
import math
import ShipDataReader as sdr

#various globals (tiny one window application means using global variables not THAT bad. Makes code arguably more readable.)
hyperDriveClass = sdr.getShipHyperdriveClass() #How fast hyperdrive travels. Higher the class, slower it goes.
shipFuel = sdr.getShipFuel()
shipFuelRemain = sdr.getShipFuel()
hyperUses = sdr.getShipHyperdriveUses() #hyperspace uses total (before bad things happen)
spentHyper = 0 #spent hyperspace uses
hyperCalc = 0 #used to keep track of fuel spent in hyperspace jumps
maintainEvents = 0 #maintainence events add up to equal maintainence hours over time (5 per hour)
portGrade = 1 #how good the port is (higher grade = more popular port)
portFuelCosts = sdr.getPortFuelCosts() #fuel costs per cell
portPartCosts = sdr.getPartCosts() #parts not guaranteed at tier 5 ports

 
#tk window stuff
window = Tk()
 
window.title("Operational Costs")
window.geometry('400x300')


#Hyperspace Fuel Calculations Display/Buttons

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
    hyperCalc = float(baseTimeEntry.get())*4*hyperDriveClass
    #24 hours per square, 1 fuel cell spent per 6 hours of hyperspace travel
    #This is for a class 1 hyperdrive though. Class 2 is 2x slower, class 3 is 3x, etc.

    hyperCalc = math.ceil(hyperCalc - (hyperCalc*float(modTimeEntry.get())))
    #add fuel cost modifiers.
    #calculations NOT in player's favor (tiny jumps take minimum of 1 fuel)
    

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

    fuelCostDisplay.configure(text="Refuel Cost: "+str(portFuelCosts[portGrade-1]*(shipFuel-shipFuelRemain)))

def DecFuel():
    global shipFuelRemain
    shipFuelRemain -= 1
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))

    fuelCostDisplay.configure(text="Refuel Cost: "+str(portFuelCosts[portGrade-1]*(shipFuel-shipFuelRemain)))

def ResFuel():
    global shipFuelRemain
    shipFuelRemain = shipFuel
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))

    fuelCostDisplay.configure(text="Refuel Cost: "+str(portFuelCosts[portGrade-1]*(shipFuel-shipFuelRemain)))

def HyperFuelCalc(): #subtract fuel cost from hyperspace jump; inc hyperspace jumps
    global shipFuelRemain
    global spentHyper
    shipFuelRemain -= hyperCalc
    spentHyper += 1
    spentHyperDisplay.configure(text="Hyper: "+str(spentHyper) + "/" + str(hyperUses))
    remainFuelDisplay.configure(text="Fuel: "+str(shipFuelRemain) + "/" + str(shipFuel))

    fuelCostDisplay.configure(text="Refuel Cost: "+str(portFuelCosts[portGrade-1]*(shipFuel-shipFuelRemain)))


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

#=================================

def IncM():
    global maintainEvents
    maintainEvents += 1
    mEventsDisplay.configure(text="M. Events: "+str(maintainEvents))
    mHoursDisplay.configure(text="M. Hours: "+str(int(maintainEvents/5)))
    mCostDisplay.configure(text="Parts Cost: "+str(portPartCosts[portGrade-1]*int(maintainEvents/5)))

def DecM():
    global maintainEvents
    maintainEvents -= 1
    mEventsDisplay.configure(text="M. Events: "+str(maintainEvents))
    mHoursDisplay.configure(text="M. Hours: "+str(int(maintainEvents/5)))
    mCostDisplay.configure(text="Parts Cost: "+str(portPartCosts[portGrade-1]*int(maintainEvents/5)))

def ResM():
    global maintainEvents
    maintainEvents = 0
    mEventsDisplay.configure(text="M. Events: "+str(maintainEvents))
    mHoursDisplay.configure(text="M. Hours: "+str(int(maintainEvents/5)))
    mCostDisplay.configure(text="Parts Cost: "+str(portPartCosts[portGrade-1]*int(maintainEvents/5)))
    

decMEventsButton = Button(window, text="-", command=DecM)
decMEventsButton.grid(column=0, row=12)

mEventsDisplay = Label(window, text="M. Events: "+str(maintainEvents))
mEventsDisplay.grid(column=1, row=12)

incMEventsButton = Button(window, text="+", command=IncM)
incMEventsButton.grid(column=2, row=12)

resMEventsButton = Button(window, text="Reset", command=ResM)
resMEventsButton.grid(column=3, row=12)


def IncMHours():
    global maintainEvents
    maintainEvents += 5 #each maintaince hour is 5 maintainence events
    mEventsDisplay.configure(text="M. Events: "+str(maintainEvents))
    mHoursDisplay.configure(text="M. Hours: "+str(int(maintainEvents/5)))
    mCostDisplay.configure(text="Parts Cost: "+str(portPartCosts[portGrade-1]*int(maintainEvents/5))) #part costs change depending on port grade

def DecMHours():
    global maintainEvents
    maintainEvents -= 5 #each maintaince hour is 5 maintainence events
    mEventsDisplay.configure(text="M. Events: "+str(maintainEvents))
    mHoursDisplay.configure(text="M. Hours: "+str(int(maintainEvents/5)))
    mCostDisplay.configure(text="Parts Cost: "+str(portPartCosts[portGrade-1]*int(maintainEvents/5))) #part costs change depending on port grade


decMHoursButton = Button(window, text="-", command=DecMHours)
decMHoursButton.grid(column=0, row=13)

mHoursDisplay = Label(window, text="M. Hours: "+str(int(maintainEvents/5)))
mHoursDisplay.grid(column=1, row=13)

incMHoursButton = Button(window, text="+", command=IncMHours)
incMHoursButton.grid(column=2, row=13)

#==================================
secondDivider = Label(window, text="-------")
secondDivider.grid(column=0, row=15)
#=====================================
#Refuel / Maintain Parts calculations

def IncPort():
    global portGrade
    if portGrade < 5:
        portGrade += 1
    portGradeDisplay.configure(text="Port Grade: "+str(portGrade))
    fuelCostDisplay.configure(text="Refuel Cost: "+str(portFuelCosts[portGrade-1]*(shipFuel-shipFuelRemain)))
    mCostDisplay.configure(text="Parts Cost: "+str(portPartCosts[portGrade-1]*int(maintainEvents/5)))

def DecPort():
    global portGrade
    if portGrade > 1:
        portGrade -= 1
    portGradeDisplay.configure(text="Port Grade: "+str(portGrade))
    fuelCostDisplay.configure(text="Refuel Cost: "+str(portFuelCosts[portGrade-1]*(shipFuel-shipFuelRemain)))
    mCostDisplay.configure(text="Parts Cost: "+str(portPartCosts[portGrade-1]*int(maintainEvents/5)))


decPortButton = Button(window, text="-", command=DecPort)
decPortButton.grid(column=0, row=20)

portGradeDisplay = Label(window, text="Port Grade: "+str(portGrade))
portGradeDisplay.grid(column=1, row=20)

incPortButton = Button(window, text="+", command=IncPort)
incPortButton.grid(column=2, row=20)



#====================================
#cost displays
fuelCostDisplay = Label(window, text="Refuel Cost: "+str(portFuelCosts[portGrade-1]*(shipFuel-shipFuelRemain)))
fuelCostDisplay.grid(column=0, row=21)

#parts cost vary depending on port, multiply by needed hours of maintainence
mCostDisplay = Label(window, text="Parts Cost: "+str(portPartCosts[portGrade-1]*int(maintainEvents/5)))
mCostDisplay.grid(column=0, row=22)

 
window.mainloop()
