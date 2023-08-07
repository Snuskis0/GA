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
    
    
    pygame.display.flip()
# End of Main
   
pygame.quit()
exit()