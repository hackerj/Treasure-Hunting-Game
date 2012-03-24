# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from os.path import normpath

class Load(object):

    def __init__(self, debug=True):
        self.debug = debug
        self.places = []
        self.overlays = {}

        self.character = None
        self.landmarks = {}       # dictionary of cities.
        self.currLandmark = None  # City with current Clue
        
        self.currClue = None   # Current Clue
        self.clueStack = []    # A list of clues

        self.score = 0
        
        self.view = None       # Container for PyQt specific data and widgets
        self.mapScale = 0.1
        
    
