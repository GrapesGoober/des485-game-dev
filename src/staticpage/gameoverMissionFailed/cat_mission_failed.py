from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list
from src.animation_loop import AnimationLoop
from src.prototype.rat import Rat 

SIZE = 48, 48
COLOR = (255, 255, 255)

SHEET = pygame.image.load('src\images\Cat Sprite.png')
SPRITES = get_sprites_list(SHEET, (16, 16), (10, 10))

CAT = AnimationLoop([SPRITES[0]])

LEFT_JUMP = AnimationLoop(SPRITES[12:14])


class CatMissionFailed(GameObject):
    def __init__(self, **metadata: Any) -> None:

        # Set metadata
        self.position = GridPosition(metadata['grid_position'])
        self.position.parent_object = self

        # Create sprite
        self.sprite = Sprite()

        # Create animation
        self.current_anim = LEFT_JUMP


    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)
        world.remove(self.position)


    def on_update(self, world: World, frame: Frame) -> None:
        self.sprite.x = self.position.grid_x * SIZE[0]
        self.sprite.y = self.position.grid_y * SIZE[1]
        self.sprite.src_image = self.current_anim.update(frame.dt)




