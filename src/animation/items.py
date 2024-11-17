import pygame
from lib import Frame, GameObject, Sprite, World
from src.animation_loop import AnimationLoop
from src.get_sprites_list import get_sprites_list

item_SHEET = pygame.image.load('src\\images\\Items.png')

peanut_coin = item_SHEET.subsurface((0, 0), (16, 16))
p_coin = pygame.transform.scale(peanut_coin, (48, 48))

cheese = item_SHEET.subsurface((16, 0), (16, 16))
c_coin = pygame.transform.scale(cheese, (48, 48))

star = item_SHEET.subsurface((64, 0), (16, 16))
STAR = pygame.transform.scale(star, (48, 48))

rainbow = item_SHEET.subsurface((80, 0), (16, 16))
r_coin = pygame.transform.scale(rainbow, (48, 48))

dirt_hole = item_SHEET.subsurface((16, 16), (16, 16))
d_hole = pygame.transform.scale(dirt_hole, (48, 48))

tuna_can = item_SHEET.subsurface((32, 16), (16, 16))
t_coin = pygame.transform.scale(tuna_can, (48, 48))

toy_hammer = item_SHEET.subsurface((64, 16), (16, 16))
h_coin = pygame.transform.scale(toy_hammer, (48, 48))

heart = item_SHEET.subsurface((80, 16), (16, 16))
HEART = pygame.transform.scale(heart, (48, 48))