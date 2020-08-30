

class Animation:

    sprites = None
    durations = None

    def __init__(self):
        self.sprites = []
        self.durations = []

    def set_frames(self, sprites, durations):
        self.sprites = sprites
        self.durations = durations
