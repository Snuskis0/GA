from Editor.Map.Block.FullBlock.fullBlock import *

class Box(FullBlock):
    def __init__(self, pos):
        super().__init__(pos, 'box.png')