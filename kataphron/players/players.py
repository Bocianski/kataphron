from kataphron.combat.combat import dice_roll


class Player:
    player_name = None
    initiative_roll = None
    army_list = []

    def __init__(self, name):
        self.player_name = name
        self.initiative_roll = dice_roll(1)
        self.army_list = []

    def add_to_army(self, unit):
        self.army_list.append(unit)
