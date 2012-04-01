"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

class Game(Object):
    "Container to hold one new or loaded game instance"

    def __init__(self, pview, mview, cview):
        "Init Classes and store references to need gui elements

        #Gui Ouput Links
        self.pview = pview
        self.mview = mview
        self.cview = cview
        
    def initNew(self):
        "Load new game from file"
        None

    def initSaved(self)
        "Load existing game from file"
        None
