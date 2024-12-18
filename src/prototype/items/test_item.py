from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.inventory import InventoryGUI
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 48, 48
COLOR = (0, 0, 255)

IMAGE = pygame.Surface(SIZE)
IMAGE.fill(COLOR)

ITEM_NUT_COST = 1

class BaseTestItem(GameObject):
    def __init__(self) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = IMAGE

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

class TestItemProp(BaseTestItem):
    def __init__(self, player: Rat, inventory: InventoryGUI, grid_position: tuple[int, int]) -> None:
        super().__init__()
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)
        self.player: Rat = player
        self.inventory: InventoryGUI = inventory
        self.is_picked = False

    def on_update(self, world: World, frame: Frame) -> None:
        # check player collision to add itself to inventory GUI
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:
                item_gui = TestItemInventoryGUI(self.player, self.inventory)
                world.add(item_gui)
                self.inventory.add_item_gui(item_gui)
                world.remove(self)

class TestItemInventoryGUI(BaseTestItem):
   
    def __init__(self, player: Rat, inventory: InventoryGUI) -> None:
        super().__init__()
        self.player: Rat = player
        self.inventory: InventoryGUI = inventory

    def on_update(self, world, frame):
        # the inventory GUI will figure what coordinate to pose as
        self.sprite.position = self.inventory.get_item_gui_position(self)
        # right now, as a place holder, just use space bar
        # realistically, use mouse position
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            print("hi, using item")
            print(f"i have the player here {self.player} what should I do with it?")
            world.remove(self)
class TestItemShopGUI(BaseTestItem):
   
    def __init__(self, player: Rat, inventory: InventoryGUI, position: tuple[int, int]) -> None:
        super().__init__()
        self.player: Rat = player
        self.sprite.position = position
        self.inventory = inventory

    def on_update(self, world, frame):
        for e in frame.events:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                in_bounds = (
                    mouse_x > self.sprite.x - SIZE[0] and 
                    mouse_x < self.sprite.x + SIZE[0] and 
                    mouse_y > self.sprite.y - SIZE[1] and 
                    mouse_y < self.sprite.y + SIZE[1]
                )

                if in_bounds and self.player.nut_counter >= ITEM_NUT_COST:
                    self.player.nut_counter -= ITEM_NUT_COST
                    item_gui = TestItemInventoryGUI(self.player, self.inventory)
                    world.add(item_gui)
                    self.inventory.add_item_gui(item_gui)