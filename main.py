# Imports
import pygame
import random
import os

# Setup
pygame.init()
running = True

# Main
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                        
pygame.quit()
exit()