import unittest
from kataphron.game.game import *
from kataphron.players.players import *
from kataphron.kataphrons.kataphrons import *
from kataphron.weapons import *


class GameTests(unittest.TestCase):
    def test_ok(self):
        player1 = Player("test")
        player2 = Player("testing")
        game = Game(player1, player2)
        print(player1)
        length = len(game.players)
        print(game.players)
        self.assertEqual(length, 2)

    def test_add_no_interface_ranges(self):
        distance = 90
        breacher = Breacher(HeavyArcRifle(), ArcClaw())
        p1 = Player('1')
        p1.add_to_army(breacher)
        p2 = Player('2')
        p2.add_to_army(Destroyer(PlasmaCulverin(), CognisFlamer()))
        game = Game(p1, p2)
        # ---
        len_start = len(game.ranges)
        # ---
        game.roll_of()
        game.give_ranges([distance])

        self.assertNotEqual(len_start, len(game.ranges))

    def test_movement(self):
        distance = [40, 33]
        p1 = Player('p1')
        breacher = Breacher(HeavyArcRifle(), ArcClaw())
        p1.add_to_army(breacher)
        p1.add_to_army(Breacher(HeavyGravCanon(), ArcClaw()))
        p2 = Player('p2')
        destroyer = Destroyer(PlasmaCulverin(), CognisFlamer())
        p2.add_to_army(destroyer)
        game = Game(p1, p2)

        game.roll_of()
        game.give_ranges(distance)
        game.ranges[0].modify_range(breacher.stats.get('M'))

        self.assertNotEqual(distance, game.ranges)

    def test_move_to_engagement(self):
        distance = [4, 30]
        ranges = []
        modify = [-4, 6]
        p1 = Player('p1')
        breacher = Breacher(HeavyArcRifle(), ArcClaw())
        p1.add_to_army(breacher)
        p1.add_to_army(Breacher(HeavyGravCanon(), ArcClaw()))
        p2 = Player('p2')
        destroyer = Destroyer(PlasmaCulverin(), CognisFlamer())
        p2.add_to_army(destroyer)
        game = Game(p1, p2)

        game.roll_of()
        game.give_ranges(distance)
        for x in range(len(game.ranges)):
            game.ranges[x].modify_range(modify[x])
        for object in game.ranges:
            ranges.append(object.range_between)

        self.assertFalse(0 in ranges)
