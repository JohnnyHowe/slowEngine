from .screen import Screen
from .camera import Camera
from ..vector2 import Vector2


class Display:
    """ Static class for display things.
    Contains screen scale methods and conversions from world to screen coordinates and back. """

    @staticmethod
    def get_screen_scale():
        screen_size = Screen.get_instance().size
        scale = min(screen_size.x, screen_size.y)
        return scale / Camera.get_instance().zoom

    @staticmethod
    def world_to_screen_position(position):
        """ Convert the position from world coordinates to screen coordinates. """
        scale = Display.get_screen_scale()
        screen_size = Screen.get_instance().size
        offset = screen_size / 2 + Camera.get_instance().position
        return Vector2(position.x, -position.y) * scale + offset

    @staticmethod
    def screen_to_world_position(position):
        """ Convert the position from screen coordinates to world coordinates. """
        scale = Display.get_screen_scale()
        screen_size = Screen.get_instance().size
        offset = screen_size / 2 + Camera.get_instance().position
        # screen_pos = Vector2(position.x, -position.y) * scale + offset
        game_pos = (position - offset) / scale
        return Vector2(game_pos.x, -game_pos.y)

    @staticmethod
    def world_to_screen_size(size):
        """ Convert the size from world size to screen size. """
        return size * Display.get_screen_scale()

