from pgzhelper import *


class Ship(Actor):
    def __init__(self, x, y):
        super(Ship, self).__init__('ship')
        self.pos = (x,y)
        self.turning = 0

    def update(self):
        #self.angle = self.angle + self.turning
        self.angle += self.turning



