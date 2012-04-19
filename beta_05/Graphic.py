"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.5 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

# Should FIXME

from PyQt4.QtCore import QObject, QString
from PyQt4.QtGui import QPixmap
from Globals import *
from os.path import normpath

class Graphic(QObject):

    SCALE = 0.1
    OBJ_TYPES = {u'tree'    : ('Forest3.png', 'tree.png'), 
                 u'mountain' : ('Mountain.png', 'mountain.png'),
                 u'landmark' : ('city2.png', 'city.png'), 
                 u'capital'  : ('city2.png','capital.png'), 
                 u'city'     : ('city2.png', 'city.png'), 
                 u'grass'    : ('grasstexture2.png', None),
                 u'mapBG'    : (None, 'mapBackground.png'),
                 u'Character' : ('circle.png','circle.png')}
                    
    def __init__(self, xval, yval, name = '', objType=None):
        """Data container for graphics equivalent of location objects"""
        self.pViewObject = None
        self.mViewObject = None
        self.x = xval
        self.y = yval
        self.objType = str(objType)
        self.name = name

        # Add slot for signal from location object
        # The signal will call 
    
    def chooseImages(self):
        """Associate location with location images"""
        pViewName, mViewName = self.OBJ_TYPES[self.objType]
                
        if pViewName:
            pViewImage = normpath("images/"+pViewName)
        else: pViewImage = None
        
        if mViewName:
            mViewImage = normpath("images/"+mViewName)
        else: mViewImage = None
        return pViewImage, mViewImage
    
    def addGraphicsObjects(self, pView, mView, pViewImage, mViewImage):
        """Make each location object as graphic objs"""
        if pViewImage:
            self.pViewObject = pView.scene.addPixmap(QPixmap(pViewImage))
        else:
            debug("No Person Image")
        if mViewImage:
            self.mViewObject = mView.scene.addPixmap(QPixmap(mViewImage))
        else:
            debug("No Map Image")
        self.update(self.x, self.y)
    
    def __repr__(self):
        return "QGraphicsObject at "+`self.x`+","+`self.y`+ \
               " of type " + `self.objType`
    
    def createInitial(self, pView, mView):
        """Display loc objs to screen"""
        pViewImage, mViewImage = self.chooseImages()
        debug(pViewImage, mViewImage, self.objType)
        self.addGraphicsObjects(pView, mView, pViewImage, mViewImage)
    
    def update(self, newx, newy):
        """Update the graphic objs with character movement"""
        self.x = newx 
        self.y = newy
        #debug(self.name, " has positon: ", self.x, self.y)        
        if self.pViewObject:
            self.updateGraphicsItem(self.pViewObject, 1)
        if self.mViewObject:
            if not self.pViewObject:
                scale = 1
            else:
                scale = self.SCALE
            self.updateGraphicsItem(self.mViewObject, scale)

        if self.objType == 'Character':
            scene = self.pViewObject.scene()
            view = scene.views()[0]
            view.centerOn(self.pViewObject)

    def updateGraphicsItem(self, item, scale = 1):
        """When character walk out of frame, update graphic"""
        try:
            width = item.pixmap().width()/2
            heigth = item.pixmap().height()/2
            #debug("update helper: width, hight", width, heigth)
            item.setX((self.x - width)* scale)
            item.setY((self.y - heigth)* scale)
        except:
            debug("Could not update graphics item", mapScale)
            
            
    
