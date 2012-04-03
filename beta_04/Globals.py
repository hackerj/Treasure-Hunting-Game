"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

#Not really global, but that is how we are going to use it.
DEBUG = True

def debug( *args ):
    if DEBUG:
        for message in args:
            print message,
        print