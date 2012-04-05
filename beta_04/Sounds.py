"""
---------------
Map Master Game
---------------
Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
Version: 0.4 using PyQt4.9
Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/
"""

from pygame import mixer
from os.path import normpath
from Globals import *

class Sounds(object):
    """This module handle sound (sets volume and switches sound)"""
    
    def __init__(self, volume):
        #mixer.pre_init(44100, -16, 2, 1024)
        mixer.init()
        
        self.menuSound = normpath("sounds/theme.mp3")
        self.gameSound = normpath("sounds/gameTheme.mp3")
        self.currSound = self.menuSound

        
        self.volumeLevel = volume
        self.setVolume(self.volumeLevel)

        
        mixer.music.load(self.menuSound)

        
    def setVolume(self, slider):
        """Set volume (only works on music right now)"""
        mixer.music.set_volume((float(slider))/100.0)
        self.volumeLevel = slider
        debug(self.volumeLevel)
        
    def switchSongs(self, songnum):
        """Change songs (only has songs for menu and game)"""
        
        if songnum == 0:
            newSound = self.menuSound
        elif songnum == 2:
            newSound = self.gameSound
        else:
            newSound = self.menuSound

        if self.currSound != newSound:
            mixer.music.fadeout(500)
            self.currSound = newSound
            self.playCurrMusic()
            
    def playCurrMusic(self):
        mixer.music.load(self.currSound)
        mixer.music.play(-1)
        self.setVolume(self.volumeLevel)
        
