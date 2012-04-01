# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4.QtGui import QMainWindow, QMessageBox, QFileDialog
from PyQt4.QtCore import connect
from Globals import *

class ViewMain(QMainWindow):
    def __init__(self, parent=None):
        """Initialize the abstracted class instance"""
        super(WidMain, self).__init__(parent)

        #Init Data Members
        self.gui  = Gui(self)
        self.game = None
        
########################################
### Signals and slots connected here ###
########################################

        self.gui.actionQuit.triggered.connect(self.close)
        self.gui.quitButton.released.connect(self.close)
        self.gui.settingsButton.released.connect(self.setSettings)
        self.gui.actionSettings.triggered.connect(self.setSettings)
        self.gui.loadButton.released.connect(self.loadFileDialog)
        self.gui.actionSave_Game.triggered.connect(self.saveFileDialog)
        self.gui.doneButton.released.connect(self.goBack)
        self.gui.startButton.released.connect(self.newGame)
        self.gui.actionMain_Menu.triggered.connect(self.setMain)
        self.gui.actionHelp.triggered.connect(self.setInstructions)
        self.gui.instrButton.released.connect(self.setInstructions)
        self.gui.doneButton2.released.connect(self.goBack)
        self.gui.doneButton3.released.connect(self.goBack)
        self.gui.actionCredits.triggered.connect(self.setCredits)
        self.gui.latLongCheck.stateChanged.connect(self.latLong)
        self.gui.colorCheck.stateChanged.connect(self.colorize)
        self.gui.legendCheck.stateChanged.connect(self.legend)
        self.gui.searchButton.released.connect(self.doSearch)
        self.gui.nextButton.released.connect(self.storyButton)
        self.gui.volumeSlider.sliderMoved.connect(self.setVol)

########################################
##### Custom signals defined here ######
########################################

# SET INDICES AS VARIABLES!!!
    def setSettings(self):
        self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
        self.gui.stackedWidget.setCurrentIndex(1)
        
    def setInstructions(self):
        self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
        self.gui.stackedWidget.setCurrentIndex(3)

    def setCredits(self):
        self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
        
    def goBack(self):
        self.gui.stackedWidget.setCurrentIndex(self.gui.stackIndex)
        if self.gui.stackIndex == 0:
            self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
        else:
            None
            #Should be something here later
    
    def loadFileDialog(self):
        fd = QFileDialog()
        filename = fd.getOpenFileName(None, "Load Saved Game",
                                      "saves", "MapMaster Save files (*.save)")
            if isfile(filename):
                self.gui.loadSaved = True
                self.gui.stackedWidget.setCurrentIndex(2)
                self.gui.location = 2
                self.gui.soundManager.switchSongs(self.location)
                
    def saveFileDialog(self):
        filename = QFileDialog.getSaveFileName(None, "Save Game", "saves", 
                                               "MapMaster Save files (*.save)")
        if filename == "":
            debug("No file specified!")
        else:
            if ".save" in filename:
                fname = open(filename, "w")
            else:
                fname = open(filename + ".save", "w")
            score = `self.gui.data.score`
            numClues = `len(self.gui.data.clueStack)`
            charX, charY = `self.gui.data.character.getCenter()
            toWriteList = '\t' + `charX` + '\t' + `charY` + '\t'
                        + numClues + '\t' + score
                        
    def newGame(self):
        self.gui.background.setPixmap(self.backgroundPixmapSettings)
        self.gui.stackedWidget.setCurrentIndex(5)
        self.gui.location = 5
        
    def storyButton(self):
        self.gui.stackedWidget.setCurrentIndex(2)
        self.gui.location = 2
        self.gui.soundManager.switchSongs(self.location)
        
    def setMain(self):
        self.saveFileDialog()
        self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
        self.gui.stackedWidget.setCurrentIndex(0)
        self.gui.location = 0
        self.gui.soundManager.switchSongs(self.location)
        
    def latLong(self):
        if self.gui.latLongCheck.isChecked():
            debug("Lat/long overlay on")
        else:
            debug("Lat/long overlay off")
        self.gui.data.overlays['latLongOverlay'].mViewObj.setVisible(
                                        self.gui.latLongCheck.isChecked())
    
    def colorize(self):
        if self.gui.colorCheck.isChecked():
            debug("Color overlay on")
        else:
            debug("Color overlay off")
        self.gui.data.overlays['colorOverlay'].mViewObj.setVisible(
                                        self.gui.colorCheck.isChecked())
                                        
    def legend(self):
        if self.legendCheck.isChecked():
            debug("Legend overlay on")
        else:
            debug("Legend overlay off")
        self.gui.data.overlays['legendOverlay'].mViewObj.setVisible(
                                        self.gui.legendCheck.isChecked())

    def setVol(self):
        self.gui.soundManager.setVolume(self.gui.volumeSlider.sliderPosition())
        
    def doSearch(self):
        self.game.events.searchLandmark()
    
########################################
######### Old methods are here #########
########################################
        
    def keyPressEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        #keyPress(self.data, event)
        print('Implement KeyPressEvent')
    
    def keyReleaseEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        #keyRelease(self.data, event)
        print('Implement keyReleaseEvent')
    
    def closeEvent(self, event):
        """Remapping the close event to a message box"""
        quit_msg = "Are you sure you want to quit?"
        reply = QMessageBox()
        reply.setWindowTitle("Quit Game")
        reply.setText(quit_msg)
        reply.setStandardButtons(
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        reply.setDefaultButton(QMessageBox.Save)
        ret = reply.exec_()
        
        if ret == QMessageBox.Discard:
            print "Accepting close event"
            event.accept()
        elif ret == QMessageBox.Cancel:
            event.ignore()
        else:
            self.saveFileDialog()
            print "Accepting close event"
            event.accept()

