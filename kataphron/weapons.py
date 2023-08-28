import abc
from dataclasses import dataclass
from typing import Sequence


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
    def use(self, with_ability: Ability|None = None) -> None:
        raise NotImplementedError()


class RangeWeapon(Weapon):

    def __init__(self, abilities: Sequence[Ability] | Ability):
        if isinstance(abilities, Ability):
            abilities = [abilities]
        self.abilities = abilities

    def use(self, with_ability: Ability|None = None): # * I wouldn't say this is perfectly valid way to do that, that's just an example
        if with_ability is None:
            return
        if with_ability not in self.abilities:
            raise AttributeError("Invalid Ability.")
        with_ability.times_used += 1


class CognisFlamer(RangeWeapon):
    def __init__(self):
        super().__init__([Ability(
            "No name", "Each time an attack is made with this weapon, that attack automatically hits the target.")])
        # FIXME: keep one super() convention, either super() or super(classname, self)
        self.name = "Cognis Flamer"
        self.range = 12
        self.type = "Assault D6 + 2"
        self.S = 4
        self.AP = 0
        self.D = 1


class HeavyGravCanon(RangeWeapon):
    def __init__(self):
        super().__init__(
            Ability("No name", "Each time an attack made with this weapon is allocated to a model"
                    "with a Save characteristic of 3+ or better, that attack has a Damage characteristic of 2."))  # FIXME
        self.name = "Heavy grav-cannon"
        self.range = 30
        self.type = "Heavy 5"
        self.S = 5
        self.AP = -3
        self.D = 1


class PlasmaCulverin(RangeWeapon):
    def __init__(self):
        super().__init__(Ability("Blast"))
        self.name = "Kataphron plasma culverin - Standard"
        self.range = 36
        self.type = "Heavy D6"
        self.S = 7
        self.AP = -3
        self.D = 1


class PlasmaCulverinSupercharged(RangeWeapon):
    def __init__(self):
        super().__init__(
            Ability("Blast", "Each time an unmodified hit roll of 1 is made for an attack with this weapon profile, the bearer's"
                    "unit suffers 1 mortal wound after shooting with this weapon."))
        self.name = "Kataphron plasma culverin - Supercharge"
        self.range = 36
        self.type = "Heavy D6"
        self.S = 8
        self.AP = -3
        self.D = 2


class PhosphorBlaster(RangeWeapon):
    def __init__(self):
        super().__init__(Ability("No Dense Cover"))
        self.name = "Phosphor blaster"
        self.range = 24
        self.type = "Rapid Fire 1"
        self.S = 5
        self.AP = -1
        self.D = 1


class HeavyArcRifle(RangeWeapon):
    def __init__(self):
        super().__init__(
            Ability("No name", "Each time an attack is made with this weapon against a VEHICLE unit, that attack has"
                    "a Damage characteristic of 3 and an unmodified wound roll of 4+ successfully wounds the target."))
        self.name = "Heavy arc rifle"
        self.range = 36
        self.type = "Heavy 2"
        self.S = 6
        self.AP = -2
        self.D = 2


class TorsionCannon(RangeWeapon):
    def __init__(self):
        super().__init__([])
        self.name = "Torsion cannon"
        self.range = 48
        self.type = "Heavy 1"
        self.S = 8
        self.AP = -4
        self.D = "D3+3"


class MeleeWeapon(Weapon):
    def __init__(self, abilities: Ability | Sequence[Ability]):
        if isinstance(abilities, Ability):
            abilities = [abilities]
        self.abilities = abilities
        self.range = 0
        self.type = "Melee"


class ArcClaw(MeleeWeapon):
    def __init__(self):
        super().__init__(
            Ability("No name", "Each time the bearer fights, it makes 1 additional attack with this weapon."
                    "Each time an attack is made with this weapon against a VEHICLE unit, that attack has a Damage"
                    "characteristic of 2 and an unmodified wound roll of 4+ successfully wounds the target."))
        self.name = "Arc claw"
        self.S = "+1"
        self.AP = -3
        self.D = 1


class HydraulicClaw(MeleeWeapon):
    def __init__(self):
        super().__init__([])
        self.name = "Hydraulic claw"
        self.S = "x2"
        self.AP = -2
        self.D = 3
