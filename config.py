import pygame

# Screen
mapScreenX = 1024
mapScreenY = 512
screen = pygame.display.set_mode((mapScreenX, mapScreenY))

# Editor

mapX = 0
mapY = 0
blockW = 70 # 1024 / 64 = 16, blocks are 70x70 but changed to 60x60
blockH = 70 # 1024 / 64 = 16
placeSpeedLimit = 100 #milliseconds

# Map
saveSpeedLimit = 60
origoDotRadius = 5