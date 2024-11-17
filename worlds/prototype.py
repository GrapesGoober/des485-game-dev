from lib import World
from src.prototype.items.cheese import Cheese
from src.prototype.items.Nut import Nut
from src.prototype.rock import Rock
from src.prototype.shop import Shop
from src.prototype.tree import Tree
from src.prototype.items.test_item import TestItemProp, TestItemShopGUI
from src.prototype.inventory import InventoryGUI
from src.prototype.diceroll import DiceRoll
from src.prototype.rat import Rat
from src.prototype.cat import Cat
from src.staticpage.startpage.bg_startpage import BackgroundStartPage
from src.staticpage.startpage.textbox_cheesehunter import TextCheeseHunter
from src.staticpage.startpage.textbox_start import TextStart
from src.staticpage.gameoverpage.bg_gameoverpage import BackgroundGameOverPage
from src.staticpage.gameoverpage.textbox_gameover import TextGameOver
from src.staticpage.gameoverpage.textbox_restart import TextRestart

def load_start_screen(world: World):

    world.add(
        BackgroundStartPage(),
        TextCheeseHunter(),
        TextStart(callback= lambda: load_gameplay(world))
    )   


def load_gameplay(world: World):

    # clear exisiting items before adding new ones
    world.remove(*world.gameobjects)

    # some objects are needed as dependency
    dice = DiceRoll((50, 50))
    inventory_gui = InventoryGUI((1180, 100))
    player = Rat(dice=dice, grid_position=(10, 10), inventory=inventory_gui)
    world.add(
        player,
        dice,
        inventory_gui,
        Cat(callback= lambda: load_end_screen(world), player=player, grid_position=(4, 6)),
        Tree(player, (6, 6), False),
        Tree(player, (7, 7), False),
        Tree(player, (8, 8), True),
        Shop(player=player, grid_position=(11, 6)),
        Nut(player=player, grid_position=(11, 7)),
        Rock(player, (11, 8)),
        Cheese(
            player, 
            callback= lambda: load_end_screen(world), 
            grid_position=(13, 6)
        ),
    )

def load_end_screen(world: World):
    # clear exisiting items before adding new ones
    world.remove(*world.gameobjects)
    # add whatever gameobject you need here
    world.add(
        BackgroundStartPage(),
        TextGameOver(),
        TextRestart(callback= lambda: load_gameplay(world))
    )   