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
from PyQt4.QtCore import QTimer, QTime #Provides Time Driven Inputs to Game

#Game is divided into three parts.
from Character import Character     #Represents Player
from Story import Story             #Manages Clues and serves Actions
from Places import Places           #Manages Location Objects

class Game(QObject):
    """Container to hold one new or loaded game instance"""
    def __init__(self):
        """Game Instance Responable For all non visual work"""
        
        #Keep track of how long we have been playing.
        self.gameTime = None
        self.frameTimer = None        
        
        #Manage Character
        self.character = None
        
        #Manage Game Progression
        self.story = Story()
        
        #Manage World
        self.places = Places()
        
    def new(self):
        """Load new game from file"""
        # FIXME load sys here
        self.temporaryLoadSys() 
        None

    def load(self):
        """Load existing game from file"""
        # FIXME load sys here 
        None
    
    def save(self):
        """Save to file"""
        # FIXME save sys here
        None
    
    def endGame(self):
        """Make things tidy for another game instance"""
        
        None
    
    def launch(self):
        """Start sending signals to the game using Timers"""
        None
    
    def temporaryLoadSys(self):
        self.character = Character((0,0), "Character", "Character")
        self.places = Places()
        self.story = Story()
        
        self.places.addLoc( Loc())
        
        