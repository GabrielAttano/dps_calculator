from model.items.equipment_model import Bonuses, Equipment, OtherBonuses, Slots
from model.player.player_model import Player
from model.combat.style_model import AttackType
from service.items.equipment_service import BonusesService, EquipmentService


class GearService:
    """A class that provides methods to gear."""
    @classmethod
    def get_gear(cls, player: Player, slot: Slots):
        return player.gear.equipments[slot.name]

    @classmethod
    def equip_item(cls, player: Player, item_to_equip: Equipment):
        """Equip an item to its corresponding slot.

        Args:
            player (Player): The player that is going to equip the equipment.
            item_to_equip (Equipment): The item that it's going to be equipped.

        Returns:
            Equipment: Returns the equipment that was in that slot.
        """

        old_item: Equipment = cls.get_gear(player, item_to_equip.slot)
        player.gear.equipments[item_to_equip.slot.name] = item_to_equip
        player.gear.total_gear_bonuses = cls.__calculate_total_gear_bonuses(player)
        return old_item

    @classmethod
    def unequip_item(cls, player: Player, slot_to_unequip: Slots):
        """Unequips an item from the player gear.

        Args:
            player (Player): The player that is going to unequip the item.
            slot_to_unequip (Slots): the slot where the equipment is.

        Returns:
            Equipment: Returns the equipment that was in that slot.
        """

        old_item: Equipment = player.gear.equipments[slot_to_unequip.name]
        player.gear.equipments[slot_to_unequip.name] = EquipmentService.create_empty_equipment(slot_to_unequip)
        player.gear.total_gear_bonuses = cls.__calculate_total_gear_bonuses(player)
        return old_item

    @classmethod
    def get_gear_attack_type_bonus(cls, player: Player, attack_type: AttackType):
        """Get the total gear attack bonus for a specific attack type.

        Args:
            player (Player): The player to get the gear bonus from.
            attack_type (AttackType): The attack type that is going to be checked.

        Returns:
            int: The value of the total gear attack bonus for the specified attack type.
        """

        total_attack_bonuses: Bonuses = player.gear.total_gear_bonuses["total_attack_bonuses"]

        if attack_type == AttackType.STAB:
            return total_attack_bonuses.stab
        if attack_type == AttackType.SLASH:
            return total_attack_bonuses.slash
        if attack_type == AttackType.CRUSH:
            return total_attack_bonuses.crush

    @classmethod
    def get_gear_defence_type_bonus(cls, player: Player, attack_type: AttackType):
        """Get the total gear defence bonus for a specific attack type.

        Args:
            player (Player): The player to get the gear bonus from.
            attack_type (AttackType): The attack type that is going to be checked.

        Returns:
            int: The value of the total gear defence bonus for the specified attack type.
        """

        total_defence_bonuses: Bonuses = player.gear.total_gear_bonuses["total_defence_bonuses"]

        if attack_type == AttackType.STAB:
            return total_defence_bonuses.stab
        if attack_type == AttackType.SLASH:
            return total_defence_bonuses.slash
        if attack_type == AttackType.CRUSH:
            return total_defence_bonuses.crush

    @classmethod
    def __calculate_total_gear_bonuses(cls, player: Player):
        """Returns the total bonuses given by the player gear.

        Args:
            player (Player): The player that is going to be used for the calculation. Its
            gear is used for it.

        Returns:
            dict: Returns a dictionary containing the keys 'total_attack_bonuses', 
            'total_defence_bonuses' and 'total_other_bonuses' with their respective values.
        """

        total_attack_bonuses = Bonuses()
        total_defence_bonuses = Bonuses()
        total_other_bonuses = OtherBonuses()
        for key, value in player.gear.equipments.items():
            total_attack_bonuses = BonusesService.add_bonuses(total_attack_bonuses, value.attack_bonuses)
            total_defence_bonuses = BonusesService.add_bonuses(total_defence_bonuses, value.defence_bonuses)
            total_other_bonuses = BonusesService.add_other_bonuses(total_other_bonuses, value.other_bonuses)

        return dict({
            "total_attack_bonuses": total_attack_bonuses,
            "total_defence_bonuses": total_defence_bonuses,
            "total_other_bonuses": total_other_bonuses
            })