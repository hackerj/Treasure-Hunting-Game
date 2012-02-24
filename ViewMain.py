# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4.QtGui import QMainWindow
from Events import movementEvent

class WidMain(QMainWindow):
    def __init__(self, data, parent=None):
        #Initialize the abstracted class instance
        super(WidMain, self).__init__(parent)
        
        #Initialize data
        self.data = data
        
    def keyPressEvent(self, event):
        "Get keyboard events no matter what widget has focus"
        movementEvent(self.data, event)
