import pygame
from config import screen, gravityScaler, maxGravity
from functions import addPos

class Player(pygame.sprite.Sprite):
    def __init__(self, startPos):
        super().__init__()
        self.pos = startPos
        self.nr = 1
        self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_front.png')
        self.rect = self.image.get_rect(topleft = self.pos)
        self.velocity = (0, 0)
    
    def update(self):
        self.applyGravity()
        self.updatePos()
        self.rect.topleft = self.pos
    
    def render(self):
        self.draw(screen)
    
    def move(self, amount):
        self.pos = addPos(self.pos, amount)
    
    def updatePos(self):
        self.pos = addPos(self.pos, self.velocity)
    
    def applyGravity(self):
        temp = self.velocity[0]
        if self.velocity[1] < maxGravity:
            self.velocity = addPos(self.velocity, (0, gravityScaler))
            if self.velocity[1] > maxGravity:
                self.velocity = (temp, maxGravity)