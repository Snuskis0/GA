from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Tundra(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'tundra.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)