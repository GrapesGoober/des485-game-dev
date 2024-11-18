import pygame
from typing import Any
from lib import Frame, GameObject, World, Sprite

from src.prototype.cat import Cat
from src.grid_position import GridPosition
from src.prototype.tree import Tree
from src.prototype.rat import Rat, RatStates

SIZE = 64, 64
ITEM_NUT_COST = 10

NUT_SIZE = 32, 32
ITEM_NUT_COST = 10
TEXT_COLOR = (255, 255, 255)
COST_SPRITES_OFFSET = 60, 20

NUT_IMAGE = pygame.transform.scale(
    pygame.image.load("src/images/items/nut.png"),
    NUT_SIZE
)

FONT = pygame.font.Font("src/fonts/Pixuf.ttf", 30) 

class HammerShopGUI(GameObject):
    """
    A Hammer object in the game world. Inherits from GameObject.

    Effects: Check if the tree has a cat on it.
    Condition: The player can use the hammer to check if the tree has a cat on it by dragging the hammer item to the tree.
    """

    def __init__(self, player: Rat, position: tuple[int, int]) -> None:

        # Set metadata
        self.player: Rat = player

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/items/hammer.png"),
            SIZE
        )
        self.sprite.position = position

        self.nut_sprite = Sprite()
        self.nut_sprite.src_image = NUT_IMAGE
        self.nut_sprite.x += position[0] + COST_SPRITES_OFFSET[0]
        self.nut_sprite.y += position[1] - COST_SPRITES_OFFSET[1]
        self.cost_sprite = Sprite()
        self.cost_sprite.x += position[0] + COST_SPRITES_OFFSET[0]
        self.cost_sprite.y += position[1] + COST_SPRITES_OFFSET[1]
        self.cost_sprite.src_image = FONT.render(str(ITEM_NUT_COST), True, TEXT_COLOR)

    def on_create(self, world: 'World'):
        world.sprites.add(self.sprite, self.nut_sprite, self.cost_sprite)

    def on_remove(self, world: 'World'):
        world.sprites.remove(self.sprite, self.nut_sprite, self.cost_sprite)

    def on_update(self, world, frame):

        for s in [self.sprite, self.nut_sprite, self.cost_sprite]:
            if self.player.nut_counter < ITEM_NUT_COST:
                s.src_image.set_alpha(100)
            if self.player.nut_counter >= ITEM_NUT_COST:
                s.src_image.set_alpha(256)

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
                    self.player.nut_counter -= ITEM_NUT_COST

                    # Play sound
                    pygame.mixer.Sound.play(pygame.mixer.Sound('src/sound/shop_buy.mp3'))

                    # Add item to inventory
                    item_gui = HammerInventoryGUI(self)
                    world.add(item_gui)
                    self.player.inventory.add_item_gui(item_gui)


class HammerInventoryGUI(GameObject):
    """
    A HammerInventoryGUI for displaying the hammer in the inventory.
    """

    def __init__(self, item: HammerShopGUI) -> None:
        super().__init__()

        self.item = item

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = item.sprite.src_image.copy()

        # Dragging state
        self.is_dragging = False

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: 'World', frame: Frame):
        
        # Update position
        if not self.is_dragging:
            self.sprite.position = self.item.player.inventory.get_item_gui_position(
                self)
            
        self.sprite.src_image.set_alpha(100)
        if self.item.player.current_state == RatStates.USE_ITEM:
            self.sprite.src_image.set_alpha(255)
            for e in frame.events:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                in_bounds = (
                    mouse_x > self.sprite.x - SIZE[0] and
                    mouse_x < self.sprite.x + SIZE[0] and
                    mouse_y > self.sprite.y - SIZE[1] and
                    mouse_y < self.sprite.y + SIZE[1]
                )

                if e.type == pygame.MOUSEBUTTONDOWN and in_bounds:

                    if in_bounds:
                        self.is_dragging = True

                elif e.type == pygame.MOUSEMOTION:
                    if self.is_dragging:
                        # Item sprite follow mouse
                        self.sprite.x = mouse_x
                        self.sprite.y = mouse_y

                elif e.type == pygame.MOUSEBUTTONUP:

                    self.is_dragging = False
                    mouse_grid_position = (mouse_x // SIZE[0], mouse_y // SIZE[1])

                    for n in GridPosition.get_objects_at(world, mouse_grid_position):
                        if isinstance(n.parent_object, Tree):

                            tree = n.parent_object
                            if tree.has_cat:
                                # draw that there's a cat, confused
                                cat = Cat(tree.player, tree.position.grid_position)
                                world.add(cat)
                                cat.become_confused()
                                # Player can walk again
                                tree.player.current_state = RatStates.WALK_END

                            # Play sound
                            pygame.mixer.Sound.play(pygame.mixer.Sound('src/sound/toy_hammer.mp3'))

                            # Remove Hammer gui from world
                            self.item.player.inventory.remove_item_gui(self)
                            world.remove(self)

                            # hammer can use for only one tree, so break loop
                            break
