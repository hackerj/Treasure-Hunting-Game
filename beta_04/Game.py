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

from Globals import *

# Game is divided into three parts.
from Character import Character     # Represents Player
from Story import Story             # Manages Clues and serves Actions
from Places import Places           # Manages Location Objects
from Loc import Loc                 # Location Objects


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
        self.story = Story(self.FRAME_RATE)
        
        # Manage World
        self.places = Places()
        
    def new(self):
        """Load new game from file"""
        
        self.gameTime = QTime()
        self.frameTimer = QTimer() # Create Frame Timer
        debug("newgame...loading charcter")
        self.character = Character((0,0), "Character", "Character")
        debug("newgame...loading places")
        self.places.loadLoc()
        self.launch()
        
    def load(self,filename):
        """Load existing game from file"""
        # FIXME if QTime and QTimer should be stored in certain way
        self.gameTime = QTime()
        self.frameTimer = QTimer() # Create Frame Timer
        
        debug("loadgame...loading initial character and places")
        self.character = Character((0,0), "Character", "Character")
        self.places.loadLoc()
        
        debug("loadgame...read data from saved file")
        savedData = open(filename)    
        nextLine = savedData.readline()
        x = 0
        y = 0
        
        # Parsing saved file
        while (nextLine):
            line = nextLine.split()
            if (len(line) == 4 and self.loadIsValid(line)):
                x = int(line[0])
                y = int(line[1])
                numClues = int(line[2])
                self.places.clueStack = self.story._clueList[:numClues]
                self.places.score = int(line[3])     
        
            nextLine = savedData.readline()
        
        savedData.close()
    
    def loadIsValid(self,obj):
        """Check that the input from saved file is valid"""         
        posx = obj[0]
        posy = obj[1]
        numClue = obj[2]
        score = obj[3]
        try:
            int(posx) and int(posy) and int(numClue) and int(score)
        except:
            print "Invalid position input"
            return False
        return True
    
    def save(self, filename):
        """Save to file"""
        fname = open(filename, "w")
        score = `self.story.score`
        numClues = `len(self.story._clueList)`
        charX, charY = self.character.getCenter()
        toWriteList = '\t' + `charX` + '\t' + `charY` + '\t' + \
                        numClues + '\t' + score
        fname.write(toWriteList)     
        fname.close()
    
    def endGame(self):
        """Make things tidy for another game instance"""
        # Signal that we have won the game and should
        None
    
    def launch(self):
        """Start sending signals to the game using Timers"""
        self.gameTime.start()
        self.frameTimer.start(ONE_SECOND/self.FRAME_RATE)
        self.frameTimer.timeout.connect(self.story.frameTime)
    
    def temporaryLoadSys(self):
        """For testing game independed of normal save and load 
        funcitonality"""
        None
        
        
    def keyPress(self, event):
        key = event.key()
        self.character.keyPress(key)
        
        
    def keyRelease(self, event):
        None
        
    def frameUpdate(self):
        self.story.frameTime()
        self.character.frameUpdate(FRAME_RATE)
        
        
        
        
