from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Grass(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'grass.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)