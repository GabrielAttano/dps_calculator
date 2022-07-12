from model.player.player_model import Player
from model.items.equipment_model import Slots, Bonuses, OtherBonuses, Equipment
from model.player.level_model import Skills
from model.player.prayer_model import PrayerBonuses
from service.items.equipment_service import BonusesService, EquipmentService

class PlayerService:
    """A class that provides methods to the Player."""

    @classmethod
    def print_gear(cls, player: Player, ignore_empty= False):
        """Print the name of all equipment currently in the player.

        Args:
            player (Player): The player to print.
            ignore_empty (Bool, optional): Wheter is going to print the empty slots or not. Defaults to False.
        """

        for key, value in player.gear.equipments.items():
            if ignore_empty and value.name == "empty":
                continue
            print(f"====== {key} =====")
            print(value.name)

    @classmethod
    def print_gear_with_stats(cls, player: Player, ignore_empty= False):
        """Print the name and stats of all equipment currently in the player.

        Args:
            player (Player): The player to print.
            ignore_empty (bool, optional): Wheter is going to print the empty slots or not. Defaults to False.
        """
        
        for key, value in player.gear.equipments.items():
            if ignore_empty and value.name == "empty":
                continue
            print(f"====== {key} =====")
            print(value.name)
            attack_bonuses: Bonuses = value.attack_bonuses
            print("< Attack Bonuses >")
            print(f"stab = {str(attack_bonuses.stab)}", end = " | ")
            print(f"slash =  {str(attack_bonuses.slash)}", end = " | ")
            print(f"crush =  {str(attack_bonuses.crush)}", end = " | ")
            print(f"magic =  {str(attack_bonuses.magic)}", end = " | ")
            print(f"range =  {str(attack_bonuses.range)}")
            defence_bonuses: Bonuses = value.defence_bonuses
            print("< Defence Bonuses >")
            print(f"stab = {str(defence_bonuses.stab)}", end = " | ")
            print(f"slash = {str(defence_bonuses.slash)}", end = " | ")
            print(f"crush = {str(defence_bonuses.crush)}", end = " | ")
            print(f"magic = {str(defence_bonuses.magic)}", end = " | ")
            print(f"range = {str(defence_bonuses.range)}")
            other_bonuses: OtherBonuses = value.other_bonuses
            print("< Other Bonuses >")
            print(f"melee_strength = {str(other_bonuses.melee_strength)}", end = " | ")
            print(f"ranged_strength = {str(other_bonuses.ranged_strength)}", end = " | ")
            print(f"magic_damage = {str(other_bonuses.magic_damage)}", end = " | ")
            print(f"prayer = {str(other_bonuses.prayer)}")

    @classmethod
    def level_up_skill(cls, player: Player, skill: Skills):
        """level up a specific skill (adds one to the player level).
        It uses the levels.set_level with validate_level set to true.

        Args:
            player (Player): The player that is going to have its skill leveled up.
            skill (Skills): The skill to be leveled up.
        """

        new_level = player.levels.get_level(skill) + 1
        player.levels.set_level(skill, new_level, validate_level=True)

    @classmethod
    def activate_prayer(cls, player: Player, prayer: PrayerBonuses):
        """Activates a specified prayer to the player. Currently, the player can't have
        more than one prayer up at the same time.

        Args:
            player (Player): The player that is going to activate a prayer.
            prayer (PrayerBonuses): The prayer that is going to be activated.
        """
        
        if len(player.prayers.active_prayer_bonuses) >= 1:
            player.prayers.active_prayer_bonuses.clear()
        player.prayers.active_prayer_bonuses.append(prayer)
