import pygame

# Screen
editorScreenX = 400
mapScreenX = round(1920/1.2)-editorScreenX # 1024 Default
mapScreenY = round(1080/1.2) # 512 Default
editorScreenY = mapScreenY
screen = pygame.display.set_mode((mapScreenX+editorScreenX, mapScreenY))

# Editor
mapX = 0
mapY = 0
blockW = 70
blockH = 70
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
fallSpeedScaler = 0.8*blockH/70
maxFallSpeed = 50*blockH/70
jumpPower = 15*blockH/70
movementSpeed = 2*blockH/70
# Slows down this many pixels per frame
friction = 1*blockW/70
maxMoveSpeed = 8*blockW/70
minXSpeed = 1/4*(blockW/70)
doubleJumpCDVal = 15
playerW = blockW*72/100
playerH = blockH*97/100