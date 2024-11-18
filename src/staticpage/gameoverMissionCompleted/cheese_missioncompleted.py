from typing import Callable
import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition

SIZE = 120, 120
COLOR = (255, 255, 255)

IMAGE = pygame.Surface(SIZE)
IMAGE.fill(COLOR)

class CheeseMissionCompleted(GameObject):
    def __init__(self, position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        original_image = pygame.image.load("src/images/items/cheese.png")
        self.sprite.src_image = pygame.transform.scale(original_image, SIZE)
        self.sprite.position = position

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        pass
