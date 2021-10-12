# package exercises.ex2asteroids

import random

from Asteroid import Asteroid
from Spaceship import Spaceship


# Class representing the over all game - singleton!
# Most of game logic here (nothing about the look here)
class Asteroids:

    GAME_SPEED = 20
    GAME_WIDTH = 500
    GAME_HEIGHT = 500
    SEC = 1_000_000_000

    ship = Spaceship(GAME_WIDTH / 2, GAME_HEIGHT / 2, 20, 20)
    oid = None
    points = 0
    game_over = False
    time_of_last_hit = 0

    @classmethod
    # Main game loop (called by timer in GUI)
    def update(cls, now):
        cls.ship.move()
        oid = cls.oid
        if oid is None and now - cls.time_of_last_hit > cls.SEC:
            oid = cls.create_asteroid()
            cls.oid = oid
            cls.time_of_last_hit = now
        if oid is not None:
            oid.move()
            if cls.ship.intersects(oid):
                cls.game_over = True
            is_left = oid.get_x() < -1
            is_right = oid.get_x() > cls.GAME_WIDTH + 1
            is_above = oid.get_y() < -1
            is_below = oid.get_y() > cls.GAME_HEIGHT + 1
            if is_left or is_right or is_above or is_below:
                cls.oid = None

    @classmethod
    # Asteroid may come from all directions
    def create_asteroid(cls):
        is_horizontal = random.randint(0, 1)
        starts_from_low = random.randint(0, 1)
        dx = 4 - random.randint(0, 3)
        dy = 4 - random.randint(0, 3)
        x, factor_x, y, factor_y = cls.__help_build_asteroid_that(is_horizontal, starts_from_low)
        size = 50 - random.randint(1, 40)
        return Asteroid(x, y, size, size, dx*factor_x, dy*factor_y)

    @classmethod
    def __help_build_asteroid_that(cls, is_horizontal, starts_from_low):
        maxes = {True: cls.GAME_WIDTH, False: cls.GAME_HEIGHT}
        fixed = -1 if starts_from_low else maxes[is_horizontal] + 1
        factor_fixed = 1 if starts_from_low else -1
        rand = random.randint(1, maxes[not is_horizontal])
        factor_rand = 1 if random.randint(0, 1) else -1
        if is_horizontal:
            return fixed, factor_fixed, rand, factor_rand
        else:
            return rand, factor_rand, fixed, factor_fixed

    # -------- Used by GUI --------------------
    @classmethod
    def stop_ship(cls):
        cls.ship.stop()

    @classmethod
    def set_ship_speed(cls, dx, dy):
        cls.ship.set_dx(dx)
        cls.ship.set_dy(dy)

    @classmethod
    def get_ship(cls):
        return cls.ship

    @classmethod
    def get_asteroid(cls):
        return cls.oid

    @classmethod
    def get_points(cls):
        return cls.points

    @classmethod
    def is_game_over(cls):
        return cls.game_over
