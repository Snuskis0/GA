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
    
    def update(self):
        pass
    
    def showGrid(self):
        x = int(pygame.display.get_window_size()[0] / blockW)
        y = int(pygame.display.get_window_size()[1] / blockH)
        
        for i in range(x):
            for j in range(y):
                pygame.draw.line(screen,'black',(0,j*blockW),(x*blockW,j*blockH))
                pygame.draw.line(screen,'black',(i*blockW,0),(i*blockW,y*blockH))
                
class ObstacleCell(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('Graphics/Tiles/dirt.png') # does not show later
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect(topleft = pos)
    
    def render(self):
        screen.blit(self.image, self.rect)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.pos = pos
        self.image = image
        self.rect = self.image.get_rect(topleft = self.pos)
    
    def render(self):
        screen.blit(self.image, self.rect)
        
class Box(Obstacle):
    def __init__(self, pos):
        self.image = pygame.image.load('Graphics/Tiles/box.png')
        self.image = pygame.transform.scale(self.image,(64,64))
        super().__init__(pos, self.image)

class Grass(Obstacle):
    def __init__(self, pos):
        self.image = pygame.image.load('Graphics/Tiles/grass.png')
        self.image = pygame.transform.scale(self.image,(blockW, blockH))
        super().__init__(pos, self.image)        

# Functions

def placeObst(obst, pos):
    if obst == 'box':
        obst_list.add(Box(pos))
    if obst == 'grass':
        obst_list.add(Grass(pos))

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
    #implement later
    pass

def getBlockAtMouse():
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    for block in obst_list:
        if block.rect.collidepoint((mouseX, mouseY)):
            return block
    return 'Air'


def checkifSameBlocksAroundMouse():
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    
    up = False
    down = False
    left = False
    right = False
    
    # is probably faster than calling "GetBlockOneXY", implement a function that runs the code in the for loop (4x faster, looks better in code)
    for block in obst_list:
        if block.rect.collidepoint((mouseX, mouseY-blockH)) and block.__class__.__name__ == getBlockAtMouse().__class__.__name__:
            up = True
        if block.rect.collidepoint((mouseX, mouseY+blockH)) and block.__class__.__name__ == getBlockAtMouse().__class__.__name__:
            down = True
        if block.rect.collidepoint((mouseX-blockW, mouseY)) and block.__class__.__name__ == getBlockAtMouse().__class__.__name__:
            left = True
        if block.rect.collidepoint((mouseX+blockW, mouseY)) and block.__class__.__name__ == getBlockAtMouse().__class__.__name__:
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
        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - start_time > placeSpeedLimit and getBlockAtMouse() == 'Air':
            placeObst('box', calcGridCellCorner(pygame.mouse.get_pos()))
            # place limit
            # start_time = pygame.time.get_ticks()    
        if pygame.mouse.get_pressed()[2] and pygame.time.get_ticks() - start_time > placeSpeedLimit and getBlockAtMouse() == 'Air':
            placeObst('grass', calcGridCellCorner(pygame.mouse.get_pos()))
            # place limit
            # start_time = pygame.time.get_ticks()    
        if pygame.mouse.get_pressed()[1]  and getBlockAtMouse() != 'Air':
            getBlockAtMouse().kill()
    print(getBlockOneUp((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])).__class__.__name__)
    # Drawing order
    screen.fill('White')
    editor.render()

    editor.showGrid()
    obst_list.draw(screen)
    
    # pygame.draw.circle(screen,'Red',pygame.mouse.get_pos(),5)

    
    pygame.display.flip()
    clock.tick(60)
# End of Main
   
pygame.quit()
exit()