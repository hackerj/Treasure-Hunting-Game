# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from Game import Game

def startGame():
    "Run Game without terminal or debuging"
    gameInstance = Game(debug = False)

if __name__ == '__main__':
    startGame()
    
