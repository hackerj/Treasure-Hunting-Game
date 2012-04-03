"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QObject, pyqtSignal

#Game takes inputs based on time.
from PyQt4.QtCore import QTimer, QTime #Provides Time Driven Inputs to Game
from Globals import *

class Story(QObject):
    """Manage what happens in the game"""
    
    # Declare Constants to avoid Magic Values
    LANDMARK_RADIUS = 256
    
    def __init__(self):
        #Over Simplified Clue managment.
        #Clue object are represented as dictionaries.
        self._cluelist = []
        self.currClue = {}
        
        #Keep the score for the game.
        self.score = 0
        
        #Is the game running or over?
        self.status = 1
        
        #Measure Time
        self.clueTime = None
        self.clueTroubleTimer = None
        self.searchProgress = None
        self.messageFade = None
        self.timerCounter = 0
        self.timerEnable = False
        
    def frameTime(self):
        if self.timerEnable:
            self.timerCounter += 1
        
    def foundClue(self):
        None
        
    def searchForClue(self, position):
        if not self.currClue:
            self.currClue['position'] = position
        dist = getDistance(position)
        searchTime = pyqtSignal(float)
        while self.timerCounter < 
        if not dist < LANDMARK_RADIUS:
            if self.status:
                
        
    def getDistance(self, position):
        charX, charY = position
        clueX, clueY = currClue['position']
        return ((charX-clueX)**2 + (charY-clueY)**2)**0.5
        
    def troubleFindingClue(self):
        None
        
    def loadData(self):
        None
    
    def launch(self):
        """Start sending signals to the game using Timers"""
        None
        
