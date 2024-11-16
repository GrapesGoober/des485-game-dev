import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.items.test_item import TestItemShopGUI
from src.prototype.inventory import InventoryGUI
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 20, 20
COLOR = (0, 255, 100)

IMAGE = pygame.Surface(SIZE)
IMAGE.fill(COLOR)

class Shop(GameObject):
    def __init__(self, player: Rat, inventory: InventoryGUI, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = IMAGE
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)
        self.player: Rat = player
        self.items: list[GameObject] = [
            # add items here
            TestItemShopGUI(player, inventory, (50, 200))
        ]

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)
        world.remove(self.position)
    
    def on_update(self, world: World, frame: Frame) -> None:
        world.remove(*self.items)
        for n in self.position.get_neighbours(world, manhat_dist=1):
            if n.parent_object == self.player: 
                world.add(*self.items)
