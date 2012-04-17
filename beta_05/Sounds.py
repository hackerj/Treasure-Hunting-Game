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
        mixer.pre_init(44100, -16, 2, 1024)
        mixer.init()
        
        self.menuSound = normpath("sounds/theme.mp3")
        self.gameSound = normpath("sounds/gameTheme.mp3")

        self.successSound = mixer.Sound(normpath("sounds/success.wav"))
        self.failureSound = mixer.Sound(normpath("sounds/failure.wav"))

        self.currSound = self.menuSound

        
        self.volumeLevel = volume
        self.setVolume(self.volumeLevel)
        #self.setVolume(0)

        
        mixer.music.load(self.menuSound)

        
    def setVolume(self, slider):
        """Set volume (only works on music right now)"""
        mixer.music.set_volume((float(slider))/100.0)
        self.volumeLevel = slider
        
    def switchSongs(self, songNum):
        """Change songs (only has songs for menu and game)"""
        
        if songNum == 0:
            newSound = self.menuSound
        elif songNum == 2:
            newSound = self.gameSound
        else:
            newSound = self.menuSound

        if self.currSound != newSound:
            mixer.music.fadeout(500)
            self.currSound = newSound
            self.playCurrMusic()
            
    def playCurrMusic(self):
        """Allow current music to be played"""
        mixer.music.load(self.currSound)
        mixer.music.play(-1)
        self.setVolume(self.volumeLevel)

    def playSound(self, soundName):
        """PLay different songs according to whether 
           player successfully find clues
        """
        if soundName == "success":
            self.successSound.play()
        elif soundName == "failure":
            self.failureSound.play()
        
