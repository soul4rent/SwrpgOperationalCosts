#for now, it's just a bunch of functions that return ship data for my own
#tabletop RPG campaign. I'll make these read from a file if I need this to be
#more flexible and easier to edit.
import re


def DataNumber(s):
    m = re.search(r'\d+$', s) #get number trailing at end of string
    return int(m.group()) if m else None #return the number


#give a string to search each line for, and return number at end of the line
#like an SQL search in a database, but worse, and easier to edit in a config file.
def ReadDataFile(searchString): 
    try:
        sd = open('ShipData.txt')
        data = sd.readlines()
        data = [x.strip() for x in data] #strip out uneccessary chars to make data more readable
        
        for line in data:
            if (line.find(searchString) != -1): #string found
                return DataNumber(line) #return data at end of line
    except:
        print("ERR: PROBLEM WITH READING FILE") 

    finally:
        sd.close()


#each of these reads from a text file to get the relevant data
#for use in operationalcostscalc program
def getShipHyperdriveClass():
    return ReadDataFile("Hyperdrive")

def getShipFuel():
    return ReadDataFile("ShipFuel")

def getShipHyperdriveUses():
    return ReadDataFile("ShipHyperdriveUses")

def getPortFuelCosts():
    return [15, 25, 25, 30, 40]

def getPartCosts():
    return [15, 15, 20, 25, 0]


