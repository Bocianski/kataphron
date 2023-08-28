import unittest

from kataphron.info import Kataphron, Destroyer, Breacher
from kataphron.weapons import ArcClaw, HeavyArcRifle, PlasmaCulverin, CognisFlamer, TorsionCannon


# FIXME: This is just an example, don't include it in the project
class ExampleTest(unittest.TestCase):
    def test_example(self):
        #! given
        string = "test"

        #! when
        stringLower = string.upper()

        #! then
        self.assertEqual(stringLower, "TEST")
        self.assertNotEqual(stringLower, string)


class WeaponTests(unittest.TestCase):
    def test_ok(self):
        weapon = CognisFlamer()

        self.assertIsNotNone(weapon.name)
        self.assertIsNotNone(weapon.type)
        self.assertIsNotNone(weapon.range)
        self.assertEqual(weapon.abilities[0].times_used, 0)

    def test_different_types(self):
        ranged_weapon = CognisFlamer()
        meelee_weapon = ArcClaw()

        self.assertFalse(ranged_weapon.type == meelee_weapon.type)

    def test_special_rules(self):
        weapon = TorsionCannon()

        self.assertCountEqual(weapon.abilities, [])

    def test_use_ability(self):
        weapon = HeavyArcRifle()
        ability = weapon.abilities[0]

        for _ in range(3):
            weapon.use(ability)

        self.assertEqual(weapon.abilities[0].times_used, 3)


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
