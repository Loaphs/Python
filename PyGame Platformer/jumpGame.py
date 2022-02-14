import pygame as py
from pygame.locals import *

py.init()
vect = py.math.Vector2

HEI = 450
WID = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = py.time.Clock()

displaysurface = py.display.set_mode((WID, HEI))
py.display.set_caption("GAME")

class Player(py.sprite.Sprite):
    def __init_(self):
        super().__init__()
        self.surf = py.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center = (10, 240))

class Platform(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = py.Surface((WID, 20))