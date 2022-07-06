from model.items.equipment_model import Bonuses, OtherBonuses, Slots
from service.items.equipment_service import EquipmentService


class Gear:
    """A class to represent a player gear.
    
    Attributes:
        equipments (dict): The equipments that compose the gear. 
        The keys are (Slots.name) and the values are (Equipment).
        total_gear_bonuses (dict): The value of the total bonuses given by all equipment bonuses added.
        The keys are "total_attack_bonuses", "total_defence_bonuses" and "total_other_bonuses".
    """

    def __init__(self,):
        self.equipments = dict()
        for slot in Slots:
            self.equipments[slot.name] = EquipmentService.create_empty_equipment(slot)
    
        self.total_gear_bonuses = dict({
            "total_attack_bonuses": Bonuses(),
            "total_defence_bonuses": Bonuses(),
            "total_other_bonuses": OtherBonuses()
        })