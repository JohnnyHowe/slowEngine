from .component import Component
from ..vector2 import Vector2


class Transform(Component):

    position = None
    size = None

    def __init__(self, game_object):
        super().__init__(game_object)

        self.position = Vector2(0, 0)
        self.size = Vector2(1, 1)

    def update(self):
        pass
