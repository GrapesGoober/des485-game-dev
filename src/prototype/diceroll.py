import pygame
from src.animation_loop import AnimationLoop
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random

def gen_dice_face() -> pygame.Surface:
    f = pygame.Surface((50, 50))
    f.fill((
        random.randrange(100,255), 
        random.randrange(100,255), 
        random.randrange(100,255)
    ))
    return f

DICE_FACES = [
    (1, gen_dice_face()),
    (2, gen_dice_face()),
    (3, gen_dice_face()),
    (4, gen_dice_face()),
    (5, gen_dice_face()),
    (6, gen_dice_face()),
]

class DiceRoll(GameObject):
    def __init__(self, position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.dice_anim = AnimationLoop([], is_looping=False)
        self.sprite.position = position

        # Test Dice
        self.walk_step = 0
        self.can_walk = True

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:

        # ran out of moves => start rolling dice
        if self.walk_step == 0: 
            roll_times = 10
            rolls = [
                random.choice(DICE_FACES) for _ in range(roll_times)
            ]
            self.dice_anim.reset()
            self.dice_anim.image_list = [r[1] for r in rolls]
            self.walk_step = rolls[-1][0]

        self.sprite.src_image = self.dice_anim.update(frame.dt)
        self.can_walk = self.dice_anim.is_done 
