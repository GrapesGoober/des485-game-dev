import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 20, 20
COLOR = (255, 255, 255)
PLAYER_KEY = "PLAYER"

class TestItem(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)
        self.player: Rat = None

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

        self.player = world.global_states.get(PLAYER_KEY)
        assert self.player, f"Missing {PLAYER_KEY} required in Item"

    def on_remove(self, world):
        world.sprites.remove(self.sprite)
        world.remove(self.position)

    def on_update(self, world: World, frame: Frame) -> None:
        # check player collision to add itself to inventory
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:
                print("item picked")
                world.remove(self)