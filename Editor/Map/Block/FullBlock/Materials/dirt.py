from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Dirt(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'dirt.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)