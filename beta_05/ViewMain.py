"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.5 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from PyQt4.QtGui import QMainWindow, QMessageBox, QFileDialog, QPixmap, QInputDialog
from PyQt4.QtCore import Qt, QTimeLine, QTimer, QPropertyAnimation, QRect, pyqtSignal
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
    SCORE_PAGE = 6

    finished = pyqtSignal()
    
    def __init__(self, parent=None):
        """Initialize the abstracted class instance"""
        super(ViewMain, self).__init__(parent)

        # Init Data Members
        self.gui  = Gui(self)
        self.game = None
        self.connectGui()

        self.gameWasLoaded = False
        self.useLoadWorkaround = True

        # Dictionary of Graphics Objects
        self.graphicsObjects = {}
        
        # Overlays
        self.overlays = {}
        
        self.currStackIndex = self.MAIN_PAGE
        self.gui.soundManager.playCurrMusic()
        #self.gui.soundManager.setVolume(0)
        
        # Timer initialization and setup for normal popups
        self.popupTimelineStart = QTimeLine(200)
        self.popupTimelineStart.setFrameRange(0,100)
        self.popupTimelineEnd = QTimeLine(200)
        self.popupTimelineEnd.setFrameRange(0,100)
        self.popupTimelineWait = QTimeLine()
        self.popupTimelineWait.setFrameRange(0,100)
        self.popupClue = False
        self.popupStory = False
        
        # Initialization and setup for animated popups
        self.popupAnimationOpen = QPropertyAnimation(self.gui.popup,"geometry")
        self.popupAnimationOpen.setDuration(200)
        self.popupAnimationOpen.setStartValue(QRect(0, 591, 0, 0))
        self.popupAnimationOpen.setEndValue(QRect(25, 25, 750, 450))
        self.popupAnimationClose = QPropertyAnimation(self.gui.popup,"geometry")
        self.popupAnimationClose.setDuration(200)
        self.popupAnimationClose.setStartValue(QRect(25, 25, 750, 450))
        self.popupAnimationClose.setEndValue(QRect(0, 591, 0, 0))
        self.popupAnimationWait = QTimeLine()
        
        self.toMain = False
        #self.gui.personView.centerOn(0,0)
        self.gui.mapView.centerOn(0,0)
        
########################################
### Signals and slots connected here ###
########################################

        # Connections for normal popups
        self.popupTimelineStart.frameChanged.connect(self.drawPopup)
        self.popupTimelineStart.finished.connect(self.popupWait)
        self.popupTimelineEnd.frameChanged.connect(self.erasePopup)   
        self.popupTimelineWait.finished.connect(self.enableErasePopup) 
        self.popupTimelineEnd.finished.connect(self.writeClue)
        
        # Connections for animated popups
        self.popupAnimationOpen.finished.connect(self.popupAnimationWait.start)
        self.popupAnimationWait.finished.connect(self.popupAnimationClose.start)
        self.popupAnimationClose.finished.connect(self.popupAnimationCleanup)
        self.finished.connect(self.writeStory)
    
    def connectGui(self):
        """Connect signals for Gui"""
        self.gui.actionQuit.triggered.connect(self.close)
        self.gui.quitButton.released.connect(self.close)
        self.gui.settingsButton.released.connect(self.setSettings)
        self.gui.actionSettings.triggered.connect(self.setSettings)
        self.gui.loadButton.released.connect(self.loadFileDialog)
        self.gui.actionSave_Game.triggered.connect(self.saveFileDialog)
        self.gui.doneButton.released.connect(self.goBack)
        self.gui.startButton.released.connect(self.enterName)
        self.gui.actionMain_Menu.triggered.connect(self.setMain)
        self.gui.actionHelp.triggered.connect(self.setInstructions)
        self.gui.instrButton.released.connect(self.setInstructions)
        self.gui.doneButton2.released.connect(self.goBack)
        self.gui.doneButton3.released.connect(self.goBack)
        self.gui.doneButtonScore.released.connect(self.scoreButton)
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
        self.game.frameTimer.timeout.connect(self.game.story.frameTime)
        self.game.story.clueTrouble.connect(self.giveHint)

########################################
###### Custom slots defined here #######
########################################

    def setSettings(self):
        """Change to the settings page in the stack widget"""
        self.setStackWidgetIndex(self.SETTINGS_PAGE)
        
    def setInstructions(self):
        """Change to the instructions page in the stack widget"""
        self.setStackWidgetIndex(self.INSTRUCTIONS_PAGE)

    def setCredits(self):
        """Change to the credits page in the stack widget"""
        self.setStackWidgetIndex(self.CREDITS_PAGE)
        
    def goBack(self):
        """Return to the last primary page in the stack"""
        self.setStackWidgetIndex(self.gui.stackIndex)
        if self.gui.stackIndex == self.GAME_PAGE:
            self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
        else:
            self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
    
    def scoreButton(self):
        """Set widget to main menu after winning the game"""
        self.setStackWidgetIndex(self.MAIN_PAGE)
        self.gui.stackIndex = self.MAIN_PAGE
        
    def scoreWidget(self):
        """change to score widget"""
        self.game.loadScores()
        if self.game.topTen:
            text = "Congratulations "+ self.game.playerName+ \
                   ".\nYou make the Top Ten List !!"
        else:
            text = "Congratulations "+ self.game.playerName + \
                   ".\nYour score is "+ `self.game.story.score` + "!!"
        self.gui.scores.setText(text)
        self.displayHighScores()
        self.setStackWidgetIndex(self.SCORE_PAGE)
    
    def displayHighScores(self):
        """After player wins the game, we want to display
           the 10th high scores on screen
        """
        text = ""
        markCurr = 0 # Mark curr player if he made to the top ten list
        debug("len of scoreLIst is: ", len(self.game.scoreList))
        for prevPlayer in self.game.scoreList:
            prevName = prevPlayer[0]
            prevScore = prevPlayer[1]
            if (markCurr == 0 and prevName == self.game.playerName \
            and prevScore == self.game.story.score):
                markCurr = 1
                text = text + prevPlayer[0] + 40*"."  + `prevPlayer[1]` + "  *****" + "\n"
            else:
                text = text + prevPlayer[0] + 40*"."  + `prevPlayer[1]` + "\n"
        self.gui.topTenScores.setText(text)
        self.game.writeScoreToFile() 
 

    def enterName(self):
        """Name enter dialog"""
        playerName, ok = QInputDialog.getText(self, 'Enter Name Dialog', 
            'Please enter your name:')

        if ok and playerName!="":
            self.newGame()
            self.game.playerName = playerName
        else:
            pass
            
    def loadFileDialog(self):
        """pop up the loading dialog for players to choose saved file"""
        fd = QFileDialog()
        filename = fd.getOpenFileName(None, "Load Saved Game",
                                      "saves", "MapMaster Save files (*.save)")

        if isfile(filename):
            self.loadGame(filename)
        
            self.gameWasLoaded = True
            self.filename = filename
        else:
            debug("invalid file")

    def loadGame(self, filename):
        """pop up the loading dialog for players to choose saved file"""

        self.setStackWidgetIndex(self.GAME_PAGE)
        self.game = Game() 
        self.connectGame()
        self.game.load(filename)
        debug("Initializing the saved game...")
        
        
        self.overlays['latLongOverlay'] = self.addOverlay(
                    normpath("images/latOverlayNew.png"))
        self.overlays['colorOverlay'] = self.addOverlay(
                    normpath("images/colorOverlay.png"))
        self.overlays['legendOverlay'] = self.addOverlay(
                    normpath("images/legendOverlayNew.png"))

        self.gui.scoreBox.setText((str)(self.game.story.score))
        self.gui.clueView.setText(self.game.story.currClue['text'])
        self.gui.stackIndex = self.GAME_PAGE

    def saveFileDialog(self,toMain = False):
        """Dialog to save a game"""
        filename = QFileDialog.getSaveFileName(None, "Save Game", "saves", 
                                               "MapMaster Save files (*.save)")        
        if filename == "":
            return False
        else:
            if ".save" not in filename:
                debug(".save is not in the file, add one..")
                filename = filename + ".save"
            debug("correctly save data to file...",filename)
            self.game.save(filename)    
              
                        
    def newGame(self):
        """Start a new game"""
        self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
        self.setStackWidgetIndex(self.STORY_PAGE)
        self.gui.stackIndex = self.STORY_PAGE
        
        # Create game instance and start the game
        self.game = Game()
        self.connectGame()
        self.game.new()
        debug("Starting a new game")
        
        self.overlays['latLongOverlay'] = self.addOverlay(
                        normpath("images/latOverlayNew.png"))
        self.overlays['colorOverlay'] = self.addOverlay(
                        normpath("images/colorOverlay.png"))
        self.overlays['legendOverlay'] = self.addOverlay(
                        normpath("images/legendOverlayNew.png"))
        self.gui.clueView.setText(self.game.story.currClue['text'])
        self.gui.scoreBox.setText((str)(0))

        self.gameWasLoaded = False
        
    def storyButton(self):
        """Continue from the story page to the game page"""
        self.setStackWidgetIndex(self.GAME_PAGE)
        self.gui.stackIndex = self.GAME_PAGE

    def setMain(self):
        """Create a message box when player want to go back to main menu
           from the middle of the game. Make sure that player save the game.
        """
        quit_msg = "Go back to Main Menu will lose all the game, are you sure?"
        reply = QMessageBox()
        reply.setWindowTitle("Back to Main")
        reply.setText(quit_msg)
        reply.setStandardButtons(
             QMessageBox.Ok | QMessageBox.Save |  QMessageBox.Cancel)
        reply.setDefaultButton(QMessageBox.Save)
        ret = reply.exec_()
        
        if ret == QMessageBox.Ok:
            debug( "Go back to main menu" )
            self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
            self.setStackWidgetIndex(self.MAIN_PAGE)
            self.gui.stackIndex = self.MAIN_PAGE
        elif ret == QMessageBox.Cancel:
            debug("cancel back to main menu action...")
            pass
        else:
            if (self.saveFileDialog() == False):
                debug("Not save yet, go back to game...")
                pass
            else:
                debug("save and back to main menu...")
                self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
                self.setStackWidgetIndex(self.MAIN_PAGE)
                self.gui.stackIndex = self.MAIN_PAGE
        
    def setStackWidgetIndex(self, index):
        """Allow to switch between widgets."""
        if index == self.MAIN_PAGE:
            self.gui.background.setPixmap(self.gui.backgroundPixmapMenu)
        else:
            self.gui.background.setPixmap(self.gui.backgroundPixmapSettings)
    
        self.gui.stackedWidget.setCurrentIndex(index)
        self.currStackIndex = index
        self.gui.soundManager.switchSongs(index)
    
    def latLong(self):
        """Turn on/off latitude graphic overlays in the mapView"""
        if self.gui.latLongCheck.isChecked():
            debug("Lat/long overlay on")
        else:
            debug("Lat/long overlay off")
        self.overlays['latLongOverlay'].setVisible(
                                        self.gui.latLongCheck.isChecked())
    
    def colorize(self):
        """Turn on/off color coding graphic overlays in the mapView"""
        if self.gui.colorCheck.isChecked():
            debug("Color overlay on")
        else:
            debug("Color overlay off")
        self.overlays['colorOverlay'].setVisible(
                                        self.gui.colorCheck.isChecked())
                                        
    def legend(self):
        """Turn on/off legend graphic overlays in the mapView"""
        if self.gui.legendCheck.isChecked():
            debug("Legend overlay on")
        else:
            debug("Legend overlay off")
        self.overlays['legendOverlay'].setVisible(
                                        self.gui.legendCheck.isChecked())

    def setVol(self):
        """Set volumn level for the game"""
        self.gui.soundManager.setVolume(self.gui.volumeSlider.sliderPosition())
        
    def doSearch(self):
        """Begins searching for a clue"""
        self.popupClue = True
        self.popupMessage("Searching...", 2*ONE_SECOND)
    
    def writeClue(self):
        """Handles the result of searching for a clue"""
        self.popupStory = False
        if self.popupClue:
            clueResult = self.game.story.searchForClue(
                                        self.game.character.getCenter())
            self.handleClueResult(clueResult[0], clueResult[1])
            self.popupClue = False
            if clueResult[0] == 'ClueFound':
                self.popupMessageAnimated(
                        'You found a clue!\n' + clueResult[1], 4*ONE_SECOND)
                self.gui.soundManager.playSound("success")
            elif clueResult[0] == 'ClueFailed':
                self.popupMessage(clueResult[1], 2*ONE_SECOND)
                self.gui.soundManager.playSound("failure")
            elif clueResult[0] == 'GameOver':
                self.popupMessage(clueResult[1], 5*ONE_SECOND) 
                self.gui.soundManager.playSound("victory")
                QTimer.singleShot(4*ONE_SECOND, self.scoreWidget)
            else:
                None

    def writeStory(self):
        """Handles drawing story"""
        if self.game.story.currClue['story'] != 'none':
            self.popupStory = True
            self.popupMessage(self.game.story.currClue['story'], 5*ONE_SECOND)
           
    def drawPopup(self, value):
        """Draws the popup to the screen"""
        debug("Called drawPopup")
        if self.popupStory:
            self.gui.popupStoryImage.setOpacity(value/100.0)
        else:
            self.gui.popupImage.setOpacity(value/100.0)
        self.gui.popupText.setOpacity(value/100.0)
        
    def enableErasePopup(self):
        """Starts the timeline for erasePopup"""
        debug("Enabled erase popup")
        self.popupTimelineEnd.start()
        
    def erasePopup(self, value):
        """Erases the popup from the screen"""
        debug("Called erase popup")
        if self.popupStory:
            self.gui.popupStoryImage.setOpacity(1-(value/100.0))
        else:
            self.gui.popupImage.setOpacity(1-(value/100.0))
        self.gui.popupText.setOpacity(1-(value/100.0))
        
    def popupWait(self):
        """Keeps the popup on the screeen"""
        debug("Entered popupWait")
        self.popupTimelineWait.start()
        
    def popupMessageAnimated(self, text, time):
        """Uses an animated popup to display text for some time"""
        self.gui.popupText.setPlainText('')
        self.gui.popup.setGeometry(QRect(0, 591, 0, 0))
        self.gui.popupImage.setOpacity(1)
        self.popupAnimationWait.setDuration(time)
        self.popupAnimationOpen.start()
        self.gui.popupText.setPlainText(text)
        self.gui.popupText.setOpacity(1)
        
    def popupAnimationCleanup(self):
        """Returns the popup to its original state after it finishes"""
        self.gui.popupImage.setOpacity(0)
        self.gui.popupText.setOpacity(0)
        self.gui.popup.setGeometry(QRect(25, 25, 750, 450))
        self.finished.emit()
        
    def handleClueResult(self, action, text):
        """Performs the writing to gui after a clue was found"""
        if action == 'ClueFound':
            self.gui.clueView.setText(text)
            self.gui.scoreBox.setText(`self.game.story.score`)
        elif action == 'GameOver':
            self.gui.clueView.setText(text)
        else:
            None
            
    def giveHint(self):
        """If the player has been stuck on a clue, give a hint"""
        text = self.game.story.troubleFindingClue()
        self.popupMessage(text, 5*ONE_SECOND)
    
    def popupMessage(self, text, time):
        """Displays the given text for the given time in a popup"""
        self.gui.popupText.setPlainText(text)
        self.popupTimelineWait.setDuration(time)
        self.popupTimelineStart.start()
       
    def keyPressEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        if self.game and (self.gui.stackIndex == self.GAME_PAGE):
            self.game.keyPress(event)

        #Work around because to make load work.
        if self.useLoadWorkaround and self.gameWasLoaded:
            self.game = Game() 
            self.connectGame()
            self.game.load(self.filename)
            
            debug("use work round")
            self.useLoadWorkaround = False
        
    
    def keyReleaseEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        if self.game and (self.gui.stackIndex == self.GAME_PAGE):
            key = event.key()
            if key==Qt.Key_Space or key==Qt.Key_Enter or key==Qt.Key_Return:
                self.doSearch()
            elif key==Qt.Key_L:
                debug('Character location is ' 
                        + `self.game.character.getCenter()`)
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
            debug("Accepting close event")
            event.accept()
        elif ret == QMessageBox.Cancel:
            event.ignore()
        else:
            if (self.saveFileDialog() == False):
                debug("Not quit yet, go back to game...")
                event.ignore()
            else:
                debug("Accepting close event")
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
        
    def updateGraphicsObject(self, xpos, ypos, name):
        """Changes the position of the character on the screen"""
        self.graphicsObjects[name].update(xpos, ypos)
        
    def addOverlay(self, filename):
        """Adds an overlay to the map view"""
        obj = self.gui.mapView.scene.addPixmap(QPixmap(filename))
        obj.setX(-195)
        obj.setY(-250)
        obj.setVisible(False)
        return obj
        
    def frameUpdate(self):
        """One tick of the game clock sent to the character"""
        self.game.character.frameUpdate(self.game.FRAME_RATE)

