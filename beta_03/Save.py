# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/


class Save(object):

    def __init__(self, data, filename = "Jessie.save", debug = True):
        """Initialize Save"""      
        self.debug = data.debug
        self.landmarks = data.landmarks
            
        self.places = data.places    # graphics objects (non cities)
        self.overlays = data.overlays  # a dictionary of overlays
        
        self.character =  data.character    # A special Loc for our character
        self.landmarks = data.landmarks      # dictionary of cities.
 
        self.clueStack = data.clueStack    # A list of clues
        
        self.score = data.score


def writeToFile(data,filename):
    """Save games to file, player is able to resume the game next time"""
    posx = None #None is a place holder because I have no clue what this does
    
    
        
