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
            
    
    

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()
        

# Functions



# Setup
pygame.init()
screen = pygame.display.set_mode((screenX, screenY))
running = True

editorOrigo = (editorX, editorY)
editor = Editor(editorOrigo)

# Main
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        
            
    
    screen.fill('White')
    editor.render()
    if pygame.mouse.get_pressed()[0]:
        editor.showGrid()
    
    pygame.draw.circle(screen,'Red',pygame.mouse.get_pos(),5)
    
    
    pygame.display.flip()
# End of Main
   
pygame.quit()
exit()