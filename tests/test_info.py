import unittest

from kataphron.info import Destroyer, Breacher
from kataphron.weapons import ArcClaw, HeavyArcRifle, PlasmaCulverin, CognisFlamer, Weapon, TorsionCannon


class WeaponTests(unittest.TestCase):
    def test_constructor(self):
        self.assertTrue(Weapon is not None)

    def test_different_types(self):
        self.assertFalse(CognisFlamer().type == ArcClaw().type)

    def test_special_rules(self):
        self.assertTrue(TorsionCannon.abilities == "")


class KataphronTests(unittest.TestCase):
    def test_kataphton_constructor(self):
        self.assertTrue(Breacher(HeavyArcRifle, ArcClaw) is not None)


class DestroyerTests(unittest.TestCase):
    def test_destroyer_constructor(self):
        self.assertTrue(Destroyer(PlasmaCulverin, CognisFlamer) is not None)

    def test_destroyer_stats_size(self):
        self.assertTrue(len(Destroyer(PlasmaCulverin, CognisFlamer).stats) == 9)

    def test_destroyer_one_stat(self):
        self.assertEqual(Destroyer(PlasmaCulverin, CognisFlamer).stats.get(self, "W"), Breacher(HeavyArcRifle, ArcClaw).stats.get(self, "W"))
