import pygame
from config import configData
from functions import howManyTrueIn

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, shouldUpdate, baseFileName):
        super().__init__()
        # All blocks look like grass, until updated
        self.filename = baseFileName
        self.shouldUpdate = shouldUpdate
        self.pos = pos
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')
        self.image = pygame.transform.scale(self.image,(configData.blockW,configData.blockH))
        self.rect = self.image.get_rect(topleft = self.pos)
    
    def update(self, blocksAround):
        if self.shouldUpdate == False:
            return None
        # Gets classname in lowercase (materials name)
        matName = self.__class__.__name__.lower()
        
        # Determined form of the block
        form = ''
        up = blocksAround[0]
        down = blocksAround[1]
        left = blocksAround[2]
        right = blocksAround[3]
        
        blocksAroundCount = howManyTrueIn(blocksAround)
        
        if blocksAroundCount == 0:
            form = ''
        if blocksAroundCount == 1:
            if right:
                form = 'Left'
            if left:
                form = 'Right'
            if up:
                form = 'Center'
            if down:
                form = 'Mid'
        if blocksAroundCount == 2: 
            if up and down:
                form = 'Center'
            if up and left:
                form = 'Center'
            if up and right:
                form = 'Center'
            if down and left:
                form = 'Mid'
            if down and right:
                form = 'Mid'
            if left and right:
                form = 'Mid'
        if blocksAroundCount == 3:
            if up and down and left:
                form = 'Center'
            if up and down and right:
                form = 'Center'
            if up and left and right:
                form = 'Center'
            if down and left and right:
                form = 'Mid'    
        if up and down and left and right:
            form = 'Center'
        
        self.filename = f'{matName}{form}.png'                   
        #updates img of instance
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')
        self.image = pygame.transform.scale(self.image,(configData.blockW,configData.blockH))
        self.rect = self.image.get_rect(topleft = self.rect.topleft)