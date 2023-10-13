from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Snow(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'snow.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)