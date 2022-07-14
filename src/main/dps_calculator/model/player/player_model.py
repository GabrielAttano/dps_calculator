from model.player.level_model import Levels
from model.player.prayer_model import Prayer
from model.player.gear_model import Gear
from model.combat.style_model import AttackStyle

class Player:
    """A class to represent a player.
    
    Attributes:
        levels (Levels): The player levels. 
        effective_levels (Levels): the player effective levels.
        prayers (Prayer): The player prayers.
        gear (Gear): The player gear.
        style (AttackStyle): The attack style of the player.
    """

    def __init__(self,):
        """Constructs all the attributes for the Player object."""
        self.levels = Levels()
        self.effective_levels = self.levels
        self.prayers = Prayer()
        self.style = AttackStyle.ACCURATE
        self.gear = Gear()

    def set_levels(self, levels: Levels):
        self.levels = levels

