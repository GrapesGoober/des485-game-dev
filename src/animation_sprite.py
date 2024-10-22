
import pygame
from lib import Sprite

class AnimationSprite(Sprite):
    
    def __init__(self, image_list: list[pygame.Surface], 
            is_looping: bool = True, interval_time: float = 0.15):

        super().__init__()

        self.image_list = image_list
        self.interval_time = interval_time
        self.is_looping = is_looping # whether or not to loop the animation
        self.src_image = self.image_list[0]

        self.dt_timer: float = 0
        self.index: int = 0
        self.is_done: bool = False # whether the animation is over
        # Note: if is_looping, then is_done will never be true

    def reset(self):
        self.dt_timer = 0
        self.index = 0
        self.is_done = False

    def update(self, dt):
        # one time animation check (attacking)
        if self.is_done: return

        self.dt_timer = self.dt_timer + dt

        if self.dt_timer > self.interval_time:
            self.dt_timer = self.dt_timer % self.interval_time
            self.index += 1 
            self.index = self.index % len(self.image_list)
            
            if self.index == 0 and not self.is_looping: 
                self.is_done = True

        self.src_image = self.image_list[self.index]