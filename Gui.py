from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 603)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Map Master: Search for the Lost City", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon_medium.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))        
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.Menu = QtGui.QMenu(self.menubar)
        self.Menu.setTitle(_fromUtf8(""))
        self.Menu.setObjectName(_fromUtf8("Menu"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Game = QtGui.QAction(MainWindow)
        self.actionNew_Game.setText(QtGui.QApplication.translate("MainWindow", "New Game", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Game.setObjectName(_fromUtf8("actionNew_Game"))
        self.actionLoad_Game = QtGui.QAction(MainWindow)
        self.actionLoad_Game.setText(QtGui.QApplication.translate("MainWindow", "Load Game", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Game.setObjectName(_fromUtf8("actionLoad_Game"))
        self.actionSave_Game = QtGui.QAction(MainWindow)
        self.actionSave_Game.setText(QtGui.QApplication.translate("MainWindow", "Save Game", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Game.setObjectName(_fromUtf8("actionSave_Game"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionCredits = QtGui.QAction(MainWindow)
        self.actionCredits.setText(QtGui.QApplication.translate("MainWindow", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setObjectName(_fromUtf8("actionCredits"))
        self.menuMenu.addAction(self.actionNew_Game)
        self.menuMenu.addAction(self.actionLoad_Game)
        self.menuMenu.addAction(self.actionSave_Game)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionCredits)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.Menu.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

class Ui_Game(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        Frame.setFrameShape(QtGui.QFrame.NoFrame)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        Frame.resize(790, 560)
        
        
        self.gridLayout = QtGui.QGridLayout(Frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.PersonView = QtGui.QGraphicsView(Frame)
        self.PersonView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.PersonView.setObjectName(_fromUtf8("PersonView"))
        self.gridLayout.addWidget(self.PersonView, 0, 0, 2, 1)
        self.MapView = QtGui.QGraphicsView(Frame)
        self.MapView.setObjectName(_fromUtf8("MapView"))
        self.gridLayout.addWidget(self.MapView, 0, 1, 1, 4)
        self.GeoToggle = QtGui.QCheckBox(Frame)
        self.GeoToggle.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable geographical features", None, QtGui.QApplication.UnicodeUTF8))
        self.GeoToggle.setText(QtGui.QApplication.translate("MainWindow", "Geographical", None, QtGui.QApplication.UnicodeUTF8))
        self.GeoToggle.setObjectName(_fromUtf8("GeoToggle"))
        self.gridLayout.addWidget(self.GeoToggle, 1, 1, 1, 2)
        self.ManMadeToggle = QtGui.QCheckBox(Frame)
        self.ManMadeToggle.setToolTip(QtGui.QApplication.translate("MainWindow", "Show man-made features", None, QtGui.QApplication.UnicodeUTF8))
        self.ManMadeToggle.setText(QtGui.QApplication.translate("MainWindow", "Man-Made", None, QtGui.QApplication.UnicodeUTF8))
        self.ManMadeToggle.setObjectName(_fromUtf8("ManMadeToggle"))
        self.gridLayout.addWidget(self.ManMadeToggle, 1, 3, 1, 1)
        self.EconToggle = QtGui.QCheckBox(Frame)
        self.EconToggle.setToolTip(QtGui.QApplication.translate("MainWindow", "Show economic features", None, QtGui.QApplication.UnicodeUTF8))
        self.EconToggle.setText(QtGui.QApplication.translate("MainWindow", "Economic", None, QtGui.QApplication.UnicodeUTF8))
        self.EconToggle.setObjectName(_fromUtf8("EconToggle"))
        self.gridLayout.addWidget(self.EconToggle, 1, 4, 1, 1)
        self.ClueView = QtGui.QGraphicsView(Frame)
        self.ClueView.setObjectName(_fromUtf8("ClueView"))
        self.gridLayout.addWidget(self.ClueView, 2, 0, 2, 1)
        self.SearchButton = QtGui.QPushButton(Frame)
        self.SearchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.SearchButton.setObjectName(_fromUtf8("SearchButton"))
        self.gridLayout.addWidget(self.SearchButton, 2, 1, 1, 1)
        self.ActionsView = QtGui.QTextBrowser(Frame)
        self.ActionsView.setObjectName(_fromUtf8("ActionsView"))
        self.gridLayout.addWidget(self.ActionsView, 2, 2, 2, 3)
        self.DigButton = QtGui.QPushButton(Frame)
        self.DigButton.setText(QtGui.QApplication.translate("MainWindow", "Dig", None, QtGui.QApplication.UnicodeUTF8))
        self.DigButton.setObjectName(_fromUtf8("DigButton"))
        self.gridLayout.addWidget(self.DigButton, 3, 1, 1, 1)
        
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        
    def retranslateUi(self, Frame):
        pass
        

class Ui_Menu(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(615, 463)
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        Frame.setFrameShape(QtGui.QFrame.NoFrame)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.NewGame = QtGui.QPushButton(Frame)
        self.NewGame.setGeometry(QtCore.QRect(180, 50, 231, 61))
        self.NewGame.setText(QtGui.QApplication.translate("Frame", "New Game", None, QtGui.QApplication.UnicodeUTF8))
        self.NewGame.setObjectName(_fromUtf8("NewGame"))
        self.LoadGame = QtGui.QPushButton(Frame)
        self.LoadGame.setGeometry(QtCore.QRect(180, 150, 231, 61))
        self.LoadGame.setText(QtGui.QApplication.translate("Frame", "Load Game", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadGame.setObjectName(_fromUtf8("LoadGame"))
        self.SaveGame = QtGui.QPushButton(Frame)
        self.SaveGame.setGeometry(QtCore.QRect(180, 250, 231, 61))
        self.SaveGame.setText(QtGui.QApplication.translate("Frame", "Save Game", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveGame.setObjectName(_fromUtf8("SaveGame"))
        self.SettingsButton = QtGui.QPushButton(Frame)
        self.SettingsButton.setGeometry(QtCore.QRect(180, 350, 231, 61))
        self.SettingsButton.setText(QtGui.QApplication.translate("Frame", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.SettingsButton.setObjectName(_fromUtf8("SettingsButton"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        pass

