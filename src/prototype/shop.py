from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite

from src.prototype.items.TunaCan import TunaCanShopGUI
from src.prototype.items.Hammer import HammerShopGUI
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 20, 20

class Shop(GameObject):
    def __init__(self, **metadata: Any) -> None:

        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.player: Rat = metadata['player']

        # Create sprite 
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
