# Imports
import pygame
from config import *
import os
import json
from enum import Enum
import copy

class Editor():
    def __init__(self, map):
        self.map = map
    def setBgSize(map, size):
        map.background = pygame.transform.scale(map.background, size)
    
    def placeObst(obst, pos):
        if obst == 'Box':
            map.blocks.add(Box(pos))
        if obst == 'Grass':
            map.blocks.add(Grass(pos))
        #updates blocks around and self
        if getBlockAtPos(pos) != "Air":
            getBlockAtPos(pos).update()
        updateBlocksAround(pos)
    
class OrigoDot():
    def __init__(self):
        self.pos = (0,0)
    
    def render(self):
        pygame.draw.circle(screen, 'Black', self.pos, origoDotRadius)
    
    def updatePos(self, add):
        self.pos = addPos(self.pos, add)
    
      
class Map():
    def __init__(self):
        self.blocks = pygame.sprite.Group()
        self.background = pygame.image.load('Graphics/Backgrounds/bg_grasslands.png')
        self.rect = self.background.get_rect(topleft = (mapX, mapY))
    
    def render(self):
        screen.blit(self.background, self.rect)
        map.blocks.draw(screen)
    
    def addPosAllBlocks(self, add):
        for block in self.blocks:
            block.rect[0] += add[0]
            block.rect[1] += add[1]
    
    # Save and load should be in editor, is in map currently for easier access
    def save(self):
        origoX = origoDot.pos[0]
        origoY = origoDot.pos[1]
        with open('save_game.json', 'w') as file:
            print('Saving')
            data = [(addPos(block.rect.topleft, (-origoX, -origoY)), block.__class__.__name__)
            for block in self.blocks]
            json.dump(data, file)

    def load(self):
        with open('save_game.json', 'r') as file:
            print('Loading')
            data = json.load(file)
            self.blocks.empty()
            for pos, mat in data:
                Editor.placeObst(mat, pos)
            origoDot.pos = (0, 0)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, filename):
        super().__init__()
        self.filename = filename
        self.pos = pos
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')
        self.image = pygame.transform.scale(self.image,(blockW,blockH))
        self.rect = self.image.get_rect(topleft = self.pos)
        # self.direction = Direction.DEFAULT

class Direction(Enum):
    DEFAULT = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Box(Obstacle):
    def __init__(self, pos):
        super().__init__(pos, 'box.png')

class Grass(Obstacle):
    def __init__(self, pos):
        super().__init__(pos, 'grass.png')        

    def update(self):
        blocks = checkIfBlocksAround(self.pos)
        up = blocks[0]
        down = blocks[1]
        left = blocks[2]
        right = blocks[3]
        
        BlocksAroundCount = howManyTrueIn(blocks)
        #long, can't think of a faster / better way
        #Maybe divide material name and form into 2?
        #Looks awfull
        #add update when delete blocks too
        #Missing textures for topleft/right, might delete corners (make own graphic) if I ever feel like it
        if BlocksAroundCount == 1:
            if right:
                self.filename = 'grassLeft.png'
            if left:
                self.filename = 'grassRight.png'
            if up:
                self.filename = 'grassCenter.png'
            if down:
                self.filename = 'grassMid.png'
        if BlocksAroundCount == 2: 
            if up and down:
                self.filename = 'grassCenter.png'
            if up and left:
                self.filename = 'grassCenter.png'
            if up and right:
                self.filename = 'grassCenter.png'
            if down and left:
                self.filename = 'grassMid.png'
            if down and right:
                self.filename = 'grassMid.png'
            if left and right:
                self.filename = 'grassMid.png'
        if BlocksAroundCount == 3:
            if up and down and left:
                self.filename = 'grassCenter.png'
            if up and down and right:
                self.filename = 'grassCenter.png'
            if up and left and right:
                self.filename = 'grassCenter.png'
            if down and left and right:
                self.filename = 'grassMid.png'    
        if up and down and left and right:
            self.filename = 'grassCenter.png'   
        
        #updates img of instance
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')

# Functions
def howManyTrueIn(list):
    count = 0
    for item in list:
        if item:
            count += 1
    return count

def addPos(pos1, pos2):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    return (x1+x2,y1+y2)

def updateBlocksAround(pos):
    blocksAround = getBlocksOneAround(pos)
    for block in blocksAround:
        if block != 'Air':
            block.update()

def calcGridCellCorner(pos):
    # calcs cornerPos for a given position (check whiteboard for better explaination)
    x = pos[0]
    y = pos[1]
    return (int(x/blockW)*blockW,int(y/blockH)*blockH)

def getBlockOneUp(pos):
    x = pos[0]
    y = pos[1]
    for block in map.blocks:
        if block.rect.collidepoint((x, y-blockH)):
            return block
    return 'Air'

def getBlockOneDown(pos):
    x = pos[0]
    y = pos[1]
    for block in map.blocks:
        if block.rect.collidepoint((x, y+blockH)):
            return block
    return 'Air'

def getBlockOneLeft(pos):
    x = pos[0]
    y = pos[1]
    for block in map.blocks:
        if block.rect.collidepoint((x-blockW, y)):
            return block
    return 'Air'

def getBlockOneRight(pos):
    x = pos[0]
    y = pos[1]
    for block in map.blocks:
        if block.rect.collidepoint((x+blockW, y-blockH)):
            return block
    return 'Air'

def getBlocksOneAround(pos):
    # Returns block objects in order: Up, Down, Left, Right
    up = 'Air'
    down = 'Air'
    left = 'Air'
    right = 'Air'
    x = pos[0]
    y = pos[1]
    
    
    for block in map.blocks:
        if block.rect.collidepoint((x, y-blockH)):
            up = block
        if block.rect.collidepoint((x, y+blockH)):
            down = block
        if block.rect.collidepoint((x-blockW, y)):
            left = block
        if block.rect.collidepoint((x+blockW, y)):
            right = block
    
    return [up, down, left, right]

def getBlockAtMouse():
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    for block in map.blocks:
        if block.rect.collidepoint((mouseX, mouseY)):
            return block
    return 'Air'

def getBlockAtPos(pos):
    x = pos[0]
    y = pos[1]
    for block in map.blocks:
        if block.rect.collidepoint((x, y)):
            return block
    return 'Air'

def checkIfBlocksAround(pos):
    blocksAround = getBlocksOneAround(pos)
    
    up = False
    down = False
    left = False
    right = False
    
    if blocksAround[0] != 'Air':
        up = True
    if blocksAround[1] != 'Air':
        down = True
    if blocksAround[2] != 'Air':
        left = True
    if blocksAround[3] != 'Air':
        right = True
    
    return [up, down, left, right]
    
def checkIfSameBlocksAround(pos):        
    up = False
    down = False
    left = False
    right = False

    blocksAround = getBlocksOneAround(pos)
    posBlock = getBlockAtMouse().__class__.__name__
    if blocksAround[0].__class__.__name__ == posBlock:
        up = True
    if blocksAround[1].__class__.__name__ == posBlock:
        down = True
    if blocksAround[2].__class__.__name__ == posBlock:
        left = True
    if blocksAround[3].__class__.__name__ == posBlock:
        right = True
    
    return up, down, left, right

def checkifSameBlocksAroundMouseBlock():
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    
    up = False
    down = False
    left = False
    right = False

    blocksAround = getBlocksOneAround((mouseX, mouseY))
    mouseBlock = getBlockAtMouse().__class__.__name__
    if blocksAround[0].__class__.__name__ == mouseBlock:
        up = True
    if blocksAround[1].__class__.__name__ == mouseBlock:
        down = True
    if blocksAround[2].__class__.__name__ == mouseBlock:
        left = True
    if blocksAround[3].__class__.__name__ == mouseBlock:
        right = True
    
    return up, down, left, right

# Setup
pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
origoDot = OrigoDot()
running = True
start_time = 0
editorOrigo = (mapX, mapY)
map = Map()
editor = Editor(map)
saveTicker = 0

# Main
while running:
    pygame.mouse.get_rel()
    keys = pygame.key.get_pressed()
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0] and getBlockAtMouse() == 'Air':
            Editor.placeObst('Grass', calcGridCellCorner(pygame.mouse.get_pos()))
        
        if pygame.mouse.get_pressed()[2]:
            relPos = pygame.mouse.get_rel()
            map.addPosAllBlocks(relPos)
            origoDot.updatePos(relPos)
         
        if pygame.mouse.get_pressed()[1] and getBlockAtMouse() != 'Air':
            getBlockAtMouse().kill()
            updateBlocksAround(pygame.mouse.get_pos())
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                map.addPosAllBlocks((0,-blockH))
            
            if event.key == pygame.K_s:
                map.addPosAllBlocks((0,blockH))
            
            if event.key == pygame.K_a:
                map.addPosAllBlocks((-blockW,0))
            
            if event.key == pygame.K_d:
                map.addPosAllBlocks((blockW,0))
            
            if event.key == pygame.K_l and saveTicker == 0:
                map.load()
                saveTicker = saveSpeedLimit
            
            if event.key == pygame.K_SPACE and saveTicker == 0:
                map.save()
                saveTicker = saveSpeedLimit
    
    # Drawing order
    screen.fill('White')
    map.render()
    origoDot.render()
    
    
    # EndVariables
    if saveTicker > 0:
        saveTicker -= 1
    
    pygame.display.flip()
    clock.tick(60)
# End of Main
   
pygame.quit()
exit()