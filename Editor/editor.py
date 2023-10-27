import pygame
import json
from Editor.Map.map import Map
from Editor.OrigoDot.origoDot import OrigoDot
from Editor.dict import stringToClassDict
from Editor.Ui.ui import Ui
from Editor.Player.player import Player
from Editor.PreviewBlock.previewBlock import PreviewBlock
from config import blockW, blockH, mapScreenX, mapScreenY, screen

class Editor():
    def __init__(self):
        self.map = Map()
        self.origoDot = OrigoDot()
        self.ui = Ui()
        self.currentBlock = "Grass"
        self.players = pygame.sprite.Group()
        self.players.add(Player((100, 100)))
        self.previewBlock = PreviewBlock((0, 0), self.currentBlock)
    
    def update(self, mousePos):
        for player in self.players:
            player.update()
        previewBlockPos = self.calcGridCellCorner(mousePos)
        self.previewBlock.update(previewBlockPos, self.currentBlock, self.checkIfBlocksAround(previewBlockPos))
    
    def getPlayer(self, nr):
        try: 
            for player in self.players.sprites():
                if player.nr == nr:
                    return player
        except:
            return False
    
    def render(self):
        self.map.render()
        self.previewBlock.render()
        self.players.draw(screen)
        self.origoDot.render()
        self.ui.render()
    
    def updateBlock(self, block, blocksAround):
        block.update(blocksAround)
    
    def save(self, saveFile):
        self.map.save(self.origoDot.pos, saveFile)
    
    def load(self, saveFile):
        path = f"Editor/saveFiles/file{saveFile}.json"
        with open(path, 'r') as file:
            print(f'Loading save file {saveFile}')
            data = json.load(file)
            self.map.blocks.empty()
            for pos, mat in data:
                self.setCurrentBlock(mat)
                self.placeBlock(pos)
            self.origoDot.pos = (0, 0)
        for block in self.map.blocks:
            self.updateBlock(block, self.checkIfBlocksAround(block.pos))
    
    def setBgSize(map, size):
        map.background = pygame.transform.scale(map.background, size)

    def setCurrentBlock(self, block):
        self.currentBlock = block
    
    def placeBlock(self, pos):
        self.map.blocks.add(stringToClassDict[self.currentBlock](pos))
        
        #updates blocks around and self
        blocksAround = self.checkIfBlocksAround(pos)
        if self.getBlockAtPos(pos) != "Air":
            self.getBlockAtPos(pos).update(blocksAround)
        self.updateBlocksAround(pos)
    
    def getBlockAtMouse(self):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        for block in self.map.blocks:
            if block.rect.collidepoint((mouseX, mouseY)):
                print("Block: ", block.rect)
                return block
        return False
    
    def calcGridCellCorner(self, pos):
        # calcs cornerPos for a given position (check whiteboard for better explaination)
        (x, y) = pos
        offsetX = self.origoDot.pos[0] % blockW
        offsetY = self.origoDot.pos[1] % blockH
        # Magic equation, whiteboard (private) explains it roughly
        return ((int((x-offsetX+blockW)/blockW)-1)*blockW+offsetX, (int((y-offsetY+blockW)/blockH)-1)*blockH+offsetY)
    
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