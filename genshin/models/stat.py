from __future__ import annotations

import json
from importlib import resources

from ..i18n import I18n


LEVEL_CURVES = {
    4: [0, 1, 1.083, 1.165, 1.248, 1.33, 1.413, 1.495, 1.578, 1.661, 1.743, 1.826, 1.908, 1.991, 2.073, 2.156, 2.239, 2.321, 2.404, 2.486, 2.569, 2.651, 2.734, 2.817, 2.899, 2.982, 3.064, 3.147, 3.229, 3.312, 3.394, 3.477, 3.56, 3.642, 3.725, 3.807, 3.89, 3.972, 4.055, 4.138, 4.22, 4.303, 4.385, 4.468, 4.55, 4.633, 4.716, 4.798, 4.881, 4.963, 5.046, 5.128, 5.211, 5.294, 5.376, 5.459, 5.541, 5.624, 5.706, 5.789, 5.872, 5.954, 6.037, 6.119, 6.202, 6.284, 6.367, 6.45, 6.532, 6.615, 6.697, 6.78, 6.862, 6.945, 7.028, 7.11, 7.193, 7.275, 7.358, 7.44, 7.523, 7.606, 7.688, 7.771, 7.853, 7.936, 8.018, 8.101, 8.183, 8.266, 8.349, 8.431, 8.514, 8.596, 8.679, 8.761, 8.844, 8.927, 9.009, 9.092, 9.174],
    5: [0, 1, 1.083, 1.166, 1.25, 1.333, 1.417, 1.5, 1.584, 1.668, 1.751, 1.835, 1.919, 2.003, 2.088, 2.172, 2.256, 2.341, 2.425, 2.51, 2.594, 2.679, 2.764, 2.849, 2.934, 3.019, 3.105, 3.19, 3.275, 3.361, 3.446, 3.532, 3.618, 3.704, 3.789, 3.875, 3.962, 4.048, 4.134, 4.22, 4.307, 4.393, 4.48, 4.567, 4.653, 4.74, 4.827, 4.914, 5.001, 5.089, 5.176, 5.263, 5.351, 5.438, 5.526, 5.614, 5.702, 5.79, 5.878, 5.966, 6.054, 6.142, 6.23, 6.319, 6.407, 6.496, 6.585, 6.673, 6.762, 6.851, 6.94, 7.029, 7.119, 7.208, 7.297, 7.387, 7.476, 7.566, 7.656, 7.746, 7.836, 7.926, 8.016, 8.106, 8.196, 8.286, 8.377, 8.467, 8.558, 8.649, 8.739, 8.83, 8.921, 9.012, 9.103, 9.195, 9.286, 9.377, 9.469, 9.56, 9.652]
}

class Stats:
    def __init__(self, data: dict) -> None:
        self.base = BaseStats(data["base"])
        self.curve = data["curve"]

        self.max = MaxStats(data)  # TODO: replace with all levels
        # self.ascensions = ...

class BaseStats:
    def __init__(self, data: dict) -> None:
        self.hp = Stat("base_hp", data["hp"])
        self.attack = Stat("base_attack", data["attack"])
        self.defense = Stat("base_defense", data["defense"])

class MaxStats:
    def __init__(self, data: dict) -> None:
        self.hp = Stat(
            "base_hp",
            data["base"]["hp"]*LEVEL_CURVES[data["curve"]][90] + \
                data["ascensions"][-1]["add_props"]["base_hp"]
            )
        self.attack = Stat(
            "base_attack",
            data["base"]["attack"]*LEVEL_CURVES[data["curve"]][90] + \
                data["ascensions"][-1]["add_props"]["base_attack"]
            )
        self.defense = Stat(
            "base_defense",
            data["base"]["defense"]*LEVEL_CURVES[data["curve"]][90] + \
                data["ascensions"][-1]["add_props"]["base_defense"]
            )
        self.secondary = Stat(
            *list(data["ascensions"][-1]["add_props"].items())[-1],
            )

class Stat:
    def __init__(self, identifier: str, value: int) -> None:
        self.type = stat_types.get(identifier)
        self.value = value

class StatType:
    def __init__(self, identifier: str, data: dict) -> None:
        self.identifier = identifier
        self.name = I18n(data["name"])

    def __str__(self) -> str:
        return self.identifier


stat_types: dict[str, StatType] = {}
with resources.open_text("genshin.assets", "stat_types.json") as file:
    for identifier, data in json.load(file).items():
        stat_types[identifier] = StatType(identifier, data)

__all__ = [
    "Stat",
    "Stats",
    "BaseStats",
    "MaxStats",
    "StatType",
    "stat_types"
]
    