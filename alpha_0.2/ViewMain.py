# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.2 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4.QtGui import QMainWindow, QMessageBox
from Events import movementEvent

class WidMain(QMainWindow):
    def __init__(self, data, parent=None):
        #Initialize the abstracted class instance
        super(WidMain, self).__init__(parent)
        
        #Initialize data
        self.data = data
        
    def keyPressEvent(self, event):
        """Get keyboard events no matter what widget has focus"""
        movementEvent(self.data, event)
        
    def closeEvent(self,event):
        quit_msg = "Are you sure you want to quit?"
        reply = QMessageBox()
        reply.setWindowTitle("Quit Game")
        reply.setText(quit_msg)
        reply.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        reply.setDefaultButton(QMessageBox.Save)
        ret = reply.exec_()
        
        if ret == QMessageBox.Discard:
            self.data.view.guiMain.soundManager.stopSounds()
            print "Accepting close event"
            event.accept()
        elif ret == QMessageBox.Cancel:
            event.ignore()
        else:
            self.data.view.guiMain.save_file_dialog()
            self.data.view.guiMain.soundManager.stopSounds()
            print "Accepting close event"
            event.accept()
