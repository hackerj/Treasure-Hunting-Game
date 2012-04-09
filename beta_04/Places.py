"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QObject, pyqtSignal
from Globals import *
from Loc import Loc

class Places(QObject):
    """Dictionary of Location Objects with name collision Checking"""
    passLoc = pyqtSignal('QString', int, int, 'QString') 
    
    def __init__(self):
        """Internaly Places is represented as a dictonary"""
        
        self.locList = {}
 
    def loadLoc(self, filename = "saves/places.loc"):
        """Load location objects from file"""
        locData = open(filename)
        n = 0
        nextLine = locData.readline()
        while (nextLine):
            obj = nextLine.split()
        
            if (len(obj)>2):
                objCommand = obj[0]
                if (objCommand == "addLoc" and self.isValidLoc(obj)):
                    objType = obj[1]
                    posx = int(obj[2])
                    posy = int(obj[3])
                    pos = (posx, posy)
                    itemName = obj[4]
                    locObject = Loc(pos, itemName, objType)
                    self.addLoc(locObject)
            else:
                debug( "Places.loadLoc...Line ", n, " is invalid!")
            nextLine = locData.readline()
            n+=1

        locData.close()
    
    def isValidLoc(self, obj):
        """Check whether the loc command is valid"""
        TYPES = {"tree", "landmark"} #obj types, for debugging
        
        if(len(obj) != 5):
            debug("location is invalid,missing command")
            return False
        
        try:
            int(obj[2]) and int(obj[3])
        except:
            debug(obj[1], " doesn't have the right type for x and y position")
            return False
        
        return obj[1] in TYPES 
 

    def addLoc(self, Loc):
        """Add Location to Places and check for name collisions"""
        
        if Loc.name == "":
            Loc.name = 'staticItem'+`self.newId`
            self.newId += 1
            return self.addLoc(Loc) # Do we actually want to store these?

        elif self.locList.has_key(Loc.name):
            debug("Name collision for ", Loc.name)
            return False
        
        self.locList[Loc.name] = Loc        
        #self.passLoc.emit(Loc.name, Loc.x, Loc.y, Loc.objType)
        #debug("Emitting location: " + Loc.name + '' + `(Loc.x, Loc.y)`)
        return Loc.name
                
    def getLoc(self, name):
        """Retrive Location from Places"""
        
        return self.locList[name]

    def getLocsNear(self, x, y):
        """Find Location Objects Need Position"""
        None
        
        
        
        
