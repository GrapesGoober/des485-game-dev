import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list
from typing import Callable

SIZE = 1280, 720

class BackgroundGameOverFailPage(GameObject):
    def __init__(self, callback: Callable) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image = pygame.transform.scale(
            pygame.image.load('src\images\gameover_ratgone.png'),
            (1280, 720) 
        )
        self.callback: Callable = callback

    def on_create(self, world: World) -> None:
        pass

    def on_remove(self, world: World) -> None:
        pass

    def on_update(self, world: World, frame: Frame) -> None:    
        screen = pygame.display.get_surface() 
        screen.blit(self.sprite.src_image, (0, 0))
        for event in frame.events:
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN:
                    self.callback()


