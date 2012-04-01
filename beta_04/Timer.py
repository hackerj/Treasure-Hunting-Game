"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.3 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QTimer, QTime

class GameTimers(object):
    """
    Class to create and manage time related inputs
    """    
    def __init__(self):
        "Create Lists to store objects and init time related data members"
        self.timeMeasureList = [] #List of Qtime Objects
        self.delayExecList = [] #List of Qtimer Objects

        self.framerate = 25 #universal frame rate for the game.

    def addTimeMeasureObject(self):
        None

    def addDelayExecObject(self):
        None
    
        
