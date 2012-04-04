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
        
    def addLoc(self, Loc):
        """Add Location to Places"""
        
        # Check For name Collision
        if Loc.name == "" or self.locList.has_key(Loc.name):
            debug("Name collision for ", Loc.name)
            return False
        
        self.locList[Loc.name] = Loc        
        self.passLoc.emit(Loc.name, Loc.x, Loc.y, Loc.objType)
        debug("Emitting location: " + Loc.name + '' + `(Loc.x, Loc.y)`)
        return True
                
    def getLoc(self, name):
        """Retrive Location from Places"""
        
        return self.locList[name]        
        
