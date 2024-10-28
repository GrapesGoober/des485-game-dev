import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_object import GridObject

SIZE = 100, 100
COLOR = (255, 255, 255)

class MovableBox(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.grid_obj = GridObject(grid_position)

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.grid_obj)

    def on_update(self, world: World, frame: Frame) -> None:

        next_x, next_y = self.grid_obj.grid_position
        for event in frame.events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_w: next_y -= 1
                    case pygame.K_a: next_x -= 1
                    case pygame.K_s: next_y += 1
                    case pygame.K_d: next_x += 1

        if not GridObject.is_occupied(world, (next_x, next_y)):
            self.grid_obj.grid_position = (next_x, next_y)


        self.sprite.x = self.grid_obj.grid_x * SIZE[0]
        self.sprite.y = self.grid_obj.grid_y * SIZE[1]