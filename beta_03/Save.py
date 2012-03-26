
class Save(object):

    def __init__(self, data, debug = True):      
        self.debug = data.debug
        self.landmarks = data.landmarks
            
        self.places = data.places    # graphics objects (non cities)
        self.overlays = data.overlays  # a dictionary of overlays
        
        self.character =  data.character    # A special Loc for our character
        self.landmarks = data.landmarks      # dictionary of cities.
 
        self.clueStack = []    # A list of clues
        
        self.score = data.score
        
    
