class Servitor:
    def __init__(self, robot_type):
        print('Servitor type: ', robot_type)


class Kataphron(Servitor):
    stats = {"M": 6, "WS": 4, "BS": 4, "S": 5, "T": 5, "W": 3, "A": 3, "Ld": 7, }
    weapon = []

    def __init__(self, exact_type):
        super(Kataphron, self).__init__('Kataphron ' + exact_type)


class Destroyer(Kataphron):
    def __init__(self, weapon1, weapon2):
        # if 0
        super(Destroyer, self).__init__('Destroyer')
        self.stats["Sv"] = 3
        self.weapon = [weapon1, weapon2]
        print(weapon1, weapon2)


class Breacher(Kataphron):
    def __init__(self, ranged, melee):
        # if ranged != 5 or ranged != 6:
        #     ranged = 5
        # if melee != 0 or melee != 1:
        #     melee = 0
        super(Breacher, self).__init__('Breacher')
        self.stats["Sv"] = 2
        self.weapon = {ranged, melee}
