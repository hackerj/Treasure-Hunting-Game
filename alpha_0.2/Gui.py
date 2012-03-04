# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created: Wed Feb 22 19:13:47 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui       #All of QT
from ViewGraphics import ViewGraphics #Person View Class
from os.path import normpath
from PyQt4.QtGui import QPixmap
from Events import searchCity
from os.path import normpath
from pygame import mixer

#Specify character encoding (8 Bit Unicode)
try:
    _fromUtf8 = QtCore.QString.fromUtf8 
except AttributeError:
    _fromUtf8 = lambda s: s

#Toplevel Widget Class for Game Window
class GuiMain(object):
    def __init__(self, data):
        
        self.data = data
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        
        #Set size of window and make it non-resizeable
        MainWindow.resize(818, 665)
        MainWindow.setFixedHeight(665)
        MainWindow.setFixedWidth(818)
        
        MainWindow.setWindowTitle("Map Master: Search for the Lost City")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon_medium.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        #Test Experimental Code
        self.background = QtGui.QLabel(MainWindow)
        self.background.setPixmap(QtGui.QPixmap(normpath("images/gameMenu2.png")))
        self.background.setGeometry(QtCore.QRect(0, 0, 818, 665))
        
        self.fg = "QLabel {color:black}"
        self.fgb = "QPushButton {color:black}"

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.menuPage = QtGui.QWidget()
        
        #Experimental audio (SHOULD NOT BE HERE)
        mixer.init()
        
        self.menuPage.setObjectName(_fromUtf8("menuPage"))
        self.startButton = QtGui.QPushButton(self.menuPage)
        self.startButton.setStyleSheet(self.fgb)
        self.startButton.setGeometry(QtCore.QRect(600, 200, 180, 60))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Start Game", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.loadButton = QtGui.QPushButton(self.menuPage)
        self.loadButton.setStyleSheet(self.fgb)
        self.loadButton.setGeometry(QtCore.QRect(600, 280, 180, 60))
        self.loadButton.setText(QtGui.QApplication.translate("MainWindow", "Load Game", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.settingsButton = QtGui.QPushButton(self.menuPage)
        self.settingsButton.setStyleSheet(self.fgb)
        self.settingsButton.setGeometry(QtCore.QRect(600, 440, 180, 60))
        self.settingsButton.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.quitButton = QtGui.QPushButton(self.menuPage)
        self.quitButton.setStyleSheet(self.fgb)
        self.quitButton.setGeometry(QtCore.QRect(600, 520, 180, 60))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.instrButton = QtGui.QPushButton(self.menuPage)
        self.instrButton.setStyleSheet(self.fgb)
        self.instrButton.setGeometry(QtCore.QRect(600, 360, 180, 60))
        self.instrButton.setText(QtGui.QApplication.translate("MainWindow", "Instructions", None, QtGui.QApplication.UnicodeUTF8))
        self.instrButton.setObjectName(_fromUtf8("instrButton"))
        self.stackedWidget.addWidget(self.menuPage)
        self.settingsPage = QtGui.QWidget()
        self.settingsPage.setObjectName(_fromUtf8("settingsPage"))
        self.volumeSlider = QtGui.QSlider(self.settingsPage)
        self.volumeSlider.setGeometry(QtCore.QRect(200, 200, 400, 30))
        self.volumeSlider.setProperty("value", 50)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.soundLabel = QtGui.QLabel(self.settingsPage)
        self.soundLabel.setGeometry(QtCore.QRect(340, 160, 120, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.soundLabel.setFont(font)
        self.soundLabel.setStyleSheet(self.fg)
        self.soundLabel.setText(QtGui.QApplication.translate("MainWindow", "Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.soundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.soundLabel.setObjectName(_fromUtf8("soundLabel"))
        
        #Quiet Sound Graphic
        self.quietGraphic = QtGui.QLabel(self.settingsPage)
        self.quietGraphic.setPixmap(QtGui.QPixmap(normpath("images/speakerQuiet.png")))
        self.quietGraphic.setGeometry(QtCore.QRect(90, 180, 80, 80))
        self.quietGraphic.setObjectName(_fromUtf8("quietGraphic"))
        
        #Loud Sound Graphic
        self.loudGraphic = QtGui.QLabel(self.settingsPage)
        self.loudGraphic.setPixmap(QtGui.QPixmap(normpath("images/speakerLoud.png")))
        self.loudGraphic.setEnabled(True)
        self.loudGraphic.setGeometry(QtCore.QRect(630, 180, 80, 80))
        self.loudGraphic.setObjectName(_fromUtf8("loudGraphic"))
        
        self.settingsLabel = QtGui.QLabel(self.settingsPage)
        self.settingsLabel.setGeometry(QtCore.QRect(260, 30, 280, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(36)
        self.settingsLabel.setFont(font)
        self.settingsLabel.setStyleSheet(self.fg)
        self.settingsLabel.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.settingsLabel.setObjectName(_fromUtf8("settingsLabel"))
        self.doneButton = QtGui.QPushButton(self.settingsPage)
        self.doneButton.setStyleSheet(self.fgb)
        self.doneButton.setGeometry(QtCore.QRect(600, 520, 161, 61))
        self.doneButton.setText(QtGui.QApplication.translate("MainWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setObjectName(_fromUtf8("doneButton"))
        self.stackedWidget.addWidget(self.settingsPage)
        self.mainPage = QtGui.QWidget()
        self.mainPage.setObjectName(_fromUtf8("mainPage"))
        
        #Person View
        self.personView = ViewGraphics(self.mainPage)
        self.personView.setGeometry(QtCore.QRect(0, 0, 390, 500))
        self.personView.setObjectName(_fromUtf8("personView"))
        
        #Map View
        self.mapView = ViewGraphics(self.mainPage)
        self.mapView.setGeometry(QtCore.QRect(410, 0, 390, 500))
        self.mapView.setObjectName(_fromUtf8("mapView"))
        
        #ClueView
        self.clueView = QtGui.QLabel(self.mainPage)
        self.clueView.setGeometry(QtCore.QRect(0, 510, 390, 91))
        self.clueView.setObjectName(_fromUtf8("clueView"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.clueView.setFont(font)
        self.clueView.setStyleSheet(self.fg)
        self.latLongCheck = QtGui.QCheckBox(self.mainPage)
        self.latLongCheck.setGeometry(QtCore.QRect(420, 510, 97, 41))
        self.latLongCheck.setText(QtGui.QApplication.translate("MainWindow", "Latitude/ \n"
        "Longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.latLongCheck.setObjectName(_fromUtf8("latLongCheck"))

        self.colorCheck = QtGui.QCheckBox(self.mainPage)
        self.colorCheck.setGeometry(QtCore.QRect(560, 510, 97, 41))
        self.colorCheck.setText(QtGui.QApplication.translate("MainWindow", "Color\n"
        "Coding", None, QtGui.QApplication.UnicodeUTF8))
        self.colorCheck.setObjectName(_fromUtf8("colorCheck"))
        self.legendCheck = QtGui.QCheckBox(self.mainPage)
        self.legendCheck.setGeometry(QtCore.QRect(680, 520, 97, 22))
        self.legendCheck.setText(QtGui.QApplication.translate("MainWindow", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.legendCheck.setObjectName(_fromUtf8("legendCheck"))
        self.searchButton = QtGui.QPushButton(self.mainPage)
        self.searchButton.setStyleSheet(self.fgb)
        self.searchButton.setGeometry(QtCore.QRect(420, 560, 211, 41))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.scoreBox = QtGui.QLabel(self.mainPage)
        self.scoreBox.setStyleSheet(self.fg)
        self.scoreBox.setGeometry(QtCore.QRect(720, 560, 71, 41))
        self.scoreBox.setObjectName(_fromUtf8("scoreBox"))
        self.scoreBox.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.scoreLabel = QtGui.QLabel(self.mainPage)
        self.scoreLabel.setStyleSheet(self.fg)
        self.scoreLabel.setGeometry(QtCore.QRect(660, 570, 51, 17))
        self.scoreLabel.setText(QtGui.QApplication.translate("MainWindow", "Score:", None, QtGui.QApplication.UnicodeUTF8))
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel.setObjectName(_fromUtf8("scoreLabel"))
        self.stackedWidget.addWidget(self.mainPage)
        self.helpPage = QtGui.QWidget()
        self.helpPage.setObjectName(_fromUtf8("helpPage"))
        self.HelpLabel = QtGui.QLabel(self.helpPage)
        self.HelpLabel.setStyleSheet(self.fg)
        self.HelpLabel.setGeometry(QtCore.QRect(260, 30, 280, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(36)
        self.HelpLabel.setFont(font)
        self.HelpLabel.setText(QtGui.QApplication.translate("MainWindow", "Instructions", None, QtGui.QApplication.UnicodeUTF8))
        self.HelpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HelpLabel.setObjectName(_fromUtf8("HelpLabel"))
        self.wInstr = QtGui.QLabel(self.helpPage)
        self.wInstr.setStyleSheet(self.fg)
        self.wInstr.setGeometry(QtCore.QRect(200, 150, 40, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.wInstr.setFont(font)
        self.wInstr.setText(QtGui.QApplication.translate("MainWindow", "W", None, QtGui.QApplication.UnicodeUTF8))
        self.wInstr.setAlignment(QtCore.Qt.AlignCenter)
        self.wInstr.setObjectName(_fromUtf8("wInstr"))
        self.sInstr = QtGui.QLabel(self.helpPage)
        self.sInstr.setStyleSheet(self.fg)
        self.sInstr.setGeometry(QtCore.QRect(200, 200, 40, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.sInstr.setFont(font)
        self.sInstr.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.sInstr.setAlignment(QtCore.Qt.AlignCenter)
        self.sInstr.setObjectName(_fromUtf8("sInstr"))
        self.aInstr = QtGui.QLabel(self.helpPage)
        self.aInstr.setStyleSheet(self.fg)
        self.aInstr.setGeometry(QtCore.QRect(200, 250, 40, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.aInstr.setFont(font)
        self.aInstr.setText(QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.aInstr.setAlignment(QtCore.Qt.AlignCenter)
        self.aInstr.setObjectName(_fromUtf8("aInstr"))
        self.dInstr = QtGui.QLabel(self.helpPage)
        self.dInstr.setStyleSheet(self.fg)
        self.dInstr.setGeometry(QtCore.QRect(200, 300, 40, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.dInstr.setFont(font)
        self.dInstr.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.dInstr.setAlignment(QtCore.Qt.AlignCenter)
        self.dInstr.setObjectName(_fromUtf8("dInstr"))
        self.wInstr2 = QtGui.QLabel(self.helpPage)
        self.wInstr2.setStyleSheet(self.fg)
        self.wInstr2.setGeometry(QtCore.QRect(400, 150, 180, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.wInstr2.setFont(font)
        self.wInstr2.setText(QtGui.QApplication.translate("MainWindow", "Move North", None, QtGui.QApplication.UnicodeUTF8))
        self.wInstr2.setAlignment(QtCore.Qt.AlignCenter)
        self.wInstr2.setObjectName(_fromUtf8("wInstr2"))
        self.sInstr2 = QtGui.QLabel(self.helpPage)
        self.sInstr2.setStyleSheet(self.fg)
        self.sInstr2.setGeometry(QtCore.QRect(400, 200, 180, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.sInstr2.setFont(font)
        self.sInstr2.setText(QtGui.QApplication.translate("MainWindow", "Move South", None, QtGui.QApplication.UnicodeUTF8))
        self.sInstr2.setAlignment(QtCore.Qt.AlignCenter)
        self.sInstr2.setObjectName(_fromUtf8("sInstr2"))
        self.aInstr2 = QtGui.QLabel(self.helpPage)
        self.aInstr2.setStyleSheet(self.fg)
        self.aInstr2.setGeometry(QtCore.QRect(400, 250, 180, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.aInstr2.setFont(font)
        self.aInstr2.setText(QtGui.QApplication.translate("MainWindow", "Move West", None, QtGui.QApplication.UnicodeUTF8))
        self.aInstr2.setAlignment(QtCore.Qt.AlignCenter)
        self.aInstr2.setObjectName(_fromUtf8("aInstr2"))
        self.dInstr2 = QtGui.QLabel(self.helpPage)
        self.dInstr2.setStyleSheet(self.fg)
        self.dInstr2.setGeometry(QtCore.QRect(400, 300, 180, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.dInstr2.setFont(font)
        self.dInstr2.setText(QtGui.QApplication.translate("MainWindow", "Move East", None, QtGui.QApplication.UnicodeUTF8))
        self.dInstr2.setAlignment(QtCore.Qt.AlignCenter)
        self.dInstr2.setObjectName(_fromUtf8("dInstr2"))
        self.searchInstr = QtGui.QPushButton(self.helpPage)
        self.searchInstr.setStyleSheet(self.fgb)
        self.searchInstr.setEnabled(True)
        self.searchInstr.setGeometry(QtCore.QRect(170, 350, 100, 30))
        self.searchInstr.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchInstr.setAutoDefault(False)
        self.searchInstr.setDefault(False)
        self.searchInstr.setFlat(False)
        self.searchInstr.setObjectName(_fromUtf8("searchInstr"))
        self.dInstr2_2 = QtGui.QLabel(self.helpPage)
        self.dInstr2_2.setStyleSheet(self.fg)
        self.dInstr2_2.setGeometry(QtCore.QRect(380, 350, 211, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.dInstr2_2.setFont(font)
        self.dInstr2_2.setText(QtGui.QApplication.translate("MainWindow", "Search for clues", None, QtGui.QApplication.UnicodeUTF8))
        self.dInstr2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dInstr2_2.setObjectName(_fromUtf8("dInstr2_2"))
        self.doneButton2 = QtGui.QPushButton(self.helpPage)
        self.doneButton2.setStyleSheet(self.fgb)
        self.doneButton2.setGeometry(QtCore.QRect(600, 520, 161, 61))
        self.doneButton2.setText(QtGui.QApplication.translate("MainWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton2.setObjectName(_fromUtf8("doneButton2"))
        self.stackedWidget.addWidget(self.helpPage)
        self.creditsPage = QtGui.QWidget()
        self.creditsPage.setObjectName(_fromUtf8("creditsPage"))
        self.creditsLabel = QtGui.QLabel(self.creditsPage)
        self.creditsLabel.setStyleSheet(self.fg)
        self.creditsLabel.setGeometry(QtCore.QRect(260, 30, 280, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(36)
        self.creditsLabel.setFont(font)
        self.creditsLabel.setText(QtGui.QApplication.translate("MainWindow", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.creditsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.creditsLabel.setObjectName(_fromUtf8("creditsLabel"))
        self.credits = QtGui.QLabel(self.creditsPage)
        self.credits.setStyleSheet(self.fg)
        self.credits.setGeometry(QtCore.QRect(180, 150, 440, 210))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        self.credits.setFont(font)
        self.credits.setText(QtGui.QApplication.translate("MainWindow", "Gary Lent\n"
        "Grant Stafford\n"
        "Jessie Liu\n"
        "Peter Andrien\n"
        "Nokia (Qt4 framework)\n"
        "Riverbank Computing Ltd (PyQt)\n"
        "Celestial Aeon Project", None, QtGui.QApplication.UnicodeUTF8))
        self.credits.setAlignment(QtCore.Qt.AlignCenter)
        self.credits.setObjectName(_fromUtf8("credits"))
        self.doneButton3 = QtGui.QPushButton(self.creditsPage)
        self.doneButton3.setStyleSheet(self.fgb)
        self.doneButton3.setGeometry(QtCore.QRect(600, 520, 161, 61))
        self.doneButton3.setText(QtGui.QApplication.translate("MainWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton3.setObjectName(_fromUtf8("doneButton3"))
        self.stackedWidget.addWidget(self.creditsPage)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.actionSave_Game = QtGui.QAction(MainWindow)
        self.actionSave_Game.setText(QtGui.QApplication.translate("MainWindow", "Save Game", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Game.setObjectName(_fromUtf8("actionSave_Game"))
        self.actionCredits = QtGui.QAction(MainWindow)
        self.actionCredits.setText(QtGui.QApplication.translate("MainWindow", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setObjectName(_fromUtf8("actionCredits"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionMain_Menu = QtGui.QAction(MainWindow)
        self.actionMain_Menu.setText(QtGui.QApplication.translate("MainWindow", "Main Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMain_Menu.setObjectName(_fromUtf8("actionMain_Menu"))
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
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL(_fromUtf8("released()")), MainWindow.close)
        QtCore.QObject.connect(self.settingsButton, QtCore.SIGNAL(_fromUtf8("released()")), self.setSettings)
        QtCore.QObject.connect(self.actionSettings, QtCore.SIGNAL(_fromUtf8("triggered()")), self.setSettings)
        QtCore.QObject.connect(self.loadButton, QtCore.SIGNAL(_fromUtf8("released()")), self.load_file_dialog)
        QtCore.QObject.connect(self.actionSave_Game, QtCore.SIGNAL(_fromUtf8("triggered()")),self.save_file_dialog)
        QtCore.QObject.connect(self.doneButton, QtCore.SIGNAL(_fromUtf8("released()")), self.goBack)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL(_fromUtf8("released()")), self.newGame)
        QtCore.QObject.connect(self.actionMain_Menu, QtCore.SIGNAL(_fromUtf8("triggered()")), self.setMain)
        QtCore.QObject.connect(self.actionHelp, QtCore.SIGNAL(_fromUtf8("triggered()")), self.setInstructions)
        QtCore.QObject.connect(self.instrButton, QtCore.SIGNAL(_fromUtf8("released()")), self.setInstructions)
        QtCore.QObject.connect(self.doneButton2, QtCore.SIGNAL(_fromUtf8("released()")), self.goBack)
        QtCore.QObject.connect(self.doneButton3, QtCore.SIGNAL(_fromUtf8("released()")), self.goBack)
        QtCore.QObject.connect(self.actionCredits, QtCore.SIGNAL(_fromUtf8("triggered()")), self.setCredits)
        self.latLongCheck.stateChanged.connect(self.latLong)
        self.colorCheck.stateChanged.connect(self.colorize)
        self.legendCheck.stateChanged.connect(self.legend)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("released()")), self.doSearch)
        self.volumeSlider.sliderMoved.connect(self.setVol)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.newSound = mixer.Sound(normpath("sounds/theme.wav"))
        self.newSound.set_volume(float(self.volumeSlider.sliderPosition())/100.0)
        self.newSound.play()

    def retranslateUi(self, MainWindow):
        pass

    #Custom signals are here        
    def setSettings(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def setInstructions(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def setCredits(self):
        self.stackedWidget.setCurrentIndex(4)
        
    def goBack(self):
        self.stackedWidget.setCurrentIndex(self.location)
        
    def load_file_dialog(self):
        fd = QtGui.QFileDialog()
        self.filename = fd.getOpenFileName(None, "Load Saved Game", "saves", "MapMaster Save files (*.save)")
        from os.path import isfile
        if isfile(self.filename):
            self.fname = open(self.filename)
            self.loadData = self.fname.read()
            print self.loadData
            self.fname.close()
            
    def save_file_dialog(self):
        filename = QtGui.QFileDialog.getSaveFileName(None,"Save Game", "saves", "MapMaster Save files (*.save)")
        if ".save" in filename:
            self.fname = open(filename, "w")
        else:
            self.fname = open(filename + ".save",'w')
        self.fname.write("Hello")
        self.fname.close()
    
    def newGame(self):
        self.stackedWidget.setCurrentIndex(2)
        self.location = 2
        
    def setMain(self):
        self.save_file_dialog()
        self.stackedWidget.setCurrentIndex(0)
        self.location = 0
        
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
        num = self.volumeSlider.sliderPosition()
        self.newSound.set_volume(float(num)/100.0)
    
    def doSearch(self):
        searchCity(self.data)
            
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
