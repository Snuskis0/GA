import pygame
from config import screen, maxFallSpeed, fallSpeedScaler, jumpPower, friction, maxMoveSpeed, minXSpeed
from functions import addPos

class Player(pygame.sprite.Sprite):
    def __init__(self, startPos, nr):
        super().__init__()
        self.nr = nr
        self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_front.png') #72x97 default
        self.rect = self.image.get_rect(topleft = startPos)
        self.velocity = (0, 0)
        self.onGround = False
    
    def update(self, mapBlocks):
        self.fall()
        # Remaking update function because it fucked up before
        
        self.friction()
        self.updatePosX()
        self.collisionX(mapBlocks)
        self.updatePosY()
        self.collisionY(mapBlocks)
    
    def collisionX(self, blocks):
        (x, y) = self.velocity
        for block in blocks.sprites():
            if self.rect.colliderect(block.rect):
                if x > 0:
                    self.rect.right = block.rect.left
                if x < 0:
                    self.rect.left = block.rect.right
                self.velocity = (0, y)
    
    def collisionY(self, blocks):
        (x, y) = self.velocity
        for block in blocks.sprites():
            if self.rect.colliderect(block.rect):
                if y > 0:
                    self.rect.bottom = block.rect.top
                if y < 0:
                    self.rect.top = block.rect.bottom
                self.velocity = (x, 0)    
    
    def move(self, amount):
        self.rect.topleft = addPos(self.rect.topleft, amount)
    
    def updatePos(self):
        self.rect.center = addPos(self.rect.center, self.velocity)
    
    def jump(self):
        self.velocity[1] = jumpPower
    
    def friction(self):
        (x, y) = self.velocity
        newX = abs(x) - friction
        if x > 0:
            self.velocity = (newX, y)
        elif x < 0:
            self.velocity = (-newX, y)
    
    def fall(self):
        if not self.onGround:
            self.velocity = addPos(self.velocity, (0, fallSpeedScaler))
        if self.velocity[1] >= maxFallSpeed:
            self.velocity = (self.velocity[0], maxFallSpeed)
    
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
    
    def updatePosX(self):
        self.rect.centerx += self.velocity[0]

    def updatePosY(self):
        self.rect.centery += self.velocity[1]