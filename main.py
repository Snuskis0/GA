# Imports
import pygame
from config import *
import os

os.system('cls')

# Classes
class Editor():
    def __init__(self, origin):
        self.origin = origin
        self.background = pygame.image.load('Graphics/Backgrounds/bg_grasslands.png')
        self.rect = self.background.get_rect(topleft = (editorX, editorY))
    
    def render(self):
        screen.blit(self.background, self.rect)
        
    def setBgSize(self, size):
        self.background = pygame.transform.scale(self.background, size)
    
    def showGrid(self):
        x = int(pygame.display.get_window_size()[0] / blockW)
        y = int(pygame.display.get_window_size()[1] / blockH)
        
        for i in range(x):
            for j in range(y):
                pygame.draw.line(screen,'black',(0,j*blockW),(x*blockW,j*blockH))
                pygame.draw.line(screen,'black',(i*blockW,0),(i*blockW,y*blockH))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.pos = pos
        self.image = image
        self.rect = self.image.get_rect(topleft = self.pos)
        
class Box(Obstacle):
    def __init__(self, pos):
        self.filename = 'box.png'
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')
        self.image = pygame.transform.scale(self.image,(blockW,blockH))
        super().__init__(pos, self.image)

class Grass(Obstacle):
    def __init__(self, pos):
        self.filename = 'grass.png'
        self.image = pygame.image.load(f'Graphics/Tiles/{self.filename}')
        self.image = pygame.transform.scale(self.image,(blockW, blockH))
        super().__init__(pos, self.image)        

    def update(self):
        blocks = checkIfSameBlocksAround(self.pos)
        up = blocks[0]
        down = blocks[1]
        left = blocks[2]
        right = blocks[3]
        
        sameBlocksAroundCount = howManyTrueIn(blocks)
        #long, can't think of a faster / better way
        #Maybe divide material name and form into 2?
        #Looks awfull
        #add update when delete blocks too
        #Missing textures for topleft/right, might delete corners (make own graphic) if I ever feel like it
        if sameBlocksAroundCount == 1:
            if right:
                self.filename = 'grassLeft.png'
            if left:
                self.filename = 'grassRight.png'
            if up:
                self.filename = 'grassCenter.png'
            if down:
                self.filename = 'grass.png'
        if sameBlocksAroundCount == 2: 
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
        if sameBlocksAroundCount == 3:
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

def placeObst(obst, pos):
    if obst == 'box':
        obst_list.add(Box(pos))
    if obst == 'grass':
        obst_list.add(Grass(pos))
    #updates blocks around and self
    blocksAround = getBlocksOneAround(pos)
    placedBlock = getBlockAtPos(pos)
    placedBlock.update()
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
    for block in obst_list:
        if block.rect.collidepoint((x, y-blockH)):
            return block
    return 'Air'

def getBlockOneDown(pos):
    x = pos[0]
    y = pos[1]
    for block in obst_list:
        if block.rect.collidepoint((x, y+blockH)):
            return block
    return 'Air'

def getBlockOneLeft(pos):
    x = pos[0]
    y = pos[1]
    for block in obst_list:
        if block.rect.collidepoint((x-blockW, y)):
            return block
    return 'Air'

def getBlockOneRight(pos):
    x = pos[0]
    y = pos[1]
    for block in obst_list:
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
    
    
    for block in obst_list:
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
    for block in obst_list:
        if block.rect.collidepoint((mouseX, mouseY)):
            return block
    return 'Air'

def getBlockAtPos(pos):
    x = pos[0]
    y = pos[1]
    for block in obst_list:
        if block.rect.collidepoint((x, y)):
            return block
    return 'Air'

def checkIfSameBlocksAround(pos):
    x = pos[0]
    y = pos[1]
        
    up = False
    down = False
    left = False
    right = False

    blocksAround = getBlocksOneAround((x, y))
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
running = True
start_time = 0
editorOrigo = (editorX, editorY)
editor = Editor(editorOrigo)

obst_list = pygame.sprite.Group()

# Main
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0] and getBlockAtMouse() == 'Air':
            placeObst('box', calcGridCellCorner(pygame.mouse.get_pos()))
               
        if pygame.mouse.get_pressed()[2] and getBlockAtMouse() == 'Air':
            placeObst('grass', calcGridCellCorner(pygame.mouse.get_pos()))
            
         
        if pygame.mouse.get_pressed()[1] and getBlockAtMouse() != 'Air':
            getBlockAtMouse().kill()
    
    # Drawing order
    screen.fill('White')
    editor.render()
    
    # editor.showGrid()
    obst_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
# End of Main
   
pygame.quit()
exit()