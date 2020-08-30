import pygame

from .display import Display, Screen


# def fill_screen(fill_color):
#     """ Fill the screen with a solid color. """
#     Screen.get_instance().surface.fill(fill_color)

class Drawer:

    @staticmethod
    def draw_rect(position, size, color=(0, 0, 0), screen_coordinates=False):
        if screen_coordinates:
            print("not in yet lol")
            rect = (0, 0, 0, 0)
        else:
            screen_size = Display.world_to_screen_size(size)
            screen_position = Display.world_to_screen_position(position) - screen_size / 2
            rect = (screen_position.x, screen_position.y, screen_size.x, screen_size.y)
        pygame.draw.rect(Screen.get_instance().surface, color, rect)
