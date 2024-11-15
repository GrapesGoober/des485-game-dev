from lib import World
from src.prototype.items.test_item import TestItemShopGUI
from src.prototype.level_manager import LevelManager
from src.prototype.inventory import InventoryGUI
from src.prototype.diceroll import DiceRoll
from src.prototype.rat import Rat
from src.prototype.cat import Cat
from worlds import levels

def load(world: World):
    dice = DiceRoll((50, 50))
    player = Rat(dice, (5, 5))
    inventory_gui = InventoryGUI((1180, 100))
    cat = Cat((30, 2))

    world.add(
        player,
        dice,
        inventory_gui,
        cat
    )

    # start with a test level just for this prototype
    level_manager = LevelManager(world)
    level1 = levels.create_level_test_1(player, inventory_gui, level_manager)
    level_manager.transition(level1)
