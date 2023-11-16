# Imports
import pygame
import os
from config import mapScreenX, standardUiPageOne, saveSpeedLimit, screen, blockW, blockH, movementSpeed, maxMoveSpeed
from Editor.editor import Editor
from functions import howManyTrueIn, addPos

# This is the working version (Home PC)

# Setup
os.system('cls')
os.system('clear')
pygame.init()

clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
running = True
start_time = 0
editor = Editor()
player1 = editor.getPlayer(1)
saveTicker = 0
callCounter = 0
# Pygame does not handle key_states the way I want/need, therefore I will make my own.
keyStates = {}

# Main
while running:
    pygame.mouse.get_rel()
    mousePos = pygame.mouse.get_pos()
    # Event loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Adds and removes keystates to the dict whenever it should
        elif event.type == pygame.KEYDOWN:
            keyStates[event.key] = True
        elif event.type == pygame.KEYUP:
            keyStates[event.key] = False
        
        # Key events
        # Continous
        if keyStates.get(pygame.K_r, False):
            player1.rect.center = pygame.mouse.get_pos()
            player1.velocity = (0,0)
        
    # End of event loop used for multiple events
    # Start of "Once events (Only allowed to happen ONCE per loop, multiple events caused the below code to run multiple times in some instances since no event.type is specified)"  
    
    if (keyStates.get(pygame.K_w, False) or keyStates.get(pygame.K_SPACE, False)) and player1.onGround:
        player1.jump()
        
    if keyStates.get(pygame.K_d, False):
        player1.limitedAccel(movementSpeed)
        
    if keyStates.get(pygame.K_a, False):
        player1.limitedAccel(-movementSpeed)
    
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
    editor.update(mousePos)
    print(int(clock.get_fps()))
    
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