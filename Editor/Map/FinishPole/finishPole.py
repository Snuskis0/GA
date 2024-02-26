import pygame
from config import configData
from functions import addPos

class FinishPole(pygame.sprite.Sprite):
    def __init__(self, pos, colour):
        super().__init__()
        # Blue, Green, Red, Yellow valid colours
        self.colour = colour
        self.image = pygame.image.load(f"./Graphics/Items/flag{self.colour}.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.animationFrame = 1
        
    def update(self):
        self.updateImg()
        self.updateAnimationFrame()
        
    def updateImg(self):
        if self.animationFrame <= configData.flagAnimationSpeed:
            self.image = pygame.image.load(f"./Graphics/Items/flag{self.colour}.png")
        elif self.animationFrame > configData.flagAnimationSpeed:
            self.image = pygame.image.load(f"./Graphics/Items/flag{self.colour}2.png")
        
    def updateAnimationFrame(self):
        self.animationFrame += 1
        if self.animationFrame > configData.flagAnimationSpeed*2:
            self.animationFrame = 0