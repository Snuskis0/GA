# Imports
import pygame
import os
from config import mapScreenX, standardUiPageOne, saveSpeedLimit, screen, blockW, blockH, movementSpeed, maxMoveSpeed
from Editor.editor import Editor
from functions import howManyTrueIn

# This is the working version (Home PC)

# Setup
os.system('cls')
os.system('clear')
pygame.init()

clock = pygame.time.Clock()
running = True
start_time = 0
editor = Editor()
player1 = editor.getPlayer(1)
saveTicker = 0
callCounter = 0

# Main
while running:
    pygame.mouse.get_rel()
    mousePos = pygame.mouse.get_pos()
    # Event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Key events
        keys = pygame.key.get_pressed()
        # Continous
        if keys[pygame.K_r]:
            player1.rect.center = pygame.mouse.get_pos()
            player1.velocity = (0,0)
        
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and player1.onGround:
            callCounter += 1
            # print(callCounter)
            player1.jump()
        
        # if keys[pygame.K_d] and player1.velocity[0] <= maxMoveSpeed:
        #     player1.limitedAccel(movementSpeed)
        
        # if keys[pygame.K_d] and player1.velocity[0] >= -maxMoveSpeed:
        #     player1.limitedAccel(-movementSpeed)

        # Single
        if event.type == pygame.KEYDOWN:
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
    
    # End of event loop used for multiple events
    # Start of "Once events (Only allowed to happen ONCE per loop, multiple events caused the below code to run multiple times in some instances since no event.type is specified)"  
    
    # Mouse events
    if howManyTrueIn(pygame.mouse.get_pressed()) > 0: # If mouse is pressed at all
        if pygame.mouse.get_pressed()[0] and editor.getBlockAtPos(editor.calcGridCellCorner(mousePos)) == False and mousePos[0] < mapScreenX:
            editor.placeBlock(editor.calcGridCellCorner(mousePos))
      
        if pygame.mouse.get_pressed()[2]:
            relPos = pygame.mouse.get_rel()
            editor.map.addPosAllBlocks(relPos)
            editor.origoDot.updatePos(relPos)
            for player in editor.players.sprites():
                player.move(relPos)
                            
        if pygame.mouse.get_pressed()[1] and editor.getBlockAtMouse() != False:
            editor.getBlockAtMouse().kill()
            editor.updateBlocksAround(mousePos)
           
        if pygame.mouse.get_pressed()[0]:
            if editor.ui.checkIfHovered():
                for block in editor.ui.pages[editor.ui.currentPage]:
                    if block.checkIfHovered():
                        editor.setCurrentBlock(block.mat)
        
    
    # Events
    print("before: ", player1.velocity, player1.rect.center)
    editor.update(mousePos)
    print("after: ", player1.velocity, player1.rect.center)
    
    # Drawing order
    editor.render()
    pygame.draw.circle(screen, 'black', mousePos, 3)

    # EndVariables
    
    if saveTicker > 0:
        saveTicker -= 1
    
    pygame.display.flip()
    clock.tick(60)
# End of Main
   
pygame.quit()
exit()