from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list
from src.animation_loop import AnimationLoop
from typing import Callable
from src.prototype.rat import Rat 

SIZE = 48, 48
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
    def __init__(self, callback: Callable, **metadata: Any) -> None:

        # Set metadata
        self.player: Rat = metadata['player']
        self.position = GridPosition(metadata['grid_position'])
        self.position.parent_object = self
        self.callback: Callable = callback

        # Create sprite
        self.sprite = Sprite()

        # Create animation
        self.current_anim = DOWN_IDLE

        # Duration
        self.duration = 2000  # 2 seconds in milliseconds
        self.start_time = None  # Timestamp when the Cat is created

    def on_create(self, world: World) -> None:
        self.start_time = pygame.time.get_ticks() 
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

        # current_time = pygame.time.get_ticks()
        # if current_time - self.start_time >= self.duration:
        #     world.remove(self)

        for n in self.position.get_neighbours(world, manhat_dist=1):
            if n.parent_object == self.player:
                print("rat near cat")
                self.callback()


