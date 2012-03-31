# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from PyQt4.QtGui import QMainWindow, QMessageBox
from Events import keyPress, keyRelease

class ViewMain(QMainWindow):
    def __init__(self, parent=None):
        """Initialize the abstracted class instance"""
        super(WidMain, self).__init__(parent)

        #Init Data Members
        self.gui  = None
        self.game = None
        
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
            self.data.view.guiMain.save_file_dialog()
            print "Accepting close event"
            event.accept()
