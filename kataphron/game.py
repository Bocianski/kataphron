from kataphron.combat import dice_roll

class Range:
    army1_unit = None
    army2_unit = None
    range_between = None

    def __init__(self, a1unit, a2unit, range):
        self.army1_unit = a1unit
        self.army2_unit = a2unit
        self.range_between = range

class Game:
    players_in_order = []
    players = []
    ranges = []

    def __init__(self, player1, player2, range):
        self.players.append(player1)
        self.players.append(player2)
        self.ranges.append(range)
    def rollof(self, army1, army2):
        if army1.initiative_roll > army2.initiative_roll:
            self.players_in_order.append(army1)
            self.players_in_order.append(army2)
        elif army1.initiative_roll == army2.initiative_roll:
            army1.initiative_roll = dice_roll(1)
            army2.initiative_roll = dice_roll(1)
            self.rollof(army1, army2)
        else:
            self.players_in_order.append(army2)
            self.players_in_order.append(army1)

    def command_phase(self):
        pass

    def movement_phase(self):
        for
        pass

    def shooting_phase(self):
        pass

    def charge_phase(self):
        pass

    def fight_phase(self):
        pass

    def morale_phase(self):
        pass
