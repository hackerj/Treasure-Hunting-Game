"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QObject

#Game takes inputs based on time.
from PyQt4.QtCore import QTimer, QTime #Provides Time Driven Inputs to Game

class Story(QObject):
    def __init__(self):
        #Over Simplified Clue managment.
        #Clue object are represented as dictionaries.
        self._cluelist = []
        self.curClue = None
        
        #Keep the score for the game.
        self.score = 0
        
        #Measure Time
        self.clueTime = None
        self.clueTroubleTimer = None
        self.searchProgress = None
        self.messageFade = None
        
    def foundClue(self):
        None
        
    def searchForClue(self, position):
        None
        
    def troubleFindingClue(self):
        None
        
    def loadData(self):
        None
    
    def launch(self):
        """Start sending signals to the game using Timers"""
        None
        
