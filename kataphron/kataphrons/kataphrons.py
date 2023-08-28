from kataphron.kataphrons import Kataphron
from kataphron.weapons.base import Weapon, MeleeWeapon, RangeWeapon

__all__ = ["Destroyer", "Breacher"]


class Destroyer(Kataphron):
    def __init__(self, weapon1: Weapon, weapon2: Weapon):
        super(Destroyer, self).__init__('Destroyer')
        # FIXME: keep one super() convention, either super() or super(classname, self)
        self.stats["Sv"] = 3
        self.weapon = [weapon1, weapon2]  # FIXME: is it list or a set?


class Breacher(Kataphron):
    def __init__(self, ranged: RangeWeapon, melee: MeleeWeapon):
        super(Breacher, self).__init__('Breacher')
        self.stats["Sv"] = 2
        self.weapon = {ranged, melee}  # FIXME: is it list or a set?
