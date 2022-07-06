from model.items.equipment_model import Slots, Equipment, Bonuses, OtherBonuses

class BonusesService:
    """A class that provides methods to Bonuses and OtherBonuses."""

    @classmethod
    def create_bonuses(cls, stab, slash, crush, magic, range):
        """Create a Bonuses object with the given stats.

        Args:
            stab (int): The value that stab is going to be set to.
            slash (int): The value that slash is going to be set to.
            crush (int): The value that crush is going to be set to.
            magic (int): The value that magic is going to be set to.
            range (int): The value that range is going to be set to.

        Returns:
            Bonuses: Returns a Bonuses object with the given stats.
        """

        bonuses = Bonuses()
        bonuses.stab = stab
        bonuses.slash = slash
        bonuses.crush = crush
        bonuses.magic = magic
        bonuses.range = range
        return bonuses
    
    @classmethod
    def create_other_bonuses(cls, melee_strength, ranged_strength, magic_damage, prayer):
        """Creates a OtherBonuses object with the given stats.

        Args:
            melee_strength (int): the value that melee_strength is going to be set to.
            ranged_strength (int): the value that ranged_strength is going to be set to.
            magic_damage (float): the value (is a multiplier).
            prayer (int): the value that prayer is going to be set to.

        Returns:
            OtherBonuses: Returns a OtherBonuses object with the given stats.
        """

        other_bonuses = OtherBonuses()
        other_bonuses.melee_strength = melee_strength
        other_bonuses.ranged_strength = ranged_strength
        other_bonuses.magic_damage = magic_damage
        other_bonuses.prayer = prayer
        return other_bonuses

    @classmethod
    def add_bonuses(cls, x: Bonuses, y: Bonuses):
        """Add all the bonuses of two Bonuses objects.

        Args:
            x (Bonuses): Bonuses object to be added.
            y (Bonuses): Bonuses object to be added.

        Returns:
            Bonuses: A bonuses object with the value of its attributes set to the sum of x and y attributes. 
        """

        stab_total = x.stab + y.stab
        slash_total = x.slash + y.slash
        crush_total = x.crush + y.crush
        magic_total = x.magic + y.magic
        range_total = x.range + y.range
        total_bonuses = cls.create_bonuses(stab_total, slash_total, crush_total, magic_total, range_total)
        return total_bonuses

    @classmethod
    def add_other_bonuses(cls, x: OtherBonuses, y: OtherBonuses):
        """Add all the otherBonuses of two OtherBonuses objects.

        Args:
            x (OtherBonuses): OtherBonuses object to add.
            y (OtherBonuses): OtherBonuses object to add.

        Returns:
            OtherBonuses: A otherBonuses object with the value of its attributes set to the sum of x and y attributes.
        """

        melee_strength_total = x.melee_strength + y.melee_strength
        ranged_strength_total = x.ranged_strength + y.ranged_strength
        magic_damage_total = x.magic_damage + y.magic_damage # This is wrong. Since both are multipliers, if we add them up some weird things are going to happen. It should be a list with all multiplier values.
        prayer_total = x.prayer + y.prayer
        total_other_bonuses = cls.create_other_bonuses(melee_strength_total, ranged_strength_total, magic_damage_total, prayer_total)
        return total_other_bonuses

class EquipmentService:
    """A class that provides methods to Equipment."""

    @classmethod
    def create_empty_equipment(cls, slot: Slots):
        """Creates an empty equipment.

        Args:
            slot (Slots): The slot that the equipment is going to be set to.

        Returns:
            Equipment: A Equipment object with its name set to "empty" and bonuses set to 0.
        """

        return Equipment(slot)

    @classmethod
    def create_equipment(cls, slot: Slots, attack_bonuses: Bonuses, defence_bonuses: Bonuses, other_bonuses: OtherBonuses, name):
        """Create a equipment with the specified stats.

        Args:
            slot (Slots): The slot that the equipment is going to be set to.
            attack_bonuses (Bonuses): The equipment attack bonuses.
            defence_bonuses (Bonuses): The equipment defence bonuses.
            other_bonuses (OtherBonuses): The equipment other bonuses.
            name (Str): The equipment name.

        Returns:
            Equipment: A equipment with the specified stats.
        """

        equipment = Equipment(slot, name)
        equipment.attack_bonuses = attack_bonuses
        equipment.defence_bonuses = defence_bonuses
        equipment.other_bonuses = other_bonuses
        return equipment
        