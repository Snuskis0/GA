import pygame
from config import mapScreenX, editorScreenX, editorScreenY, screen, blockW, blockH
from functions import addPos

class MatCell(pygame.sprite.Sprite):
    def __init__(self, pos, mat):
        super().__init__()
        self.pos = pos
        self.mat = mat
        self.image = pygame.image.load("Graphics/Tiles/grass.png") 
        self.rect = self.image.get_rect(center = self.pos)
    
    def checkIfHovered(self):
        if pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()):
            return True
        else:
            return False

class Ui(pygame.sprite.Sprite):
    def __init__(self):
        self.pos = (mapScreenX, 0)
        self.barrierBottomPos = addPos(self.pos, (0, editorScreenY))
        self.backgroundRect = pygame.Rect(mapScreenX, 0, editorScreenX, editorScreenY)
        self.uiBlocks = pygame.sprite.Group()
        self.pages = []
        self.currentPage = 0
    
    def render(self):
        pygame.draw.rect(screen, (255,255,220), self.backgroundRect)
        pygame.draw.line(screen, 'Black', self.pos, self.barrierBottomPos, 1)
        if self.pages != []:
            self.pages[self.currentPage].draw(screen)
    
    def checkIfHovered(self):
        if pygame.Rect.collidepoint(self.backgroundRect, pygame.mouse.get_pos()):
            return True
        else:
            return False
    
    def createPage(self, items):
        pageContent = pygame.sprite.Group()
        counter = 0
        
        for x in range(2):
            for y in range(4):
                blockToAdd = MatCell((mapScreenX + (editorScreenX/3)*(x+1), 0 + (editorScreenY/5)*(y+1)), items[counter]) 
                pageContent.add(blockToAdd)
                counter += 1
        return pageContent
    
    def addPage(self, content):
        #content should be a pygame group
        self.pages.append(content)