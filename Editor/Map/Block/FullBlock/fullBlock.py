from Editor.Map.Block.block import Block

class FullBlock(Block):
    def __init__(self, pos, shouldUpdate, baseFileName):
        super().__init__(pos, shouldUpdate, baseFileName)
        