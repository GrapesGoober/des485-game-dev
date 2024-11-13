import random
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 20, 20
COLOR = (255, 255, 255)

class Tree(GameObject):
    def __init__(self, player: Rat, grid_position: tuple[int, int], has_cat: bool) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)

        self.has_cat: bool = has_cat
        self.player: Rat = player

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_update(self, world: World, frame: Frame) -> None:
        for n in self.position.get_neighbours(world, manhat_dist=1):
            if n.parent_object == self.player and self.has_cat:
                world.remove(self.player)
