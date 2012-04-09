"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtGui import QMainWindow, QMessageBox, QFileDialog, QPixmap
from Globals import *
from os.path import normpath, isfile
from Gui import Gui
from Game import Game

class ViewMain(QMainWindow):
    """This Class Provides the Graphical Interface for Game"""

    # Use Constants To Avoid Magic Numbers
    
    # Declare stack widget names
    MAIN_PAGE = 0
    SETTINGS_PAGE = 1
    GAME_PAGE = 2
    INSTRUCTIONS_PAGE = 3
    CREDITS_PAGE = 4
    STORY_PAGE = 5
    
    def __init__(self, parent=None):
        """Initialize the abstracted class instance"""
        super(ViewMain, self).__init__(parent)

        # Init Data Members
        self.gui  = Gui(self)
        self.game = None
        self.connectGui()
        self.messageFade = None

        # List of Graphics Objects
        self.graphicsObjects = []
        
        # Overlays
        self.overlays = {}
        
        self.currStackIndex = self.MAIN_PAGE
        self.gui.soundManager.playCurrMusic()
        
        
########################################
### Signals and slots connected here ###
########################################
    def connectGui(self):
        """Connect signals for Gui"""
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
        
    def connectGame(self):
        # character (emits when updates) , emits newpos
        # places (emits when loc added), emits loc and signal
        # - viewMain connects that signal between the location obj and 
        # - the graphics obj
        # story (emits when working on a clue for too long), emits nothing
        # story (emits signal updating search progress), emits 0-1
        # story (emits signal for message fade), emits 1-0
        None

########################################
###### Custom slots defined here #######
########################################

    def setSettings(self):
        self.setStackWidgetIndex(self.SETTINGS_PAGE)
        
    def setInstructions(self):
        self.setStackWidgetIndex(self.INSTRUCTIONS_PAGE)

    def setCredits(self):
        self.setStackWidgetIndex(self.CREDITS_PAGE)
        
    def goBack(self):
        self.setStackWidgetIndex(self.gui.stackIndex)
        if self.gui.stackIndex == self.GAME_PAGE:
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
            self.setStackWidgetIndex(self.GAME_PAGE)
                
    def saveFileDialog(self):
        filename = QFileDialog.getSaveFileName(None, "Save Game", "saves", 
                                               "MapMaster Save files (*.save)")
        if filename == "":
            filename = "temp.save"
        else:
            if ".save" not in filename:
                filename = filename + ".save"
        self.game.save(filename)    
                
                        
    def newGame(self):
        self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
        self.setStackWidgetIndex(self.STORY_PAGE)
        
        self.overlays['latLongOverlay'] = self.addOverlay(
                        normpath("images/latOverlay.png"))
        self.overlays['colorOverlay'] = self.addOverlay(
                        normpath("images/colorOverlay.png"))
        self.overlays['legendOverlay'] = self.addOverlay(
                        normpath("images/legendOverlay.png"))
        
        # Create game instance and start the game
        self.game = Game()
        debug("Initialized a new game")
        self.game.new()
        debug("Starting a new game")
        
    def storyButton(self):
        self.setStackWidgetIndex(self.GAME_PAGE)
        
    def setMain(self):
        self.saveFileDialog()
        self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
        self.setStackWidgetIndex(self.MAIN_PAGE)
        
    def setStackWidgetIndex(self, index):
        if index == self.MAIN_PAGE:
            self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
        else:
            self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
    
        self.gui.stackedWidget.setCurrentIndex(index)
        self.currStackIndex = index
        self.gui.soundManager.switchSongs(index)
    
    def latLong(self):
        if self.gui.latLongCheck.isChecked():
            debug("Lat/long overlay on")
        else:
            debug("Lat/long overlay off")
        self.overlays['latLongOverlay'].setVisible(
                                        self.gui.latLongCheck.isChecked())
    
    def colorize(self):
        if self.gui.colorCheck.isChecked():
            debug("Color overlay on")
        else:
            debug("Color overlay off")
        self.overlays['colorOverlay'].setVisible(
                                        self.gui.colorCheck.isChecked())
                                        
    def legend(self):
        if self.gui.legendCheck.isChecked():
            debug("Legend overlay on")
        else:
            debug("Legend overlay off")
        self.overlays['legendOverlay'].setVisible(
                                        self.gui.legendCheck.isChecked())

    def setVol(self):
        self.gui.soundManager.setVolume(self.gui.volumeSlider.sliderPosition())
        
    def doSearch(self):
        self.game.story.searchForClue(self.game.character.getCenter())
    
########################################
####### Other methods are here #########
########################################
        
    def keyPressEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        if self.game:
            self.game.keyPress(event)
    
    def keyReleaseEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        if self.game:
            self.game.keyRelease(event)
    
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

    def addGraphicsObject(self, signal, center, name, objType):
        """Add graphics object to the person veiw and map view properly and
        leave a graphics object in ViewMain to handle it. """
        # FIXME connect signal from Places for whenever a loc object is
        # Created.
        graphic = Graphic(self, center, name, objType)
        # FIXME connect signal from Loc object to graphic for whenever a
        # graphic need to update.
        
        self.graphicsObjects.append(graphic)
        
    def addOverlay(self, filename):
        obj = self.gui.mapView.scene.addPixmap(QPixmap(filename))
        obj.setVisible(False)
        return obj
