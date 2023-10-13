from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Stone(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'stone.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)