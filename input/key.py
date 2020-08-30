import pygame


class Key:
    """ Key class.
    Uses singleton pattern.
    Controls key handling
    """

    # Singleton things
    _instance = None
    @staticmethod
    def get_instance():
        if Key._instance is None:
            Key()
        return Key._instance

    def __init__(self):
        if Key._instance is not None:
            print("Key instance already made.")
        else:
            self.on_startup()
            Key._instance = self

    @staticmethod
    def init():
        Key.get_instance()

    def on_startup(self):
        pass

    def is_pressed(self, key_name):
        return pygame.key.get_pressed()[eval("pygame.K_" + key_name)]
