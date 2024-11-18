from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite

from src.prototype.items.TunaCan import TunaCanShopGUI
from src.prototype.items.Hammer import HammerShopGUI
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 64, 64

class Shop(GameObject):
    def __init__(self, **metadata: Any) -> None:

        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.player: Rat = metadata['player']

        # Create sprite 
        self.sprite = Sprite()
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/shop.png"),
            SIZE
        )
        
        self.sprite.x = self.position.grid_position[0] * SIZE[0]
        self.sprite.y = self.position.grid_position[1] * SIZE[1]
        self.items: list[GameObject] = [
            # add items here
            TunaCanShopGUI(player=self.player, position=(50, 200)),
            HammerShopGUI(player=self.player, position=(50, 300)),
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
