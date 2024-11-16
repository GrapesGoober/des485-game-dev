
import pygame

class AnimationLoop:
    """
    `AnimationLoop` holds a list of images, and allows you to regularly 
    update to get its current image to be assigned to a sprite's image.

    Methods:
        `reset` reset the animation to default
        `update` progress the animation by `dt`, and returns current image

    Attributes:
        `image_list` a list of pygame surface images
        `interval_time` how long (in seconds) do each image last
        `is_looping` whether or not to loop the animation
        `dt_timer` the timer for the current image
        `index` index of current image
        `is_done` boolean whether the animation is over; if `is_looping`, never `True`
    """
    
    def __init__(self, image_list: list[pygame.Surface], 
            is_looping: bool = True, interval_time: float = 0.15):

        super().__init__()

        self.image_list = image_list
        self.interval_time = interval_time
        self.is_looping = is_looping

        self.dt_timer: float = 0
        self.index: int = 0
        self.is_done: bool = False # whether the animation is over
        # Note: if is_looping, then is_done will never be true

    def reset(self):
        self.dt_timer = 0
        self.index = 0
        self.is_done = False

    def update(self, dt) -> pygame.Surface:
        # one time animation check (attacking)
        if not self.is_done:
            self.dt_timer = self.dt_timer + dt

        if self.dt_timer > self.interval_time:
            self.dt_timer = self.dt_timer % self.interval_time
            self.index += 1 
            self.index = self.index % len(self.image_list)
            
            if self.index == 0 and not self.is_looping: 
                self.is_done = True

        return self.image_list[self.index]