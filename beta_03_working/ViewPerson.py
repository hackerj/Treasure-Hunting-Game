"""ViewPerson class"""
# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QGraphicsView, \
                        QGraphicsScene

class ViewPerson(QGraphicsView):
    """QGraphicsView widget which will show where the player is located."""
    def __init__(self, data, parent=None):
        
        """Initialize the abstracted class instance"""
        super(ViewPerson, self).__init__(parent)

        #Create Containter to store graphicObjectsaaaaa
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        #View Settings (Fix Scroll Bars)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        #Reference to data for event calls.
        self.data = data
        
        self.initUI()         #LoadObjects

    def initUI(self):
        """Load places and character"""
        #Load Places from Loc Object List
        for loc in self.data.places:
            self.loadGraphic(loc)

        #Load Character
        self.loadGraphic(self.data.character)

    def loadGraphic(self, loc):
        """Loads graphics"""
        obj = self.scene.addPixmap(QtGui.QPixmap(loc.image))
        loc.pViewObj = obj
        obj.setX(loc.x)
        obj.setY(loc.y)
        loc.updatePViewObj()
        
        if self.data.debug: 
            print 'Load '+str(loc.image)+' at:', obj.x(), obj.y()
