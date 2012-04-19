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
    
    TYPES = {"tree", "mountain","lake","landmark","grass","water","mapBG", "capital"} #obj types, for debugging use
    OBJ_COMMANDS = {"addLoc"}
    passLoc = pyqtSignal(str, int, int, str) 
    
    def __init__(self):
        """Internaly Places is represented as a dictonary"""
        super(QObject, self).__init__()
        self.locList = {}
        self.newId = 0
        
    def loadLoc(self, filename = "saves/places.loc"):
        """Load location objects from file"""
        
        if(not isfile(filename)):
            debug("location file does not exist!!!")
            return
            
        n = 0
        itemName = ""   
        locData = open(filename)
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
                    if (len(obj) > 4):
                        itemName = obj[4]
                    locObject = Loc(pos, itemName, objType)
                    if (self.addLoc(locObject) == False):
                        pass
                else:
                    debug("Places...loading loc line ",n," is an invalid input!")
            nextLine = locData.readline()
            n+=1
            itemName = ""       
        locData.close()
        debug("while loop ends")
    
    def isValidLoc(self, obj):
        """Check whether the loc command is valid"""
        if(len(obj) < 4):
            debug("Places...loading loc.... miss command, should at least 4")
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
        return True
 
    def addLoc(self, Loc):
        debug("Load tag")
        """Add Location to Places and check for name collisions"""
        
        if Loc.name == "":
            Loc.name = 'staticItem'+`self.newId`
            self.newId += 1
            return self.addLoc(Loc) # Do we actually want to store these?

        if self.locList.has_key(Loc.name):
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
        
        
        
        
