# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4 import QtCore, QtGui              #All of QT
from ViewGraphics import ViewGraphics #Person View Class
from os.path import normpath
from os.path import isfile
from PyQt4.QtGui import QPixmap, QIcon, QWidget, QLabel, QStackedWidget, \
    QGridLayout, QPushButton, QApplication, QSlider, QFont, QCheckBox, \
    QMenuBar, QMenu, QAction, QFileDialog, QMainWindow
from Events import searchLandmark
from Sounds import Sounds
from Load import *


#Toplevel Widget Class for Game Window
class GuiMain(object):
    def __init__(self, data):
        
        self.data = data
        self.loadSave = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        #Set size of window and make it non-resizeable
        MainWindow.resize(818, 665)
        MainWindow.setFixedHeight(665)
        MainWindow.setFixedWidth(818)
        
        MainWindow.setWindowTitle("Map Master: Search for the Lost City")
        MainWindow.setWindowIcon(QIcon("icon_medium.ico"))

        #Set window backgrounds
        self.background = QLabel(MainWindow)
        
        
        self.backgroundPixmapMenu = QPixmap(normpath("images/gameMenu2.png"))
        self.backgroundPixmapSettings = QPixmap(normpath("images/gameMenuSettings2.png"))
        self.background.setPixmap(self.backgroundPixmapMenu)       
        
        self.background.setGeometry(QtCore.QRect(0, 0, 818, 665))
        
        #Stylesheet settings for labels and buttons
        self.fg = "QLabel {color:black}"
        self.fgb = "QPushButton {color:black}"

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName("stackedWidget")
        
        #Main Menu page
        self.menuPage = QWidget()
        self.menuPage.setObjectName("menuPage")
        self.startButton = QPushButton(self.menuPage)
        self.startButton.setStyleSheet(self.fgb)
        self.startButton.setGeometry(QtCore.QRect(600, 200, 180, 60))
        self.startButton.setText(QApplication.translate("MainWindow", "Start Game", None, QApplication.UnicodeUTF8))
        self.startButton.setObjectName("startButton")
        self.loadButton = QPushButton(self.menuPage)
        self.loadButton.setStyleSheet(self.fgb)
        self.loadButton.setGeometry(QtCore.QRect(600, 280, 180, 60))
        self.loadButton.setText(QApplication.translate("MainWindow", "Load Game", None, QApplication.UnicodeUTF8))
        self.loadButton.setObjectName("loadButton")
        self.settingsButton = QPushButton(self.menuPage)
        self.settingsButton.setStyleSheet(self.fgb)
        self.settingsButton.setGeometry(QtCore.QRect(600, 440, 180, 60))
        self.settingsButton.setText(QApplication.translate("MainWindow", "Settings", None, QApplication.UnicodeUTF8))
        self.settingsButton.setObjectName("settingsButton")
        self.quitButton = QPushButton(self.menuPage)
        self.quitButton.setStyleSheet(self.fgb)
        self.quitButton.setGeometry(QtCore.QRect(600, 520, 180, 60))
        self.quitButton.setText(QApplication.translate("MainWindow", "Quit", None, QApplication.UnicodeUTF8))
        self.quitButton.setObjectName("quitButton")
        self.instrButton = QPushButton(self.menuPage)
        self.instrButton.setStyleSheet(self.fgb)
        self.instrButton.setGeometry(QtCore.QRect(600, 360, 180, 60))
        self.instrButton.setText(QApplication.translate("MainWindow", "Instructions", None, QApplication.UnicodeUTF8))
        self.instrButton.setObjectName("instrButton")
        self.stackedWidget.addWidget(self.menuPage)
        
        #Settings page
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.volumeSlider = QSlider(self.settingsPage)
        self.volumeSlider.setGeometry(QtCore.QRect(200, 200, 400, 30))
        self.volumeSlider.setProperty("value", 50)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.soundLabel = QLabel(self.settingsPage)
        self.soundLabel.setGeometry(QtCore.QRect(340, 160, 120, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.soundLabel.setFont(font)
        self.soundLabel.setStyleSheet(self.fg)
        self.soundLabel.setText(QApplication.translate("MainWindow", "Volume", None, QApplication.UnicodeUTF8))
        self.soundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.soundLabel.setObjectName("soundLabel")
        
        #Quiet Sound Graphic
        self.quietGraphic = QLabel(self.settingsPage)
        self.quietGraphic.setPixmap(QPixmap(normpath("images/speakerQuiet.png")))
        self.quietGraphic.setGeometry(QtCore.QRect(90, 180, 80, 80))
        self.quietGraphic.setObjectName("quietGraphic")
        
        #Loud Sound Graphic
        self.loudGraphic = QLabel(self.settingsPage)
        self.loudGraphic.setPixmap(QPixmap(normpath("images/speakerLoud.png")))
        self.loudGraphic.setEnabled(True)
        self.loudGraphic.setGeometry(QtCore.QRect(630, 180, 80, 80))
        self.loudGraphic.setObjectName("loudGraphic")
        
        self.settingsLabel = QLabel(self.settingsPage)
        self.settingsLabel.setGeometry(QtCore.QRect(260, 30, 280, 60))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(36)
        self.settingsLabel.setFont(font)
        self.settingsLabel.setStyleSheet(self.fg)
        self.settingsLabel.setText(QApplication.translate("MainWindow", "Settings", None, QApplication.UnicodeUTF8))
        self.settingsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.settingsLabel.setObjectName("settingsLabel")
        self.doneButton = QPushButton(self.settingsPage)
        self.doneButton.setStyleSheet(self.fgb)
        self.doneButton.setGeometry(QtCore.QRect(600, 520, 161, 61))
        self.doneButton.setText(QApplication.translate("MainWindow", "Done", None, QApplication.UnicodeUTF8))
        self.doneButton.setObjectName("doneButton")
        self.stackedWidget.addWidget(self.settingsPage)
        
        self.soundManager = Sounds(self.volumeSlider.sliderPosition())
        
        #Main Game page
        self.mainPage = QWidget()
        self.mainPage.setObjectName("mainPage")
        
        #Person View
        self.personView = ViewGraphics(self.mainPage)
        self.personView.setGeometry(QtCore.QRect(0, 0, 390, 500))
        self.personView.setObjectName("personView")
        
        #Map View
        self.mapView = ViewGraphics(self.mainPage)
        self.mapView.setGeometry(QtCore.QRect(410, 0, 390, 500))
        self.mapView.setObjectName("mapView")
        
        #ClueView
        self.clueView = QLabel(self.mainPage)
        self.clueView.setGeometry(QtCore.QRect(0, 510, 390, 91))
        self.clueView.setObjectName("clueView")
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.clueView.setFont(font)
        self.clueView.setStyleSheet(self.fg)
        
        #Map Toggles
        self.latLongCheck = QCheckBox(self.mainPage)
        self.latLongCheck.setGeometry(QtCore.QRect(420, 510, 97, 41))
        self.latLongCheck.setText(QApplication.translate("MainWindow", "Latitude/ \n"
        "Longitude", None, QApplication.UnicodeUTF8))
        self.latLongCheck.setObjectName("latLongCheck")

        self.colorCheck = QCheckBox(self.mainPage)
        self.colorCheck.setGeometry(QtCore.QRect(560, 510, 97, 41))
        self.colorCheck.setText(QApplication.translate("MainWindow", "Color\n"
        "Coding", None, QApplication.UnicodeUTF8))
        self.colorCheck.setObjectName("colorCheck")
        self.legendCheck = QCheckBox(self.mainPage)
        self.legendCheck.setGeometry(QtCore.QRect(680, 520, 97, 22))
        self.legendCheck.setText(QApplication.translate("MainWindow", "Legend", None, QApplication.UnicodeUTF8))
        self.legendCheck.setObjectName("legendCheck")
        self.searchButton = QPushButton(self.mainPage)
        self.searchButton.setStyleSheet(self.fgb)
        self.searchButton.setGeometry(QtCore.QRect(420, 560, 211, 41))
        self.searchButton.setText(QApplication.translate("MainWindow", "Search", None, QApplication.UnicodeUTF8))
        self.searchButton.setObjectName("searchButton")
        
        #Score pieces
        self.scoreBox = QLabel(self.mainPage)
        self.scoreBox.setStyleSheet(self.fg)
        self.scoreBox.setGeometry(QtCore.QRect(720, 560, 71, 41))
        self.scoreBox.setObjectName("scoreBox")
        self.scoreBox.setText(QApplication.translate("MainWindow", "0", None, QApplication.UnicodeUTF8))
        self.scoreLabel = QLabel(self.mainPage)
        self.scoreLabel.setStyleSheet(self.fg)
        self.scoreLabel.setGeometry(QtCore.QRect(660, 570, 51, 17))
        self.scoreLabel.setText(QApplication.translate("MainWindow", "Score:", None, QApplication.UnicodeUTF8))
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel.setObjectName("scoreLabel")
        self.stackedWidget.addWidget(self.mainPage)
        
        #Help page
        self.helpPage = QWidget()
        self.helpPage.setObjectName("helpPage")
        self.HelpLabel = QLabel(self.helpPage)
        self.HelpLabel.setStyleSheet(self.fg)
        self.HelpLabel.setGeometry(QtCore.QRect(260, 30, 280, 60))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(36)
        self.HelpLabel.setFont(font)
        self.HelpLabel.setText(QApplication.translate("MainWindow", "Instructions", None, QApplication.UnicodeUTF8))
        self.HelpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HelpLabel.setObjectName("HelpLabel")
        self.wInstr = QLabel(self.helpPage)
        self.wInstr.setStyleSheet(self.fg)
        self.wInstr.setGeometry(QtCore.QRect(200, 150, 40, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.wInstr.setFont(font)
        self.wInstr.setText(QApplication.translate("MainWindow", "W", None, QApplication.UnicodeUTF8))
        self.wInstr.setAlignment(QtCore.Qt.AlignCenter)
        self.wInstr.setObjectName("wInstr")
        self.sInstr = QLabel(self.helpPage)
        self.sInstr.setStyleSheet(self.fg)
        self.sInstr.setGeometry(QtCore.QRect(200, 200, 40, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.sInstr.setFont(font)
        self.sInstr.setText(QApplication.translate("MainWindow", "S", None, QApplication.UnicodeUTF8))
        self.sInstr.setAlignment(QtCore.Qt.AlignCenter)
        self.sInstr.setObjectName("sInstr")
        self.aInstr = QLabel(self.helpPage)
        self.aInstr.setStyleSheet(self.fg)
        self.aInstr.setGeometry(QtCore.QRect(200, 250, 40, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.aInstr.setFont(font)
        self.aInstr.setText(QApplication.translate("MainWindow", "A", None, QApplication.UnicodeUTF8))
        self.aInstr.setAlignment(QtCore.Qt.AlignCenter)
        self.aInstr.setObjectName("aInstr")
        self.dInstr = QLabel(self.helpPage)
        self.dInstr.setStyleSheet(self.fg)
        self.dInstr.setGeometry(QtCore.QRect(200, 300, 40, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.dInstr.setFont(font)
        self.dInstr.setText(QApplication.translate("MainWindow", "D", None, QApplication.UnicodeUTF8))
        self.dInstr.setAlignment(QtCore.Qt.AlignCenter)
        self.dInstr.setObjectName("dInstr")
        self.wInstr2 = QLabel(self.helpPage)
        self.wInstr2.setStyleSheet(self.fg)
        self.wInstr2.setGeometry(QtCore.QRect(400, 150, 180, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.wInstr2.setFont(font)
        self.wInstr2.setText(QApplication.translate("MainWindow", "Move North", None, QApplication.UnicodeUTF8))
        self.wInstr2.setAlignment(QtCore.Qt.AlignCenter)
        self.wInstr2.setObjectName("wInstr2")
        self.sInstr2 = QLabel(self.helpPage)
        self.sInstr2.setStyleSheet(self.fg)
        self.sInstr2.setGeometry(QtCore.QRect(400, 200, 180, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.sInstr2.setFont(font)
        self.sInstr2.setText(QApplication.translate("MainWindow", "Move South", None, QApplication.UnicodeUTF8))
        self.sInstr2.setAlignment(QtCore.Qt.AlignCenter)
        self.sInstr2.setObjectName("sInstr2")
        self.aInstr2 = QLabel(self.helpPage)
        self.aInstr2.setStyleSheet(self.fg)
        self.aInstr2.setGeometry(QtCore.QRect(400, 250, 180, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.aInstr2.setFont(font)
        self.aInstr2.setText(QApplication.translate("MainWindow", "Move West", None, QApplication.UnicodeUTF8))
        self.aInstr2.setAlignment(QtCore.Qt.AlignCenter)
        self.aInstr2.setObjectName("aInstr2")
        self.dInstr2 = QLabel(self.helpPage)
        self.dInstr2.setStyleSheet(self.fg)
        self.dInstr2.setGeometry(QtCore.QRect(400, 300, 180, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.dInstr2.setFont(font)
        self.dInstr2.setText(QApplication.translate("MainWindow", "Move East", None, QApplication.UnicodeUTF8))
        self.dInstr2.setAlignment(QtCore.Qt.AlignCenter)
        self.dInstr2.setObjectName("dInstr2")
        self.searchInstr = QPushButton(self.helpPage)
        self.searchInstr.setStyleSheet(self.fgb)
        self.searchInstr.setEnabled(True)
        self.searchInstr.setGeometry(QtCore.QRect(170, 350, 100, 30))
        self.searchInstr.setText(QApplication.translate("MainWindow", "Search", None, QApplication.UnicodeUTF8))
        self.searchInstr.setAutoDefault(False)
        self.searchInstr.setDefault(False)
        self.searchInstr.setFlat(False)
        self.searchInstr.setObjectName("searchInstr")
        self.dInstr2_2 = QLabel(self.helpPage)
        self.dInstr2_2.setStyleSheet(self.fg)
        self.dInstr2_2.setGeometry(QtCore.QRect(380, 350, 211, 30))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.dInstr2_2.setFont(font)
        self.dInstr2_2.setText(QApplication.translate("MainWindow", "Search for clues", None, QApplication.UnicodeUTF8))
        self.dInstr2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dInstr2_2.setObjectName("dInstr2_2")
        self.doneButton2 = QPushButton(self.helpPage)
        self.doneButton2.setStyleSheet(self.fgb)
        self.doneButton2.setGeometry(QtCore.QRect(600, 520, 161, 61))
        self.doneButton2.setText(QApplication.translate("MainWindow", "Done", None, QApplication.UnicodeUTF8))
        self.doneButton2.setObjectName("doneButton2")
        self.stackedWidget.addWidget(self.helpPage)
        
        #Credits page
        self.creditsPage = QWidget()
        self.creditsPage.setObjectName("creditsPage")
        self.creditsLabel = QLabel(self.creditsPage)
        self.creditsLabel.setStyleSheet(self.fg)
        self.creditsLabel.setGeometry(QtCore.QRect(260, 30, 280, 60))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(36)
        self.creditsLabel.setFont(font)
        self.creditsLabel.setText(QApplication.translate("MainWindow", "Credits", None, QApplication.UnicodeUTF8))
        self.creditsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.creditsLabel.setObjectName("creditsLabel")
        self.credits = QLabel(self.creditsPage)
        self.credits.setStyleSheet(self.fg)
        self.credits.setGeometry(QtCore.QRect(180, 150, 500, 400))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        self.credits.setFont(font)
        self.credits.setText(QApplication.translate("MainWindow", 
        "Gary Lent\n"
        "Grant Stafford\n"
        "Jessie Liu\n"
        "Peter Andrien\n"
        "Nokia (Qt4 framework)\n"
        "Riverbank Computing Ltd (PyQt)\n"
        "Celestial Aeon Project", None, QApplication.UnicodeUTF8))
        self.credits.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.credits.setObjectName("credits")
        self.doneButton3 = QPushButton(self.creditsPage)
        self.doneButton3.setStyleSheet(self.fgb)
        self.doneButton3.setGeometry(QtCore.QRect(600, 520, 161, 61))
        self.doneButton3.setText(QApplication.translate("MainWindow", "Done", None, QApplication.UnicodeUTF8))
        self.doneButton3.setObjectName("doneButton3")
        self.stackedWidget.addWidget(self.creditsPage)
        
        #Story page
        self.storyPage = QWidget()
        self.storyPage.setObjectName("storyPage")
        self.storyLabel = QLabel(self.storyPage)
        self.storyLabel.setStyleSheet(self.fg)
        self.storyLabel.setGeometry(QtCore.QRect(100, 50, 600, 400))
        font = QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(25)
        self.storyLabel.setFont(font)
        self.storyLabel.setText(QApplication.translate("MainWindow", "My name is Travis Sinclair.\n I'm a skilled cartographer.\n I recently lost my job, but stumbled\n on a clue that may change my life \nforever. I've set off on a quest - a quest\n to find a lost city. I've found a clue,\n and believe there may be more.\n Help me find the lost city.  ", None, QApplication.UnicodeUTF8))
        self.storyLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.storyLabel.setObjectName("storyLabel")
        self.nextButton = QPushButton(self.storyPage)
        self.nextButton.setGeometry(QtCore.QRect(600, 520, 161, 61))
        self.nextButton.setText(QApplication.translate("MainWindow", "Next", None, QApplication.UnicodeUTF8))
        self.nextButton.setObjectName("nextButton")
        self.stackedWidget.addWidget(self.storyPage)
        
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        #Menu bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 25))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setTitle(QApplication.translate("MainWindow", "Menu", None, QApplication.UnicodeUTF8))
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave_Game = QAction(MainWindow)
        self.actionSave_Game.setText(QApplication.translate("MainWindow", "Save Game", None, QApplication.UnicodeUTF8))
        self.actionSave_Game.setObjectName("actionSave_Game")
        self.actionCredits = QAction(MainWindow)
        self.actionCredits.setText(QApplication.translate("MainWindow", "Credits", None, QApplication.UnicodeUTF8))
        self.actionCredits.setObjectName("actionCredits")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setText(QApplication.translate("MainWindow", "Quit", None, QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName("actionQuit")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setText(QApplication.translate("MainWindow", "Settings", None, QApplication.UnicodeUTF8))
        self.actionSettings.setObjectName("actionSettings")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setText(QApplication.translate("MainWindow", "Help", None, QApplication.UnicodeUTF8))
        self.actionHelp.setObjectName("actionHelp")
        self.actionMain_Menu = QAction(MainWindow)
        self.actionMain_Menu.setText(QApplication.translate("MainWindow", "Main Menu", None, QApplication.UnicodeUTF8))
        self.actionMain_Menu.setObjectName("actionMain_Menu")
        self.menuMenu.addAction(self.actionSettings)
        self.menuMenu.addAction(self.actionHelp)
        self.menuMenu.addAction(self.actionSave_Game)
        self.menuMenu.addAction(self.actionCredits)
        self.menuMenu.addAction(self.actionMain_Menu)
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())
        

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #These are the slots and signals to connect buttons to other functions
        self.location = 0
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL("released()"), MainWindow.close)
        QtCore.QObject.connect(self.settingsButton, QtCore.SIGNAL("released()"), self.setSettings)
        QtCore.QObject.connect(self.actionSettings, QtCore.SIGNAL("triggered()"), self.setSettings)
        QtCore.QObject.connect(self.loadButton, QtCore.SIGNAL("released()"), self.load_file_dialog)
        QtCore.QObject.connect(self.actionSave_Game, QtCore.SIGNAL("triggered()"),self.save_file_dialog)
        QtCore.QObject.connect(self.doneButton, QtCore.SIGNAL("released()"), self.goBack)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL("released()"), self.newGame)
        QtCore.QObject.connect(self.actionMain_Menu, QtCore.SIGNAL("triggered()"), self.setMain)
        QtCore.QObject.connect(self.actionHelp, QtCore.SIGNAL("triggered()"), self.setInstructions)
        QtCore.QObject.connect(self.instrButton, QtCore.SIGNAL("released()"), self.setInstructions)
        QtCore.QObject.connect(self.doneButton2, QtCore.SIGNAL("released()"), self.goBack)
        QtCore.QObject.connect(self.doneButton3, QtCore.SIGNAL("released()"), self.goBack)
        QtCore.QObject.connect(self.actionCredits, QtCore.SIGNAL("triggered()"), self.setCredits)
        self.latLongCheck.stateChanged.connect(self.latLong)
        self.colorCheck.stateChanged.connect(self.colorize)
        self.legendCheck.stateChanged.connect(self.legend)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL("released()"), self.doSearch)
        QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL("released()"), self.storyButton)
        self.volumeSlider.sliderMoved.connect(self.setVol)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

    #Custom signals are here        
    def setSettings(self):
        self.background.setPixmap(self.backgroundPixmapSettings)    
        self.stackedWidget.setCurrentIndex(1)
        
    def setInstructions(self):
        self.background.setPixmap(self.backgroundPixmapSettings)    
        self.stackedWidget.setCurrentIndex(3)
        
    def setCredits(self):
        self.background.setPixmap(self.backgroundPixmapSettings)       
        self.stackedWidget.setCurrentIndex(4)
        
    def goBack(self):
        self.stackedWidget.setCurrentIndex(self.location)
        if self.location == 0:
            self.background.setPixmap(self.backgroundPixmapMenu)
        else:
            None
            #Should be something here later.
        
    def load_file_dialog(self):
        fd = QFileDialog()
        self.filename = fd.getOpenFileName(None, "Load Saved Game", "saves", "MapMaster Save files (*.save)")
        if isfile(self.filename):
            self.loadSaved = True
            self.stackedWidget.setCurrentIndex(2)
            self.location = 2
            self.soundManager.switchSongs(self.location)
            
            
    def save_file_dialog(self):
        filename = QtGui.QFileDialog.getSaveFileName(None,"Save Game", "saves", "MapMaster Save files (*.save)")
        if filename == "":
            print "No file specified!"
        else:
           
            if ".save" in filename:
                self.fname = open(filename, "w")
            else:
                self.fname = open(filename + ".save",'w')
                
            score = str(self.data.score)
            numClues = str(len(self.data.clueStack))
            charX, charY = self.data.character.getCenter()
            whiteSpace = "       "
            toWriteList = whiteSpace + str(charX) + whiteSpace + str(charY) + whiteSpace + numClues + whiteSpace + score
            self.fname.write(toWriteList)     
            self.fname.close()
            
    
        
       
    def newGame(self):
        self.background.setPixmap(self.backgroundPixmapSettings)
        self.filename = None    
        self.stackedWidget.setCurrentIndex(5)
        self.location = 5
        
    def storyButton(self):
    
        self.stackedWidget.setCurrentIndex(2)
        self.location = 2
        self.soundManager.switchSongs(self.location)
       
    def setMain(self):
        self.save_file_dialog()
        self.background.setPixmap(self.backgroundPixmapMenu)
        self.stackedWidget.setCurrentIndex(0)
        self.location = 0
        self.soundManager.switchSongs(self.location)      
           
        
    def latLong(self):
        if self.latLongCheck.isChecked():
            print "Lat/long overlay on"
        else:
            print "Lat/long overlay off"
        self.data.overlays['latLongOverlay'].mViewObj.setVisible(self.latLongCheck.isChecked())
        
    def colorize(self):
        if self.colorCheck.isChecked():
            print "Color overlay on"
        else:
            print "Color overlay off"
        self.data.overlays['colorOverlay'].mViewObj.setVisible(self.colorCheck.isChecked())
        
    def legend(self):
        if self.legendCheck.isChecked():
            print "Legend overlay on"
        else:
            print "Legend overlay off"
        self.data.overlays['legendOverlay'].mViewObj.setVisible(self.legendCheck.isChecked())
    
    def setVol(self):
        self.soundManager.setVolume(self.volumeSlider.sliderPosition())
    
    def doSearch(self):
        searchLandmark(self.data)
            
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
