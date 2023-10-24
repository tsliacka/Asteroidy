from pgzhelper import *


class Bullet(Actor):
    def __init__(self, x, y, a):
        super(Bullet, self).__init__('bullet')
        self.pos = (x, y)
        self.angle = a


    def update(self):
        self.move_forward(5)