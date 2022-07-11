from enum import Enum

class StandartSpells(Enum):
    """Class that represents the standart spells. The attributes are the spell name and its value is the max hit."""

    WIND_STRIKE = 2
    WATER_STRIKE = 4
    EARTH_STRIKE = 6
    FIRE_STRIKE = 8
    WIND_BOLT = 9
    WATER_BOLT = 10
    EARTH_BOLT = 11
    FIRE_BOLT = 12
    WIND_BLAST = 13
    WATER_BLAST = 14
    CRUMBLE_UNDEAD = 15
    EARTH_BLAST = 15
    FIRE_BLAST = 16
    WIND_WAVE = 17
    WATER_WAVE = 18
    EARTH_WAVE = 19
    SARADOMIN_STRIKE = 20
    CLAWS_OF_GUTHIX	= 20
    FLAMES_OF_ZAMORAK = 20
    FIRE_WAVE = 20
    WIND_SURGE = 21
    WATER_SURGE = 22
    EARTH_SURGE = 23
    FIRE_SURGE = 24
    IBAN_BLAST = 25

class AncientMagicks(Enum):
    SMOKE_RUSH = 13
    SHADOW_RUSH = 14
    BLOOD_RUSH = 15
    ICE_RUSH = 16
    SMOKE_BURST = 17
    SHADOW_BURST = 18
    BLOOD_BURST = 21
    ICE_BURST = 22
    SMOKE_BLITZ = 23
    SHADOW_BLITZ = 24
    BLOOD_BLITZ = 25
    ICE_BLITZ = 26
    SMOKE_BARRAGE = 27
    SHADOW_BARRAGE = 28
    BLOOD_BARRAGE = 29
    ICE_BARRAGE = 30

class Magic:
    def __init__(self,):
        self.active_spell = None
    
    def set_active_spell(self, spell):
        self.active_spell = spell
        
