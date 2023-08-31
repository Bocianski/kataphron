from kataphron.game.game import Game
from kataphron.players.players import Player
from kataphron.kataphrons import *
from kataphron.weapons import *

if __name__ == '__main__':
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

    # print(game1.pl)

    game1 = Game(player_piotr, player_szymon)
    game1.roll_of()
    game1.give_ranges([4, 5])
    print(game1.players[2])
    # game1.ask_for_ranges()
    game1.play_game()
