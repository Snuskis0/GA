import pygame
from config import configData

class MatCell(pygame.sprite.Sprite):
    def __init__(self, pos, mat):
        super().__init__()
        self.pos = pos
        self.mat = mat.lower()
        self.image = pygame.image.load(f"./Graphics/UI_Tiles/{self.mat}.png") 
        self.image = pygame.transform.scale(self.image, (configData.UIblockW-20, configData.UIblockH-20))
        self.rect = self.image.get_rect(center = self.pos)
    
    def checkIfHovered(self):
        if pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()):
            return True
        else:
            return False