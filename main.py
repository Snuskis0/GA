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
        self.rect = self.image.get_rect(center = self.pos)
    
    def render(self):
        screen.blit(self.image, self.rect)
        
class Box(Obstacle):
    def __init__(self, pos):
        self.image = pygame.image.load('Graphics/Tiles/box.png')
        self.image = pygame.transform.scale(self.image,(64,64))
        super().__init__(pos, self.image)
        

# Functions

def createCell(pos):
    cell_group.add(ObstacleCell(pos))

# useless code, kept for now
# def createCellFill():
#     # simple for now
#     # print(screenX/blockW, screenY/blockH)
#     for i in range(int(screenX/blockW)):
#         for j in range(int(screenY/blockH)):
#             createCell((i*blockW, j*blockH))

def placeObst(obst, pos):
    if obst == 'box':
        obst_list.add(Box(pos))

def calcGridCellCorner(pos):
    # calcs cornerPos for a given position (check whiteboard for better explaination)
    x = pos[0]
    y = pos[1]
    return (int(x/blockW)*blockW,int(y/blockH)*blockH)
    

# Setup
pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True
start_time = 0
editorOrigo = (editorX, editorY)
editor = Editor(editorOrigo)

cell_group = pygame.sprite.Group()
obst_list = pygame.sprite.Group()

# Main
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - start_time > placeSpeedLimit:
            placeObst('box', pygame.mouse.get_pos())
            start_time = pygame.time.get_ticks()    
        
            
    # Drawing order
    screen.fill('White')
    editor.render()

    editor.showGrid()
    obst_list.draw(screen)
    cell_group.draw(screen)
    
    pygame.draw.circle(screen,'Red',pygame.mouse.get_pos(),5)
    pygame.draw.circle(screen,'Blue',calcGridCellCorner(pygame.mouse.get_pos()),3)
    print(calcGridCellCorner(pygame.mouse.get_pos()))
    
    pygame.display.flip()
    clock.tick(60)
# End of Main
   
pygame.quit()
exit()