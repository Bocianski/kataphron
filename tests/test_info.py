import unittest

from kataphron.info import Destroyer, Breacher
from kataphron.weapons import ArcClaw, HeavyArcRifle, PlasmaCulverin, CognisFlamer


class KataphronTests(unittest.TestCase):
    def test_constructor(self):
        self.assertTrue(Breacher(HeavyArcRifle, ArcClaw) is not None)


class DestroyerTests(unittest.TestCase):
    def test_destroyer_constuctor(self):
        self.assertTrue(Destroyer(PlasmaCulverin, CognisFlamer) is not None)

    def test_destroyer_stats_size(self):
        self.assertTrue(len(Destroyer(PlasmaCulverin, CognisFlamer).stats) == 9)

    def test_destroyer_one_stat(self):
        Destroyer
