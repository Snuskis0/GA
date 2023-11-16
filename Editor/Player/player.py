import pygame
from config import screen, gravityScaler, speedDecline, lowestSpeed, maxSpeedX, maxSpeedY
from functions import addPos

class Player(pygame.sprite.Sprite):
    def __init__(self, startPos):
        super().__init__()
        self.nr = 1
        self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_front.png')
        self.rect = self.image.get_rect(topleft = startPos)
        self.onGround = False
    
    def update(self):
        pass
    
    def render(self):
        self.draw(screen)
   