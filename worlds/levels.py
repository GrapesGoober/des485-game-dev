from src.prototype.shop import Shop
from src.prototype.level_manager import LevelManager
from src.prototype.items.cheese import Cheese
from src.prototype.inventory import InventoryGUI
from src.prototype.items.test_item import TestItemProp
from src.prototype.rat import Rat
from src.prototype.tree import Tree
from src.prototype.rock import Rock

from src.prototype.items.RatHole import RatHole
from src.prototype.items.Star import Star
from src.prototype.items.Rainbow import Rainbow
from src.prototype.items.Nut import Nut

def create_level_test_1(player: Rat, inventory_gui: InventoryGUI, level_manager: LevelManager):
    return [
        Tree(player, (6, 6), False),
        Tree(player, (7, 7), False),
        Tree(player, (8, 8), True),
        Rock(player, (5, 12)),
        Cheese(
            player, 
            callback= lambda: level_manager.transition(
                create_level_test_2(player, inventory_gui)
            ), 
            grid_position=(20, 20)
        ),

        Star(player=player, grid_position=(10, 12)),
        RatHole(player=player, grid_position=(10, 13)),
        Rainbow(player=player, grid_position=(10, 14)),
        Nut(player=player, grid_position=(10, 15)),
        Nut(player=player, grid_position=(10, 16)),
        Nut(player=player, grid_position=(10, 17)),
        Nut(player=player, grid_position=(10, 18)),
        Shop(player=player, grid_position=(10, 20)),
    ]
    
def create_level_test_2(player: Rat, inventory_gui: InventoryGUI):
    return [
        Tree(player, (9, 19), False),
        Tree(player, (9, 21), False),
        Tree(player, (11, 21), True),
        TestItemProp(player, inventory_gui, (10, 20)),
        TestItemProp(player, inventory_gui, (10, 30)),
        TestItemProp(player, inventory_gui, (10, 40)),
    ]