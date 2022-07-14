from tkinter.filedialog import Open
from model.player.player_model import Player
from model.player.level_model import Skills
from model.items.equipment_model import Slots
from model.combat.style_model import AttackStyle, AttackType
from service.player.gear_service import GearService
from service.player.level_service import LevelService
from service.items.equipment_service import BonusesService, EquipmentService
from service.combat.melee_service import MeleeCalculator
from service.requests.requests_service import RequestsService

def melee_demo():
    # Creating player 
    player = Player()

    # Set player levels
    player.levels.set_level(Skills.STRENGTH, 83)
    player.levels.set_level(Skills.ATTACK, 78)
    player.levels.set_level(Skills.DEFENCE, 77)

    # Set player attack style
    player.style = AttackStyle.ACCURATE

    # Creating equipment and equip 
    new_item = EquipmentService.create_equipment(
        Slots.WEAPON_SLOT,
        BonusesService.create_bonuses(0, 82, 0, 0, 0),
        BonusesService.create_bonuses(0, 0, 0, 0, 0),
        BonusesService.create_other_bonuses(82, 0, 0, 0),
        "Abyssal Whip"
    )
    GearService.equip_item(player, new_item)

    # Calculating max hit
    max_hit = MeleeCalculator.calculate_max_hit(player)
    print(f"Maxhit = {str(max_hit)}")

    # Calculating attack roll
    attack_roll = MeleeCalculator.calculate_attack_roll(player, AttackType.SLASH)
    print(f"Attack roll = {str(attack_roll)}")

    # Calculating defence roll
    defence_roll = MeleeCalculator.calculate_defence_roll(
        AttackType.SLASH, 
        target_defence_level = 1, 
        target_style_defence_bonus = 0
        )
    print(f"Defence roll = {str(defence_roll)}")

    # Calculating hit chance
    hit_chance = MeleeCalculator.calculate_hit_chance(attack_roll, defence_roll)
    print(f"Hit chance = {str(hit_chance)}")

def requests_demo():
    player = Player()
    player.set_levels(RequestsService.fetch_player_levels())
    LevelService.print_levels(player.levels.get_levels())
