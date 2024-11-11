import pygame
from lib import Frame, GameObject, World, Sprite

ITEM_GUI_HEIGHT = 100

class InventoryGUI(GameObject):
    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position
        self.items = World()
        self.screen: pygame.Surface = None

    def on_create(self, world: World) -> None:
        self.screen = pygame.display.get_surface()

    def on_update(self, world: World, frame: Frame) -> None:
        self.items.update(frame.events, frame.dt)
        self.items.draw(self.screen)

    def add_item_gui(self, item: GameObject) -> None:
        self.items.add(item)
    
    def get_item_gui_position(self, item: GameObject) -> tuple[int, int]:
        x = self.position[0]
        y = self.position[1] + self.items.gameobjects.index(item) * ITEM_GUI_HEIGHT
        return x, y
