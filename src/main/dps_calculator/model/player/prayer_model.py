from enum import Enum

class PrayerBonuses(Enum):
    """Class that represents Prayers and their respective multipliers."""
    BURST_OF_STRENGTH = 1.05
    SUPERHUMAN_STRENGTH = 1.1
    ULTIMATE_STRENGTH = 1.15
    CHIVALRY = 1.18
    PIETY = 1.23

class Prayer():
    """A class that represents the prayer tab.

    Attributes:
    active_prayer_bonuses (list): A list containing the active prayer bonuses of the player.
    """
    def __init__(self,):
        self.active_prayer_bonuses = list()
