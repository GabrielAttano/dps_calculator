from enum import Enum, auto

class AttackStyle(Enum):
    """Class containing all attack styles."""

    AGGRESSIVE = auto()
    CONTROLLED = auto()
    ACCURATE = auto()
    DEFENSIVE = auto()

class CombatStyle(Enum):
    """Class containing all combat styles."""
    MELEE = auto()
    RANGED = auto()
    MAGIC = auto()

class AttackType(Enum):
    """Class containing all attack types."""
    

    STAB = auto()
    SLASH = auto()
    CRUSH = auto()

