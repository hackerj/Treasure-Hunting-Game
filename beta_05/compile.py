"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.5 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

#Repace Dirs with a meaningfull command when I get back to my room.

from os import popen3
from time import sleep

def main():
    fi,fo,fe = popen3("C:\Python27\python compile_help.py py2exe")
    
    for i in fe.xreadlines():
        print "error> ",i
    for i in fo.readlines():
        print 'stdout> ',i,

if __name__ == '__main__':
    main()

    "C:\Python27\python compile_help.py py2exe\r"
