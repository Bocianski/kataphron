import abc
from dataclasses import dataclass
from typing import Sequence

__all__ = ["Ability", "Weapon", "RangeWeapon", "MeleeWeapon"]


@dataclass
class Ability:
    name: str
    description: str | None = None
    # * this can now do much more than a simple string
    times_used = 0


class Weapon:
    name: str
    range: int
    type: str
    S: int | str  # FIXME: this should be int or str or custom type
    AP: int
    D: int | str  # FIXME: this should be int or str or custom type
    abilities: Sequence[Ability] = []

    def __str__(self):
        return f'{self.name} | {self.range} | {self.type} | {self.S} | {self.AP} | {self.D} | {self.abilities}'

    @abc.abstractmethod
    def use(self, with_ability: Ability | None = None) -> None:
        raise NotImplementedError()


class RangeWeapon(Weapon):

    def __init__(self, abilities: Sequence[Ability] | Ability):
        if isinstance(abilities, Ability):
            abilities = [abilities]
        self.abilities = abilities

    # * I wouldn't say this is perfectly valid way to do that, that's just an example
    def use(self, with_ability: Ability | None = None):
        if with_ability is None:
            return
        if with_ability not in self.abilities:
            raise AttributeError("Invalid Ability.")
        with_ability.times_used += 1


class MeleeWeapon(Weapon):
    def __init__(self, abilities: Ability | Sequence[Ability]):
        if isinstance(abilities, Ability):
            abilities = [abilities]
        self.abilities = abilities
        self.range = 0
        self.type = "Melee"
