import unittest
from kataphron.info import Kataphron, Destroyer

class KataphronTests(unittest.TestCase):
    def test_constructor(self):
        robot = Kataphron('yes')
        self.assertTrue(robot is not None)

class DestroyerTests(unittest.TestCase):
    def test_destroyer_constuctor(self):
        self.assertTrue(Destroyer() is not None)