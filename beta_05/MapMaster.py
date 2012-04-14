"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.4 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from ViewMain import ViewMain
import sys

from PyQt4.QtGui import QMainWindow, QApplication, QCloseEvent

def main():
    """Create an instance of the game"""
    app = QApplication(sys.argv)
    MainWindow = ViewMain()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
