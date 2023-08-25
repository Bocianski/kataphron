class Servitor:
    def __init__(self, robot_type):
        print('Servitor type: ', robot_type)


class Kataphron(Servitor):
    stats = {['M', 6], ['WS', 4], ['BS', 4], ['S', 5], ['T', 5], ['W', 3], ['A', 3], ['Ld', 7], ['Sv', None]}

    # def keywords():
    #     list
    def __init__(self, exact_type):
        super().__init__('Kataphron ' + exact_type)


class Destroyer(Kataphron):
    def __init__(self):
        super().__init__('Destroyer')

    # Name, Range, Type, S, AP, D
    ranged_weapons = dict(Name=["Cognis flamer", "Heavy grav-cannon", "Kataphron plasma culverin - Standard",
                                "Kataphron plasma culverin - Supercharge", "Phosphor blaster"],
                          Range=[12, 30, 36, 36, 24],
                          Type=["Assault D6+2", "Heavy 5", "Heavy D6", "Heavy D6", "Rapid Fire 1"],
                          S=[4, 5, 7, 8, 5],
                          AP=[0, -3, -3, -3, -1],
                          D=[1, 1, 1, 2, 1])
