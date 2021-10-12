# package samples.catchtherain

from HasPosition import HasPosition
from abc import ABC


# Base class for anything that can be positioned in the world.
# This class holds common data and methods
class AbstractGameItem(HasPosition, ABC):
    def __init__(self, x, y, width, height):
        self.x = x      # 0, 0 is upper left corner
        self.y = y
        self.width = width
        self.height = height

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # Nice utility method possibly useful for any positionable object
    def intersects(self, other):
        above = other.__get_max_y() < self.get_y()
        below = other.get_y() > self.__get_max_y()
        left_of = other.__get_max_x() < self.get_x()
        right_of = other.get_x() > self.__get_max_x()
        return not (above or below or left_of or right_of)

    # Getters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Convenience
    def __get_max_x(self):
        return self.x + self.width

    def __get_max_y(self):
        return self.y + self.height
