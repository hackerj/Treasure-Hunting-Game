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
from os.path import isfile
class Places(QObject):
    """Dictionary of Location Objects with name collision Checking"""
    NAMES = {'city2', 'city1', 'tree5', 'tree4', 'tree6', 'tree1', 'grass1',\
              'tree3', 'tree2', 'grass4', 'mapBG', 'grass2', 'city0', 'grass3'}
    TYPES = {"tree", "landmark","grass","mapBG", "capital"} #obj types, for debugging use
    OBJ_COMMANDS = {"addLoc"}
    passLoc = pyqtSignal(str, int, int, str) 
    
    def __init__(self):
        """Internaly Places is represented as a dictonary"""
        super(QObject, self).__init__()
        self.locList = {}

    def loadLoc(self, filename = "saves/places.loc"):
        """Load location objects from file"""
        
        if(not isfile(filename)):
            debug("location file does not exist!!!")
            return
            
        locData = open(filename)
        n = 0
        nextLine = locData.readline()
        while (nextLine):        # start parsing..
            obj = nextLine.split()
            if (len(obj)>2 and obj[0]!= "Command"):
                objCommand = obj[0]
                if (self.isValidLoc(obj)):
                    objType = obj[1]
                    posx = int(obj[2])
                    posy = int(obj[3])
                    pos = (posx, posy)
                    itemName = obj[4]
                    locObject = Loc(pos, itemName, objType)
                    self.addLoc(locObject)
                else:
                    debug("Places...loading loc line ",n," is an invalid input!")

            nextLine = locData.readline()
            n+=1       
        locData.close()
        debug("while loop ends")
    
    def isValidLoc(self, obj):
        """Check whether the loc command is valid"""
        if(len(obj) != 5):
            debug("Places...loading loc.... has missing command, should be 5")
            return False
        
        if(obj[0] not in self.OBJ_COMMANDS):
            debug(obj[0], " Places...loading loc.... has an invalid command")
            return False
        
        if(obj[1] not in self.TYPES):
            debug(obj[1], " Places...loading loc.... has an invalid obj type")
            return False
        
        try:
            int(obj[2]) and int(obj[3])
        except:
            debug(obj[1], " doesn't have the right type for x and y position")
            return False

        if (obj[4] not in self.NAMES):
            debug(obj[1], " Places...loading loc.... has an invalid name")
            return False
        
        return True
 

    def addLoc(self, Loc):
        debug("Load tag")
        """Add Location to Places and check for name collisions"""
        
        if Loc.name == "":
            Loc.name = 'staticItem'+`self.newId`
            self.newId += 1
            return self.addLoc(Loc) # Do we actually want to store these?

        elif self.locList.has_key(Loc.name):
            debug("Name collision for ", Loc.name)
            return False
        
        self.locList[Loc.name] = Loc      
        self.passLoc.emit(Loc.name, Loc.x, Loc.y, Loc.objType)
        debug("Emitting location: " + Loc.name + '' + `(Loc.x, Loc.y)`)
        return Loc.name
                
    def getLoc(self, name):
        """Retrive Location from Places"""
        
        return self.locList[name]

    def getLocsNear(self, x, y):
        """Find Location Objects Need Position"""
        None
        
        
        
        
