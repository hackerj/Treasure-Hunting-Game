# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from random import randint #Only temporary
from View import View      #Everything Graphics Related
from Events import loadGraphics, searchCity
from os.path import normpath

class Data(object):
    CITY_RADIUS = 256

    def __init__(self, debug = True):
        "Initialize with defaults"
        self.debug = debug
        self.places = []       # graphics objects (non cities)
        self.overlays = {}     # a dictionary of overlays
        
        self.character =  None # A special Loc for our character
        self.charSpeed = 5
        
        self.cities = {}       # dictionary of cities.
        self.currCity = None   # City with current Clue
        
        self.currClue = None   # Current Clue
        self.clueStack = []    # A list of clues
        
        self.view = None       # Container for PyQt specific data and widgets
        self.mapScale = 0.1

        self.loadDataInitial()

    def loadDataInitial(self):
        "Initialize with heap objects"
        self._temperaryLoadSystem2() # Load data before init view
        self.view = View(self)      # Initialize view
        loadGraphics(self)          # Initialize graphics
        
        #Hack to get overlays to work
        self.overlays['latLongOverlay'].mViewObj.setVisible(False)
        
        #Initial Search Yealds first clue.
        searchCity(self)

    def _temperaryLoadSystem2(self):
        # Add Background
        for i in xrange(-2,2):
            for j in xrange(-2,2):
                self.addLoc((i*1024,j*1024),'bg',pViewImag= 'grasstexture2.png')
        
        self.addLoc((-390/2/self.mapScale,-500/2/self.mapScale), 'bg',
                    mViewImag = 'mapBackground.png')
        
        # Add Trees
        treeList = [(200,158), (80,45),(120,80), (310,470), 
                    (220, -400), (-200,500)]
        
        for position in treeList:
            self.addLoc(position, 'tree', pViewImag = 'Forest3.png', 
                        mViewImag = 'tree.png')
                     
        # Add Cities
        self.addLoc((-350, 100), 'city', pViewImag = 'city2.png',
                     mViewImag = 'city.png', itemName = 'city0')
        
        self.addLoc((-450, 700), 'city', pViewImag = 'city2.png', 
                     mViewImag = 'city.png', itemName = 'city1')
                     
        self.addLoc((450, -700), 'city', pViewImag = 'city2.png', 
                     mViewImag = 'city.png', itemName = 'city2')
                     
        #Add Lat/Long overlay
        self.addLoc((-390/2/self.mapScale,-500/2/self.mapScale), 'overlay',
                    mViewImag = 'latOverlay.png', itemName = 'latLongOverlay')
        
        # Add Character
        self.addLoc((0,0),'char',pViewImag='circle.png', mViewImag='circle.png')
        
        # Add Clues:
        self.addClue('city2', 
                     "For this final clue look\n"
                     "Look to the city most southernly")
        
        # Add Clues:
        self.addClue('city2', 
                     "For this final clue look\n"
                     "Look to the city most southernly")
        self.addClue('city1', 
                     "For this first clue\n"
                     "You must journey north")
                             
    def loadDataFromUserFile(self, path):
        None #Not Implemented!

    def saveData(self, path):
        None #Not Implemented!
    
    def addLoc(self, position, objType = None,
                mViewImag=None, pViewImag = None, itemName = None):
        
        if mViewImag:
            mViewImagPath = normpath("./images/"+mViewImag)
        else: mViewImagPath = None
        
        if pViewImag:
            pViewImagPath = normpath("./images/"+pViewImag)
        else: pViewImagPath = None
        
        locObj = Loc(position, objType, mViewImag = mViewImagPath, pViewImag = pViewImagPath)
        
        if objType == 'char':
            self.character = locObj
        else:
            self.places.append(locObj)
        
        if objType == 'city' and itemName:
            self.cities[itemName] = locObj
            
        if objType == 'overlay' and itemName:
            self.overlays[itemName] = locObj
            
        return

    def addClue(self, city, text):
        clue = Clue(city, text)
        self.clueStack.append(clue)

 
class Loc(object):
    def __init__(self, position, objType=None,
                 pViewImag = None, mViewImag = None,
                 pViewText = None, mViewText = None):

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
        str = ''
        if self.objType: str += self.objType
        if self.pViewImag: str += self.pViewImag
        elif self.mViewImag: str += self.mViewImag
        return str

    def translate(self, data, xDist,yDist):
        self.x += xDist
        self.y += yDist
        self.updatePViewObj()
        self.updateMViewObj(data.mapScale)
    
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
    def __init__(self, targetCity, text):
        self.text = text
        self.targetCity = targetCity