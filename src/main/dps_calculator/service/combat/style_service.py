from model.combat.style_model import AttackStyle

class AttackStyleService:
    """A class that provides methods for the Style."""

    @classmethod
    def get_style_attack_bonus(cls, attack_style: AttackStyle):
        """Get the attack bonus given by the attack style.

        Args:
            attack_style (AttackStyle): the attack style.

        Returns:
            int: The value of the attack bonus.
        """

        if attack_style == AttackStyle.ACCURATE:
            return 3
        if attack_style == AttackStyle.CONTROLLED:
            return 1
        
        return 0

    @classmethod
    def get_style_strength_bonus(cls, attack_style: AttackStyle):
        """Get the strength bonus given by the attack style.

        Args:
            attack_style (AttackStyle): the attack style.

        Returns:
            int: The value of the strength bonus.
        """

        if attack_style == AttackStyle.AGGRESSIVE:
            return 3
        if attack_style == AttackStyle.CONTROLLED:
            return 1
    
        return 0