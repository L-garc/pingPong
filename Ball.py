'''
Ball class for the pong game

The ball moves around on the screen
'''

import pygame
from random import randrange

class ball:
    def __init__(self, color, xpos, ypos, radius):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.rect = pygame.Rect(xpos+radius, ypos+radius, radius, radius)
        self.dX = -300
        self.dY = -150
        
    def draw(self, ds):
        self.rect = pygame.draw.circle(ds, self.color, (self.xpos, self.ypos), self.radius)

    def rand_yVel(self):
        return randrange(-250, 250)

    def resetBall(self, ds_width, ds_height):
        self.xpos = ds_width/2 - self.radius
        self.ypos = ds_height/2 - self.radius
        self.dY = self.rand_yVel() * 2
    
    def move(self, tDelta):
        self.rect = self.rect.move(self.dX * tDelta, self.dY * tDelta)
        
        self.xpos = self.rect.centerx
        self.ypos = self.rect.centery

    def checkBounce(self, p1, p2):
        if self.rect.colliderect(p1.rect) or self.rect.colliderect(p2.rect):
            self.dX *= -1
