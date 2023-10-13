from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Castle(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'castle.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)