from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite

from src.grid_position import GridPosition

SIZE = 720, 480

class GrassField(GameObject):
    def __init__(self, **metadata: Any) -> None:

        # Set metadata
        self.position = GridPosition(metadata['grid_position'])

        # Create sprite 
        self.sprite = Sprite()
        self.sprite.src_image = pygame.image.load("src/images/grass_field.png")
        self.sprite.x = self.position.grid_position[0] * 48
        self.sprite.y = self.position.grid_position[1] * 48
        
    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)
        world.remove(self.position)
    
    def on_update(self, world: World, frame: Frame) -> None:
        pass
