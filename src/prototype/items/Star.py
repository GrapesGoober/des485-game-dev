import pygame
from typing import Any
from src.prototype.inventory import InventoryGUI
from src.grid_position import GridPosition
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat

class Star(GameObject):
    """
    A Star object in the game world. Inherits from GameObject.

    Effects: +1 to dice role
    Condition: Star effects will be triggered once player roll a dice. Player can choose to use the star or not.
    """

    def __init__(self, **metadata: Any) -> None:
        super().__init__(**metadata)

        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.player: Rat = metadata['player']
        self.inventory: InventoryGUI = metadata['inventory']

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.image.load("src/images/items/star.png")
        
    def on_create(self, world: 'World'):
        world.sprites.add(self.sprite)

    def on_remove(self, world: 'World'):
        world.sprites.remove(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:

                print("Player: Star collected")
                world.remove(self)

                # Add item to inventory
                item_gui = StarInventoryGUI(self)
                world.add(item_gui)
                self.inventory.add_item_gui(item_gui)

    def use_item(self):
        self.player.diceroll.walk_step += 1

class StarInventoryGUI():
    def __init__(self, item: GameObject) -> None:
        super().__init__()

        self.item = item

        self.sprite = Sprite()
        self.sprite.src_image = item.sprite.src_image

        self.inventory: InventoryGUI = item.inventory

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        # Update position
        self.sprite.position = self.inventory.get_item_gui_position(self)

        if pygame.key.get_pressed()[pygame.K_1]:
            print("Player: Star used")
            self.item.use_item()
            world.remove(self)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

