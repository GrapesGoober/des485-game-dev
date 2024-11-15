
from src.prototype.level_manager import LevelManager
from src.prototype.items.cheese import Cheese
from src.prototype.inventory import InventoryGUI
from src.prototype.items.test_item import TestItemProp
from src.prototype.rat import Rat
from src.prototype.tree import Tree

def create_level_test_1(player: Rat, inventory_gui: InventoryGUI, level_manager: LevelManager):
    return [
        Tree(player, (6, 6), False),
        Tree(player, (7, 7), False),
        Tree(player, (8, 8), True),
        TestItemProp(player, inventory_gui, (10, 8)),
        Cheese(
            player, 
            callback= lambda: level_manager.transition(
                create_level_test_2(player, inventory_gui)
            ), 
            grid_position=(20, 20)
        ),
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