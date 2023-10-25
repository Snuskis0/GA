from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Choco(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'choco.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)