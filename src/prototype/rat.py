import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random
from src.prototype.diceroll import DiceRoll

SIZE = 20, 20
COLOR = (255, 255, 255)

class Rat(GameObject):
    def __init__(self, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.position = GridPosition(grid_position)
        self.position.parent_object = self

        # Test Dice
        self.diceroll = DiceRoll([5, 5])

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)
        world.remove(self.position)

    def on_update(self, world: World, frame: Frame) -> None:
        next_x, next_y = self.position.grid_position
        
        if self.diceroll.walk_step == 0:
            self.diceroll.can_walk = False
            self.diceroll.on_update(world, frame)
        for event in frame.events:
            # Test Dice
            if event.type == pygame.KEYDOWN:
                if self.diceroll.can_walk and self.diceroll.walk_step != 0:    
                    match event.key:
                        case pygame.K_w: next_y -= 1
                        case pygame.K_a: next_x -= 1
                        case pygame.K_s: next_y += 1
                        case pygame.K_d: next_x += 1

                    self.diceroll.walk_step -= 1 
                    print("rat remaining walk_step ", self.diceroll.walk_step)     

        if not GridPosition.has_objects_at(world, (next_x, next_y)):
            self.position.grid_position = (next_x, next_y)

        self.sprite.x = self.position.grid_x * SIZE[0]
        self.sprite.y = self.position.grid_y * SIZE[1]
