import pgzrun

from ship import Ship
from asteroid import Asteroid
from bullet import Bullet

WIDTH = 900
HEIGHT = 500

perfectShip = Ship(WIDTH/2, HEIGHT/2)
asteroid = Asteroid(5, 5)
bullets = []

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

    #naboje
    if key == keys.SPACE:
        b = Bullet(perfectShip.x, perfectShip.y)
        bullets.append(b)

def update():
    perfectShip.update(WIDTH, HEIGHT)
    asteroid.update(WIDTH, HEIGHT)

    for b in bullets:
        b.update()

def draw():
    screen.clear()
    perfectShip.draw()
    asteroid.draw()

    for b in bullets:
        b.draw()


pgzrun.go()