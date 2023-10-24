import pgzrun

from ship import Ship
from asteroid import Asteroid

WIDTH = 900
HEIGHT = 500

perfectShip = Ship(WIDTH/2, HEIGHT/2)
asteroid = Asteroid(5, 5)

def on_key_down(key):
    #otacanie
    if key == keys.RIGHT:
        perfectShip.turning = -5

    if key == keys.LEFT:
        perfectShip.turning = 5

    #pohyb vpred
    if key == keys.UP:
        perfectShip.accelerate = 1

def on_key_up(key):
    #otacanie
    if key == keys.RIGHT:
        perfectShip.turning = 0

    if key == keys.LEFT:
        perfectShip.turning = 0

    #pohyb vpred
    if key == keys.UP:
        perfectShip.accelerate = 0

def update():
    perfectShip.update(WIDTH, HEIGHT)
    asteroid.update(WIDTH, HEIGHT)

def draw():
    screen.clear()
    perfectShip.draw()
    asteroid.draw()

pgzrun.go()