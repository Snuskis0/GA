import pygame
import json
from Editor.Map.map import Map
from Editor.OrigoDot.origoDot import OrigoDot
from Editor.dict import stringToClassDict
from Editor.Ui.ui import Ui
from Editor.Player.player import Player
from Editor.PreviewBlock.previewBlock import PreviewBlock
from config import configData
from functions import addPos

class Editor():
    def __init__(self):
        self.map = Map()
        self.origoDot = OrigoDot()
        self.ui = Ui()
        self.currentBlock = "Grass"
        self.players = pygame.sprite.Group()
        for i in range(1):
            self.players.add(Player(((i+1)*100, 100), i+1))
        self.camFollowsPlayer()
        self.previewBlock = PreviewBlock((0, 0), self.currentBlock)
    
    def update(self, mousePos):
        for player in self.players.sprites():
            player.update(self.getCloseBlocks(player.nr))
        previewBlockPos = self.calcGridCellCorner(mousePos)
        self.previewBlock.update(previewBlockPos, self.currentBlock, self.checkIfBlocksAround(previewBlockPos))
    
    def camFollowsPlayer(self):
        # Check if player is approaching any walls, if close: Move all except players
        # By default follows player 1 to avoid camera jumps between players moving close to different walls
        player = self.getPlayer(1)
        (x, y) = player.rect.center
        
        # Checks left wall
        if x - configData.camSensX <= 0:
            self.camLogic(((x - configData.camSensX)*-1, 0))
        # Checks right wall
        elif x + configData.camSensX >= configData.mapScreenX:
            self.camLogic(((x+configData.camSensX-configData.mapScreenX)*-1, 0))
        # Checks top wall
        if y - configData.camSensY <= 0:
            self.camLogic((0, (y - configData.camSensY)*-1))
        # Checks bottom wall
        elif y + configData.camSensY >= configData.mapScreenY:
            self.camLogic((0, (y+configData.camSensY-configData.mapScreenY)*-1))
    
    def camLogic(self, pan):
        self.map.addPosAllBlocks(pan)
        self.origoDot.updatePos(pan)
        for player in self.players.sprites():
            player.move(pan)
    
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
        self.players.draw(configData.screen)
        self.origoDot.render()
        self.ui.render()
    
    def updateBlock(self, block, blocksAround):
        block.update(blocksAround)
    
    def save(self, saveFile):
        self.map.save(self.origoDot.pos, saveFile, self.players)
    
    def emptyAll(self):
        self.map.blocks.empty()
        self.players.empty()
    
    def load(self, saveFile):
        path = f"Editor/saveFiles/file{saveFile}.json"
        with open(path, 'r') as file:
            print(f'Loading save file {saveFile}')
            data = json.load(file)
            self.emptyAll()
            blocks = data["map"]
            players = data["players"]
            blockSize = data["blockSize"]
            configData.setBlockSize(blockSize[0], blockSize[1])
            configData.updateVariables()
            for block in blocks:
                self.setCurrentBlock(block["mat"])
                self.placeBlock(block["pos"])
            for player in players:
                self.players.add(Player(player["pos"], player["nr"]))
        for block in self.map.blocks:
            self.updateBlock(block, self.checkIfBlocksAround(block.pos))
        self.origoDot.pos= (0, 0)
    
    def getCloseBlocks(self, playerNum):
        foundBlocks = pygame.sprite.Group()
        playerCoords = (playerX, playerY) = self.getPlayer(playerNum).rect.center
        # Bounds to check for blocks in
        (lowerX, upperX) = (playerX - 2*configData.blockW, playerX + 2*configData.blockW)
        (lowerY, upperY) = (playerY - 2*configData.blockH, playerY + 2*configData.blockH)
        
        for block in self.map.blocks.sprites():
            if (lowerX <= block.rect.centerx <= upperX) and (lowerY <= block.rect.centery <= upperY):
                foundBlocks.add(block)
        return foundBlocks
    
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
                return block
        return False
    
    def calcGridCellCorner(self, pos):
        # calcs cornerPos for a given position (check whiteboard for better explaination)
        (x, y) = pos
        offsetX = self.origoDot.pos[0] % configData.blockW
        offsetY = self.origoDot.pos[1] % configData.blockH
        # Magic equation, whiteboard (private) explains it roughly
        return ((int((x-offsetX+configData.blockW)/configData.blockW)-1)*configData.blockW+offsetX, (int((y-offsetY+configData.blockW)/configData.blockH)-1)*configData.blockH+offsetY)
    
    def calcCornerOffset(self):
        cornerOffsetX = self.origoDot.pos[0] % configData.blockW
        cornerOffsetY = self.origoDot.pos[1] % configData.blockH
        return(cornerOffsetX, cornerOffsetY)
    
    def getBlockAtPos(self, pos):
            x = pos[0]
            y = pos[1]
            for block in self.map.blocks:
                if block.rect.collidepoint((x, y)):
                    return block
            return False
    
    def getAllPlayers(self):
        players = []
        for player in self.players.sprites():
            players.append(player)
        return players
                
    def checkIfBlockAtPos(self, pos):
        (x, y) = pos
        for block in self.map.blocks:
            if block.rect.collidepoint((pos)):
                return True
        return False

    def getBlocksOneAround(self, pos):
        # Returns block objects in order: Up, Down, Left, Right
        up = False
        down = False
        left = False
        right = False
        (x, y)= pos
        
        for block in self.map.blocks:
            if block.rect.collidepoint((x, y-configData.blockH)):
                up = block
            if block.rect.collidepoint((x, y+configData.blockH)):
                down = block
            if block.rect.collidepoint((x-configData.blockW, y)):
                left = block
            if block.rect.collidepoint((x+configData.blockW, y)):
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
            if block.rect.collidepoint((x, y-configData.blockH)):
                return block
        return False

    def getBlockOneDown(self, pos):
        x = pos[0]
        y = pos[1]
        for block in self.map.blocks:
            if block.rect.collidepoint((x, y+configData.blockH)):
                return block
        return False

    def getBlockOneLeft(self, pos):
        x = pos[0]
        y = pos[1]
        for block in self.map.blocks:
            if block.rect.collidepoint((x-configData.blockW, y)):
                return block
        return False

    def getBlockOneRight(self, pos):
        x = pos[0]
        y = pos[1]
        for block in self.map.blocks:
            if block.rect.collidepoint((x+configData.blockW, y-configData.blockH)):
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