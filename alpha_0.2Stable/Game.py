# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.2 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from sys import exit
from Data import Data #Toplevel data class

from PyQt4.QtCore import QTimer, SIGNAL
from PyQt4.QtCore import QObject

class Game(object):
    def __init__(self, debug = True):
        """Start Game"""
        data = Data(debug)          #Load Data and View
        
        #Initialize frames
        data.timer = QTimer()
        QObject.connect(data.timer, SIGNAL("timeout()"), self.frame)
        data.timer.start(1000)

        data.view.widMain.show()    #Start mainloop

        exit(data.view.app.exec_()) #Mainloop is finished. Close Window
        
    def frame(self):
        print "new frame"

def testGame():
    print 'Starting Game' 
    gameInstance = Game(debug = True)

if __name__ == '__main__':
    testGame()
