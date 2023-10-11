import pygame
from config import blockW, blockH

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, filename):
        super().__init__()
        self.filename = filename
        self.pos = pos
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')
        self.image = pygame.transform.scale(self.image,(blockW,blockH))
        self.rect = self.image.get_rect(topleft = self.pos)