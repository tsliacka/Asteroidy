import pgzrun

from ship import Ship

WIDTH = 900
HEIGHT = 500

perfectShip = Ship(WIDTH/2, HEIGHT/2)

def on_key_down(key):
    #otacanie
    if key == keys.RIGHT:
        perfectShip.turning = -5

def on_key_up(key):
    #otacanie
    if key == keys.RIGHT:
        perfectShip.turning = 0

def update():
    perfectShip.update()

def draw():
    screen.clear()
    perfectShip.draw()

pgzrun.go()