"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.5 using PyQt4.9
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

from operator import itemgetter

class Game(QObject):
    """Container to hold one new or loaded game instance"""
    FRAME_RATE = 25 # Frame rate in frames per second.
    
    def __init__(self):
        """Game Instance responsible For all non visual work"""
        
        # Keep track of how long we have been playing.
        self.gameTime = None
        self.frameTimer = QTimer()
        
        # Manage Character
        self.character = None
        
        # Manage Game Progression
        self.story = Story(self.FRAME_RATE)
        
        # Manage World
        self.places = Places()
        
        # Store player's name
        self.playerName = ""
        
        # Store scores from previous play
        self.scoreList = []
        self.topTen = True
        
    def new(self):
        """Load new game from file"""
        debug("newgame...loading clues")
        self.story.loadClues()
        debug("newgame...loading charcter")
        self.character = Character((0,0), "Character", "Character")
        debug("newgame...loading places")
        self.places.loadLoc()
        debug("end of load")
        self.places.addLoc(self.character)
        self.story.currClue = self.story._clueList.pop()
        #self.frameTimer = QTimer() # Create Frame Timer
        self.gameTime = QTime()
        self.launch()
        
    def load(self,filename):
        """Load existing game from file"""
        
        debug("loadgame...read data from saved file")
        debug("loadgame...loading clues")
        self.story.loadClues()
        
        savedData = open(filename)    
        nextLine = savedData.readline()
        # Parsing saved file
        while (nextLine):
            line = nextLine.split()
            if (len(line) == 5 and self.loadIsValid(line)):
                x = int(line[0])
                y = int(line[1])
                numClues = int(line[2])+1
                self.story._clueList =  self.story._clueList[:numClues]
                self.story.score = int(line[3])
                self.playerName = line[4]
            nextLine = savedData.readline()       
        savedData.close()
        self.story.currClue = self.story._clueList.pop()
        
        debug("loadgame...loading initial character and places")
        self.character = Character((x,y), "Character", "Character")
        self.places.loadLoc()
        
        debug("end of load")
        self.places.addLoc(self.character)
        # FIXME if QTime and QTimer should be stored in certain way
        self.gameTime = QTime()
        #self.frameTimer = QTimer() # Create Frame Timer
        self.launch()
      
    def loadIsValid(self,obj):
        """Check that the input from saved file is valid"""         
        posx = obj[0]
        posy = obj[1]
        numClue = obj[2]
        score = obj[3]
        try:
            int(posx) and int(posy) and int(numClue) and int(score)
        except:
            debug("Invalid position input in save file")
            return False
        return True
    
    def loadScores(self, filename = "saves/player.score"):
        """load the 10 highest score from file"""
        scoreData = open(filename)    
        nextLine = scoreData.readline()
        # Parsing saved file
        while (nextLine):
            prevScore = nextLine.strip().split(";")
            if (len(prevScore) == 2):
                loadedName = prevScore[0]
                loadedScore = int(prevScore[1])
                self.scoreList.append((loadedName, loadedScore))
            nextLine = scoreData.readline()       
        scoreData.close()
        self.addCurrScoreToList()
    
    def addCurrScoreToList(self):
        """save player's score into top 10 list if the player make it"""
        listLen = len(self.scoreList)
        lowestScore = 0
        
        if (listLen > 0):
            lowestScore = self.scoreList[-1][1]
        if (self.story.score <= lowestScore and listLen > 9):
            debug("player's score is not high enough to write to file")
            self.topTen = False
            return
        elif listLen < 10:
            debug("Player score append to scoreList")
            self.scoreList.append((self.playerName, self.story.score))
        else:
            debug("Pop the bad score, and add in player score to file")
            self.scoreList.pop()
            self.scoreList.append((self.playerName, self.story.score))
        # sorted previous player by score
        self.scoreList = sorted(self.scoreList, \
                                key = itemgetter(1), reverse = True) 
        
    def writeScoreToFile(self, filename = "saves/player.score"):
        """Save the 10 highest score to file.."""
        text = ""
        if (len(self.scoreList)<=10):
            scoreFile = open(filename, "w")
            while (self.scoreList):
                scores = self.scoreList.pop()
                text = text + scores[0] + ";" + `scores[1]` + "\n"
            scoreFile.write(text)
            scoreFile.close()
        else:
            print "Error: Too many scores to be stored in scoreList"
            return    
        
    def save(self, filename):
        """Save to file"""
        fname = open(filename, "w")
        score = `self.story.score`
        numClues = `len(self.story._clueList)`
        charX, charY = self.character.getCenter()
        name = self.playerName
        toWriteList = '\t' + `charX` + '\t' + `charY` + '\t' \
                       + numClues + '\t'+ score + '\t'+ name
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
        
    def keyPress(self, event):
        """Recieve events from keyboard, pass to update character movement"""
        key = event.key()
        self.character.keyPress(key)
        
    def keyRelease(self, event):
        """Recieve events from keyboard, pass to update character movement"""
        key = event.key()
        self.character.keyRelease(key)

