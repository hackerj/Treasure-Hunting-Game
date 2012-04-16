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
    LOAD_TIME = 2   #seconds
    CLUE_COMMANDS = {"addClue"} #use to check uploaded file
    
    #loadBar = pyqtSignal(int, int)
    searchTime = pyqtSignal()
    clueTrouble = pyqtSignal()
    clueResult = pyqtSignal(str, str)

    
    def __init__(self, frameRate):
        super(QObject, self).__init__()
        #Over Simplified Clue managment.
        #Clue object are represented as dictionaries.
        self._clueList = []
        self.currClue = {}
        
        self.currAction = ('','')
        
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
        self.FRAME_RATE = frameRate
        self.SEARCH_FRAME_COUNT = self.FRAME_RATE * self.LOAD_TIME
        
        self.searchTime.connect(self.searchResults)
        
    # Emits clueTrouble if the player has been stuck on a clue for 5 min
    def frameTime(self):
        if self.timerEnable:
            self.timerCounter += 1
            #self.loadBar.emit(self.timerCounter, self.SEARCH_FRAME_COUNT)
            debug ("Story timer increased, now " + `self.timerCounter`)
            if self.timerCounter == self.SEARCH_FRAME_COUNT:
                debug("Emitting searchTime")
                self.searchTime.emit()
        if self.clueTimeEnable:
            self.clueTime += 1
        if self.clueTime >= self.CLUE_TROUBLE:
            self.clueTrouble.emit()
            debug("Emitting clueTrouble")
            self.clueTime = 0
        
    def searchForClue(self, position):
        if not self.currClue:
            self.currClue['position'] = position
        dist = self.getDistance(position)
        self.timerEnable = True
        debug("Timer now enabled")
        self.clueTimeEnable = False
        if not dist < self.LANDMARK_RADIUS:
            if self.status:
                self.currAction =  ('ClueFailed',
                        "No clue here, must be \n somewhere else")
        elif self._clueList:
            self.currClue = self._clueList.pop()
            self.score += 100
            self.currAction =  ('ClueFound', 
                    self.currClue['text'])
        else:
            self.status = 0
            #self.currAction = ('GameOver', 
                        #"YOU WON!\nBut the game has just begun")
        
    def searchResults(self):
        self.timerEnable = False
        self.timerCounter = 0
        self.clueTimeEnable = True
        debug("SearchResults: Signal accepted")
        self.clueResult.emit(self.currAction[0], self.currAction[1])
        debug("Emitting search result")
        
    def getDistance(self, position):
        """Calculate the distance between character's location and the clue"""
        charX, charY = position
        clueX, clueY = self.currClue['position']
        return ((charX-clueX)**2 + (charY-clueY)**2)**0.5
        
    def troubleFindingClue(self):
        return self.currClue['hint']
        
    def loadClues(self, filename = "saves/story.clue"):
        """load clues from file"""
        filedata = open(filename)
        n = 0
        nextLine = filedata.readline()
        while (nextLine):
            loadClues = nextLine.split(';')
            if (len(loadClues)>2):
                objCommand = loadClues[0]
                if (objCommand in self.CLUE_COMMANDS):
                    clues = filter(lambda x: x!="", loadClues)
                    self.addClues(clues)
            nextLine = filedata.readline()
            
    def addClues(self,obj):
        """add new clues to the clueStack"""    
        clue = {}
        clue['landmark'] = obj[1]
        try:
            int(obj[2]) and int(obj[3])
        except:
            debug("clue position x and y has invalid type, should be int...")
            return
        posx = int(obj[2])
        posy = int(obj[3])
        clue['position'] = (posx, posy)
        clue['text'] = obj[4].replace('\\n ', '\n') # ensure proper formate
        clue['hint'] = obj[5][:-1].replace('\\n ', '\n') #get rid of the return
        self._clueList.append(clue)

   
