from enum import Enum
import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
from src.get_sprites_list import get_sprites_list
from src.animation_loop import AnimationLoop

SIZE = 48, 48
COLOR = (255, 255, 255)

SHEET = pygame.image.load('src\images\Mouse_Walking_Sprite.png')
SPRITES = get_sprites_list(SHEET, (16, 16), (10, 10))
DOWN_WALK = AnimationLoop(SPRITES[0:4])
RIGHT_WALK = AnimationLoop(SPRITES[8:12])
UP_WALK = AnimationLoop(SPRITES[16:20])
LEFT_WALK = AnimationLoop(SPRITES[24:28])

DOWN_IDLE = AnimationLoop([SPRITES[0]])
RIGHT_IDLE = AnimationLoop([SPRITES[8]])
UP_IDLE = AnimationLoop([SPRITES[16]])
LEFT_IDLE = AnimationLoop([SPRITES[24]])


class RatMissionCompleted(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)

        # Create grid position
        self.position = GridPosition(grid_position)
        self.position.parent_object = self

        # Create dice roll
        self.current_anim = LEFT_IDLE  
        self.nut_counter: int = 0

        # Set spawn position
        self.spawn_position = self.position.grid_position
        self.rat_animated = True


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
