import pygame
from typing import Any
from grid_position import GridPosition
from lib import Frame, GameObject, World, Sprite
from prototype.rat import Rat

class TunaCan(GameObject):
    """
    A TunaCan object in the game world. Inherits from GameObject.

    Effects: Stun the cat
    Condition: The effect will be triggered once the player going to get eaten by the cat. 
    The prompt will be shown on the screen whether the player want to use the tuna can or not.
    """

    def __init__(self, **metadata: Any) -> None:
        super().__init__(**metadata)

        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.player: Rat = metadata['player']

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.image.load("src/images/star.png")

    def on_create(self, world: 'World'):
        world.sprites.add(self.sprite)

    def on_remove(self, world: 'World'):
        world.sprites.remove(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:
                world.remove(self)

    def use_item(self):
        self.player.dice_role += 1