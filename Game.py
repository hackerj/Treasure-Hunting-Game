# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

import sys
from Data import Data
from View.PersonView import PersonView

class game(object):
    def __init__(self):
        print 'Game has started'
        data = Data()
        data.loadDataInitial()

        app = QtGui.QApplication(sys.argv)
        p = PersonView(data)
        sys.exit(app.exec_())
