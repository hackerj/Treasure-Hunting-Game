# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from random import randint
from Events import movementEvent
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QGraphicsView, \
                        QGraphicsScene, \
                        QPixmap

class ViewPerson(QGraphicsView):
    def __init__(self, data, parent=None):
        """
        QGraphicsView widget which will show where the player is located.
        """
        
        #Initialize the class instance
        super(ViewPerson, self).__init__()

        #Create Containter to store graphicObjectsaaaaa
        self.scene = QtGui.QGraphicsScene()
        self.setScene(self.scene)

        #remember data 
        self.data = data # Should be modified to no longer need this.

        #View Settings
        self.setWindowTitle('Map Master Prototype')
        self.setWindowIcon(QtGui.QIcon('icon_medium.png'))
        self.setGeometry(300, 300, 800, 640)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        #LoadObjects
        self.initUI()

        #print dir(self)


    def initUI(self):
        # Load Loc Objects
        for loc in self.data.places:
            self.loadGraphic(loc)

        self.loadGraphic(self.data.character)
		
	self.show()

    def loadGraphic(self, loc):
        obj = self.scene.addPixmap(QPixmap(loc.image))
        loc.pViewObj = obj
        obj.setX(loc.x)
        obj.setY(loc.y)
        loc.updatePViewObj()
        
        print 'Load '+str(loc.image)+' at:', obj.x(), obj.y()
        
    def keyPressEvent(self, event):
        movementEvent(self.data, event)
