# Imports
import pygame
import os
from config import *
from Editor.editor import *

# Setup
os.system('cls')
os.system('clear')
pygame.init()

clock = pygame.time.Clock()
running = True
start_time = 0
editor = Editor()
saveTicker = 0

# Main
while running:
    pygame.mouse.get_rel()
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if pygame.mouse.get_pressed()[0] and editor.getBlockAtMouse() == False:
            # print(editor.getBlocksOneAround(pygame.mouse.get_pos()))
            editor.placeObst('Grass', editor.calcGridCellCorner(pygame.mouse.get_pos()))
        
        if pygame.mouse.get_pressed()[2]:
            relPos = pygame.mouse.get_rel()
            editor.map.addPosAllBlocks(relPos)
            editor.origoDot.updatePos(relPos)
         
        if pygame.mouse.get_pressed()[1] and editor.getBlockAtMouse() != False:
            editor.getBlockAtMouse().kill()
            editor.updateBlocksAround(pygame.mouse.get_pos())
        
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_l] and keys[pygame.K_1] and saveTicker == 0 :
                editor.load(1)
                saveTicker = saveSpeedLimit
            
            if saveTicker == 0 and keys[pygame.K_k] and keys[pygame.K_1] and saveTicker == 0 :
                editor.save(1)
                saveTicker = saveSpeedLimit
    
    # Drawing order
    screen.fill('White')
    editor.map.render()
    editor.origoDot.render()
    pygame.draw.circle(screen, 'black', pygame.mouse.get_pos(), 3)
    # pygame.draw.circle(screen, 'red', editor.calcGridCellCorner(pygame.mouse.get_pos()), 3)

    # EndVariables
    if saveTicker > 0:
        saveTicker -= 1
    
    pygame.display.flip()
    clock.tick(60)
# End of Main
   
pygame.quit()
exit()