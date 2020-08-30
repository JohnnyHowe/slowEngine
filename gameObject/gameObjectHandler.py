""" Handles the updating of gameObject components. """


class GameObjectHandler:

    # Singleton things
    _instance = None

    @staticmethod
    def get_instance():
        if GameObjectHandler._instance is None:
            GameObjectHandler()
        return GameObjectHandler._instance

    def __init__(self):
        if GameObjectHandler._instance is not None:
            print("GameObjectHandler instance already made.")
        else:
            self.on_startup()
            GameObjectHandler._instance = self

    @staticmethod
    def init():
        GameObjectHandler.get_instance()

    # GameObjectHandler help
    game_objects = None

    def on_startup(self):
        """ When the singleton is first initialized, this is called. """
        self.game_objects = []

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def update_game_objects(self):
        """ Loop through the game_objects and update their components. """
        for game_object in self.game_objects:
            game_object.update()
            game_object._update_components()

