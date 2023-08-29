import unittest
from kataphron.kataphrons import Kataphron, Breacher, Destroyer
from kataphron.weapons.melee import *
from kataphron.weapons.ranged import *

class KataphronTests(unittest.TestCase):
    def test_ok(self):
        kataphron = Kataphron("test")

        # * without default_stats it fails
        self.assertEqual(len(kataphron.stats), 8)

    def test_breacher(self):
        ranged_weapon = HeavyArcRifle()
        melee_weapon = ArcClaw()
        bracher = Breacher(ranged_weapon, melee_weapon)

        self.assertEqual(len(bracher.stats), 9)
        self.assertCountEqual(bracher.weapon, [ranged_weapon, melee_weapon])

    def test_destroyer(self):
        weapon_1 = PlasmaCulverin()
        weapon_2 = CognisFlamer()
        destroyer = Destroyer(weapon_1, weapon_2)

        self.assertEqual(len(destroyer.stats), 9)
        self.assertCountEqual(destroyer.weapon, [weapon_1, weapon_2])

    def test_common_stats(self):
        ranged_weapon = CognisFlamer()
        melee_weapon = ArcClaw()
        breacher = Breacher(ranged_weapon, melee_weapon)
        destroyer = Destroyer(ranged_weapon, melee_weapon)

        self.assertEqual(breacher.stats["W"], destroyer.stats["W"])