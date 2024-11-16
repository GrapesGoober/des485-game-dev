import pygame
from typing import Any
from lib import Frame, GameObject, World, Sprite

from src.grid_position import GridPosition
from src.prototype.inventory import InventoryGUI
from src.prototype.rat import Rat

SIZE = 20, 20

class Rainbow(GameObject):
    """
    A Rainbow object in the game world. Inherits from GameObject.

    Effects: +2 to dice role
    Condition: Rainbow effects will be triggered once player roll a dice. Player can choose to use the Rainbow or not.
    """

    def __init__(self, **metadata: Any) -> None:
        super().__init__(**metadata)
        
        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.player: Rat = metadata['player']

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.image.load("src/images/items/rainbow.png")
        self.sprite.x = metadata['grid_position'][0] * SIZE[0]
        self.sprite.y = metadata['grid_position'][1] * SIZE[1]

    def on_create(self, world: 'World'):
        world.sprites.add(self.sprite)

    def on_remove(self, world: 'World'):
        world.sprites.remove(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:
                print("Player: Rainbow collected")
                world.remove(self)

                # Add item to inventory
                item_gui = RainbowInventoryGUI(self)
                world.add(item_gui)
                self.player.inventory.add_item_gui(item_gui)

    def use_item(self):
        self.player.diceroll.walk_step += 2

class RainbowInventoryGUI():
    def __init__(self, item: Rainbow) -> None:
        super().__init__()

        self.item = item

        self.sprite = Sprite()
        self.sprite.src_image = item.sprite.src_image

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        # Update position
        self.sprite.position = self.item.player.inventory.get_item_gui_position(self)

        if pygame.key.get_pressed()[pygame.K_2]:
            print("Player: Rainbow used")
            self.item.use_item()
            world.remove(self)