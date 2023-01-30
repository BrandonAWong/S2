from MobileCritter import MobileCritter
from Insect import Insect


class Spider(Insect, MobileCritter):
    def __init__(self):
        Insect.__init__(self)

    def move_right(self):
        """moves this spider's position 1 unit right"""
        self.position[0] += 1
        return self.position

    def move_left(self):
        """moves this spider's position 2 units left"""
        self.position[0] -= 2
        return self.position

    def move_up(self):
        """moves this spider's position 1 unit up"""
        self.position[1] += 1
        return self.position

    def move_down(self):
        """moves this spider's position 2 units down"""
        self.position[1] -= 2
        return self.position

    def __str__(self):
        return u'\u1F577'
