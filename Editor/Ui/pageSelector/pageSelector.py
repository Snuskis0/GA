import pygame

class PageSelector(pygame.sprite.Sprite()):
    def __init__(self, pos, id):
        super().__init__()
        self.pos = pos
        self.id = id
        self.getImage()
        self.rect = self.image.get_rect(topleft = self.pos)
    
    def getImage(self):
        self.filename = f"Graphics/HUD/hud_{self.id}.png"
        self.image = pygame.image.load(self.filename)