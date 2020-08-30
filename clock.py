import time


class Clock:
    """ Clock class.
    Uses singleton pattern.
    Time tings
    """

    # Singleton things
    _instance = None
    @staticmethod
    def get_instance():
        if Clock._instance is None:
            Clock()
        return Clock._instance

    def __init__(self):
        if Clock._instance is not None:
            print("Clock instance already made.")
        else:
            self.on_startup()
            Clock._instance = self

    @staticmethod
    def init():
        Clock.get_instance()

    def on_startup(self):
        self.start_time = time.time()
        self._last_frame_time = self.start_time

    # Clock tings
    start_time = None
    _last_frame_time = None
    _delta_time = 0

    def _update(self):
        current_time = time.time()
        self._delta_time = current_time - self._last_frame_time
        self._last_frame_time = current_time

    def get_delta_time(self):
        return self._delta_time
