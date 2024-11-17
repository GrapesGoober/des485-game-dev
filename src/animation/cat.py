import pygame
from lib import Frame, GameObject, Sprite, World
from src.animation_loop import AnimationLoop
from src.get_sprites_list import get_sprites_list

cat_SHEET = pygame.image.load('src\\images\\Cat Sprite.png')

cat = cat_SHEET.subsurface((32, 0), (16, 16))
cat_idle = pygame.transform.scale(cat, (48, 48))

cat_jump_down = get_sprites_list(cat_SHEET, (16, 16), (3, 3), slice=(0, 2), interval_time = 0.5)
cat_jump_right = get_sprites_list(cat_SHEET, (16, 16), (3, 3), slice=(4, 6), interval_time = 0.5)
cat_jump_up = get_sprites_list(cat_SHEET, (16, 16), (3, 3), slice=(8, 10), interval_time = 0.5)
cat_jump_left = get_sprites_list(cat_SHEET, (16, 16), (3, 3), slice=(12, 14), interval_time = 0.5)

cat_confused_down_tiles = [get_sprites_list(cat_SHEET, (16, 16), (5, 5), interval_time = 0.5)[i] for i in [0, 1, 2, 8, 9]]
cat_confused_down = [pygame.transform.scale(tile, (48, 48)) for tile in cat_confused_down_tiles]

cat_confused_right_tiles = [get_sprites_list(cat_SHEET, (16, 16), (5, 5), interval_time = 0.5)[i] for i in [4, 5, 6, 12, 13]]
cat_confused_right = [pygame.transform.scale(tile, (48, 48)) for tile in cat_confused_right_tiles]

cat_confused_up_tiles = [get_sprites_list(cat_SHEET, (16, 16), (5, 5), interval_time = 0.5)[i] for i in [8, 9, 10, 0, 1]]
cat_confused_up = [pygame.transform.scale(tile, (48, 48)) for tile in cat_confused_up_tiles]

cat_confused_left_tiles = [get_sprites_list(cat_SHEET, (16, 16), (5, 5), interval_time = 0.5)[i] for i in [12, 13, 14, 4, 5]]
cat_confused_left = [pygame.transform.scale(tile, (48, 48)) for tile in cat_confused_left_tiles]