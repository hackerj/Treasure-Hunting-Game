# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.2 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from Events import movementEvent
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QGraphicsView, \
                        QGraphicsScene, \
                        QPixmap

class ViewPerson(QGraphicsView):
    def __init__(self, data, parent=None):
        """QGraphicsView widget which will show where the player is located."""
        
        #Initialize the abstracted class instance
        super(ViewPerson, self).__init__(parent)

        #Create Containter to store graphicObjectsaaaaa
        self.scene = QtGui.QGraphicsScene()
        self.setScene(self.scene)

        #View Settings (Fix Scroll Bars)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        #Reference to data for event calls.
        self.data = data
        
        self.initUI()         #LoadObjects

    def initUI(self):
        #Load Places from Loc Object List
        for loc in self.data.places:
            self.loadGraphic(loc)

        #Load Character
        self.loadGraphic(self.data.character)

    def loadGraphic(self, loc):
        obj = self.scene.addPixmap(QPixmap(loc.image))
        loc.pViewObj = obj
        obj.setX(loc.x)
        obj.setY(loc.y)
        loc.updatePViewObj()
        
        if self.data.debug: 
            print 'Load '+str(loc.image)+' at:', obj.x(), obj.y()
