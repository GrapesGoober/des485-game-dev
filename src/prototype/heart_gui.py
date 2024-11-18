from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite

from src.prototype.rat import Rat
from src.grid_position import GridPosition

TOP_LEFT_POSITION = (50, 220)
SPACING = 64

HEART = pygame.transform.scale(
    pygame.image.load("src/images/heart.png"),
    (64, 64)
)

class HeartGUI(GameObject):
    def __init__(self, player: Rat) -> None:

        # Set metadata
        self.player: Rat = player

        # Create heart sprites
        self.hearts = [Sprite() for _ in range(self.player.max_health)]
        for index, sprite in enumerate(self.hearts):
            sprite.src_image = HEART.copy()
            sprite.x = TOP_LEFT_POSITION[0] + int(index >= 3) * SPACING
            sprite.y = TOP_LEFT_POSITION[1] + index % 3 * SPACING
        ...

    def on_create(self, world: World) -> None:
        world.sprites.add(*self.hearts)

    def on_remove(self, world):
        world.sprites.remove(*self.hearts)
    
    def on_update(self, world: World, frame: Frame) -> None:
        for index, sprite in enumerate(self.hearts):
            sprite.src_image.set_alpha(0)
            if index < self.player.health:
                sprite.src_image.set_alpha(255)

