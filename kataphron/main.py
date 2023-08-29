from kataphron.game import Range, Game
from kataphron.info import Destroyer, Breacher
from kataphron.player import Player
from weapons import CognisFlamer, HeavyGravCanon, PlasmaCulverin, PlasmaCulverinSupercharged, PhosphorBlaster, HeavyArcRifle, TorsionCannon, ArcClaw, HydraulicClaw
from combat import dice_roll

if __name__ == '__main__':
    ranged_weapon_list = list([CognisFlamer, HeavyGravCanon, PlasmaCulverin, PlasmaCulverinSupercharged, PhosphorBlaster, HeavyArcRifle, TorsionCannon])
    melee_weapon_list = list([ArcClaw, HydraulicClaw])
    Destroyer(ranged_weapon_list[0], ranged_weapon_list[3])
    Breacher(ranged_weapon_list[1], melee_weapon_list[0]).__str__()

    bron = TorsionCannon()
    print(bron.__str__())
    print(bron.range)

    print(CognisFlamer().type + '  |  ' + ArcClaw().type)

    print(dice_roll(4))

    unit11 = Destroyer(CognisFlamer(), HeavyGravCanon())
    unit21 = Destroyer(PlasmaCulverinSupercharged(), PhosphorBlaster())
    force1 = Player('Szymon')
    force1.add_to_army(unit11)
    force2 = Player("Piort")
    force2.add_to_army(unit21)

    game = Game(force1, force2, Range(unit11, unit21, 30))
