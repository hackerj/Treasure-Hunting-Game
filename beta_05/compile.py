"""
 ---------------
 Map Master Game
 ---------------
 Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
 Version: 0.5 using PyQt4.9
 Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

#Repace Dirs with a meaningfull command when I get back to my room.

from subprocess import call

def main():
    print "Be patient. It takes a few seconds to finish."
    call('C:\Python27\python compile_help.py py2exe 1> compile.out 2> compile.err', shell=True)
    
if __name__ == '__main__':
    main()
