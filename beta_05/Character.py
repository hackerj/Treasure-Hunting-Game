"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.5 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from Loc import Loc
from Globals import *

from PyQt4.QtCore import Qt, pyqtSignal

class Character(Loc):
    """Inherit from Location Objects and add functionality for"""
    SPEED = 1000
    
    def __init__(self, center = (0,0), name = '', objType=None):
        super(Character, self).__init__(center, name, objType)
        
        debug("Character name is", name)
        
        self.charVelocityX = 0  # Gives the X offset to use every frame
        self.charVelocityY = 0  # Gives the Y offset to use every frame
        self.updateSignal = None
        
    def translate(self, xDist, yDist):
        if (self.isValidMove( xDist, yDist)):
            self.x += xDist
            self.y += yDist
            self.changePos.emit(self.x, self.y, self.name)
            #debug("Character is emitting changePos")

    def isValidMove(self, xDist, yDist):
        """Stop Character From walking off the edge of the map"""
        #debug("isValidMove not implemented!")
        checkX = self.x + xDist
        checkY = self.y + yDist
        if (checkX > 2024 or checkX < -2024 or checkY > 2024
                               or checkY < -2024):
            return False
        else:
            return True
    
    def frameUpdate(self, framerate):
        """update character position for the new frame"""
        #debug("character frame update")
        xDist = self.charVelocityX/framerate
        yDist = self.charVelocityY/framerate
        self.translate(xDist, yDist)
    
    def keyPress(self, key):
        #debug("Key Press reaches Character")
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
            
