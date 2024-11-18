import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list


FONT_SIZE = 100  
TEXT = "Game Over"  
TEXT_COLOR = (255, 255, 255)  
SIZE = 1280, 720

class TextGameOver(GameObject):
    def __init__(self) -> None:
        self.sprite = None 
        self.text_surface = None  
        self.text_rect = None  

    def on_create(self, world: World) -> None:
        pass

    def on_remove(self, world: World) -> None:
        pass

    def on_update(self, world: World, frame: Frame) -> None:
        screen = (pygame.display.get_surface())
        font = pygame.font.Font(None, FONT_SIZE)
        text_surface = font.render(TEXT, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2))
        screen.blit(text_surface, text_rect)    