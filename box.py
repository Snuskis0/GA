from obstacle import *

class Box(Obstacle):
    def __init__(self, pos):
        super().__init__(pos, 'box.png')