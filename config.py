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
blockW = 60
blockH = 60
placeSpeedLimit = 100 #milliseconds
standardUiPageOne = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Tundra", "Cake", "Choco"]
mainBlockLibrary = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Tundra", "Cake", "Choco"]

# Map
saveSpeedLimit = 20
origoDotRadius = 5

# Ui
blockSelectorXAmount = 3
blockSelectorYAmount = 3
UIblockW = 80
UIblockH = 80
showFPS = False

# Player
fallSpeedScaler = 1
maxFallSpeed = 50
jumpPower = 20
movementSpeed = 2
# Slows down this many pixels per frame
friction = 1
maxMoveSpeed = 10
minXSpeed = 1/4
