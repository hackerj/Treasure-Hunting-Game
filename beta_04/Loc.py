'''
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.3 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
'''

class Loc(object):
    def __init__(self, position, objType=None,
                 pViewImag = None, mViewImag = None,
                 pViewText = None, mViewText = None):
        """Data container for objects appearing in the person and map views"""

        self.x = position[0]
        self.y = position[1]
        self.objType = objType

        #Person View Data
        self.pViewImag = pViewImag
        self.pViewText = pViewText
        self.pViewObj = None

        #Map View Data
        self.mViewImag = mViewImag
        self.mViewText = pViewText
        self.mViewObj = None
        
    def __repr__(self):
        """Print some info about object for debugging."""
        str = ''
        if self.objType: str += self.objType
        if self.pViewImag: str += self.pViewImag
        elif self.mViewImag: str += self.mViewImag
        return str

    def translate(self, data, xDist, yDist):
        if (self.isValidMove(data, xDist, yDist)):
            self.x += xDist
            self.y += yDist
            self.updatePViewObj()
            self.updateMViewObj(data.mapScale)

            # Update the step count to erase outdated messages
            data.stepCount += 1
            if (data.stepCount > 5 and data.gameStatus):
                data.view.guiMain.clueView.setText(data.currClue.text)
                data.stepCount = 0

    def isValidMove(self, data, xDist, yDist):
        checkX = self.x + xDist
        checkY = self.y + yDist
        if (checkX > data.maxX or checkX < data.minX or checkY > data.maxY or checkY < data.minY):
            return False
        else:
            return True
        
    
    def getCenter(self):
        #print dir(self.pViewObj.pixmap)
        
        return self.x + self.pViewObj.pixmap().width()/2, self.y + self.pViewObj.pixmap().height()/2

        try:
            self.x + self.pViewObj.width()/2, \
                   self.y + self.pViewObj.height()/2
        except:
            print "could not find center", self
            print dir(self.pViewObj)
        
        
    def updatePViewObj(self):
        try:
            self.pViewObj.setX(self.x)
            self.pViewObj.setY(self.y)
        except:
            print 'Could not update person view', self.test, \
                  'from', self.x, self.y
                  
    def updateMViewObj(self, mapScale):
        if (self.pViewImag):
            newx, newy = self.getCenter()
        else:
            newx, newy = self.x, self.y
            print 'no pView'
        self.mViewObj.setX(newx * mapScale)
        self.mViewObj.setY(newy * mapScale)
