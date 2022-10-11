from aiogram import Dispatcher

from bot.handlers.character import callback, inline

def setup(dispatcher: Dispatcher) -> None:
    callback.setup(dispatcher)
