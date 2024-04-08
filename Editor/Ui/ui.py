import pygame
from config import configData
from functions import addPos
from Editor.Ui.MatCell.matCell import MatCell
from Editor.Ui.pageSelector.pageSelector import PageSelector

class Ui(pygame.sprite.Sprite):
    def __init__(self):
        self.pos = (configData.mapScreenX, 0)
        self.barrierBottomPos = addPos(self.pos, (0, configData.editorScreenY))
        self.backgroundRect = pygame.Rect(configData.mapScreenX, 0, configData.editorScreenX, configData.editorScreenY)
        self.pages = []
        self.currentPage = 0
        # Main blocks (page 1)
        pageContent = []
        for blockType in configData.mainBlockLibrary:
            pageContent.append(blockType)
        self.pages.append(self.createPage(pageContent))
        # Flagpoles (page 2)
        pageContent = []
        for flag in configData.flagpoleLibrary:
            pageContent.append(flag)
        self.pages.append(self.createPage(pageContent))
        self.pageSelectors = pygame.sprite.Group()
        self.addPageSelectors()
    
    def switchToPage(self, page):
        self.currentPage = page
    
    def render(self):
        pygame.draw.rect(configData.screen, (255,255,220), self.backgroundRect)
        pygame.draw.line(configData.screen, 'Black', self.pos, self.barrierBottomPos, 1)
        self.pageSelectors.draw(configData.screen)
        if self.pages != []:
            self.pages[self.currentPage].draw(configData.screen)
    
    def addPageSelectors(self):
        for i in range(5):
            self.pageSelectors.add(PageSelector((configData.mapScreenX+50+70*i, configData.editorScreenY-50), (i)))
    
    def checkIfHovered(self):
        if pygame.Rect.collidepoint(self.backgroundRect, pygame.mouse.get_pos()):
            return True
        else:
            return False
    
    def createPage(self, items):
        pageContent = pygame.sprite.Group()
        counter = 0
        # second page is not a group somehow???? (list)
        # try:
        for x in range(configData.blockSelectorXAmount):
            for y in range(configData.blockSelectorYAmount):
                xPos = configData.mapScreenX + configData.editorScreenX/(configData.blockSelectorXAmount+1)*(x+1)
                yPos = 0 + configData.editorScreenY - ((y+1)*configData.blockSelectorYAmount*30)-30
                try:
                    items[counter]
                except IndexError:
                    # Item does not exist
                    pass
                else:
                    # Item exists
                    blockToAdd = MatCell((xPos, yPos), items[counter])
                    pageContent.add(blockToAdd)
                counter += 1
        return pageContent
        # except:
        #         print("Too many blocktypes to display")
        #         return self.createPage(configData.standardUiPageOne)
    
    def addPage(self, content):
        # Content should be a pygame group
        self.pages.append(content)