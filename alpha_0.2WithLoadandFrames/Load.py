from os.path import *
from Loc import Loc


def loadData(data,filename = "load.txt"):
    """ load Data from file and check for existences
    """
    
    for i in xrange(-2,2):
        for j in xrange(-2,2):
            addObj(data,['None','bg',i*1024,j*1024,"grasstexture2", "None", "None"])  #Should replace magic value.
    if (not filename):
        print "File doesnt exist!"
        return
        
    filedata = open(filename)
    n = 0
    nextLine = filedata.readline()
    while (nextLine):
        obj = nextLine.split()
        
        if (isValidInput(data,obj)):
            objCommand = obj[0]
            
            if (objCommand == "addLoc"):
                addObj(data,obj)
            if (objCommand == "addClue"):
                addClue(data,obj)
        else:
            print "Line ", n, " is invalid!"
        nextLine = filedata.readline()
        n+=1  
         
    filedata.close()
    
def addObj(data, obj, pos= None, pViewImag =None, 
           mViewImag = None, itemName = None):
    """Add objects to the map"""
    scale = (-390/2/data.mapScale,-500/2/data.mapScale)
     
    objType = obj[1]
    posx = obj[2]
    posy = obj[3]
    
    if (objType == "tree"):
        pViewImag = normpath("images/Forest3.png")
        mViewImag = normpath("images/tree.png")
     
    if ( obj[4] != "None"): # person view image exists?
        pViewImag = obj[4]
        pViewImag = normpath("images/"+pViewImag+".png")
    if ( obj[5] != "None" ): # map image exists?
        mViewImag = obj[5]
        mViewImag = normpath("images/"+mViewImag+".png")
        
    if (posx != "None" and posy != "None"):
        pos = (int(posx), int(posy))
        
    if (objType == 'overlay' or objType == 'bg' and pos == None):
        pos = scale
    
    if (obj[6]!= "None"): # check whether item name exists
        itemName = obj[6]
        
    print ".. ", objType, " pos is ", pos
    locObj = Loc(pos,objType,pViewImag, mViewImag, itemName )
    
    if objType == 'char':
        data.character = locObj
    else:
        data.places.append(locObj)
    
    if objType == 'landmark' and itemName:
        data.landmarks[itemName] = locObj
        
    if objType == 'overlay' and itemName:
        data.overlays[itemName] = locObj
        
    return
    
    
def isValidInput(data,obj):
    """Check to see whether input is valid"""
    commands = {"addLoc", "addClue"}
    types = {"char", "bg","tree", "overlay", "landmark"} #obj types, for debugging
    mViews = {"None", "colorOverlay", "latLongOverlay", "legendOverlay", "city", "capital", "circle", "mapBackground"}
    pViews = {"None", "city2", "circle"}
    if (len(obj) == 7 and obj[0] in commands):
        objType = obj[1]
        posx = obj[2]
        posy = obj[3]
        pView = obj[4]
        mView = obj[5]
        itemName = obj[6]
        if ( posx != "None" and posy!="None"):
            try:
                int(posx) and int(posy)
            except:
                print "Invalid position input"
                return False
            
        if (objType not in types):
            print "Invalid objType input"
            return False
        
        if (pView not in pViews):
            print "Invalid pViews input"
            return False
        if (mView not in mViews):
            print "Invalid mViews input"
            return False
        return True
      
    print "Invalid Input, length or command type doesnt match!"
    return False







   
        
