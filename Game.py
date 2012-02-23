# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from Data import Data #Toplevel data class

class Game(object):
    def __init__(self, debug = True):
        "Start Game"
        data = Data(debug) #Load Data 
        #Load View
        #Start Mainloop
        #Mainloop is finished

def testGame():
    print 'Starting Game' 
    gameInstance = Game(debug = True)

if __name__ == '__main__':
    testGame()
