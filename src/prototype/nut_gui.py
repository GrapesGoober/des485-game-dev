from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite

from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 50, 50

class NutGUI(GameObject):
    def __init__(self, **metadata) -> None:

        # Set metadata
        self.player: Rat = metadata['player']

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load("src/images/items/nut.png"),
            SIZE
        )

    def on_create(self, world: World) -> None:
        pass
        # world.sprites.add(self.sprite)

    def on_remove(self, world):
        pass
        # world.sprites.remove(self.sprite)
    
    def on_update(self, world: World, frame: Frame) -> None:
        # Text 
        FONT_SIZE = 55
        TEXT = str(self.player.nut_counter)
        TEXT_COLOR = (255, 255, 255)
        screen = (pygame.display.get_surface())
        font = pygame.font.Font("src/fonts/Pixuf.ttf", FONT_SIZE)  # Load the custom font
        text_surface = font.render(TEXT, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(topleft=(100, 145))
        screen.blit(text_surface, text_rect)

        # Nut
        screen = pygame.display.get_surface() 
        screen.blit(self.sprite.src_image, (40, 140))

