#for now, it's just a bunch of functions that return ship data for my own
#tabletop RPG campaign. I'll make these read from a file if I need this to be
#more flexible and easier to edit.

def getShipHyperdriveClass():
    return 2

def getShipFuel():
    return 60

def getShipHyperdriveUses():
    return 20

def getPortFuelCosts():
    return [15, 25, 25, 30, 40]

def getPartCosts():
    return [15, 15, 20, 25, 0]
