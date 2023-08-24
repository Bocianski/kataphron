import unittest
from kataphron.info import Kataphron

class KataphronTests(unittest.TestCase):
    def test_constructor(self):
        robot = Kataphron()
        self.assertTrue(robot is not None)