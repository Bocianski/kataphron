from kataphron.kataphrons import Destroyer, Breacher
from kataphron.weapons import CognisFlamer, HeavyGravCanon, PlasmaCulverin, PlasmaCulverinSupercharged, PhosphorBlaster, HeavyArcRifle, TorsionCannon, ArcClaw, HydraulicClaw

if __name__ == '__main__':
    ranged_weapon_list = list([CognisFlamer, HeavyGravCanon, PlasmaCulverin, PlasmaCulverinSupercharged, PhosphorBlaster, HeavyArcRifle, TorsionCannon])
    melee_weapon_list = list([ArcClaw, HydraulicClaw])
    Destroyer(ranged_weapon_list[0](), ranged_weapon_list[3]())
    Breacher(ranged_weapon_list[1](), melee_weapon_list[0]()).__str__()

    weapon = TorsionCannon()
    print(weapon)
    print(weapon.range)

    print(CognisFlamer().type + '  |  ' + ArcClaw().type)
