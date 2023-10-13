import pygame
from config import blockW, blockH

class MatCell(pygame.sprite.Sprite):
    def __init__(self, pos, mat):
        super().__init__()
        self.pos = pos
        self.mat = mat
        self.image = pygame.image.load("Graphics/Tiles/grass.png") 
        self.image = pygame.transform.scale(self.image, (blockW-20, blockH-20))
        self.rect = self.image.get_rect(center = self.pos)
    
    def checkIfHovered(self):
        if pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()):
            return True
        else:
            return False