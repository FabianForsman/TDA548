# package exercises.ex2asteroids

# Class representing a Spaceship
class Spaceship:
    MAX_DX = 2
    MAX_DY = 2

    def __init__(self, x, y, width, height, dx=0, dy=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy

    # We're using a simplification of intersection here,
    # treating an asteroid as its rectangular bounding box.
    def intersects(self, asteroid):
        above = asteroid.get_max_y() < self.get_y()
        below = asteroid.get_y() > self.get_max_y()
        left_of = asteroid.get_max_x() < self.get_x()
        right_of = asteroid.get_x() > self.get_max_x()
        return not (above or below or left_of or right_of)

    def stop(self):
        self.dx = self.dy = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def set_dx(self, dx):
        self.dx = dx

    def set_dy(self, dy):
        self.dy = dy

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_max_x(self):
        return self.x + self.width

    def get_max_y(self):
        return self.y + self.height
