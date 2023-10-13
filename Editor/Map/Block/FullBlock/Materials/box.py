from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Box(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = False
        baseFileName = 'box.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)