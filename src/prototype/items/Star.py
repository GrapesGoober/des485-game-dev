import pygame
from typing import Any
from src.prototype.inventory import InventoryGUI
from src.grid_position import GridPosition
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat, RatStates

SIZE = 64, 64

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

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/items/star.png"),
            SIZE
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

                print("Player: Star collected")
                world.remove(self)

                # Add item to inventory
                item_gui = StarInventoryGUI(self)
                world.add(item_gui)
                self.player.inventory.add_item_gui(item_gui)

                self.player.nut_counter += 3


    def use_item(self):
        self.player.diceroll.walk_step += 1

class StarInventoryGUI():
    def __init__(self, item: Star) -> None:
        super().__init__()

        self.item = item

        self.sprite = Sprite()
        self.sprite.src_image = item.sprite.src_image.copy()

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        self.sprite.position = self.item.player.inventory.get_item_gui_position(self)

        self.sprite.src_image.set_alpha(100)
        if self.item.player.current_state == RatStates.USE_ITEM:
            self.sprite.src_image.set_alpha(255)
            for e in frame.events:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    in_bounds = (
                        mouse_x > self.sprite.x - SIZE[0] and
                        mouse_x < self.sprite.x + SIZE[0] and
                        mouse_y > self.sprite.y - SIZE[1] and
                        mouse_y < self.sprite.y + SIZE[1]
                    )
                    if in_bounds:
                        self.item.use_item()
                        self.item.player.inventory.remove_item_gui(self)
                        world.remove(self)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

