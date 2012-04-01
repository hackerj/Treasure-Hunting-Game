import unittest

class ClassInstantiation(unittest.TestCase):
    "Basics tests to catch the obvious stuff."
    
    def setUp(self):
        print "Automated Tests For Mapmaster Game:\n"
        import Globals
        import Gui
        import Timer
        import Sounds
        import ViewGraphics
        import ViewMain
        
    def test_InstanceClass(self):
        from Gui import Gui
        Gui()
        
if __name__ == '__main__':
    try:
        x = unittest.main()
    except:
        None
