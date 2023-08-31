class Range:
    army1_unit = None
    army2_unit = None
    range_between = None

    def __init__(self, a1unit, a2unit, distance):
        self.army1_unit = a1unit
        self.army2_unit = a2unit
        self.range_between = int(distance)

    def check_engage(self):
        if self.range_between <= 0:
            self.range_between = 1

    def modify_range(self, value):
        self.range_between += value
        self.check_engage()
