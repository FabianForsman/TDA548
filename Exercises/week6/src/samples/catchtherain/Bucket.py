# package samples.catchtherain

from AbstractGameItem import AbstractGameItem


# A class to collect falling rain drops into
# This is the object the player can move.
class Bucket(AbstractGameItem):
    BUCKET_WIDTH = 40
    BUCKET_HEIGHT = 40
    BUCKET_SPEED = 5

    def __init__(self, x, y, width=BUCKET_WIDTH, height=BUCKET_HEIGHT, color=None):
        super().__init__(x, y, width, height)
        self.__dx = 0
        self.__color = color

    def move(self):
        self.set_x(self.get_x() + self.__dx)

    def set_dx(self, dx):
        self.__dx = dx

    def get_color(self):
        return self.__color
