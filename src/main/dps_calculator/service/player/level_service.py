class LevelService:
    """A class that provides methods for levels."""

    @classmethod
    def validate_level(cls, level):
        """Validate a level. For a level to be valid it has to be higher than 1 and lower than 100.

        Args:
            level (int): The level that is going to be validated.

        Returns:
            Bool: Whether or not the level value is valid.
        """
        
        if level == None:
            return False
        if level < 1 or level > 99:
            return False
        else:
            return True

    @classmethod
    def print_levels(cls, levels: dict):
        for key, value in levels.items():
            print(f"===== {key}:{value} =====")
