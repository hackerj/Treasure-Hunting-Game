"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.5 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from os import popen3

def main():
    # FIXME only support for windows right now.
    
    testErrFiles = open("test.err","w")
    fi,fo,fe = popen3("C:\Python27\python AutomatedTests.py")
    for i in fe.readlines():
        testErrFiles.write(i)
    testErrFiles.close()
        
if __name__ == '__main__':
    main()
