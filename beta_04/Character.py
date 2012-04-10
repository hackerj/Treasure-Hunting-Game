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

from PyQt4.QtCore import Qt, pyqtSignal

class Character(Loc):
    """Inherit from Location Objects and add functionality for"""
    SPEED = 200
    
    def __init__(self, center = (0,0), name = '', objType=None):
        super(Character, self).__init__(center = (0,0), 
                                        name = '', objType=None)
        
        self.charVelocityX = 0  # Gives the X offset to use every frame
        self.charVelocityY = 0  # Gives the Y offset to use every frame
        self.updateSignal = None
        
    def translate(self, xDist, yDist):
        if (self.isValidMove( xDist, yDist)):
            self.x += xDist
            self.y += yDist
            self.changePos.emit((self.x, self.y))
            debug("Character is emitting changePos")

    def isValidMove(self, xDist, yDist):
        """Stop Character From walking off the edge of the map"""
        
        debug("isVaidMove not implemented!")
        return True
        
    def frameUpdate(self, framerate):
        """update character position for the new frame"""
        
        xLoc = self.charVelocityX/framerate
        yLoc = self.charVelocityY/framerate
        self.translate(data, xLoc, yLoc)
    
    def keyPress(self, key):
        """Change Velocity based on key press"""
        
        if key == Qt.Key_W or key == Qt.Key_Up:
            self.charVelocityY = -self.SPEED #Forward

        elif key == Qt.Key_S or key == Qt.Key_Down:
            self.charVelocityY = self.SPEED #Backward

        elif key == Qt.Key_A or key == Qt.Key_Left:
            self.charVelocityX = -self.SPEED #Left

        elif key == Qt.Key_D or key == Qt.Key_Right:
            self.charVelocityX = self.SPEED #Right
    
    def keyRelease(self, key):
        """Change Velocity based on key release"""
        
        if key == Qt.Key_W or key == Qt.Key_Up:
            self.charVelocityY = 0 #Forward

        elif key == Qt.Key_S or key == Qt.Key_Down:
            self.charVelocityY = 0 #Backward

        elif key == Qt.Key_A or key == Qt.Key_Left:
            self.charVelocityX = 0 #Left

        elif key == Qt.Key_D or key == Qt.Key_Right:
            self.charVelocityX = 0 #Right
            
