import pygame
from config import screen, maxFallSpeed, fallSpeedScaler, jumpPower, friction, maxMoveSpeed, minXSpeed
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
        self.frictionLogic()
        # Should be last
        self.updatePos()
    
    def move(self, amount):
        self.rect.topleft = addPos(self.rect.topleft, amount)
    
    def updateImg(self):
        (x, y) = self.velocity
        # if y < 0:
            
    
    def accel(self, amount):
        self.velocity = addPos(self.velocity, amount)
    
    def limitedAccel(self, x):
        (newX, y) = addPos(self.velocity, (x, 0))
        if newX < -minXSpeed:
            if abs(newX) > maxMoveSpeed:
                newX = -maxMoveSpeed
        if newX > minXSpeed:
            if newX > maxMoveSpeed:
                newX = maxMoveSpeed
        self.velocity = (newX, y)
        
        
    def resetFall(self):
        self.velocity = (self.velocity[0], 0)
    
    def render(self):
        self.draw(screen)
    
    def jump(self):
        (x, y) = self.velocity
        self.velocity = (x, 0)
        self.velocity = addPos(self.velocity, (0, -jumpPower))
    
    def frictionLogic(self):
        (x, y) = self.velocity
        x *= (1-friction)
        if -minXSpeed < x < minXSpeed:
            x = 0
        self.velocity = (x, y)
    
    def updatePos(self):
        self.rect.center = addPos(self.velocity, self.rect.center)
    
    def fall(self):
        if self.onGround == False:
            (x, y) = self.velocity
            if y < maxFallSpeed:
                self.velocity = addPos(self.velocity, (0, fallSpeedScaler))
            if y > maxFallSpeed:
                self.velocity = (x, maxFallSpeed)