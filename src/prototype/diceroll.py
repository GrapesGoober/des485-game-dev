import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random

SIZE = 20, 20
COLOR = (0, 255, 0)

class DiceRoll(GameObject):
    def __init__(self, position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.sprite.position = position

        # Test Dice
        self.walk_step = 5
        self.can_walk = True
        self.start_time = None 

    # Test Dice 
    def random_walk_step(self):
        self.walk_step = random.randint(1, 6)
        self.start_time = pygame.time.get_ticks()  
        print("--------- Diceroll Regenerated walk step: ", self.walk_step)

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        
        if self.walk_step == 0:
            self.can_walk = False

        if not self.can_walk and self.walk_step == 0: 
            if self.start_time is None:
                self.start_time = pygame.time.get_ticks()
            
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.start_time) / 1000 
            print(f"DiceRoll Count to 4 before unfreezing rat: ", elapsed_time)

            if elapsed_time >= 4:
                self.random_walk_step() 
                self.can_walk = True 
                self.start_time = None            
