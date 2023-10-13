import pygame
from Editor.Map.Block.FullBlock.fullBlock import *
from functions import howManyTrueIn

class Grass(FullBlock):
    def __init__(self, pos):
        super().__init__(pos, 'grass.png')