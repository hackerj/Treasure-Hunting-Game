"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

# Should FIXME

from PyQt4.QtCore import QObject, QString
from PyQt4.QtGui import QPixmap
from Globals import *
from os.path import normpath

class Graphic(QObject):

    OBJ_TYPES = {u'tree'    : ('Forest3.png', 'tree.png'), 
                 u'landmark' : ('city2.png', 'city.png'), 
                 u'capital'  : ('city2.png','capital.png'), 
                 u'city'     : ('city2.png', 'city.png'), 
                 u'grass'    : ('grasstexture2.png', None),
                 u'mapBG'    : (None, None)}
                    
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
        pViewName, mViewName = self.OBJ_TYPES[self.objType]
                
        if pViewName:
            pViewImage = normpath("images/"+pViewName)
        else: pViewImage = None
        
        if mViewName:
            mViewImage = normpath("images/"+mViewName)
        else: mViewImage = None
        return pViewImage, mViewImage
    
    def addGraphicsObjects(self, pView, mView, pViewImage, mViewImage):
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
        pViewImage, mViewImage = self.chooseImages()
        debug(pViewImage, mViewImage, self.objType)
        self.addGraphicsObjects(pView, mView, pViewImage, mViewImage)
    
    def update(self, newx, newy):
        debug(self.name + " connected")
        if self.pViewObject:
            self.updateGraphicsItem(self.pViewObject, 1)
        if self.mViewObject:
            self.updateGraphicsItem(self.mViewObject, 0.1)

    def updateGraphicsItem(self, item, scale = 1):
        try:
            item.setX(self.x * scale)
            item.setY(self.y * scale)
        except:
            debug("Could not update graphcis item", mapScale)
