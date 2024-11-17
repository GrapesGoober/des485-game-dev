import pygame
from src.animation_loop import AnimationLoop
from lib import Frame, GameObject, World, Sprite
import random

DICE_FACES = [
    (1, pygame.image.load("src/images/dice/1.png")),
    (2, pygame.image.load("src/images/dice/2.png")),
    (3, pygame.image.load("src/images/dice/3.png")),
    (4, pygame.image.load("src/images/dice/4.png")),
    (5, pygame.image.load("src/images/dice/5.png")),
    (6, pygame.image.load("src/images/dice/6.png")),
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

    def roll_dice(self) -> None:
        roll_times = 10
        rolls = [
            random.choice(DICE_FACES) for _ in range(roll_times)
        ]
        self.dice_anim.reset()
        self.dice_anim.image_list = [r[1] for r in rolls]
        self.walk_step = rolls[-1][0]

    def on_update(self, world: World, frame: Frame) -> None:
        self.sprite.src_image = self.dice_anim.update(frame.dt)
        self.can_walk = self.dice_anim.is_done 
