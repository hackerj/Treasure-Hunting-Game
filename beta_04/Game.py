"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

# Game uses signals to communicate
from PyQt4.QtCore import QObject, pyqtSignal

# Game takes inputs based on time.
from PyQt4.QtCore import QTimer, QTime #Provides Time Driven Inputs to Game

# Game is divided into three parts.
from Character import Character     # Represents Player
from Story import Story             # Manages Clues and serves Actions
from Places import Places           # Manages Location Objects

class Game(QObject):
    """Container to hold one new or loaded game instance"""
    FRAME_RATE = 25 # Frame rate in frames per second.
    
    def __init__(self):
        """Game Instance responsible For all non visual work"""
        
        # Keep track of how long we have been playing.
        self.gameTime = None
        self.frameTimer = None        
        
        # Manage Character
        self.character = None
        
        # Manage Game Progression
        self.story = Story(FRAME_RATE)
        
        # Manage World
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
        self.gameTime.start()
        self.frameTimer.start(ONE_SECOND/FRAME_RATE)
        self.frameTimer.timeout.connect(self.frameUpdate)
    
    def temporaryLoadSys(self):
        """For testing game independed of normal save and load 
        funcitonality"""
        
        self.gameTime = QTime()
        self.frameTimer = QTimer() # Create Frame Timer
        
        debug("loading charcter")
        self.character = Character((0,0), "Character", "Character")
    
        self.places.addLoc( Loc())
        
    def keyPress(self, event):
        
        
    def keyRelease(self, event):
        None
        
    def frameUpdate(self):
        self.story.frameTime()
        self.character.frameUpdate(FRAME_RATE)
        
        
        
        
