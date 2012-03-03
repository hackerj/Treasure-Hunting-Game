# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
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
    elif key == QtCore.Qt.Key_Space:
        searchCity(data) #Searches with space bar
    else:
        print 'You pressed', event.text()

    data.view.guiMain.personView.centerOn(data.character.pViewObj);

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

def searchCity(data):
    if not data.currCity:
        data.currCity = data.character
    
    if not getDistance(data, data.currCity) < data.CITY_RADIUS:
        return False
    
    if data.clueStack:            
        #Load new Clue and City Data.
        data.currClue = data.clueStack.pop()
        data.currCity = data.cities[data.currClue.targetCity]
        
        #updateClueGui
        data.view.guiMain.clueView.setText(data.currClue.text)
        return True
    
    #else
    data.view.guiMain.clueView.setText(" YOU WON!\n"
                                       "But the game has just begun")
    return True
        
def getDistance(data,city):
    charX, charY = data.character.getCenter()
    cityX, cityY = city.getCenter()
    
    return ((charX - cityX)**2 + (charY - cityY)**2)**0.5
