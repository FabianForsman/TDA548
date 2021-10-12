# package samples.catchtherain

from AbstractGameItem import AbstractGameItem
from Config import *


# The ground the bucket is standing (moving) on.
class Ground(AbstractGameItem):
    GROUND_HEIGHT = 10

    def __init__(self, x, y, width=GAME_WIDTH, height=GROUND_HEIGHT, color="Brown"):
        super().__init__(x, y, width, height)
        self.__color = color

    def get_color(self):
        return self.__color
