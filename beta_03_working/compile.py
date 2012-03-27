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

buildLoc = normpath("../../builds/Mapmaster02")

fileList = []
fileList += [('imageformats',
             ['C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll',
              'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qmng4.dll',
              ])]

fileList += [("", ["C:\Python27\Lib\site-packages\pygame\SDL_ttf.dll",
                   "C:\Python27\Lib\site-packages\pygame\SDL_mixer.dll",
                   "C:\Python27\Lib\site-packages\pygame\libogg-0.dll"]),]

fileList += [("", ["COPYING.txt", "README","icon_medium.ico"])]

fileList += [("saves", ["saves\save1.save"])]


def addFileRoot(a , dirname, filenames):
    global fileList
    tempList = []
    for name in filenames:
        print name
        path = normpath( "./" + dirname + "/" + name)
        tempList.append(path)
    fileList += [("", tempList)]

def addFile(a , dirname, filenames):
    global fileList
    tempList = []
    for name in filenames:
        print name
        path = normpath( "./" + dirname + "/" + name)
        tempList.append(path)
    fileList += [(dirname, tempList)]

walk('images', addFile, None)
walk('sounds', addFile, None)
walk('dlls', addFileRoot, None)

includes = ["sip"]
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl','numpy'
            'Tkconstants', 'Tkinter']

#print fileList

setup(windows=[{"script" : "MapMaster.pyw",
               "icon_resources" : [(1, normpath("./icon_medium.ico"))]}],
      data_files = fileList,
      options = {"py2exe" : {"includes"   : includes,
                             "excludes"   : excludes,
                             "optimize"   : 2,
                             "compressed" : 2,
                             'bundle_files': 1, 
                             "dist_dir"   : buildLoc}})
