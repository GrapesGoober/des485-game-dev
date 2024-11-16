import pygame
from typing import Any
from lib import Frame, GameObject, World, Sprite

from src.grid_position import GridPosition
from src.prototype.rat import Rat

SIZE = 20, 20
ITEM_NUT_COST = 1

class TunaCanShopGUI(GameObject):
    """
    A TunaCan object in the game world. Inherits from GameObject.

    Effects: Stun the cat
    Condition: The effect will be triggered once the player going to get eaten by the cat. 
    The prompt will be shown on the screen whether the player want to use the tuna can or not.
    """

    def __init__(self, **metadata: Any) -> None:
        super().__init__(**metadata)

        # Set metadata
        self.player: Rat = metadata['player']

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.image.load("src/images/items/tuna_can.png")
        self.sprite.position = metadata['position']

    def on_create(self, world: 'World'):
        world.sprites.add(self.sprite)

    def on_remove(self, world: 'World'):
        world.sprites.remove(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        for n in self.position.get_neighbours(world):
            if n.parent_object == self.player:
                world.remove(self)

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

                    # Remove nut from player
                    self.player.nut_counter -= 1

                    # Add item to inventory
                    item_gui = TunaCanInventoryGUI(self)
                    world.add(item_gui)
                    self.player.inventory.add_item_gui(item_gui)

class TunaCanInventoryGUI(GameObject):
    """
    A TunaCanInventoryGUI for displaying the tuna can in the inventory.
    """
    
    def __init__(self, item: TunaCanShopGUI) -> None:
        super().__init__()

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = item.sprite.src_image
        self.sprite.position = item.player.inventory.get_item_gui_position(self)

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)
    
    def on_update(self, world: World, frame: Frame):
        pass

class TunaCanGUI(GameObject):
    """
    A TunaCanGUI for asking the player if they want to use the tuna can.
    """

    def __init__(self, **metadata: Any) -> None:

        # size
        self.size = 144, 48
        
        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.player: Rat = metadata['player']

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.image.load("src/images/items/tuna_can_prompt.png")

        # Set sprite position
        self.sprite.x = metadata['grid_position'][0] * self.size[0]
        self.sprite.y = metadata['grid_position'][1] * self.size[1]

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)
        world.remove(self.position)
    
    def on_update(self, world: World, frame: Frame) -> None:
        
        if pygame.key.get_pressed()[pygame.K_y]:
            print("Player: Tuna can used")

            # Remove tuna can from world
            world.remove(self)

        elif pygame.key.get_pressed()[pygame.K_n]:
            print("Player: Get eaten")
            self.player.get_eaten(world)
            world.remove(self)
