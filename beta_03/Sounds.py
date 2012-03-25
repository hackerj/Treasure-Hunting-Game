# ---------------
# Map Master Game
# ---------------
# Authors: MI Maps Team, CS121-SoftwareDevelopment, Harvey Mudd College
# Version: 0.3 using PyQt4.9
# Wiki_url: https://www.cs.hmc.edu/trac/cs121sp2012_4/

from pygame import mixer
from os.path import normpath
from platform import system
#if system() == 'Windows':
#    print system()
#    from pygame import _view

class Sounds(object):
    """This module handle sound (sets volume and switches sound)"""
    def __init__(self, initialSlider):
        #mixer.pre_init(44100, -16, 2, 1024)
        mixer.init()
        self.menuSound = normpath("sounds/theme.mp3")
        self.gameSound = normpath("sounds/gameTheme.mp3")
        self.currSound = self.menuSound
        mixer.music.load(self.menuSound)
        mixer.music.play(-1)
        self.volumeLevel = initialSlider
        self.setVolume(self.volumeLevel)
        
    #Set volume (only works on music right now)
    def setVolume(self, slider):
        mixer.music.set_volume((float(slider))/100.0)
        self.volumeLevel = slider
        
    #Change songs (only has songs for menu and game)
    def switchSongs(self, songnum):
        mixer.music.fadeout(500)
        if songnum == 0:
            self.currSound = self.menuSound
        elif songnum == 2:
            self.currSound = self.gameSound
        else:
            self.currSound = self.menuSound
        mixer.music.load(self.currSound)
        mixer.music.play(-1)
        self.setVolume(self.volumeLevel)
        
    def stopSounds(self):
        mixer.music.stop()
