from enum import Enum, auto

class Slots(Enum):
    """A class that represents all the slots that a equipment can be equipped to"""

    HEAD_SLOT = auto()
    CAPE_SLOT = auto()
    NECK_SLOT = auto()
    AMMUNITION_SLOT  = auto()
    WEAPON_SLOT = auto()
    SHIELD_SLOT = auto()
    BODY_SLOT = auto()
    LEGS_SLOT = auto()
    HANDS_SLOT = auto()
    FEET_SLOT = auto()
    RING_SLOT = auto()

class Bonuses:
    """A class to represent all possible bonuses.
    
    Attributes:
        stab (int): Stab bonus value.
        slash (int): slash bonus value.
        crush (int): crush bonus value.
        magic (int): magic bonus value.
        range (int): range bonus value.

    """

    def __init__(self,):
        self.stab = int()
        self.slash = int()
        self.crush = int()
        self.magic = int()
        self.range = int()

class OtherBonuses:
    """A class to represent all possible other bonuses.
    
    Attributes: 
    melee_strength (int): melee_strength bonus value.
    ranged_strength (int): ranged_strength bonus value.
    magic_damage (float): magic_damage bonus value.
    prayer (int): prayer bonus value.

    """

    def __init__(self,):
        self.melee_strength = int()
        self.ranged_strength = int()
        self.magic_damage = float()
        self.prayer = int()

class Equipment:
    """A class to represent a equipment.

    Attributes:
        name (Str): The equipment name.
        slot (Slots): The equipment slot.
        attack_bonuses (Bonuses): The equipment attack bonuses.
        defence_bonuses(Bonuses): The equipment defence bonuses
        other_bonuses(OtherBonuses): The equipment other bonuses.
    """

    def __init__(self, slot: Slots, equipment_name = "empty"):
        """Construct all attributes for the equipment.

        Args:
            slot (Slots): The slot that the equipment is going to be used.
            equipment_name (str, optional): The equipment name. Defaults to "empty".
        """
        
        self.name = equipment_name
        self.slot = slot
        self.attack_bonuses = Bonuses()
        self.defence_bonuses = Bonuses()
        self.other_bonuses = OtherBonuses()