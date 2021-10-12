# package samples.catchtherain

from Config import *
from Bucket import Bucket
from CatchTheRain import CatchTheRain
from Ground import Ground
from RainDrop import RainDrop
from time import time_ns

import pygame as pg

pg.init()


# A game for catching raindrops in a bucket
# This is the GUI and application file
class CatchTheRainGUI:
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)

    def __init__(self):
        drops = []
        bucket = self.__create_bucket()
        ground = self.__create_ground()
        self.ctr_model = CatchTheRain(drops, ground, bucket)
        self.screen = pg.display.set_mode([GAME_WIDTH, GAME_HEIGHT])
        self.points_font = pg.font.SysFont(None, 36)
        self.clock = pg.time.Clock()

    @staticmethod
    def __create_ground():
        return Ground(0, GAME_HEIGHT - Ground.GROUND_HEIGHT)

    @staticmethod
    def __create_bucket():
        bucket = Bucket(GAME_WIDTH / 2,
                        GAME_HEIGHT - Ground.GROUND_HEIGHT - Bucket.BUCKET_HEIGHT,
                        color="Red")
        return bucket

    def run(self):
        keep_going = True
        while keep_going:
            self.clock.tick(GAME_SPEED)
            self.update()
            keep_going = self.handle_events()
        pg.quit()

    # Called by timer
    def update(self):
        self.ctr_model.update(time_ns())
        self.render()

    # ------------ pygame graphics etc.  -----------------------------
    @staticmethod
    def __update_screen():
        pg.display.flip()

    def __draw_background(self):
        self.screen.fill(self.WHITE)

    def __show_points(self):
        points = self.ctr_model.get_points()
        img, rect = self.__create_points_image(points)
        self.__draw_points_image(img, rect)

    def __draw_points_image(self, img, rect):
        rect.topleft = (20, 20)
        self.screen.blit(img, rect)

    def __create_points_image(self, points):
        text = f"Points: {points}"
        img = self.points_font.render(text, True, self.RED)
        rect = img.get_rect()
        return img, rect

    def __draw_ground(self):
        ground = self.ctr_model.get_ground()
        color = ground.get_color()
        pg.draw.rect(self.screen, color, (ground.get_x(), ground.get_y(), ground.get_width(), ground.get_height()))

    def __draw_bucket(self):
        bucket = self.ctr_model.get_bucket()
        color = bucket.get_color()
        pg.draw.rect(self.screen, color,
                     (bucket.get_x(), bucket.get_y(), bucket.get_width(), bucket.get_height()))

    def __draw_drops(self):
        for drop in self.ctr_model.get_drops():
            self.__draw_drop(drop)

    def __draw_drop(self, drop: RainDrop):
        color = drop.get_color()
        center = (drop.get_x() + drop.get_width() / 2, drop.get_y() + drop.get_height() / 2)
        pg.draw.circle(self.screen, color, center, drop.get_width() / 2)

    def render(self):
        self.__draw_background()
        self.__show_points()
        self.__draw_ground()
        self.__draw_bucket()
        self.__draw_drops()
        self.__update_screen()

    # ---- Event handlers ----
    def handle_events(self):
        keep_going = True
        events = pg.event.get()
        for event in events:
            self.__handle_key_event(event)
            keep_going &= self.__check_for_quit(event)
        return keep_going

    def __handle_key_event(self, event):
        print(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.__update_bucket_speed(-1)
            elif event.key == pg.K_RIGHT:
                self.__update_bucket_speed(1)
        elif event.type == pg.KEYUP:
            self.__update_bucket_speed(0)

    def __update_bucket_speed(self, factor):
        self.ctr_model.set_bucket_speed(Bucket.BUCKET_SPEED * factor)

    @staticmethod
    def __check_for_quit(event):
        return event.type != pg.QUIT


if __name__ == "__main__":
    gui = CatchTheRainGUI()
    gui.run()
