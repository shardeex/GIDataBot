from aiogram import Dispatcher
from aiogram.utils.i18n import I18n

from bot.middlewares import i18n


def setup(dp: Dispatcher, i18n_aiogram: I18n):
    i18n.setup(dp, i18n_aiogram)
