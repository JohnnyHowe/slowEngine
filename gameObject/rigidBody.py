from .component import Component
from ..vector2 import Vector2
from ..clock import Clock


class RigidBody(Component):

    velocity = None

    def __init__(self, game_object):
        super().__init__(game_object)
        self.velocity = Vector2(0, 0)

    def update(self):
        self.game_object.transform.position += self.velocity * Clock.get_instance().get_delta_time()
