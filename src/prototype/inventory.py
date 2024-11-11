import pygame
from lib import Frame, GameObject, World, Sprite

ITEM_GUI_HEIGHT = 100

class InventoryGUI(GameObject):
    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position
        self.items: list[GameObject] = []

    def add_item_gui(self, item: GameObject) -> None:
        self.items.append(item)
    
    def get_item_gui_position(self, item: GameObject) -> tuple[int, int]:
        x = self.position[0]
        y = self.position[1] + self.items.index(item) * ITEM_GUI_HEIGHT
        return x, y
