# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from random import randint #Only temporary
from View import View      #Everything Graphics Related
from Events import loadGraphics, searchLandmark
from os.path import normpath

class Data(object):
    LANDMARK_RADIUS = 256

    def __init__(self, debug = True):
        "Initialize with defaults"
        self.debug = debug
        self.places = []       # graphics objects (non cities)
        self.overlays = {}     # a dictionary of overlays

        # Size of the world for bounds checking
        self.maxX = 0
        self.minX = 0
        self.maxY = 0
        self.minY = 0
        
        self.character =  None # A special Loc for our character
        self.charSpeed = 10
        
        self.landmarks = {}       # dictionary of cities.
        self.currLandmark = None   # City with current Clue
        
        self.currClue = None   # Current Clue
        self.clueStack = []    # A list of clues
        
        self.stepCount = 0    # Step counter for erasing updates

        self.score = 0
        
        self.view = None       # Container for PyQt specific data and widgets
        self.mapScale = 0.1

        self.loadDataInitial()

    def loadDataInitial(self):
        "Initialize with heap objects"
        self._temperaryLoadSystem() # Load data before init view
        self.view = View(self)      # Initialize view
        loadGraphics(self)          # Initialize graphics
        self.view.guiMain.personView.centerOn(self.character.pViewObj); # Center on the character

        # Set boundaries
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

    def _temperaryLoadSystem(self):
        "Used by loadData Initial until we create a save and load system."
        # Add Background
        for i in xrange(-2,2):
            for j in xrange(-2,2):
                self.addLoc((i*1024,j*1024),'bg',pViewImag= 'grasstexture2.png')
        
        self.addLoc((-390/2/self.mapScale,-500/2/self.mapScale), 'bg',
                    mViewImag = 'mapBackground.png')
        
        # Add Trees
        treeList = [(200,158), (-800,45),(120,80), (310,470), 
                    (220, -400), (100,500)]
        
        for position in treeList:
            self.addLoc(position, 'tree', pViewImag = 'Forest3.png', 
                        mViewImag = 'tree.png')
                     
        # Add Cities
        self.addLoc((-350, 100), 'landmark', pViewImag = 'city2.png',
                     mViewImag = 'city.png', itemName = 'city0')
        
        self.addLoc((-450, 910), 'landmark', pViewImag = 'city2.png', 
                     mViewImag = 'city.png', itemName = 'city1')
                     
        self.addLoc((450, -700), 'landmark', pViewImag = 'city2.png', 
                     mViewImag = 'city.png', itemName = 'city2')
                     
        #Add Color overlay
        self.addLoc((-390/2/self.mapScale,-500/2/self.mapScale), 'overlay',
                    mViewImag = 'colorOverlay.png', itemName = 'colorOverlay')
                     
        #Add Lat/Long overlay
        self.addLoc((-390/2/self.mapScale,-500/2/self.mapScale), 'overlay',
                    mViewImag = 'latOverlay.png', itemName = 'latLongOverlay')
                    
        #Add Legend overlay
        self.addLoc((-390/2/self.mapScale,-500/2/self.mapScale), 'overlay',
                    mViewImag = 'legendOverlay.png', itemName = 'legendOverlay')
        
        # Add Character
        self.addLoc((0,0),'char',pViewImag='circle.png', mViewImag='circle.png')
        
        # Add Clues:
        # Clue 3
        self.addClue('city1',
                     "For this final clue\n"
                     "Look to the city most southernly")
        # Clue 2
        self.addClue('city0',
                     "Check 37.8 deg latitude\n"
                     "(Distance from Equator)")
        # Clue 1     
        self.addClue('city2', 
                     "Search for the second Clue \n"
                     "in the northern most city")

                             
    def loadDataFromUserFile(self, path):
        None #Not Implemented!

    def saveData(self, path):
        None #Not Implemented!
    
    def addLoc(self, position, objType = None,
                mViewImag=None, pViewImag = None, itemName = None):
        "Helper Function used when loading objects  into data for use in the"
        "into the person and map view."
        
        if mViewImag:
            mViewImagPath = normpath("images/"+mViewImag)
        else: mViewImagPath = None
        
        if pViewImag:
            pViewImagPath = normpath("images/"+pViewImag)
        else: pViewImagPath = None
        
        locObj = Loc(position, objType, mViewImag = mViewImagPath, pViewImag = pViewImagPath)
        
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
        "Data container for objects appearing in the person and map views"

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
        "Print some info about object for debuging."
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
            if (data.stepCount > 5):
                data.view.guiMain.clueView.setText(data.currClue.text)
                data.stepCount = 0

    def isValidMove(self, data, xDist, yDist):
        checkX = self.x + xDist
        checkY = self.y + yDist
        if (checkX > data.maxX or checkX < data.minX or checkY > data.maxY or checkY < data.minY):
            return False
        else:
            return True
        
    
    def getCenter(self):
        #print dir(self.pViewObj.pixmap)
        
        return self.x + self.pViewObj.pixmap().width()/2, self.y + self.pViewObj.pixmap().height()/2

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
            print 'no pView'
        self.mViewObj.setX(newx * mapScale)
        self.mViewObj.setY(newy * mapScale)
            
class Clue(object):
    def __init__(self, targetLandmark, text):
        self.text = text
        self.targetLandmark = targetLandmark
