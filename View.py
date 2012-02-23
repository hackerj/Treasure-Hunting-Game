# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from sys import argv                     #Get command line arguments
from PyQt4.QtGui import QApplication     #PyQt Application Window
from ViewMain import WidMain             #Toplevel Widget
from Gui import Ui_MainWindow as UIMain  #Gui for Toplevel Widget

class View(object):
    def __init__(self):
        "Init Window and Gui"
        self.app = QApplication(argv)    #Create Window
        self.widMain = WidMain()         #Inherits from QMainWindow
        self.uiMain  = UIMain()          #Contains buttons, graphics, etc.
        self.uiMain.setupUi(self.widMain)    #Add ui to main window
        self.widMain.show()              #Start mainloop
        exit(self.app.exec_())                #When done with mainloop close the window