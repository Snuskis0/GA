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
standardUiPageOne = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Tundra", "Cake", "Choco"]
mainBlockLibrary = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Tundra", "Cake", "Choco"]

# Map
saveSpeedLimit = 20
origoDotRadius = 5

# Ui
blockSelectorXAmount = 3
blockSelectorYAmount = 3

# Player
gravityScaler = 3
maxSpeedY = 20
speedDecline = 2
jumpPower = 20
playerSpeed = 5
lowestSpeed = 1/5
maxSpeedX = 10
