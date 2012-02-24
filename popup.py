# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created: Fri Feb 24 01:59:23 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 150)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.iconLabel = QtGui.QLabel(self.centralwidget)
        self.iconLabel.setGeometry(QtCore.QRect(20, 20, 81, 31))
        self.iconLabel.setText(QtGui.QApplication.translate("MainWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setObjectName(_fromUtf8("iconLabel"))
        self.textLabel = QtGui.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(150, 20, 151, 31))
        self.textLabel.setText(QtGui.QApplication.translate("MainWindow", "Do you want to save?", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel.setObjectName(_fromUtf8("textLabel"))
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(280, 70, 100, 27))
        self.cancelButton.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.noButton = QtGui.QPushButton(self.centralwidget)
        self.noButton.setGeometry(QtCore.QRect(150, 70, 100, 27))
        self.noButton.setText(QtGui.QApplication.translate("MainWindow", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.noButton.setObjectName(_fromUtf8("noButton"))
        self.yesButton = QtGui.QPushButton(self.centralwidget)
        self.yesButton.setGeometry(QtCore.QRect(20, 70, 100, 27))
        self.yesButton.setText(QtGui.QApplication.translate("MainWindow", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.yesButton.setDefault(True)
        self.yesButton.setObjectName(_fromUtf8("yesButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

