import pygame
from typing import Any
from grid_position import GridPosition
from lib import Frame, GameObject, World, Sprite
from prototype.rat import Rat

class RatHole(GameObject):
    """
    A RatHole object in the game world. Inherits from GameObject.

    Effects: Set checkpoint for player
    Condition: RatHole effects will be triggered once player collide with the RatHole.
    """

    def __init__(self, **metadata: Any) -> None:
        super().__init__(**metadata)

        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.player: Rat = metadata['player']
        
        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.image.load("src/images/rat_hole.png")

    def on_create(self, world: 'World'):
        world.sprites.add(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:
                world.remove(self)
