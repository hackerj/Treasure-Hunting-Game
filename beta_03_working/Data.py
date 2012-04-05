# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from random import randint #Only temporary
from View import View      #Everything Graphics Related
from Events import loadGraphics, searchLandmark, initFrames, frameupdate
from os.path import normpath
from newGameData import *

class Data(object):
    LANDMARK_RADIUS = 256

    def __init__(self, debug = True):
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
        self.charSpeed = 1000   # Pixels per second.
        
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

        self.loadDataInitial()
    
    def frame(self):
        frameupdate(self)

    def loadDataInitial(self):
        """Initialize with heap objects"""
        self._initialNewGame() # Load data before init view
        self.view = View(self)      # Initialize view
        loadGraphics(self)          # Initialize graphics
         # Center on the character
        self.view.guiMain.personView.centerOn(self.character.pViewObj)

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

    def _initialNewGame(self):
        """Load data from New Game. Will have additional informations for 
        saved game"""
        
        # Add Background (5x5)
        for i in xrange(-2,2):
            for j in xrange(-2,2):
                #Should replace magic value.
                self.addLoc((i*1024,j*1024),'bg',pViewImag= 'grasstexture2.png')

	# Read Object data from file
        for keys in commands.keys():
            if keys == 'addloc':
                for i in range(len(commands['addloc'])):
                    if len(commands[keys][i]) < 2 :
                           print "TypeError: ", keys," ", 
                           i, " takes at least 2 arguments"
                           pass
                    else:
                        self.loadObj(commands[keys][i])
 
	    if keys == 'addClue':
		for i in range(len(commands[keys])):
		    if len(commands[keys][i]) != 2 :
		            print "TypeError: ", keys," ", i, " takes 2 arguments"
		            pass
		    else:
                        landmark = commands[keys][i]['landmark']
                        text = commands[keys][i]['text']
                        self.addClue(landmark,text)

    def loadObj(self, obj, pos= None, pViewImage = None,mViewImage = None, \
        itemName = None):
        """Interpret the data from file, could be cleaned up and combined 
        with addLoc"""
	
        scale = (-390/2/self.mapScale,-500/2/self.mapScale)
        objType = obj['objType']

        if (objType == 'tree'):
            pViewImage = 'Forest3.png'
            mViewImage = 'tree.png'

        if (objType == 'overlay' or objType == 'bg'):
            pos = scale

        if 'pos' in obj:
            pos = obj['pos']

        if 'pViewImage' in obj:
            pViewImage = obj['pViewImage']            

        if 'mViewImage' in obj:
            mViewImage = obj['mViewImage']
                
        if 'itemName' in obj:
            itemName = obj ['itemName']

        self.addLoc(pos, objType,mViewImage, pViewImage, itemName)          
                   
    def loadData(self,path):
    	None #Not Implemented!

    def saveData(self, path):
        None #Not Implemented!
    
    def addLoc(self, position, objType = None,
                mViewImag=None, pViewImag = None, itemName = None):
        """Helper Function used when loading objects into data for use in the
        person and map view."""
        
        if mViewImag:
            mViewImagPath = normpath("images/"+mViewImag)
        else: mViewImagPath = None
        
        if pViewImag:
            pViewImagPath = normpath("images/"+pViewImag)
        else: pViewImagPath = None
        
        locObj = Loc(position, objType, mViewImag = mViewImagPath, 
                     pViewImag = pViewImagPath)
        
        if objType == 'char':
            self.character = locObj
        else:
            self.places.append(locObj)
        
        if objType == 'landmark' and itemName:
            self.landmarks[itemName] = locObj
            
        if objType == 'overlay' and itemName:
            self.overlays[itemName] = locObj
            
        return

    def addClue(self, landmark, text):
        clue = Clue(landmark, text)
        self.clueStack.append(clue)

 
class Loc(object):
    def __init__(self, position, objType=None,
                 pViewImag = None, mViewImag = None,
                 pViewText = None, mViewText = None):
        """Data container for objects appearing in the person and map views"""

        self.x = position[0]
        self.y = position[1]
        self.objType = objType

        #Person View Data
        self.pViewImag = pViewImag
        self.pViewText = pViewText
        self.pViewObj = None

        #Map View Data
        self.mViewImag = mViewImag
        self.mViewText = pViewText
        self.mViewObj = None
        
    def __repr__(self):
        """Print some info about object for debugging."""
        str = ''
        if self.objType: str += self.objType
        if self.pViewImag: str += self.pViewImag
        elif self.mViewImag: str += self.mViewImag
        return str

    def translate(self, data, xDist, yDist):
        if (self.isValidMove(data, xDist, yDist)):
            self.x += xDist
            self.y += yDist
            self.updatePViewObj()
            self.updateMViewObj(data.mapScale)

            # Update the step count to erase outdated messages
            data.stepCount += 1
            if (data.stepCount > 5 and data.gameStatus):
                data.view.guiMain.clueView.setText(data.currClue.text)
                data.stepCount = 0

    def isValidMove(self, data, xDist, yDist):
        checkX = self.x + xDist
        checkY = self.y + yDist
        if (checkX > data.maxX or checkX < data.minX or checkY > data.maxY 
                               or checkY < data.minY):
            return False
        else:
            return True
        
    
    def getCenter(self):
        #print dir(self.pViewObj.pixmap)
        
        return self.x + self.pViewObj.pixmap().width()/2, \
               self.y + self.pViewObj.pixmap().height()/2

        try:
            self.x + self.pViewObj.width()/2, \
                   self.y + self.pViewObj.height()/2
        except:
            print "could not find center", self
            print dir(self.pViewObj)
        
        
    def updatePViewObj(self):
        try:
            self.pViewObj.setX(self.x)
            self.pViewObj.setY(self.y)
        except:
            print 'Could not update person view', self.test, \
                  'from', self.x, self.y
                  
    def updateMViewObj(self, mapScale):
        if (self.pViewImag):
            newx, newy = self.getCenter()
        else:
            newx, newy = self.x, self.y
            #print 'no pView'
        self.mViewObj.setX(newx * mapScale)
        self.mViewObj.setY(newy * mapScale)
            
class Clue(object):
    """Definition of a clue"""
    def __init__(self, targetLandmark, text):
        self.text = text
        self.targetLandmark = targetLandmark
        
