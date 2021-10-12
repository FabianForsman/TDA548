# package exercises.ex2asteroids
import time

from Asteroids import Asteroids
from Spaceship import Spaceship
import pygame as pg
pg.init()


# The GUI for the Asteroid application (model). There's only ever one,
# so we implement it entirely as a static class, no instances needed.
#
# No game logic here!
#
# See:
# - catchtherain
# - PygameEvents
# - inheritance
# - initialization
class AsteroidsGUI:

    screen = pg.display.set_mode([Asteroids.GAME_WIDTH, Asteroids.GAME_HEIGHT])
    points_font = pg.font.SysFont(None, 36)
    game_over_font = pg.font.SysFont(None, 72)
    clock = pg.time.Clock()

    BLACK = (  0,   0,   0)
    BLUE  = (  0,   0, 255)
    RED   = (255,   0,   0)

    @classmethod
    def run(cls):
        keep_going = True
        while keep_going:
            cls.clock.tick(Asteroids.GAME_SPEED)
            Asteroids.update(time.time_ns())
            cls.render()
            keep_going &= not Asteroids.is_game_over()
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        Asteroids.set_ship_speed(-Spaceship.MAX_DX, 0)
                    elif event.key == pg.K_RIGHT:
                        Asteroids.set_ship_speed(Spaceship.MAX_DX, 0)
                    elif event.key == pg.K_UP:
                        Asteroids.set_ship_speed(0, -Spaceship.MAX_DY)
                    elif event.key == pg.K_DOWN:
                        Asteroids.set_ship_speed(0, Spaceship.MAX_DY)
                elif event.type == pg.KEYUP:
                    if event.key in [pg.K_LEFT, pg.K_RIGHT, pg.K_DOWN, pg.K_UP]:
                        Asteroids.stop_ship()
                elif event.type == pg.QUIT:
                    keep_going = False
        pg.quit()

    # --------  pygame graphics rendering etc. -----------------------
    @classmethod
    def render(cls):
        cls.screen.fill(cls.BLACK)
        points = Asteroids.get_points()
        text = f"Points: {points}"
        img = cls.points_font.render(text, True, cls.RED)
        rect = img.get_rect()
        rect.topleft = (20, 20)
        cls.screen.blit(img, rect)
        ship = Asteroids.get_ship()
        pg.draw.rect(cls.screen, cls.BLUE,
                     (ship.get_x(), ship.get_y(),
                      ship.get_width(), ship.get_height()))
        oid = Asteroids.get_asteroid()
        if oid is not None:
            pg.draw.circle(cls.screen, cls.RED,
                           (oid.get_center_x(), oid.get_center_y()),
                           oid.get_width() / 2)
        if Asteroids.is_game_over():
            img = cls.game_over_font.render("GAME OVER", True, cls.RED)
            rect = img.get_rect()
            rect.topleft = (50, 50)
            cls.screen.blit(img, rect)
        pg.display.flip()

    # We don't want any instances of this class.
    def __init__(self):
        raise NotImplementedError("")


if __name__ == "__main__":
    gui = AsteroidsGUI()
    AsteroidsGUI.run()
