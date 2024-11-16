import pygame
from typing import Any
from lib import Frame, GameObject, World, Sprite

from src.prototype.cat import Cat
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

    def on_update(self, world: 'World', frame: Frame):
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

        self.item = item

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)
    
    def on_update(self, world: World, frame: Frame):
        if self.item.player.inventory.has_item(TunaCanInventoryGUI):
            self.sprite.position = self.item.player.inventory.get_item_gui_position(self)
        else:
            # Remove item gui from world
            world.remove(self)

class TunaCanGUI(GameObject):
    """
    A TunaCanGUI for asking the player if they want to use the tuna can.
    """

    def __init__(self, **metadata: Any) -> None:

        super().__init__()
        
        # Set metadata
        self.player: Rat = metadata['player']
        self.cat: Cat = metadata['cat']

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface((400, 100))
        self.sprite.src_image.fill((255, 255, 255))

        font = pygame.font.Font("src/fonts/Pixuf.ttf", 24)
        text_surface = font.render("Do you want to use the tuna can?", True, (0, 0, 0))  # Text color is black for visibility
        self.sprite.src_image.blit(text_surface, (10, 10))

        text_surface = font.render("[Y] Yes", True, (0, 0, 0))
        self.sprite.src_image.blit(text_surface, (10, 50))

        text_surface = font.render("[N] No", True, (0, 0, 0))
        self.sprite.src_image.blit(text_surface, (100, 50))

        # Set sprite position: middle-bottom of the scene
        sprite_width, sprite_height = self.sprite.src_image.get_size()
        self.sprite.position = ((1280 - sprite_width) // 2, 720 - sprite_height - 20)
        
        self.is_used = False

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:

        # Player cannot walk
        self.player.diceroll.can_walk = False

        if not self.is_used:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_y]:
                print("Player: Tuna can used")

                # Remove tuna can gui from world
                world.remove(self)

                # Remove cat from world
                world.remove(self.cat)

                # Remove item gui from inventory
                for item in self.player.inventory.items:
                    if isinstance(item, TunaCanInventoryGUI):
                        self.player.inventory.items.remove(item)

                # Player can walk again
                self.player.diceroll.can_walk = True

                # Set tuna can as used
                self.is_used = True

            elif pressed_key[pygame.K_n]:
                print("Player: Get eaten")

                # Player get eaten
                self.player.get_eaten(world)

                # Remove tuna can gui from world
                world.remove(self)

                # Remove cat from world
                world.remove(self.cat)

                # Player can walk again
                self.player.diceroll.can_walk = True

                self.is_used = True
