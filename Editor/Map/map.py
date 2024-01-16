import pygame
import json
from functions import addPos, subPos, multiplyPos
from config import mapX, mapY, screen, mapScreenX, mapScreenY, blockW, blockH

class Map():
    def __init__(self):
        self.blocks = pygame.sprite.Group()
        self.background = pygame.image.load('Graphics/Backgrounds/bg_grasslands.png')
        self.background = pygame.transform.scale(self.background, (mapScreenX, mapScreenY))
        self.rect = self.background.get_rect(topleft = (mapX, mapY))
    
    def render(self):
        screen.blit(self.background, self.rect)
        self.blocks.draw(screen)
    
    def multiplyPosAllBlocks(self, factor):
        for block in self.blocks:
            block.rect[0] *= factor
            block.rect[1] *= factor
            block.pos = multiplyPos(block.pos, factor)
    
    def addPosAllBlocks(self, add):
        for block in self.blocks:
            block.rect[0] += add[0]
            block.rect[1] += add[1]
            block.pos = addPos(block.pos, add)
    
    # Save and load should be in editor, is in map currently for easier access
    def save(self, origoPos, saveFile):
        path = f"Editor/saveFiles/file{saveFile}.json"
        with open(path, 'w') as file:
            print(f'Saving to save file {saveFile}')
            data = [(subPos(block.rect.topleft, origoPos), block.__class__.__name__)
            for block in self.blocks]
            json.dump(data, file)