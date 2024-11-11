import pygame
from lib import Frame, GameObject, World, Sprite
from src.grid_position import GridPosition
import random

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
        self.rat_walk = True
        self.walk_step = 5
        self.start_time = pygame.time.get_ticks()  # Start the timer

    # Test Dice 
    def random_walk_step(self):
        self.walk_step = random.randint(1, 6)
        self.start_time = pygame.time.get_ticks()  # Reset the timer for the next countdown
        print("New walk step:", self.walk_step)

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)
        world.remove(self.position)

    def on_update(self, world: World, frame: Frame) -> None:
        next_x, next_y = self.position.grid_position
        for event in frame.events:
            # Test Dice
            if event.type == pygame.KEYDOWN:
                if self.rat_walk and self.walk_step != 0:    
                    match event.key:
                        case pygame.K_w: 
                            next_y -= 1
                            self.walk_step -= 1 
                        case pygame.K_a: 
                            next_x -= 1
                            self.walk_step -= 1
                        case pygame.K_s: 
                            next_y += 1
                            self.walk_step -= 1
                        case pygame.K_d: 
                            next_x += 1
                            self.walk_step -= 1

                if self.walk_step == 0:
                    self.rat_walk = False
                    self.start_time = pygame.time.get_ticks() 

        if not self.rat_walk: 
            # Test Dice: Time logic
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.start_time) / 1000  # time in seconds  
            print("Count to 4 before unfreezing rat ", elapsed_time)
            if elapsed_time >= 4:
                self.random_walk_step()
                print("Regenerated walk step:", self.walk_step)
                self.rat_walk = True

        if not GridPosition.has_objects_at(world, (next_x, next_y)):
            self.position.grid_position = (next_x, next_y)

        self.sprite.x = self.position.grid_x * SIZE[0]
        self.sprite.y = self.position.grid_y * SIZE[1]
