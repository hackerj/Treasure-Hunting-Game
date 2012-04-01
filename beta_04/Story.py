"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QObject

class Story(QObject):
    def __init__(self):
        #Over Simplified Clue managment.
        self._cluelist = []
        self.curClue
        
        #Clue object are represented as dictionaries.
        
    def foundClue(self):
        None
        
    def searchForClue(self, position):
        None
        
    def troubleFindingClue(self):
        None
        
    def loadData(self):
        None
        
