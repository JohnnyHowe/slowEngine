from .component import Component
from .spriteRenderer import SpriteRenderer


class Animator(Component):

    sprite_renderer = None
    animation = None

    def __init__(self, game_object):
        super().__init__(game_object)
        self.sprite_renderer = game_object.get_component(SpriteRenderer)




