
from lib import GameObject, World

class LevelManager:
    def __init__(self, world: World):
        self.world = world
        self.current_level: list[GameObject] = []

    def transition(self, level: list[GameObject]):
        self.world.remove(*self.current_level)
        self.world.add(*level)
        self.current_level = level