import pygame
from typing import Any
from lib import Frame, GameObject, World, Sprite

from src.prototype.cat import Cat
from src.prototype.rat import Rat, RatStates

SIZE = 64, 64
NUT_SIZE = 32, 32
ITEM_NUT_COST = 7
TEXT_COLOR = (255, 255, 255)
COST_SPRITES_OFFSET = 60, 20

NUT_IMAGE = pygame.transform.scale(
    pygame.image.load("src/images/items/nut.png"),
    NUT_SIZE
)

FONT = pygame.font.Font("src/fonts/Pixuf.ttf", 30) 

class TunaCanShopGUI(GameObject):
    """
    A TunaCan object in the game world. Inherits from GameObject.

    Effects: Stun the cat
    Condition: The effect will be triggered once the player going to get eaten by the cat. 
    The prompt will be shown on the screen whether the player want to use the tuna can or not.
    """

    def __init__(self, player: Rat, position: tuple[int, int]) -> None:
        # Set metadata
        self.player: Rat = player

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/items/tuna_can.png"),
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

    def on_update(self, world: 'World', frame: Frame):
        
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
            self.item.player.inventory.remove_item_gui(self)

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
        
    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:

        # Player cannot walk
        self.player.diceroll.can_walk = False

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_y]:
            print("Player: Tuna can used")

            # Play sound
            pygame.mixer.Sound.play(pygame.mixer.Sound('src/sound/tuna_can_used.mp3'))

            # Remove tuna can gui from world
            world.remove(self)

            # Remove tuna can from inventory
            for item in self.player.inventory.items:
                if isinstance(item, TunaCanInventoryGUI):
                    self.player.inventory.remove_item_gui(item)
                    world.remove(item)

            # Have cat become confused
            self.cat.become_confused()

            # Remove item gui from inventory
            for item in self.player.inventory.items:
                if isinstance(item, TunaCanInventoryGUI):
                    self.player.inventory.items.remove(item)

            # Player can walk again
            self.player.current_state = RatStates.WALK_END

            # Player move to previous position
            self.player.position.grid_position = self.player.previous_position

        elif pressed_key[pygame.K_n]:
            self.cat.pounce_player()
            world.remove(self)
