import pygame

# Class that contains ALL config settings, SOLVES SO MANY PROBLEMS!!!
class ConfigData():
    def __init__(self):
        # Globals
        self.gameState = "editing"
        self.gameStateTextCoords = (10, 20)
        self.gameStateSwitchSpeed = 30
        self.gameStateSwitchSpeedCounter = 0
        
        # Screen
        self.editorScreenX = 400
        self.mapScreenX = round(1920/1.5)-self.editorScreenX # 1024 Default
        self.mapScreenY = round(1080/1.5) # 512 Default
        self.editorScreenY = self.mapScreenY
        self.screen = pygame.display.set_mode((self.mapScreenX+self.editorScreenX, self.mapScreenY))
        self.camSens = 300
        self.camSensX = self.camSens
        self.camSensY = self.camSens / 2

        # Editor
        self.mapX = 0
        self.mapY = 0
        self.blockW = 40
        self.blockH = 40
        self.placeSpeedLimit = 100 #milliseconds
        self.standardUiPageOne = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Tundra", "Cake", "Choco"]
        self.mainBlockLibrary = ["Grass", "Dirt", "Castle", "Sand", "Snow", "Stone", "Tundra", "Cake", "Choco"]
        self.flagpoleLibrary = ["flagBlue", "flagGreen", "flagRed", "flagYellow"]

        # Map
        self.saveSpeedLimit = 20
        self.origoDotRadius = 5
        self.flagAnimationSpeed = 10

        # Ui
        self.blockSelectorXAmount = 3
        self.blockSelectorYAmount = 3
        self.UIblockW = 80
        self.UIblockH = 80
        self.showFPS = False
        
        # Player
        self.fallSpeedScaler = 0.8 * self.blockH / 70
        self.maxFallSpeed = 50 * self.blockH / 70
        self.maxWallSlide = self.maxFallSpeed * 0.1
        self.jumpPower = 15 * self.blockH / 70
        self.movementSpeed = 2 * self.blockH / 70
        self.airStrafeSpeed = self.movementSpeed *0.4 # 0.4 is lowest that "works"
        self.friction = 1 * self.blockW / 70
        self.airResistance = self.friction * 0.25
        self.maxMoveSpeed = 8 * self.blockW / 70
        self.minXSpeed = 1 / 4 * (self.blockW / 70)
        self.doubleJumpCDVal = 15
        self.playerW = self.blockW * 72 / 100
        self.playerH = self.blockH * 97 / 100
        
    def updateVariables(self):
        self.fallSpeedScaler = 0.8 * self.blockH / 70
        self.maxFallSpeed = 50 * self.blockH / 70
        self.maxWallSlide = self.maxFallSpeed * 0.1
        self.jumpPower = 15 * self.blockH / 70
        self.movementSpeed = 2 * self.blockH / 70
        self.airStrafeSpeed = self.movementSpeed *0.4 # 0.4 is lowest that "works"
        self.friction = 1 * self.blockW / 70
        self.airResistance = self.friction * 0.25
        self.maxMoveSpeed = 8 * self.blockW / 70
        self.minXSpeed = 1 / 4 * (self.blockW / 70)
        self.doubleJumpCDVal = 15
        self.playerW = self.blockW * 72 / 100
        self.playerH = self.blockH * 97 / 100
    
    def setBlockSize(self, w, h):
        self.blockW = w
        self.blockH = h

configData = ConfigData()