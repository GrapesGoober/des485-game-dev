import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll

SIZE = 20, 20
COLOR = (255, 255, 255)

class Rat(GameObject):
    def __init__(self, dice: DiceRoll, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.position = GridPosition(grid_position)
        self.position.parent_object = self
        self.diceroll: DiceRoll = dice

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

    def on_update(self, world: World, frame: Frame) -> None:
        
        for event in frame.events:
            # Test Dice
            if event.type == pygame.KEYDOWN:
                if self.diceroll.can_walk:    
                    match event.key:
                        case pygame.K_w: self.move(( 0, -1), world)
                        case pygame.K_a: self.move((-1,  0), world)
                        case pygame.K_s: self.move(( 0,  1), world)
                        case pygame.K_d: self.move(( 1,  0), world)

        self.sprite.x = self.position.grid_x * SIZE[0]
        self.sprite.y = self.position.grid_y * SIZE[1]
