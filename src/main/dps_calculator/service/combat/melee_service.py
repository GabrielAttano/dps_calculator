# For questions about the steps taken, check https://oldschool.runescape.wiki/w/Damage_per_second/Melee

from model.items.equipment_model import OtherBonuses
from model.player.player_model import Player
from model.player.level_model import Skills
from model.combat.style_model import AttackStyle, AttackType
from service.player.prayer_service import PrayerService
from service.player.gear_service import GearService
from service.combat.style_service import AttackStyleService
import math

class MeleeCalculator:
    """A class that provides methods to calculate melee damage."""
    
    @classmethod
    def __calculate_effective_strength(cls, player: Player, void_bonus: bool):
        """Calculates the player effective strength

        Args:
            player (Player): The player to calculate with.
            void_bonus (bool): Whether to calculate the effective strength with void bonus or not.

        Returns:
            int: The value of the effective strength of a player.
        """

        # (Strength level + Strength level boost) * prayer bonus)
        effective_strength = player.effective_levels.get_level(Skills.STRENGTH) * PrayerService.get_prayer_bonus(player.prayers)
        # Round down to nearest integer
        effective_strength = math.trunc(effective_strength)
        # +3 if using the aggressive attack style, +1 if using controlled
        effective_strength += AttackStyleService.get_style_strength_bonus(player.style)
        # +8
        effective_strength += 8
        # Multiply by 1.1 if wearing full melee void
        if void_bonus:
            effective_strength *= 1.1
            # Round down to nearest integer
            effective_strength = math.trunc(effective_strength)
        
        return effective_strength

    @classmethod
    def __calculate_effective_attack(cls, player: Player, void_bonus: bool):
        """Calculates the player effective attack.

        Args:
            player (Player): The player to calculate with.
            void_bonus (bool): Whether to calculate the effective attack with void bonus or not.


        Returns:
            int: The value of the effective attack of a player.
        """

        # (Attack level + Attack level boost) * prayer bonus
        effective_attack = player.effective_levels.get_level(Skills.ATTACK) * PrayerService.get_prayer_bonus(player.prayers)
        # Round down to nearest integer
        effective_attack = math.trunc(effective_attack)
        # +3 if using the accurate attack style, +1 if using controlled
        effective_attack += AttackStyleService.get_style_attack_bonus(player.style)
        # +8
        effective_attack += 8
        # Multiply by 1.1 if wearing full melee void
        if void_bonus:
            effective_attack *= 1.1
            # Round down to nearest integer
            effective_attack = math.trunc(effective_attack)
        
        return effective_attack

    @classmethod
    def calculate_max_hit(cls, player: Player, void_bonus = False):  
        """Calculates the player max hit.

        Args:
            player (Player): The player to calculate the max hit with.
            void_bonus (bool, optional): Whether to calculate the max hit
            with void bonus or not. Defaults to False.

        Returns:
            int: The value of the player max hit.
        """

        # Effective strength level
        effective_strength = cls.__calculate_effective_strength(player, void_bonus)
        # Multiply by (Equipment Melee Strength + 64)
        total_other_bonuses: OtherBonuses = player.gear.total_gear_bonuses["total_other_bonuses"]
        total_melee_strength = total_other_bonuses.melee_strength
        max_hit = effective_strength * (total_melee_strength + 64)
        # Add 320
        max_hit += 320
        # Divide by 640
        max_hit /= 640
        # Round down to nearest integer
        max_hit = math.trunc(max_hit)
        # Multiply by gear bonus >> TO BE IMPLEMENTED
            # If slaying monsters on task while wearing a black mask or slayer helm, gear bonus is 7/6.
            # If killing undead monsters while wearing a salve amulet, gear bonus is 7/6, or 1.2 if 
            # using salve amulet (e) or (ei).
            # Note that these two bonuses DO NOT stack.
            # If attacking another player who has the Protect from Melee prayer active, multiply by 6/10.
            
        return max_hit

    @classmethod
    def calculate_attack_roll(cls, player: Player, attack_type: AttackType):
        """Calculates the player attack roll.

        Args:
            player (Player): The player to calculate with.
            attack_type (AttackType): The attack type used by the player.

        Returns:
            int: The value of the attack roll.
        """

        # Effective attack level * (Equipment Attack bonus + 64)
        attack_roll = cls.__calculate_effective_attack(player, False) * (GearService.get_gear_attack_type_bonus(player, attack_type) + 64)

        # Multiply by gear bonus >> TO BE IMPLEMENTED
            # If slaying monsters on task while wearing a black mask or slayer helm, gear bonus is 7/6.
            # If killing undead monsters while wearing a salve amulet, gear bonus is 7/6, or 1.2 if 
            # using salve amulet (e) or (ei).
            # Note that these two bonuses DO NOT stack.
            # If attacking another player who has the Protect from Melee prayer active, multiply by 6/10.

        # Round down to nearest integer

        return attack_roll

    @classmethod
    def calculate_defence_roll(cls, attack_type: AttackType, player_target: Player = None, target_defence_level = 0, target_style_defence_bonus = 0):
        """Calculates the defence roll. Can be against a player if player_target is set or a monster by
        using its defence level and style defence bonus.

        Args:
            attack_type (AttackType): The attack type that is going to be used.
            player_target (Player, optional): The player that is going to be the target. 
            Defaults to None.
            target_defence_level (int, optional): The target defence level. Should be 
            ignored if player_target is set. Defaults to 0.
            target_style_defence_bonus (int, optional): The target defence bonus against that style. Should
            be ignored if player_target is set. Defaults to 0.

        Returns:
            int: The value of the defence roll.
        """

        if player_target != None:
            defence_roll = player_target.effective_levels.get_level(Skills.DEFENCE)
            defence_roll = defence_roll * (GearService.get_gear_defence_type_bonus(player_target, attack_type) + 64)
            return defence_roll
        defence_roll = target_defence_level + 9
        defence_roll = defence_roll * (target_style_defence_bonus + 64)
        return defence_roll

    @classmethod
    def calculate_hit_chance(cls, attack_roll, defence_roll):
        """Calculates the hit chance.

        Args:
            attack_roll (int): The value of the attack roll.
            defence_roll (int): The value of the defence roll.

        Returns:
            float: The value of hit chance
        """
        if attack_roll > defence_roll:
            hit_chance = 1 - ( (defence_roll + 2) / (2 * (attack_roll + 1)) )
        else:
            hit_chance = attack_roll / (2 * (defence_roll + 1))
        return hit_chance * 100
        