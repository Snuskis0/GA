import pygame

# Screen
mapScreenX = 1024
mapScreenY = 512
editorScreenX = 400
editorScreenY = mapScreenY
screen = pygame.display.set_mode((mapScreenX+editorScreenX, mapScreenY))

# Editor
mapX = 0
mapY = 0
blockW = 70 # 1024 / 64 = 16, blocks are 70x70 but changed to 60x60
blockH = 70 # 1024 / 64 = 16
placeSpeedLimit = 100 #milliseconds
standardUiPageOne = ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",]
blockLibrary = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Box"]

# Map
saveSpeedLimit = 20
origoDotRadius = 5