from .component import Component
from .transform import Transform
from ..drawer import Drawer


class SpriteRenderer(Component):

    sprite = None
    color = (0, 0, 0)

    def __init__(self, game_object):
        super().__init__(game_object)

    def update(self):
        self.draw_rect()

    def draw_rect(self):
        """ Draw a rect of the gameObject's position and size. """
        transform = self.game_object.get_component(Transform)
        Drawer.draw_rect(transform.position, transform.size, self.color)
