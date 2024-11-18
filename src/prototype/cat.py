from enum import Enum
from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.rat import Rat, RatStates
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list
from src.animation_loop import AnimationLoop
from typing import Callable
from src.prototype.rat import Rat 

SIZE = 64, 64
COLOR = (255, 255, 255)

SHEET = pygame.image.load('src\images\Cat Sprite.png')
SPRITES = get_sprites_list(SHEET, (16, 16), (4, 4))

CAT = AnimationLoop([SPRITES[0]])


DOWN_JUMP = AnimationLoop(SPRITES[0:3], is_looping=False, interval_time=0.3)
RIGHT_JUMP = AnimationLoop(SPRITES[4:6], is_looping=False, interval_time=0.3)
UP_JUMP = AnimationLoop(SPRITES[8:10], is_looping=False, interval_time=0.3)
LEFT_JUMP = AnimationLoop(SPRITES[12:14], is_looping=False, interval_time=0.3)

DOWN_IDLE = AnimationLoop([SPRITES[0]], is_looping=False, interval_time=0.3)
RIGHT_IDLE = AnimationLoop([SPRITES[4]], is_looping=False, interval_time=0.3)
UP_IDLE = AnimationLoop([SPRITES[8]], is_looping=False, interval_time=0.3)
LEFT_IDLE = AnimationLoop([SPRITES[12]], is_looping=False, interval_time=0.3)
# I'd just use default confused idle
CONFUSED = AnimationLoop([SPRITES[2]], is_looping=False, interval_time=0.5)

class CatStates(Enum):
    IDLE = 1        # show itself in front of tree, using DOWN_JUMP
    WILL_POUNCE = 2 # wait for the idle to finish before start pouncing
    POUNCE = 3      # jump towards player, using proper jump animation
    CONFUSE = 4     # confused, then use UP_JUMP to go behind tree
    RETURN = 5      # return to previous position, then deletes itself

class Cat(GameObject):
    def __init__(self, player: Rat, grid_position: tuple[int, int]) -> None:

        # Set metadata
        self.player: Rat = player
        self.position = GridPosition(grid_position)
        self.initial_position = grid_position
        self.position.parent_object = self

        self.sprite = Sprite()
        self.sprite.layer = 6
        self.current_anim: AnimationLoop = DOWN_IDLE
        self.current_state = CatStates.IDLE

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

        match self.current_state:
            case CatStates.IDLE: ...
            case CatStates.WILL_POUNCE:
                if self.current_anim.is_done:
                    self.current_state = CatStates.POUNCE
                    self.current_anim.reset()
                    self._jumps_towards(self.player.position.grid_position)
            case CatStates.POUNCE:
                if self.current_anim.is_done:
                    self.current_state = CatStates.RETURN
                    self._jumps_towards(self.initial_position)
                    self.player.get_eaten(world)
            case CatStates.CONFUSE:
                if self.current_anim.is_done:
                    self.current_state = CatStates.RETURN
                    self._jumps_towards(self.initial_position)
            case CatStates.RETURN:
                if self.current_anim.is_done:
                    world.remove(self)

    # show itself in front of tree, using DOWN_JUMP animation
    def show_in_front_of_tree(self) -> None:
        self.current_state = CatStates.IDLE
        self.current_anim = DOWN_JUMP
        self.current_anim.reset()

    # after show: jump towards player, using proper jump animation
    def pounce_player(self) -> None:
        self.current_state = CatStates.WILL_POUNCE
        self.current_anim.reset()

    # internal function to use for jumping animation
    def _jumps_towards(self, to: tuple[int, int]) -> None:
        # defualt to UP_JUMP if no direction found
        self.current_anim = UP_JUMP
        if to[0] < self.position.grid_x:
            self.current_anim = LEFT_JUMP
        if to[0] > self.position.grid_x:
            self.current_anim = RIGHT_JUMP  
        if to[1] < self.position.grid_y:
            self.current_anim = UP_JUMP
        if to[1] > self.position.grid_y:
            self.current_anim = DOWN_JUMP
        self.current_anim.reset()
        self.position.grid_position = to

    def become_confused(self) -> None:
        self.current_state = CatStates.CONFUSE
        self.current_anim = CONFUSED
        self.current_anim.reset()
        