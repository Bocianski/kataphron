import unittest

from kataphron.weapons import ArcClaw, HeavyArcRifle, CognisFlamer, TorsionCannon


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
