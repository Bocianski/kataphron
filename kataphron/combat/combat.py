"""
2 models stand next to themselves and take turns making all through all battle phases. Distance between them will be set in constructor. First turn takes who wins roll-of
"""

import random


class Battlefield:
    pass


class Round:
    # phases:    1 - command    2 - movement     3 - shooting    4 - charge  5 - fight   6 - morale
    phase_counter = 1
    initiative = None


def dice_roll(number_of_dices):
    results = []
    for i in range(number_of_dices):
        results.append(random.randint(1, 6))
    return results
