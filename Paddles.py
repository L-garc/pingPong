'''
Paddles class for the pong game

Each player has a paddle they get to control
Computer vs player
or
player vs player
'''
import pygame

class paddle:
    def __init__(self, color, xpos, ypos, w, h):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.w = w
        self.h = h
        self.rect = pygame.Rect(xpos, ypos, w, h)

    def move(self, yVel):
        self.rect = self.rect.move(0, yVel)
        self.ypos = self.rect.y

    def ai_move(self, pingPong):
        if (self.ypos < pingPong.ypos - pingPong.radius) and (self.ypos + self.h > pingPong.ypos + pingPong.radius):
            return 0
        elif self.ypos > pingPong.ypos - pingPong.radius:
            return -300
        elif self.ypos + self.h < pingPong.ypos + pingPong.radius:
            return 300
        else:
            return 0
    
    def setPos(self, new_y):
        self.rect = pygame.Rect(self.xpos, new_y, self.w, self.h)
        self.ypos = self.rect.y

    def draw(self, ds):
        pygame.draw.rect(ds, self.color, self.rect)
