from lib import World
from src.prototype.tree import Tree
from src.prototype.items.test_item import TestItem
from src.prototype.inventory import InventoryGUI
from src.prototype.diceroll import DiceRoll
from src.prototype.rat import Rat

def load(world: World):
    dice = DiceRoll((50, 50))
    player = Rat(dice, (5, 5))
    inventory_gui = InventoryGUI((1180, 100))

    world.add(
        player,
        dice,
        inventory_gui,
        Tree(player, (6, 6), False),
        Tree(player, (7, 7), False),
        Tree(player, (8, 8), True),
        TestItem(player, inventory_gui, (10, 10)),
    )