from kataphron.combat.combat import dice_roll
from kataphron.game.range import Range


class Game:
    players_in_order = []
    players = []
    ranges = []
    round = 0
    turn = 0
    units_ready = []
    units_activated = []

    def __init__(self, player1, player2):
        self.players.append(player1)
        self.players.append(player2)

    def ask_for_ranges(self):
        for Army1Unit in self.players_in_order[0].army_list:
            for Army2Unit in self.players_in_order[1].army_list:
                self.ranges.append(
                    Range(Army1Unit, Army2Unit, input(f"Odleglosc miedzy {Army1Unit} and {Army2Unit}: ")))

    def rollof(self):
        army1 = self.players[0]
        army2 = self.players[1]
        if army1.initiative_roll > army2.initiative_roll:
            self.players_in_order.append(army1)
            self.players_in_order.append(army2)
        elif army1.initiative_roll == army2.initiative_roll:
            army1.initiative_roll = dice_roll(1)
            army2.initiative_roll = dice_roll(1)
            self.rollof()
        else:
            self.players_in_order.append(army2)
            self.players_in_order.append(army1)

    def command_phase(self, active_player):
        self.movement_phase(active_player)

    def movement_phase(self, active_player):
        active_unit = self.get_active_unit(active_player)
        if active_unit is None:
            input('Brak jednostek do poruszenia. Nacisnij ENTER by kontynuowac do Shooting phase')
            self.activate_units()
            self.shooting_phase(active_player)
        self.movement_phase_with_unit(active_player, active_unit)

    def movement_phase_with_unit(self, active_player, active_unit):
        choice = int(input(
            "\nCo chcesz zrobic?\n1 - oddalic sie od przeciwnika.\n2 - zblizyc sie do przeciwnika.\n3 - stac w miejscu\n"))
        if choice == 1:
            for movement in self.ranges:
                if active_unit == movement.army1_unit or active_unit == movement.army2_unit:
                    movement.range_between += active_unit.stats.get("M")
        elif choice == 2:
            for movement in self.ranges:
                if active_unit == movement.army1_unit or active_unit == movement.army2_unit:
                    movement.range_between -= active_unit.stats.get("M")
        elif choice == 3:
            print('Wybrales pozostac nieruchomym')
        else:
            print('Chyba cos zle nacinales ;)\n')
            self.movement_phase_with_unit(active_player, active_unit)
        self.units_activated.append(self.units_ready.pop(self.units_ready.index(active_unit)))
        self.movement_phase(active_player)

    def shooting_phase(self, active_player):
        active_unit = self.get_active_unit(active_player)
        if active_unit is None:
            input('Brak jednostek do oddania srzalu. Nacisnij ENTER by kontynuowac do Charge phase')
            self.charge_phase_with_unit(active_player, active_unit)
        # choice = int(input()
        print("Mozliwe cele:\n")

        print("\nW jaki cel chcesz oddac strzal?\n")

    def charge_phase(self, active_player):
        active_unit = self.get_active_unit(active_player)
        if active_unit is None:
            input('Wybrano czynnosc dla kazdej jednostki. Nacisnij ENTER by kontynuowac do Fight phase')
            self.activate_units()
            self.fight_phase(active_player)
        self.charge_phase_with_unit(active_player, active_unit)

    def charge_phase_with_unit(self, active_player, active_unit):
        target_list = []
        range_list = []
        tmp = 1
        while True:
            choice = int(input("Co chcesz zrobic?\n1 - zaszarzowac\n2 - stac w miejscu"))
            if choice == 2:
                self.units_activated.append(self.units_ready.pop(self.units_ready.index(active_unit)))
                self.charge_phase(active_player)
            elif choice == 1:
                for possible_targets in self.ranges:
                    if possible_targets.army1_unit == active_unit and possible_targets.range_between <= 12:
                        print(f"{tmp}. {possible_targets.army2_unit} jest w  {possible_targets.range_between}")
                        target_list.append(possible_targets.army2_unit)
                    elif possible_targets.army2_unit == active_unit and possible_targets.possible_targets_between <= 12:
                        print(
                            f"{tmp}. {possible_targets.army1_unit} jest w  {possible_targets.possible_targets_between}")
                        target_list.append(possible_targets.army1_unit)
                    range_list.append(possible_targets)
                    tmp += 1
                choice = input("Do kogo szarrzujesz?")
                target = range_list[int(choice) - 1]
                roll = dice_roll(2)
                if target.range_between <= roll:
                    print("Szarza sie udala")
                    target.range_between = 0
                else:
                    print("Szarza sie nie udala")
                self.units_activated.append(self.units_ready.pop(self.units_ready.index(active_unit)))
                self.charge_phase(active_player)
            else:
                print("Chyba cos zle wybrales ;)")

    def fight_phase(self, active_player):
        pass

    def morale_phase(self):
        pass

    def get_active_unit(self, active_player):
        print('Jednostki mozliwe do wyboru:\n')
        counter_of_possible_units = 0
        for unit in active_player.army_list:
            if unit in self.units_activated:
                continue
            else:
                counter_of_possible_units += 1
                print(unit.__str__)
        if counter_of_possible_units == 0:
            print('Brak jednostek do uzycia')
            return None
        else:
            n = int(input('Wybierz jednostke ktora ma podjac teraz dzialanie:\n')) - 1
            return active_player.army_list[n]

    def activate_units(self):
        while len(self.units_activated) != 0:
            self.units_ready.append(self.units_activated.pop())

    def fill_ready_units(self):
        for i in range(len(self.players)):
            for unit in self.players[i].army_list:
                self.units_ready.append(unit)

    def play_game(self):
        self.fill_ready_units()
        while self.round < 5:
            n = self.turn % 2
            active_player = self.players_in_order[n]
            print(f'\nZaczynamy runde {self.round + 1}\nTura gracza: {active_player.player_name}')
            self.command_phase(active_player)
            self.round += 1
            self.turn += 1
