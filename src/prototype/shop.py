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
        self.sprite.src_image = pygame.image.load("src/images/items/shop.png")

        # Set sprite position
        self.sprite.x = metadata['grid_position'][0] * SIZE[0]
        self.sprite.y = metadata['grid_position'][1] * SIZE[1]

        self.gui_subworld = World()
        self.gui_subworld.add(
            # add items here
            TunaCanShopGUI(player=self.player, position=(50, 200)),
            HammerShopGUI(player=self.player, position=(80, 200))
        )

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)
        world.remove(self.position)
    
    def on_update(self, world: World, frame: Frame) -> None:
        self.gui_subworld.update(frame.events, frame.dt)
        self.gui_subworld.draw(pygame.display.get_surface())