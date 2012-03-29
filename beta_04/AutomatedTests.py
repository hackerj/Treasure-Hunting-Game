import unittest

class ClassInstantiation(unittest.TestCase):
    def setUp(self):
        print "Automated Tests For Mapmaster Game:\n"
        import Data, Events, Game, Gui, Load, Loc, MapMaster, Save, Sounds, \
           timer, View, ViewGraphics, ViewMain, ViewPerson
        
    def test_InstanceClass(self):
        None

if __name__ == '__main__':
    try:
        x = unittest.main()
    except:
        print "\n-------------------------------------------------------------"\
          "---------\n\n"\
          "Code Is Broken and won't run at all.\n"\
          "Do not commit unless absolutly nessasary"\
          "\n-------------------------------------------------------------"\
          "---------\n\n"
