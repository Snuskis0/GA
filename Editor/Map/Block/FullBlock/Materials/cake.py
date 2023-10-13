from Editor.Map.Block.FullBlock.fullBlock import FullBlock

class Cake(FullBlock):
    def __init__(self, pos):
        self.shouldUpdate = True
        baseFileName = 'cake.png'
        super().__init__(pos, self.shouldUpdate, baseFileName)