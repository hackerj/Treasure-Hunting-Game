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

class Loc(QObject):
    
    changePos = pyqtSignal(int, int, str)
    
    def __init__(self, center = (0,0), name = '', objType=None):
        """Data container for objects appearing in the person and map views"""
        super(QObject, self).__init__()

        self.name = name
        self.x = center[0]
        self.y = center[1]
        self.objType = objType
        
        
    def __repr__(self):
        return "Loc Object at "+`self.x`+","+`self.y`+ \
               " of type " + `self.objType`
    
    def getCenter(self):
        return (self.x, self.y)
        
    def emitter(self):
        debug("Hi from", self.name)
        self.changePos.emit(self.x,self.y, self.name)
