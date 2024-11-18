import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 64, 64
COLOR = (255, 0, 255)

class Rock(GameObject):
    def __init__(self, player: Rat, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/rock.png"),
            SIZE
        )
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)

        self.player: Rat = player

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)
        world.remove(self.position)

    def on_update(self, world: World, frame: Frame) -> None:
        pass