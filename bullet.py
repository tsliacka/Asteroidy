from pgzhelper import *


class Bullet(Actor):
    def __init__(self, x, y):
        super(Bullet, self).__init__('bullet')
        self.pos = (x, y)


    def update(self):
        self.move_forward(5)