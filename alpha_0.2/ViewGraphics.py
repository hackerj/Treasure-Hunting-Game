# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.2 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from Events import movementEvent
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QGraphicsView, QGraphicsScene

class ViewGraphics(QGraphicsView):
    def __init__(self, parent=None):
        """QGraphicsView widget which will show where the player is located."""
        
        #Initialize the abstracted class instance
        super(ViewGraphics, self).__init__(parent)

        #Create Containter to store graphicObjectsaaaaa
        self.scene = QtGui.QGraphicsScene()
        self.setScene(self.scene)

        #View Settings (Fix Scroll Bars)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
    def wheelEvent(self, event):
        event.ignore()
        
    def keyPressEvent(self, event):
        event.ignore()
            
