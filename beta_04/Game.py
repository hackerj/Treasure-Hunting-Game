"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

#Game uses signals to communicate
from PyQt4.QtCore import QObject, pyqtSignal

#Game takes inputs based on time.
from Timer import Timer             #Provides Time Driven Inputs to Game

#Game is divided into three parts.
from Character import Character     #Represents Player
from Story import Story             #Manages Clues and serves Actions
from Places import Places           #Manages Location Objects

class Game(QObject):
    """Container to hold one new or loaded game instance"""
    def __init__(self):
        """Game Instance Responable For all non visual work"""
        
        #Init Time Inputs
        self.timer = Places()
        
        #Manage Character
        self.character = Character()
        
        #Manage Game Progression
        self.story = Story()
        
        #Manage World
        self.places = Places()
        
        #Keep the score for the game.
        self.score = 0
        
    def initNew(self):
        """Load new game from file"""
        None

    def initSaved(self):
        """Load existing game from file"""
        None
    
    def endGame(self):
        """Make things tidy for another game instance"""
        None     
    