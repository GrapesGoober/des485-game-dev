import pygame
from lib import Frame, GameObject, Sprite, World
from src.animation_loop import AnimationLoop

SIZE = 100, 100
WHITE = (255, 255, 255)
RED = (255, 0, 0)

IMG1 = pygame.Surface(SIZE)
IMG1.fill(WHITE)

IMG2 = pygame.Surface(SIZE)
pygame.draw.circle(IMG2, WHITE, (SIZE[0]//2, SIZE[1]//2), SIZE[0]//2)

IMG3 = pygame.Surface(SIZE)
IMG3.fill(RED)

IMG4 = pygame.Surface(SIZE)
pygame.draw.circle(IMG4, WHITE, (SIZE[0]//2, SIZE[1]//2), SIZE[0]//2)

class AnimableObject(GameObject):
    def __init__(self) -> None:
        self.sprite = Sprite()
        self.anim1 = AnimationLoop([IMG1, IMG2, IMG3, IMG4], is_looping=False)

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        self.sprite.src_image = self.anim1.update(frame.dt)
