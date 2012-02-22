# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4 import QtCore, QtGui
from Gui import Ui_Menu, Ui_Game

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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


def _swapGui(data):
    
    if data.view.guiState == 'Game':
        _swapToMenu(data)
    elif data.view.guiState == 'Menu':
        _swapToGame(data)
    else:
        #print 'Error no gui swap'
        _swapToGame(data)
    
def _swapToGame(data):
    frame = data.view.MainWindow.frame
    #frame.deleteLater()
    frame.hide()
    
    frame = QtGui.QFrame(data.view.MainWindow.centralwidget)
    frame.setFrameShape(QtGui.QFrame.NoFrame)
    frame.setFrameShadow(QtGui.QFrame.Raised)
    frame.setObjectName(_fromUtf8("frame"))
    
    ui_game = Ui_Game()
    ui_game.setupUi(frame)
    frame.show()
    data.view.guiState = 'Game'
    
def _swapToMenu(data):
    frame = data.view.MainWindow.frame
    #frame.deleteLater()

    frame.hide()
    data.view.MainWindow.show()
    '''
    frame = QtGui.QFrame(data.view.MainWindow.centralwidget)
    frame.setFrameShape(QtGui.QFrame.NoFrame)
    frame.setFrameShadow(QtGui.QFrame.Raised)
    frame.setObjectName(_fromUtf8("frame"))
    
    ui_menu = Ui_Menu()
    ui_menu.setupUi(frame)
    frame.show()
    
    data.view.guiState = 'Menu'
    '''


