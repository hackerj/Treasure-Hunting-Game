import unittest

class ClassInstantiation(unittest.TestCase):
    "Basics tests to catch the obvious stuff."
    
    def test_fileLoad(self):
        #print "Automated Tests For Mapmaster Game:\n"
        import Globals
        import Graphic
        import Gui
        import Loc
        import Places
        import Sounds
        import Story
        import Timer
        import ViewGraphics
        import ViewMai
        
    def test_Game(self):
        from Game import Game
        game = Game()
        
##    def test_Gui(self):
##        from Gui import Gui
##        import sys
##        from PyQt4.QtGui import QMainWindow, QApplication, QCloseEvent
##        app = QApplication(sys.argv)
##        MainWindow = QMainWindow()
##        ui = Gui(MainWindow)
##        ui.stackedWidget.setCurrentIndex(1)
##        MainWindow.show()
##        sys.exit(app.exec_())
        

        
        
if __name__ == '__main__':
    try:
        x = unittest.main()
    except:
        None
