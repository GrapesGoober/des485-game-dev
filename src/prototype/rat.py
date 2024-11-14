import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list
from src.animation_loop import AnimationLoop

SIZE = 20, 20
COLOR = (255, 255, 255)

SHEET = pygame.image.load('src\images\Mouse_Walking_Sprite.png')
SPRITES = get_sprites_list(SHEET, (16, 16), (3, 3))
DOWN_WALK = AnimationLoop(SPRITES[0:4])
RIGHT_WALK = AnimationLoop(SPRITES[8:12])
UP_WALK = AnimationLoop(SPRITES[16:20])
LEFT_WALK = AnimationLoop(SPRITES[24:28])

DOWN_IDLE = AnimationLoop([SPRITES[0]])
RIGHT_IDLE = AnimationLoop([SPRITES[8]])
UP_IDLE = AnimationLoop([SPRITES[16]])
LEFT_IDLE = AnimationLoop([SPRITES[24]])

class Rat(GameObject):
    def __init__(self, dice: DiceRoll, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.position = GridPosition(grid_position)
        self.position.parent_object = self
        self.diceroll: DiceRoll = dice
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
            self.diceroll.walk_step -= 1 
            print("rat remaining walk_step ", self.diceroll.walk_step)     

    def on_update(self, world: World, frame: Frame) -> None:
        
        for event in frame.events:
            # Test Dice
            if event.type == pygame.KEYDOWN:
                if self.diceroll.can_walk:    
                    match event.key:
                        case pygame.K_w: 
                            self.current_anim = UP_WALK
                            self.move(( 0, -1), world)
                        case pygame.K_a: 
                            self.current_anim = LEFT_WALK
                            self.move((-1,  0), world)
                        case pygame.K_s:
                            self.current_anim = DOWN_WALK 
                            self.move(( 0,  1), world)
                        case pygame.K_d:
                            self.current_anim = RIGHT_WALK 
                            self.move(( 1,  0), world)

            else:
                if self.diceroll.walk_step == 0:
                    if self.current_anim == DOWN_WALK: self.current_anim = DOWN_IDLE
                    if self.current_anim == LEFT_WALK: self.current_anim = LEFT_IDLE
                    if self.current_anim == UP_WALK: self.current_anim = UP_IDLE
                    if self.current_anim == RIGHT_WALK: self.current_anim = RIGHT_IDLE

                    
        self.sprite.x = self.position.grid_x * SIZE[0]
        self.sprite.y = self.position.grid_y * SIZE[1]
        self.sprite.src_image = self.current_anim.update(frame.dt)
