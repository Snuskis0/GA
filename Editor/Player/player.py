import pygame
from config import screen, maxFallSpeed, fallSpeedScaler, jumpPower, friction, maxMoveSpeed, minXSpeed, blockW, blockH, doubleJumpCDVal, playerW, playerH
from functions import addPos

class Player(pygame.sprite.Sprite):
    def __init__(self, startPos, nr):
        super().__init__()
        self.nr = nr
        self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_front.png') #72x97 default
        self.image = pygame.transform.scale(self.image, (playerW, playerH))
        self.imageLink = ""
        self.animationTimer = 0
        self.rect = self.image.get_rect(topleft = startPos)
        self.velocity = (0, 0)
        self.onGround = False
        self.doubleJump = False
        self.doubleJumpCD = doubleJumpCDVal # Counts down to 0 and lower
        self.frame = 1
        self.prevAttrib = {
            "onGround": self.onGround,
            "velocity": self.velocity,
        }
    
    def update(self, mapBlocks):
        self.doubleJumpCD -= 1
        self.animationTimer += 1
        self.fall()
        self.friction()
        self.updatePosX()
        self.collisionX(mapBlocks)
        self.updatePosY()
        self.collisionY(mapBlocks)
        self.updateOnGround(mapBlocks)
        self.animationHandler()
        self.updateAnimation()
    
    def animationHandler(self):
        # Checks different critera; Determines what frame should be used;
        
        resetBool = False
        
        if self.prevAttrib["onGround"] != self.onGround:
            self.frame = 1
            resetBool = True
        (x1, y1) = self.prevAttrib["velocity"]
        (x2, y2) = self.velocity
        
        if x1*x2 < 0: # Switched direction
            self.frame = 1
            resetBool = True
        
        self.prevAttrib = {
            "onGround": self.onGround,
            "velocity": self.velocity,
        }
        if not resetBool:
            self.frame += 1
    
    def updateAnimation(self):
        (x, y) = self.velocity
        # Walking
        if self.onGround and x == 0:
            self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_front.png')
        if self.onGround and abs(x) > 0:
            maxFrame = 11
            if maxFrame < self.frame:
                self.frame = 1            
            # Walking right
            if self.frame < 10:
                self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_walk/PNG/p{self.nr}_walk0{self.frame}.png')
            if self.frame >= 10:
                self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_walk/PNG/p{self.nr}_walk{self.frame}.png')
            
            if x < 0: # Flip if left
                self.image = pygame.transform.flip(self.image, True, False)
        # Jumping (up)
        if not self.onGround:
            self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_jump.png')
            if x < 0:
                self.image = pygame.transform.flip(self.image, True, False)
        
        self.image = pygame.transform.scale(self.image, (playerW, playerH))

    
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
                break
    
    def updateOnGround(self, blocks):
        blockFound = False
        for block in blocks:
            if self.rect.bottom == block.rect.top and ((block.rect.left < self.rect.right < block.rect.right) or (block.rect.right > self.rect.left > block.rect.left)):
                blockFound = True
                self.doubleJump = True
        self.onGround = blockFound
    
    def move(self, amount):
        self.rect.topleft = addPos(self.rect.topleft, amount)
    
    def updatePos(self):
        self.rect.center = addPos(self.rect.center, self.velocity)
    
    def jump(self):
        if self.onGround or (self.doubleJump and self.doubleJumpCD <= 0):
            (x, y) = self.velocity
            self.velocity = (x, -jumpPower)
            self.doubleJumpCD = doubleJumpCDVal 
            # If double jump
            if self.onGround == False and self.doubleJump == True:
                self.doubleJump = False
                
    
    def friction(self):
        (x, y) = self.velocity
        newX = abs(x) - friction
        if abs(x) < abs(friction):
            newX = 0
            # In case friction makes player go other way
        if x > 0:
            self.velocity = (newX, y)
        elif x < 0:
            self.velocity = (-newX, y)
        else:
            self.velocity = (0, y)
    
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
    
    def updatePosX(self):
        self.rect.centerx += self.velocity[0]

    def updatePosY(self):
        self.rect.centery += self.velocity[1]