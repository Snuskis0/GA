from Editor.Map.Block.FullBlock.fullBlock import *

class Sand(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'sand.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)