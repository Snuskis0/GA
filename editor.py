import pygame
from map import *
from origoDot import *
from grass import *
#from box import *
from config import blockW, blockH, screenX, screenY

class Editor():
    def __init__(self):
        self.map = Map()
        self.origoDot = OrigoDot()
    
    def save(self):
        self.map.save(self.origoDot.pos)
    
    def load(self):
        with open('save_game.json', 'r') as file:
            print('Loading')
            data = json.load(file)
            self.map.blocks.empty()
            for pos, mat in data:
                self.placeObst(mat, pos)
            self.origoDot.pos = (0, 0)
    
    def setBgSize(map, size):
        map.background = pygame.transform.scale(map.background, size)
    
    def placeObst(self, obst, pos):
        if obst == 'Box':
            self.map.blocks.add(Box(pos))
        if obst == 'Grass':
            self.map.blocks.add(Grass(pos))
        #updates blocks around and self
        blocksAround = self.checkIfSameBlocksAround(pos)
        if self.getBlockAtPos(pos) != "Air":
            self.getBlockAtPos(pos).update(blocksAround)
        self.updateBlocksAround(pos)
    
    def showGrid(self):
        (offsetX, offsetY) = self.calcCornerOffset()
        for x in range(20):
            for y in range(10):
                pygame.draw.line(screen, 'black', (0, y*blockH+offsetY),(screenX, y*blockH+offsetY))
                pygame.draw.line(screen, 'black', (x*blockW+offsetX, 0),(x*blockW+offsetX, screenY))
    
    def getBlockAtMouse(self):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        for block in self.map.blocks:
            if block.rect.collidepoint((mouseX, mouseY)):
                return block
        return False
    
    def calcGridCellCorner(self, pos):
        # calcs cornerPos for a given position (check whiteboard for better explaination)
        (x, y) = pos
        offsetX = self.origoDot.pos[0] % blockW
        offsetY = self.origoDot.pos[1] % blockH
        # bugtesting here
        return ((int((x-offsetX)/blockW))*blockW+offsetX, int((y-offsetY)/blockH)*blockH+offsetY)
    
    def calcCornerOffset(self):
        cornerOffsetX = self.origoDot.pos[0] % blockW
        cornerOffsetY = self.origoDot.pos[1] % blockH
        return(cornerOffsetX, cornerOffsetY)
    
    def getBlockAtPos(self, pos):
            x = pos[0]
            y = pos[1]
            for block in self.map.blocks:
                if block.rect.collidepoint((x, y)):
                    return block
            return False
    
    def getBlocksOneAround(self, pos):
        # Returns block objects in order: Up, Down, Left, Right
        up = False
        down = False
        left = False
        right = False
        (x, y)= pos
        
        for block in self.map.blocks:
            if block.rect.collidepoint((x, y-blockH)):
                up = block
            if block.rect.collidepoint((x, y+blockH)):
                down = block
            if block.rect.collidepoint((x-blockW, y)):
                left = block
            if block.rect.collidepoint((x+blockW, y)):
                right = block
        
        return [up, down, left, right]
    
    def updateBlocksAround(self, pos):
        blocksAround = self.getBlocksOneAround(pos)
        for block in blocksAround:
            if block != False:
                blocksAround = self.checkIfBlocksAround(block.pos)
                block.update(blocksAround)
    
    def getBlockOneUp(self, pos):
        x = pos[0]
        y = pos[1]
        for block in self.map.blocks:
            if block.rect.collidepoint((x, y-blockH)):
                return block
        return False

    def getBlockOneDown(self, pos):
        x = pos[0]
        y = pos[1]
        for block in self.map.blocks:
            if block.rect.collidepoint((x, y+blockH)):
                return block
        return False

    def getBlockOneLeft(self, pos):
        x = pos[0]
        y = pos[1]
        for block in self.map.blocks:
            if block.rect.collidepoint((x-blockW, y)):
                return block
        return False

    def getBlockOneRight(self, pos):
        x = pos[0]
        y = pos[1]
        for block in self.map.blocks:
            if block.rect.collidepoint((x+blockW, y-blockH)):
                return block
        return False
    
    def checkIfBlocksAround(self, pos):
        blocksAround = self.getBlocksOneAround(pos)
        
        up = False
        down = False
        left = False
        right = False
        
        if blocksAround[0] != False:
            up = True
        if blocksAround[1] != False:
            down = True
        if blocksAround[2] != False:
            left = True
        if blocksAround[3] != False:
            right = True
        
        return [up, down, left, right]
    
    def checkIfSameBlocksAround(self, pos):        
        up = False
        down = False
        left = False
        right = False

        blocksAround = self.getBlocksOneAround(pos)
        posBlock = self.getBlockAtMouse().__class__.__name__
        if blocksAround[0].__class__.__name__ == posBlock:
            up = True
        if blocksAround[1].__class__.__name__ == posBlock:
            down = True
        if blocksAround[2].__class__.__name__ == posBlock:
            left = True
        if blocksAround[3].__class__.__name__ == posBlock:
            right = True
        
        return up, down, left, right
    
    def checkifSameBlocksAroundMouseBlock(self):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        
        up = False
        down = False
        left = False
        right = False

        blocksAround = self.getBlocksOneAround((mouseX, mouseY))
        mouseBlock = self.getBlockAtMouse().__class__.__name__
        if blocksAround[0].__class__.__name__ == mouseBlock:
            up = True
        if blocksAround[1].__class__.__name__ == mouseBlock:
            down = True
        if blocksAround[2].__class__.__name__ == mouseBlock:
            left = True
        if blocksAround[3].__class__.__name__ == mouseBlock:
            right = True
        
        return up, down, left, right