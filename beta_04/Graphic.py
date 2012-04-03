"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QObject

class Graphic(QObject):
    def __init__(self, center, name = '', objType=None):
        """Data container for graphics equivalent of location objects"""

        self.PviewObject = None
        self.MviewObject = None
        self.x = center[0]
        self.y = center[1]
        self.objType = objType

        # Add slot for signal from location object.
        
    def __repr__(self):
        return "QGraphicsObject at "+`self.x`+","+`self.y`+ \
               " of type " + `self.objType`
    
    def creatInitial(self):
        None
    
    def update(self):
        None
