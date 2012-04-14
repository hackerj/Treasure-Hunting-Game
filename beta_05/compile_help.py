"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.5 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

# ----------------------
# py2exe compiler script
#-----------------------
# How to Compile:
#
# This Script will compile a PythonScripInto and executable. It is been
# modified to include the nessary libraries for this map master test.
#
# Run The Following command to compile (compand line not shell)
# python compile.py py2exe
# or specifically for my machine
# C:\Python27\python compile.py py2exe

from distutils.core import setup
import py2exe
from os.path import walk, normpath

def addFileRoot(a , dirname, filenames):
    """Same as add file except it creates the files in the root"""
    global fileList
    tempList = []
    for name in filenames:
        print name
        path = normpath( "./" + dirname + "/" + name)
        tempList.append(path)
    fileList += [("", tempList)]

def addFile(a , dirname, filenames):
    """For Adding files to folder of same name in distribution directory"""
    global fileList
    tempList = []
    for name in filenames:
        print name
        path = normpath( "./" + dirname + "/" + name)
        tempList.append(path)
    fileList += [(dirname, tempList)]

# Paths we will need later

buildLoc = normpath("../../builds/Mapmaster04")
icon_path = ".\icon_medium.ico"

# List for all extra files that need to be Added
fileList = []

# Add Image DLLs
fileList += [('imageformats',
             ['C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats'
              '\qico4.dll',
              'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats'
              '\qmng4.dll',
              ])]

# Add Pygame DLLs
fileList += [("", ["C:\Python27\Lib\site-packages\pygame\SDL_ttf.dll",
                   "C:\Python27\Lib\site-packages\pygame\SDL_mixer.dll",
                   "C:\Python27\Lib\site-packages\pygame\libogg-0.dll"]),]

# Add Licence Agreement Readme and Application Icon
fileList += [("", ["COPYING.txt", "README","icon_medium.ico"])]

# Add save data
fileList += [("saves", ["saves\save1.save",
                        "saves\story.clue",
                        "saves\places.loc"])]

# Add all the images, sounds and dlls
walk('images', addFile, None)
walk('sounds', addFile, None)
walk('dlls', addFileRoot, None)

# Sip Library is needed
includes = ["sip"]

# Ignore libraries that are not needed
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl','numpy'
            'Tkconstants', 'Tkinter']



# Actually Build the Game
setup(windows=[{"script" : "MapMaster.pyw",
                "icon_resources":[(1, icon_path)]}],
      data_files = fileList,
      options = {"py2exe" : {"includes"   : includes,
                             "excludes"   : excludes,
                             "optimize"   : 2,
                             "compressed" : 2,
                             'bundle_files': 1, 
                             "dist_dir"   : buildLoc}})
