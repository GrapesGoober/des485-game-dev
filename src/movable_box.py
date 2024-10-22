import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_sprites import GridSprites

SIZE = 100, 100
COLOR = (255, 255, 255)

class MovableBox(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)

        self.grid_sprites = GridSprites(grid_position, self.sprite)

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        for event in frame.events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_w: self.grid_sprites.grid_y -= 1
                    case pygame.K_a: self.grid_sprites.grid_x -= 1
                    case pygame.K_s: self.grid_sprites.grid_y += 1
                    case pygame.K_d: self.grid_sprites.grid_x += 1
