from kataphron.weapons.base import MeleeWeapon, Ability

__all__ = ["ArcClaw", "HydraulicClaw"]


class ArcClaw(MeleeWeapon):
    def __init__(self):
        super().__init__(
            Ability("No name", "Each time the bearer fights, it makes 1 additional attack with this weapon."
                    "Each time an attack is made with this weapon against a VEHICLE unit, that attack has a Damage"
                    "characteristic of 2 and an unmodified wound roll of 4+ successfully wounds the target."))
        self.name = "Arc claw"
        self.S = "+1"
        self.AP = -3
        self.D = 1


class HydraulicClaw(MeleeWeapon):
    def __init__(self):
        super().__init__([])
        self.name = "Hydraulic claw"
        self.S = "x2"
        self.AP = -2
        self.D = 3
