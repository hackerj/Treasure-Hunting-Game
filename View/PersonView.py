# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from random import randint
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QGraphicsView, \
                        QGraphicsScene, \
                        QPixmap

class PersonView(QGraphicsView):
    def __init__(self, parent=None, data):
        """
        QGraphicsView widget which will show where the player is located.
        """
        
        #Initialize the class instance
        super(PersonView, self).__init__()

        #Create Containter to store graphicObjectsaaaaa
        self.scene = QtGui.QGraphicsScene()
        self.setScene(self.scene)

        #remember data
        self.data = data
        self.data.view.personView = self

        #View Settings
        self.setWindowTitle('Map Master Prototype')
        self.setWindowIcon(QtGui.QIcon('icon_medium.png'))
        self.setGeometry(300, 300, 800, 640)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #setCornerWidget(QPointF
        
        #LoadObjects
        self.initUI()

        #print dir(self)


    def initUI(self):
        # Load Background.
        self.loadGraphic(-512,-512,'image','grass texture2.png')

        # Load Trees.
        numTrees = 20
        for i in xrange(7):
            treeX = randint(-350,350)
            treeY = randint(-350,350)
            self.loadGraphic(treeX-162,treeY-162,'image','Forest3.png')

        # Person
        person = self.loadGraphic(0,0, 'image','circle.png')
        self.data.person = person
        self.centerOn(person);

        self.show()

        
    def loadGraphic(self, x, y, graphicType = None, name=''):
        if graphicType == 'text':
            obj = self.scene.addText(name)            
        elif graphicType == 'image':
            obj = self.scene.addPixmap(QPixmap(name))
        else:
            print 'error'
            return False

        self.data.places.append(obj)   
        obj.setX(x)
        obj.setY(y)        
        print 'Load '+str(name)+' at:', obj.x(), obj.y()
        return obj

    def keyPressEvent(self, event):
        movementEvent(self.data, event)
