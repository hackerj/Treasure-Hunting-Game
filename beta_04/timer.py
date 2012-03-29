

from QtCore import QTimer, QTime

class GameTimers(object):

    def __init__(self):
        # Time objects measure how long it's been since the time object was
        # started
        self.TimeObjectList = []

        # Time
        self.TimerObjectList = []
        
