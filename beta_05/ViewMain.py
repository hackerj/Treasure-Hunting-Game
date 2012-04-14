"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtGui import QMainWindow, QMessageBox, QFileDialog, QPixmap
from PyQt4.QtCore import Qt, QTimeLine
from Globals import *
from os.path import normpath, isfile
from Gui import Gui
from Game import Game
from Graphic import Graphic

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

        # Dictionary of Graphics Objects
        self.graphicsObjects = {}
        
        # Overlays
        self.overlays = {}
        
        self.currStackIndex = self.MAIN_PAGE
        self.gui.soundManager.playCurrMusic()
        self.gui.soundManager.setVolume(0)
        
        self.popupTimelineStart = QTimeLine(200)
        self.popupTimelineStart.setFrameRange(0,100)
        self.popupTimelineEnd = QTimeLine(200)
        self.popupTimelineEnd.setFrameRange(0,100)
        self.popupTimelineWait = QTimeLine()
        self.popupTimelineWait.setFrameRange(0,100)
        self.popupClue = False
        
        self.toMain = False
        #self.gui.personView.centerOn(0,0)
        self.gui.mapView.centerOn(0,0)
        
########################################
### Signals and slots connected here ###
########################################

        self.popupTimelineStart.frameChanged.connect(self.drawPopup)
        self.popupTimelineStart.finished.connect(self.popupWait)
        self.popupTimelineEnd.frameChanged.connect(self.erasePopup)   
        self.popupTimelineWait.finished.connect(self.enableErasePopup) 
        self.popupTimelineEnd.finished.connect(self.writeClue)
    
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
        """Connect signals for Game"""
        self.game.places.passLoc.connect(self.addGraphicsObject)
        self.game.frameTimer.timeout.connect(self.frameUpdate)

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
            self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
        else:
            self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
            #Should be something here later
    
    def loadFileDialog(self):
        
        fd = QFileDialog()
        filename = fd.getOpenFileName(None, "Load Saved Game",
                                      "saves", "MapMaster Save files (*.save)")
        
        if isfile(filename):
            self.setStackWidgetIndex(self.GAME_PAGE)
            self.game = Game() 
            self.connectGame()
            self.game.load(filename)
            debug("Initializing the saved game...")
            
            
            self.overlays['latLongOverlay'] = self.addOverlay(
                        normpath("images/latOverlay.png"))
            self.overlays['colorOverlay'] = self.addOverlay(
                        normpath("images/colorOverlay.png"))
            self.overlays['legendOverlay'] = self.addOverlay(
                        normpath("images/legendOverlay.png"))

            self.gui.scoreBox.setText((str)(self.game.story.score))
            self.gui.clueView.setText(self.game.story.currClue['text'])
            self.gui.stackIndex = self.GAME_PAGE

    def saveFileDialog(self,toMain = False):
        filename = QFileDialog.getSaveFileName(None, "Save Game", "saves", 
                                               "MapMaster Save files (*.save)")
        if filename == "":
            if toMain:
                self.setStackWidgetIndex(self.MAIN_PAGE)                
            else:
                return False
        else:
            if ".save" not in filename:
                debug(".save is not in the file, add one..")
                filename = filename + ".save"
            debug("correctly save data to file...",filename)
            self.game.save(filename)    
               
                        
    def newGame(self):
        self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
        self.setStackWidgetIndex(self.STORY_PAGE)
        self.gui.stackIndex = self.GAME_PAGE
        
        # Create game instance and start the game
        self.game = Game()
        debug("Initialized a new game")
        self.connectGame()
        self.game.new()
        debug("Starting a new game")
        
        self.overlays['latLongOverlay'] = self.addOverlay(
                        normpath("images/latOverlay.png"))
        self.overlays['colorOverlay'] = self.addOverlay(
                        normpath("images/colorOverlay.png"))
        self.overlays['legendOverlay'] = self.addOverlay(
                        normpath("images/legendOverlay.png"))
        self.gui.clueView.setText(self.game.story.currClue['text'])
        
    def storyButton(self):
        self.setStackWidgetIndex(self.GAME_PAGE)
        
    def setMain(self):
        self.saveFileDialog(self.toMain)
        self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
        self.setStackWidgetIndex(self.MAIN_PAGE)
        self.gui.stackIndex = self.MAIN_PAGE
        
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
        self.popupClue = True
        self.popupMessage("Searching...", 2*ONE_SECOND)
        
    def writeClue(self):
        if self.popupClue:
            clueResult = self.game.story.searchForClue(self.game.character.getCenter())
            self.handleClueResult(clueResult[0], clueResult[1])
            self.popupClue = False
            if clueResult[0] == 'ClueFound':
                self.popupMessage('You found a clue!\n' + clueResult[1], 5*ONE_SECOND)
            elif clueResult[0] == 'ClueFailed':
                self.popupMessage(clueResult[1], 3*ONE_SECOND)
            elif clueResult[0] == 'GameOver':
                self.popupMessage(clueResult[1], 3*ONE_SECOND)
            else:
                None
        
    def drawPopup(self, value):
        debug("Called drawPopup")
        self.gui.popupImage.setOpacity(value/100.0)
        self.gui.popupText.setOpacity(value/100.0)
        
    def enableErasePopup(self):
        debug("Enabled erase popup")
        self.popupTimelineEnd.start()
        
    def erasePopup(self, value):
        debug("Called erase popup")
        self.gui.popupImage.setOpacity(1-(value/100.0))
        self.gui.popupText.setOpacity(1-(value/100.0))
        
    def popupWait(self):
        debug("Entered popupWait")
        self.popupTimelineWait.start()
        
    # FIXME This needs time actions
    def handleClueResult(self, action, text):
        if action == 'ClueFound':
            #self.popupMessage("You found a clue!", 2000)
            self.gui.clueView.setText(text)
            self.gui.scoreBox.setText(`self.game.story.score`)
        elif action == 'GameOver':
            self.gui.clueView.setText(text)
        else:
            None
    
    def popupMessage(self, text, time):
        self.gui.popupText.setPlainText(text)
        self.popupTimelineWait.setDuration(time)
        self.popupTimelineStart.start()
        
    def keyPressEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        if self.game:
            self.game.keyPress(event)
    
    def keyReleaseEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        if self.game:
            key = event.key()
            if key == Qt.Key_Space or key == Qt.Key_Enter or key == Qt.Key_Return:
                self.doSearch()
            else:
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
            if (self.saveFileDialog() == False):
                debug("Not quit yet, go back to game...")
                event.ignore()
            else:
                print "Accepting close event"
                event.accept()

    def addGraphicsObject(self, name, xval, yval, objType):
        """Add graphics object to the person veiw and map view properly and
        leave a graphics object in ViewMain to handle it. """
        debug("Receiving passLoc")
        graphic = Graphic(xval, yval, str(name), str(objType))
        graphic.createInitial(self.gui.personView, self.gui.mapView)
        self.graphicsObjects[name] = graphic
        self.game.places.locList[str(name)].changePos.connect(
                                        self.updateGraphicsObject)
        debug("Connecting Loc to Graphic for " + name)
        
        self.game.places.locList[str(name)].emitter()
        
        #self.graphicsObjects.append(graphic)
    def updateGraphicsObject(self, xpos, ypos, name):
        #debug("Updating the graphics object")
        self.graphicsObjects[name].update(xpos, ypos)
        
    def addOverlay(self, filename):
        obj = self.gui.mapView.scene.addPixmap(QPixmap(filename))
        obj.setX(-195)
        obj.setY(-250)
        obj.setVisible(False)
        return obj
        
    def frameUpdate(self):
        #debug('Frame update sent to character')
        self.game.character.frameUpdate(self.game.FRAME_RATE)
