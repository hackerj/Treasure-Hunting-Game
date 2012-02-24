# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from random import randint #Only temporary
from View import View      #Everything Graphics Related
from Events import loadGraphics

class Data(object):
    CITY_RADIUS = 256

    def __init__(self, debug = True):
        "Initialize with defaults"
        self.debug = debug
        self.places = []       # graphics objects (non cities)
        
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
        self._temperaryLoadSystem1() # Load data before init view
        self.view = View(self)      # Initialize view
        loadGraphics(self)          # Initialize graphics

    def _temperaryLoadSystem1(self):
        "Use untill we have a save and load system"
        #Add Person View Background
        bgSize = 1024
        for i in xrange(-2,2):
            for j in xrange(-2,2):
                self.places.append(
                    Loc((i*bgSize,j*bgSize), 'bg',
                        pViewImag = 'grasstexture2.png'))
                        
        #Add Map View Background
        self.places.append(Loc((-390/2/self.mapScale,-500/2/self.mapScale),
                               'bg', mViewImag = 'mapBackground.png'))
        
        #Add Trees
        numTrees = 7
        for i in xrange(numTrees):
            treeX = randint(-1300,700)
            treeY = randint(-800,600)
            self.places.append(Loc((treeX, treeY), 'tree',
                                    pViewImag = 'Forest3.png',
                                    mViewImag = 'treeSymbol.png'))

        #Add Trees
        numCites = 3
        for i in xrange(numCites):
            cityX = randint(-500,500)
            cityY = randint(-500,500)
            self.places.append(Loc((cityX, cityY), 'city',
                                    pViewImag = 'city2.png',
                                    mViewText = 'City'))
        
        #Add Character
        self.character = Loc((0,0), 'char',
                             pViewImag='circle.png',
                             mViewImag='circle.png')


    def _temperaryLoadSystem2(self):
        None
                             
    def loadDataFromUserFile(self, path):
        None #Not Implemented!

    def saveData(self, path):
        None #Not Implemented!
    
    def addPlace(self):
        None #Not Implemented!


class Loc(object):
    def __init__(self, position = (0,0), objType=None,
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
        try:
            return city.x + city.pViewObj.width/2, \
                   city.y + city.pViewObj.hight/2
        except:
            print "could not find center"
            
    def updatePViewObj(self):
        try:
            self.pViewObj.setX(self.x)
            self.pViewObj.setY(self.y)
        except:
            print 'Could not update person view', self.test, \
                  'from', self.x, self.y
                  
    def updateMViewObj(self, mapScale):
        #try:
        self.mViewObj.setX(self.x * mapScale)
        self.mViewObj.setY(self.y * mapScale)
        #except:
        #    print 'Could not update map view', self.text, \
        #         'from', self.x, self.y
            
class clue(object):
    def __init__(self, data, difficulty = 0, target= None, 
                 cityName = None, text = ''):
        self.data = data
        self.difficulty = difficulty
        self.target = target
        self.cityName = cityName
        self.text = text
