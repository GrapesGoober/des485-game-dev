from typing import Any
import pygame
from lib import Frame, GameObject, World, Sprite
from src.prototype.inventory import InventoryGUI
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 20, 20
COLOR = (0, 255, 100)

IMAGE = pygame.Surface(SIZE)
IMAGE.fill(COLOR)

class Nut(GameObject):
    def __init__(self, player: Rat, inventory: InventoryGUI, grid_position: tuple[int, int]) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = IMAGE
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]
        self.position = GridPosition(grid_position)
        self.player: Rat = player
        self.inventory: InventoryGUI = inventory
        self.is_picked = False

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)

    def on_remove(self, world):
        world.sprites.remove(self.sprite)

    
    def on_update(self, world: World, frame: Frame) -> None:

        if self.is_picked == False:
            # check player collision 
            for n in self.position.get_neighbours(world):
                if n.parent_object == self.player: 

                    self.is_picked = True 
                    print("----------------")
                    print("nut_counter b4 collision", self.player.nut_counter)
                    
                    self.player.nut_counter += 1 #update nut_counter in rat.py
                    world.remove(self) # remove itself from world

                    print("Nut collided")
                    print("nut_counter after collision: ", self.player.nut_counter)
                    print("Bye world")

        # if self.is_picked == True:
        #     # the inventory GUI will figure what coordinate to pose as
        #     self.sprite.position = self.inventory.get_item_gui_position(self)
        #     # right now, as a place holder, just use space bar
        #     # realistically, use mouse position
        #     if pygame.key.get_pressed()[pygame.K_SPACE]:
        #         print("hi, using item")
        #         print(f"i have the player here {self.player} what should I do with it?")
        #         world.remove(self)
