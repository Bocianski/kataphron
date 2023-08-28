from kataphron.weapons.base import RangeWeapon, Ability

__all__ = ["CognisFlamer",
           "HeavyGravCanon",
           "PlasmaCulverin",
           "PlasmaCulverinSupercharged",
           "PhosphorBlaster",
           "HeavyArcRifle",
           "TorsionCannon",
           ]


class CognisFlamer(RangeWeapon):
    def __init__(self):
        super().__init__([Ability(
            "No name", "Each time an attack is made with this weapon, that attack automatically hits the target.")])
        # FIXME: keep one super() convention, either super() or super(classname, self)
        self.name = "Cognis Flamer"
        self.range = 12
        self.type = "Assault D6 + 2"
        self.S = 4
        self.AP = 0
        self.D = 1


class HeavyGravCanon(RangeWeapon):
    def __init__(self):
        super().__init__(
            Ability("No name", "Each time an attack made with this weapon is allocated to a model"
                    "with a Save characteristic of 3+ or better, that attack has a Damage characteristic of 2."))  # FIXME
        self.name = "Heavy grav-cannon"
        self.range = 30
        self.type = "Heavy 5"
        self.S = 5
        self.AP = -3
        self.D = 1


class PlasmaCulverin(RangeWeapon):
    def __init__(self):
        super().__init__(Ability("Blast"))
        self.name = "Kataphron plasma culverin - Standard"
        self.range = 36
        self.type = "Heavy D6"
        self.S = 7
        self.AP = -3
        self.D = 1


class PlasmaCulverinSupercharged(RangeWeapon):
    def __init__(self):
        super().__init__(
            Ability("Blast", "Each time an unmodified hit roll of 1 is made for an attack with this weapon profile, the bearer's"
                    "unit suffers 1 mortal wound after shooting with this weapon."))
        self.name = "Kataphron plasma culverin - Supercharge"
        self.range = 36
        self.type = "Heavy D6"
        self.S = 8
        self.AP = -3
        self.D = 2


class PhosphorBlaster(RangeWeapon):
    def __init__(self):
        super().__init__(Ability("No Dense Cover"))
        self.name = "Phosphor blaster"
        self.range = 24
        self.type = "Rapid Fire 1"
        self.S = 5
        self.AP = -1
        self.D = 1


class HeavyArcRifle(RangeWeapon):
    def __init__(self):
        super().__init__(
            Ability("No name", "Each time an attack is made with this weapon against a VEHICLE unit, that attack has"
                    "a Damage characteristic of 3 and an unmodified wound roll of 4+ successfully wounds the target."))
        self.name = "Heavy arc rifle"
        self.range = 36
        self.type = "Heavy 2"
        self.S = 6
        self.AP = -2
        self.D = 2


class TorsionCannon(RangeWeapon):
    def __init__(self):
        super().__init__([])
        self.name = "Torsion cannon"
        self.range = 48
        self.type = "Heavy 1"
        self.S = 8
        self.AP = -4
        self.D = "D3+3"
