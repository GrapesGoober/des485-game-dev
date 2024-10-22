import pygame
from lib import Frame, GameObject, World
from src.grid_sprite import GridSprite

SIZE = 100, 100
COLOR = (255, 255, 255)

class MovableBox(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.sprite = GridSprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.sprite.grid_position = grid_position

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        for event in frame.events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_w: self.sprite.grid_y -= 1
                    case pygame.K_a: self.sprite.grid_x -= 1
                    case pygame.K_s: self.sprite.grid_y += 1
                    case pygame.K_d: self.sprite.grid_x += 1
