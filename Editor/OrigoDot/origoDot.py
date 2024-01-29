import pygame
from config import configData
from functions import addPos

class OrigoDot():
    def __init__(self):
        self.pos = (0,0)
    
    def render(self):
        pygame.draw.circle(configData.screen, 'black', self.pos, configData.origoDotRadius)
    
    def updatePos(self, add):
        self.pos = addPos(self.pos, add)