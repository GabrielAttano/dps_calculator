from enum import Enum, auto
from pprint import pprint
from service.player.level_service import LevelService

class Skills(Enum):
    """A class that represents all the skills."""
    ATTACK = auto()
    DEFENCE = auto()
    STRENGTH = auto()
    HITPOINTS = auto()
    RANGED = auto()
    PRAYER = auto()
    MAGIC = auto()
    COOKING = auto()
    WOODCUTTING = auto()
    FLETCHING = auto()
    FISHING = auto()
    FIREMAKING = auto()
    CRAFTING = auto()
    SMITHING = auto()
    MINING = auto()
    HERBLORE = auto()
    AGILITY = auto()
    THIEVING = auto()
    SLAYER = auto()
    FARMING = auto()
    RUNECRAFTING = auto()
    HUNTER = auto()
    CONSTRUCTION = auto()

class Levels:
    """A class to represent the level of all Skills.

    Attributes:
        __levels (dict): The level of each skill. The keys are (Skills.name) and the values (Int)
    """

    def __init__(self,):
        """Constructs all the skills and their levels
        
        All levels are set to 1.
        """

        self.__levels = dict()
        for skill in Skills:
            self.__levels[skill.name] = 1

        
    def set_level(self, skill: Skills, level, validate_level = False):
        """Set a new level to a specific skill.

        Args:
            skill (Skills): The skill that is going to have the level changed.
            level (int): The new level that is going to be assigned to the specified skill.
            validate_level (bool, optional): Whether is going to check if the specified level is valid.
            or not. Defaults to False.

        Raises:
            ValueError: if validate_level is set to True and the level value is invalid.
        """
        
        if validate_level:
            if LevelService.validate_level(level) == False:
                raise ValueError("can't use value higher than 99 or smaller than 1")
        self.__levels[skill.name] = level
    
    def get_level(self, skill: Skills = None):
        """Get the level of a specific skill.

        Args:
            skill (Skills, optional): The skill that you want to get the level. 
            If not provided, all levels will be returned. Defaults to None.

        Returns:
            dict: If no skill is specified, the __levels attribute 
            of the levels class. The keys are (Skills.name) and the values (Int)
            int: The current level of the specified skill.
        """

        if skill == None:
            return self.__levels
        return self.__levels[skill.name]

    def get_levels(self, ):
        return self.__levels