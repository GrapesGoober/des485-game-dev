import pygame
from lib import Frame, GameObject, Sprite, World
from src.animation_loop import AnimationLoop
from src.get_sprites_list import get_sprites_list

mouse_SHEET = pygame.image.load('src\\images\\Mouse_Walking_Sprite.png')

mouse = mouse_SHEET.subsurface((0, 0), (16, 16))
mouse_idle = pygame.transform.scale(mouse, (48, 48))

mouse_walk_down = get_sprites_list(mouse_SHEET, (16, 16), (3, 3), slice=(0, 5), interval_time = 0.15)
mouse_walk_right = get_sprites_list(mouse_SHEET, (16, 16), (3, 3), slice=(8, 12), interval_time = 0.15)
mouse_walk_up = get_sprites_list(mouse_SHEET, (16, 16), (3, 3), slice=(16, 20), interval_time = 0.15)
mouse_walk_left = get_sprites_list(mouse_SHEET, (16, 16), (3, 3), slice=(24, 28), interval_time = 0.15)