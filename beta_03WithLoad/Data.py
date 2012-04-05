# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from random import randint #Only temporary
from View import View      #Everything Graphics Related
from Events import loadGraphics, searchLandmark, initFrames, frameupdate
from Load import *
from Loc import Loc, Clue



class Data(object):
    LANDMARK_RADIUS = 256
 
    def __init__(self,debug = True):
        """Initialize with defaults"""
        self.gameStatus = 1
        self.debug = debug
        self.places = []    # graphics objects (non cities)
        self.overlays = {}  # a dictionary of overlays

        self.maxX = self.minX = 0 # Size of the world for bounds checking
        self.maxY = self.minY = 0 # Size of the world for bounds checking
        
        self.character =  None    # A special Loc for our character
        self.charVelocityX = 0 # Gives the X offset to use every frame
        self.charVelocityY = 0 # Gives the Y offset to use every frame
        self.charSpeed = 1000       # Now based on keyboard should be pixles per second.
        
        self.landmarks = {}       # dictionary of cities.
        self.currLandmark = None  # City with current Clue
        
        self.currClue = None   # Current Clue
        self.clueStack = []    # A list of clues
        
        self.stepCount = 0     # Step counter for erasing updates

        self.score = 0
        
        self.view = None       # Container for PyQt specific data and widgets
        self.mapScale = 0.1
        
        self.timer = None      # Place for Qtimer object
        
        self.framerate = 25    # Number of frames per second.
        self.keys = None       # Keeping track of directional keys
        
       
        self.initNewGame()
        #self.loadSavedGame()
        
    def frame(self):
        frameupdate(self)

    def initNewGame(self):
        """Initialize with heap objects"""
        
        loadNewGame(self, "load.txt", False)  # Initialize data from file
        
        self.view = View(self)      # Initialize view
        loadGraphics(self)          # Initialize graphics
        self.view.guiMain.personView.centerOn(self.character.pViewObj); # Center on the character
        self.view.guiMain.mapView.centerOn(self.character.mViewObj)
        # Set boundaries (Hard Coded values at the mommment perhaps 
        # implement automatic bounds checking later)
        self.maxX = 1768
        self.minX = -2024
        self.maxY = 2024
        self.minY = -2024
        
        #Add overlays
        
        self.overlays['latLongOverlay'].mViewObj.setVisible(False)
        self.overlays['colorOverlay'].mViewObj.setVisible(False)
        self.overlays['legendOverlay'].mViewObj.setVisible(False)
        
        #Initial search yields first clue.
        searchLandmark(self)
        
        #Initialize frames
        initFrames(self)
        
    def loadSavedGame(self):
        
        loadNewGame(self, "load.txt", True)  # Initialize data from file
        
        self.view = View(self)      # Initialize view
        loadGraphics(self)          # Initialize graphics
        self.view.guiMain.personView.centerOn(self.character.pViewObj); # Center on the character
      
        # Set boundaries (Hard Coded values at the mommment perhaps 
        # implement automatic bounds checking later)
        self.maxX = 1768
        self.minX = -2024
        self.maxY = 2024
        self.minY = -2024
        
        #Add overlays
        
        self.overlays['latLongOverlay'].mViewObj.setVisible(False)
        self.overlays['colorOverlay'].mViewObj.setVisible(False)
        self.overlays['legendOverlay'].mViewObj.setVisible(False)
        
        #Initial search yields first clue.
        searchLandmark(self)
        
        #Initialize frames
        initFrames(self)
        
                        
           
