from __future__ import annotations

import json
from importlib import resources

from ..i18n import I18n


class WeaponType:
    def __init__(self, identifier: str, data: dict) -> None:
        self.identifier = identifier
        self.name = I18n(data["name"])

    def __str__(self) -> str:
        return self.identifier


weapon_types: dict[str, WeaponType] = {}
with resources.open_text("genshin.assets", "weapon_types.json") as file:
    for identifier, data in json.load(file).items():
        weapon_types[identifier] = WeaponType(identifier, data)

__all__ = [
    "WeaponType",
    "weapon_types"
]
    