
from enum import Enum

class States(Enum):
    """
    Interface enums used by various gameobjects to check current state for when to do certain things.
    The states here is are used as common ground interface, but the implementation logic is built
    separately by various gameobjects.
    """
    START_DICEROLL  : int = 1 # this state tells dice to start rolling
    DURING_DICEROLL : int = 2 # once dice ends, it prompts player to use items
    AFTER_DICEROLL  : int = 3 # prompts player to use every items except TUNA
    MOVE            : int = 4 # tells player it can move, and move only (no item use)
    MOVE_END        : int = 5 # triggers tree's cat check, & prompts TUNA item use       
    CAT_POUNCE      : int = 6 # animation state for cat

current_state = States.START_DICEROLL 
