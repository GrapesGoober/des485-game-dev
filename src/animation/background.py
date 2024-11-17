import pygame
from lib import Frame, GameObject, Sprite, World
from src.animation_loop import AnimationLoop
from src.get_sprites_list import get_sprites_list

bg_SHEET = pygame.image.load('src\\images\\Grass_field_map2.png')
background = bg_SHEET.subsurface((0, 0), (240, 160))