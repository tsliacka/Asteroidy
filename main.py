import pgzrun

from ship import Ship

WIDTH = 900
HEIGHT = 500

perfectShip = Ship(WIDTH/2, HEIGHT/2)


def draw():
    perfectShip.draw()

pgzrun.go()