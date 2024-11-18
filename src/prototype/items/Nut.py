from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite

from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 64, 64

class Nut(GameObject):
    def __init__(self, **metadata) -> None:

        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.player: Rat = metadata['player']

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/items/nut.png"),
            SIZE
        )

        # Set sprite position
        self.sprite.x = metadata['grid_position'][0] * SIZE[0]
        self.sprite.y = metadata['grid_position'][1] * SIZE[1]

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)
    
    def on_update(self, world: World, frame: Frame) -> None:

        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:
                self.player.nut_counter += 1
                print("Player nut counter: ", self.player.nut_counter)
                world.remove(self)
