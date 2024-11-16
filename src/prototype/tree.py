import random
import pygame
from lib import Frame, GameObject, World, Sprite

from src.prototype.items.TunaCan import TunaCanGUI, TunaCanInventoryGUI
from src.prototype.cat import Cat
from src.prototype.rat import Rat
from src.grid_position import GridPosition

SIZE = 20, 20
COLOR = (255, 255, 255)

class Tree(GameObject):
    def __init__(self, player: Rat, grid_position: tuple[int, int], has_cat: bool) -> None:
        self.sprite = Sprite()
        self.sprite.src_image = pygame.Surface(SIZE)
        self.sprite.src_image.fill(COLOR)
        self.sprite.x = grid_position[0] * SIZE[0]
        self.sprite.y = grid_position[1] * SIZE[1]

        # Set grid position
        self.position = GridPosition(grid_position)
        self.position.parent_object = self

        self.has_cat: bool = has_cat
        self.player: Rat = player

    def on_create(self, world: World) -> None:
        world.sprites.add(self.sprite)
        world.add(self.position)

    def on_remove(self, world: World) -> None:
        world.sprites.remove(self.sprite)
        world.remove(self.position)

    def on_update(self, world: World, frame: Frame) -> None:
        for n in self.position.get_neighbours(world, manhat_dist=1):
            if n.parent_object == self.player and self.has_cat:
                print("Tree: Has cat")

                # Create a new cat at the tree's position
                cat = Cat(player=self.player, grid_position=self.position.grid_position)
                world.add(cat)

                # Check if the player has a tuna can
                if self.player.inventory.has_item(TunaCanInventoryGUI):
                    print("Tree: Player has tuna can")
                    world.add(TunaCanGUI(player=self.player, grid_position=(3, 6)))
                    
                    # Player move to previous position
                    self.player.position.grid_position = self.player.previous_position
                else:

                    # Player get eaten
                    self.player.get_eaten(world)
