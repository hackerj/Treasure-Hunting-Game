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
    def __init__(self, debug = True):
        "Initialize with defaults"
        self.debug = debug
        self.places = []       # A list of Locs (e.g. cities).
        self.character =  None # A special Loc for our character
        self.charSpeed = 5
        self.clues = []         # A list of clues for the game.
        self.view = None       # A container for PyQt specific data and widgets
        self.mapScale = 0.2

        self.loadDataInitial()

    def loadDataInitial(self):
        "Initialize with heap objects"
        self._temperaryLoadSystem() #Load data before init view
        self.view = View(self)          #Initialize view
        loadGraphics(self)          #Initialize graphics

    def _temperaryLoadSystem(self):
        "Use untill we have a save and load system"
        #Add Person View Background
        bgSize = 1024
        for i in xrange(-1,1):
            for j in xrange(-1,1):
                self.places.append(
                    Loc((i*bgSize,j*bgSize), 'bg', 'bg',
                        pViewImag = 'grasstexture2.png'))
                        
        #Add Map View Background
        self.places.append(Loc((-390/2/self.mapScale,-500/2/self.mapScale), 'bg', 'bg',
                        mViewImag = 'mapBackground.png'))
        
        #Add Trees
        numTrees = 7
        for i in xrange(numTrees):
            treeX = randint(-500,500)
            treeY = randint(-500,500)
            self.places.append(Loc((treeX, treeY), 'tree','tree',
                                    pViewImag = 'Forest3.png',
                                    mViewImag = 'treeSymbol.png'))

        
        #Add Character
        self.character = Loc((0,0), 'char','x',
                             pViewImag='circle.png',
                             mViewImag='circle.png')

    def loadDataFromUserFile(self, path):
        None #Not Implemented!

    def saveData(self, path):
        None #Not Implemented!


class Loc(object):
    def __init__(self, position = (0,0), text='', objType=None,
                 pViewImag = None, mViewImag = None):

        self.x = position[0]
        self.y = position[1]
        self.text = text
        self.objType = objType

        self.clue = None

        #Person View Data
        self.pViewImag = pViewImag
        self.pViewObj = None

        #Map View Data
        self.mViewImag = mViewImag
        self.mViewObj = None

    def translate(self, data, xDist,yDist):
        self.x += xDist
        self.y += yDist
        self.updatePViewObj()
        self.updateMViewObj(data.mapScale)

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
    def __init__(self, data, difficulty = 0, target= None, loc = None, text = ''):
        self.data = data
        self.difficulty = difficulty
        self.target = target
        self.loc = loc
        self.text = text

    def drawNewClue(self):
        None


