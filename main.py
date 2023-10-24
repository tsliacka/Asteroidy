import pgzrun
import pygame
import random

from ship import Ship
from asteroid import Asteroid
from bullet import Bullet

WIDTH = 900
HEIGHT = 500
TITLE = 'Asteroidky'

perfectShip = Ship(WIDTH/2, HEIGHT/2)
asteroids = []
bullets = []
img = pygame.image.load('images/space.png')

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
        b = Bullet(perfectShip.x, perfectShip.y, perfectShip.angle)
        bullets.append(b)

def update():
    perfectShip.update(WIDTH, HEIGHT)

    for b in bullets:
        b.update()

    for a in asteroids:
        a.update(WIDTH, HEIGHT)

    #kolizia - asteroid + lod
    for a in asteroids:
        if perfectShip.collide_pixel(a):
            sounds.asteroid_explosion.play()

    #kolizia - naboj + asteroid
    for b in bullets:
        for a in asteroids:
            if b.collide_pixel(a):
                sounds.asteroid_explosion.play()
                bullets.remove(b)
                asteroids.remove(a)

    #nahodne vytvaranie asteroidov
    if random.randint(0, 150) == 5:
        a = Asteroid(0, 0)
        asteroids.append(a)

def draw():
    screen.clear()
    screen.blit(img, (0, 0))
    perfectShip.draw()

    for b in bullets:
        b.draw()

    for a in asteroids:
        a.draw()

pgzrun.go()