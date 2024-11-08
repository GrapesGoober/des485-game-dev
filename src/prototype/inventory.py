import pygame
from lib import Frame, GameObject, World, Sprite

class Inventory(GameObject):
    def __init__(self, position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.items: list[tuple[Sprite, function]] = []

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    def on_update(self, world: World, frame: Frame) -> None:
        # check mouse click onto item
        mouse_x, mouse_y = pygame.mouse.get_pos()
        ...

        # right now, as a place holder, just use space bar
        for s, on_item_use in self.items:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                on_item_use()

    def add_item(self, sprite: Sprite, on_item_use: 'function') -> None:
        self.items.append((sprite, on_item_use))
        # also, re-adjust item position