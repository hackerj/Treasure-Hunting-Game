"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QObject

class Loc(QObject):
    def __init__(self, center, name = '', objType=None):
        """Data container for objects appearing in the person and map views"""

        self.name = name
        self.x = center[0]
        self.y = center[1]
        self.objType = objType
        #Signal Here
        
    def __repr__(self):
        return "QGraphicsObject at "+`self.x`+","+`self.y`+ \
               " of type " + `self.objType`
    
    def getCenter(self):
        return (self.x, self.y)