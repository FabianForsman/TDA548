# package samples.catchtherain

from AbstractGameItem import AbstractGameItem


# A class for rain drops falling down
# (to be collected in the bucket or will hit the ground)
class RainDrop(AbstractGameItem):
    def __init__(self, x, y, width, height, dy, color):
        super().__init__(x, y, width, height)
        self.__dy = dy
        self.__color = color

    def move(self):
        self.set_y(self.get_y() + self.__dy)

    def get_dy(self):
        return self.__dy

    def get_color(self):
        return self.__color
