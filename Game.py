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
from Gui import Ui_MainWindow
from Events import movementEvent

#Hack to allow key presses
class MainWindow(QtGui.QMainWindow):
    def __init__(self, data, parent = None):
        super(MainWindow, self).__init__()
        self.data = data
        
    def keyPressEvent(self, event):
        movementEvent(self.data, event)

class game(object):
    def __init__(self):
        print 'Game has started'
        data = Data()
        data.loadDataInitial()
        data.view = View()
        

        app = QtGui.QApplication(sys.argv)
        mainWindow = MainWindow(data)
        
        ui_main = Ui_MainWindow()
        ui_main.setupUi(mainWindow)
        data.view.MainWindow = ui_main
        
        
        #p = PersonView(data)
        mainWindow.show()
        sys.exit(app.exec_())

# For testing only
def main():
    print 'Starting Game'
    gameInstance = game()

if __name__ == '__main__':
    main()

