"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from Loc import Loc
from Globals import *

class Character(Loc):
    """Inherit from Location Objects and add functionality for"""
    SPEED = 200
    
    def __init__(self, position, objType=None)
        super(ViewGraphics, self).__init__(self, position, objType)
        
        self.charVelocityX = 0     # Gives the X offset to use every frame
        self.charVelocityY = 0     # Gives the Y offset to use every frame
        self.charSpeed     = SPEED # Pixels per second.
        
    def translate(self, xDist, yDist):
        if (self.isValidMove( xDist, yDist)):
            self.x += xDist
            self.y += yDist

    def isValidMove(self, data, xDist, yDist):
        debug("isVaidMove not implemented!")
        return True
        