import unittest

class ClassInstantiation(unittest.TestCase):
    "Basics tests to catch the obvious stuff."
    
    def test_otherImports(self):
        #print "Automated Tests For Mapmaster Game:\n"

        import Globals
        import Gui
        
        import Sounds
        import Story
        import ViewGraphics
        import ViewMain
        
        #Already Tested
        #import Character 
        #import Game
        #import Graphic
        #import Loc
        #import Places

    def test_character(self):
        from Character import Character
        char = Character((1,1), "Character", "Character")

    def test_Game(self):
        from Game import Game
        game = Game()

    def test_Graphic(self):
        from Graphic import Graphic
        graphic = Graphic(0,0,'name','type')
        
    def test_loc(self):
        from Loc import Loc
        loc_default = Loc()

    def test_places(self):
        from Places import Places
        places = Places()

    def test_sounds(self):
        from Sounds import Sounds
        sounds = Sounds(50)

    def test_story(self):
        from Story import Story
        Story(25)

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
        """Check if default locations initialize properly"""
        from Loc import Loc
        loc_default = Loc()

        self.assertEqual(loc_default.name, '')
        self.assertEqual(loc_default.objType, None)
        self.assertEqual(loc_default.x, 0)
        self.assertEqual(loc_default.y, 0)       

    def test_LocComplex(self):
        """Check if locations store information correctly"""
        from Loc import Loc
        loc_complex = Loc((5,7), "city name", "city")
        
        self.assertEqual(loc_complex.name, "city name")
        self.assertEqual(loc_complex.objType, "city")
        self.assertEqual(loc_complex.x, 5)
        self.assertEqual(loc_complex.y, 7)

    def test_Story(self):
        from Story import Story
        story = Story(25)
        
class LoadTests(unittest.TestCase):
    from Places import Places
    TYPES = {"landmark", "tree", "grass", "mapBG"}
    def test_loadLoc(self):
        """Check if locations are correctly loaded from file"""
        
        # load location check from good file
        locNames = {"mapBG", "tree2", "grass1", "grass4", "city1", "city2"}
        numObjs = 6
        placesGood = self.Places()    
        placesGood.loadLoc("tests/load1.test")
        locObjs = placesGood.locList
        self.assertEqual(len(locObjs), numObjs)
        objList = locObjs.keys()
        for eachObj in objList:
            self.assertIn(locObjs[eachObj].name, locNames)
            self.assertIsInstance(locObjs[eachObj].x, int)
            self.assertIsInstance(locObjs[eachObj].y, int)
            self.assertIn(locObjs[eachObj].objType, self.TYPES)
            
        # load location check from file that contains invalid commands,including
        # invalid objType, pos type, item names and obj command. Make sure that
        # only two objs can be loaded from error file.
        badObjs = 2 
        placesBad= self.Places()    
        placesBad.loadLoc("tests/load2.test")
        locObjs = placesBad.locList
        self.assertEqual(len(locObjs), badObjs)
        objList = locObjs.keys()
        for eachObj in objList:
            self.assertIn(locObjs[eachObj].name, locNames)
            self.assertIsInstance(locObjs[eachObj].x, int)
            self.assertIsInstance(locObjs[eachObj].y, int)
            self.assertIn(locObjs[eachObj].objType, self.TYPES)
        
        # load objs from invalid file path
        placesEmpty = self.Places()
        placesEmpty.loadLoc("tests/empty.test")
        locObjs = placesEmpty.locList
        self.assertEqual(len(locObjs),0)
        
if __name__ == '__main__':
    try:
        x = unittest.main()
    except:
        None
