from os.path import *



class load(object):

    def __init__(self, debug = True):
        
        self.debug = debug
        self.places = []    # graphics objects (non cities)
        self.overlays = {}  # a dictionary of overlays

       
        self.character =  None    # A special Loc for our character
        
        self.landmarks = {}       # dictionary of cities.
        self.currLandmark = None  # City with current Clue
        
        self.currClue = None   # Current Clue
        self.clueStack = []    # A list of clues
        
        self.score = 0
        
        self.view = None       # Container for PyQt specific data and widgets
        self.mapScale = 0.1
        
    def loadData(self,filename = "load.txt"):
        """ load Data from file and check for existences
        """
        if (not filename):
            print "File doesnt exist!"
            return
            
        filedata = open(filename)
        nextLine = filename.readline()
        while (nextLine):
            listOfCommands = nextLine.split()
            if (len(obj) > 4):
                command = obj[0]
                obj 


        filename.close()

       
            
