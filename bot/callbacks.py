# should be rewritten or even deleted fr
from aiogram.filters.callback_data import CallbackData


class Menu(CallbackData, prefix="menu"):
    menu: str  # only characters for now
    character: int = 1  # optional: character index

class Character(CallbackData, prefix="character"):
    identifier: str  # character identifier
    menu: str  # callable menu
    talent: int = 1  # optional: selected talent index
    constellation: int = 1  # optional: selected const index
    story: int = 1  # optional: selected story index
    quote: int = 1  # optional: selected quote index

class Settings(CallbackData, prefix="settings"):
    menu: str
    language: str = "en"
    # gender not needed because it can switch only to other