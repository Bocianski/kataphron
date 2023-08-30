
__all__ = ["Servitor", "Kataphron"]


class Servitor:
    def __init__(self, robot_type: str):
        ...


class Kataphron(Servitor):
    default_stats = {"M": 6, "WS": 4, "BS": 4, "S": 5,  # * FIXED: This not being default was not working properly, copy KataphronTests.test_ok to your old code to see why
                     "T": 5, "W": 3, "A": 3, "Ld": 7, }
    stats = {}
    weapon = []  # FIXME: is it list or a set?
    weapon_shot = []

    def __init__(self, exact_type: str):
        self.stats = {**self.default_stats}
        super(Kataphron, self).__init__('Kataphron ' + exact_type)
