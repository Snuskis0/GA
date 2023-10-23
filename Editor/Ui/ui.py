import pygame
from config import mapScreenX, editorScreenX, editorScreenY, screen, blockW, blockH, standardUiPageOne, blockSelectorXAmount, blockSelectorYAmount, mainBlockLibrary
from functions import addPos
from Editor.Ui.MatCell.matCell import MatCell
from Editor.Ui.pageSelector.pageSelector import PageSelector

class Ui(pygame.sprite.Sprite):
    def __init__(self):
        self.pos = (mapScreenX, 0)
        self.barrierBottomPos = addPos(self.pos, (0, editorScreenY))
        self.backgroundRect = pygame.Rect(mapScreenX, 0, editorScreenX, editorScreenY)
        self.pages = []
        self.currentPage = 0
        
        #Temporary, here until I have a working item selector
        pageContent = []
        for blockType in mainBlockLibrary:
            pageContent.append(blockType)
        self.pages.append(self.createPage(pageContent))
        self.pageSelectors = pygame.sprite.Group()
        self.addPageSelectors()
    
    def render(self):
        pygame.draw.rect(screen, (255,255,220), self.backgroundRect)
        pygame.draw.line(screen, 'Black', self.pos, self.barrierBottomPos, 1)
        self.pageSelectors.draw(screen)
        if self.pages != []:
            # print(self.pages)
            print(self.pages)
            for block in self.pages:
                print(block)
                # try:
                block.draw(screen)
                # except:
                    # print("Block not of right type")
            # self.pages[self.currentPage].draw(screen)
    
    def addPageSelectors(self):
        for i in range(5):
            self.pageSelectors.add(PageSelector((mapScreenX+50+blockW*i, editorScreenY-50), (i+1)))
    
    def checkIfHovered(self):
        if pygame.Rect.collidepoint(self.backgroundRect, pygame.mouse.get_pos()):
            return True
        else:
            return False
    
    def createPage(self, items):
        pageContent = pygame.sprite.Group()
        counter = 0
        
        try:
            for x in range(blockSelectorXAmount):
                for y in range(blockSelectorYAmount):
                    xPos = mapScreenX + editorScreenX/(blockSelectorXAmount+1)*(x+1)
                    yPos = 0 + editorScreenY - ((y+1)*blockSelectorYAmount*30)-30
                    blockToAdd = MatCell((xPos, yPos), items[counter])
                    pageContent.add(blockToAdd)
                    counter += 1
            return pageContent
        except:
                print("Too many blocktypes to display")
                return standardUiPageOne
    
    def addPage(self, content):
        #content should be a pygame group
        self.pages.append(content)