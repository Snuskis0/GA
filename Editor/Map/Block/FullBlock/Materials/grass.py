from Editor.Map.Block.FullBlock.fullBlock import *

class Grass(FullBlock):
    def __init__(self, pos):
        super().__init__(pos, 'grass.png')