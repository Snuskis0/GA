# Imports
import pygame
import os
from config import mapScreenX, standardUiPageOne, saveSpeedLimit, screen, blockW, blockH
from Editor.editor import Editor
from functions import howManyTrueIn

# This is the working version (Home PC)

# Setup
try:
    os.system('cls')
except:
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
        
        if event.type == pygame.MOUSEWHEEL:
            # Trying to make a zoom function
            print(event.x, event.y)
        
        if howManyTrueIn(pygame.mouse.get_pressed()) > 0: # If mouse is pressed at all
            if pygame.mouse.get_pressed()[0] and editor.getBlockAtMouse() == False and pygame.mouse.get_pos()[0] < mapScreenX:
                editor.placeBlock(editor.calcGridCellCorner(pygame.mouse.get_pos()))
            
            if pygame.mouse.get_pressed()[2]:
                relPos = pygame.mouse.get_rel()
                editor.map.addPosAllBlocks(relPos)
                editor.origoDot.updatePos(relPos)
            
            if pygame.mouse.get_pressed()[1] and editor.getBlockAtMouse() != False:
                editor.getBlockAtMouse().kill()
                editor.updateBlocksAround(pygame.mouse.get_pos())
            
            if pygame.mouse.get_pressed()[0]:
                if editor.ui.checkIfHovered():
                    for block in editor.ui.pages[editor.ui.currentPage]:
                        if block.checkIfHovered():
                            editor.setCurrentBlock(block.mat)
        
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            
            if event.key == pygame.K_t:
                editor.ui.addPage(editor.ui.createPage(standardUiPageOne))
                print(editor.ui.pages)
            
            if event.key == pygame.K_p:
                #used for bugtesting
                callCounter += 1
                
                print(callCounter)
                print("")

            if keys[pygame.K_LCTRL] and keys[pygame.K_c] and saveTicker == 0:
                editor.map.blocks.empty()
                saveTicker = saveSpeedLimit
            
            # Saves
            # No saveticker currently
            if keys[pygame.K_k]:
                if keys[pygame.K_1]: 
                    editor.save(1)
                    saveTicker = saveSpeedLimit
                if keys[pygame.K_2]: 
                    editor.save(2)
                    saveTicker = saveSpeedLimit
                if keys[pygame.K_3]: 
                    editor.save(3)
                    saveTicker = saveSpeedLimit
            #Loads
            #No saveticker currently
            if keys[pygame.K_l]:
                if keys[pygame.K_1]: 
                    editor.load(1)
                    saveTicker = saveSpeedLimit
                if keys[pygame.K_2]: 
                    editor.load(2)
                    saveTicker = saveSpeedLimit
                if keys[pygame.K_3]: 
                    editor.load(3)
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