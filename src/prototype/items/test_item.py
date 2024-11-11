from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.inventory import InventoryGUI
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 20, 20
COLOR = (255, 255, 255)
PLAYER_KEY = "PLAYER"
INVENTORY_KEY = "INVENTORY"

IMAGE = pygame.Surface(SIZE)
IMAGE.fill(COLOR)

class TestItemProp(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = IMAGE
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)
        self.player: Rat = None
        self.inventory: InventoryGUI = None

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
                item_gui = TestItemGUI(self.inventory)
                self.inventory.add_item_gui(item_gui)
                world.remove(self)

class TestItemGUI(GameObject):
    def __init__(self, inventory: InventoryGUI) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = IMAGE
        self.inventory = inventory

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        self.sprite.position = self.inventory.get_item_gui_position(self)
        # right now, as a place holder, just use space bar
        # realistically, use mouse position
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            print("hi, using item")
            world.remove(self)
