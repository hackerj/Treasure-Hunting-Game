# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/


def writeToFile(data,filename):
    """Save games to file, player is able to resume the game next time"""
    score = str(data.score)
    numClues = str(len(data.clueStack))
    charX, charY = data.character.getCenter()
    whiteSpace = "       "
    fileData = open(filename, "w")
    toWriteList = whiteSpace + str(charX) + whiteSpace + str(charY) + whiteSpace + numClues + whiteSpace + score
    fileData.write(toWriteList)     
    fileData.close()
    
        
