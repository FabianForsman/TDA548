# package samples.catchtherain

from Config import *
from Bucket import Bucket
from Ground import Ground
from RainDrop import RainDrop
from typing import List
import random


#  CatchTheRain, a game for catching raindrops in a bucket
#  This class represents the overall game
#
# See:
# - asteroids/*
class CatchTheRain:
    def __init__(self, drops, ground, bucket):
        self.__drops: List[RainDrop] = drops
        self.__ground: Ground = ground
        self.__bucket: Bucket = bucket

        self.__to_remove = []
        self.__points = 0
        self.__time_for_last_drop = 0

    # The main "game loop" that makes everything happens
    # Called by GUI timer approx. 1/60 sec.
    def update(self, now):
        self.__move_the_bucket()
        self.__move_all_drops()
        self.__add_new_raindrop_if_time(now)

    def __add_new_raindrop_if_time(self, now):
        if self.__enough_time_has_passed(now):
            self.__add_new_raindrop()
            self.__time_for_last_drop = now

    def __add_new_raindrop(self):
        self.__drops.append(self.create_raindrop())

    def __enough_time_has_passed(self, now):
        return now - self.__time_for_last_drop > HALF_SEC

    def __move_all_drops(self):
        for drop in self.__drops:
            drop.move()
            self.__add_for_removal_if_hit(drop)
        self.__remove_all_hit_drops()

    def __remove_all_hit_drops(self):
        for item in self.__to_remove:
            self.__drops.remove(item)
        self.__to_remove.clear()

    def __add_for_removal_if_hit(self, drop):
        if drop.intersects(self.__ground) or drop.intersects(self.__bucket):
            self.__to_remove.append(drop)
            if drop.intersects(self.__bucket):
                self.__points += drop.get_dy()

    def __move_the_bucket(self):
        self.__bucket.move()  # No check for hitting left/right margin

    # Create Raindrop with random size, speed, color
    @staticmethod
    def create_raindrop():
        x = 50 + random.randint(0, GAME_WIDTH - 100)
        y = 0  # - random.randint(0, 20)
        width = 5 + random.randint(0, 20)
        height = width
        dy = 1 + random.randint(5, int(125 / width))
        # color = Color.color(rand.nextDouble(), rand.nextDouble(), rand.nextDouble())
        color = "Blue"
        return RainDrop(x, y, width, height, dy, color)

    # --------- Used by GUI for rendering -------------------------
    def get_drops(self):
        return self.__drops

    def get_bucket(self):
        return self.__bucket

    def get_ground(self):
        return self.__ground

    def get_points(self):
        return self.__points

    # ------------ From GUI to model ---------------
    def set_bucket_speed(self, speed):
        self.__bucket.set_dx(speed)
