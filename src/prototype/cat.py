from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list
from src.animation_loop import AnimationLoop

SIZE = 20, 20
COLOR = (255, 255, 255)

SHEET = pygame.image.load('src\images\Cat Sprite.png')
SPRITES = get_sprites_list(SHEET, (16, 16), (3, 3))

CAT = AnimationLoop([SPRITES[0]])


DOWN_JUMP = AnimationLoop(SPRITES[0:3])
RIGHT_JUMP = AnimationLoop(SPRITES[5:7])
UP_JUMP = AnimationLoop(SPRITES[10:12])
LEFT_JUMP = AnimationLoop(SPRITES[15:17])

DOWN_IDLE = AnimationLoop([SPRITES[0]])
RIGHT_IDLE = AnimationLoop([SPRITES[5]])
UP_IDLE = AnimationLoop([SPRITES[10]])
LEFT_IDLE = AnimationLoop([SPRITES[15]])


class Cat(GameObject):
    def __init__(self, **metadata: Any) -> None:

        # Set metadata
        self.player: Rat = metadata['player']
        self.position = GridPosition(metadata['grid_position'])
        self.position.parent_object = self

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)

        # Create animation
        self.current_anim = DOWN_IDLE

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)
        world.remove(self.position)

    def move(self, amount: tuple[int, int], world: World) -> None:
        next_x, next_y = self.position.grid_position
        next_x += amount[0]
        next_y += amount[1]

        if not GridPosition.has_objects_at(world, (next_x, next_y)):
            self.position.grid_position = (next_x, next_y)

    def on_update(self, world: World, frame: Frame) -> None:

        self.sprite.x = self.position.grid_x * SIZE[0]
        self.sprite.y = self.position.grid_y * SIZE[1]
        self.sprite.src_image = self.current_anim.update(frame.dt)
