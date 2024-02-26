# Imports
import pygame
import os
from Editor.editor import Editor
from functions import howManyTrueIn, addPos, reverseXInTuple
from config import configData

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
saveTicker = 0
callCounter = 0
font = pygame.font.Font(None, 36)
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
        
    # End of event loop used for multiple events
    # Start of "Once events (Only allowed to happen ONCE per loop, multiple events caused the below code to run multiple times in some instances since no event.type is specified)"  
    
    if keyStates.get(pygame.K_DELETE, False):
        if configData.gameStateSwitchSpeedCounter <= 0:
            if configData.gameState == "playing":
                configData.gameState = "editing"
                configData.gameStateSwitchSpeedCounter = configData.gameStateSwitchSpeed
            elif configData.gameState == "editing":
                configData.gameState = "playing"
                configData.gameStateSwitchSpeedCounter = configData.gameStateSwitchSpeed
    
    editingText = font.render(f'{configData.gameState}', True, (0, 0, 0))
    # Start of playing
    if configData.gameState == "playing":
        if keyStates.get(pygame.K_r, False):
            editor.getPlayer(1).rect.center = pygame.mouse.get_pos()
            editor.getPlayer(1).velocity = (0,0)
        
        if editor.getPlayer(1).onGround:
            if keyStates.get(pygame.K_d, False):
                editor.getPlayer(1).limitedAccelAdd(configData.movementSpeed)
            if keyStates.get(pygame.K_a, False):
                editor.getPlayer(1).limitedAccelAdd(-configData.movementSpeed)
        else:
            if keyStates.get(pygame.K_d, False):
                editor.getPlayer(1).limitedAccelAdd(configData.airStrafeSpeed)
                # print("strafing right")
            elif keyStates.get(pygame.K_a, False):
                editor.getPlayer(1).limitedAccelAdd(-configData.airStrafeSpeed)
                # print("strafing left")

        if not editor.getPlayer(1).facingWall(editor.getCloseBlocks(1)):
            if (keyStates.get(pygame.K_w, False) or keyStates.get(pygame.K_SPACE, False)):
                editor.getPlayer(1).jump()
        else:
            if (keyStates.get(pygame.K_w, False) or keyStates.get(pygame.K_SPACE, False)):
                editor.getPlayer(1).wallJump()
        editor.camFollowsPlayer()
        
        editor.updateAll(mousePos)
        if editor.detectWin():
            print("You won!")
            running = False
    # End of playing

    
    # Start of editing
    if configData.gameState == "editing":
        if keyStates.get(pygame.K_r, False):
            editor.getPlayer(1).rect.center = pygame.mouse.get_pos()
            editor.getPlayer(1).velocity = (0,0)

        if saveTicker == 0:
            if keyStates.get(pygame.K_l, False):
                if keyStates.get(pygame.K_1, False):
                    editor.load(1)
                    saveTicker = configData.saveSpeedLimit
                if keyStates.get(pygame.K_2, False):
                    editor.load(2)
                    saveTicker = configData.saveSpeedLimit
                if keyStates.get(pygame.K_3, False):
                    editor.load(3)
                    saveTicker = configData.saveSpeedLimit
            if keyStates.get(pygame.K_k, False):
                if keyStates.get(pygame.K_1, False):
                    editor.save(1)
                    saveTicker = configData.saveSpeedLimit
                if keyStates.get(pygame.K_2, False):
                    editor.save(2)
                    saveTicker = configData.saveSpeedLimit
                if keyStates.get(pygame.K_3, False):
                    editor.save(3)
                    saveTicker = configData.saveSpeedLimit
            if keyStates.get(pygame.K_c, False) and keyStates.get(pygame.K_LCTRL, False):
                editor.map.blocks.empty()
        
        if howManyTrueIn(pygame.mouse.get_pressed()) > 0: # If mouse is pressed at all
            if pygame.mouse.get_pressed()[0] and editor.getBlockAtPos(editor.calcGridCellCorner(mousePos)) == False and mousePos[0] < configData.mapScreenX:
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
                    for page in editor.ui.pageSelectors.sprites():
                        if page.checkIfHovered():
                            editor.ui.currentPage = page.id
        editor.updateEditor(mousePos)
    # End of editing

    # Events
    
    if configData.showFPS:
        print(int(clock.get_fps()))
    
    # Drawing order
    editor.render()
    configData.screen.blit(editingText, (configData.gameStateTextCoords))
    pygame.draw.circle(configData.screen, 'black', mousePos, 3)

    # EndVariables
    
    if saveTicker > 0:
        saveTicker -= 1
    configData.gameStateSwitchSpeedCounter -= 1
    pygame.display.flip()
    clock.tick(60)
# End of Main
   
pygame.quit()
exit()