# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4.QtGui import QPixmap
from PyQt4.QtCore import QTimer, SIGNAL, QObject
from PyQt4.QtCore import Qt

def initFrames(data):
    data.timer = QTimer()
    QObject.connect(data.timer, SIGNAL("timeout()"), data.frame)
    frameTime = 1000/data.framerate
    data.timer.start(frameTime)
    
def keyPress(data, event):
    key = event.key()
    sp  = data.charSpeed

    if key == Qt.Key_W or key == Qt.Key_Up:
        data.charVelocityY = -sp #Forward

    elif key == Qt.Key_S or key == Qt.Key_Down:
        data.charVelocityY = sp #Backward

    elif key == Qt.Key_A or key == Qt.Key_Left:
        data.charVelocityX = -sp #Left

    elif key == Qt.Key_D or key == Qt.Key_Right:
        data.charVelocityX = sp #Right

    elif key == Qt.Key_Space or key == Qt.Key_Enter or key == Qt.Key_Return:
        searchLandmark(data) #Searches

    else:
        if data.debug:
            print 'You pressed', event.text()
 
def keyRelease(data, event):
    key = event.key()


    if key == Qt.Key_W or key == Qt.Key_Up:
        data.charVelocityY = 0 #Forward

    elif key == Qt.Key_S or key == Qt.Key_Down:
        data.charVelocityY = 0 #Backward

    elif key == Qt.Key_A or key == Qt.Key_Left:
        data.charVelocityX = 0 #Left

    elif key == Qt.Key_D or key == Qt.Key_Right:
        data.charVelocityX = 0 #Right

    else:
        if data.debug:
            print 'You released ', event.text()
    
def frameupdate(data):
    updateCharacter(data)
    
def updateCharacter(data):
    xLoc = data.charVelocityX/data.framerate
    yLoc = data.charVelocityY/data.framerate  
    data.character.translate(data, xLoc, yLoc)
    data.view.guiMain.personView.centerOn(data.character.pViewObj)
    
def loadGraphics(data):
    if data.debug:
        print "Loading Graphics"
    
    for loc in data.places:
        loadPNG(data, loc)
            
    #Load Character
    loadPNG(data, data.character)
    
def loadPNG(data, loc):

    if loc.pViewImag:
        obj = data.view.guiMain.personView.scene.addPixmap(
					QPixmap(loc.pViewImag))
        loc.pViewObj = obj
        loc.updatePViewObj()
    
    elif loc.pViewText:
        obj = data.view.guiMain.personView.scene.addText(loc.pViewText)
        loc.pViewObj = obj
        loc.updatePViewObj()
    
    if loc.mViewImag:
        obj = data.view.guiMain.mapView.scene.addPixmap(QPixmap(loc.mViewImag))
        loc.mViewObj = obj
        loc.updateMViewObj(data.mapScale)
        
    elif loc.mViewText:
        obj = data.view.guiMain.mapView.scene.addText(loc.mViewText)
        loc.mViewObj = obj
        loc.updateMViewObj(data.mapScale)
        
    
    if data.debug: 
        print 'Load ', loc

def searchLandmark(data):
    if not data.currLandmark:
        data.currLandmark = data.character

    dist = getDistance(data, data.currLandmark)
    
    if not dist < data.LANDMARK_RADIUS:
        if data.gameStatus:
            data.view.guiMain.clueView.setText(
			"No clue here, must be \n somewhere else")
        return False
    
    if data.clueStack:            
        #Load new Clue and City Data.
        data.currClue = data.clueStack.pop()
        data.currLandmark = data.landmarks[data.currClue.targetLandmark]
        
        #updateClueGui
        data.view.guiMain.clueView.setText(data.currClue.text)

        #updateScore
        data.score += 100
        data.view.guiMain.scoreBox.setText((str)(data.score))
        return True
    
    
    #else
    data.view.guiMain.clueView.setText(" YOU WON!\n"
                                       "But the game has just begun")
    data.gameStatus = 0
    return True
        
def getDistance(data, landmark):
    charX, charY = data.character.getCenter()
    lmX, lmY = landmark.getCenter()
    
    return ((charX - lmX)**2 + (charY - lmY)**2)**0.5
