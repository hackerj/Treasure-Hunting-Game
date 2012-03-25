# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from sys import argv, exit               #Get command line arguments
from PyQt4.QtGui import QApplication     #PyQt Application Window
from ViewMain import WidMain             #Toplevel Widget
from Gui import GuiMain as GuiMain       #Gui for Toplevel Widget

class View(object):
    def __init__(self, data):
        """Init Window and Gui"""
        self.app = QApplication(argv)      #Create Window
        self.widMain = WidMain(data)       #Inherits from QMainWindow
        self.guiMain  = GuiMain(data)      #Contains buttons, graphics, etc.
        self.guiMain.setupUi(self.widMain) #Add ui to main window
