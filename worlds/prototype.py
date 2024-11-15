from lib import World
from src.prototype.level_manager import LevelManager
from src.prototype.inventory import InventoryGUI
from src.prototype.diceroll import DiceRoll
from src.prototype.rat import Rat
from src.prototype.nut import Nut
from worlds import levels

def load(world: World):
    dice = DiceRoll((50, 50))
    player = Rat(dice, (5, 5))
    inventory_gui = InventoryGUI((1180, 100))
    nut_test = Nut(player, inventory_gui, (10, 11))

    world.add(
        player,
        dice,
        inventory_gui,
        nut_test
    )

    # start with a test level just for this prototype
    level_manager = LevelManager(world)
    level1 = levels.create_level_test_1(player, inventory_gui, level_manager)
    level_manager.transition(level1)
