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

    if key == QtCore.Qt.Key_W:
        data.character.translate(data, 0,-s) #Forward

    elif key == QtCore.Qt.Key_S:
        data.character.translate(data, 0, s) #Backward

    elif key == QtCore.Qt.Key_A:
        data.character.translate(data, -s,0) #Left
    elif key == QtCore.Qt.Key_D:
        data.character.translate(data, s,0) #Right
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
    if getDistance(self.clueCity) < CITY_RADIUS:
        
        if self.clueStack:            
            #Load new Clue and City Data.
            data.currClue = self.clueStack.pop()
            data.currCity = self.cities[self.currClue.cityName]
            
            #updateClueGui
            data.view.clueView.setText(self.currClue.text)
            return True
         
        print "you have won or the the game has not started"
        return True
         
    else:
        return False
    
def getDistance(data,city):
    charX, charY = data.character.center(data.mapScale)
    cityX, cityY = city.center(data.mapScale)
    
    return ((charX - cityX)^2 + (charY - cityY)^2)^0.5