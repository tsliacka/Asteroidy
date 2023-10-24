from pgzhelper import *


class Ship(Actor):
    def __init__(self, x, y):
        super(Ship, self).__init__('ship')
        self.pos = (x,y)

