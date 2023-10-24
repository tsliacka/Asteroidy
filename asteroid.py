from pgzhelper import *


class Asteroid(Actor):
    def __init__(self, x, y):
        super(Asteroid, self).__init__('asteroid1')
        self.pos = (x, y)

    def update(self, w, h):
        self.move_forward(3)

        self.x = self.x % w
        self.y = self.y % h