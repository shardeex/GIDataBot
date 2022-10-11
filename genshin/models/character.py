from __future__ import annotations

import json
from datetime import datetime
from importlib import resources

from .item import GenshinItem
from .element import elements
from .weapon import weapon_types
from .stat import *
from ..i18n import I18n


class Character(GenshinItem):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

        self.weapon_type = weapon_types.get(data["weapon_type"], None)
        self.vision = elements.get((data["vision"]), None)
        self.info = CharacterInfo(data["info"])
        self.stats = Stats(data["stats"])

        self.talents = [Talent(t) for t in data["talents"]]
        self.constellation = [Constellation(c) for c in data["constellation"]]

        self.quotes = [About(q) for q in data["about"]["quotes"]]
        self.story = [About(s) for s in data["about"]["story"]]

        self.icon_url = \
            f"gidatabot.deta.dev/api/character/icons/{self.identifier}.png"
        self.artwork_url = \
            f"gidatabot.deta.dev/api/character/artwork/{self.identifier}.png"

    def __repr__(self):
        return f"{self.name} ({self.vision}) {self.stars}"

class CharacterInfo:
    def __init__(self, data: dict) -> None:
        self.title = I18n(data["title"])
        self.birthday = CharacterBirthday(data["birthday"])
        self.constellation = I18n(data["constellation"])
        # self.nation: str
        self.affilation = I18n(data["affilation"])
        self.character_voice = I18n(data["character_voice"])

class CharacterBirthday:
    def __init__(self, data: dict) -> None:
        self.month = data["month"]
        self.day = data["day"]

    def __repr__(self) -> str:
        return f"{self.month}.{self.day}"

    @property
    def days_left(self) -> int:
        if (self.month, self.day) == (0, 0):
            return None

        birthday = datetime(2000, self.month, self.day)  # високосный
        now = datetime.now()

        try:
            this_year = datetime(now.year, birthday.month, birthday.day)
        except ValueError:  # Bennett
            this_year = datetime(now.year, birthday.month, birthday.day-1)

        try:
            next_year = datetime(now.year+1, birthday.month, birthday.day)
        except ValueError:  # Bennett
            next_year = datetime(now.year+1, birthday.month, birthday.day-1)  

        return ((this_year if this_year >= now else next_year) - now).days + 1

class Talent:
    def __init__(self, data: dict) -> None:
        self.type = talent_types.get((data["type"]), None)
        self.name = I18n(data["name"])
        self.description = I18n(data["description"])

class TalentType:
    def __init__(self, identifier: str, data: dict) -> None:
        self.identifier = identifier
        self.name = I18n(data["name"])
    
    def __str__(self) -> str:
        return self.identifier

class Constellation:
    def __init__(self, data: dict) -> None:
        self.index = data["index"]
        self.name = I18n(data["name"])
        self.description = I18n(data["description"])

class About:
    def __init__(self, data: dict) -> None:
        self.title = I18n(data["title"])
        self.text = I18n(data["text"])

        condition = I18n(data["condition"]) if data["condition"] \
            is not None else None
        self.condition = condition


talent_types: dict[str, TalentType] = {}
with resources.open_text("genshin.assets", "talent_types.json") as file:
    for identifier, data in json.load(file).items():
        talent_types[identifier] = TalentType(identifier, data)

characters: dict[str, Character] = {}
path = 'genshin.assets.characters'
for filename in [f for f in resources.contents(path) if f.endswith('.json')]:
    identifier = filename[:filename.find('.')]
    with resources.open_text(path, filename) as file:
        data = json.load(file)
    characters[identifier] = Character(data)

__all__ = [
    "Character",
    "Stats",
    "Talent",
    "TalentType",
    "Constellation",
    "About",
    "characters",
    "talent_types"
]