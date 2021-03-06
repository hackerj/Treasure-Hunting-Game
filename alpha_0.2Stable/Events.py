# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.2 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QPixmap

def movementEvent(data, event):
    key = event.key()
    s = data.charSpeed

    if key == QtCore.Qt.Key_W or key == QtCore.Qt.Key_Up:
        data.character.translate(data, 0,-s) #Forward

    elif key == QtCore.Qt.Key_S or key == QtCore.Qt.Key_Down:
        data.character.translate(data, 0, s) #Backward

    elif key == QtCore.Qt.Key_A or key == QtCore.Qt.Key_Left:
        data.character.translate(data, -s,0) #Left

    elif key == QtCore.Qt.Key_D or key == QtCore.Qt.Key_Right:
        data.character.translate(data, s,0) #Right

    elif key == QtCore.Qt.Key_Space or key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
        searchLandmark(data) #Searches with space bar

    else:
        print 'You pressed', event.text()

    data.view.guiMain.personView.centerOn(data.character.pViewObj);

    
def keyboardEvent(data, event):
    key = event.key()
    
    
def loadGraphics(data):
    if data.debug:
        print "Loading Graphics"
    
    for loc in data.places:
                loadPNG(data, loc)
            
    #Load Character
    loadPNG(data, data.character)
    
def loadPNG(data, loc):

    if loc.pViewImag:
        obj = data.view.guiMain.personView.scene.addPixmap(QPixmap(loc.pViewImag))
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
            data.view.guiMain.clueView.setText("No clue here, must be \n somewhere else")
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
        
def getDistance(data,landmark):
    charX, charY = data.character.getCenter()
    lmX, lmY = landmark.getCenter()
    
    return ((charX - lmX)**2 + (charY - lmY)**2)**0.5
