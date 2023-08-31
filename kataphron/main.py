from kataphron.game.game import Game
from kataphron.players.players import Player
from kataphron.kataphrons import *
from kataphron.weapons import *

if __name__ == '__main__':
    # ranged_weapon_list = list([CognisFlamer, HeavyGravCanon, PlasmaCulverin, PlasmaCulverinSupercharged, PhosphorBlaster, HeavyArcRifle, TorsionCannon])
    # melee_weapon_list = list([ArcClaw, HydraulicClaw])
    # Destroyer(ranged_weapon_list[0], ranged_weapon_list[3])
    # Breacher(ranged_weapon_list[1], melee_weapon_list[0]).__str__()
    #
    # bron = TorsionCannon()
    # print(bron.__str__())
    # print(bron.range)
    #
    # print(CognisFlamer().type + '  |  ' + ArcClaw().type)
    #
    # print(dice_roll(4))
    #
    # unit11 = Destroyer(CognisFlamer(), HeavyGravCanon())
    # unit21 = Destroyer(PlasmaCulverinSupercharged(), PhosphorBlaster())
    # force1 = Player('Szymon')
    # force1.add_to_army(unit11)
    # force2 = Player("Piort")
    # force2.add_to_army(unit21)
    #
    # game = Game(force1, force2, Range(unit11, unit21, 30))
    #
    # data = {7058, 7059, 7072, 7074, 7076}
    # print(data)
    #
    # # retrieve 1 st element
    # print("0th index: ", list(data)[0])
    # print("0th index: ", list(data)[1])
    # print("0th index: ", list(data)[2])
    # print("0th index: ", list(data)[3])
    # print("0th index: ", list(data)[4])

    destroyer = Destroyer(PlasmaCulverin(), CognisFlamer())

    player_szymon = Player("Szymon")
    player_szymon.add_to_army(destroyer)
    player_piotr = Player('Piotr')
    player_piotr.add_to_army(Breacher(HeavyGravCanon(), ArcClaw()))
    player_piotr.add_to_army(Breacher(TorsionCannon(), HydraulicClaw()))

    game1 = Game(player_piotr, player_szymon)
    game1.rollof()
    game1.ask_for_ranges()
    game1.play_game()
