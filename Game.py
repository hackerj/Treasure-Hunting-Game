# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

import sys
from Data import Data, View
from PersonView import PersonView
from PyQt4 import QtGui

class game(object):
    def __init__(self):
        print 'Game has started'
        data = Data()
        data.loadDataInitial()

        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        
        
        p = PersonView(data)
        sys.exit(app.exec_())

# For testing only
def main():
    print 'Starting Game'
    gameInstance = game()

if __name__ == '__main__':
    main()
