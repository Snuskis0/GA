import pygame
from config import screen, gravity
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
        self.rect.topleft = self.pos
    
    def render(self):
        self.draw(screen)
    
    def move(self, amount):
        self.pos = addPos(self.pos, amount)
    
    def applyGravity(self):
        self.pos = addPos(self.pos, (0, gravity))