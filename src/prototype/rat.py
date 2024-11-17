import pygame
from lib import Frame, GameObject, World, Sprite
import random

from src.prototype.inventory import InventoryGUI
from src.grid_position import GridPosition
from src.prototype.diceroll import DiceRoll
from src.get_sprites_list import get_sprites_list
from src.animation_loop import AnimationLoop

SIZE = 48, 48
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
    def __init__(self, dice: DiceRoll, grid_position: tuple[int, int], inventory: InventoryGUI) -> None:

        # Create sprite
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)

        # Create grid position
        self.position = GridPosition(grid_position)
        self.position.parent_object = self

        # Create dice roll
        self.diceroll: DiceRoll = dice
        self.current_anim = DOWN_IDLE
        self.nut_counter: int = 0

        # Create inventory
        self.inventory: InventoryGUI = inventory

        # Set spawn position
        self.spawn_position = self.position.grid_position

        # Set health
        self.max_health = 3
        self.health = self.max_health

        # previous position
        self.previous_position = self.position.grid_position

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)
        world.remove(self.position)

    def move(self, amount: tuple[int, int], world: World) -> None:
        self.previous_position = self.position.grid_position
        next_x, next_y = self.position.grid_position
        next_x += amount[0]
        next_y += amount[1]
        
        if not GridPosition.has_objects_at(world, (next_x, next_y)):
            self.position.grid_position = (next_x, next_y)
            self.diceroll.walk_step -= 1

    def get_eaten(self, world: World) -> None:
        self.health -= 1
        if self.health <= 0:

            # Remove the rat from the world
            world.remove(self)

            print("Player: Game Over")
        else:

            print("Player: Get eaten")

            # Reset the rat to the spawn position
            self.position.grid_position = self.spawn_position
            self.diceroll.walk_step = 0

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
