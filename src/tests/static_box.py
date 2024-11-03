import pygame
from lib import GameObject, World, Sprite
from src.grid_position import GridPosition

SIZE = 100, 100
COLOR = (255, 255, 255)

class StaticBox(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)
