import pygame
import json
from functions import addPos, subPos, multiplyPos
from config import configData
from Editor.Map.FinishPole.finishPole import FinishPole

class Map():
    def __init__(self):
        self.blocks = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.background = pygame.image.load('Graphics/Backgrounds/bg_grasslands.png')
        self.background = pygame.transform.scale(self.background, (configData.mapScreenX, configData.mapScreenY))
        self.rect = self.background.get_rect(topleft = (configData.mapX, configData.mapY))
        self.finishPoles = pygame.sprite.Group()
        self.finishPoles.add(FinishPole((420, 210), "Red"))
        
    def render(self):
        configData.screen.blit(self.background, self.rect)
        self.blocks.draw(configData.screen)
        self.finishPoles.draw(configData.screen)
    
    def animate(self):
        for pole in self.finishPoles.sprites():
            pole.update()
    
    def addPosAllContent(self, add):
        self.addPosAllBlocks(add)
        for pole in self.finishPoles.sprites():
            pole.rect.center = addPos(pole.rect.center, add)
    
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
    
    def save(self, origoPos, saveFile, players):
        path = f"Editor/saveFiles/file{saveFile}.json"
        relMap = []
        for block in self.blocks.sprites():
            blockPos = subPos(block.rect.topleft, origoPos)
            relMap.append({
                "pos": blockPos,
                "mat": block.__class__.__name__
            })
        playerData = []
        for player in players.sprites():
            playerPos = subPos(player.rect.center, origoPos)
            playerData.append({
                "pos": playerPos,
                "nr": player.nr
            })
        with open(path, 'w') as file:
            print(f'Saving to save file {saveFile}')
            data = {
                "map": relMap,
                "blockSize": (configData.blockW, configData.blockH),
                "players": playerData
            }
            
            # data = [(subPos(block.rect.topleft, origoPos), block.__class__.__name__)
            # for block in self.blocks]
            json.dump(data, file)