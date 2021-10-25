# package samples.catchtherain

from abc import ABC, abstractmethod


# All objects the GUI shall render must implement this
# (so that the GUI is able to position it and know the size)
class HasPosition(ABC):
    @abstractmethod
    def get_x(self) -> int:  # MinX and Y is upper left corner (y-axis pointing down)
        raise NotImplementedError

    @abstractmethod
    def get_y(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_width(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_height(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_color(self):  # We just use colors for this game (i.e. no images)
        raise NotImplementedError
