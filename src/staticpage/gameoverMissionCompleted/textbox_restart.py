import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list
from typing import Callable


FONT_SIZE = 70  # Large font size
TEXT = "Press enter to play again"  # Text to display
TEXT_COLOR = (255, 255, 255)  # White color
BACKGROUND_COLOR = (200, 200, 50)  # Black background
SIZE = 1280, 720

class TextRestart(GameObject):
    def __init__(self, callback: Callable) -> None:
        self.sprite = None 
        # self.position = GridPosition(grid_position)
        # self.position.parent_object = self
        self.text_surface = None  
        self.text_rect = None  
        self.callback: Callable = callback

    def on_create(self, world: World) -> None:
        pass

    def on_remove(self, world: World) -> None:
        # world.sprites.remove(self.sprite)
        # world.remove(self.position)
        pass

    def on_update(self, world: World, frame: Frame) -> None:
        screen = (pygame.display.get_surface())
        font = pygame.font.Font(None, FONT_SIZE)
        text_surface = font.render(TEXT, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 + 50))
        screen.blit(text_surface, text_rect)    

        for event in frame.events:
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN:
                    self.callback()