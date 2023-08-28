from kataphron.weapons import Weapon, MeleeWeapon, RangeWeapon


class Servitor:
    def __init__(self, robot_type: str):
        ...


class Kataphron(Servitor):
    default_stats = {"M": 6, "WS": 4, "BS": 4, "S": 5,  # * FIXED: This not being default was not working properly, copy KataphronTests.test_ok to your old code to see why
                     "T": 5, "W": 3, "A": 3, "Ld": 7, }
    stats = {}
    weapon = []  # FIXME: is it list or a set?

    def __init__(self, exact_type: str):
        self.stats = {**self.default_stats}
        super(Kataphron, self).__init__('Kataphron ' + exact_type)


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
