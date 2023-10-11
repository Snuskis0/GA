import pygame
from config import blockW, blockH
from Editor.Map.Block.block import Block

class FullBlock(Block):
    def __init__(self, pos, filename):
        super().__init__(pos, filename)
        