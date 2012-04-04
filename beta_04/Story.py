"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QObject, pyqtSignal, QTimer
from Globals import *

class Story(QObject):
    """Manage what happens in the game"""
    
    # Declare Constants to avoid Magic Values
    LANDMARK_RADIUS = 256
    CLUE_TROUBLE = 1000 * 60 * 5

    def __init__(self):
        #Over Simplified Clue managment.
        #Clue object are represented as dictionaries.
        self._clueList = []
        self.currClue = {}
        self.loadData() #initial clues from file
        
        #Keep the score for the game.
        self.score = 0
        
        #Is the game running or over?
        self.status = 1
        
        #Measure Time
        self.clueTime = 0
        self.clueTimeEnable = True
        self.messageFade = None
        self.timerCounter = 0
        self.timerEnable = False
        self.searchTime = pyqtSignal(float)
        self.clueTrouble = pyqtSignal()
        
        
        
    # Emits clueTrouble if the player has been stuck on a clue for 5 min
    def frameTime(self):
        if self.timerEnable:
            self.timerCounter += 1
        if self.clueTimeEnable:
            self.clueTime += 1
        if self.clueTime >= CLUE_TROUBLE:
            self.clueTrouble.emit()
            self.clueTime = 0
        
    # Emits searchTime(float). The float is between 0 and 1.
    def searchForClue(self, position, framerate):
        if not self.currClue:
            self.currClue['position'] = position
        dist = self.getDistance(position)
        self.timerEnable = True
        self.clueTimeEnable = False
        while self.timerCounter <= framerate*5:
            self.searchTime.emit(float(self.timerCounter)/(framerate*5))
        self.timerEnable = False
        self.clueTimeEnable = True
        self.timerCounter = 0
        if not dist < LANDMARK_RADIUS:
            if self.status:
                return ('ClueFailed',
                        "No clue here, must be \n somewhere else")
        if self.clueStack:
            self.currClue = self.clueStack.pop()
            self.score += 100
            return ('ClueFound', 
                    currClue['text'])
        else:
            self.gameStatus = 0
            return ('GameOver', "YOU WON!\nBut the game has just begun")
        
    def getDistance(self, position):
        """Calculate the distance between character's location and the clue"""
        charX, charY = position
        clueX, clueY = self.currClue['position']
        return ((charX-clueX)**2 + (charY-clueY)**2)**0.5
        
    def troubleFindingClue(self):
        return self.currClue['hint']
        
    def loadData(self, filename = "saves/story.clue"):
        """load clues from file"""
        
        CLUE_COMMANDS = {"addClue"}
        filedata = open(filename)
        n = 0
        nextLine = filedata.readline()
        while (nextLine):
            loadClues = nextLine.split('\t')
            if (len(loadClues)>2):
                objCommand = loadClues[0]
                if (objCommand in CLUE_COMMANDS):
                    clues = filter(lambda x: x!="", loadClues)
                    self.addClues(clues)
            nextLine = filedata.readline()
            
        
    def addClues(self,obj):
        """add new clues to the clueStack"""    
        
        clue = {}
        clue['landmark'] = obj[1]
        clue['text'] = obj[2].replace('\\n ', '\n') # ensure proper formate
        clue['hints'] = obj[3].replace('\\n ', '\n')
        self._clueList.append(clue)
        
        
        
