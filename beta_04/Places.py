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

class Places(QObject):
    """Dictionary of Location Objects with name collision Checking"""
    passLoc = pyqtSignal('QString', int, int, 'QString') 
    
    def __init__(self):
        """Internaly Places is represented as a dictonary"""
        
        self.locList = {}
    
    def loadLoc(self, filename = "saves/load.loc")
    
    
    
        
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
        self.passLoc.emit(Loc.name, Loc.x, Loc.y, Loc.objType)
        debug("Emitting location: " + Loc.name + '' + `(Loc.x, Loc.y)`)
        return Loc.name
                
    def getLoc(self, name):
        """Retrive Location from Places"""
        
        return self.locList[name]

    def getLocsNear(self, x, y):
        """Find Location Objects Need Position"""
        None
