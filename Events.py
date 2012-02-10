# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.1 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

def movementEvent(data, event):
    key = event.key()
	
    if key == QtCore.Qt.Key_W:
		data.character.translate(0,-1) #Forward
        
    elif key == QtCore.Qt.Key_S:
        data.character.translate(0,1) #Backward
	
    elif key == QtCore.Qt.Key_A:
        print 'Left'
    elif key == QtCore.Qt.Key_D:
        print 'Right'
    else:
        print 'You pressed', event.text()

	data.view.PersonView.centerOn(data.character);
        
        
