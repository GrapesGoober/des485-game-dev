import pygame
from typing import Any
from lib import Frame, GameObject, World, Sprite

from src.prototype.cat import Cat
from src.prototype.rat import Rat, RatStates

FONT = pygame.font.Font("src/fonts/Pixuf.ttf", 24)

class ItemUsePrompt(GameObject):
    """
    Prompt telling the player to use item. Will only engage in player state USE_ITEM. 
    When press ENTER, will transition rat state to MOVE. 
    """

    def __init__(self, player: Rat) -> None:

        super().__init__()
        
        self.player: Rat = player

        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface((400, 100))
        self.sprite.src_image.fill((255, 255, 255))
        text_surface = FONT.render(
            "This is time to use your items!", 
            True, 
            (0, 0, 0))
        self.sprite.src_image.blit(text_surface, (10, 10))

        text_surface = FONT.render("[ENTER] Done", True, (0, 0, 0))
        self.sprite.src_image.blit(text_surface, (100, 50))

        sprite_width, sprite_height = self.sprite.src_image.get_size()
        self.sprite.position = ((1280 - sprite_width) // 2, 720 - sprite_height - 20)
        
    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        self.sprite.src_image.set_alpha(0)
        if self.player.current_state == RatStates.USE_ITEM:
            self.sprite.src_image.set_alpha(255)    
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_RETURN]:
                self.player.current_state = RatStates.WALK