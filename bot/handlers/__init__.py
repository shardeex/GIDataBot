from aiogram import Dispatcher

from bot.handlers import base, settings, inline, menu, character


def setup(dispatcher: Dispatcher) -> None:
    base.setup(dispatcher)
    settings.setup(dispatcher)
    inline.setup(dispatcher)
    menu.setup(dispatcher) 
    character.setup(dispatcher)
