import pygame
from Editor.Map.Block.FullBlock.fullBlock import *
from functions import howManyTrueIn

class Grass(FullBlock):
    def __init__(self, pos):
        super().__init__(pos, 'grass.png')
    
    def update(self, blocksAround):
        up = blocksAround[0]
        down = blocksAround[1]
        left = blocksAround[2]
        right = blocksAround[3]
        
        blocksAroundCount = howManyTrueIn(blocksAround)
        
        if blocksAroundCount == 0:
            self.filename = 'grass.png'
        if blocksAroundCount == 1:
            if right:
                self.filename = 'grassLeft.png'
            if left:
                self.filename = 'grassRight.png'
            if up:
                self.filename = 'grassCenter.png'
            if down:
                self.filename = 'grassMid.png'
        if blocksAroundCount == 2: 
            if up and down:
                self.filename = 'grassCenter.png'
            if up and left:
                self.filename = 'grassCenter.png'
            if up and right:
                self.filename = 'grassCenter.png'
            if down and left:
                self.filename = 'grassMid.png'
            if down and right:
                self.filename = 'grassMid.png'
            if left and right:
                self.filename = 'grassMid.png'
        if blocksAroundCount == 3:
            if up and down and left:
                self.filename = 'grassCenter.png'
            if up and down and right:
                self.filename = 'grassCenter.png'
            if up and left and right:
                self.filename = 'grassCenter.png'
            if down and left and right:
                self.filename = 'grassMid.png'    
        if up and down and left and right:
            self.filename = 'grassCenter.png'                   
        #updates img of instance
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')