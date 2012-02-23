from distutils.core import setup
import py2exe

setup(windows=[{"script" : "MapMaster.pyw"}],
      data_files = [('imageformats',
                     ['C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qmng4.dll',
                      'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qmng4.dll'])],
      options={"py2exe" : {"includes" : ["sip"]}})

#, "PyQt4._qt"

# How to Compile:
#
# This Script will compile a PythonScripInto and executable. It is been
# modified to include the nessary libraries for this map master test.
#
# Run The Following command to compile (compand line not shell)
# python compile.py py2exe
# or specifically for my machine
# C:\Python27\python compile.py py2exe
