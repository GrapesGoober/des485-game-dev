import pygame
from typing import Any
from lib import Frame, GameObject, World, Sprite

from src.grid_position import GridPosition
from src.prototype.inventory import InventoryGUI
from src.prototype.rat import Rat, RatStates

SIZE = 64, 64
RAINBOW_SIZE = 64, 40

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
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/items/rainbow.png"),
            RAINBOW_SIZE
        )
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
        self.player.nut_counter += 3

class RainbowInventoryGUI():
    def __init__(self, item: Rainbow) -> None:
        super().__init__()

        self.item = item

        self.sprite = Sprite()
        self.sprite.src_image = item.sprite.src_image.copy()

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        self.sprite.position = self.item.player.inventory.get_item_gui_position(self)
        
        self.sprite.src_image.set_alpha(100)
        if self.item.player.current_state == RatStates.USE_ITEM:
            self.sprite.src_image.set_alpha(255)    
            mouse_x, mouse_y = pygame.mouse.get_pos()
            in_bounds = (
                mouse_x > self.sprite.x - SIZE[0] and
                mouse_x < self.sprite.x + SIZE[0] and
                mouse_y > self.sprite.y - SIZE[1] and
                mouse_y < self.sprite.y + SIZE[1]
            )
            if in_bounds:
                self.item.use_item()
                world.remove(self)