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
        import ViewMain
        
    def test_loc(self):
        from Loc import Loc
        loc_default = Loc()

    def test_character(self):
        from Character import Character
        char = Character((1,1), "Character", "Character")
        
    def test_places(self):
        from Places import Places
        places = Places()

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

class GameTests(unittest.TestCase):

    def test_LocDefault(self):
        from Loc import Loc
        loc_default = Loc()
        self.assertEqual(loc_default.name, '')
        self.assertEqual(loc_default.objType, None)
        self.assertEqual(loc_default.x, 0)
        self.assertEqual(loc_default.y, 0)       

    def test_LocComplex(self):
        loc_complex = Loc((5,7), "city name", "city")
        self.assertEqual(loc_complex.name, "city name")
        self.assertEqual(loc_complex.objType, "city")
        self.assertEqual(loc_complex.x, 5)
        self.assertEqual(loc_complex.y, 7)
        
if __name__ == '__main__':
    try:
        x = unittest.main()
    except:
        None
