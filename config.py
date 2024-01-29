import pygame

# Class that contains ALL config settings, SOLVES SO MANY PROBLEMS!!!
class ConfigData():
    def __init__(self):
        # Screen
        self.editorScreenX = 400
        self.mapScreenX = round(1920/2)-self.editorScreenX # 1024 Default
        self.mapScreenY = round(1080/2) # 512 Default
        self.editorScreenY = self.mapScreenY
        self.screen = pygame.display.set_mode((self.mapScreenX+self.editorScreenX, self.mapScreenY))

        # Editor
        self.mapX = 0
        self.mapY = 0
        self.blockW = 40
        self.blockH = 40
        self.placeSpeedLimit = 100 #milliseconds
        self.standardUiPageOne = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Tundra", "Cake", "Choco"]
        self.mainBlockLibrary = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Tundra", "Cake", "Choco"]

        # Map
        self.saveSpeedLimit = 20
        self.origoDotRadius = 5

        # Ui
        self.blockSelectorXAmount = 3
        self.blockSelectorYAmount = 3
        self.UIblockW = 80
        self.UIblockH = 80
        self.showFPS = False
        
        # Player
        self.fallSpeedScaler = 0.8 * self.blockH / 70
        self.maxFallSpeed = 50 * self.blockH / 70
        self.jumpPower = 15 * self.blockH / 70
        self.movementSpeed = 2 * self.blockH / 70
        self.friction = 1 * self.blockW / 70
        self.maxMoveSpeed = 8 * self.blockW / 70
        self.minXSpeed = 1 / 4 * (self.blockW / 70)
        self.doubleJumpCDVal = 15
        self.playerW = self.blockW * 72 / 100
        self.playerH = self.blockH * 97 / 100
        
    def updateVariables(self):
        self.fallSpeedScaler = 0.8 * self.blockH / 70
        self.maxFallSpeed = 50 * self.blockH / 70
        self.jumpPower = 15 * self.blockH / 70
        self.movementSpeed = 2 * self.blockH / 70
        self.friction = 1 * self.blockW / 70
        self.maxMoveSpeed = 8 * self.blockW / 70
        self.minXSpeed = 1 / 4 * (self.blockW / 70)
        self.doubleJumpCDVal = 15
        self.playerW = self.blockW * 72 / 100
        self.playerH = self.blockH * 97 / 100
    
    def setBlockSize(self, w, h):
        self.blockW = w
        self.blockH = h

configData = ConfigData()