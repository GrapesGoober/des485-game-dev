import pygame
from lib import Frame, GameObject, Sprite, World
from src.animation_loop import AnimationLoop
from src.get_sprites_list import get_sprites_list

SHEET = pygame.image.load('src\\images\\Mouse_Walking_Sprite.png')
SPRITES = get_sprites_list(SHEET, (16, 16), (3, 3))

class AnimableObject(GameObject):
    def __init__(self) -> None:
        self.sprite = Sprite()
        self.anim1 = AnimationLoop(SPRITES)

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        self.sprite.src_image = self.anim1.update(frame.dt)
