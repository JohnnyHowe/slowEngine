from .gameObjectHandler import GameObjectHandler
from .transform import Transform


class GameObject:
    """ Game object,
    really just a container for a bunch of components. """

    transform = None    # Quick reference to transform component
    components = None

    def __init__(self):
        GameObjectHandler.get_instance().add_game_object(self)
        self.components = []
        self.transform = self.add_component(Transform)

    def add_component(self, component):
        component_obj = component(self)
        self.components.append(component_obj)
        return component_obj

    def get_component(self, component_type):
        """ Get the 1st component found with the right type. """
        for component in self.components:
            if isinstance(component, component_type):
                return component

    def _update_components(self):
        """ Call the update method of all the components. """
        for component in self.components:
            component.update()

    def update(self):
        """ Placeholder """
        pass
