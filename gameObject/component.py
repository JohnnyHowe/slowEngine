
class Component:

    gameObject = None   # Parent obj

    def __init__(self, game_object):
        self.game_object = game_object

    def update(self):
        print("Update in component not implemented")
