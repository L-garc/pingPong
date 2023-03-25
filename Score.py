'''
Score class for the pong game

Tracks the scores of each player then uses PyGame to create a surface object with text on it
that we can blit to the game window in main
'''
import pygame

class score:
    def __init__(self, fontName="Segoe UI", color="white", size=32):
        self.fontName = fontName
        self.color = color
        self.size = size

        self.gameFont = pygame.freetype.SysFont(self.fontName, self.size)

        self.score = 0

    def incrementScore(self):
        self.score += 1

    def renderScore(self):
        return self.gameFont.render( str(self.score), self.color )
