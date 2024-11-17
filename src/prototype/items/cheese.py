from typing import Callable
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 48, 48
COLOR = (255, 255, 255)

IMAGE = pygame.Surface(SIZE)
IMAGE.fill(COLOR)

class Cheese(GameObject):
    def __init__(self, player: Rat, callback: Callable, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = IMAGE
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)
        self.player: Rat = player
        self.callback: Callable = callback

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:
                self.callback()
