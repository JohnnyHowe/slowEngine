from slowEngine.vector2 import Vector2


class Camera:
    """ Camera class.
    Uses singleton pattern.
    Deals with game/world display things.
    """

    # Singleton things
    _instance = None
    @staticmethod
    def get_instance():
        if Camera._instance is None:
            Camera()
        return Camera._instance

    def __init__(self):
        if Camera._instance is not None:
            print("Camera instance already made.")
        else:
            self.on_startup()
            Camera._instance = self

    @staticmethod
    def init():
        Camera.get_instance()

    # Camera help
    zoom = None     # How many pixels on screen? (min of height and width)
    position = None

    def on_startup(self):
        """ When the singleton is first initialized, this is called. """
        self.zoom = 10
        self.position = Vector2(0, 0)
