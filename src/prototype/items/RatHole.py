import pygame
from typing import Any
from lib import Frame, GameObject, World, Sprite

from src.grid_position import GridPosition
from src.prototype.rat import Rat

SIZE = 64, 64

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
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/items/rat_hole.png"),
            SIZE
        )
        self.sprite.x = metadata['grid_position'][0] * SIZE[0]
        self.sprite.y = metadata['grid_position'][1] * SIZE[1]

    def on_create(self, world: 'World'):
        world.sprites.add(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:

                print("Player: Reached Rat Hole")
                
                # Set the player's spawn position to the rat hole's position
                self.player.spawn_position = self.position.grid_position

                # Play sound
                pygame.mixer.Sound.play(pygame.mixer.Sound('src/sound/rathole_reached.mp3'))

                # Change sprite
                self.sprite.src_image = pygame.transform.scale(
                    pygame.image.load("src/images/items/rat_hole_reached.png"),
                    SIZE
                )

    def on_remove(self, world: 'World'):
        world.sprites.remove(self.sprite)
    
