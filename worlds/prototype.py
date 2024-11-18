from lib import World
from src.prototype.item_use_prompt import ItemUsePrompt
from src.prototype.GrassField import GrassField
from src.prototype.items.cheese import Cheese
from src.prototype.rock import Rock
from src.prototype.shop import Shop
from src.prototype.tree import Tree
from src.prototype.items.test_item import TestItemProp, TestItemShopGUI
from src.prototype.inventory import InventoryGUI
from src.prototype.diceroll import DiceRoll
from src.prototype.rat import Rat
from src.prototype.cat import Cat
from src.prototype.bordergrass import BorderGrass
from src.prototype.items.Rainbow import Rainbow
from src.prototype.items.Star import Star
from src.prototype.items.cheese import Cheese
from src.prototype.items.RatHole import RatHole
from src.prototype.items.Nut import Nut


from src.staticpage.startpage.bg_startpage import BackgroundStartPage
from src.staticpage.startpage.textbox_cheesehunter import TextCheeseHunter
from src.staticpage.startpage.textbox_start import TextStart
from src.staticpage.startpage.rat_startpage import RatStartPage

from src.staticpage.gameoverMissionCompleted.bg_gameoverpage import BackgroundGameOverPage
from src.staticpage.gameoverMissionCompleted.textbox_gameover import TextGameOver
from src.staticpage.gameoverMissionCompleted.textbox_restart import TextRestart
from src.staticpage.gameoverMissionCompleted.rat_missioncompleted import RatMissionCompleted
from src.staticpage.gameoverMissionCompleted.cheese_missioncompleted import CheeseMissionCompleted

from src.staticpage.gameoverMissionFailed.bg_gameover_failed import BackgroundGameOverFailPage
from src.staticpage.gameoverMissionFailed.cat_mission_failed import CatMissionFailed

def load_start_screen(world: World):

    world.add(
        BackgroundStartPage(callback= lambda: load_gameplay(world)),
        RatStartPage((13.5, 10))
    )   


def load_gameplay(world: World):

    # clear exisiting items before adding new ones
    world.remove(*world.gameobjects)

    # some objects are needed as dependency
    dice = DiceRoll((1210, 660))
    inventory_gui = InventoryGUI((1180, 100))
    player = Rat(dice=dice, grid_position=(3, 1), inventory=inventory_gui)
    
    tree_params = [
        ((3, 2), False), ((4, 3), False), ((3, 7), False), ((4, 9), False), ((5, 6), False),
        ((5, 5), False), ((6, 8), False), ((6, 6), False), ((6, 3), False), ((6, 2), False),
        ((6, 1), False), ((7, 1), False), ((7, 4), False), ((7, 8), False), ((8, 9), False),
        ((9, 7), False), ((9, 4), False), ((9, 2), False), ((10, 6), False), ((10, 10), False),
        ((11, 10), False), ((11, 3), False), ((12, 7), False), ((12, 1), False), ((13, 3), False),
        ((13, 8), False), ((13, 9), False), ((14, 8), False), ((14, 6), False), ((14, 5), False),
        ((14, 1), False), ((15, 3), False), ((15, 5), False), ((16, 10), False), ((16, 8), False),
        ((17, 4), False), ((17, 1), False)
    ]


    trees = [Tree(player, position, param) for position, param in tree_params]

    border_positions = [
        (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
        (18, 1), (18, 2), (18, 3), (18, 4), (18, 5), (18, 6), (18, 7), (18, 8), (18, 9), (18, 10),
        (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0),
        (14, 0), (15, 0), (16, 0), (17, 0),
        (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11), 
        (13, 11), (14, 11), (15, 11), (16, 11), (17, 11),
        (2, 0), (18, 0), (2, 11), (18, 11)
    ]

    border = [BorderGrass(player, position) for position in border_positions]

    rock_positions = [
        (3, 3), (3, 6), (3, 10), (6, 10), (7, 2), (10, 7), (11, 1), (11, 6), (13, 5), (14, 9), 
        (15, 1), (15, 6), (17, 6)
    ]

    rocks = [Rock(player, position) for position in rock_positions]

    rainbow_positions = [(3, 5), (7, 3), (12, 9)]
    rainbows = [Rainbow(player=player, grid_position=position) for position in rainbow_positions]

    star_positions = [(8, 7), (13, 7), (16, 2)]
    stars = [Star(player=player, grid_position=position) for position in star_positions]

    cheese = Cheese(player, callback= lambda: load_end_screen_mission_completed(world), grid_position= (17, 10))
    # cheese2 = Cheese(player, callback= lambda: load_end_screen_mission_completed(world), grid_position= (8, 3))

    rathole_positions = [(4, 10), (8, 1), (13, 1)]
    ratholes = [RatHole(player=player, grid_position=position) for position in rathole_positions]

    nut_positions = [(4, 8), (7, 5), (8, 10), (13, 2), (15, 8), (17, 5)]
    nuts = [Nut(player=player, grid_position=position) for position in nut_positions]

    shop = Shop(player=player, grid_position=(11, 5))

    cat = Cat(player = player, grid_position = (3, 8), callback= lambda: load_end_screen_mission_failed(world))

    world.add(
        GrassField(grid_position=(13, 8)),
        player,
        *rocks,
        *trees,
        dice,
        inventory_gui,
        # I think the item prompt is clunky
        # Imma remove this for the time being
        # ItemUsePrompt(player),
        *rainbows,
        *stars,
        cheese,
        *ratholes,
        *nuts,
        shop, 
        cat,
        *border
        # *border
    )

def load_end_screen_mission_completed(world: World):
    # clear exisiting items before adding new ones
    world.remove(*world.gameobjects)
    # add whatever gameobject you need here
    world.add(
        BackgroundGameOverPage(callback= lambda: load_gameplay(world)),
        RatMissionCompleted((13, 7)),
        CheeseMissionCompleted((600, 400))
        # TextGameOver(),
        # TextRestart(callback= lambda: load_gameplay(world))
    )   

def load_end_screen_mission_failed(world: World):
    world.remove(*world.gameobjects)
    world.add(
        BackgroundGameOverFailPage(callback= lambda: load_gameplay(world)),
        CatMissionFailed(grid_position = (13, 7))
    )

