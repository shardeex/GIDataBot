from __future__ import annotations

import json
from importlib import resources

from ..i18n import I18n


class Element:
    def __init__(self, identifier: str, data: dict) -> None:
        self.identifier = identifier
        self.name = I18n(data["name"])

    def __str__(self) -> str:
        return self.identifier


elements: dict[str, Element] = {}
with resources.open_text("genshin.assets", "elements.json") as file:
    for identifier, data in json.load(file).items():
        elements[identifier] = Element(identifier, data)

__all__ = [
    "Element",
    "elements"
]
    