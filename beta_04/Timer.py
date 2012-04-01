"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtCore import QTimer, QTime

class GameTimers(object):
    """
    Class to create and manage time related inputs
    """
    FRAMERATE = 25
    
    def __init__(self):
        """Init QTimers and QTime objects"""
        #Measure Time
        self.clueTime = None
        self.gameTime = None

        #Send Signals after Delay
        self.frameTimer = None        
        self.clueTroubleTimer = None
        self.messageFade = None
        self.searchProgress = None
        
    def launch(self):
        """Start sending signals to the game using Timers"""
        None
        
    
