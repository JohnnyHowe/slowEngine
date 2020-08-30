import pygame

from .clock import Clock
from .display import Screen
from .vector2 import Vector2
from .gameObject import GameObjectHandler


def update_engine():
    Clock.get_instance()._update()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.VIDEORESIZE:
            Screen.get_instance().set_size(Vector2(event.w, event.h))

    GameObjectHandler.get_instance().update_game_objects()

    pygame.display.flip()
