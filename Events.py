# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4 import QtCore, QtGui

def movementEvent(data, event):
    key = event.key()
    s = 5

    if key == QtCore.Qt.Key_W:
        data.character.translate(data,0,-s) #Forward

    elif key == QtCore.Qt.Key_S:
        data.character.translate(data,0,s) #Backward

    elif key == QtCore.Qt.Key_A:
        data.character.translate(data,-s,0) #Left
    elif key == QtCore.Qt.Key_D:
        data.character.translate(data,s,0) #Right
    elif key == QtCore.Qt.Key_J:
        print 'swap'
        _swapGui(data)
        return
    else:
        print 'You pressed', event.text()

    #data.view.personView.centerOn(data.character.pViewObj);

