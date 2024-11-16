from lib import World
from src.prototype.items.cheese import Cheese
from src.prototype.nut import Nut
from src.prototype.rock import Rock
from src.prototype.shop import Shop
from src.prototype.tree import Tree
from src.prototype.items.test_item import TestItemProp, TestItemShopGUI
from src.prototype.inventory import InventoryGUI
from src.prototype.diceroll import DiceRoll
from src.prototype.rat import Rat
from src.prototype.cat import Cat

def load_gameplay(world: World):

    # clear exisiting items before adding new ones
    world.remove(*world.gameobjects)

    # some objects are needed as dependency
    dice = DiceRoll((50, 50))
    player = Rat(dice, (5, 5))
    inventory_gui = InventoryGUI((1180, 100))

    world.add(
        player,
        dice,
        inventory_gui,
        Cat((30, 2)),
        Tree(player, (6, 6), False),
        Tree(player, (7, 7), False),
        Tree(player, (8, 8), True),
        Shop(player, inventory_gui, (13, 6)),
        TestItemProp(player, inventory_gui, (10, 8)),
        Nut(player, inventory_gui, (10, 11)),
        Rock(player, (5, 12)),
        Cheese(
            player, 
            callback= lambda: load_end_screen(world), 
            grid_position=(20, 20)
        ),
    )

def load_end_screen(world: World):
    # clear exisiting items before adding new ones
    world.remove(*world.gameobjects)
    # add whatever gameobject you need here