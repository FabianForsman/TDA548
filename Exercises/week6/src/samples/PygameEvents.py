# package samples

import pygame
pygame.init()


#   Basic event driven pygame application
#
#  # Nothing of this on exam (some of it used in lab4) #
class PygameEvents:

    WIDTH = 500
    HEIGHT = 500

    # For some reason, THECOLORS isn't in the interface file for pygame.color,
    # but it's there, and we can use it. It contains tons of pre-defined colors.
    BLACK        = pygame.color.THECOLORS['black']
    DARKGREEN    = pygame.color.THECOLORS['darkgreen']
    ROYALBLUE    = pygame.color.THECOLORS['royalblue']
    ANTIQUEWHITE = pygame.color.THECOLORS['antiquewhite']
    DARKORCHID   = pygame.color.THECOLORS['darkorchid']

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    screen.fill(BLACK)
    mouse_button_is_down = False

    # Handlers for key events emitted by pygame. The pygame library
    # is not fully event-based, we need to make sure ourselves that
    # the events are handled properly. But it's a good principle
    # to design an application as being event-based anyway, separating
    # event handlers from event dispatch loop.
    #
    # ------------ Handle keyboard -----------------
    @staticmethod
    def key_pressed(key_event):
        key_string = key_event.key if key_event.unicode == '' else key_event.unicode
        print(f"{key_string} pressed")

    @staticmethod
    def key_released(key_event):
        key_string = key_event.key if key_event.unicode == '' else key_event.unicode
        print(f"{key_string} released")

    # ------------- Handle mouse -------------------
    @classmethod
    def on_mouse_released(cls, mouse_event):
        print("Mouse released")
        x, y = mouse_event.pos
        pygame.draw.circle(cls.screen, cls.DARKGREEN, (x, y), 15)

    @classmethod
    def on_mouse_pressed(cls, mouse_event):
        print("Mouse pressed")
        x, y = mouse_event.pos
        pygame.draw.circle(cls.screen, cls.DARKORCHID, (x, y), 15)

    @classmethod
    def on_mouse_drag(cls, mouse_event):
        x, y = mouse_event.pos
        lmb, mmb, rmb = mouse_event.buttons
        color = cls.ANTIQUEWHITE if lmb or mmb or rmb else cls.ROYALBLUE
        pygame.draw.circle(cls.screen, color, (x, y), 2)

# --------  pygame, setup graphics, event handling -----------------------
    @classmethod
    def run(cls):
        keep_going = True
        # Event dispatch loop
        while keep_going:
            events = pygame.event.get()
            for event in events:
                # Uncomment the print statement below to see all the events emitted -
                # there are far more than what we've written handlers for here.
                # print(event)

                # This really ought to be a switch statement - can you rewrite it as one?
                if event.type == pygame.KEYDOWN:
                    cls.key_pressed(event)
                elif event.type == pygame.KEYUP:
                    cls.key_released(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    cls.on_mouse_released(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cls.on_mouse_pressed(event)
                elif event.type == pygame.MOUSEMOTION:
                    cls.on_mouse_drag(event)
                elif event.type == pygame.QUIT:
                    keep_going = False

            # Make sure changes are displayed
            cls.render()
        pygame.quit()

    # --------  pygame graphics rendering etc. -----------------------
    @classmethod
    def render(cls):
        # We have to do this to make any queued up changes from pygame.draw
        # actually show on the display
        pygame.display.flip()


if __name__ == "__main__":
    PygameEvents.run()
