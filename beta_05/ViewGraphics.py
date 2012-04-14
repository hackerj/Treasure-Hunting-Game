"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QGraphicsView, QGraphicsScene

class ViewGraphics(QGraphicsView):
    """QGraphicsView widget which will show where the player is located."""
    def __init__(self, parent=None):
        """Initialize the abstracted class instance"""
        super(ViewGraphics, self).__init__(parent)

        #Create Containter to store graphicObjectsaaaaa
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        #View Settings (Fix Scroll Bars)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
    def wheelEvent(self, event):
        """Ignore wheel events"""
        event.ignore()
        
    def keyPressEvent(self, event):
        """Ignore keypress events"""
        event.ignore()
            
