import unittest

class ClassInstantiation(unittest.TestCase):
    def setUp(self):
        print "Automated Tests For Mapmaster Game:\n"
        import Globals
        import Timer
        import ViewMain 
        
    def test_InstanceClass(self):
        None

if __name__ == '__main__':
    try:
        x = unittest.main()
    except:
        None
