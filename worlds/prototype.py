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
    dice = DiceRoll((50, 50))
    inventory_gui = InventoryGUI((1180, 100))
    player = Rat(dice=dice, grid_position=(6, 3), inventory=inventory_gui)
    
    tree_params = [
        ((6, 4), False), # tree1
        ((7, 5), False), # 2
        ((6, 9), False), # 3
        ((7, 11), False), # 4
        ((8, 8), False), # 5
        ((8, 7), False),
        ((9, 10), False),
        ((9, 8), False),
        ((9, 5), False),
        ((9, 4), False),
        ((9, 3), False),
        ((10, 3), False),
        ((10, 6), False),
        ((10, 10), False), # 14
        ((11, 11), False),
        ((12, 9), False),
        ((12, 6), False),
        ((12, 4), False),
        ((13, 8), False),
        ((13, 12), False), # 20
        ((14, 12), False), 
        ((14, 5), False), 
        ((15, 9), False), 
        ((15, 3), False), # 24
        ((16, 5), False), 
        ((16, 10), False),
        ((16, 11), False), # 27
        ((17, 10), False), 
        ((17, 8), False), 
        ((17, 7), False), 
        ((17, 3), False), # 31
        ((18, 5), False),  
        ((18, 7), False),  
        ((19, 12), False),  
        ((19, 10), False),  
        ((20, 6), False), 
        ((20, 3), False), 
    ]
    trees = [Tree(player, position, param) for position, param in tree_params]

    border_positions = [
        (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12),
        (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 11), (21, 12),
        (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2),
        (6, 13), (7, 13), (8, 13), (9, 13), (10, 13), (11, 13), (12, 13), (13, 13), (14, 13), (15, 13), (16, 13), (17, 13), (18, 13), (19, 13), (20, 13),
        (5, 2), (21, 2), (5, 13), (21, 13)

    ]
    border = [BorderGrass(player, position) for position in border_positions]

    rock_positions = [
        (6, 5),(6, 8), (6, 12), (9, 12), (10, 4), (13, 9), (14, 3), (14, 8), (16, 7), (17, 11),
        (18, 3), (18, 8), (20, 8)
    ]
    rocks = [Rock(player, position) for position in rock_positions]

    rainbow_positions = [(6, 7), (10, 5), (15, 11)]
    rainbows = [Rainbow(player=player, grid_position=position) for position in rainbow_positions]

    star_positions = [(11, 9), (16, 9), (19, 4)]
    stars = [Star(player=player, grid_position=position) for position in star_positions]

    cheese = Cheese(player, callback= lambda: load_end_screen_mission_completed(world), grid_position= (20, 12))
    # cheese2 = Cheese(player, callback= lambda: load_end_screen_mission_completed(world), grid_position= (8, 3))

    rathole_positions = [(7, 12), (11, 3), (16, 3)]
    ratholes = [RatHole(player=player, grid_position=position) for position in rathole_positions]

    nut_positions = [(7, 10), (10, 7), (11, 12), (16, 4), (18, 10), (20, 7)]
    nuts = [Nut(player=player, grid_position=position) for position in nut_positions]

    shop = Shop(player=player, grid_position=(14, 7))

    cat = Cat(player = player, grid_position = (6, 10), callback= lambda: load_end_screen_mission_failed(world))

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

