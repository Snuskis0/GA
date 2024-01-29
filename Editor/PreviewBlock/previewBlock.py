import pygame
from config import configData
from functions import howManyTrueIn

class PreviewBlock(pygame.sprite.Sprite):
    def __init__(self, pos, mat):
        super().__init__()
        self.mat = mat.lower()
        self.image = pygame.image.load(f"./Graphics/Tiles/{self.mat}.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (configData.blockW, configData.blockH))
        self.rect = self.image.get_rect(center = pos)
        self.image.set_alpha(120)

    def render(self):
        configData.screen.blit(self.image, self.rect)
    
    def update(self, pos, mat, blocksAround):
        self.updatePos(pos)
        self.updateMat(mat)
        self.updateImg(blocksAround)
    
    def updateMat(self, mat):
        self.mat = mat.lower()
    
    def updatePos(self, pos):
        self.rect.topleft = pos

    def updateImg(self, blocksAround):
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
        
        self.filename = f'{self.mat}{form}.png'                   
        #updates img of instance
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')
        self.image = pygame.transform.scale(self.image,(configData.blockW,configData.blockH)).convert_alpha()
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
        self.image.set_alpha(120)