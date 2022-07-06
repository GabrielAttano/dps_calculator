from model.player.prayer_model import Prayer, PrayerBonuses

class PrayerService:
    """A class that provides methods to Prayer."""
    
    @classmethod
    def get_prayer_bonus(cls, prayers: Prayer):
        """Get the prayer bonus provided by the active prayers

        Args:
            prayers (Prayer): A Prayer class containing a list of active prayers.

        Returns:
            float: Returns a float that represents the multiplier.
            1: If no multipliers are on.
        """

        total_prayer_bonus = float()
        for prayer in prayers.active_prayer_bonuses:
            total_prayer_bonus += prayer.value
        if total_prayer_bonus == 0:
            return 1
        return total_prayer_bonus


