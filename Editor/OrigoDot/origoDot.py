import pygame
from config import origoDotRadius, screen
from functions import addPos

class OrigoDot():
    def __init__(self):
        self.pos = (0,0)
    
    def render(self):
        pygame.draw.circle(screen, 'black', self.pos, origoDotRadius)
    
    def updatePos(self, add):
        self.pos = addPos(self.pos, add)