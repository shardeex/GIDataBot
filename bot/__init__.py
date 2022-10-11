from aiogram import Dispatcher
from aiogram.utils.i18n import I18n

from bot import handlers, middlewares


i18n = I18n(path="locales", default_locale="en", domain="messages")
dispatcher = Dispatcher()

handlers.setup(dispatcher)
middlewares.setup(dispatcher, i18n)

__all__ = ['dispatcher', 'i18n']
__version__ = "1.0-3.1"