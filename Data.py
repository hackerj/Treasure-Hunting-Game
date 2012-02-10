# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

class Data(object):
    def __init__(self):
        self.places = []       # A list of Locs (e.g. cities).
        self.character =  None # A special Loc for our character (only one)
        self.clue = []         # A list of clues for the game.
        self.view = None       # A container for PyQt specific data and widgets
        
    def loadDataInitial(self):
        #Initialize View
        self.view = View()
        self.character = Loc()
        
        #There really should be more stuff here.
    
    def loadDataFromUserFile(self, path):
        None #Not Implemented!

    def saveData(self, path):
        None #Not Implemented!

    def addPlace(graphObject, position = (0,0)):
        place = Loc(graphicObject = graphObject)
        self.places.append(place)
    
class Loc(object):
    def __init__(self, data, name = None, objType=None,
                 position = (0,0), graphicObject = None):
        self.data = data
        self.name = name
        self.objType = objType
        self.x = position[0]
        self.y = position[1]
        self.graphicObject = graphicObject

    def translate(self, xDist,yDist):
        try:
            self.x += xDist
            self.y += yDist

            self.QGraphicObject.setX(self.x)
            self.QGraphicObject.setY(self.y)
        else:
            print 'Could not transform    
        #print 'location is: ', data.person.x(), data.person.y()
        
class View(object):
    def __init__(self):
        self.PersonView = None
        #There really should be more stuff here.
    
