import pygame
from ..vector2 import Vector2


class Screen:
    """ Screen class.
    Uses singleton pattern.
    Deals only with screen things, for normal display things, refer to Display. """

    # Singleton things
    _instance = None
    @staticmethod
    def get_instance():
        if Screen._instance is None:
            Screen()
        return Screen._instance

    def __init__(self):
        if Screen._instance is not None:
            print("Screen instance already made.")
        else:
            self.on_startup()
            Screen._instance = self

    @staticmethod
    def init():
        Screen.get_instance()

    # Screen help
    surface = None
    size = None

    def on_startup(self):
        """ When the singleton is first initialized, this is called. """
        self.size = Vector2(600, 400)
        self.set_surface()

    def set_size(self, new_size):
        self.size = new_size
        self.set_surface()

    def set_surface(self):
        self.surface = pygame.display.set_mode((self.size.x, self.size.y), pygame.RESIZABLE)

