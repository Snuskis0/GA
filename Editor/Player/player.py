import pygame
from config import screen, maxFallSpeed, fallSpeedScaler, jumpPower
from functions import addPos

class Player(pygame.sprite.Sprite):
    def __init__(self, startPos, nr):
        super().__init__()
        self.nr = nr
        self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_front.png')
        self.rect = self.image.get_rect(topleft = startPos)
        self.velocity = (0, 0)
        self.onGround = False
    
    def update(self):
        self.fall()
        self.updatePos()
    
    def move(self, amount):
        self.rect.topleft = addPos(self.rect.topleft, amount)
    
    def render(self):
        self.draw(screen)
    
    def jump(self):
        (x, y) = self.velocity
        self.velocity = (x, 0)
        self.velocity = addPos(self.velocity, (0, -jumpPower))
    
    def updatePos(self):
        self.rect.center = addPos(self.velocity, self.rect.center)
    
    def fall(self):
        (x, y) = self.velocity
        if y < maxFallSpeed:
            self.velocity = addPos(self.velocity, (0, fallSpeedScaler))
        if self.velocity[1] > maxFallSpeed:
            self.velocity = (x, maxFallSpeed)