import unittest

class FileLoadTests(unittest.TestCase):
    def test_Load(self):
        import Data, Events, Game, Gui, Load, Loc, MapMaster, Save, Sounds, \
               timer, View, ViewGraphics, ViewMain, ViewPerson

class ClassInstantiation(unittest.TestCase):
    def setup(self):
        import Data, Game
        
    def test_InstanceClass(self):
        data = Data()
        game = Game()

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        None
