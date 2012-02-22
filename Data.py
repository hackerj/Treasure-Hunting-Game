# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from random import randint #Only temporary

class Data(object):
    def __init__(self):
        self.places = []       # A list of Locs (e.g. cities).
        self.character =  None # A special Loc for our character (only one)
        self.clues = []         # A list of clues for the game.
        self.view = None       # A container for PyQt specific data and widgets
        
    def loadDataInitial(self):
        #Initialize View
        self.view = View()
        self._temperaryLoadSystem()
        
        #There really should be more stuff here.
        
    def _temperaryLoadSystem(self):
        bgSize = 1024

        for i in xrange(-1,1):
            for j in xrange(-1,1):
                self.places.append(Loc(image = 'grasstexture2.png', position = (i*bgSize,j*bgSize)))
        numTrees = 7
        for i in xrange(numTrees):
            treeX = randint(-500,500)
            treeY = randint(-500,500)
            self.places.append(Loc(image = 'Forest3.png', 
			           position = (treeX, treeY))) 
        
        self.character = Loc(image='circle.png', position = (0,0))
    
    def loadDataFromUserFile(self, path):
        None #Not Implemented!

    def saveData(self, path):
        None #Not Implemented!

    def addPlace(graphObject, position = (0,0)):
        place = Loc(graphicObject = graphObject)
        self.places.append(place)
    
class Loc(object):
    def __init__(self, name=None, image = None, clue = None, objType=None,
                 position = (0,0)):
        self.name = name
        self.image = image
        self.clue = clue
        self.objType = objType
        self.x = position[0]
        self.y = position[1]
        self.pViewObj = None
        self.mViewObj = None

    def translate(self, data, xDist,yDist):
        self.x += xDist
        self.y += yDist
        self.updatePViewObj()

    def updatePViewObj(self):
        try:
            self.pViewObj.setX(self.x)
            self.pViewObj.setY(self.y)
        except:
            print 'Could not transform'
        #print 'location is: ', data.person.x(), data.person.y()

class clue(object):
    def __init__(self, data, difficulty = 0, target= None, loc = None, text = ''):
        self.data = data
        self.difficulty = difficulty
        self.target = target
        self.loc = loc
        self.text = text

    def drawNewClue(self):
        None
    
class View(object):
    def __init__(self, MainWindow=None):
        self.MainWindow = MainWindow
        self.guiState = None
        self.personView = None
        #There really should be more stuff here.
    
