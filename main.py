# Imports
import pygame
import os
from config import *
from Editor.editor import *
from Editor.Ui.ui import *

# Setup
os.system('cls')
os.system('clear')
pygame.init()

clock = pygame.time.Clock()
running = True
start_time = 0
editor = Editor()
saveTicker = 0
callCounter = 0

# Main
while running:
    pygame.mouse.get_rel()
    # Event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if pygame.mouse.get_pressed()[0] and editor.getBlockAtMouse() == False and pygame.mouse.get_pos()[0] < mapScreenX:
            editor.placeObst(editor.calcGridCellCorner(pygame.mouse.get_pos()))
        
        if pygame.mouse.get_pressed()[2]:
            relPos = pygame.mouse.get_rel()
            editor.map.addPosAllBlocks(relPos)
            editor.origoDot.updatePos(relPos)
         
        if pygame.mouse.get_pressed()[1] and editor.getBlockAtMouse() != False:
            editor.getBlockAtMouse().kill()
            editor.updateBlocksAround(pygame.mouse.get_pos())
        
        if pygame.mouse.get_pressed()[0]:
            if editor.ui.checkIfHovered():
                for block in editor.ui.uiBlocks:
                    if block.checkIfHovered():
                        print(block, "clicked!")
        
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
    
            if event.key == pygame.K_1:
                editor.setCurrentBlock('Grass')
            
            if event.key == pygame.K_2:
                editor.setCurrentBlock('Box')
            
            if event.key == pygame.K_t:
                editor.ui.addPage(editor.ui.createPage(["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",]))
                print(editor.ui.pages)
            
            if event.key == pygame.K_p:
                #used for bugtesting
                callCounter += 1
                
                print(callCounter)
                print("")

            if keys[pygame.K_l] and keys[pygame.K_c] and saveTicker == 0:
                editor.map.blocks.empty()
                saveTicker = saveSpeedLimit
            
            #Save/Load 1
            if keys[pygame.K_1] and keys[pygame.K_l] and saveTicker == 0 :
                editor.load(1)
                saveTicker = saveSpeedLimit
            
            if keys[pygame.K_1] and keys[pygame.K_k] and saveTicker == 0:
                editor.save(1)
                saveTicker = saveSpeedLimit
            #Save/Load 2
            if keys[pygame.K_2] and keys[pygame.K_l] and saveTicker == 0 :
                editor.load(2)
                saveTicker = saveSpeedLimit
            
            if keys[pygame.K_2] and keys[pygame.K_k] and saveTicker == 0:
                editor.save(2)
                saveTicker = saveSpeedLimit
            #Save/Load 3
            if keys[pygame.K_3] and keys[pygame.K_l] and saveTicker == 0 :
                editor.load(3)
                saveTicker = saveSpeedLimit
            
            if keys[pygame.K_3] and keys[pygame.K_k] and saveTicker == 0:
                editor.save(3)
                saveTicker = saveSpeedLimit


    # Drawing order
    screen.fill('White')
    editor.map.render()
    editor.origoDot.render()
    editor.ui.render()
    
    pygame.draw.circle(screen, 'black', pygame.mouse.get_pos(), 3)

    
    # EndVariables
    if saveTicker > 0:
        saveTicker -= 1
    
    pygame.display.flip()
    clock.tick(60)
# End of Main
   
pygame.quit()
exit()