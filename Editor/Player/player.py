import pygame
from config import configData
from functions import addPos, reverseXInTuple

class Player(pygame.sprite.Sprite):
    def __init__(self, startPos, nr):
        super().__init__()
        self.nr = nr
        self.image = pygame.image.load(f'./Graphics/Player/p{self.nr}_front.png') #72x97 default
        self.image = pygame.transform.scale(self.image, (configData.playerW, configData.playerH))
        self.imageLink = ""
        self.animationTimer = 0
        self.rect = self.image.get_rect(topleft = startPos)
        self.velocity = (0, 0)
        self.onGround = False
        self.doubleJump = False
        self.doubleJumpCD = configData.doubleJumpCDVal # Counts down to 0 and lower
        self.frame = 1
        self.prevAttrib = {
            "onGround": self.onGround,
            "velocity": self.velocity,
        }
    
    def update(self, mapBlocks):
        self.doubleJumpCD -= 1
        self.animationTimer += 1
        self.fall(mapBlocks)
        self.friction()
        self.updatePosX()
        self.collisionX(mapBlocks)
        self.updatePosY()
        self.collisionY(mapBlocks)
        self.updateOnGround(mapBlocks)
        self.animationHandler()
        self.updateAnimation()
    
    def facingWall(self, blocks):
        (x, y) = velocity = self.velocity
        if x == 0:
            velocity = (1, y)
        # 1 and 2 for different directions
        predictedPos1 = addPos(velocity, self.rect.topleft)
        predictedPos2 = addPos(reverseXInTuple(velocity), self.rect.topleft)
        futureRect1 = pygame.rect.Rect(predictedPos1, (configData.playerW, configData.playerH))
        futureRect2 = pygame.rect.Rect(predictedPos2, (configData.playerW, configData.playerH))
        for block in blocks.sprites():
            if futureRect1.colliderect(block.rect):
                return True
            elif futureRect2.colliderect(block.rect):
                return True
        return False
    
    def wallJump(self):
        if self.doubleJumpCD <= 0:
            if self.velocity[0] < 0:
                self.velocity = (configData.maxMoveSpeed, -configData.jumpPower)
            elif self.velocity[0] > 0:
                self.velocity = (-configData.maxMoveSpeed, -configData.jumpPower)
            self.doubleJumpCD = configData.doubleJumpCDVal
            self.doubleJump = True
    
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
        
        self.image = pygame.transform.scale(self.image, (configData.playerW, configData.playerH))

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
            self.velocity = (x, -configData.jumpPower)
            self.doubleJumpCD = configData.doubleJumpCDVal 
            # If double jump
            if self.onGround == False and self.doubleJump == True:
                self.doubleJump = False
                
    
    def friction(self):
        if self.onGround:    
            (x, y) = self.velocity
            newX = abs(x) - configData.friction
            if abs(x) < abs(configData.friction):
                newX = 0
                # In case friction makes player go other way
            if x > 0:
                self.velocity = (newX, y)
            elif x < 0:
                self.velocity = (-newX, y)
            else:
                self.velocity = (0, y)
        else:
            (x, y) = self.velocity
            newX = abs(x) - configData.airResistance
            if abs(x) < abs(configData.airResistance):
                newX = 0
                # In case friction makes player go other way
            if x > 0:
                self.velocity = (newX, y)
            elif x < 0:
                self.velocity = (-newX, y)
            else:
                self.velocity = (0, y)
    
    def fall(self, blocks):
        if not self.onGround:
            self.velocity = addPos(self.velocity, (0, configData.fallSpeedScaler))
        if self.velocity[1] >= configData.maxFallSpeed:
            if not self.facingWall(blocks):
                self.velocity = (self.velocity[0], configData.maxFallSpeed)
            else:
                self.velocity = (self.velocity[0], configData.maxWallSlide)
    
    def accel(self, amount):
        self.velocity = addPos(self.velocity, amount)
    
    def limitedAccelSet(self, x):
        if x < -configData.minXSpeed:
            if abs(x) > configData.maxMoveSpeed:
                x = -configData.maxMoveSpeed
        if x > configData.minXSpeed:
            if x > configData.maxMoveSpeed:
                x = configData.maxMoveSpeed
        self.velocity = (x, self.velocity[0])
    
    def limitedAccelAdd(self, x):
        (newX, y) = addPos(self.velocity, (x, 0))
        if newX < -configData.minXSpeed:
            if abs(newX) > configData.maxMoveSpeed:
                newX = -configData.maxMoveSpeed
        if newX > configData.minXSpeed:
            if newX > configData.maxMoveSpeed:
                newX = configData.maxMoveSpeed
        self.velocity = (newX, y)
        
    def resetFall(self):
        self.velocity = (self.velocity[0], 0)
    
    def render(self):
        self.draw(configData.screen)
    
    def updatePosX(self):
        self.rect.centerx += self.velocity[0]

    def updatePosY(self):
        self.rect.centery += self.velocity[1]