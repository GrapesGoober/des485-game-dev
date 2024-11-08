import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.inventory import Inventory
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 20, 20
COLOR = (255, 255, 255)
PLAYER_KEY = "PLAYER"
INVENTORY_KEY = "INVENTORY"

class TestItemProp(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)
        self.player: Rat = None
        self.inventory: Inventory = None

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        self.player = world.global_states.get(PLAYER_KEY)
        self.inventory = world.global_states.get(INVENTORY_KEY)
        assert self.player, f"Missing '{PLAYER_KEY}'"
        assert self.inventory, f"Missing '{INVENTORY_KEY}'"

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        # check player collision to add itself to inventory
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:

                def on_item_use():
                    print("hi, using item")

                self.inventory.add_item(
                    sprite      = self.sprite,
                    on_item_use = on_item_use
                )

                world.remove(self)
